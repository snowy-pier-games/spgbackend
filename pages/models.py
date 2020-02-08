from django.urls import reverse
from django.db import models
from html.parser import HTMLParser
import os
from pathlib import Path
import re


class HTMLSearcher(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.data = ""

    def handle_data(self, data):
        self.data += data

    def get_data(self):
        return self.data

    def error(self, message):
        print(message)


class Content:
    def __init__(self):
        pass

    def searchInFile(self, searchText, subdir, filename):
        displayText = ""

        filepath = subdir + os.sep + filename
        with open(filepath, encoding="utf8") as file:
            text = file.read()
            searcher = HTMLSearcher()
            searcher.feed(text)
            text = searcher.get_data()
            text = re.sub(r"{%.*%}", "", text)

            textBegin = text.lower().find(searchText.lower())
            if textBegin > -1:
                textEnd = textBegin + len(searchText)
                lookBehind = max(0, textBegin - 64)
                lookAhead = min(len(text), textEnd + 64)

                prefix = ""
                suffix = ""
                if lookBehind > 0:
                    prefix = "..."
                if lookAhead < len(text):
                    suffix = "..."

                viewname = Path(filename).stem
                displayText = "<h3><a href='" + reverse(viewname) + "'>" + viewname + "</a></h3><p>" + prefix + \
                              text[lookBehind:textBegin] + "<span style='color:red;'>" + text[textBegin:textEnd] + \
                              "</span>" + text[textEnd:lookAhead] + suffix + "</p>"

        return displayText

    def search(self, searchText):
        displayText = ""

        for subdir, dirs, files in os.walk("pages/templates/pages"):
            for filename in files:
                displayText += self.searchInFile(searchText, subdir, filename)

        if not displayText:
            displayText = "No results"

        return displayText
