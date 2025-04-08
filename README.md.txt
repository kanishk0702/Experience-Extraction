Experience Extractor

Project Description :-
This project extracts and normalizes years of experience from job descriptions using Natural Language Processing (NLP). Given a set of job descriptions, it identifies relevant experience requirements and normalize them.

How It Works :-
-Reads job descriptions from a text file (job_descriptions.txt).
-Uses spacy for NLP processing.
-Identifies phrases containing experience requirements.
-Extracts and normalizes years of experience.
-Outputs structured experience data.

File Structure :-

experience_extractor :-

-experience_extractor.py - Main Python script
-job_descriptions.txt - Input job descriptions
-README.md - Project documentation

Project Setup and Library installation :-

1.Install Dependencies :-
Make sure you have Python installed and install spacy then run:
In command prompt;
pip install spacy
python -m spacy download en_core_web_sm

2.Add Job Descriptions :-
Open job_descriptions.txt
Add job descriptions separated by ---

3.Run the Extractor :-
python experience_extractor.py

Sample Results :-

Job Descriptions;

-Job Description - Data Scientist - "Experience Required: 3 to 5 years"
 extracted_experience - "3 - 5 years"

-Job Description - Software Engineer - "Looking for candidates with at least 2 years experience"
 extracted_experience - "2 - 4 years"

-Job Description - Full Stack Developer - "Minimum 5 years in MERN Stack"
 extracted_experience - "5 - 7 years"

-Job Description - HR Manager - "5+ years experience required"
 extracted_experience - "5 - 6 years"


