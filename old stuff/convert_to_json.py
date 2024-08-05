# translate old specs into json and account for file name changes

from old_specs import *
import json

def main():
  output_name = "output/Specifications OLD NAMES.json"
  pretty = True # set to false if using Python version < 3

  CognitiveSpecsOut = []
  DemoSpecsOut = []
  NeuralDataSpecsOut = []
  OutcomeSpecsOut = []

  for fs in CognitiveSpecs:
    CognitiveSpecsOut.append(file_spec_to_dict(fs))

  for fs in DemoSpecs:
    DemoSpecsOut.append(file_spec_to_dict(fs))

  for fs in NeuralDataSpecs:
    NeuralDataSpecsOut.append(file_spec_to_dict(fs))

  for fs in OutcomeSpecs:
    OutcomeSpecsOut.append(file_spec_to_dict(fs))

  final = {
    "CognitiveSpecs": CognitiveSpecsOut,
    "DemoSpecs": DemoSpecsOut,
    "NeuralDataSpecs": NeuralDataSpecsOut,
    "OutcomeSpecs": OutcomeSpecsOut,
  }

  if pretty:
    with open(output_name, 'w', encoding='utf-8') as f:
      json.dump(final, f, ensure_ascii=False, indent=4)
  else:
    with open(output_name, 'w') as f:
      json.dump(final, f)

if __name__ == "__main__":
  main()