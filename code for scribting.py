#  ايمبورت كل المكاتب المستخدمة
import requests
from bs4 import BeautifulSoup as Soup
import csv

# حدد البيانات المراد اخراجة لملف ال (سي اس في) وعينها ك لست فارغة
job_title = []
job_skill = []
company_name = []
location_city = []

# احضر المصدر الا وهو رابط صفحة ويب
The_Source = requests.get("https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&q=python")

# احفظة  محتوى الصفحة ك متغير
all_data = The_Source.content

# فلتر  الداتا من الكود البرجي
soup = Soup(all_data, "lxml")

#  قسم الداتا الى فات تريدها واحفظ كل منها ك متغير وتخلى عن الباقي
job_titles = soup.find_all("h2", {"class": "css-m604qf"})
job_skills = soup.find_all("div", {"class": "css-y4udm8"})
company_names = soup.find_all("a", {"class": "css-17s97q8"})
locations_city = soup.find_all("span", {"class": "css-5wys0k"})

# استخرج من كل قسم (التكست فقط) و انقلها الى اللست الفارغة
for a in range(len(job_titles)):
    job_title.append(job_titles[a].text)
    job_skill.append(job_skills[a].text)
    company_name.append(company_names[a].text)
    location_city.append(locations_city[a].text)

# انشاء او افتح ملف (سي اس في) لنقل البيانات فيه
with open("C:.......", "w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow([" job title ", " job skill ", " company name ", " location city "])
    for w in range(len(job_title)):
        wr.writerow([job_title[w], job_skill[w], company_name[w], location_city[w]])

print("DONE")
