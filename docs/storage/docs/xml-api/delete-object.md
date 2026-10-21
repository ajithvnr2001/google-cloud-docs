---
url: https://docs.cloud.google.com/storage/docs/xml-api/delete-object/
title: DELETE Object \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:47.279280+00:00
---

# DELETE Object  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/delete-object/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  DELETE Object Stay organized with collections  Save and categorize content based on your preferences. 

Deletes an object.

If you make a DELETE request for an object that doesn't exist, you will get a [404 Not Found](https://docs.cloud.google.com/storage/docs/xml-api/reference-status) status code and the body of the error response will contain `NoSuchKey` in the `Code` element.

## Query string parameters

Parameter | Description | Required  
---|---|---  
`[generation](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#generation)` | You can use this if you want to delete a specific object generation. If this query parameter is used on a versioned bucket and the generation specified is the live version of the object, the version does not become a noncurrent version of the object, but instead is deleted completely. | No  
  
See [signed URL query string parameters](https://docs.cloud.google.com/storage/docs/authentication/canonical-requests#required-query-parameters) for information on the parameters you include when creating and using [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).

## Request headers

Header | Description | Required  
---|---|---  
`[Authorization](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#authorization)` | The authentication string for the request. | Yes  
`[Content-Length](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentlength)` | The length of the request body without headers (in bytes). * Not required for requests that use chunked transfer encoding. | Yes*  
`[Date](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#date)` | The date and time of the request. | Yes  
`[Host](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#host)` | The URI for Cloud Storage. For more information, see [Request Endpoints](https://docs.cloud.google.com/storage/docs/request-endpoints). | Yes  
`[x-goog-if-generation-match](https://docs.cloud.google.com/storage/docs/reference-headers#xgoogifgenerationmatch)` | In order for the request to succeed, the value you specify for this header must match the [generation](https://docs.cloud.google.com/storage/docs/metadata#generation-number) of the object you're requesting. If it does not, the request fails with a `412 Precondition Failed` status code. | No  
`[x-goog-if-metageneration-match](https://docs.cloud.google.com/storage/docs/reference-headers#xgoogifmetagenerationmatch)` | In order for the request to succeed, the value you specify for this header must match the [metageneration](https://docs.cloud.google.com/storage/docs/metadata#generation-number) of the object you're requesting. If it does not, the request fails with a `412 Precondition Failed` status code. | No  
`[x-goog-user-project](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgooguserproject)` | The project to be billed for charges associated with the request. | No  
  
## Request body elements

This request does not include an XML document in the request body.

## Request syntax
    
    
    DELETE /OBJECT_NAME HTTP/1.1
    Host: BUCKET_NAME.storage.googleapis.com
    Date: DATE
    Content-Length: 0
    Authorization: AUTHENTICATION_STRING
    

## Response headers

The request can return a variety of response headers depending on the request headers you use.

## Response body elements

The response does not include an XML document in the response body.

## Example

The following sample deletes an object named paris.jpg.

**Request**
    
    
    DELETE /paris.jpg HTTP/1.1
    Host: travel-maps.storage.googleapis.com
    Date: Mon, 15 Feb  2010 11:00:00 GMT
    Content-Length: 0
    Authorization: Bearer ya29.AHES6ZRVmB7fkLtd1XTmq6mo0S1wqZZi3-Lh_s-6Uw7p8vtgSwg
    

**Response**
    
    
    HTTP/1.1 204 No Content
    Date: Mon, 15 Feb  2010 11:00:01 GMT
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
