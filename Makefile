# Makefile for Playwright Automation

# Default variables (can be overridden via CLI)
TEST_DIR ?= tests/
BROWSER ?= chromium
export REPORT_DIR ?= reports/
WORKERS ?= auto

.PHONY: help install test test-parallel report clean lint format

help:
	@echo "Available commands:"
	@echo "  make install             - Install dependencies and browsers"
	@echo "  make test                - Run tests sequentially"
	@echo "  make test-parallel       - Run tests in parallel"
	@echo "  make report              - Generate and open Allure report"
	@echo "  make lint                - Check code quality"
	@echo "  make format              - Format code"
	@echo "  make clean               - Clean project"

install:
	pip install -r requirements.txt
	playwright install --with-deps $(BROWSER)

test:
	pytest $(TEST_DIR) \
		--browser $(BROWSER) \
		--headless=$(HEADLESS) \
		--html=$(REPORT_DIR)/report.html \
		--self-contained-html
		--alluredir=$(REPORT_DIR)/allure-results \
		--reruns 2
		
		

test-parallel:
	pytest $(TEST_DIR) \
		-n $(WORKERS) \
		--browser $(BROWSER) \
		--headless=$(HEADLESS) \
		--html=$(REPORT_DIR)/report.html \
		--self-contained-html \
		--reruns 2

report:
	allure serve $(REPORT_DIR)/allure-results

lint:
	flake8 $(TEST_DIR)
	black --check $(TEST_DIR)

format:
	black $(TEST_DIR)

clean:
	rm -rf .pytest_cache/
	rm -rf $(REPORT_DIR)/*
	rm -rf playwright_logs/
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
