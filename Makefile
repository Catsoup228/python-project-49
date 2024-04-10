install:
	poetry install

brain-games:
	poetry run python -m brain_games1.scripts.brain_games

brain-even:
	poetry run python -m brain_games1.scripts.brain_even

publish:
	poetry publish --dry-run

build:
	poetry build

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

make lint:
	poetry run flake8 brain_games

