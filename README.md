Code to extract a bunch of variables from the ABCD data release folder into a single CSV file. 

You can specify which variables to extract in specifications/New Specifications 5.1.json. 

In order to run the code:

1. Place the abcd-data-release-5.1 folder into this folder (in the same folder as main_extraction.ipynb, etc.). If you are trying to extract a newer release, you will have to change the path to the main data release folder in condense_files_from_folder.py. (This code won't work for earlier releases, because the file names and folder structures are different.)

2. Run condense_files_from_folder.py

3. Run main_extraction.ipynb

4. Run main_cleaning.ipynb. The condensed/cleaned data should be in output/clean in .csv and .sav file formats.
