---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseComments
title: REST Resource: projects.locations.instances.cases.caseComments \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:37:24.824140+00:00
---

# REST Resource: projects.locations.instances.cases.caseComments  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseComments

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.cases.caseComments Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: CaseComment
    * JSON representation
    * CaseAttachment
      * JSON representation
  * Methods



## Resource: CaseComment

This service is available for customers who migrated SOAR to a customer managed project and have the Chronicle API enabled. Case Comment - Chronicle SOAR Case Comment.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "user": string,
      "comment": string,
      "deletionInvoker": string,
      "alertIdentifier": string,
      "caseAttachment": {
        object ([CaseAttachment](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseComments#CaseComment.CaseAttachment))
      },
      "userOwnerFullName": string,
      "lastEditorFullName": string,
      "deletedByUser": string,
      "case": string,
      "isFavorite": boolean,
      "isDeleted": boolean
    }  
  
Fields  
---  
`name` |  `string` Output only. Identifier. The unique name(ID) of the CaseComment. Format: projects/{project}/locations/{location}/instances/{instance}/cases/{case}/caseComments/{caseComment}  
`createTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The timestamp when the comment was created.  
`updateTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The timestamp when the comment was last updated.  
`user` |  `string` Output only. User owner of the comment.  
`comment` |  `string` Required. The content of the comment.  
`deletionInvoker` |  `string` Output only. The user who deleted the comment.  
`alertIdentifier` |  `string` Optional. The alert associated with the comment.  
`caseAttachment` |  `object (`[CaseAttachment](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseComments#CaseComment.CaseAttachment)`)` Optional. The attachment associated with the comment.  
`userOwnerFullName` |  `string` Output only. The user who created the comment.  
`lastEditorFullName` |  `string` Output only. The user who last edited the comment.  
`deletedByUser` |  `string` Output only. The user who deleted the comment.  
`case` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The case associated with the comment.  
`isFavorite` |  `boolean` Optional. Whether the comment is marked as a favorite.  
`isDeleted` |  `boolean` Output only. Indicates if the comment has been softly deleted.  
  
### CaseAttachment

Case Attachment of the Case Comment.

JSON representation  
---  
      
    
    {
      "attachmentBase64": string,
      "fileType": string,
      "fileName": string,
      "fileId": string
    }  
  
Fields  
---  
`attachmentBase64` |  `string` Required. Base64 encoded attachment associated with the comment (if exists).  
`fileType` |  `string` Required. The file type of the attachment (if exists).  
`fileName` |  `string` Required. The file name of the attachment (if it exists).  
`fileId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The file id of the attachment.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseComments/create)`

|  Creates a new CaseComment.  
  
### `[delete](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseComments/delete)`

|  Performs a soft delete of a CaseComment.  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseComments/get)`

|  Gets a single CaseComment by its resource name.  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseComments/list)`

|  Lists CaseComments associated with a specific Case.  
  
### `[patch](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases.caseComments/patch)`

|  Updates an existing CaseComment.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
