from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CORE_DIR = BASE_DIR / "core"
TEMPLATES_DIR = CORE_DIR / "templates"
PARSING_TEMPLATES_DIR = TEMPLATES_DIR / "parsing"
SCORING_TEMPLATES_DIR = TEMPLATES_DIR / "scoring"

##### Prompt templates #####
INITIAL_EXTRACTION_TXT = PARSING_TEMPLATES_DIR / "initial_extraction.txt"
EDUCATION_EXTRACTION_TXT = PARSING_TEMPLATES_DIR / "education_extraction.txt"
EXPERIENCE_EXTRACTION_TXT = PARSING_TEMPLATES_DIR / "experience_extraction.txt"
LEADERSHIP_EXTRACTION_TXT = PARSING_TEMPLATES_DIR / "leadership_extraction.txt"
PROJECTS_EXTRACTION_TXT = PARSING_TEMPLATES_DIR / "projects_extraction.txt"
RESEARCH_EXTRACTION_TXT = PARSING_TEMPLATES_DIR / "research_extraction.txt"
SKILLS_EXTRACTION_TXT = PARSING_TEMPLATES_DIR / "skills_extraction.txt"
FINAL_SCORING_TXT = SCORING_TEMPLATES_DIR / "final_scoring.txt"
WEIGHT_ASSIGNMENT_TXT = SCORING_TEMPLATES_DIR / "weight_assignment.txt"