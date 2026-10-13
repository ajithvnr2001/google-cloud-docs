---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.entityTypes/import/
title: Method: projects.locations.agents.entityTypes.import \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:01.028370+00:00
---

# Method: projects.locations.agents.entityTypes.import  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.entityTypes/import/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  Method: projects.locations.agents.entityTypes.import Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * MergeOption
  * Try it!



Imports the specified entitytypes into the agent.

### HTTP request

`POST https://{endpoint}/v3/{parent=projects/*/locations/*/agents/*}/entityTypes:import`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The agent to import the entity types into. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dialogflow.entityTypes.create`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "mergeOption": enum ([MergeOption](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.entityTypes/import#MergeOption)),
      "targetEntityType": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "entityTypesUri": string,
      "entityTypesContent": {
        object ([InlineSource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/InlineSource))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`mergeOption` |  `enum (`[MergeOption](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.entityTypes/import#MergeOption)`)` Required. Merge option for importing entity types.  
`targetEntityType` |  `string` Optional. The target entity type to import into. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/entityTypes/<EntityTypeID>`. If set, there should be only one entity type included in [entityTypes][google.cloud.dialogflow.cx.v3.ImportEntityTypesRequest.entity_types], of which the type should match the type of the target entity type. All `[entities](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.entityTypes#EntityType.FIELDS.entities)` in the imported entity type will be added to the target entity type.  
Required. The entity types to import. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`entityTypesUri` |  `string` The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to import entity types from. The format of this URI must be `gs://<bucket-name>/<object-name>`.Dialogflow performs a read operation for the Cloud Storage object on the caller's behalf, so your request authentication must have read permissions for the object. For more information, see [Dialogflow access control](https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage).  
`entityTypesContent` |  `object (`[InlineSource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/InlineSource)`)` Uncompressed byte content of entity types.  
End of mutually exclusive fields.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dialogflow`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## MergeOption

Merge option when display name conflicts exist during import.

Enums  
---  
`MERGE_OPTION_UNSPECIFIED` | Unspecified. If used, system uses REPORT_CONFLICT as default.  
`REPLACE` | Replace the original entity type in the agent with the new entity type when display name conflicts exist.  
`MERGE` | Merge the original entity type with the new entity type when display name conflicts exist.  
`RENAME` | Create new entity types with new display names to differentiate them from the existing entity types when display name conflicts exist.  
`REPORT_CONFLICT` | Report conflict information if display names conflict is detected. Otherwise, import entity types.  
`KEEP` | Keep the original entity type and discard the conflicting new entity type when display name conflicts exist.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
