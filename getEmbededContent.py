import httplib  
import urllib
from sys import argv
import re

# Open connection to domain
conn = httplib.HTTPConnection("www.dickssportinggoods.com", port=80)

#inputs. URLS.txt is the list of URLs on domain wwww.site-x.com
file_name = "URLS.txt"
fileOpen = open(file_name)
write_file = "URLlist.txt"
file_text = ""
tempStr=""
#count is optional. I use it to check that the script is running
count=1

#HTTPConnection.request(method, url[, body[, headers]])
params = urllib.urlencode({})
procesing_num =0

print "\r\nStarting process... \r\n\r\n"

#you can uncomment the print below  to look at how the script is working
for line in fileOpen:
	print count
	count=count+1
	url_path =  line[0:-1] 
	headers = {"Pragma": "akamai-x-cache-on,akamai-x-get-cache-key,akamai-x-get-cache-key"}
	conn.request("GET", url_path, params, headers)	
	response = conn.getresponse()   
	data = response.read()
	#print data
	urls = re.findall('''http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|
                      [!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+''', data)
	#print urls
	tempStr=str(urls)
	file_text=file_text + "\r\n" + tempStr	
	#print file_text
	conn.close()

file_text=file_text.replace("['", "")
file_text=file_text.replace("']", "")
file_text=file_text.replace("', '", "\r\n")
#print file_text

#write results and save it
writeResult = open(write_file, 'w')
writeResult.truncate()
writeResult.write(file_text)
writeResult.close()
