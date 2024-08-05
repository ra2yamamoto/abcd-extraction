import json
import csv

def main():
  old_names_filename = "output/Specifications OLD NAMES.json"
  table_name_map_filename = "5.0 to 4.0 table name map.csv"
  pretty = True # set to false if using Python version < 3
  output_name = "output/Specifications 5.1.json"

  table_name_map = {}

  data = None

  with open(old_names_filename) as f:
    data = json.load(f)
  
  with open(table_name_map_filename) as f:
    csv_file = csv.reader(f)
    for line in csv_file:
      table_name_map[line[1]] = line[0]
  
  print(table_name_map)

  group_names = ["CognitiveSpecs", "DemoSpecs", "NeuralDataSpecs", "OutcomeSpecs"]

  for name in group_names:
    for spec in data[name]:
      spec["filename"] = table_name_map[spec["filename"][:-4]] + ".csv"

  if pretty:
    with open(output_name, 'w', encoding='utf-8') as f:
      json.dump(data, f, ensure_ascii=False, indent=4)
  else:
    with open(output_name, 'w') as f:
      json.dump(data, f)

if __name__ == "__main__":
  main()