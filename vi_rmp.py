import requests
from bs4 import BeautifulSoup
import time

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
}

def grab_rmp_data(professor_name, sid=124):
    """
    Returns:
    {
        "rating": float,
        "difficulty": float,
        "url": str
    }
    """
    base_search = "https://www.ratemyprofessors.com/search/professors/"
    params = {
        "q": professor_name,
        "sid": sid  # Boston University
    }

    # QUERY RATE MY PROFESSOR
    search_resp = requests.get(base_search, params=params, headers=HEADERS, timeout=10)
    soup = BeautifulSoup(search_resp.text, "html.parser")

    card = soup.find("a", href=lambda h: h and h.startswith("/professor/"))
    if not card:
        return {"rating": -1, "difficulty": -1, "url": ""}

    prof_url = "https://www.ratemyprofessors.com" + card["href"]

    # QUERY SPEC. PROFESSOR PAGE
    prof_resp = requests.get(prof_url, headers=HEADERS, timeout=10)
    prof_soup = BeautifulSoup(prof_resp.text, "html.parser")

    # ACCESS RATING
    ratingTag = prof_soup.find("div", class_ = "RatingValue__Numerator-qw8sqy-2 duhvlP")
    rating = ratingTag.text.strip() if ratingTag else -1
    
    # ACCESS 'WOULD TAKE AGAIN' VALUE AND DIFFICULTY
    feedbackTags = prof_soup.find_all("div", class_ = "FeedbackItem__FeedbackNumber-uof32n-1 ecFgca")
    feedbackTags = [feedbackTag.text.strip() for feedbackTag in feedbackTags]

    # goofy discriminant, if it has a % we assume its the 'percent would take again'  (jk its whichever one comes first)
    wouldTakeAgain, difficulty = feedbackTags[0], float(feedbackTags[1])
    
    return {
        "rating": rating,
        "wouldTakeAgain":wouldTakeAgain,
        "difficulty":difficulty,
        "url": prof_url
    }
start = time.time()
grab_rmp_data("Bunch")
end = time.time()
print(end-start)