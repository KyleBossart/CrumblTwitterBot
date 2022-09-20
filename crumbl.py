import requests
from bs4 import BeautifulSoup


data = requests.get('https://crumblcookies.com/')
soup = BeautifulSoup(data.text, 'html.parser')

# Finds 'ul' element in HTML that contains the weekly flavors.
flavor_list = soup.find('ul', {'id' : "weekly-cookie-flavors"}) 
 
# List of cookie flavors.
cookies = []

# List of descriptions
descriptions = [] 


# Strips text from the 'h3' element where the flavors are located, appends to 'cookies' list.
for individual_flavors in flavor_list.find_all('h3'):
    cookies.append(individual_flavors.get_text())

# Strips text from the 'p' element where the descriptions are located, appends to 'descriptions' list.
for individual_descriptions in flavor_list.find_all('p'):
    descriptions.append(individual_descriptions.get_text())


# Creates dictionary of key = 'cookies' and value = 'descriptions'
final_cookies = dict(zip(cookies, descriptions))

# Outputs dictinoary values to a text file
with open('readme.txt', 'w') as f:
    for index, (key, value) in enumerate(final_cookies.items()):
        test =  str((key, value))
        f.write(test)
        f.write("\n")











