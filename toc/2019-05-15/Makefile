SHELL = /bin/bash -eu
.DELETE_ON_ERROR:
.SECONDARY:
.SUFFIXES:

.PHONY: all bootstrap

slides.html: slides.adoc custom.css
	bundle exec asciidoctor-revealjs $<

bootstrap:
	gem install --user bundler
	bundle
