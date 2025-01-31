import requests
from bs4 import BeautifulSoup

# URL of a sample job listing website
URL = "https://realpython.github.io/fake-jobs/"

# Fetch page content
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

# Extract job titles and links
jobs = soup.find_all("div", class_="card-content")
for job in jobs[:5]:  # Get first 5 jobs
    title = job.find("h2", class_="title").text.strip()
    company = job.find("h3", class_="company").text.strip()
    print(f"Job: {title}, Company: {company}")
