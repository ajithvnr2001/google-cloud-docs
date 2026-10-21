---
url: https://docs.cloud.google.com/storage/docs/xml-api/get-bucket-acls/
title: Get bucket ACLs \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:47.475301+00:00
---

# Get bucket ACLs  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/get-bucket-acls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Get bucket ACLs Stay organized with collections  Save and categorize content based on your preferences. 

To list a bucket's ACLs you make a GET request that is scoped to a bucket and you use the `acl` query string parameter. The ACLs are returned in an XML document in the response body.

## Query string parameters

Parameter | Description | Required  
---|---|---  
`[acl](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#acl)` | You can use this to display the ACLs of an existing bucket. | No  
  
See [signed URL query string parameters](https://docs.cloud.google.com/storage/docs/authentication/canonical-requests#required-query-parameters) for information on the parameters you include when creating and using [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).

## Request headers

See [common request headers](https://docs.cloud.google.com/storage/docs/xml-api/get-bucket#request-headers).

## Request body elements

This request does not include an XML document in the request body.

## Request syntax

The following syntax applies to GET Bucket requests that use the `acl` query string parameter.
    
    
    GET /?acl HTTP/1.1
    Host: BUCKET_NAME.storage.googleapis.com
    Date: DATE
    Content-Length: 0
    Authorization: AUTHENTICATION_STRING
    

## Response headers

The request can return a variety of response headers depending on the request headers you use.

## Response body elements

The following response body elements are applicable only if you use the `acl` query string parameter to list a bucket's ACLs.

Element | Description  
---|---  
`Owner` | Container for bucket owner information.  
`ID` | The Cloud Storage ID of the bucket owner or theCloud Storage ID of the user or group for whom the ACLs apply.  
`Name` | Comment field for `GroupByEmail`, `GroupById`, `UserByEmail`, and `UserById`.  
`AccessControlList` | Container for the ACLs you are retrieving.  
`Entries` | Container for the ACL entries you are retrieving.  
`Entry` | The ACL entry you are retrieving.  
`Scope` | The scope to which the ACLs apply.  
`Permission` | The permission that has been granted. Can be any of the Cloud Storage permissions, including `READ`, `WRITE`, or `FULL_CONTROL`  
`EmailAddress` | A user account email address, a service account email address, or a Google group email address.  
`Domain` | A Google Workspace or Cloud Identity domain.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
