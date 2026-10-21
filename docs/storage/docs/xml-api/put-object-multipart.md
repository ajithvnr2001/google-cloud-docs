---
url: https://docs.cloud.google.com/storage/docs/xml-api/put-object-multipart/
title: Object upload part \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:50:05.418520+00:00
---

# Object upload part  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/put-object-multipart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Object upload part Stay organized with collections  Save and categorize content based on your preferences. 

Uploads a part of a [multipart upload](https://docs.cloud.google.com/storage/docs/multipart-uploads). Returns an ETag which must be used when [completing the multipart upload](https://docs.cloud.google.com/storage/docs/xml-api/post-object-complete).

To ensure that data is not corrupted, you should specify a `Content-MD5` header or a `x-goog-hash` header in the request so that Cloud Storage can check the uploaded data against the provided value.

Uploaded parts are not included in requests to list objects in the bucket, but uploaded parts are [charged for storage and early deletion](https://docs.cloud.google.com/storage/pricing) as if they were objects.

See [Quotas & limits](https://docs.cloud.google.com/storage/quotas#requests) for limits associated with multipart uploads, including limits on part size and number of parts. For tips on uploading to Cloud Storage, see [Best Practices](https://docs.cloud.google.com/storage/docs/best-practices#uploading).

## Query string parameters

Parameter | Description | Required  
---|---|---  
`[partNumber](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#partnumber)` | Uniquely identifies the position of the part within the larger multipart upload. `partNumber` is an integer with a mimimum value of 1 and a maximum value of 10,000. | Yes  
`[uploadId](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#uploadid-multipart)` | Indicates the multipart upload that this part is associated with. | Yes  
  
See [signed URL query string parameters](https://docs.cloud.google.com/storage/docs/authentication/canonical-requests#required-query-parameters) for information on the parameters you include when creating and using [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).

## Request headers

In addition to [common request headers](https://docs.cloud.google.com/storage/docs/xml-api/put-object#request-headers), the following can be used.

Header | Description | Required  
---|---|---  
`[x-goog-hash](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgooghash)` | An MD5 and/or CRC32C base64-encoded checksum of the part data. | No  
  
If you specified a customer-supplied encryption key in the request to initiate the multipart upload, you must use the [same headers](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys#headers) and values in each part upload.

## Request body elements

The request body contains the data for the part being uploaded.

## Request syntax

The following syntax applies to PUT Object requests that use the `uploadId` query string parameter.
    
    
    PUT /OBJECT_NAME?partNumber=PART_NUMBER&uploadId=UPLOAD_ID HTTP/1.1
    Host: BUCKET_NAME.storage.googleapis.com
    Date: DATE
    Content-Length: REQUEST_BODY_LENGTH
    Content-MD5: MD5_DIGEST
    Authorization: AUTHENTICATION_STRING
    x-goog-hash: MD5_DIGEST
    

## Response headers

Included in the response headers are `x-goog-hash` headers that specify the CRC32C and MD5 base64-encoded checksums of the uploaded part.

The response also includes an `ETag` header that must be used in the final request to complete the multipart upload.

## Response body elements

The response does not include an XML document in the response body.

## Example

The following sample uploads the first part of an object named `paris.jpg` to a bucket named `travel-maps`.

**Request**
    
    
    PUT /paris.jpg?partNumber=1&uploadId=VXBsb2FkIElEIGZvciBlbHZpbmcncyBteS1tb3ZpZS5tMnRzIHVwbG9hZA HTTP/1.1
    Host: travel-maps.storage.googleapis.com
    Date: Wed, 31 Mar 2021 16:31:08 GMT
    Content-Length: 100000000
    Content-MD5: Ojk9c3dhfxgoKVVHYwFbHQ==
    Authorization: Bearer ya29.AHES6ZRVmB7fkLtd1XTmq6mo0S1wqZZi3-Lh_s-6Uw7p8vtgSwg
    
    ***part data omitted***
    

**Response**
    
    
    HTTP/1.1 200 OK
    Date:  Wed, 31 Mar 2021 20:34:56 GMT
    ETag: "39a59594290b0f9a30662a56d695b71d"
    Content-Length: 0
    Server: UploadServer
    x-goog-hash: crc32c=n03x6A==
    x-goog-hash: md5=Ojk9c3dhfxgoKVVHYwFbHQ==
    

## Common error codes

If the supplied MD5 digest is malformed, you get a [400 Bad Request](https://docs.cloud.google.com/storage/docs/xml-api/reference-status) status code and the body of the error response has `InvalidDigest` in the `Code` element.

If the digest does not match the digest we compute from the body, you get a [400 Bad Request](https://docs.cloud.google.com/storage/docs/xml-api/reference-status) status code and the body of the error response has `BadDigest` in the `Code` element.

If one of the parts specified in the request is more than 5 GiB, you get a [400 Bad Request](https://docs.cloud.google.com/storage/docs/xml-api/reference-status) status code and the body of the error response has `EntityTooLarge` in the `Code` element.

If the `uploadId` specified in the request is invalid or applies to a multipart upload that has already been completed or aborted, you get a [404 Not Found](https://docs.cloud.google.com/storage/docs/xml-api/reference-status) status code and the body of the error response has `NoSuchUpload` in the `Code` element.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
