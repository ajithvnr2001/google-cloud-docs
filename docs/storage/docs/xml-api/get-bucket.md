---
url: https://docs.cloud.google.com/storage/docs/xml-api/get-bucket/
title: GET Bucket \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:37:39.267697+00:00
---

# GET Bucket  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/get-bucket/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  GET Bucket Stay organized with collections  Save and categorize content based on your preferences. 

Use a GET bucket request to:

  * [List Objects](https://docs.cloud.google.com/storage/docs/xml-api/get-bucket-list) contained in a bucket
  * [List Multipart Uploads](https://docs.cloud.google.com/storage/docs/xml-api/get-bucket-uploads) underway in a bucket
  * [Get Bucket ACLs](https://docs.cloud.google.com/storage/docs/xml-api/get-bucket-acls)
  * [Get Bucket Metadata](https://docs.cloud.google.com/storage/docs/xml-api/get-bucket-metadata)



If you make a GET request that's scoped to a bucket that doesn't exist, you get a [404 Not Found](https://docs.cloud.google.com/storage/docs/xml-api/reference-status) status code, and the body of the error response contains `NoSuchBucket` in the `Code` element.

## Common request headers

The following are common request headers for GET bucket requests.

Header | Description | Required  
---|---|---  
`[Authorization](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#authorization)` | The authentication string for the request. | Yes  
`[Content-Length](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentlength)` | The length of the request body without headers (in bytes). * Not required for requests that use chunked transfer encoding. | Yes*  
`[Date](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#date)` | The date and time of the request. | Yes  
`[Host](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#host)` | The URI for Cloud Storage. For more information, see [Request Endpoints](https://docs.cloud.google.com/storage/docs/request-endpoints). | Yes  
`[x-goog-if-metageneration-match](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogifmetagenerationmatch)` | For the request to succeed, the value specified for this header must match the [metageneration](https://docs.cloud.google.com/storage/docs/bucket-metadata#non-editable) of the requested bucket. If it does not, the request fails with a `412 Precondition Failed` status code. Note that this header is ignored in list requests. | No  
`[x-goog-user-project](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgooguserproject)` | The project to be billed for charges associated with the request. | No  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
