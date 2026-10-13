---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents
title: REST Resource: projects.locations.collections.dataStores.branches.documents \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:27:08.054476+00:00
---

# REST Resource: projects.locations.collections.dataStores.branches.documents  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Reference ](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis)



Send feedback 

#  REST Resource: projects.locations.collections.dataStores.branches.documents Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Document
    * JSON representation
    * Content
      * JSON representation
    * AclInfo
      * JSON representation
    * AccessRestriction
      * JSON representation
    * Principal
      * JSON representation
    * IndexStatus
      * JSON representation
  * Methods



## Resource: Document

Document captures all raw metadata information of items to be recommended or searched.

JSON representation  
---  
      
    
    {
      "name": string,
      "id": string,
      "schemaId": string,
      "content": {
        object ([Content](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents#Document.Content))
      },
      "parentDocumentId": string,
      "derivedStructData": {
        object
      },
      "aclInfo": {
        object ([AclInfo](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents#Document.AclInfo))
      },
      "indexTime": string,
      "indexStatus": {
        object ([IndexStatus](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents#Document.IndexStatus))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "structData": {
        object
      },
      "jsonData": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Immutable. The full resource name of the document. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStore}/branches/{branch}/documents/{documentId}`.This field must be a UTF-8 encoded string with a length limit of 1024 characters.  
`id` |  `string` Immutable. The identifier of the document.Id should conform to [RFC-1034](https://tools.ietf.org/html/rfc1034) standard with a length limit of 128 characters.  
`schemaId` |  `string` The identifier of the schema located in the same data store.  
`content` |  `object (`[Content](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents#Document.Content)`)` The unstructured data linked to this document. Content can only be set and must be set if this document is under a `CONTENT_REQUIRED` data store.  
`parentDocumentId` |  `string` The identifier of the parent document. Currently supports at most two level document hierarchy.Id should conform to [RFC-1034](https://tools.ietf.org/html/rfc1034) standard with a length limit of 63 characters.  
`derivedStructData` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Output only. This field is OUTPUT_ONLY. It contains derived data that are not in the original input document.  
`aclInfo` |  `object (`[AclInfo](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents#Document.AclInfo)`)` Access control information for the document.  
`indexTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the document was last indexed.If this field is populated, it means the document has been indexed. While documents typically become searchable within seconds of indexing, it can sometimes take up to a few hours.If this field is not populated, it means the document has never been indexed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`indexStatus` |  `object (`[IndexStatus](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents#Document.IndexStatus)`)` Output only. The index status of the document.

  * If document is indexed successfully, the indexTime field is populated.
  * Otherwise, if document is not indexed due to errors, the errorSamples field is populated.
  * Otherwise, if document's index is in progress, the pendingMessage field is populated.

  
Data representation. One of `[struct_data](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents#Document.FIELDS.struct_data)` or `[json_data](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents#Document.FIELDS.json_data)` should be provided otherwise an `INVALID_ARGUMENT` error is thrown. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`structData` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` The structured JSON data for the document. It should conform to the registered `[Schema](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.schemas#Schema)` or an `INVALID_ARGUMENT` error is thrown.  
`jsonData` |  `string` The JSON string representation of the document. It should conform to the registered `[Schema](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.schemas#Schema)` or an `INVALID_ARGUMENT` error is thrown.  
End of mutually exclusive fields.  
  
### Content

Unstructured data linked to this document.

JSON representation  
---  
      
    
    {
      "mimeType": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "rawBytes": string,
      "uri": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`mimeType` |  `string` The MIME type of the content. Supported types:

  * `application/pdf` (PDF, only native PDFs are supported for now)
  * `text/html` (HTML)
  * `text/plain` (TXT)
  * `application/xml` or `text/xml` (XML)
  * `application/json` (JSON)
  * `application/vnd.openxmlformats-officedocument.wordprocessingml.document` (DOCX)
  * `application/vnd.openxmlformats-officedocument.presentationml.presentation` (PPTX)
  * `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` (XLSX)
  * `application/vnd.ms-excel.sheet.macroenabled.12` (XLSM)

The following types are supported only if layout parser is enabled in the data store:

  * `image/bmp` (BMP)
  * `image/gif` (GIF)
  * `image/jpeg` (JPEG)
  * `image/png` (PNG)
  * `image/tiff` (TIFF)

See <https://www.iana.org/assignments/media-types/media-types.xhtml>.  
The content of the unstructured document. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`rawBytes` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The content represented as a stream of bytes. The maximum length is 1,000,000 bytes (1 MB / ~0.95 MiB).Note: As with all `bytes` fields, this field is represented as pure binary in Protocol Buffers and base64-encoded string in JSON. For example, `abc123!?$*&()'-=@~` should be represented as `YWJjMTIzIT8kKiYoKSctPUB+` in JSON. See <https://developers.google.com/protocol-buffers/docs/proto3#json>.A base64-encoded string.  
`uri` |  `string` The URI of the content. Only Cloud Storage URIs (e.g. `gs://bucket-name/path/to/file`) are supported. The maximum file size is 2.5 MB for text-based formats, 200 MB for other formats.  
End of mutually exclusive fields.  
  
### AclInfo

ACL Information of the Document.

JSON representation  
---  
      
    
    {
      "readers": [
        {
          object ([AccessRestriction](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents#Document.AccessRestriction))
        }
      ]
    }  
  
Fields  
---  
`readers[]` |  `object (`[AccessRestriction](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents#Document.AccessRestriction)`)` Readers of the document.  
  
### AccessRestriction

AclRestriction to model complex inheritance restrictions.

Example: Modeling a "Both Permit" inheritance, where to access a child document, user needs to have access to parent document.

Document Hierarchy - Space_S --> Page_P.

Readers: Space_S: group_1, user_1 Page_P: group_2, group_3, user_2

Space_S ACL Restriction - { "aclInfo": { "readers": [ { "principals": [ { "groupId": "group_1" }, { "userId": "user_1" } ] } ] } }

Page_P ACL Restriction. { "aclInfo": { "readers": [ { "principals": [ { "groupId": "group_2" }, { "groupId": "group_3" }, { "userId": "user_2" } ], }, { "principals": [ { "groupId": "group_1" }, { "userId": "user_1" } ], } ] } }

JSON representation  
---  
      
    
    {
      "principals": [
        {
          object ([Principal](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents#Document.Principal))
        }
      ],
      "idpWide": boolean
    }  
  
Fields  
---  
`principals[]` |  `object (`[Principal](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents#Document.Principal)`)` List of principals.  
`idpWide` |  `boolean` All users within the Identity Provider.  
  
### Principal

Principal identifier of a user or a group.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "userId": string,
      "groupId": string,
      "externalEntityId": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Union field principal. Principal can be a user or a group. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`userId` |  `string` User identifier. For Google Workspace user account, userId should be the google workspace user email. For non-google identity provider user account, userId is the mapped user identifier configured during the workforcepool config.  
`groupId` |  `string` Group identifier. For Google Workspace user account, groupId should be the google workspace group email. For non-google identity provider user account, groupId is the mapped group identifier configured during the workforcepool config.  
`externalEntityId` |  `string` For 3P application identities which are not present in the customer identity provider.  
End of mutually exclusive fields.  
  
### IndexStatus

Index status of the document.

JSON representation  
---  
      
    
    {
      "indexTime": string,
      "errorSamples": [
        {
          object ([Status](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/Shared.Types/ListOperationsResponse#Status))
        }
      ],
      "pendingMessage": string
    }  
  
Fields  
---  
`indexTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time when the document was indexed. If this field is populated, it means the document has been indexed. While documents typically become searchable within seconds of indexing, it can sometimes take up to a few hours.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`errorSamples[]` |  `object (`[Status](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/Shared.Types/ListOperationsResponse#Status)`)` A sample of errors encountered while indexing the document. If this field is populated, the document is not indexed due to errors.  
`pendingMessage` |  `string` Immutable. The message indicates the document index is in progress. If this field is populated, the document index is pending.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents/create)`

|  Creates a `[Document](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents#Document)`.  
  
### `[delete](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents/delete)`

|  Deletes a `[Document](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents#Document)`.  
  
### `[get](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents/get)`

|  Gets a `[Document](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents#Document)`.  
  
### `[getProcessedDocument](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents/getProcessedDocument)`

|  Gets the parsed layout information for a `[Document](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents#Document)`.  
  
### `[import](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents/import)`

|  Bulk import of multiple `[Document](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents#Document)`s.  
  
### `[list](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents/list)`

|  Gets a list of `[Document](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents#Document)`s.  
  
### `[patch](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents/patch)`

|  Updates a `[Document](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents#Document)`.  
  
### `[purge](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents/purge)`

|  Permanently deletes all selected `[Document](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents#Document)`s in a branch.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-14 UTC."],[],[]] 
