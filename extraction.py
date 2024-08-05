import pandas as pd
import numpy as np
import json

data_dir = "data/"
output_dir = "output/"

def extract_cols(filename, period, numeric, rename):
  df = pd.read_csv(f'{data_dir}{filename}', low_memory=False)

  cols = list(rename.keys())
  df = df[['src_subject_id', 'eventname'] + cols].iloc[1:, :]
  df = df.rename(columns={'src_subject_id': 'subject'})
  df = df.query(f'eventname.str.contains("{period}", na=False)', engine='python').drop(columns=['eventname'])

  if filename == 'nc_y_smarte.csv':
    df = df.replace({'cannot be computed': np.nan})

  for col in cols:
    if col not in numeric:
      df[col] = df[col].astype(str)
      df[col] = [x.replace(',', '.') for x in df[col]]
      try: 
        df[col] = df[col].astype(float)
      except Exception as err:
        print(f"ERROR converting back from str to float in {filename} in column {col}: {err}")
      df = df.replace({555: np.nan, 777: np.nan, 888: np.nan, 999: np.nan})
  df = df.rename(columns=rename)
  return df

def get_cognitive_tasks(period, version, spec_list):
  cognitive = pd.DataFrame([], columns=['subject']).astype('category')
  for i, spec in enumerate(spec_list):
    df = extract_cols(spec["filename"], period, spec["nonnumericcols"], spec["cols"])

    if 'sst_acceptable_performance' in df.columns:
      df = df.query('sst_acceptable_performance == 1').reset_index(drop=True)
    elif 'mid_acceptable_performance' in df.columns and 'mid_num_trials' in df.columns:
      df = df.query('mid_acceptable_performance == 1').reset_index(drop=True)
      df = df.query('mid_num_trials >= 100').reset_index(drop=True)
    elif 'lmt_accuracy' in df.columns:
      df['lmt_efficiency'] = df['lmt_accuracy'] / df['lmt_correct_mrt']
    elif 'nb_acceptable_performance' in df.columns:
      df = df.query('nb_acceptable_performance == 1').reset_index(drop=True)
    elif 'ddt_choice_validity' in df.columns:
      df = df.query('ddt_choice_validity > 2').reset_index(drop=True)
    elif 'str_mrt_ic' in df.columns:
      df['str_stroop_mrt'] = df['str_mrt_ic'] - df['str_mrt_c']
      df['str_stroop_acc'] = df['str_accuracy_c'] - df['str_accuracy_ic']

    cognitive = pd.merge(cognitive, df, on='subject', how='outer')
  cognitive = cognitive.convert_dtypes(convert_string=False)
  cognitive.to_csv(f'{output_dir}/cognitive_{period}_{version}.csv')
  return cognitive

def get_demographics(period, version, spec_list):
  demo = pd.DataFrame([], columns=['subject']).astype('category')
  for i, spec in enumerate(spec_list):
    df = extract_cols(spec["filename"], period, spec["nonnumericcols"], spec["cols"])

    if 'w1' in df.columns:
      df['weight'] = df[['w1', 'w2', 'w3']].mean(axis=1, skipna=True)
      df.drop(columns=['w1', 'w2', 'w3'], inplace=True)
    elif 'medhx_doctorvisit_p' in df.columns:
      df['medhx_p'] = df[["medhx_doctorvisit_p", "medhx_asthma_p", "medhx_allergies_p", "medhx_brain_p",
                          "medhx_diabetes_p", "medhx_epilepsy_p", "medhx_heart_p", "medhx_headaches_p",
                          "medhx_emergencyroom_p", "medhx_brokenbones_p", "medhx_seriousinjury_p"]].mean(axis=1)
    elif 'puberty_k' in df.columns: # TODO: FIX HERE, WHERE DO WE GET SEX FROM ????????
      df['puberty_k'] = np.where(df.sex == 'M', df.male_puberty, df.female_puberty)
      df = df[['subject', 'puberty_k']]
    elif 'fitbit_include' in df.columns:
      df = df.query('fitbit_include == 1').reset_index(drop=True)
      df = df.groupby(['subject']).mean().reset_index(drop=False)
    elif 'parent_care_misbehave_k' in df.columns:
      df['parent_cares_ss_k'] = df[['parent_care_misbehave_k', 'parent_care_whereabouts_k',
                                    'parent_care_friends_k', 'parent_helphomework_k','parent_safeplay_k',
                                    'parent_gotoschool_k', 'parent_troubleschool_k',
                                    'parent_helpunderstanding_k']].mean(axis=1)
    demo = pd.merge(demo, df, on='subject', how='outer')
  demo = demo.convert_dtypes(convert_string=False)
  demo.to_csv(f'{output_dir}/demographic_{period}_{version}.csv')
  return demo

def get_neuraldata(period, version, spec_list):
  neuraldata = pd.DataFrame([], columns=['subject']).astype("category")
  for i, spec in enumerate(spec_list):
    df = extract_cols(spec["filename"], period, spec["nonnumericcols"], spec["cols"])
    neuraldata = pd.merge(neuraldata, df, on='subject', how='outer')

  neuraldata = neuraldata.convert_dtypes(convert_string=False)
  neuraldata.to_csv(f'{output_dir}/neuraldata_{period}.csv')
  return neuraldata

def get_outcomes(period, version, spec_list):
  outcomes = pd.DataFrame([], columns=['subject']).astype("category")

  for i, spec in enumerate(spec_list):
    df = extract_cols(spec["filename"], period, spec["nonnumericcols"], spec["cols"])

    if "emoreg_sup_control_k" in df.columns:
      df['emoreg_sup_ss_k'] = df[['emoreg_sup_control_k', 'emoreg_sup_hide_k', 'emoreg_sup_self_k']].mean(axis=1)
      df['emoreg_reapp_ss_k'] = df[['emoreg_reapp_happy_k', 'emoreg_reapp_less_bad_k',
                                    'emoreg_reapp_thoughts_k']].mean(axis=1)
    outcomes = pd.merge(outcomes, df, on='subject', how='outer')

  outcomes = outcomes.convert_dtypes(convert_string=False)
  outcomes.to_csv(f'{output_dir}/outcomes_{period}_{version}.csv')
  return outcomes

if __name__ == "__main__":
  data = None
  with open("specifications/New Specifications 5.1.json") as f:
    data = json.load(f)
  a = get_cognitive_tasks("3_year", "test", data["DemoSpecs"])
  print(a)