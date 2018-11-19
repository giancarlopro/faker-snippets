import re
from os import listdir
from pprint import pprint

resnip = re.compile(r"(Faker::(\w+)\.(\w+)(\(.+\)){0,1}) #=>")

files = listdir("faker/doc/v1.9.1/")

snippets = list()

for f in files:
    with open("faker/doc/v1.9.1/{}".format(f)) as snpfile:
        for snippet in resnip.finditer(snpfile.read()):
            snippets.append(snippet)

formated_snippet = dict()
grouped = dict()

for s in snippets:
    group_1 = s.group(1).replace("\\", "\\\\")
    group_1 = group_1.replace("\"", "\\\"")
    formated_snippet[group_1] = dict()
    formated_snippet[group_1]["scope"] = "ruby"
    formated_snippet[group_1]["prefix"] = group_1
    formated_snippet[group_1]["body"] = group_1
    formated_snippet[group_1]["description"] = "Fake {} {}".format(s.group(2), s.group(3))
    
    if s.group(4):
        formated_snippet[group_1]["short"] = "{}.{}{}".format(s.group(2), s.group(3), s.group(4))
    else:
        formated_snippet[group_1]["short"] = "{}.{}".format(s.group(2), s.group(3))
    
    formated_snippet[group_1]["short"] = formated_snippet[group_1]["short"].replace("\\", "\\\\")
    formated_snippet[group_1]["short"] = formated_snippet[group_1]["short"].replace("\"", "\\\"")
    try:
        grouped[s.group(2)].append(formated_snippet[group_1])
    except KeyError:
        grouped[s.group(2)] = list()
        grouped[s.group(2)].append(formated_snippet[group_1])

def is_last_key(d, key):
    keys = list(d.keys())
    p = keys.pop()
    if p == "short":
        return key == "description"
    return key == p

with open("../snippets/snippets.json", "w") as f:
    f.write("{")
    for name in formated_snippet:
        f.write("\n\t\"{}\":{{".format(name))
        for key in formated_snippet[name]:
            if key == "short":
                continue
            f.write("\n\t\t\"{0}\":\"{1}\"".format(key, formated_snippet[name][key]))
            if not is_last_key(formated_snippet[name], key):
                f.write(",")
        f.write("\n\t}")
        f.write(",")
        # Short one
        f.write("\n\t\"{}\":{{".format(formated_snippet[name]["short"]))
        for key in formated_snippet[name]:
            if key == "short":
                continue
            f.write("\n\t\t\"{0}\":\"{1}\"".format(key, formated_snippet[name][key if key != "prefix" else "short"]))
            if not is_last_key(formated_snippet[name], key):
                f.write(",")
        f.write("\n\t}")
        if not is_last_key(formated_snippet, name):
            f.write(",")
    f.write("\n}\n")

with open("../README.md", "w") as f:
    with open('stub.md') as rs:
        stub = rs.read()
    
    f.write(stub)
    f.write("## Features\n\n")

    f.write("|Index|\n")
    f.write("|-----|\n")
    for group in grouped:
        f.write("| [{}](#{}) |\n".format(group, str(group).lower()))
    f.write("\n")

    for group in grouped:
        f.write("### {}\n".format(group))
        f.write("|Snippet|Short Snippet|\n")
        f.write("|-------|-------------|\n")
        for snip in grouped[group]:
            f.write("| {} | {} |\n".format(snip["body"], snip["short"]))