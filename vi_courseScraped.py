import requests
import time
from bs4 import BeautifulSoup
start_time = time.time()
# Course to scrape


def courseData(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Course title
    h1_tags = soup.find_all("h1") # find all <h1> tags
    title = 'No title found'
    for h1 in h1_tags:
        text = h1.text.strip()
        if "Uh Oh, Page Not Found." in text:
            return(0)
        if "Boston University Academics" not in text:
            title = text

    p_tags = soup.find_all("p")
    descriptionParas = [p.text.strip() for p in p_tags if "Boston University" not in p.text]
    descriptionText = " ".join(descriptionParas)
    
    course = {
        'Title': title,
        'Description': descriptionText
    }

    return(course)
for courseCode in range(100, 1000):
    url = f"https://www.bu.edu/academics/cas/courses/cas-ma-{courseCode}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    # Course title
    h1_tags = soup.find_all("h1") # find all <h1> tags
    title = 'No title found'
    for h1 in h1_tags:
        text = h1.text.strip()
        if "Boston University Academics" not in text:
            title = text

    p_tags = soup.find_all("p")
    descriptionParas = [p.text.strip() for p in p_tags if "Boston University" not in p.text]
    descriptionText = " ".join(descriptionParas)
    
    course = {
        'Title': title,
        'Description': descriptionText
    }

for course_code in [242, 226, 225, 411, 116, 113, 115, 511, 512]:
    url = f"https://www.bu.edu/academics/cas/courses/cas-ma-{course_code}/"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    # Course title
    h1_tags = soup.find_all("h1") # find all <h1> tags
    for h1 in h1_tags:
        text = h1.text.strip()
        if "Boston University Academics" not in text:
            print("Course heading:", text)

    p_tags = soup.find_all("p")
    description_paras = [p.text.strip() for p in p_tags if "Boston University" not in p.text]
    description_text = " ".join(description_paras)
    print(description_text[:500], "...")  # print first 500 chars
    print("\n" + "-"*60 + "\n")


# # Description (first <p> inside content div or fallback)
desc_tag = soup.find("div", class_="content") or soup.find("p")
description = desc_tag.text.strip() if desc_tag else "No description found."

# # Prerequisites
# prereq = "None"
# for p in soup.find_all("p"):
#     if "Prerequisite" in p.text or "Prereq" in p.text:
#         prereq = p.text.strip()
#         break

# # Credits (look for the word "credit")
# credits = "Unknown"
# for p in soup.find_all("p"):
#     if "credit" in p.text.lower():
#         credits = p.text.strip()
#         break

# # Output
# course_info = {
#     "title": title,
#     "description": description,
#     "prerequisites": prereq,
#     "credits": credits,
#     "url": url
# }

# end_time = time.time()
# elapsed = end_time - start_time
# print(f"Elapsed time: {elapsed:.6f} seconds")

#print(course_info['title'])
