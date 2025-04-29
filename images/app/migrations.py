import asyncio
import os
import asyncpg
from typing import List, Dict, Any

# Database connection DSN from environment variable
DB_DSN = os.getenv('DB_DSN', 'postgresql://postgres:postgres@localhost:5432/images_db')

# List of migrations to apply in order
MIGRATIONS = [
    """
    CREATE TABLE IF NOT EXISTS images (
        id SERIAL PRIMARY KEY,
        filename VARCHAR(255) NOT NULL,
        file_path VARCHAR(255) NOT NULL,
        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
    );
    """,
    """
    CREATE INDEX IF NOT EXISTS idx_images_filename ON images(filename);
    """
]

async def get_db_connection() -> asyncpg.Connection:
    """Create a database connection using DSN."""
    return await asyncpg.connect(DB_DSN)

async def apply_migrations() -> None:
    """Apply all pending migrations to the database."""
    conn = await get_db_connection()
    try:
        # Create migrations table if it doesn't exist
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS migrations (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                applied_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
            );
        """)

        # Get already applied migrations
        applied_migrations = await conn.fetch("SELECT name FROM migrations")
        applied_names = {m['name'] for m in applied_migrations}

        # Apply new migrations
        for i, migration in enumerate(MIGRATIONS):
            migration_name = f'migration_{i+1}'
            if migration_name not in applied_names:
                print(f"Applying migration {migration_name}...")
                await conn.execute(migration)
                await conn.execute(
                    "INSERT INTO migrations (name) VALUES ($1)",
                    migration_name
                )
                print(f"Migration {migration_name} applied successfully")
            else:
                print(f"Migration {migration_name} already applied")

    finally:
        await conn.close()

if __name__ == "__main__":
    asyncio.run(apply_migrations()) 