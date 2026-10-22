---
url: https://docs.cloud.google.com/storage/docs/xml-api/put-bucket/
title: PUT Bucket \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:37:39.850589+00:00
---

# PUT Bucket  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/put-bucket/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  PUT Bucket Stay organized with collections  Save and categorize content based on your preferences. 

Creates a bucket in a specified project, sets the ACL for an existing bucket, or modifies the metadata for an existing bucket. You can only apply one configuration setting per request.

Use a PUT bucket request to:

  * [Create a Bucket](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-create)
  * [Set Bucket ACLs](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-acls)
  * [Set Bucket Metadata](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-metadata)

**Note:** Bucket configuration changes may take time to propagate. For more information, see [Consistency](https://docs.cloud.google.com/storage/docs/consistency).

## Common request headers

The following are common request headers for PUT bucket requests.

Header | Description | Required  
---|---|---  
`[Authorization](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#authorization)` | The authentication string for the request. | Yes  
`[Content-Length](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentlength)` | The length of the request body without headers (in bytes). * Not required for requests that use chunked transfer encoding. | Yes*  
`[Content-Type](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contenttype)` | The MIME type of the request body. | No  
`[Date](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#date)` | The date and time of the request. | Yes  
`[Host](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#host)` | The URI for Cloud Storage. For more information, see [Request Endpoints](https://docs.cloud.google.com/storage/docs/request-endpoints). | Yes  
`[x-goog-user-project](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgooguserproject)` | The project to be billed for charges associated with the request. | No  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
