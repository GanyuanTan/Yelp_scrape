import requests
from bs4 import BeautifulSoup

base_url = "https://www.yelp.com/search?find_desc=&find_loc="
loc = input("Enter your location: ")
current_page = 0
print("Trying to pulling items...")


inp = ''
while inp != 'n':
	print("Loading Page: ", current_page, "...")

	#url init
	url = base_url + loc + "&start=" + str(current_page)
	url_req = requests.get(url)

	#only access when return 200
	if url_req.status_code == 200:
		url_soup = BeautifulSoup(url_req.text, 'html.parser')

		#lookup the current div
		class_name = 'lemon--li__373c0__1r9wz border-color--default__373c0__3-ifU'
		business = url_soup.findAll('li', {class_name})

		#print the title in the current div
		for card in range(len(business)):
			if card != 1:
				for title in business[card].findAll('a', {'lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE'}):
					print(title.text)

	inp = input("Press ENTER to countinue or type 'n' to EXIT...\n")

	current_page += 10