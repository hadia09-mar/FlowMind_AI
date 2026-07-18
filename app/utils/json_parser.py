import json
import re


def parse_json_response(response: str) -> dict:
    """
    Safely parse JSON returned by Gemini.
    """

    response = re.sub(r"^```json", "", response.strip())
    response = re.sub(r"```$", "", response.strip())

    return json.loads(response.strip())