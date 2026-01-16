# Makefile for HDR Project

PROJNAME := hdr
MAIN_FILE := $(PROJNAME).tex

# Tools
LATEXMK := latexmk

# Options
# -pdf    : Generate PDF using pdflatex
# -interaction=nonstopmode : Don't stop on errors
LATEXMK_OPT := -pdf -interaction=nonstopmode -use-make -f

all: $(PROJNAME).pdf

$(PROJNAME).pdf: $(MAIN_FILE) all.bib
	$(LATEXMK) $(LATEXMK_OPT) $(MAIN_FILE)

clean:
	$(LATEXMK) -C
	rm -f *.bbl *.run.xml *.synctex.gz

.PHONY: all clean
