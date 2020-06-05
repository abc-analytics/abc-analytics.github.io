#a script to parse old html file for each book title and box file link, save them to a new csv file, which will later be used to feed into new html format
import csv

old = open("C:/Users/bluer/Dropbox/ABC Analytics/Website/books/deprecated version/otherstatbook.html", "r", encoding="utf-8") #the old html file to parse
new = open("C:/Users/bluer/Dropbox/ABC Analytics/Website/books/abc_csv.txt", "w", encoding="utf-8") #the new csv file to save

#function identifying, extracting and returning the link portion of a line input
def linkSearch(thisline):
	     substart = "https://app.box"
	     subend = '"'
	     substartindex = thisline.index(substart)
	     subendindex = thisline.index(subend, substartindex, len(thisline))
	     return thisline[substartindex:subendindex]

#function identifying, extracting and returning the title portion of a line input
def titleSearch(thisline):
	     substart = "_blank"
	     subenda = "</a>"
	     subendb = "</B>"
	     subendu = "</U>"
	     substartindex = thisline.index(substart) + 8
	     subendindexa = thisline.index(subenda)
	     subendindexb = thisline.index(subendb)
	     subendindexu = thisline.index(subendu)
	     subendindex = min(subendindexa, subendindexb, subendindexu)
	     return thisline[substartindex:subendindex].strip()

line = "" #initiation  to empty string
titles = [] #titles list
links = [] #links list

#loop through the old file to extract the containing book titles and links
while (not "Back</a>" in line): #until reaching Back</a> at the bottom of file
    line = old.readline()
    if ("app.box.com" in line):  #app.box.com signals presence of book title and link in this line
        try:
            title = titleSearch(line)
            link = linkSearch(line)
            titles.append(title)
            links.append(link)
        except ValueError:
            print ("Error incurred in: " + line)

        
#write the extracted titles and links to a csv file
writer = csv.writer(new)
for (i, t) in enumerate(titles):
	writer.writerow([t, links[i]])


new.flush()
old.close()
new.close()
print("csv file successfully created")
