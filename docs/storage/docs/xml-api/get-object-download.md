---
url: https://docs.cloud.google.com/storage/docs/xml-api/get-object-download/
title: Download an object \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:37:56.247534+00:00
---

# Download an object  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/get-object-download/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Download an object Stay organized with collections  Save and categorize content based on your preferences. 

Downloads an object.

GET requests for objects can include a Range header as defined in the HTTP 1.1 RFC to limit the scope of the returned data within the object, but be aware that in [certain circumstances](https://docs.cloud.google.com/storage/docs/transcoding#range) the range header is ignored.

Objects that are stored in Cloud Storage in a compressed state can be [automatically decompressed](https://docs.cloud.google.com/storage/docs/transcoding) as part of a download request when certain criteria are met. This _transcoding_ behavior eliminates the need for a requester to decompress the object.

Requests can also include If-Modified-Since or If-Unmodified-Since headers, causing the response to omit the body if the object has not been modified, or has been modified, since a specified timestamp. If the object does not meet an If- Modified-Since header condition, the response is a 304 Not Modified, and if the object fails to meet an If-Unmodified-Since header condition, the response is 412 Precondition Failed.

Similarly, requests can include If-Match and If-None- Match headers with an ETag to match. If the object does not match an If-Match header condition, the response is 412 Precondition Failed, and if the object matches the given hash in an If-None-Match header, the response is 304 Not Modified.

See the [Downloading Objects](https://docs.cloud.google.com/storage/docs/downloading-objects) guide for instructions on how to download an object.

## Query string parameters

Parameter | Description | Required  
---|---|---  
`[generation](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#generation)` | You can use this if you want to fetch a specific object version. | No  
  
See [signed URL query string parameters](https://docs.cloud.google.com/storage/docs/authentication/canonical-requests#required-query-parameters) for information on the parameters you include when creating and using [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).

## Request headers

In addition to [common request headers](https://docs.cloud.google.com/storage/docs/xml-api/get-object#request-headers), the following can be used.

Header | Description | Required  
---|---|---  
`[If-Match](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#ifmatch)` | An entity tag (ETag). If the ETag you specify is the same as the ETag for the object, then the object is downloaded. | No  
`[If-Modified-Since](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#ifmodifiedsince)` | A date and time. If the object has been modified later than the date and time you specify, then the object is downloaded. | No  
`[If-None-Match](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#ifnonematch)` | An entity tag (ETag). If the ETag you specify is different from the ETag for the object, then the object is downloaded. | No  
`[If-Unmodified-Since](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#ifunmodifiedsince)` | A date and time. If the object has not been modified later than the date you specify, then the object is downloaded. | No  
`[Range](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#range)` | An object's range (in bytes) that you want to download. **Warning:** The checksum(s) returned when downloading data from Cloud Storage cover the complete object content. Thus, if you specify a request range there's no way to detect data corruption for that byte range alone. We therefore recommend using range requests only for restarting the download of a full object after the last received offset, because in that case you can compute and validate the checksum when the full download completes.  | No  
`[x-goog-if-generation-match](https://docs.cloud.google.com/storage/docs/reference-headers#xgoogifgenerationmatch)` | In order for the request to succeed, the value you specify for this header must match the [generation](https://docs.cloud.google.com/storage/docs/metadata#generation-number) of the object you're requesting. If it does not, the request fails with a `412 Precondition Failed` status code. Also see the [generation query parameter](https://docs.cloud.google.com/storage/docs/reference-headers#generation). | No  
`[x-goog-if-metageneration-match](https://docs.cloud.google.com/storage/docs/reference-headers#xgoogifmetagenerationmatch)` | In order for the request to succeed, the value you specify for this header must match the [metageneration](https://docs.cloud.google.com/storage/docs/metadata#generation-number) of the object you're requesting. If it does not, the request fails with a `412 Precondition Failed` status code. | No  
  
To download an object encrypted by a customer-supplied encryption key, use the [headers listed on the Encryption page](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys#headers) in your request.

## Request body elements

This request does not include an XML document in the request body.

## Request syntax

The following syntax applies to GET Object requests that don't use the `acl` query string parameter.
    
    
    GET /OBJECT_NAME HTTP/1.1
    Host: BUCKET_NAME.storage.googleapis.com
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

The response contains the object data.

## Example

The following example downloads an object named paris.jpg that's in a bucket named travel-maps.

**Request**
    
    
    GET /paris.jpg HTTP/1.1
    Host: travel-maps.storage.googleapis.com
    Content-Length: 0
    Authorization: Bearer ya29.AHES6ZRVmB7fkLtd1XTmq6mo0S1wqZZi3-Lh_s-6Uw7p8vtgSwg
    

**Response**
    
    
    HTTP/1.1 200 OK
    Content-Type: image/jpg
    Last-Modified: Fri, 19 Feb 2010 22:13:49 GMT
    ETag: "2281880ef78388266ecd7d4c1b472a0e"
    Content-Length: 328
    Date: Fri, 19 Feb 2010 22:13:49 GMT
    
    328 bytes of data...
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
