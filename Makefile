.PHONY: install run test robot ci-local clean

install:
	pip install -r requirements.txt

run:
	python -m uvicorn app.main:app --host 127.0.0.1 --port 8000

test:
	pytest -q

robot:
	robot -d robot-reports robot_tests

ci-local:
	@echo "Starting API in background..."
	python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --log-level warning & \
	PID=$$!; \
	python scripts/wait_for_http.py http://127.0.0.1:8000/health 30; \
	echo "Running pytest..."; \
	pytest -q; \
	echo "Running robot..."; \
	robot -d robot-reports robot_tests; \
	echo "Stopping API..."; \
	kill $$PID

clean:
	rm -rf robot-reports .pytest_cache __pycache__
