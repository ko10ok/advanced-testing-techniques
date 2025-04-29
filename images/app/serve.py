import asyncio
import os
import sys
import logging
from datetime import datetime
import json
from os import environ

import aiohttp
import asyncpg
from aiohttp import web

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

@web.middleware
async def logging_middleware(request, handler):
    # Log request start
    logger.info(f"Request started: {request.method} {request.path}")
    
    try:
        # Process the request
        response = await handler(request)
        
        # Log response status
        logger.info(f"Request completed: {request.method} {request.path} - Status: {response.status}")
        return response
    except Exception as e:
        # Log any exceptions
        logger.error(f"Request failed: {request.method} {request.path} - Error: {str(e)}")
        raise

class ItemService:
    def __init__(self):
        self.app = aiohttp.web.Application(middlewares=[logging_middleware])
        self.pool = None
        self.items = []

    async def setup_db(self, loop):
        dsn = os.getenv('DB_DSN', 'postgresql://postgres:postgres@localhost:5432/images_db')
        max_retries = 5
        retry_delay = 2  # seconds
        
        for attempt in range(max_retries):
            try:
                logger.info(f"Attempting to connect to database (attempt {attempt + 1}/{max_retries})")
                # First try to connect to check if database exists
                conn = await asyncpg.connect(dsn)
                await conn.close()
                
                # If connection successful, create pool
                self.pool = await asyncpg.create_pool(dsn, loop=loop)
                logger.info("Database connection established successfully")
                return
            except asyncpg.InvalidCatalogNameError:
                logger.error("Database does not exist. Please create the database first.")
                sys.exit(1)
            except (asyncpg.PostgresError, OSError) as e:
                if attempt < max_retries - 1:
                    logger.warning(f"Connection attempt failed: {str(e)}. Retrying in {retry_delay} seconds...")
                    await asyncio.sleep(retry_delay)
                else:
                    logger.error(f"Failed to connect to database after {max_retries} attempts: {str(e)}")
                    sys.exit(1)

    async def healthcheck(self, request):
        return web.Response(status=200, text="OK")

    async def create_item(self, request):
        data = await request.json()
        name = data.get('name')
        description = data.get('description')
        if not name or not description:
            logger.warning(f"Invalid request data: name={name}, description={description}")
            return aiohttp.web.Response(status=400)
        
        logger.info(f"Creating new item: name={name}")
        stmt = "INSERT INTO items (name, description, creation_date) VALUES ($1, $2, $3)"
        await self.pool.execute(stmt, name, description, datetime.utcnow())
        logger.info(f"Item created successfully: name={name}")
        return aiohttp.web.Response(status=201)

    async def list_items(self, request):
        logger.info("Listing all items")
        rows = await self.pool.fetch("SELECT * FROM items")
        items = [{"id": row[0], "name": row[1], "description": row[2], "creation_date": row[3]} for row in rows]
        logger.info(f"Found {len(items)} items")
        return aiohttp.web.Response(body=json.dumps(items).encode(), content_type='application/json')

    async def get_env(self, request):
        logger.info("Get envs")
        return aiohttp.web.Response(body=json.dumps(dict(environ)).encode(), content_type='application/json')

    def add_routes(self):
        self.app.router.add_route('GET', '/healthcheck', self.healthcheck)
        self.app.router.add_route('POST', '/items', self.create_item)
        self.app.router.add_route('GET', '/env', self.get_env)

async def main():
    logger.info("Starting service...")
    service = ItemService()
    service.add_routes()
    await service.setup_db(asyncio.get_event_loop())
    logger.info("Service is ready to accept requests")
    return service.app

if __name__ == '__main__':
    app = asyncio.run(main())
    web.run_app(app, host='0.0.0.0', port=8080)
