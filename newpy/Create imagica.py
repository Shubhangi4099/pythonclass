#Import Libraries
import urllib.request    #urllib for Extracting web pages
import time       #Importing the time library to check the time of code execution


#This list is used to search keywords. You can edit this list to search for google images of your choice. You can simply add and remove elements of the list.
search_keyword = ['Taj Mahal', 'Pyramid of Giza']

#This list is used to further add sufix to your search term. Each element of the list will help you download 100 images. First element is blank which denotes that no sufix is added to the search keyword of the above list. You can edit the list by adding/deleting elements from it.
keywords = ['','%20high%20resolution','%20paintings','%20at%20night','%20from%20top']


#Downloading entire Web Document (Raw Page Content)
def download_page(url):
    try:
        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
        req = urllib.request.Request(url, headers = headers)
        resp = urllib.request.urlopen(req)
        respData = str(resp.read())
        return respData
    except Exception as e:
        print(str(e))


#Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_di"')
        start_content = s.find('imgurl=',start_line+1)
        end_content = s.find('&amp;',start_content+1)
        content_raw = str(s[start_content+7:end_content])
        return content_raw, end_content


#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            #time.sleep(0.1)  #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items


############## Main Program ############
t0 = time.time()   #start the timer

#Download Image Links
i= 0
while i<len(search_keyword):
    items = []
    iteration = "Item no.: " + str(i+1) + " -->" + " Item name = " + str(search_keyword[i])
    print (iteration)
    search_keywords = search_keyword[i]
    search = search_keywords.replace(' ','%20')
    j = 0
    while j<len(keywords):
        url = 'https://www.google.com/search?q=' + search + keywords[j] + '&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg'
        #print(url)
        raw_html =  (download_page(url))
        #time.sleep = 0.1
        items = items + (_images_get_all_items(raw_html))
        j = j + 1
    print ("Image Links = "+str(items))
    print ("Total Image Links = "+str(len(items)))
    print ("\n")
    i = i+1


    #This allows you to write all the links into a test file. This text file will be created in the same directory as your code. You can comment out the below 3 lines to stop writing the output to the text file.
    info = open('output.txt', 'a')        #Open the text file called database.txt
    info.write(str(i) + ': ' + str(search_keyword[i-1]) + ": " + str(items) + "\n\n\n")         #Write the title of the page
    info.close()                            #Close the file

t1 = time.time()    #stop the timer
total_time = t1-t0   #Calculating the total time required to crawl, find and download all the links of 60,000 images
print("Total time taken: "+str(total_time)+" Seconds")

#----End of the program ----#