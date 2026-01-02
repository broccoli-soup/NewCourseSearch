from datetime import datetime
import requests
import base64

def grab_rmp_data(professor_name):
    """
    Fetch RateMyProfessors rating and difficulty for a given professor.
    Returns a dict: {"rating": float, "difficulty": float, "url": str}
    """
    bu_school_id = 124  # BU's RMP school ID
    # Encode the URL correctly
    prof_query = professor_name.replace(" ", "%20")
    school_encoded = base64.b64encode(f"School-{bu_school_id}".encode('ascii')).decode('ascii')
    
    url = f"https://www.ratemyprofessors.com/search/teachers?query={prof_query}&sid={school_encoded}"
    
    response = requests.get(url).text
    data = {"rating": -1, "difficulty": -1, "url": url}

    # Parse rating
    if '"avgRating":' in response:
        i = response.index('"avgRating":')
        ss = response[i+12:i+15]
        if "," in ss:
            ss = ss[0:1]
        data["rating"] = float(ss)

    # Parse difficulty
    if '"avgDifficulty":' in response:
        i = response.index('"avgDifficulty":')
        ss = response[i+16:i+19]
        if "," in ss:
            ss = ss[0:1]
        data["difficulty"] = float(ss)
    
    return data

# Example usage:
prof_info = grab_rmp_data("Christine Papadakis")
print(prof_info)