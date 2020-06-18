.PHONY: install uninstall reinstall test clean pak unpak

install:
	pip install .

uninstall:
	pip uninstall hrot-cli-tools -y

reinstall: uninstall install

publish:
	python setup.py sdist
	twine upload dist/*

publish-test:
	python setup.py sdist
	python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

package:
	python package.py

build: pak unpak

pak:
	pyinstaller --name=pak --onefile ./hcli/pak/cli.py

unpak:
	pyinstaller --name=unpak --onefile ./hcli/unpak/cli.py

test:
	python -m unittest discover -s tests

clean:
	find . -name "*.pyc" -delete
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf *.spec
	rm -rf *.zip
