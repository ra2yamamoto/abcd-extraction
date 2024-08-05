### Missing columns
"rsfmri_c_ngd_stnvols": "rsfmri_frames_fd",
"rsfmri_c_ngd_stcontignvols": "rsfmri_frames_fg_contig"

### TODO
1. Incorporate the new variables from Shuquan and other places
  Get from doc, should be pretty easy
2. Stratify ALEs
  PROBLEM: ALEs aren't stable across time points
  QUESTION:
    I can't tell whether or not ALEs are cumulative. You would expect the responses to be cumulative based off of the questions, but sometimes people respond with fewer ALEs from one time point to the next. Should I just take the max? That seems the safest, but may undercount responses. I could also just take data from the latest time point, but that also wouldn't take all ALEs into account. 
  or, just collapse across time points
    i.e. calculate percentiles including all time points
    and stratify people at each time point according to that
    in that case, some people may end up in one group at one time point, but another in another time point
    based on the percentiles generated using aggregate data from all time points
    but that may skew things, since there's also within person variation

stratify 
bad_life_events
b_lifeevents_ss_k
  take the max?

if([ple_died_fu_y] = '2',1,0) plus if([ple_injured_fu_y] = '2',1,0) plus if([ple_crime_fu_y]= '2',1,0) plus if([ple_friend_fu_y]= '2',1,0) plus if([ple_friend_injur_fu_y]= '2',1,0) plus if([ple_financial_fu_y]= '2',1,0) plus if([ple_sud_fu_y]= '2',1,0) plus if([ple_ill_fu_y]= '2',1,0) plus if([ple_injur_fu_y]= '2',1,0) plus if([ple_argue_fu_y]= '2',1,0) plus if([ple_job_fu_y]= '2',1,0) plus if([ple_away_fu_y] = '2',1,0) plus if([ple_arrest_fu_y]= '2',1,0) plus if([ple_friend_died_fu_y]= '2',1,0) plus if([ple_mh_fu_y]= '2',1,0) plus if([ple_sib_fu_y]= '2',1,0) plus if([ple_victim_fu_y]= '2',1,0) plus if([ple_separ_fu_y]= '2',1,0) plus if([ple_law_fu_y]= '2',1,0) plus if([ple_school_fu_y]= '2',1,0) plus if([ple_move_fu_y]= '2',1,0) plus if([ple_jail_fu_y]= '2',1,0) plus if([ple_step_fu_y]= '2',1,0) plus if([ple_new_job_fu_y]= '2',1,0) plus if([ple_new_sib_fu_y] = '2',1,0)

### New Vars

ALEs: 
Anything else? 

Clark:

KSADS: (DSM Diagnosis) 
(ksads_10_869_t ; GAD_present) (ksads_11_917_t ; OCD_present)
(https://nda.nih.gov/data-structure/abcd_ksad501)

Mh_y_ksads_ss: 
Ksads_11_917_t: OCD_present
Ksads_10_869_t: GAD_present

Ph_y_mctq
Mctq_fd_min_to_sleep_calc: fallsleeptime
Mctq_fd_min_to_get_up_calc: wakeuptime
Mctq_sdweek_calc :wakesleepcalc
Mctq_msfsc_calc: chronotype

Ph_p_meds
med1_rxnorm_p : medname
Brought_medications: medtaken
medication1_dosage ; meddosage
prescribe_med_2_yn ; othermed
med2_rxnorm_p ; othermedname
medication2_dosage ; othermeddose

Mh_p_ssrs
ssrs_15r_p ; face_understanding

Munich ChronoType Questionnaire (mctq_fd_min_to_sleep_calc ; fallsleeptime) (mctq_fd_min_to_get_up_calc ; wakeuptime) (mctq_sdweek_calc; weeksleepcalc) (mctq_msfsc_calc ; chronotype)
( https://nda.nih.gov/data-structure/abcd_mcqc01 )

Medication Data Medsy01 (med1_rxnorm_p ; medname) (brought_medications ; medtaken) (medication1_dosage ; meddosage) (prescribe_med_2_yn ; othermed) (med2_rxnorm_p ; othermedname) (medication2_dosage ; othermeddose)
( https://nda.nih.gov/data-structure/medsy01 ) 

autism abcd_pssrs01.txt (ssrs_15r_p ; face_understanding)

# Neurocognition Battery

# ABCD Youth Life Events
# Let's use all life events instead of just including severe sickness.

ABCD Youth Family Environment Scale-Family Conflict Subscale Modified from PhenX (FES) all items and following items from the parent form: fam_enviro1_p - fam_enviro9r_p (including: “Family members sometimes get so angry they throw things”; “Family members hardly ever lose their tempers”; “Family members often criticize each other”; “Family members sometimes hit each other”; “Family members often try to one-up or outdo each other”; “In our family, we believe you don't ever get anywhere by raising your voice”.)

ABCD Youth Neighborhood Safety/Crime Survey Modified from PhexX (NSC)

ABCD Parent Diagnostic Interview for DSM-5 Full (KSADS-5) Traumatic Events
also PTSD symptoms and diagnosis, present and past
Difficulties in Emotion Regulation Scale Short Form

Sexual Orientation: kbi_desc_self , kbi_desc_self_2, kbi_desc_self_3, gish2_sexual_attract (should have sexual orientation in all waves because it may change over time among adolescents)

Discrimination (ce_y_dm): dim_matrix_q1 - dim_matrix_q7


Abcd_p_demo.csv
Demo_fam_exp2_v2
Demo_fam_exp3_v2
Demo_fam_exp4_v2
Demo_fam_exp5_v2
Demo_fam_exp6_v2
Demo_fam_exp7_v2

Ce_y_crpbi.csv
Crpbi_y_ss_parent
Crpbi_y_ss_caregiver

---

Ce_p_comc.csv

Ce_y_pnh.csv

Led_l_adi.csv
Reshist_addr1_adi_wsum

Ce_p_fes.csv
Fam_enviro1_p
Fam_enviro2r_p
Fam_enviro3_p
Fam_enviro4r_p
Fam_enviro5_p
Fam_enviro6_p
Fam_enviro7r_p
Fam_enviro8_p
Fam_enviro9r_p

Ce_y_nsc.csv
Neighborhood_crime_y

Mh_p_ksads_ptsd.csv
ksads_ptsd_raw_754_p	
ksads_ptsd_raw_755_p	
ksads_ptsd_raw_756_p	
ksads_ptsd_raw_757_p	
Ksads_ptsd_raw_758_p
Ksads_ptsd_raw_759_p
Ksads_ptsd_raw_760_p
Ksads_ptsd_raw_761_p
ksads_ptsd_raw_762_p	
Ksads_ptsd_raw_763_p
Ksads_ptsd_raw_764_p
Ksads_ptsd_raw_765_p
Ksads_ptsd_raw_766_p
Ksads_ptsd_raw_767_p
Ksads_ptsd_raw_768_p	
Ksads_ptsd_raw_769_p
Ksads_ptsd_raw_770_p

Mh_p_ders.csv		

Gish_y_sex.csv
Kbi_desc_self
Kbi_desc_self_2
Kbi_desc_self_3
gish2_sexual_attract

ce_y_dm.csv
Dim_matrix_q1
Dim_matrix_q2
Dim_matrix_q3
Dim_matrix_q4
Dim_matrix_q5
Dim_matrix_q6
Dim_matrix_q7

aggregate parent rated life events
exclusion
    parent rated ales

demo_fam_exp2_v2 (couldnt_afford_phone): 
demo_fam_exp3_v2 (couldnt_afford_rent_mortgage): 
demo_fam_exp4_v2 (evicted): 
demo_fam_exp5_v2 (gas_electric_oil_turned_off): 
demo_fam_exp6_v2 (needed_doc_didnt_go): 
demo_fam_exp7_v2 (needed_dentist_didnt_go): 


crpbi_y_ss_parent (y_acceptance_ss_p_crpbi): 
crpbi_y_ss_caregiver (y_acceptance_ss_caregiver_crpbi):

comc_ss_cohesion_p (p_comm_cohesion_ss)
comc_ss_control_p (p_comm_ctrl_ss)
comc_ss_collective_capacity_p (p_comm_collective_efficacy_ss)

fam_enviro3_p (family_angry_throw_things_p)
fam_enviro4r_p (family_lose_temper_rare_p)
fam_enviro5_p (family_criticize_each_other_often_p)
fam_enviro6_p (family_hit_each_other_p)
fam_enviro8_p (family_outdo_each_other_often_p)
fam_enviro9r_p (family_believe_not_raise_voice_p)