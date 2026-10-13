---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.entityTypes/batchUpdate/
title: Method: projects.agent.entityTypes.batchUpdate \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:32:02.740453+00:00
---

# Method: projects.agent.entityTypes.batchUpdate  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.entityTypes/batchUpdate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  Method: projects.agent.entityTypes.batchUpdate Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Updates/Creates multiple entity types in the specified agent.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: `[BatchUpdateEntityTypesResponse](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/BatchUpdateEntityTypesResponse)`



Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

### HTTP request

`POST https://{endpoint}/v2/{parent=projects/*/agent}/entityTypes:batchUpdate`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The name of the agent to update or create entity types in. Format: `projects/<Project ID>/agent`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dialogflow.entityTypes.batchUpdate`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "languageCode": string,
      "updateMask": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "entityTypeBatchUri": string,
      "entityTypeBatchInline": {
        object ([EntityTypeBatch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/EntityTypeBatch))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`languageCode` |  `string` Optional. The language used to access language-specific data. If not specified, the agent's default language is used. For more information, see [Multilingual intent and entity data](https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity).  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Optional. The mask to control which fields get updated.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
The source of the entity type batch.For each entity type in the batch:

  * If `name` is specified, we update an existing entity type.
  * If `name` is not specified, we create a new entity type. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

  
`entityTypeBatchUri` |  `string` The URI to a Google Cloud Storage file containing entity types to update or create. The file format can either be a serialized proto (of EntityBatch type) or a JSON object. Note: The URI must start with "gs://".  
`entityTypeBatchInline` |  `object (`[EntityTypeBatch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/EntityTypeBatch)`)` The collection of entity types to update or create.  
End of mutually exclusive fields.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dialogflow`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
