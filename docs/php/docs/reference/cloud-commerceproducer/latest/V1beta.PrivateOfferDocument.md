---
url: https://docs.cloud.google.com/php/docs/reference/cloud-commerceproducer/latest/V1beta.PrivateOfferDocument
title: Google Cloud Commerce Producer V1beta Client - Class PrivateOfferDocument (0.2.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:17:54.781312+00:00
---

# Google Cloud Commerce Producer V1beta Client - Class PrivateOfferDocument (0.2.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-commerceproducer/latest/V1beta.PrivateOfferDocument

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Commerce Producer V1beta Client - Class PrivateOfferDocument (0.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.2.0 (latest)  0.1.3 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Commerce Producer V1beta Client class PrivateOfferDocument.

Message describing the PrivateOfferDocument resource.

Used to attach documents to a private offer in state DRAFT. Once a private offer is no longer in state DRAFT, the set of child documents is immutable. Existing documents cannot be updated or deleted, and new documents cannot be added. A private offer may have at most one document of each type, and may not have both a standard EULA and a custom EULA. Which document types are required, optional, or not permitted depends on the service the offer is for, and is returned in `Service.document_requirement`.

Generated from protobuf message `google.cloud.commerceproducer.v1beta.PrivateOfferDocument`

## Namespace

Google \ Cloud \ CommerceProducer \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ inline_content` |  `string`   
Optional. Byte content of an unstructured document. Max size: 4MB  
`↳ name` |  `string`   
Identifier. Name of the resource.  
`↳ create_time` |  `Google\Protobuf\Timestamp`   
Output only. The creation time of the resource.  
`↳ update_time` |  `Google\Protobuf\Timestamp`   
Output only. The last update time of the resource.  
`↳ document_type` |  `int`   
Required. The classification type of the document. Used to distinguish between different types of documents that may be attached to a private offer for different business purposes.  
`↳ mime_type` |  `string`   
Optional. The MIME type of the document. Used to distinguish between different document formats. Supported formats (which may be expanded in the future) - 'application/pdf'  
  
### getInlineContent

Optional. Byte content of an unstructured document.

Max size: 4MB

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasInlineContent

### setInlineContent

Optional. Byte content of an unstructured document.

Max size: 4MB

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getName

Identifier. Name of the resource.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Identifier. Name of the resource.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCreateTime

Output only. The creation time of the resource.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasCreateTime

### clearCreateTime

### setCreateTime

Output only. The creation time of the resource.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUpdateTime

Output only. The last update time of the resource.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasUpdateTime

### clearUpdateTime

### setUpdateTime

Output only. The last update time of the resource.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDocumentType

Required. The classification type of the document.

Used to distinguish between different types of documents that may be attached to a private offer for different business purposes.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [DocumentType](https://docs.cloud.google.com/php/docs/reference/cloud-commerceproducer/latest/V1beta.PrivateOfferDocument.DocumentType).  
  
### setDocumentType

Required. The classification type of the document.

Used to distinguish between different types of documents that may be attached to a private offer for different business purposes.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [DocumentType](https://docs.cloud.google.com/php/docs/reference/cloud-commerceproducer/latest/V1beta.PrivateOfferDocument.DocumentType).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMimeType

Optional. The MIME type of the document.

Used to distinguish between different document formats. Supported formats (which may be expanded in the future)

  * 'application/pdf'



**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setMimeType

Optional. The MIME type of the document.

Used to distinguish between different document formats. Supported formats (which may be expanded in the future)

  * 'application/pdf'



**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getContent

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
