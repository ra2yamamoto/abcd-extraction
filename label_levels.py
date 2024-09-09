# Written in part by ChatGPT

import json
import pandas as pd

specs_filename = "specifications/New Specifications 5.1.json"

# Load the JSON file
with open(specs_filename) as f:
  specs = json.load(f)

# Load the CSV file
csv_file = 'data/variable_descriptions.csv'
df = pd.read_csv(csv_file)

# Function to parse the notes string into a dictionary, including only English descriptions
def parse_notes(notes):
  try:
    level_dict = {}
    if pd.notna(notes):  # Check if notes are not NaN
      entries = notes.split(';')
      for entry in entries:
        if '=' in entry:
          level, description = entry.split('=')
          # Keep only the English part if both English and Spanish are given
          english_description = description.split('/')[0].strip()
          try:
            level_dict[int(level.strip())] = english_description
          except ValueError:
            pass  # Ignore entries where the level is not an integer
  except Exception as e:
    print(e)
    print(notes)
  return level_dict

def get_labels():
  # List of variables for custom labels
  my_vars = [
    "tb_fluid_grouped", 
    "fitbit_veryactive_mins_grouped", 
    "fitbit_steps_grouped", 
    "socialmedia_hoursperday_k_grouped", 
    "area_deprivation_idx_grouped", 
    "parent_education_grouped", 
    "parent_age_grouped", 
    "weight_grouped", 
    "feelsafe_at_school_k_grouped", 
    "bdefs_lazy_p_grouped", 
    "easily_offended_p_grouped", 
    "bad_grades_grouped"
  ]

  # Custom labels
  custom_labels = {0: "bottom 25", 1: "middle 50", 2: "top 25"}

  # Initialize the dictionary to store the variable value labels
  variable_value_labels = {}

  # Iterate over the list of variables and assign the custom labels
  for var in my_vars:
    variable_value_labels[var] = custom_labels.copy()

  # Populate the variable_value_labels dictionary with annotations from the CSV
  for key in specs.keys():
    for spec in specs[key]:
      cols = spec['cols']
      for old_var, new_var in cols.items():
        # Find the row in the CSV that matches the old variable name
        match = df[df['var_name'] == old_var]
        if not match.empty:
          notes = match.iloc[0]['notes']
          parsed_notes = parse_notes(notes)
          if parsed_notes:  # Only add to the dictionary if there are annotations
            variable_value_labels[new_var] = parsed_notes

  return variable_value_labels