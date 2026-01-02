import requests
import time
import re
from bs4 import BeautifulSoup
start_time = time.time()
import pandas as pd
# Course to scrape


def extractPrerequisites(description):
    match = re.search(
        r"Undergraduate Prerequisites:\s*(.+?)(?=(?:\.|\-|Undergraduate Corequisites|$))",
        description,
        flags=re.IGNORECASE | re.DOTALL
    )
    #match = re.search(r"Undergraduate Prerequisites:\s*(.+?)(?:[.\-]|$)", description, flags=re.IGNORECASE)
    if match:
        plainText = match.group(1).strip()
        plainText = plainText.replace("Undergraduate Prerequisites:", "").strip() #strip 'Undergraduate Prerequisites'
        plainText = plainText.upper()
        plainText = re.sub(r"[ \t\n().]", "", plainText)
        plainText = plainText.replace("ORCONSENTOFINSTRUCTOR", "")
        plainText = plainText.replace("ORCONSENTOFTHEINSTRUCTOR", "")
        plainText = plainText.replace("ORCONSENTOFINSTRUCTOR", "")
        plainText = plainText.replace("ORPERMISSIONOFINSTRUCTOR", "")
        plainText = plainText.replace("OREQUIVALENT", "")
        parts = re.split(r'\s*(?:AND|&|;)\s*', plainText, flags=re.IGNORECASE)
        parts = [p.strip() for p in parts]
        parts = [re.sub(r'OR', ' OR ', p) for p in parts]
        # include all schools!
        parts = [re.sub(r'CAS([A-Z]{2})(\d{3})', r'CAS \1 \2', p) for p in parts]
        parts = [re.sub(r'ENG([A-Z]{2})(\d{3})', r'ENG \1 \2', p) for p in parts]
        parts = [re.sub(r'CDS([A-Z]{2})(\d{3})', r'CDS \1 \2', p) for p in parts]
        return(parts)
    return('No prerequisites found')

def safeGet(list, index):
    if list == 'No prerequisites found':
        return("")
    if index < len(list):
        return(list[index])
    else:
        return("")
    
def courseData(courseCode, url):
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
    
    prerequisites = extractPrerequisites(descriptionText)
    course = {
        'Title': title,
        'Course Code': courseCode,
        'Prerequisite 1': safeGet(prerequisites, 0), # you could probably make this more efficient by looping through and setting dict to that value... but we're not THAT strapped for time
        'Prerequisite 2': safeGet(prerequisites, 1),
        'Prerequisite 3': safeGet(prerequisites, 2),
        'Prerequisite 4': safeGet(prerequisites, 3),
        'Prerequisite 5': safeGet(prerequisites, 4),
        'Description': descriptionText,
        #'Prerequisites': prerequisites # TEMPORARY FOR PRINTING CONVENIENCE
    }
    return(course)

courseList = [] #to be made into df and thus into an array
fastList = [100, 101, 102, 105, 107, 109, 202, 203, 311, 312, 401, 402, 413, 414, 441, 491, 492]
for courseNum in fastList:
    url = f"https://www.bu.edu/academics/cas/courses/cas-as-{courseNum}/"
    courseCode = 'CAS AS ' + str(courseNum)
    courseInfo = courseData(courseCode, url)
    if not courseInfo == False:
        courseList.append(courseInfo)
        print(courseInfo['Course Code'], courseInfo['Title'], 'Prerequisite 1', courseInfo['Prerequisite 1'])

df = pd.DataFrame(courseList)
df.to_csv('bu_astronomy_courses.csv', index = False)

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
