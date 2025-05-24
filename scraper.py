import requests
from bs4 import BeautifulSoup
import json

base_url = "https://kishanptl34.github.io/kishan-goyani-portfolio/"

pages = {
    "1": ("Index", "index.html"),
    "2": ("Education", "portfolio/Education.html"),
    "3": ("Achievements", "portfolio/certificate.html"),
    "4": ("Experience", "portfolio/experience.html"),
    "5": ("About", "portfolio/about.html")
}

print("\nSelect a page to scrape:\n")
for key, (label, _) in pages.items():
    print(f"{key}. {label}")
print()  # extra newline after menu

choice = input("Enter the number (1-5): ").strip()
selected_entry = pages.get(choice)

if not selected_entry:
    print("\n❌ Invalid choice. Please run the script again.\n")
    exit()

display_name, path = selected_entry
full_url = base_url + path
print(f"\n🔗 Fetching: {full_url}\n")

tag = input("Enter the HTML tag to scrape (e.g. h1, p, div): ").strip()
attr = input(
    "Enter the attribute (e.g. class, id) [press Enter to skip]: ").strip()
value = input("Enter the attribute value [press Enter to skip]: ").strip()

try:
    response = requests.get(full_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    if attr and value:
        elements = soup.find_all(tag, {attr: value})
    elif attr:
        elements = soup.find_all(tag, attrs={attr: True})
    else:
        elements = soup.find_all(tag)

    results = [
        el.get_text(strip=True) for el in elements if el.get_text(strip=True)
    ]

    with open('scraped_data.json', 'w') as json_file:
        json.dump({f"{tag}_elements": results}, json_file, indent=2)

    with open('scraped_data.txt', 'w') as txt_file:
        txt_file.write("\n".join(results))

    print(f"\n✅ Scraped {len(results)} element(s) from {display_name}.")
    print("✅ Saved to 'scraped_data.json' and 'scraped_data.txt'.\n")

except Exception as e:
    print(f"\n❌ Error: {e}\n")
