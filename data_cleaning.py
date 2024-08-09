# Functions and variables for data cleaning

import numpy as np
from sklearn.preprocessing import StandardScaler

def remove_outlier_bounds(series, bounds):
    lower, upper = bounds
    series = np.where(series < lower, np.nan, series)
    series = np.where(series > upper, np.nan, series)
    return series

def remove_outlier_IQR(df, cutoff=2.5):
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    df_final = df[~((df < (Q1 - cutoff * IQR)) | (df > (Q3 + cutoff * IQR)))]
    return df_final

def standardize(df):
    scaler = StandardScaler()
    df_z = scaler.fit_transform(df)
    return df_z

outlier_vars = {
    'height': (40, 80),
    'waist': (20, 50),
    'weight': (50, 200),
    'socialmedia_hoursperday_k': (0, 18),
    'screentime_weekday_ss_k': (0, 18),
    'screentime_weekend_ss_k': (0, 18),
    'nb_correct_mrt': (200, 2000),
    'nb_correct_mrt_2back': (200, 2000),
    'nb_correct_mrt_pos': (200, 2000),
    'nb_correct_mrt_neutral': (200, 2000),
    'nb_correct_mrt_neg': (200, 2000),
    'sst_ssrt_mean_est': (0, 2000),
    'sst_ssrt_int_est': (0, 2000),
    'mid_mrt_smrw': (150, 500),
    'mid_mrt_lgrw': (150, 500),
    'lmt_mrt': (200, 5000),
    'lmt_correct_mrt': (200, 5000),
    'lmt_incorrect_mrt': (200, 5000),
    'str_mrt': (200, 2500),
    'str_mrt_ic': (200, 2500),
    'str_mrt_c': (200, 2500),
    'str_stroop_mrt': (-2300, 2300),
    'ddt_mrt': (200, 4000),
    'ddt_mrt_delayed': (200, 4000),
    'ddt_mrt_delayed': (200, 4000),
    'ddt_mrt_immediate': (200, 4000),
    'correctRT_singlearith': (200, 5000)
}

standardize_vars = ['gd_safebets',
                    'gd_riskybets',
                    'ravlt_s_total',
                    'ravlt_l_total',
                    'mr_total',
                    'tb_picvocab',
                    'tb_flanker',
                    'tb_list',
                    'tb_cardsort',
                    'tb_pattern',
                    'tb_picture',
                    'tb_reading',
                    # 'tb_fluid',
                    # 'tb_cryst',
                    'tb_total',
                    'nb2_accuracy_pos',
                    'nb2_accuracy_neg',
                    'nb2_resp_bias_pos',
                    'nb2_D_prime_pos',
                    'nb2_resp_bias_neg',
                    'nb2_D_prime_neg',
                    'mid_total_payout',
                    'lmt_accuracy',
                    'str_accuracy',
                    'str_accuracy_ic',
                    'str_accuracy_c',
                    'str_stroop_acc',
                    'accu_mixeddigitarith',
                    'saliva_DHEA',
                    'saliva_estradiol',
                    'saliva_testosterone',
                    'blood_pressure_sys',
                    'blood_pressure_dia',
                    'fitbit_resting_hr',
                    'fitbit_steps',
                    'fitbit_sedentary_mins',
                    'fitbit_lightlyactive_mins',
                    'fitbit_fairlyactive_mins',
                    'fitbit_veryactive_mins',
                    'parent_monitoring_ss_k',
                    'family_conflict_ss_k',
                    'prosocial_ss_k',
                    'school_environment_ss_k',
                    'school_involvement_ss_k',
                    'school_disengagement_ss_k',
                    'problem_solving_ss_k',
                    'discrimination_ss_k',
                    'peers_beh_prosocial_ss_k',
                    'peers_beh_delinquent_ss_k',
                    'peer_net_protective_ss_k',
                    'parent_cares_ss_k',
                    'socialinfluence_meanfinal_k',
                    'neighborhood_safety_ss_p',
                    'prosocial_ss_p',
                    'family_conflict_ss_p',
                    'family_expression_ss_p',
                    'family_intellectual_ss_p',
                    'family_activities_ss_p',
                    'family_organisation_ss_p',
                    'atschool_total_problems_ss_t',
                    'atschool_external_ss_t',
                    'atschool_internal_ss_t',
                    'atschool_attention_ss_t',
                    'parent_anxdep_D_p',
                    'parent_attention_D_p',
                    'parent_aggressive_D_p',
                    'parent_internal_D_p',
                    'parent_external_D_p',
                    'parent_depress_D_p',
                    'parent_anxdisord_D_p',
                    'parent_adhd_D_p',
                    'parent_antisocial_D_p',
                    'parent_hyperactive_D_p',
                    'parent_somatic_problems_D_p',
                    'parent_intrusive_thoughts_D_p',
                    'parent_avoidant_person_D_p',
                    'parent_personal_strength_D_p',
                    # 'g_lifeevents_ss_k',
                    # 'b_lifeevents_ss_k',
                    # 'b_lifeevents_affected_ss_k',
                    'up_negative_urgency_ss_k',
                    'up_lackofplanning_ss_k',
                    'up_sensationseeking_ss_k',
                    'up_positiveurgency_ss_k',
                    'up_lackperseverance_ss_k',
                    'bis_behav_inhibition_ss_k',
                    'bis_reward_responsive_ss_k',
                    'bis_drive_ss_k',
                    'bis_funseeking_ss_k',
                    'mania_7up_ss_k',
                    'relational_victimization_ss_k',
                    'reputational_aggression_ss_k',
                    'reputational_victimization_ss_k',
                    'overt_aggression_ss_k',
                    'overt_victimization_ss_k',
                    'relational_aggression_ss_k',
                    'emoreg_sup_ss_k',
                    'emoreg_reapp_ss_k',
                    # 'g_lifeevents_ss_p',
                    # 'b_lifeevents_ss_p',
                    # 'b_lifeevents_affected_ss_p',
                    'anxdep_D_p',
                    'attention_D_p',
                    'aggressive_D_p',
                    'internal_D_p',
                    'external_D_p',
                    'somatic_problems_D_p',
                    'social_problems_D_p',
                    'thought_disorder_D_p',
                    'rule_breaking_D_p',
                    'depress_D_p',
                    'anxdisord_D_p',
                    'adhd_D_p',
                    'ocd_D_p',
                    'nb_correct_mrt',
                    'nb_correct_mrt_2back',
                    'nb_correct_mrt_pos',
                    'nb_correct_mrt_neutral',
                    'nb_correct_mrt_neg',
                    'sst_ssrt_mean_est',
                    'sst_ssrt_int_est',
                    'mid_mrt_smrw',
                    'mid_mrt_lgrw',
                    'lmt_mrt',
                    'lmt_correct_mrt',
                    'lmt_incorrect_mrt',
                    'str_mrt',
                    'str_mrt_ic',
                    'str_mrt_c',
                    'str_stroop_mrt',
                    'ddt_mrt',
                    'ddt_mrt_delayed',
                    'ddt_mrt_immediate',
                    'correctRT_singlearith']

fixed_vars = ['sex',
              'child_religion',
              'religious_service_frequency',
              'relig_importance',
              'child_white',
              'child_black',
              'parent_education',
              'parent_income',
              'parent_age',
              'struggle_food_expenses',
              'sex_P',
              '#_brothers_p',
              '#_sisters_p',
              'mother_dep',
              'father_dep',
              'parent_dep',
              'parent_suicide',
              'father_alcohol',
              'mother_alcohol',
              'father_druguse',
              'mother_druguse',
              'd_grandfather_dep',
              'd_grandmother_dep',
              'm_grandfather_dep',
              'm_grandmother_dep',
              'sibling_dep',
              'father_mania',
              'mother_mania',
              'father_trouble',
              'parent_hospitalized_emo',
              'parent_therapy_emo',
              'birth_weight_p',
              'prescriptionmed_pregnancy_p',
              'cigs_before_pregnancy_p',
              'alcohol_before_pregnancy_p',
              'weed_before_pregnancy_p',
              'cocaine_before_pregnancy_p',
              'heroin_before_pregnancy_p',
              'drugs_before_pregnancy_p',
              'cigs_during_pregnancy_p',
              'alcohol_during_pregnancy_p',
              'drinksperweek_during_pregnancy_p',
              'weed_during_pregnancy_p',
              'cocaine_during_pregnancy_p',
              'heroin_during_pregnancy_p',
              'drugs_during_pregnancy_p',
              'caffeine_during_pregnancy_p',
              'premature_birth_p',
              'months_breastfed_p',
              'firstwords_months_p',
              'asd_diagnosis',
              'schizophrenia_diagnosis']
