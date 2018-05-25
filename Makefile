build:
	python3 setup.py sdist
.PHONY: build

publish:
	twine upload dist/* --skip-existing
.PHONY: publish

convert:
	pandoc --from=markdown --to=rst --output=README.rst README.md
.PHONY: convert

clean:
	git clean -fdx
.PHONY: clean
