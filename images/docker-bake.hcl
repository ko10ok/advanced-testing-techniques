variable "APP_NAME" {
    default = "experimental-service"
}

group "default" {
    targets = ["service", "migrations", "e2e"]
}

target "base" {
    dockerfile = "Dockerfile"
    context = "app"
}

target "service" {
    inherits = ["base"]
    target = "service"
    tags = ["${APP_NAME}:latest"]
}

target "migrations" {
    inherits = ["base"]
    target = "migrations"
    tags = ["${APP_NAME}-migrations:latest"]
}

target "e2e" {
    dockerfile = "Dockerfile"
    context = "e2e"
    tags = ["${APP_NAME}-e2e:latest"]
} 