---
url: https://docs.cloud.google.com/appengine/docs/standard/services/mail/mail-with-headers-attachments/
title: Mail with headers or attachments \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:44:05.651388+00:00
---

# Mail with headers or attachments  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/mail/mail-with-headers-attachments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Mail with headers or attachments Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

When you send mail using the [Mail API](https://docs.cloud.google.com/appengine/docs/standard/services/mail), there are some restrictions on the headers that you can use and the types of files you can attach.

## Optional headers

An outgoing email has headers that provide details about the message, such as the sender, recipient, date, and subject. Each header has a name and a value. You can also include the following headers in an outgoing email; for security purposes, other headers are not allowed:

  * In-Reply-To
  * List-Id
  * List-Unsubscribe
  * On-Behalf-Of
  * References
  * Resent-Date
  * Resent-From
  * Resent-To



## Mail with attachments

An outgoing email message can have file attachments. Each attachment has a filename and file data. The file data can come from any source, such as an application data file or the datastore.

### Filename extensions that are prohibited

As a security measure to protect against viruses, email attachments cannot use the following filename extensions, and ZIP files cannot contain files with the following filename extensions:

  * ade
  * adp
  * bat
  * chm
  * cmd
  * com
  * cpl
  * exe
  * hta
  * ins
  * isp
  * jse
  * lib
  * mde
  * msc
  * msp
  * mst
  * pif
  * scr
  * sct
  * shb
  * sys
  * vb
  * vbe
  * vbs
  * vxd
  * wsc
  * wsf
  * wsh



### Attachments and Multipurpose Internet Mail Extensions (MIME) types

The MIME type of an attachment is determined from the file's extension. The MIME type identifies the type of content that is being sent, and can determine how that data is transferred.

The following is a list of MIME types and their corresponding filename extensions. You are not limited to these extensions, but if you use an unknown extension, App Engine will assign it the MIME type `application/octet-stream`.

MIME type | Filename extensions  
---|---  
application/msword | doc, docx  
application/pdf | pdf  
application/rss+xml | rss  
application/vnd.google-earth.kml+xml | kml  
application/vnd.google-earth.kmz | kmz  
application/vnd.ms-excel | xls, xlsx  
application/vnd.ms-powerpoint | pps, ppt, pptx  
application/vnd.oasis.opendocument.presentation | odp  
application/vnd.oasis.opendocument.spreadsheet | ods  
application/vnd.oasis.opendocument.text | odt  
application/vnd.sun.xml.calc | sxc  
application/vnd.sun.xml.writer | sxw  
application/x-gzip | gzip  
application/zip | zip  
audio/basic | au snd  
audio/flac | flac  
audio/mid | mid, rmi  
audio/mp4 | m4a  
audio/mpeg | mp3  
audio/ogg | oga, ogg  
audio/x-aiff | aif, aifc, aiff  
audio/x-wav | wav  
image/gif | gif  
image/jpeg | jpeg, jpg, jpe  
image/png | png  
image/tiff | tiff, tif  
image/vnd.wap.wbmp | wbmp  
image/x-ms-bmp | bmp  
text/calendar | ics  
text/comma-separated-values | csv  
text/css | css  
text/html | htm, html  
text/plain | asc, c, diff, log, patch, pot, text, txt  
text/x-vcard | vcf  
video/mp4 | mp4  
video/mpeg | mpeg, mpg, mpe  
video/ogg | ogv  
video/quicktime | qt, mov  
video/x-msvideo | avi  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
