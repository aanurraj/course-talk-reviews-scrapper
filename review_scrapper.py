from bs4 import BeautifulSoup
import requests
import csv

with open('coursename.csv', newline='') as f:
    reader = csv.reader(f)
    course_list = list(reader)

csv_file = open('reviews.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Comments', 'rating'])

count = 30
total_courses = len(course_list)
course_number = 1
for course_number in range(1, len(course_list) + 1):
    print("########################################################################### S C R A P P I N G #################################################################################")
    print("Course Name: " + course_list[course_number][0] + "          Course Number: " + str(course_number) + "/" + str(total_courses))
    x = course_list[course_number][0]
    course = x.replace(" ", "-").lower()
    ur = 'https://www.coursetalk.com/providers/coursera/courses/' + course
    if requests.get(ur):
        sauce = requests.get(ur).text
    else:
        continue
    soup = BeautifulSoup(sauce, 'html.parser')
    temp = soup.find("div", {"class": "course-header-ng__rating__count"})
    number_of_reviews = temp.find_all("span")[1].text.split()
    print("Number of Reviews: " + number_of_reviews[0])
    number_of_pages = int(number_of_reviews[0]) // 30
    print("Number of Pages: " + str(number_of_pages))

    for page in range(1, number_of_pages + 1):
        print("Currently Scrapping Page Number: " + str(page) + "/" + str(number_of_pages) + "      Total Number of Reviews Scrapped: " + str(count))
        ur_course = 'https://www.coursetalk.com/providers/coursera/courses/an-introduction-to-interactive-programming-in-python?page=' + str(page) + '#incourse-reviews'
        sauce = requests.get(ur).text
        soup = BeautifulSoup(sauce, 'html.parser')

        for match in soup.find_all("div", {"class": "review js-review js-view-trackable"}):
            data = []
            rating = match.find("span", {"class": "sr-only"}).text.split("/")[0]
            comment = match.find("span", {"class": "more-less-trigger__text--full"}).text.strip()
            data.append(comment)
            data.append(rating)
            csv_writer.writerow([data[0], data[1]])
        count += 30
    course_number += 1











