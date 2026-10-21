---
url: https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers.documents
title: REST Resource: projects.locations.privateOffers.documents \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:14.180510+00:00
---

# REST Resource: projects.locations.privateOffers.documents  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers.documents

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ APIs and Reference ](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference)



Send feedback 

#  REST Resource: projects.locations.privateOffers.documents Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: PrivateOfferDocument
    * JSON representation
  * Methods



## Resource: PrivateOfferDocument

Message describing the PrivateOfferDocument resource. Used to attach documents to a private offer in state DRAFT. Once a private offer is no longer in state DRAFT, the set of child documents is immutable. Existing documents cannot be updated or deleted, and new documents cannot be added.

A private offer may have at most one document of each type, and may not have both a standard EULA and a custom EULA.

Which document types are required, optional, or not permitted depends on the service the offer is for, and is returned in `Service.document_requirement`.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "documentType": enum ([DocumentType](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/DocumentType)),
      "mimeType": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "inlineContent": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Identifier. Name of the resource.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The creation time of the resource.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last update time of the resource.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`documentType` |  `enum (`[DocumentType](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/DocumentType)`)` Required. The classification type of the document. Used to distinguish between different types of documents that may be attached to a private offer for different business purposes.  
`mimeType` |  `string` Optional. The MIME type of the document. Used to distinguish between different document formats. Supported formats (which may be expanded in the future)

  * 'application/pdf'

  
Mechanism for storing the document content. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`inlineContent` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Optional. Byte content of an unstructured document. Max size: 4MBA base64-encoded string.  
End of mutually exclusive fields.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers.documents/create)`

|  Creates a new PrivateOfferDocument in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers.documents/delete)`

|  Deletes the target PrivateOfferDocument.  
  
### `[get](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers.documents/get)`

|  Gets details of a single PrivateOfferDocument.  
  
### `[list](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers.documents/list)`

|  Lists PrivateOfferDocuments for the given parent.  
  
### `[patch](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers.documents/patch)`

|  Updates the target PrivateOfferDocument.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
