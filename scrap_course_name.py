from bs4 import BeautifulSoup
import requests
import csv
import string


csv_file = open('coursename.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['course_name'])
table = str.maketrans(dict.fromkeys(string.punctuation))
for i in range(1, 1847):
    ur = 'https://www.coursetalk.com/providers/edx/courses?filters=platform:acumen,alison,canvas-network,careerfoundry,carone-academy,code-school,codecademy,coder-manual,coggno,coursera,craftsy,datacamp,duke-continuing-studies,eazl,ed2go,edcast,edraak,edx,emma,filtered,first-business-mooc,france-universite-numerique,futurelearn,fx-academy,gacco,goskills,iai-academy,international-telematic-university-uninettuno,international-writing-program,iversity,janux-interactive-learning-community,jobs-to-be-done,k-12,kadenze,khan-academy,lynda,middlebury-interactive-languages,miriada-x,mit,mongodb-university,mooc-ed,mruniversity,novoed,one-million-by-one-million,one-month,open2study,openhpi,openlearning,opensap,peer-2-peer-university,pluralsight,research-education-association,sally-ride-science,saylor,skillshare,smartly,sophia,stanford-online,straighterline,techchange,textile-learning,the-great-courses,thinkful,treehouse,tuts,udacity,udemy,university-of-tasmania&page=' + str(i) + '&sort=-rating'
    sauce = requests.get(ur).text
    soup = BeautifulSoup(sauce, 'html.parser')

    match = soup.find("div", {"class": "course-listing-summary__name"})

    print("####### S C R A P P I N G #######     Scrapping page " + str(i) + " of 1847     ####### S C R A P P I N G #######")

    for match in soup.find_all("div", {"class": "course-listing-summary__name"}):
        data = []
        name = match.find("span", {"itemprop": "name"}).text
        name = name.strip()
        # name.translate(str.maketrans('', '', string.punctuation))
        name = name.translate(table)
        data.append(name)
        csv_writer.writerow([data[0]])

