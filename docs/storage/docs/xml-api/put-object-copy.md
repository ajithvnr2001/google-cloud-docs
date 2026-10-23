---
url: https://docs.cloud.google.com/storage/docs/xml-api/put-object-copy/
title: Copy an object \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:01.869830+00:00
---

# Copy an object  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/put-object-copy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Copy an object Stay organized with collections  Save and categorize content based on your preferences. 

To copy an object, you make a `PUT` request that is scoped to the new bucket and object name and you specify the source object with the `x-goog-copy-source` request header. To copy an object to itself you must use the [`x-goog-metadata-directive` header](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogcopymeta) with a value of `REPLACE` and you must specify any object metadata for the copied object in your request.

If any of the conditional copy headers fail to match the condition you specify you will get a [412 Precondition Failed](https://docs.cloud.google.com/storage/docs/xml-api/reference-status) status code and the body of the error response will have `PreconditionFailed` in the `Code` element.

## Query string parameters

This request does not typically include query string parameters.

See [signed URL query string parameters](https://docs.cloud.google.com/storage/docs/authentication/canonical-requests#required-query-parameters) for information on the parameters you include when creating and using [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).

## Request headers

In addition to [common request headers](https://docs.cloud.google.com/storage/docs/xml-api/put-object#request-headers), the following can be used.

Header | Description | Required  
---|---|---  
`[Content-Encoding](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentencoding)` | The compression algorithm that was used to compress the object you are uploading. | No  
`[Content-Disposition](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentdisposition)` | A header you can set on an object that specifies presentational information about how the object data is to be transmitted. | No  
`[x-goog-acl](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogacl)` | The predefined ACL that you want to apply to the object. Do not use if you are using the `acl` query string parameter to apply ACLs. | No  
`[x-goog-custom-time](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogcustomtime)` | A user-specified date and time. | No  
`[x-goog-encryption-kms-key-name](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogencryptionkmskeyname)` | The [customer-managed encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys) to use to encrypt the copied object. | No  
`[x-goog-metadata-directive](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogcopymeta)` | The instructions for handling metadata during a copy operation. Can be `COPY` or `REPLACE`. The default value is `COPY`. | No  
`[x-goog-meta-](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogmeta)` | An extension header that can be used to store additional metadata that is not provided by the other fields. | No  
`[x-goog-object-lock-mode](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogobjectlockmode)` | Mode of the object's [retention configuration](https://docs.cloud.google.com/storage/docs/object-lock). `GOVERNANCE` corresponds to unlocked mode, and `COMPLIANCE` corresponds to locked mode. If this header is specified, `x-goog-object-lock-retain-until-date` must also be specified. | No  
``[x-goog-object-lock-retain-until-date](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogobjectlockretainuntildate)`` | A date and time represented in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) UTC format that determines the time until which the object is retained as immutable. If this header is specified, `x-goog-object-lock-mode` must also be specified. | No  
`[x-goog-copy-source](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogcopy)` | The bucket/object path to the object you want to copy. For example, `/travel-maps/paris.jpg`. | Yes  
`[x-goog-copy-source-generation](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogcopygeneration)` | The [generation number](https://docs.cloud.google.com/storage/docs/metadata#generation-number) of the object you want to copy. | No  
`[x-goog-copy-source-if-generation-match](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogifcopygenerationmatch)` | A generation number. If the generation number you specify matches the generation number of the source object, then the source object is copied. | No  
`[x-goog-copy-source-if-metageneration-match](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogifcopymetagenerationmatch)` | A metageneration number. If the metageneration number you specify matches the metageneration number of the source object, then the object is copied. | No  
`[x-goog-copy-source-if-match](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogcopymatch)` | An ETag. If the ETag you specify matches the ETag of the source object, then the source object is copied. | No  
`[x-goog-copy-source-if-none-match](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogcopynomatch)` | An ETag. If the ETag you specify does not match the Etag of the source object, then the object is copied. | No  
`[x-goog-copy-source-if-modified-since](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogcopymod)` | A date and time. If the date and time you specify is earlier than the `Last-Modified` date of the source object, then the object is copied. | No  
`[x-goog-copy-source-if-unmodified-since](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogcopyunmod)` | A date and time. If the date and time you specify is later than the `Last-Modified` date of the source object, then the object is copied. | No  
  
To copy an object encrypted by a [customer-supplied encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys), use the [headers listed on the Encryption page](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys#headers) in your request.

## Request body elements

This request does not include an XML document in the request body.

## Request syntax

The following syntax applies to PUT Object requests that use the `x-goog-copy-source` request header and the related conditional copy request headers.
    
    
    PUT /OBJECT_NAME HTTP/1.1
    Host: BUCKET_NAME.storage.googleapis.com
    Date: DATE
    Content-Length: REQUEST_BODY_LENGTH
    Content-Type: MIME_TYPE
    Authorization: AUTHENTICATION_STRING
    x-goog-copy-source: /BUCKET_NAME/OBJECT_NAME
    x-goog-copy-source-if-match: ETAG
    x-goog-copy-source-if-none-match: ETAG
    x-goog-copy-source-if-unmodified-since: DATE
    x-goog-copy-source-if-modified-since: DATE
    x-goog-metadata-directive: COPY | REPLACE
    

## Response headers

The request can return a variety of response headers depending on the request headers you use.

## Response body elements

The following response elements are returned when you use the `x-goog-copy-source` request header or any of the related conditional copy request headers.

Element | Description  
---|---  
CopyObjectResult | Container for copy information.  
ETag | The ETag of the newly-copied object.   
LastModified | The date and time that the source object was last modified prior to the current copy operation.  
  
## Example

The following sample uses the `x-goog-copy-source` request header to copy an object named paris.jpg from a bucket named travel-maps to a bucket named city-maps.

**Request**
    
    
    PUT /paris.jpg HTTP/1.1
    Host: city-maps.storage.googleapis.com
    Date: Fri, 23 Jul 2010 21:27:36 GMT
    Content-Length: 0
    x-goog-copy-source: travel-maps/paris.jpg
    Authorization: Bearer ya29.AHES6ZRVmB7fkLtd1XTmq6mo0S1wqZZi3-Lh_s-6Uw7p8vtgSwg
    
    

**Response**
    
    
    HTTP/1.1 200 OK
    ETag: "9930c6204b2f14e1a4496569dc200186"
    Date: Fri, 23 Jul 2010 21:27:37 GMT
    Expires: Mon, 01 Jan 1990 00:00:00 GMT
    Cache-Control: no-cache, no-store, must-revalidate
    Content-Length: 175
    Content-Type: text/html
    
    <?xml version='1.0' encoding='UTF-8'?>
    <CopyObjectResult>
      <LastModified>2010-06-17T16:18:08.291Z</LastModified>
      <ETag>"9930c6204b2f14e1a4496569dc200186"</ETag>
    </CopyObjectResult>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
