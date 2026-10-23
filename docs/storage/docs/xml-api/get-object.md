---
url: https://docs.cloud.google.com/storage/docs/xml-api/get-object/
title: GET Object \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:17:43.124532+00:00
---

# GET Object  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/get-object/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  GET Object Stay organized with collections  Save and categorize content based on your preferences. 

Use a GET object request to:

  * [Download an object](https://docs.cloud.google.com/storage/docs/xml-api/get-object-download)
  * [List the uploaded parts of an object](https://docs.cloud.google.com/storage/docs/xml-api/get-object-multipart)
  * [List object ACLs](https://docs.cloud.google.com/storage/docs/xml-api/get-object-acls)
  * [Get an object's encryption information](https://docs.cloud.google.com/storage/docs/xml-api/get-object-encryption)
  * [Get an object's retention configuration](https://docs.cloud.google.com/storage/docs/xml-api/get-object-retention)



You **should not** use a GET object request to retrieve general object metadata, because doing so incurs charges associated with downloading the entire object. Use a [HEAD object](https://docs.cloud.google.com/storage/docs/xml-api/head-object) request instead.

To download an object you make a GET request that is scoped to a bucket and object. You can also use various request headers to further scope the request. The request returns the object's contents in the response body. To list an object's ACLs you make a GET request that is scoped to a bucket and object and you use the `acl` query string parameter. The ACLs are returned in an XML document in the response body.

If you make a GET request for an object that doesn't exist, you get a [404 Not Found](https://docs.cloud.google.com/storage/docs/xml-api/reference-status) status code and the body of the error response contains `NoSuchKey` in the `Code` element.

## Common request headers

The following are common request headers for GET object requests.

Header | Description | Required  
---|---|---  
`[Authorization](https://docs.cloud.google.com/storage/docs/reference-headers#authorization)` | The authentication string for the request. Required for objects without public read access. | Maybe  
`[Host](https://docs.cloud.google.com/storage/docs/reference-headers#host)` | The URI for Cloud Storage. For more information, see [Request Endpoints](https://docs.cloud.google.com/storage/docs/request-endpoints). | Yes  
`[x-goog-user-project](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgooguserproject)` | The project to be billed for charges associated with the request. | No  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
