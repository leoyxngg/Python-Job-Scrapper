import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

search = input("Enter a key word to show related jobs: ").lower()
searchJobs = results.find_all(
    "h2", string=lambda text: search in text.lower()
)
jobElements = [
    h2_element.parent.parent.parent for h2_element in searchJobs
]
for job in jobElements:
    title = job.find("h2", class_="title")
    company = job.find("h3", class_="company")
    location = job.find("p", class_="location")
    link_url = job.find_all("a")[1]["href"]
    print()
    print(title.text.strip())
    print(company.text.strip())
    print(location.text.strip())
    print(f"Apply here: {link_url}\n")