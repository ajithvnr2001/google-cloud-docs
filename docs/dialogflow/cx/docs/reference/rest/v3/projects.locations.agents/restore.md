---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents/restore/
title: Method: projects.locations.agents.restore \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:22:59.694263+00:00
---

# Method: projects.locations.agents.restore  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents/restore/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  Method: projects.locations.agents.restore Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * GitSource
    * JSON representation
  * RestoreOption
  * Try it!



Restores the specified agent from a binary file.

Replaces the current agent with a new one. Note that all existing resources in agent (e.g. intents, entity types, flows) will be removed.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)



Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

### HTTP request

`POST https://{endpoint}/v3/{name=projects/*/locations/*/agents/*}:restore`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the agent to restore into. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dialogflow.agents.restore`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "restoreOption": enum ([RestoreOption](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents/restore#RestoreOption)),
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "agentUri": string,
      "agentContent": string,
      "gitSource": {
        object ([GitSource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents/restore#GitSource))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`restoreOption` |  `enum (`[RestoreOption](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents/restore#RestoreOption)`)` Agent restore mode. If not specified, `KEEP` is assumed.  
Required. The agent to restore. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`agentUri` |  `string` The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to restore agent from. The format of this URI must be `gs://<bucket-name>/<object-name>`.Dialogflow performs a read operation for the Cloud Storage object on the caller's behalf, so your request authentication must have read permissions for the object. For more information, see [Dialogflow access control](https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage).  
`agentContent` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Uncompressed raw byte content for agent.A base64-encoded string.  
`gitSource` |  `object (`[GitSource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents/restore#GitSource)`)` Setting for restoring from a git branch  
End of mutually exclusive fields.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dialogflow`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## GitSource

Settings for restoring from a git branch

JSON representation  
---  
      
    
    {
      "trackingBranch": string
    }  
  
Fields  
---  
`trackingBranch` |  `string` tracking branch for the git pull  
  
## RestoreOption

Restore option.

Enums  
---  
`RESTORE_OPTION_UNSPECIFIED` | Unspecified. Treated as KEEP.  
`KEEP` | Always respect the settings from the exported agent file. It may cause a restoration failure if some settings (e.g. model type) are not supported in the target agent.  
`FALLBACK` | Fallback to default settings if some settings are not supported in the target agent.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
