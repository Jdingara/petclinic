build:
	pip install -r requirements.txt

test:
	python -m pytest tests/ || python -m unittest discover -s tests -v

lint:
	flake8 clinic/ config/ --max-line-length=120 --exclude=migrations
	black --check clinic/ config/ || true

security:
	bandit -r clinic/ config/ -f json || true
	safety check || true

package:
	docker build -t petclinic:latest .
