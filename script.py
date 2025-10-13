from serpapi import GoogleSearch

def get_rmp_link(professor_name, school_name, api_key):
    query = f"{professor_name} {school_name} site:ratemyprofessors.com"

    params = {
        "q": query,
        "api_key": api_key,
        "engine": "google",
        "num": 5
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    for result in results.get("organic_results", []):
        link = result.get("link", "")
        if "ratemyprofessors.com/ShowRatings.jsp" in link or "ratemyprofessors.com/professor/" in link:
            print(f"Found: {link}")
            return link

    print("No RateMyProfessors link found.")
    return None

api_key = "e3d642a41b646a0443a810234f97f5233518a6a4a17d5b2bfbf126200ebcc542"
get_rmp_link("Ryan Goh", "Boston University", api_key)
