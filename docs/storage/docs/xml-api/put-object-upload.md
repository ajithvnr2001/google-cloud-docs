---
url: https://docs.cloud.google.com/storage/docs/xml-api/put-object-upload/
title: Object upload \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:15:08.011241+00:00
---

# Object upload  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/put-object-upload/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Object upload Stay organized with collections  Save and categorize content based on your preferences. 

To perform a single-request upload with the XML API, you make a `PUT` request that is scoped with a bucket name and the object's name, and you put the object data into the request body. The uploaded object replaces any existing object with the same name. For tips on uploading to Cloud Storage, see [Best Practices](https://docs.cloud.google.com/storage/docs/best-practices#uploading). For a quick guide to simple uploads using tools such as the XML API, see [Uploading Objects](https://docs.cloud.google.com/storage/docs/uploading-objects).

The PUT Object request uses several standard HTTP headers. `Content-Length` specifies the object's size in bytes and is required unless you are using chunked transfer encoding. Optional headers include `Content-Type`, `Content-MD5`, and those listed below. Cloud Storage stores these headers as part of the [object's metadata](https://docs.cloud.google.com/storage/docs/metadata), except for `Content-MD5`, which Cloud Storage uses to check for data integrity. See [Editing object metadata](https://docs.cloud.google.com/storage/docs/viewing-editing-metadata#edit) for information on changing metadata values for objects.

You also use a PUT Object request when you want to change the [storage class](https://docs.cloud.google.com/storage/docs/storage-classes) of an existing object, because you must rewrite the existing object to do so. The request should contain the [`x-goog-storage-class` request header](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogstorageclass), as well as the object in the request body.

**Note:** Some types of uploads, such as [resumable uploads](https://docs.cloud.google.com/storage/docs/resumable-uploads), use a [`POST` Object request](https://docs.cloud.google.com/storage/docs/xml-api/post-object).

## Query string parameters

This request does not typically include query string parameters.

See [signed URL query string parameters](https://docs.cloud.google.com/storage/docs/authentication/canonical-requests#required-query-parameters) for information on the parameters you include when creating and using [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).

## Request headers

In addition to [common request headers](https://docs.cloud.google.com/storage/docs/xml-api/put-object#request-headers), the following can be used.

Header | Description | Required  
---|---|---  
`[Cache-Control](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#cachecontrol)` | The conditions under which a publicly accessible object should be cached. `Cache-Control` is also used to determine whether an object can be transformed. | No  
`[Content-Disposition](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentdisposition)` | A header that specifies presentational information about how the object data is to be transmitted. | No  
`[Content-Encoding](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentencoding)` | The compression algorithm that was used to compress the object you are uploading. | No  
`[Content-Language](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentlanguage)` | The language code of the content. | No  
`[x-goog-acl](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogacl)` | The predefined ACL that you want to apply to the object. | No  
`[x-goog-custom-time](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogcustomtime)` | A user-specified date and time. | No  
`[x-goog-encryption-kms-key-name](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogencryptionkmskeyname)` | The [customer-managed encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys) to use to encrypt the object. | No  
`[x-goog-meta-](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogmeta)` | An extension header that can be used to store [custom metadata](https://docs.cloud.google.com/storage/docs/metadata#custom-metadata). | No  
`[x-goog-object-lock-mode](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogobjectlockmode)` | Mode of the object's [retention configuration](https://docs.cloud.google.com/storage/docs/object-lock). `GOVERNANCE` corresponds to unlocked mode, and `COMPLIANCE` corresponds to locked mode. If this header is specified, `x-goog-object-lock-retain-until-date` must also be specified. | No  
``[x-goog-object-lock-retain-until-date](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogobjectlockretainuntildate)`` | A date and time represented in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) UTC format that determines the time until which the object is retained as immutable. If this header is specified, `x-goog-object-lock-mode` must also be specified. | No  
`[x-goog-storage-class](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogstorageclass)` | A valid [storage class](https://docs.cloud.google.com/storage/docs/storage-classes). | No  
  
To provide a customer-supplied encryption key along with the object upload, use the [headers listed on the Customer-Supplied Encryption Key page](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys#headers) in your request.

## Request body elements

The request body contains the data.

## Request syntax

The following syntax applies to PUT Object requests that don't use any query string parameters and excludes the `x-goog-copy-source` request header.
    
    
    PUT /OBJECT_NAME HTTP/1.1
    Host: BUCKET_NAME.storage.googleapis.com
    Date: DATE
    Content-Length: REQUEST_BODY_LENGTH
    Content-Type: MIME_TYPE
    Content-MD5: MD5_DIGEST
    Authorization: AUTHENTICATION_STRING
    x-goog-storage-class: STORAGE_CLASS
    

## Response headers

The request can return a variety of response headers depending on the request headers you use.

## Response body elements

The response does not include an XML document in the response body.

## Example

The following sample uploads an object named paris.jpg to a bucket named travel-maps.

**Request**
    
    
    PUT /paris.jpg HTTP/1.1
    Host: travel-maps.storage.googleapis.com
    Date: Sat, 20 Feb 2010 16:31:08 GMT
    Content-Type: image/jpg
    Content-MD5: iB94gawbwUSiZy5FuruIOQ==
    Content-Length: 554
    Authorization: Bearer ya29.AHES6ZRVmB7fkLtd1XTmq6mo0S1wqZZi3-Lh_s-6Uw7p8vtgSwg
    

**Response**
    
    
    HTTP/1.1 200 OK
    ETag: "881f7881ac1bc144a2672e45babb8839"
    Date: Sat, 20 Feb 2010 16:31:09 GMT
    Content-Length: 0
    Content-Type: text/html
    

## Common error codes

If you try to upload an object into a bucket that does not exist, you get a [404 Not Found](https://docs.cloud.google.com/storage/docs/xml-api/reference-status) status code and the body of the error response has `NoSuchBucket` in the `Code` element.

If the supplied MD5 digest is malformed, you get a [400 Bad Request](https://docs.cloud.google.com/storage/docs/xml-api/reference-status) status code and the body of the error response has `InvalidDigest` in the `Code` element.

If the digest does not match the digest we compute from the body, you get a [400 Bad Request](https://docs.cloud.google.com/storage/docs/xml-api/reference-status) status code and the body of the error response has `BadDigest` in the `Code` element.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
