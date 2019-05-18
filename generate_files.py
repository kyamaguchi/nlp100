#!/usr/bin/env python

import os
import requests, bs4

url = "http://www.cl.ecei.tohoku.ac.jp/nlp100/"
base_dir = "python"

res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.content, "html.parser")

sections = soup.find_all("h3")
for section in sections:
    if section.a is not None:
        question = section.contents[1]
        number = question.split(".")[0]
        filepath = os.path.join(base_dir, number + '.py')

        if os.path.exists(filepath):
            print(filepath + " already exists.")
        else:
            print("Generating " + filepath)
            with open(filepath, 'w') as f:
                f.write("#!/usr/bin/env python\n")
                f.write("\n")
                f.write("print(\"" + question.replace('"', '\\"') + "\")\n")
                for tag in section.next_sibling.next_sibling.children:
                    if tag.name:
                        f.write("print(\"" + tag.text.strip().replace('"', '\\"').replace("\n", ', ') + "\")\n")
