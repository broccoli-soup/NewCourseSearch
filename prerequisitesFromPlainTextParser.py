import re 

plainText = 'Undergraduate Prerequisites: CASMA 213 or CASMA 115 or CASMA 113 or CDSDS 120 or CASCS 237 or consent of instructor.'
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
# Math, chemistry, english, history, french, economics, computer science, biology, physics, political science, philosophy
print(parts)