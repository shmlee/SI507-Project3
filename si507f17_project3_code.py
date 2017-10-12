from bs4 import BeautifulSoup
import unittest
import requests
import csv


#########
## Instr note: the outline comments will stay as suggestions, otherwise it's too difficult.
## Of course, it could be structured in an easier/neater way, and if a student decides to commit to that, that is OK.

## NOTE OF ADVICE:
## When you go to make your GitHub milestones, think pretty seriously about all the different parts and their requirements, and what you need to understand. Make sure you've asked your questions about Part 2 as much as you need to before Fall Break!


######### PART 0 #########

# Write your code for Part 0 here.
try:
	kitty_data = open("gallery.html",'r').read()
except:
	kitty_data = requests.get("http://newmantaylor.com/gallery.html").text #get response object that represents the literal text
	f = open("gallery.html",'w') #these three lines open up an file and save it, don't have to open up the data all the time, file object
	f.write(kitty_data)
	f.close()

soup = BeautifulSoup(kitty_data, 'html.parser')
# print(soup)

all_imgs = soup.find_all('img')
for text in all_imgs:
	print(text.get('alt',"No alternative text provided!"))
######### PART 1 #########

# Get the main page data...

# Try to get and cache main page data if not yet cached
# Result of a following try/except block should be that
# there exists a file nps_gov_data.html,
# and the html text saved in it is stored in a variable 
# that the rest of the program can access.

# We've provided comments to guide you through the complex try/except, but if you prefer to build up the code to do this scraping and caching yourself, that is OK.
try:
	nps_gov_data = open("nps_gov_data.html",'r').read()
except:
	nps_gov_data = requests.get("https://www.nps.gov/index.htm").text
	f = open("nps_gov_data.html",'w') 
	f.write(nps_gov_data)
	f.close()

park_soup = BeautifulSoup(nps_gov_data, 'html.parser')
# print(park_soup)

states_dropdown = park_soup.find("ul",{"class":"dropdown-menu SearchBar-keywordSearch"})
# print (states_dropdown)


states_links = states_dropdown.find_all("a")
# print (states_links)
# print (park_soup.find('a', href = True, text = "Michigan"))


three_states = ['Arkansas','California','Michigan']
three_links = [park_soup.find('a', text = states)['href'] for states in three_states]
count = 0
for state in three_links:
	link = "https://www.nps.gov" + state
	# print (link)
	try:
		park_data = open(link,'r').read()
	except:
		park_data = requests.get(link).text
		# print(park_data)
		name_state = str(three_states[count]) 
		name = name_state.lower() + "_data.html"
		f = open(name,'w') 
		f.write(park_data)
		f.close()
		soup_name = BeautifulSoup(park_data, "html.parser")
		# print (NationalSite(soup_name))
		count +=1
		

# print (three_links)

arkansas_data = open("arkansas_data.html",'r').read()
arkansas_soup = BeautifulSoup(arkansas_data, 'html.parser')
# print(park_soup)
california_data = open("california_data.html", 'r').read()
california_soup = BeautifulSoup(california_data, 'html.parser')

michigan_data = open("michigan_data.html", 'r').read()
michigan_soup = BeautifulSoup(michigan_data, 'html.parser')

# Get individual states' data...

# Result of a following try/except block should be that
# there exist 3 files -- arkansas_data.html, california_data.html, michigan_data.html
# and the HTML-formatted text stored in each one is available
# in a variable or data structure 
# that the rest of the program can access.

# TRY: 
# To open and read all 3 of the files

# But if you can't, EXCEPT:

# Create a BeautifulSoup instance of main page data 
# Access the unordered list with the states' dropdown

# Get a list of all the li (list elements) from the unordered list, using the BeautifulSoup find_all method

# Use a list comprehension or accumulation to get all of the 'href' attributes of the 'a' tag objects in each li, instead of the full li objects

# Filter the list of relative URLs you just got to include only the 3 you want: AR's, CA's, MI's, using the accumulator pattern & conditional statements


# Create 3 URLs to access data from by appending those 3 href values to the main part of the NPS url. Save each URL in a variable.


## To figure out what URLs you want to get data from (as if you weren't told initially)...
# As seen if you debug on the actual site. e.g. Maine parks URL is "http://www.nps.gov/state/me/index.htm", Michigan's is "http://www.nps.gov/state/mi/index.htm" -- so if you compare that to the values in those href attributes you just got... how can you build the full URLs?


# Finally, get the HTML data from each of these URLs, and save it in the variables you used in the try clause
# (Make sure they're the same variables you used in the try clause! Otherwise, all this code will run every time you run the program!)


# And then, write each set of data to a file so this won't have to run again.







######### PART 2 #########

## Before truly embarking on Part 2, we recommend you do a few things:

# - Create BeautifulSoup objects out of all the data you have access to in variables from Part 1
# - Do some investigation on those BeautifulSoup objects. What data do you have about each state? How is it organized in HTML?

# HINT: remember the method .prettify() on a BeautifulSoup object -- might be useful for your investigation! So, of course, might be .find or .find_all, etc...

# HINT: Remember that the data you saved is data that includes ALL of the parks/sites/etc in a certain state, but you want the class to represent just ONE park/site/monument/lakeshore.

# We have provided, in sample_html_of_park.html an HTML file that represents the HTML about 1 park. However, your code should rely upon HTML data about Michigan, Arkansas, and Califoria you saved and accessed in Part 1.

# However, to begin your investigation and begin to plan your class definition, you may want to open this file and create a BeautifulSoup instance of it to do investigation on.

# Remember that there are things you'll have to be careful about listed in the instructions -- e.g. if no type of park/site/monument is listed in input, one of your instance variables should have a None value...





## Define your class NationalSite here:
def get_park_list(state_soup):
 	soup_list = state_soup.find("ul", {"id":"list_parks"}).find_all("li", {"class":"clearfix"})
 	return soup_list

  
class NationalSite(object):
	def __init__(self, park_soup):
		try:
			self.location = park_soup.find("h4").get_text()
			self.name = park_soup.find("h3").get_text()
			self.type = park_soup.find("h2").get_text()
			links = park_soup.find_all("a")[2]
			self.url = links['href']
			# self.links = park_soup.find_all("a")[2]["href"]
			self.description = park_soup.find("p").get_text()
		except:
			self.type = None
			self.description = None

		# print (links)

	def __str__(self):
	 	return "{} | {}".format(self.name, self.location)


	def __contains__(self, any_name):
		return any_name in self.name

	def get_mailing_address(self):
		try:
			info = requests.get(self.url).text
			info_soup = BeautifulSoup(info, 'html.parser')
			info_div = info_soup.find('div', {'itemprop':'address'})
			address_div = info_div.find('span', {'itemprop':'streetAddress'}).text.strip()
			locality = info_div.find('span', {'itemprop':'addressLocality'}).text.strip()
			region = info_div.find('span', {'itemprop':'addressRegion'}).text.strip()
			zipcode = info_div.find('span', {'itemprop':'postalCode'}).text.strip()
			mailing_address = address_div + "/" + region + "/" + zipcode
			return mailing_address 
		except:
			return ""


		print (mailing_address)

# sample_cal = get_park_list(california_soup)[2]	
# sample_test = NationalSite(sample_cal)
# info = requests.get(sample_test.url).text
# info_soup = BeautifulSoup(info, 'html.parser')	
# info_div = info_soup.find('div', {'itemprop':'address'})
# address_div = info_div.find('span', {'itemprop':'streetAddress'}).text.strip()
# locality = info_div.find('span', {'itemprop':'addressLocality'}).text.strip()
# region = info_div.find('span', {'itemprop':'addressRegion'}).text.strip()
# zipcode = info_div.find('span', {'itemprop':'postalCode'}).text.strip()
# mailing_address = address_div + "/" + region + "/" + zipcode
# print (mailing_address)




## Recommendation: to test the class, at various points, uncomment the following code and invoke some of the methods / check out the instance variables of the test instance saved in the variable sample_inst:

# f = open("sample_html_of_park.html",'r')
# soup_park_inst = BeautifulSoup(f.read(), 'html.parser') # an example of 1 BeautifulSoup instance to pass into your class
# sample_inst = NationalSite(soup_park_inst)
# f.close()


######### PART 3 #########

# Create lists of NationalSite objects for each state's parks.

# HINT: Get a Python list of all the HTML BeautifulSoup instances that represent each park, for each state.

ark_list = get_park_list(arkansas_soup)
arkansas_natl_sites = NationalSite(ark_list)

arkansas_natl_sites = []
for item in ark_list:
	ark_object = NationalSite(item)
	arkansas_natl_sites.append(ark_object)
	# print (arkansas_natl_sites)


cal_list = get_park_list(california_soup)
california_natl_sites = NationalSite(cal_list)

california_natl_sites = []
for item in cal_list:
	cal_object = NationalSite(item)
	california_natl_sites.append(cal_object)
	# print (california_natl_sites)


mic_list = get_park_list(michigan_soup)
michigan_natl_sites = NationalSite(mic_list)

michigan_natl_sites = []
for item in mic_list:
	mic_object = NationalSite(item)
	michigan_natl_sites.append(mic_object)
	# print (michigan_natl_sites)







##Code to help you test these out:
# for p in california_natl_sites:
# 	print(p)
# for a in arkansas_natl_sites:
# 	print(a)
# for m in michigan_natl_sites:
# 	print(m)



######### PART 4 #########
with open('arkansas.csv', 'w', newline='') as f:
	writer = csv.writer(f)
	f.write("Name, Location, Type, Address, Description\n")
	for obj in arkansas_natl_sites:
		writer.writerow([obj.name, obj.location, obj.type, obj.get_mailing_address(), obj.description])

with open('california.csv', 'w', newline='') as f:
	writer = csv.writer(f)
	f.write("Name, Location, Type, Address, Description\n")
	for obj in california_natl_sites:
		writer.writerow([obj.name, obj.location, obj.type, obj.get_mailing_address(), obj.description])

with open('michigan.csv', 'w', newline='') as f:
	writer = csv.writer(f)
	f.write("Name, Location, Type, Address, Description\n")
	for obj in michigan_natl_sites:
		writer.writerow([obj.name, obj.location, obj.type, obj.get_mailing_address(), obj.description])

## Remember the hints / things you learned from Project 2 about writing CSV files from lists of objects!

## Note that running this step for ALL your data make take a minute or few to run -- so it's a good idea to test any methods/functions you write with just a little bit of data, so running the program will take less time!

## Also remember that IF you have None values that may occur, you might run into some problems and have to debug for where you need to put in some None value / error handling!

