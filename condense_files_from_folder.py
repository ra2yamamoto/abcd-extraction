# do a recursive search for file names of interest in directory, copy into a single folder

from pathlib import Path
import shutil
import json

def main():
  specs_file = "specifications/New Specifications 5.1.json"
  main_dir = "abcd-data-release-5.1"
  condensed_dir = "data"
  data = None

  with open(specs_file) as f:
    data = json.load(f)
  
  p = Path(main_dir)
  all_paths = list(p.glob('**/*.csv'))

  group_names = ["CognitiveSpecs", "DemoSpecs", "NeuralDataSpecs", "OutcomeSpecs"]

  for name in group_names:
    for spec in data[name]:
      for path in all_paths:
        s_path = str(path)
        if spec["filename"] in s_path:
          shutil.copy(s_path, condensed_dir)

if __name__ == "__main__":
  main()