REPORT = csuexperiment_main
# TEX dir
TEX_DIR = content

# Option for latexmk
LATEXMK_OPT_BASE = -xelatex -gg -silent
LATEXMK_OPT = $(LATEXMK_OPT_BASE) -f
LATEXMK_OPT_PVC = $(LATEXMK_OPT_BASE) -pvc

all: $(REPORT).pdf

.PHONY : all clean cleanall pvc view wordcount zip

$(REPORT).pdf : $(REPORT).tex $(TEX_DIR)/*.tex csuexperiment.cls csuexperiment_style.cls Makefile
	-latexmk $(LATEXMK_OPT) $(REPORT)

pvc :
	latexmk $(LATEXMK_OPT_PVC) $(REPORT)

view : $(REPORT).pdf
	@if command -v open >/dev/null 2>&1; then \
		open $<; \
	elif command -v xdg-open >/dev/null 2>&1; then \
		xdg-open $<; \
	else \
		echo "Please open $< manually."; \
	fi

wordcount:
	@texcount $(REPORT).tex -inc -ch-only | awk '/total/ {getline; print "纯中文字数\t\t\t:",$$4}'
	@texcount $(REPORT).tex -inc -chinese | awk '/total/ {getline; print "总字数（英文单词 + 中文字）\t:",$$4}'

clean :
	-@latexmk -c -silent 2> /dev/null
	-@rm -f $(TEX_DIR)/*.aux 2> /dev/null || true

cleanall :
	-@latexmk -C -silent 2> /dev/null
	-@rm -f $(TEX_DIR)/*.aux 2> /dev/null || true

zip :
	git archive --format zip --output csu-experiment-report.zip HEAD
