import pandas as pd
import deepl

# Load the CSV file
file_path = 'mcc_codes.csv'  # Ensure the file is in the same directory
data = pd.read_csv(file_path)

# Initialize the DeepL Translator with your API key
translator = deepl.Translator("")

# Extract the "edited_description" column for translation
english_texts = data['edited_description'].dropna().tolist()

# Translate to Hungarian with error handling
translations = []
for text in english_texts:
    try:
        # Translate text using DeepL
        result = translator.translate_text(text, target_lang="HU")
        translations.append(result.text)
    except Exception as e:
        # Handle any unexpected errors
        print(f"Unexpected error for text: {text}\n{e}")
        translations.append("Error: Translation failed")

# Add a new column with a "hu_" prefix for Hungarian translations
data['hu_edited_description'] = data['edited_description'].map(dict(zip(english_texts, translations)))

# Save the updated dataframe
updated_file_path = 'mcc_codes_translated.csv'
data.to_csv(updated_file_path, index=False)
print(f"Translated file saved to {updated_file_path}")
