---
url: https://docs.cloud.google.com/storage/docs/xml-api/put-object-compose/
title: Compose an object \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:50:06.184132+00:00
---

# Compose an object  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/put-object-compose/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Compose an object Stay organized with collections  Save and categorize content based on your preferences. 

The compose operation creates a new object whose contents are the concatenation of a given sequence of up to 32 source objects. The source objects must all reside in the same bucket and use the same [storage class](https://docs.cloud.google.com/storage/docs/storage-classes). The source objects are unaffected by the compose operation, and the resulting composite object does not change if its source objects are replaced or deleted.

Composite objects may be built from source objects that are themselves composite objects.

For more information, see [Composite Objects](https://docs.cloud.google.com/storage/docs/composite-objects).

## Query string parameters

Parameter | Description | Required  
---|---|---  
`[compose](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#compose)` |  Issues a [compose](https://docs.cloud.google.com/storage/docs/composite-objects) request. Requires a ComposeRequest XML document in the request body.  | No  
  
See [signed URL query string parameters](https://docs.cloud.google.com/storage/docs/authentication/canonical-requests#required-query-parameters) for information on the parameters you include when creating and using [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).

## Request headers

In addition to [common request headers](https://docs.cloud.google.com/storage/docs/xml-api/put-object#request-headers), the following can be used.

Header | Description | Required  
---|---|---  
`[Content-Encoding](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentencoding)` | The compression algorithm that was used to compress the composite object. | No  
`[Content-Disposition](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentdisposition)` | A header that specifies presentational information about how the object data is to be transmitted. | No  
`[x-goog-acl](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogacl)` | The predefined ACL that you want to apply to the composite object. | No  
`[x-goog-custom-time](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogcustomtime)` | A user-specified date and time. | No  
`[x-goog-encryption-kms-key-name](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogencryptionkmskeyname)` | The [customer-managed encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys) to use to encrypt the composed object. | No  
`[x-goog-meta-](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogmeta)` | An extension header that can be used to store [custom metadata](https://docs.cloud.google.com/storage/docs/metadata#custom-metadata). | No  
`[x-goog-object-lock-mode](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogobjectlockmode)` | Mode of the object's [retention configuration](https://docs.cloud.google.com/storage/docs/object-lock). `GOVERNANCE` corresponds to unlocked mode, and `COMPLIANCE` corresponds to locked mode. If this header is specified, `x-goog-object-lock-retain-until-date` must also be specified. | No  
``[x-goog-object-lock-retain-until-date](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogobjectlockretainuntildate)`` | A date and time represented in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) UTC format that determines the time until which the object is retained as immutable. If this header is specified, `x-goog-object-lock-mode` must also be specified. | No  
  
To compose objects encrypted by a customer-supplied encryption key, use the [headers listed on the Encryption page](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys#headers) in your request.

## Request body elements

The following request body elements are applicable only if you use the `compose` query string parameter to issue a [compose request](https://docs.cloud.google.com/storage/docs/composite-objects).

Element | Description  
---|---  
`ComposeRequest` | Container for a compose request.  
`Component` | Container for a compose request component argument.  
`Name` | Object name for a compose request component.  
`Generation` | Generation number for a compose request component.  
`IfGenerationMatch` | Expected current generation number for a compose request component. The request will fail if the component object has a different generation.  
  
## Request syntax
    
    
    PUT /OBJECT_NAME?compose HTTP/1.1
    Host: BUCKET_NAME.storage.googleapis.com
    Date: DATE
    Content-Length: REQUEST_BODY_LENGTH
    Authorization: AUTHENTICATION_STRING
    
    <ComposeRequest>
      <Component>
        <Name>component-obj-1</Name>
      </Component>
      <Component>
        <Name>component-obj-2</Name>
        <Generation>1361471441094000</Generation>
      </Component>
      <Component>
        <Name>component-obj-3</Name>
        <IfGenerationMatch>1361471441094000</IfGenerationMatch>
      </Component>
    </ComposeRequest>
    

## Response headers

The request can return a variety of response headers depending on the request headers you use.

## Response body elements

The response does not include an XML document in the response body.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
