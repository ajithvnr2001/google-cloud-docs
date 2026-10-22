---
url: https://docs.cloud.google.com/storage/docs/xml-api/post-object-multipart/
title: Initiate a multipart upload \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:37:47.664419+00:00
---

# Initiate a multipart upload  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/post-object-multipart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Initiate a multipart upload Stay organized with collections  Save and categorize content based on your preferences. 

Initiates a [XML API multipart upload](https://docs.cloud.google.com/storage/docs/multipart-uploads) with a `POST` request. This initial request generates an upload ID for use in subsequent `PUT` requests to [upload the data in parts](https://docs.cloud.google.com/storage/docs/xml-api/put-object-multipart) and in the final `POST` request to [complete the upload](https://docs.cloud.google.com/storage/docs/xml-api/post-object-complete). There is no limit to the number of multipart uploads that can be underway for a given object.

This initial request allows you to specify metadata for the completed object. Once a multipart upload completes, the uploaded object replaces any existing object with the same name. For tips on uploading to Cloud Storage, see [best practices](https://docs.cloud.google.com/storage/docs/best-practices#uploading).

For simple uploads with the XML API, you make a [`PUT` Object](https://docs.cloud.google.com/storage/docs/xml-api/put-object-upload) request instead of using `POST` Object.

## Query string parameters

Parameter | Description | Required  
---|---|---  
`[uploads](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#uploads)` | Indicates the request is to initiate a multipart upload. | Yes  
  
See [signed URL query string parameters](https://docs.cloud.google.com/storage/docs/authentication/canonical-requests#required-query-parameters) for information on the parameters you include when creating and using [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).

## Request headers

The following request headers can be used.

Header | Description | Required  
---|---|---  
`[Authorization](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#authorization)` | The authentication string for the request. | Yes  
`[Cache-Control](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#cachecontrol)` | The conditions under which the resulting object should be cached if it is publicly accessible. `Cache-Control` is also used to determine whether the resulting object can be transformed. | No  
`[Content-Disposition](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentdisposition)` | A header that specifies presentational information about how the resulting object data is to be transmitted. | No  
`[Content-Encoding](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentencoding)` | The compression algorithm that was used to compress the data you are uploading. | No  
`[Content-Language](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentlanguage)` | The language code of the content. | No  
`[Content-Length](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentlength)` | The length of the request body without headers (in bytes). For initiating a multipart upload, this value is 0. | Yes  
`[Content-Type](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contenttype)` | The MIME type of the data you are uploading. If you do not specify a content type, Cloud Storage defaults to [`application/octet-stream`](https://datatracker.ietf.org/doc/html/rfc2046#section-4.5.1) when it serves the uploaded object. | No (recommended)  
`[Date](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#date)` | The date and time of the request. | Yes  
`[Host](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#host)` | The URI for Cloud Storage. For more information, see [Request Endpoints](https://docs.cloud.google.com/storage/docs/request-endpoints). | Yes  
`[x-goog-acl](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogacl)` | The predefined ACL that you want to apply to the object. | No  
`[x-goog-custom-time](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogcustomtime)` | A user-specified date and time. | No  
`[x-goog-encryption-kms-key-name](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogencryptionkmskeyname)` | The [customer-managed encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys) to use to encrypt the object. | No  
`[x-goog-meta-](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogmeta)` | An extension header that can be used to store [custom metadata](https://docs.cloud.google.com/storage/docs/metadata#custom-metadata). | No  
`[x-goog-object-lock-mode](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogobjectlockmode)` | Mode of the object's [retention configuration](https://docs.cloud.google.com/storage/docs/object-lock). `GOVERNANCE` corresponds to unlocked mode, and `COMPLIANCE` corresponds to locked mode. If this header is specified, `x-goog-object-lock-retain-until-date` must also be specified. | No  
``[x-goog-object-lock-retain-until-date](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogobjectlockretainuntildate)`` | A date and time represented in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) UTC format that determines the time until which the object is retained as immutable. If this header is specified, `x-goog-object-lock-mode` must also be specified. | No  
`[x-goog-storage-class](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogstorageclass)` | Gives each part of the upload and the resulting object a storage class besides the default storage class of the associated bucket. | No  
`[x-goog-user-project](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgooguserproject)` | The project to be billed for charges associated with this request. | No  
  
To provide a customer-supplied encryption key along with the object upload, use the [headers listed on the Customer-Supplied Encryption Key page](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys#headers) in your request.

## Request body elements

This request does not include an XML document in the request body.

## Response headers

The request can return a variety of response headers depending on the request headers you use.

## Response body elements

The following response body elements apply to POST Object requests that use the `uploads` query string parameter.

Element | Description  
---|---  
`InitiateMultipartUploadResult` | Container for the response to the upload initiation request.  
`Bucket` | The name of the bucket the multipart upload was initiated in.  
`Key` | The name of the object the multipart upload was initiated for.  
`UploadId` | The upload ID of the initiated multipart upload.  
  
## Example

The following sample initiates a multipart upload for an object named `paris.jpg` in a bucket named `travel-maps`.

**Request**
    
    
    POST /paris.jpg?uploads HTTP/2
    Host: travel-maps.storage.googleapis.com
    Date: Wed, 24 Mar 2021 18:11:50 GMT
    Content-Type: image/jpg
    Content-Length: 0
    Authorization: Bearer ya29.AHES6ZRVmB7fkLtd1XTmq6mo0S1wqZZi3-Lh_s-6Uw7p8vtgSwg
    

**Response**
    
    
    HTTP/2 200
    Date: Wed, 24 Mar 2021 18:11:53 GMT
    Content-Length: 280
    Content-Type: application/xml
    Server: UploadServer
    
    <?xml version="1.0" encoding="UTF-8"?>
    <InitiateMultipartUploadResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
      <Bucket>travel-maps</Bucket>
      <Key>paris.jpg</Key>
      <UploadId>VXBsb2FkIElEIGZvciBlbHZpbmcncyBteS1tb3ZpZS5tMnRzIHVwbG9hZA</UploadId>
    </InitiateMultipartUploadResult>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
