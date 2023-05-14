.DEFAULT_GOAL = help

install:  ## Install dependencies
	poetry install

run:  ## Run app
	poetry run socket-chat

client:  ## Run client app
	poetry run chat-client

lint:  ## Run linter check
	poetry run flake8 socket_chat

test:  ## Run tests
	poetry run pytest -s .

type:  ## Run type check
	poetry run mypy socket_chat

test-coverage:  ## Create test coverage report
	poetry run pytest --cov=socket_chat --cov-report xml

coverage:  ## Check test coverage
	poetry run pytest --cov=socket_chat

check: lint test type  ## Run all code checks

help:  ## Display help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
	  | sort \
	  | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[0;32m%-30s\033[0m %s\n", $$1, $$2}'
