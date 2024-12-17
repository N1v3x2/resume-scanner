# AI Resume Scanner

## Project Summary
This is a tool to score resumes against a provided job description. 

### Important features for resume scoring
1. Keywords match job description
2. Validate that skills are used in context ("built Flask app with Python" vs "Python" on its own)
3. Match sentences under "Projects" and "Experience" to the job description
4. Match job titles with job description
5. Determine number of years of relevant experience
6. Education: check degree & GPA
7. Check that resume has essential sections (contact info, skills, experience, education)
8. Penalize resumes with typos

## To-Dos:
- [ ] Figure out important features for resume scoring
- [ ] Figure out how to parse important sections of job description (Qualifications, Preferred Experience, Education Requirements, etc.)
- [ ] NER model for entity parsing?
- [ ] Use resume dataset to train/fine-tune ML model? Need to evaluate effectiveness of rule-based system

## Ideas
- [ ] Integrate with LinkedIn to pull additional candidate data
- [ ] Develop a scoring system to rank candidates based on job requirements
- [ ] Add resume optimization functionality
- [ ] Create web interface for user to upload resume and job description
- [ ] Allow user to add link to job description; need to crawl site to parse job description
- [ ] Make pretty: highlight keywords visually in resume when scanning
- [ ] Suggest jobs that the user's resume is a good fit for
- [ ] Persist user information to persist profile info and previous resume scans