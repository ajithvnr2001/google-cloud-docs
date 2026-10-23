---
url: https://docs.cloud.google.com/storage/docs/xml-api/post-object-resumable/
title: Initiate a resumable upload \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:17:41.776398+00:00
---

# Initiate a resumable upload  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/post-object-resumable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Initiate a resumable upload Stay organized with collections  Save and categorize content based on your preferences. 

Initiates a [resumable upload](https://docs.cloud.google.com/storage/docs/resumable-uploads) with a `POST` request. This initial request generates a session URI for use in subsequent `PUT` requests which [upload the data](https://docs.cloud.google.com/storage/docs/performing-resumable-uploads#upload-data). The initial request also allows you to specify metadata for the object. Once a resumable upload completes, the uploaded object replaces any existing object with the same name.

For simple uploads with the XML API, you make a [`PUT` Object](https://docs.cloud.google.com/storage/docs/xml-api/put-object-upload) request instead of using `POST` Object.

## Query string parameters

This request does not typically include query string parameters.

See [signed URL query string parameters](https://docs.cloud.google.com/storage/docs/authentication/canonical-requests#required-query-parameters) for information on the parameters you include when creating and using [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).

## Request headers

The following request headers can be used.

Header | Description | Required  
---|---|---  
`[Authorization](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#authorization)` | The authentication string for the request. | Yes  
`[Cache-Control](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#cachecontrol)` | The conditions under which a publicly accessible object should be cached. `Cache-Control` is also used to determine whether an object can be transformed. | No  
`[Content-Disposition](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentdisposition)` | A header that specifies presentational information about how the object data is to be transmitted. | No  
`[Content-Encoding](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentencoding)` | The compression algorithm that was used to compress the object you are uploading. | No  
`[Content-Language](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentlanguage)` | The language code of the content. | No  
`[Content-Length](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentlength)` | The length of the request body without headers (in bytes). For initiating a resumable upload, this value is 0. | Yes  
`[Content-Type](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contenttype)` | The MIME type of the object to be uploaded. If you do not specify a content type, Cloud Storage defaults to [`application/octet-stream`](https://datatracker.ietf.org/doc/html/rfc2046#section-4.5.1) when it serves the object. | No (recommended)  
`[Date](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#date)` | The date and time of the request. | Yes  
`[Host](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#host)` | The URI for Cloud Storage. For more information, see [Request Endpoints](https://docs.cloud.google.com/storage/docs/request-endpoints). | Yes  
`[x-goog-acl](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogacl)` | The predefined ACL that you want to apply to the object. | No  
`[x-goog-custom-time](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogcustomtime)` | A user-specified date and time. | No  
`[x-goog-encryption-kms-key-name](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogencryptionkmskeyname)` | The [customer-managed encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys) to use to encrypt the object. | No  
`[x-goog-if-generation-match](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogifgenerationmatch)` | If the generation you specify is the same as the object you're replacing, then the object is replaced. You can also specify 0 as a special value to indicate that the new object is only created if there is no existing object. | No  
`[x-goog-if-metageneration-match](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogifmetagenerationmatch)` | If the metageneration you specify is the same as the object you're trying to update, then the object metadata is updated. This is only allowed if `x-goog-if-generation` is specified. By combining these two generation properties, you can implement safe read-modify-write updates. | No  
`[x-goog-meta-](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogmeta)` | An extension header that can be used to store [custom metadata](https://docs.cloud.google.com/storage/docs/metadata#custom-metadata). | No  
`[x-goog-object-lock-mode](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogobjectlockmode)` | Mode of the object's [retention configuration](https://docs.cloud.google.com/storage/docs/object-lock). `GOVERNANCE` corresponds to unlocked mode, and `COMPLIANCE` corresponds to locked mode. If this header is specified, `x-goog-object-lock-retain-until-date` must also be specified. | No  
``[x-goog-object-lock-retain-until-date](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogobjectlockretainuntildate)`` | A date and time represented in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) UTC format that determines the time until which the object is retained as immutable. If this header is specified, `x-goog-object-lock-mode` must also be specified. | No  
`[x-goog-resumable](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogresumable)` | Indicates that this request initiates the resumable upload. This header must use the value `start` | Yes  
`[x-goog-storage-class](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogstorageclass)` | Gives an object a storage class besides the default storage class of the associated bucket. | No  
`[x-goog-user-project](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgooguserproject)` | The project to be billed for charges associated with the request. Note that the project specified in the initial request is used in all future requests associated with the resumable upload. | No  
  
To provide a customer-supplied encryption key along with the object upload, use the [headers listed on the Customer-Supplied Encryption Key page](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys#headers) in your request.

## Request body elements

This request does not include an XML document in the request body.

## Response headers

The response includes a [Location](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#location) header that indicates the session URI to use when uploading the object data.

## Response body elements

The response does not include an XML document in the response body.

## Example

The following sample uploads an object named paris.jpg to a bucket named travel-maps.

**Request**
    
    
    POST /paris.jpg HTTP/2
    Host: travel-maps.storage.googleapis.com
    Date: Thu, 10 Dec 2020 18:11:50 GMT
    Content-Type: image/jpg
    Content-Length: 0
    X-Goog-Resumable: start
    Authorization: Bearer ya29.AHES6ZRVmB7fkLtd1XTmq6mo0S1wqZZi3-Lh_s-6Uw7p8vtgSwg
    

**Response**
    
    
    HTTP/2 201
    Content-Type: text/plain; charset=utf-8
    X-Guploader-Uploadid: ABf5-UxjuGIOxcy0OpOLoAHbmo5rYKWx3XfrZFTjowNwPT9JYiopVZW2gPFrusVKO5kaSZ7fNrDWkb9sT_lKxOssUTE
    Location: https://storage.googleapis.com/travel-maps/paris.jpg?upload_id=ABf5-UxjuGIOxcy0OpOLoAHbmo5rYKWx3XfrZFTjowNwPT9JYiopVZW2gPFrusVKO5kaSZ7fNrDWkb9sT_lKxOssUTE
    Content-Length: 0
    Date: Thu, 10 Dec 2020 18:11:53 GMT
    Server: UploadServer
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
