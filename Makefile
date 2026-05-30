build:
	pip install -r requirements.txt

test:
	pytest clinic/ --tb=short

lint:
	flake8 clinic/ config/ --max-line-length=120 --exclude=migrations
	black --check clinic/ config/

security:
	bandit -r clinic/ config/ -f json || true
	safety check || true

package:
	docker build -t petclinic:latest .
