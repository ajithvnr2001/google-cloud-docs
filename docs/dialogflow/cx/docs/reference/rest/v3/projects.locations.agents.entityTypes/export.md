---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.entityTypes/export/
title: Method: projects.locations.agents.entityTypes.export \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:49:50.567132+00:00
---

# Method: projects.locations.agents.entityTypes.export  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.entityTypes/export/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  Method: projects.locations.agents.entityTypes.export Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * DataFormat
  * Try it!



Exports the selected entity types.

### HTTP request

`POST https://{endpoint}/v3/{parent=projects/*/locations/*/agents/*}/entityTypes:export`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The name of the parent agent to export entity types. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dialogflow.entityTypes.get`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "entityTypes": [
        string
      ],
      "dataFormat": enum ([DataFormat](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.entityTypes/export#DataFormat)),
      "languageCode": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "entityTypesUri": string,
      "entityTypesContentInline": boolean
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`entityTypes[]` |  `string` Required. The name of the entity types to export. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/entityTypes/<EntityTypeID>`.  
`dataFormat` |  `enum (`[DataFormat](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.entityTypes/export#DataFormat)`)` Optional. The data format of the exported entity types. If not specified, `BLOB` is assumed.  
`languageCode` |  `string` Optional. The language to retrieve the entity type for. The following fields are language dependent:

  * `EntityType.entities.value`
  * `EntityType.entities.synonyms`
  * `EntityType.excluded_phrases.value`

If not specified, all language dependent fields will be retrieved. [Many languages](https://cloud.google.com/dialogflow/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used.  
The destination to export. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`entityTypesUri` |  `string` Optional. The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to export the entity types to. The format of this URI must be `gs://<bucket-name>/<object-name>`.Dialogflow performs a write operation for the Cloud Storage object on the caller's behalf, so your request authentication must have write permissions for the object. For more information, see [Dialogflow access control](https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage).  
`entityTypesContentInline` |  `boolean` Optional. The option to return the serialized entity types inline.  
End of mutually exclusive fields.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dialogflow`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## DataFormat

Data format of the exported entity types.

Enums  
---  
`DATA_FORMAT_UNSPECIFIED` | Unspecified format. Treated as `BLOB`.  
`BLOB` | EntityTypes will be exported as raw bytes.  
`JSON_PACKAGE` | EntityTypes will be exported in JSON Package format.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
