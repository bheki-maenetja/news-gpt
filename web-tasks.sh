#!/bin/bash
chmod a+x web-tasks.sh
python -m nltk.downloader all
python -m spacy download en_core_web_lg
python -m spacy download en_core_web_sm
python app.py