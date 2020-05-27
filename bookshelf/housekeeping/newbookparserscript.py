#a script to read new book info from a csv file into relevant list variables; it then inputs them into a new-book html format by reading and rewriting it line-by-line to another html file. The # of book-placeholder must match the # of books to input. 
import csv

csvfile = open("C:/Users/bluer/Dropbox/ABC Analytics/Website/books/abc_csv.txt", "r", encoding="utf-8") #the csv file to scan book data from
readfile = open("C:/Users/bluer/Dropbox/ABC Analytics/Website/books/abooks.html", "r", encoding="utf-8") #the new-book placeholder 
writefile = open("C:/Users/bluer/Dropbox/ABC Analytics/Website/books/otherstatisticsbooks.html", "w", encoding="utf-8") #the new-book file, final output

csvreader = csv.reader(csvfile, quotechar='"') #wrap csvfile in csvreader

#to return the left whitespaces of this line
def getLeftIndent(thisline):
    leftIndentNumber = len(thisline) - len(thisline.lstrip())
    return (" " * leftIndentNumber)

titles = [] #list variables to store data read from csvfile
links = []
images = []
authors =[]

for row in csvreader: #reading the csv file and storing info into list variables
    if not row:
        continue
    try:
        titles.append(row[0])
        links.append(row[1])
        images.append(row[2])
        authors.append(row[3])
    except:
        print("Error occured in processing: ")
        print(row)
        
csvfile.close() #done with the csv file

line = readfile.readline()
previousline = line 
ibook = -1 #counter for books

#loop through the placeholder file and writing it to another file with book data added
while (not "</html>" in line): #until EOF signaled by </html>
    
    if ("--book image--" in line):
        ibook = ibook + 1 #working on a new book, increment the counter
        writefile.write(line)
        writefile.write(getLeftIndent(line) + images[ibook])
    elif ("--book title--" in line):
        writefile.write(line)
        writefile.write(getLeftIndent(line) +  titles[ibook])
    elif ("--book author--" in line):
        writefile.write(line)
        writefile.write(getLeftIndent(line) +  authors[ibook])
    elif ( ("href" in line) and ("--link to book file--" in previousline) ):
        writefile.write(line)
        writefile.write(getLeftIndent(line) +  links[ibook])
    else: 
        writefile.write(line)
    
    previousline = line
    line = readfile.readline()

writefile.write(line) #the last line which includes </html>
readfile.close()
writefile.flush()
writefile.close()
print("new html file successfully created")
