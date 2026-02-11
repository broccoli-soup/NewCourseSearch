import re 

def extract(plainText):
    plainText = plainText.replace("Undergraduate Prerequisites:", "").strip() #strip 'Undergraduate Prerequisites'
    plainText = plainText.upper()
    plainText = plainText.replace("CONSENT OF INSTRUCTOR", "")
    parts = re.split(r'\s*(?:AND|&)\s*', plainText, flags=re.IGNORECASE)
    parts = [p.strip() for p in parts]
    parts = [re.sub(r"[ \t\n().]", "", p) for p in parts]
    parts = [re.sub(r'OR', ' OR ', p) for p in parts]
    # include all schools!
    parts = [re.sub(r'CAS([A-Z]{2})(\d{3})', r'CAS \1 \2', p) for p in parts]
    parts = [re.sub(r'ENG([A-Z]{2})(\d{3})', r'CAS \1 \2', p) for p in parts]
    parts = [re.sub(r'CDS([A-Z]{2})(\d{3})', r'CAS \1 \2', p) for p in parts]
    print(parts)

# example of plainText is 'Undergraduate Prerequisites: CASMA 213 or CASMA 115 or CASMA 113 or CDSDS 120 or CASCS 237 or consent of instructor. - Students may receive credit for not more than one of the following courses: CASMA 116, MA 214, or MA 614. Inference about proportions, goodness of fit, student's t-distribution, tests for normality; two-sample comparisons, regression and correlation, tests for linearity and outliers, residual analysis, contingency tables, analysis of variance. Effective Fall 2018, this course fulfills a single unit in each of the following BU Hub areas: Quantitative Reasoning II, Teamwork/Collaboration. Effective Fall 2020, this course fulfills a single unit in each of the following BU Hub areas: Quantitative Reasoning II, Critical Thinking, Teamwork/Collaboration.'