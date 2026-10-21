---
url: https://docs.cloud.google.com/storage/docs/xml-api/get-object-encryption/
title: Get an object's encryption information \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:50:08.815654+00:00
---

# Get an object's encryption information  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/get-object-encryption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Get an object's encryption information Stay organized with collections  Save and categorize content based on your preferences. 

Gets an object's encryption information. For more information about encryption in Cloud Storage, see [Data encryption options](https://docs.cloud.google.com/storage/docs/encryption).

You must have `READ` permission to get an object's encryption information.

## Query string parameters

Parameter | Description | Required  
---|---|---  
`[encryption](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#encryption)` | You can use this parameter to determine the type of encryption used on an object. If the [encryption type](https://docs.cloud.google.com/storage/docs/encryption) is customer-managed or customer-supplied, this parameter also provides an identifier for the specific encryption key that was used. | No  
  
See [signed URL query string parameters](https://docs.cloud.google.com/storage/docs/authentication/canonical-requests#required-query-parameters) for information on the parameters you include when creating and using [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).

## Request headers

See [common request headers](https://docs.cloud.google.com/storage/docs/xml-api/get-object#request-headers).

## Request body elements

This request does not include an XML document in the request body.

## Request syntax

The following syntax applies to GET Object requests that use the `encryption` query string parameter.
    
    
    GET /OBJECT_NAME?encryption HTTP/1.1
    Host: BUCKET_NAME.storage.googleapis.com
    Content-Length: 0
    Content-Type: TYPE
    Authorization: AUTHENTICATION_STRING
    

## Response headers

The request can return a variety of response headers depending on the request headers you use, including: [Cache-Control](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#cachecontrol), [Content-Length](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentlength), [Content-Type](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contenttype), [Content-Disposition](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentdisposition), [ETag](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#etag), and [Last-Modified.](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#lastmodified)

## Response body elements

The following response body elements are applicable only if you use the `encryption` query string parameter.

Element | Description  
---|---  
`Encryption` | Container for the object's encryption information.  
`KmsKeyName` | Name of the Cloud Key Management Service key resource used to encrypt the object. Available only when the object is encrypted by a [customer-managed encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys).  
`CustomerEncryption` | Container for customer-supplied encryption information. Available only when the object is encrypted by a [customer-supplied encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys).  
`EncryptionAlgorithm` | The encryption algorithm in use for the customer-supplied encryption key.  
`KeySha256` | An [RFC 4648](https://datatracker.ietf.org/doc/html/rfc4648#section-4) base64-encoded string of the SHA256 hash for the customer-supplied encryption key.  
  
## Examples

The following example retrieves the encryption information for an object named tokyo.jpg encrypted by a customer-managed encryption key.

**Request**
    
    
    GET /tokyo.jpg?encryption HTTP/1.1
    Host: travel-maps.storage.googleapis.com
    Content-Length: 0
    Authorization: Bearer ya29.AHES6ZRVmB7fkLtd1XTmq6mo0S1wqZZi3-Lh_s-6Uw7p8vtgSwg
    

**Response**
    
    
    HTTP/1.1 200 OK
    Content-Length: 164
    Content-Type: application/xml; charset=UTF-8
    Date: Tue, 01 Nov 2016 17:12:32 GMT
    
    <?xml version="1.0" encoding="UTF-8"?>
    <Encryption>
      <KmsKeyName>
        projects/my-project/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME
      </KmsKeyName>
    </Encryption>
    

The following example retrieves the encryption information for an object named paris.jpg encrypted by a customer-supplied encryption key.

**Request**
    
    
    GET /paris.jpg?encryption HTTP/1.1
    Host: travel-maps.storage.googleapis.com
    Content-Length: 0
    Authorization: Bearer ya29.AHES6ZRVmB7fkLtd1XTmq6mo0S1wqZZi3-Lh_s-6Uw7p8vtgSwg
    

**Response**
    
    
    HTTP/1.1 200 OK
    Content-Length: 220
    Content-Type: application/xml; charset=UTF-8
    Date: Tue, 01 Nov 2016 17:12:32 GMT
    
    <?xml version="1.0" encoding="UTF-8"?>
    <Encryption>
      <CustomerEncryption>
        <EncryptionAlgorithm>AES256</EncryptionAlgorithm>
        <KeySha256>Vb/C17P2fk35hguiD/pdLoXJk2j2NlmWmUmnOPsLtfA=</KeySha256>
      </CustomerEncryption>
    </Encryption>
    

The following example retrieves the encryption information for an object named london.jpg not encrypted by a customer-supplied encryption key.

**Request**
    
    
    GET /london.jpg?encryption HTTP/1.1
    Host: travel-maps.storage.googleapis.com
    Content-Length: 0
    Authorization: Bearer ya29.AHES6ZRVmB7fkLtd1XTmq6mo0S1wqZZi3-Lh_s-6Uw7p8vtgSwg
    

**Response**
    
    
    HTTP/1.1 200 OK
    Content-Length: 51
    Content-Type: application/xml; charset=UTF-8
    Date: Tue, 01 Nov 2016 20:35:29 GMT
    
    <?xml version="1.0" encoding="UTF-8"?>
    <Encryption/>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
