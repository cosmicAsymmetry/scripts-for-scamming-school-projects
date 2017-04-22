import requests
from datetime import date
from bs4 import BeautifulSoup as bs

pages = ["https://www.inshorts.com/en/read/politics",
         "https://www.inshorts.com/en/read/sports", "https://www.inshorts.com/en/read/technology"]
for link in pages:
    if link == "https://www.inshorts.com/en/read/politics":
        numberOfStories = 4
    elif link == "https://www.inshorts.com/en/read/sports":
        numberOfStories = 1
    else:
        numberOfStories = 2
    page = requests.get(link)
    soup = bs(page.content, 'html.parser')
    headlines = soup.findAll("span", {"itemprop": "headline"})[
        0:numberOfStories]
    articleBodies = soup.findAll("div", {"itemprop": "articleBody"})[
        0:numberOfStories]
    source = soup.findAll("a", {"class": "source"})[0:numberOfStories]
    n = 0
    today = date.today()
    with open("/home/sidhant/Documents/random_scripts/inshorts_scraping/"+str(today.day)+"."+str(today.month)+"."+str(today.year)+".md", "a") as f:
        f.write("\n")
        f.write("# " + str(today.day) + "/" +
                str(today.month) + "/" + str(today.year))
        f.write("\n")
        if numberOfStories == 4:
            f.write("## Politics")
        elif numberOfStories == 1:
            f.write("## Sports")
        else:
            f.write("## technology")
        f.write("\n")
        while n < numberOfStories:
            headline = str(headlines[n])[26:][:-7]
            f.write("\n")
            f.write("### " + headline)
            f.write("\n")
            articleBody = str(articleBodies[n])[28:][:-5]
            f.write("\n")
            f.write(articleBody)
            f.write("\n")
            f.write("Source: " + str(source[n]))
            f.write("\n")
            n += 1
        print(str(today.day) + "/" + str(today.month) + "/" + str(today.year))

        f.close()
