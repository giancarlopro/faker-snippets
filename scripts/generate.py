import re
from os import listdir
from pprint import pprint

resnip = re.compile(r"(Faker::(\w+)\.(\w+)(\(.+\)){0,1}) #=>")

files = listdir("doc/")

snippets = list()

for f in files:
    with open("doc/{}".format(f)) as snpfile:
        for snippet in resnip.finditer(snpfile.read()):
            snippets.append(snippet)

formated_snippet = dict()

for s in snippets:
    group_1 = s.group(1).replace("\"", "\\\"")
    formated_snippet[group_1] = dict()
    formated_snippet[group_1]["scope"] = "ruby"
    formated_snippet[group_1]["prefix"] = group_1
    formated_snippet[group_1]["body"] = group_1
    formated_snippet[group_1]["description"] = "Fake {} {}".format(s.group(2), s.group(3))

def is_last_key(d, key):
    keys = list(d.keys())
    return key == keys.pop()

with open("snippets.json", "w") as f:
    f.write("{")
    for name in formated_snippet:
        f.write("\n\t\"{}\":{{".format(name))
        for key in formated_snippet[name]:
            f.write("\n\t\t\"{0}\":\"{1}\"".format(key, formated_snippet[name][key]))
            if not is_last_key(formated_snippet[name], key):
                f.write(",")
        f.write("\n\t}")
        if not is_last_key(formated_snippet, name):
            f.write(",")
    f.write("\n}\n")
