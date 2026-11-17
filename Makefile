TEXBIN = /Library/TeX/texbin

slides:
	mkdir -p output && \
	$(TEXBIN)/pdflatex -synctex=1 -interaction=nonstopmode -file-line-error -output-directory=output main.tex && \
	$(TEXBIN)/biber --output-directory=output main && \
	$(TEXBIN)/pdflatex -synctex=1 -interaction=nonstopmode -file-line-error -output-directory=output main.tex && \
	$(TEXBIN)/pdflatex -synctex=1 -interaction=nonstopmode -file-line-error -output-directory=output main.tex

clean:
	rm -rf output

.PHONY: slides clean
