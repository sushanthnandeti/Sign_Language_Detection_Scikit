import requests
from bs4 import BeautifulSoup

url = "https://tns4lpgmziiypnxxzel5ss5nyu0nftol.lambda-url.us-east-1.on.aws/challenge"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

result = []

for section in soup.find_all("section"):
    data_id = section.get("data-id", "")
    if not data_id.startswith("92"):  # loosen pattern a bit
        continue

    # find all articles instead of just the first one
    for article in section.find_all("article"):
        data_class = article.get("data-class", "")
        if not data_class.endswith("45"):
            continue

        for div in article.find_all("div"):
            data_tag = div.get("data-tag", "")
            if "78" not in data_tag:
                continue

            for b_tag in div.find_all("b", class_="ref"):
                if b_tag.has_attr("value"):
                    result.append(b_tag["value"])

url_hidden = "".join(result)
print("Hidden URL:", url_hidden)