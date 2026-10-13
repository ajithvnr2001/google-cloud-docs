---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows/import/
title: Method: projects.locations.agents.flows.import \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:09.067879+00:00
---

# Method: projects.locations.agents.flows.import  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows/import/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  Method: projects.locations.agents.flows.import Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * ImportOption
  * FlowImportStrategy
    * JSON representation
  * Try it!



Imports the specified flow to the specified agent from a binary file.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: `[ImportFlowResponse](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ImportFlowResponse)`



Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

### HTTP request

`POST https://{endpoint}/v3/{parent=projects/*/locations/*/agents/*}/flows:import`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The agent to import the flow into. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dialogflow.flows.create`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "importOption": enum ([ImportOption](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows/import#ImportOption)),
      "flowImportStrategy": {
        object ([FlowImportStrategy](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows/import#FlowImportStrategy))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "flowUri": string,
      "flowContent": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`importOption` |  `enum (`[ImportOption](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows/import#ImportOption)`)` Flow import mode. If not specified, `KEEP` is assumed.  
`flowImportStrategy` |  `object (`[FlowImportStrategy](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows/import#FlowImportStrategy)`)` Optional. Specifies the import strategy used when resolving resource conflicts.  
Required. The flow to import. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`flowUri` |  `string` The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to import flow from. The format of this URI must be `gs://<bucket-name>/<object-name>`.Dialogflow performs a read operation for the Cloud Storage object on the caller's behalf, so your request authentication must have read permissions for the object. For more information, see [Dialogflow access control](https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage).  
`flowContent` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Uncompressed raw byte content for flow.A base64-encoded string.  
End of mutually exclusive fields.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dialogflow`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## ImportOption

Import option.

Enums  
---  
`IMPORT_OPTION_UNSPECIFIED` | Unspecified. Treated as `KEEP`.  
`KEEP` | Always respect settings in exported flow content. It may cause a import failure if some settings (e.g. custom NLU) are not supported in the agent to import into.  
`FALLBACK` | Fallback to default settings if some settings are not supported in the agent to import into. E.g. Standard NLU will be used if custom NLU is not available.  
  
## FlowImportStrategy

The flow import strategy used for resource conflict resolution associated with an `ImportFlowRequest`.

JSON representation  
---  
      
    
    {
      "globalImportStrategy": enum ([ImportStrategy](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ImportStrategy))
    }  
  
Fields  
---  
`globalImportStrategy` |  `enum (`[ImportStrategy](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ImportStrategy)`)` Optional. Import strategy for resource conflict resolution, applied globally throughout the flow. It will be applied for all display name conflicts in the imported content. If not specified, 'CREATE_NEW' is assumed.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
