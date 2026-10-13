---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.locations.agent/export/
title: Method: projects.locations.agent.export \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:45:02.129123+00:00
---

# Method: projects.locations.agent.export  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.locations.agent/export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  Method: projects.locations.agent.export Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Exports the specified agent to a ZIP file.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: `[ExportAgentResponse](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/ExportAgentResponse)`



### HTTP request

`POST https://{endpoint}/v2beta1/{parent=projects/*/locations/*}/agent:export`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The project that the agent to export is associated with. Format: `projects/<Project ID>` or `projects/<Project ID>/locations/<Location ID>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dialogflow.agents.export`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "agentUri": string
    }  
  
Fields  
---  
`agentUri` |  `string` Optional. The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to export the agent to. The format of this URI must be `gs://<bucket-name>/<object-name>`. If left unspecified, the serialized agent is returned inline.Dialogflow performs a write operation for the Cloud Storage object on the caller's behalf, so your request authentication must have write permissions for the object. For more information, see [Dialogflow access control](https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage).  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.locations.operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dialogflow`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
