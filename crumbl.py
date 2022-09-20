import requests
from bs4 import BeautifulSoup
import datetime
import TwitterAuth

data = requests.get('https://crumblcookies.com/')
data.encoding = 'utf-8'
soup = BeautifulSoup(data.text, 'html.parser')

# Finds 'ul' element in HTML that contains the weekly flavors.
flavor_list = soup.find('ul', {'id' : "weekly-cookie-flavors"}) 
 
# List of cookie flavors.
cookies = []

todaysDate = datetime.datetime.now()
todaysDate = todaysDate.strftime("%c")

# Strips text from the 'h3' element where the flavors are located, appends to 'cookies' list.
for individual_flavors in flavor_list.find_all('h3'):
    cookies.append(individual_flavors.get_text())


# Outputs list values to a text file
with open('crumbl-cookie-flavors.txt', 'w', encoding="utf-8") as f:
    f.write("Crumbl Cookie flavors as of %s \n-------------------\n\n" % todaysDate)
    for index, x in enumerate(cookies):
        new_cookie_line = (x)
        f.write(new_cookie_line)
        f.write("\n")
    f.write("\n-------------------\n https://crumblcookies.com/" )


TwitterAuth.CrumblBot()

