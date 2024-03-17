FROM texlive/texlive:latest

WORKDIR /app

COPY document.tex /app
COPY bobr.png /app

RUN pdflatex -interaction nonstopmode document.tex

CMD ["cp", "document.pdf", "/output/document.pdf"]
