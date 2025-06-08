from cookies import cookies
from bs4 import BeautifulSoup
import requests
import json

url="https://netfree2.cc/mobile/home"

def scrap(link,ott):
    # cookies.json file read karo (ye ek list of dicts hona chahiye)
    with open("cookies.json", "r") as f:
        cookies_list = json.load(f)
    # cookies ko dict format me convert karo (requests ke liye)
    # cookies = {cookie['name']: cookie['value'] for cookie in cookies_list}
    cookies_list["ott"]=ott
    response = requests.get(link, cookies=cookies_list)
    # Step 6: Parse using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Agar response sahi mila
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        body_tag = soup.body

        # Check karo ki body me data-hash attribute hai ya nahi
        if soup.body.has_attr("data-hash"):
            return soup
        else:
            print("data-hash attribute present nahi hai.")
            cookies()
            return scrap(url,ott)
    else:
        print(f"Request failed with status code: {response.status_code}")

if __name__ == "__main__":
    print(scrap(url,"pv").find_all("div",class_="tray-container"))
