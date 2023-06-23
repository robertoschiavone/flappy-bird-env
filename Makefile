.DEFAULT_GOAL := all

PROJECT := flappy_bird_env

.PHONY: all
all: clean uninstall install

.PHONY: clean
clean:
	rm -rf __pycache__

	rm -rf build
	rm -rf dist
	find . -name $(PROJECT).egg-info -type d -prune -exec rm -rf {} +

.PHONY: uninstall
uninstall:
	pip uninstall $(PROJECT)

.PHONY: install
install:
	python -m build
	pip install .
