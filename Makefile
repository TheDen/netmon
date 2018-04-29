# build app
build:
	python3 setup.py sdist
.PHONY: build

publish:
	twine upload dist/* --skip-existing
.PHONY: push

convert:
	pandoc --from=markdown --to=rst --output=README.rst README.md
.PHONY: push

clean:
	git clean -fdx

