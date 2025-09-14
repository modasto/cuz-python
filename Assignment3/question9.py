import re

def extract_emails(text):
    """
    I. Uses regular expressions to extract all email addresses from a given text.
    """
    # A common regex for finding email addresses
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(email_regex, text)

def validate_date(date_string):
    """
    II. Uses regular expressions to validate a date in the format "YYYY-MM-DD".
    """
    # Regex to check for YYYY-MM-DD format.
    # This is a basic format check, not a validation of valid dates (e.g., 2023-02-30)
    date_regex = r'^\d{4}-\d{2}-\d{2}$'
    if re.fullmatch(date_regex, date_string):
        return True
    return False

def replace_word(text, old_word, new_word):
    """
    III. Uses regular expressions to replace all occurrences of a word with another word.
    """
    # \b ensures that we match whole words only
    return re.sub(r'\b' + re.escape(old_word) + r'\b', new_word, text, flags=re.IGNORECASE)

def split_by_non_alphanumeric(text):
    """
    IV. Use regular expressions to split a string by all non-alphanumeric characters.
    """
    # \W+ matches one or more non-alphanumeric characters
    return re.split(r'\W+', text)

def main():
    """
    Main function to demonstrate the regex operations.
    """
    # --- I. Extract Emails ---
    print("--- I. Extracting Email Addresses ---")
    sample_text_emails = "Contact us at support@example.com or for sales, try sales.team@corp.co.uk. Invalid: user@.com"
    found_emails = extract_emails(sample_text_emails)
    print(f"Original text: '{sample_text_emails}'")
    print(f"Extracted emails: {found_emails}\n")

    # --- II. Validate Date ---
    print("--- II. Validating Dates (YYYY-MM-DD) ---")
    date1 = "2023-10-26"
    date2 = "26-10-2023"
    date3 = "2023/10/26"
    date4 = "not-a-date"
    print(f"Is '{date1}' a valid format? {validate_date(date1)}")
    print(f"Is '{date2}' a valid format? {validate_date(date2)}")
    print(f"Is '{date3}' a valid format? {validate_date(date3)}")
    print(f"Is '{date4}' a valid format? {validate_date(date4)}\n")

    # --- III. Replace Word ---
    print("--- III. Replacing a Word ---")
    sample_text_replace = "The quick brown fox jumps over the lazy dog. The fox is very quick."
    old_word = "quick"
    new_word = "FAST"
    replaced_text = replace_word(sample_text_replace, old_word, new_word)
    print(f"Original text: '{sample_text_replace}'")
    print(f"Text after replacing '{old_word}' with '{new_word}': '{replaced_text}'\n")

    # --- IV. Split by Non-Alphanumeric Characters ---
    print("--- IV. Splitting by Non-Alphanumeric Characters ---")
    sample_text_split = "Hello, world! This is a test...123."
    split_words = split_by_non_alphanumeric(sample_text_split)
    # Filter out empty strings that can result from leading/trailing delimiters
    split_words = [word for word in split_words if word]
    print(f"Original text: '{sample_text_split}'")
    print(f"Split words: {split_words}\n")


if __name__ == "__main__":
    main()