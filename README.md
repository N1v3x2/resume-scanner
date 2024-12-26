# AI Resume Scanner

This is a tool to score resumes against a provided job description. The current workflow takes a candidate resume as a PDF and a job description as text input and outputs JSON containing an evaluation of the resume against the job description.

## Scoring Logic

Each resume is evaluated on six key aspects:

1. Experience (specifically, work experience)
2. Education
3. Skills
4. Projects
5. Leadership
6. Research

The step of the scoring workflow takes the job description and resume and calculates scores for each of the six sections that measure how resume's **relevance** to the job requirements and the resume's **impact** and **depth** of technical detail.

Each section receives a score between 0 and 5 based on this rubric:

| Score | Meaning |
|-------|---------|
| **0** | **Not Applicable / Missing**: No content provided, or the section is irrelevant to the job. |
| **1** | **Poor**: Content exists but is highly generic, irrelevant, or underdeveloped. Little to no measurable impact is demonstrated. |
| **2** | **Below Average**: Somewhat relevant but lacks depth or specificity. Minimal impact or achievements are demonstrated. |
| **3** | **Average**: Content is moderately relevant, with adequate detail. Some measurable impact or effort is evident, but not exceptional. |
| **4** | **Good**: Content is highly relevant, well-detailed, and demonstrates meaningful contributions or achievements. Could be improved slightly to reach exceptional quality. |
| **5** | **Excellent**: Content is exceptionally relevant, detailed, and impactful, showcasing strong alignment with job requirements and significant measurable outcomes. |

The second step of the scoring workflow takes the job description as input and assigns **relative weights** for each of the six resume aspects mentioned above (experience, education, skills, projects, leadership, and research).

Finally, based on the scores assigned in step one and step two, a final score between 0 and 1 is calculated as follows:

$$\begin{align*}
\text{final score}\ = \ &\text{experience score} \cdot \text{experience weight}\ + \\
& \text{education score} \cdot \text{education weight}\ + \\
& \text{skills score} \cdot \text{skills weight}\ + \\
& \text{projects score} \cdot \text{projects weight}\ + \\
& \text{leadership score} \cdot \text{leadership weight}\ + \\
& \text{research score} \cdot \text{research weight}
\end{align*}$$

A score of 1 indicates perfect alignment between the resume and job description, whereas a score of 0 indicates no alignment. The vast majority of resumes will fall somewhere in the middle. A score of $\geq 0.7$ typically indicates strong alignment, and scores $\geq 0.85$ typically indicate a standout applicant. Scores $< 0.4$ typically indicate that the resume and job description are in different industries.

## To-Dos:

- [x] Figure out important features for resume scoring
- [x] Figure out how to parse important sections of job description (Qualifications, Preferred Experience, Education Requirements, etc.)
- [x] Add resume feedback
- [ ] Serve backend services via REST API or GraphQL?
- [ ] Create web interface for user to upload resume and job description
- [ ] Host backend on Oracle Cloud via Docker containerization + Kubernetes

## Ideas

- [ ] Allow user to add link to job description; need to crawl site to parse job description
- [ ] Persist user information to persist profile info and previous resume scans
- [ ] Package frontend into chrome extension