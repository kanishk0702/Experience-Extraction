import spacy

def experience(text):
    experience_mapping = []
    words = text.split()
    for i, word in enumerate(words):
        if word.lower() in ["minimum", "maximum", "at", "least", "years", "yrs", "year"]:
            continue
        try:
            num = int(word)
            if i > 0 and words[i - 1].lower() in ["minimum", "at", "least"]:
                experience_mapping.append((num, num + 2))
            elif i > 0 and words[i - 1].lower() == "maximum":
                experience_mapping.append((max(0, num - 2), num))
            elif i < len(words) - 1 and words[i + 1] in ["to", "-"]:
                experience_mapping.append((num, int(words[i + 2])))
            elif "+" in word:
                experience_mapping.append((num, num + 2))
        except ValueError:
            continue
    return experience_mapping if experience_mapping else [("Unknown", "Unknown")]

def extract_experience_from_jd(jd_text):
    """Extracts experience from job descriptions using NLP."""
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(jd_text)
    sentences = [sent.text for sent in doc.sents if "year" in sent.text.lower() or "yr" in sent.text.lower()]
    experience_data = {}

    def experience(sentence):
        experience_mapping = experience(sentence)
        return experience_mapping
    for sentence in sentences:
        experience_data[sentence] = experience(sentence)
    return experience_data

def read_job_descriptions(file_path):
    """Reads job descriptions from a text file."""
    with open(file_path, "r", encoding="utf-8") as file:
        job_descriptions = file.read().split("---")  
    return job_descriptions

# Example Usage:
file_path = "job_descriptions.txt"  # Ensure the file exists
job_descriptions = read_job_descriptions(file_path)

for jd in job_descriptions:
    experience_info = extract_experience_from_jd(jd)
    print(f"Extracted Experience: {experience_info}\n")