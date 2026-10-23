---
url: https://docs.cloud.google.com/storage/docs/xml-api/head-bucket/
title: HEAD Bucket \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:17:43.869102+00:00
---

# HEAD Bucket  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/head-bucket/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  HEAD Bucket Stay organized with collections  Save and categorize content based on your preferences. 

Indicates if a bucket exists and whether the requester has READ access to it.

If you make a HEAD request that's scoped to a bucket that doesn't exist, you will get a [404 Not Found](https://docs.cloud.google.com/storage/docs/xml-api/reference-status) status code.

## Query string parameters

This request does not typically include query string parameters.

See [signed URL query string parameters](https://docs.cloud.google.com/storage/docs/authentication/canonical-requests#required-query-parameters) for information on the parameters you include when creating and using [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).

## Request headers

Header | Description | Required  
---|---|---  
`[Authorization](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#authorization)` | The authentication string for the request. | Yes  
`[Content-Length](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentlength)` | The length of the request body without headers (in bytes). | No  
`[Date](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#date)` | The date and time of the request. | No  
`[Host](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#host)` | The URI for Cloud Storage. For more information, see [Request Endpoints](https://docs.cloud.google.com/storage/docs/request-endpoints). | Yes  
`[x-goog-user-project](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgooguserproject)` | The project to be billed for charges associated with the request. | No  
  
## Request body elements

This request does not include an XML document in the request body.

## Request syntax
    
    
    HEAD / HTTP/1.1
    Host: BUCKET_NAME.storage.googleapis.com
    Date: DATE
    Content-Length: 0
    Authorization: AUTHENTICATION_STRING
    

## Response headers

The request returns standard response headers.

## Response body elements

The response does not include an XML document in the response body. Error responses to HEAD requests also do not contain a response body.

## Example

The following sample shows a HEAD request for a bucket named `travel-maps`.

**Request**
    
    
    HEAD / HTTP/1.1
    Host: travel-maps.storage.googleapis.com
    Authorization: Bearer ya29.AHES6ZRVmB7fkLtd1XTmq6mo0S1wqZZi3-Lh_s-6Uw7p8vtgSwg
    

**Response**
    
    
    HTTP/1.1 200 OK
    ...
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
