SHELL = /bin/bash -eu
.SECONDARY:
.DELETE_ON_ERROR:

-include Makefile.local

presentation-skim.pdf:

%-skim.pdf: %.pdf
	cp $< $@

%.pdf: %.tex
	xelatex -interaction=nonstopmode presentation.tex
