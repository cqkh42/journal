#!/bin/sh
set -e

echo "Running migrations"
python3 manage.py migrate --noinput

echo "Starting server..."
exec "$@"