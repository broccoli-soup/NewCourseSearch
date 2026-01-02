from datetime import datetime
import requests
from bs4 import BeautifulSoup

def findProfessorRMP(prof_name, school_id=124):
    query = prof_name.replace(" ", "+")
    url = f"https://www.ratemyprofessors.com/search/professors/?q={query}&sid={school_id}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the FIRST teacher card link
    teacher_link = soup.find("a", href=True, string=False)

    # Better: explicitly match professor URLs
    teacher_link = soup.find("a", href=lambda x: x and x.startswith("/professor/"))

    if not teacher_link:
        return None

    prof_url = "https://www.ratemyprofessors.com" + teacher_link["href"]
    return prof_url

def rating(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    rating_div = soup.find(
        "div",
        class_="RatingValue__Numerator-qw8sqy-2 duhvlP"
    )

    if rating_div:
        try:
            return float(rating_div.text.strip())
        except ValueError:
            return -1
    else:
        return -1
    
print(rating(findProfessorRMP("bunch")))
# # Example usage:
# prof_info = grab_rmp_data("Manher Jariwala")
# print(prof_info)
    
# MODIFIED VERSION OF BU V2 UNDERGRAD CODE 
# def rmpData(url):
#     """
#     Parse RateMyProfessors page HTML for rating & difficulty.
#     Expects a URL that contains avgRating / avgDifficulty in the HTML.
#     """
#     response = requests.get(url).text

#     data = {
#         "rating": -1,
#         "difficulty": -1,
#         "url": url
#     }

#     # Parse rating
#     if '"avgRating":' in response:
#         i = response.index('"avgRating":')
#         ss = response[i + 12 : i + 16]  # slightly safer slice
#         ss = ss.split(",")[0]
#         try:
#             data["rating"] = float(ss)
#         except:
#             pass

#     # Parse difficulty
#     if '"avgDifficulty":' in response:
#         i = response.index('"avgDifficulty":')
#         ss = response[i + 16 : i + 20]
#         ss = ss.split(",")[0]
#         try:
#             data["difficulty"] = float(ss)
#         except:
#             pass

#     return data

