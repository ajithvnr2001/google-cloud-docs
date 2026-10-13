---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents/import/
title: Method: projects.locations.agents.intents.import \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:13.754698+00:00
---

# Method: projects.locations.agents.intents.import  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents/import/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  Method: projects.locations.agents.intents.import Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * MergeOption
  * Try it!



Imports the specified intents into the agent.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

  * `metadata`: `[ImportIntentsMetadata](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ImportIntentsMetadata)`
  * `response`: `[ImportIntentsResponse](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ImportIntentsResponse)`



### HTTP request

`POST https://{endpoint}/v3/{parent=projects/*/locations/*/agents/*}/intents:import`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The agent to import the intents into. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dialogflow.intents.create`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "mergeOption": enum ([MergeOption](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents/import#MergeOption)),
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "intentsUri": string,
      "intentsContent": {
        object ([InlineSource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/InlineSource))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`mergeOption` |  `enum (`[MergeOption](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents/import#MergeOption)`)` Merge option for importing intents. If not specified, `REJECT` is assumed.  
Required. The intents to import. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`intentsUri` |  `string` The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to import intents from. The format of this URI must be `gs://<bucket-name>/<object-name>`.Dialogflow performs a read operation for the Cloud Storage object on the caller's behalf, so your request authentication must have read permissions for the object. For more information, see [Dialogflow access control](https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage).  
`intentsContent` |  `object (`[InlineSource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/InlineSource)`)` Uncompressed byte content of intents.  
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
`MERGE_OPTION_UNSPECIFIED` | Unspecified. Should not be used.  
`REJECT` | DEPRECATED: Please use [REPORT_CONFLICT][ImportIntentsRequest.REPORT_CONFLICT] instead. Fail the request if there are intents whose display names conflict with the display names of intents in the agent.This item is deprecated!  
`REPLACE` | Replace the original intent in the agent with the new intent when display name conflicts exist.  
`MERGE` | Merge the original intent with the new intent when display name conflicts exist.  
`RENAME` | Create new intents with new display names to differentiate them from the existing intents when display name conflicts exist.  
`REPORT_CONFLICT` | Report conflict information if display names conflict is detected. Otherwise, import intents.  
`KEEP` | Keep the original intent and discard the conflicting new intent when display name conflicts exist.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
