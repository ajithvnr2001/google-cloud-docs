---
url: https://docs.cloud.google.com/storage/docs/xml-api/put-object/
title: PUT Object \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:37:47.602425+00:00
---

# PUT Object  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/put-object/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  PUT Object Stay organized with collections  Save and categorize content based on your preferences. 

Use a PUT object request to:

  * [Upload an Object](https://docs.cloud.google.com/storage/docs/xml-api/put-object-upload)
  * [Upload an Object Part](https://docs.cloud.google.com/storage/docs/xml-api/put-object-multipart)
  * [Copy an Object](https://docs.cloud.google.com/storage/docs/xml-api/put-object-copy)
  * [Compose an Object](https://docs.cloud.google.com/storage/docs/xml-api/put-object-compose)
  * [Set Object ACLs](https://docs.cloud.google.com/storage/docs/xml-api/put-object-acls)
  * [Set Object Retention](https://docs.cloud.google.com/storage/docs/xml-api/put-object-retention)



## Common request headers

The following are common request headers for PUT object requests.

Header | Description | Required  
---|---|---  
`[Authorization](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#authorization)` | The authentication string for the request. | Yes  
`[Content-Length](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentlength)` | The length of the request body without headers (in bytes). | Yes1  
`[Content-Type](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contenttype)`2 | The MIME type of the request body. If you do not specify a content type, Cloud Storage defaults to [`application/octet-stream`](https://datatracker.ietf.org/doc/html/rfc2046#section-4.5.1) when it serves the object. | No (recommended)  
`[Content-MD5](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentmd5)` | The MD5 digest of the request message without headers. While not required, this header is generally recommended as a data integrity check to verify that the data received by Cloud Storage is the same as the data that was intended to be sent. | No  
`[Date](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#date)` | The date and time of the request. | Yes  
`[Host](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#host)` | The URI for Cloud Storage. For more information, see [Request Endpoints](https://docs.cloud.google.com/storage/docs/request-endpoints). | Yes  
`[Transfer-Encoding](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#chunked)` | Indicates if the message body was chunked. In requests that use [V4 Signatures](https://docs.cloud.google.com/storage/docs/authentication/signatures) for their authentication, chunked uploads must also include the header `x-amz-decoded-content-length`. | No (except for requests that use chunked transfer encoding)  
`[x-goog-if-generation-match](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogifgenerationmatch)`2 | If the generation you specify is the same as the object you're replacing, then the object is replaced. You can also specify 0 as a special value to indicate that the new object is only created if there is no existing object. | No  
`[x-goog-if-metageneration-match](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogifmetagenerationmatch)`2 | If the metageneration you specify is the same as the object you're trying to update, then the object metadata is updated. This is only allowed if `x-goog-if-generation` is specified. By combining these two generation properties, you can implement safe read-modify-write updates. | No  
`[x-goog-storage-class](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogstorageclass)`2 | Gives an object a storage class besides the default storage class of the associated bucket. | No  
`[x-goog-user-project](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgooguserproject)` | The project to be billed for charges associated with the request. | No  
  
1 Not required for requests that use chunked transfer encoding.

2 This header is not applicable in `PUT Object` requests that [upload an object part](https://docs.cloud.google.com/storage/docs/xml-api/put-object-multipart).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
