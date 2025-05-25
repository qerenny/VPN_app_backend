.PHONY: dev lint format migrate upgrade

# Запуск FastAPI сервера
dev:
	poetry run uvicorn vpn_backend.main:app --reload

# Применить все миграции
upgrade:
	poetry run alembic upgrade head

# Создать новую миграцию
migrate:
	poetry run alembic revision --autogenerate -m "update"

# Форматирование кода
format:
	poetry run black .
	poetry run ruff --fix .

# Проверка стиля
lint:
	poetry run ruff .
