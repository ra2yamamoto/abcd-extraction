import nltk
nltk.download('words')

import pandas as pd

df = pd.read_csv('data/variable_descriptions.csv')

# Get the set of all English words
english_words_set = set(nltk.corpus.words.words())

# Function to keep only English words and special characters
def keep_english_words_only(text):
    # Split the text into words, preserving special characters
    tokens = re.findall(r'\w+|[^\w\s]', text, re.UNICODE)
    
    # Filter out tokens that are not in the English words corpus and are not special characters or numbers
    filtered_tokens = [token for token in tokens if token.lower() in english_words_set or not token.isalpha()]
    
    # Reassemble the text
    return ' '.join(filtered_tokens)

# Apply the refined function to the 'notes' column
df['notes'] = df['notes'].astype(str).apply(keep_english_words_only)

# Save the further refined DataFrame to a new CSV file
output_path_refined = '/variable_descriptions_no_non_english.csv'
df.to_csv(output_path_refined, index=False)

output_path_refined
