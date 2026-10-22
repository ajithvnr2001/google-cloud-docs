---
url: https://docs.cloud.google.com/storage/docs/xml-api/delete-bucket/
title: DELETE Bucket \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:37:57.016909+00:00
---

# DELETE Bucket  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/delete-bucket/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  DELETE Bucket Stay organized with collections  Save and categorize content based on your preferences. 

Deletes an empty bucket. The request fails if there are any objects in the bucket, but the request succeeds if the bucket only contains soft-deleted objects or incomplete uploads, such as ongoing [XML API multipart uploads](https://docs.cloud.google.com/storage/docs/multipart-uploads). Does not delete [soft-deleted objects](https://docs.cloud.google.com/storage/docs/soft-delete).

The DELETE Bucket method is a simple DELETE request with bucket scope. You must have the project owners role to delete buckets. Also, all DELETE Bucket requests must be authenticated.

As a best practice, after you delete all of the objects from a bucket you should set the bucket ACLs so that no users can create objects in the bucket.

If there are objects in the bucket when you attempt to delete it you will get a [409 Conflict](https://docs.cloud.google.com/storage/docs/xml-api/reference-status) status code and the body of the error response will contain `BucketNotEmpty` in the `Code` element.

If the bucket does not exist you will get a [404 Not Found](https://docs.cloud.google.com/storage/docs/xml-api/reference-status) status code and the body of the error response will contain `NoSuchBucket` in the `Code` element.

## Query string parameters

This request does not typically include query string parameters.

See [signed URL query string parameters](https://docs.cloud.google.com/storage/docs/authentication/canonical-requests#required-query-parameters) for information on the parameters you include when creating and using [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).

## Request headers

Header | Description | Required  
---|---|---  
`[Authorization](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#authorization)` | The authentication string for the request. | Yes  
`[Content-Length](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentlength)` | The length of the request body without headers (in bytes). * Not required for requests that use chunked transfer encoding. | Yes*  
`[Date](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#date)` | The date and time of the request. | Yes  
`[Host](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#host)` | The URI for Cloud Storage. For more information, see [Request Endpoints](https://docs.cloud.google.com/storage/docs/request-endpoints). | Yes  
`[x-goog-user-project](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgooguserproject)` | The project to be billed for charges associated with the request. | No  
  
## Request body elements

This request does not include an XML document in the request body.

## Request syntax
    
    
    DELETE / HTTP/1.1
    Host: BUCKET_NAME.storage.googleapis.com
    Date: DATE
    Content-Length: 0
    Authorization: AUTHENTICATION_STRING
    

## Response headers

The request can return a variety of response headers depending on the request headers you use.

## Response body elements

The response does not include an XML document in the response body.

## Example

The following example deletes a bucket named travel-maps.

**Request**
    
    
    DELETE / HTTP/1.1
    Host: travel-maps.storage.googleapis.com
    Date: Mon, 15 Feb  2010 11:00:00 GMT
    Content-Length: 0
    Authorization: Bearer ya29.AHES6ZRVmB7fkLtd1XTmq6mo0S1wqZZi3-Lh_s-6Uw7p8vtgSwg
    

**Response**
    
    
    HTTP/1.1 204 No Content
    Date: Mon, 15 Feb  2010 11:00:01 GMT
    Expires: Mon, 15 Feb  2010 11:00:01 GMT
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
