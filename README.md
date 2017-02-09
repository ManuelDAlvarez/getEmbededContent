# getEmbededContent
Get a all embedded URLs from a list of URLs you want to analyze

How to run it?

$ python getEmbededContent.py



The python scrip takes a text file as an input with a list of URLs separated by new line. The requiriments is that all the URLs on the input file are from the same domain you are connecting to.


At this moment you need to edit the script to add the domain you want to connect to. I want to make it more dynamic on a future release but I did not have time now. If you want to branch it an update that, be my guess!

Line to update: Replace wwww.site-x.com with your domain on the below line

  conn = httplib.HTTPConnection("wwww.site-x.com", port=80)



URLS.txt would look something like

http://wwww.site-x.com/

http://wwww.site-x.com/c/apparel-deals

http://wwww.site-x.com/c/this-weeks-deals

http://wwww.site-x.com/s/footwear



Note: I took the Regex from https://github.com/oelu/get_urls. I could not make that code run so I created my own script 
