GH-PAGES = ${HOME}/dev/urubu-gh-pages/

all: build

build:
	python -m urubu build
	touch _build/.nojekyll

serve:
	python -m urubu serve

publish:
	rm -R docs
	cp -R _build docs
