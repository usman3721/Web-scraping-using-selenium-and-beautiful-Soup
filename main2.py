from bs4 import BeautifulSoup
import requests
html_text=requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35")
web_page=html_text.text
soup=BeautifulSoup(web_page,'html.parser')
job_list=soup.find("li", class_= "clearfix job-bx wht-shd-bx")
company_name=job_list.find("h3", class_="joblist-comp-name").text.replace(' ','')
skills=soup.find("span", class_= "srp-skills").text.replace(' ','')
print(f'Company_name={company_name} \n Required_skill={skills}')

