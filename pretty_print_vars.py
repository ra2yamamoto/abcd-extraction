import json

s = None
with open("specifications/New Specifications 5.1.json") as f:
  s = json.load(f)

lines = []
for n in ["CognitiveSpecs", "DemoSpecs", "NeuralDataSpecs", "OutcomeSpecs"]:
  for spec in s[n]:
    c = "### " + spec["filename"] + "\n"
    b = "\n".join((k + " -> " + v for k, v in spec["cols"].items()))
    lines += [c + b + "\n\n"]
    
with open("output/pretty_vars.txt", "w") as f:
  f.writelines(lines)

# asd/adhd interactions