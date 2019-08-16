cd migrations
alembic revision --autogenerate -m "description of changes"
alembic upgrade head