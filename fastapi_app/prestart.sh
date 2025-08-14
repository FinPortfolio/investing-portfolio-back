#!/usr/bin/env bash

set -e

echo "Run apply migrations..."
alembic -c fastapi_app/alembic.ini upgrade head
echo "Migrations has applied!"

exec "$@"