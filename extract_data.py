import re

def extract_data(transcript):

    data = {
        "company_name": None,
        "business_hours": {},
        "services_supported": [],
        "emergency_definition": [],
        "questions_or_unknowns": []
    }

    lines = transcript.lower()

    if "sprinkler" in lines:
        data["services_supported"].append("sprinkler services")

    if "alarm" in lines:
        data["services_supported"].append("fire alarm services")

    if "sprinkler leak" in lines:
        data["emergency_definition"].append("sprinkler leak")

    if "fire alarm triggered" in lines:
        data["emergency_definition"].append("fire alarm triggered")

    hours_match = re.search(r'(\d{1,2})\s?am\s?to\s?(\d{1,2})\s?pm', lines)

    if hours_match:
        data["business_hours"] = {
            "start": hours_match.group(1) + "am",
            "end": hours_match.group(2) + "pm"
        }
    else:
        data["questions_or_unknowns"].append("business hours not specified")

    return data