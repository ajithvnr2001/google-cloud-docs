---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.uniqueEntities/addNote/
title: Method: uniqueEntities.addNote \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:06:24.947749+00:00
---

# Method: uniqueEntities.addNote  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.uniqueEntities/addNote/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: uniqueEntities.addNote Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions
  * UniqueEntityAddNote
    * JSON representation



**Full name** : projects.locations.instances.uniqueEntities.addNote

Adds a comment or note to a unique entity. Use this method to record observations or findings related to a specific entity for future investigation or collaboration.

### HTTP request

`POST https://{endpoint}/v1beta/{parent}/uniqueEntities:addNote`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Format: projects/{project}/locations/{location}/instances/{instance}/uniqueEntities  
  
### Request body

The request body contains an instance of `[UniqueEntityAddNote](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.uniqueEntities/addNote#UniqueEntityAddNote)`.

### Response body

If successful, the response body is an empty JSON object.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `chronicle.uniqueEntities.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## UniqueEntityAddNote

Request message for UniqueEntityAddNote.

JSON representation  
---  
      
    
    {
      "author": string,
      "content": string,
      "entityIdentifier": string,
      "entityType": string,
      "entityEnvironment": string
    }  
  
Fields  
---  
`author` |  `string` Required. The author of the note.  
`content` |  `string` Required. The content of the note.  
`entityIdentifier` |  `string` Required. The entity identifier.  
`entityType` |  `string` Required. The entity type.  
`entityEnvironment` |  `string` Required. The entity environment.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
