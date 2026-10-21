---
url: https://docs.cloud.google.com/storage/docs/xml-api/post-object-complete/
title: Complete a multipart upload \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:50:07.290287+00:00
---

# Complete a multipart upload  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/post-object-complete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Complete a multipart upload Stay organized with collections  Save and categorize content based on your preferences. 

Completes a [multipart upload](https://docs.cloud.google.com/storage/docs/multipart-uploads) by concatenating the parts into a single object.

Cloud Storage can take several minutes to process a request to complete a multipart upload. Once the request completes, the object created from the upload replaces any existing object with the same name, and the parts from the multipart upload no longer exist, whether or not they were used to assemble the final object.

An object created from a multipart upload has a CRC32c hash, but not an MD5 hash, and the object's ETag is not based on an MD5 hash.

## Query string parameters

Parameter | Description | Required  
---|---|---  
`[uploadId](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#uploadid-multipart)` | Indicates the multipart upload that this request is associated with. | Yes  
  
See [signed URL query string parameters](https://docs.cloud.google.com/storage/docs/authentication/canonical-requests#required-query-parameters) for information on the parameters you include when creating and using [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).

## Request headers

The following request headers can be used.

Header | Description | Required  
---|---|---  
`[Authorization](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#authorization)` | The authentication string for the request. | Yes  
`[Content-Length](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentlength)` | The length of the request body without headers (in bytes). | Yes  
`[Content-Type](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contenttype)` | The MIME type of the request body. When completing a multipart upload, this value should be `application/xml`. | No  
`[Date](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#date)` | The date and time of the request. | Yes  
`[Host](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#host)` | The URI for Cloud Storage. For more information, see [Request Endpoints](https://docs.cloud.google.com/storage/docs/request-endpoints). | Yes  
`[x-goog-user-project](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgooguserproject)` | The project to be billed for charges associated with the request. | No  
  
If you specified a customer-supplied encryption key in the request to initiate the multipart upload, you must use the [same headers](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys#headers) and values in the request to complete the upload.

## Request body elements

The following request body elements are applicable if you use the `uploadId` query string parameter to complete a multipart upload. All request body elements are required.

Element | Description  
---|---  
`CompleteMultipartUpload` | Container for the request to complete the multipart upload.  
`Part` | A container for each part of the multipart upload.  
`PartNumber` | Number that identifies the part and its order in the overall multipart upload.  
`ETag` | The entity tag for the part, which was returned when the part was uploaded.  
  
## Response headers

Included in the response headers is an `x-goog-hash` header that specifies the CRC32C base64-encoded checksum of the object.

## Response body elements

The following response body elements apply to POST Object requests that use the `uploadId` query string parameter to complete a multipart upload.

Element | Description  
---|---  
`CompleteMultipartUploadResult` | Container for the response to the request to complete the multipart upload.  
`Location` | A request endpoint that can be used to access the object created from the upload.  
`Bucket` | The name of the bucket that contains the object created from the upload.  
`Key` | The name of the object created from the upload.  
`ETag` | An entity tag that uniquely identifies the object created from the upload.  
  
## Example

The following sample completes a multipart upload. It creates an object named `paris.jpg` from two parts in a bucket named `travel-maps`.

**Request**
    
    
    POST /paris.jpg?uploadId=VXBsb2FkIElEIGZvciBlbHZpbmcncyBteS1tb3ZpZS5tMnRzIHVwbG9hZA HTTP/2
    Host: travel-maps.storage.googleapis.com
    Date: Fri, 2 Apr 2021 18:11:50 GMT
    Content-Type: application/xml
    Content-Length: 232
    Authorization: Bearer ya29.AHES6ZRVmB7fkLtd1XTmq6mo0S1wqZZi3-Lh_s-6Uw7p8vtgSwg
    
    <CompleteMultipartUpload>
      <Part>
        <PartNumber>2</PartNumber>
        <ETag>"7778aef83f66abc1fa1e8477f296d394"</ETag>
      </Part>
      <Part>
        <PartNumber>5</PartNumber>
        <ETag>"aaaa18db4cc2f85cedef654fccc4a4x8"</ETag>
      </Part>
    </CompleteMultipartUpload>
    

**Response**
    
    
    HTTP/2 200
    Content-Type: application/xml
    Content-Length: 324
    Date: Fri, 2 Apr 2021 18:11:53 GMT
    Server: UploadServer
    x-goog-hash: crc32c=n03x6A==
    
    <?xml version="1.0" encoding="UTF-8"?>
    <CompleteMultipartUploadResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
      <Location>http://travel-maps.storage.googleapis.com/paris.jpg</Location>
      <Bucket>travel-maps</Bucket>
      <Key>paris.jpg</Key>
      <ETag>"7fc8f92280ac3c975f300cb64412c16f-9"</ETag>
    </CompleteMultipartUploadResult>
    

## Common error codes

If one of the parts specified in the request has not been uploaded, or if the ETag specified in the request does not match the ETag of the uploaded part, you get a [400 Bad Request](https://docs.cloud.google.com/storage/docs/xml-api/reference-status) status code and the body of the error response has `InvalidPart` in the `Code` element.

If the list of parts specified in the request is not in ascending order, you get a [400 Bad Request](https://docs.cloud.google.com/storage/docs/xml-api/reference-status) status code and the body of the error response has `InvalidPartOrder` in the `Code` element.

If one of the parts specified in the request is less than 5 MiB and is not the final part in the upload, you get a [400 Bad Request](https://docs.cloud.google.com/storage/docs/xml-api/reference-status) status code and the body of the error response has `InvalidArgument` in the `Code` element.

If the `uploadId` specified in the request is invalid or applies to a multipart upload that has already been completed or aborted, you get a [404 Not Found](https://docs.cloud.google.com/storage/docs/xml-api/reference-status) status code and the body of the error response has `NoSuchUpload` in the `Code` element.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
