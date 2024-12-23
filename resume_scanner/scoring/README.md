# Scoring

### Important features
1. Keywords match job description
2. Validate that skills are used in context ("built Flask app with Python" vs "Python" on its own)
3. Match sentences under "Projects" and "Experience" to the job description
4. Match job titles with job description
5. Determine number of years of relevant experience
6. Education: check degree & GPA
7. Check that resume has essential sections (contact info, skills, experience, education)
8. Penalize resumes with typos

### Potential approaches
1. Deep learning-based (PyTorch)
2. LLM (ideally a reasoning model) + structured output
3. Semantic similarity