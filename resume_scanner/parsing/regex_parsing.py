import re

def parse_phone_number(text: str) -> str:
    phone_pattern = re.compile(r"""
        (?:\+(?P<country_code>1)+\s)?   # Match country code (if exists)
        (?:\()?
        (?P<area_code>\d{3})            # Match area code (first 3 digits)
        (?:[.-]|\)\s?)
        (?P<prefix>\d{3})               # Match prefix (second 3 digits)
        [.-]
        (?P<line_number>\d{4})          # Match line number (last 4 digits)
    """, re.VERBOSE)
    match = re.search(phone_pattern, text)
    if match:
        return f"{match.group("area_code")}-{match.group("prefix")}-{match.group("line_number")}"
    return ""

def parse_email(text: str) -> str:
    email_pattern = re.compile(r"""
        \b
        [A-Za-z0-9._%+-]+   # Local part
        @
        [A-Za-z0-9.-]+      # Domain 
        \.[A-Za-z]{2,}
        \b
    """, re.VERBOSE)
    match = re.search(email_pattern, text)
    if match:
        return match.group()
    return ""

def parse_linkedin(text: str) -> str:
    linkedin_pattern = r"(?:(?:https://)?(?:www.)?linkedin.com/in/(?P<profile_id>[A-Za-z0-9-]{5,30})/?\b)"
    match = re.search(linkedin_pattern, text)
    if match:
        return f"https://linkedin.com/in/{match.group("profile_id")}"
    return ""

def parse_github(text: str) -> str:
    github_pattern = r"(?:(?:https://)?(?:www.)?github.com/(?P<username>[A-Za-z0-9-]{1,39})/?\b)"
    match = re.search(github_pattern, text)
    if match:
        return f"https://github.com/{match.group("username")}"
    return ""

def parse_personal_info(resume: str) -> dict:
    return {
        "Phone": parse_phone_number(resume),
        "Email": parse_email(resume),
        "LinkedIn": parse_linkedin(resume),
        "GitHub": parse_github(resume),
    }