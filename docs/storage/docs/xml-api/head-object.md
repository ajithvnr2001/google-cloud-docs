---
url: https://docs.cloud.google.com/storage/docs/xml-api/head-object/
title: HEAD Object \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:37:48.270285+00:00
---

# HEAD Object  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/head-object/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  HEAD Object Stay organized with collections  Save and categorize content based on your preferences. 

Lists metadata for an object.

If the object does not exist, Cloud Storage returns a [404 Not Found](https://docs.cloud.google.com/storage/docs/xml-api/reference-status) status code.

## Query string parameters

Parameter | Description | Required  
---|---|---  
`[generation](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#generation)` | You can use this if you want to fetch a specific object generation. | No  
  
See [signed URL query string parameters](https://docs.cloud.google.com/storage/docs/authentication/canonical-requests#required-query-parameters) for information on the parameters you include when creating and using [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).

## Request headers

Header | Description | Required  
---|---|---  
`[Authorization](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#authorization)` | The authentication string for the request. | Yes  
`[Content-Length](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentlength)` | The length of the request body without headers (in bytes). | No  
`[Date](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#date)` | The date and time of the request. | No  
`[Host](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#host)` | The URI for Cloud Storage. For more information, see [Request Endpoints](https://docs.cloud.google.com/storage/docs/request-endpoints). | Yes  
`[If-Match](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#ifmatch)` | An entity tag (ETag). If the ETag you specify is the same as the ETag for the object, then the metadata is returned. | No  
`[If-Modified-Since](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#ifmodifiedsince)` | A date and time. If the object has been modified later than the date and time you specify, then the metadata is returned. | No  
`[If-None-Match](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#ifnonematch)` | An entity tag (ETag). If the ETag you specify is different from the ETag for the object, then the metadata is returned. | No  
`[If-Unmodified-Since](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#ifunmodifiedsince)` | A date and time. If the object has not been modified later than the date you specify, then the metadata is returned. | No  
`[Range](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#range)` | Including this header causes the response to contain a [`Content-Range`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentrange) header. However, since HEAD Object requests don't contain a response body, the `Range` header doesn't otherwise have an effect on the request. | No  
`[x-goog-if-generation-match](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogifgenerationmatch)` | If the generation you specify is the same as the generation for the object, then the metadata is returned. | No  
`[x-goog-if-metageneration-match](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogifmetagenerationmatch)` | If the metageneration you specify is the same as the metageneration for the object, then the metadata is returned. | No  
`[x-goog-user-project](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgooguserproject)` | The project to be billed for charges associated with the request. | No  
  
## Request body elements

This request does not include an XML document in the request body.

## Request syntax
    
    
    HEAD /OBJECT_NAME HTTP/1.1
    Host: BUCKET_NAME.storage.googleapis.com
    Date: DATE
    Content-Length: 0
    Authorization: AUTHENTICATION_STRING
    Range: bytes=BYTE_RANGE
    If-Match: ENTITY_TAG
    If-Modified-Since: DATE
    If-None-Match: ENTITY_TAG
    If-Unmodified-Since: DATE
    

## Response headers

The request can return a variety of response headers depending on the request headers you use, including: [Cache-Control](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#cachecontrol), [Content-Length](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentlength), [Content-Type](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contenttype), [Content-Disposition](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentdisposition), [ETag](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#etag), and [Last-Modified.](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#lastmodified)

## Response body elements

The response does not include an XML document in the response body. Error responses to HEAD requests also do not contain a response body.

## Example

The following sample gets metadata for an object named `paris.jpg` that's in a bucket named `travel-maps`.

**Request**
    
    
    HEAD /paris.jpg HTTP/1.1
    Host: travel-maps.storage.googleapis.com
    Authorization: Bearer ya29.AHES6ZRVmB7fkLtd1XTmq6mo0S1wqZZi3-Lh_s-6Uw7p8vtgSwg
    

**Response**
    
    
    ...
    expires: Wed, 30 May 2018 21:41:23 GMT
    date: Wed, 30 May 2018 21:41:23 GMT
    cache-control: private, max-age=0
    last-modified: Wed, 30 May 2018 20:36:34 GMT
    etag: "2218880ef78838266ecd7d4c1b742a0e"
    x-goog-generation: 1486161811706000
    x-goog-metageneration: 15
    x-goog-stored-content-encoding: identity
    x-goog-stored-content-length: 328
    content-type: image/jpg
    x-goog-hash: crc32c=HBrbzQ==
    x-goog-hash: md5=OCydg52+pPG1Bwawjsl7DA==
    x-goog-storage-class: STANDARD
    accept-ranges: bytes
    content-length: 328
    ...
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
