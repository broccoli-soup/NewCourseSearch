import requests
import time
import re
from bs4 import BeautifulSoup
start_time = time.time()
# Course to scrape


def extractPrerequisites(description):
    match = re.search(r"Undergraduate Prerequisites:\s*(.+?)(?:[.\-;]|$)", description, flags=re.IGNORECASE)
    if match:
        plainText = match.group(1).strip()
        plainText = plainText.replace("Undergraduate Prerequisites:", "").strip() #strip 'Undergraduate Prerequisites'
        plainText = plainText.upper()
        plainText = re.sub(r"[ \t\n().]", "", plainText)
        plainText = plainText.replace("ORCONSENTOFINSTRUCTOR", "")
        parts = re.split(r'\s*(?:AND|&)\s*', plainText, flags=re.IGNORECASE)
        parts = [p.strip() for p in parts]
        parts = [re.sub(r'OR', ' OR ', p) for p in parts]
        # include all schools!
        parts = [re.sub(r'CAS([A-Z]{2})(\d{3})', r'CAS \1 \2', p) for p in parts]
        parts = [re.sub(r'ENG([A-Z]{2})(\d{3})', r'CAS \1 \2', p) for p in parts]
        parts = [re.sub(r'CDS([A-Z]{2})(\d{3})', r'CAS \1 \2', p) for p in parts]
        return(parts)
    return('No prerequisites found')

def courseData(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Course title
    h1_tags = soup.find_all("h1") # find all <h1> tags
    title = 'No title found'
    for h1 in h1_tags:
        text = h1.text.strip()
        if "Uh Oh, Page Not Found." in text:
            return(False)
        if "Boston University Academics" not in text:
            title = text

    p_tags = soup.find_all("p")
    descriptionParas = [p.text.strip() for p in p_tags if "Boston University" not in p.text]
    descriptionText = " ".join(descriptionParas)
    
    course = {
        'Title': title,
        'Description': descriptionText,
        'Prerequisites': extractPrerequisites(descriptionText)
    }

    return(course)

fastList = [214, 225, 226, 230, 231, 242, 294, 301, 341, 401, 402, 411, 412, 415, 416, 433, 442, 491, 492, 505, 511, 512, 531, 532, 539, 541, 542, 555, 556, 561, 562, 563, 564, 565, 568, 569, 570, 571, 573, 575, 576, 577, 578, 579, 581, 581, 582, 583, 584, 585, 586, 588, 589, 592]
for courseCode in fastList:
    url = f"https://www.bu.edu/academics/cas/courses/cas-ma-{courseCode}/"
    courseInfo = courseData(url)
    if not courseInfo == False:
        print('CAS MA', str(courseCode), courseInfo['Title'], 'Prerequisites:', courseInfo['Prerequisites'])

# for courseCode in range(100, 1000):
#     url = f"https://www.bu.edu/academics/cas/courses/cas-ma-{courseCode}/"
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "html.parser")
#     # Course title
#     h1_tags = soup.find_all("h1") # find all <h1> tags
#     title = 'No title found'
#     for h1 in h1_tags:
#         text = h1.text.strip()
#         if "Boston University Academics" not in text:
#             title = text

#     p_tags = soup.find_all("p")
#     descriptionParas = [p.text.strip() for p in p_tags if "Boston University" not in p.text]
#     descriptionText = " ".join(descriptionParas)
    
#     course = {
#         'Title': title,
#         'Description': descriptionText
#     }

# for course_code in [242, 226, 225, 411, 116, 113, 115, 511, 512]:
#     url = f"https://www.bu.edu/academics/cas/courses/cas-ma-{course_code}/"

#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "html.parser")
#     # Course title
#     h1_tags = soup.find_all("h1") # find all <h1> tags
#     for h1 in h1_tags:
#         text = h1.text.strip()
#         if "Boston University Academics" not in text:
#             print("Course heading:", text)

#     p_tags = soup.find_all("p")
#     description_paras = [p.text.strip() for p in p_tags if "Boston University" not in p.text]
#     description_text = " ".join(description_paras)
#     print(description_text[:500], "...")  # print first 500 chars
#     print("\n" + "-"*60 + "\n")


# # # Description (first <p> inside content div or fallback)
# desc_tag = soup.find("div", class_="content") or soup.find("p")
# description = desc_tag.text.strip() if desc_tag else "No description found."

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
