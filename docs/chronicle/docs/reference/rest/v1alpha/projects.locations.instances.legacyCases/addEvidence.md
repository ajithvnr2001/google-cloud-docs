---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacyCases/addEvidence/
title: Method: legacyCases.addEvidence \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:20:07.484067+00:00
---

# Method: legacyCases.addEvidence  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacyCases/addEvidence/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: legacyCases.addEvidence Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * CaseCommentV2
    * JSON representation
  * EvidenceType



**Full name** : projects.locations.instances.legacyCases.addEvidence

Adds evidence, such as a file attachment, to a specific case. The evidence is recorded on the case wall with an optional description and can be marked as important.

### HTTP request

`POST https://{endpoint}/v1alpha/{name}/legacyCases:addEvidence`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`name` |  `string` Required. The evidence (attachment) of a given case. Format: projects/{project}/locations/{location}/instances/{instance}/legacyCases:addEvidence  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "caseId": string,
      "alertIdentifier": string,
      "base64Blob": string,
      "type": string,
      "description": string,
      "isImportant": boolean
    }  
  
Fields  
---  
`caseId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. CaseId is the ID of the case associated for the action.  
`alertIdentifier` |  `string`  
`base64Blob` |  `string`  
`type` |  `string`  
`description` |  `string`  
`isImportant` |  `boolean`  
  
### Response body

Response message for legacyCases.addEvidence

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "name": string,
      "caseId": string,
      "creator": string,
      "type": string,
      "isImportant": boolean,
      "comment": string,
      "commentId": string,
      "description": string,
      "evidenceThumbnail": string,
      "sizeInKb": integer,
      "isFavorite": boolean,
      "caseCommentV2": {
        object ([CaseCommentV2](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacyCases/addEvidence#CaseCommentV2))
      },
      "evidenceType": enum ([EvidenceType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacyCases/addEvidence#EvidenceType))
    }  
  
Fields  
---  
`name` |  `string`  
`caseId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. CaseId is the ID of the case associated for the action.  
`creator` |  `string`  
`type` |  `string`  
`isImportant` |  `boolean`  
`comment` |  `string`  
`commentId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)`  
`description` |  `string`  
`evidenceThumbnail` |  `string`  
`sizeInKb` |  `integer`  
`isFavorite` |  `boolean`  
`caseCommentV2` |  `object (`[CaseCommentV2](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacyCases/addEvidence#CaseCommentV2)`)`  
`evidenceType` |  `enum (`[EvidenceType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacyCases/addEvidence#EvidenceType)`)`  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `chronicle.cases.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## CaseCommentV2

JSON representation  
---  
      
    
    {
      "title": string,
      "comment": string,
      "isFromWorkflowActivity": boolean,
      "lastEditor": string,
      "isDeleted": boolean,
      "commentForClient": string,
      "modificationTimeUnixTimInMsForClient": string,
      "isFavorite": boolean
    }  
  
Fields  
---  
`title` |  `string`  
`comment` |  `string`  
`isFromWorkflowActivity` |  `boolean`  
`lastEditor` |  `string`  
`isDeleted` |  `boolean`  
`commentForClient` |  `string`  
`modificationTimeUnixTimInMsForClient` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)`  
`isFavorite` |  `boolean`  
  
## EvidenceType

Evidence Type

Enums  
---  
`ATTACHMENT` |   
`DATA` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
