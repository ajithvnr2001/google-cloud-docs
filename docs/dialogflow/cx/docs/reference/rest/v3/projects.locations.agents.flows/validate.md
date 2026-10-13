---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows/validate/
title: Method: projects.locations.agents.flows.validate \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:27:37.738575+00:00
---

# Method: projects.locations.agents.flows.validate  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows/validate/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  Method: projects.locations.agents.flows.validate Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Validates the specified flow and creates or updates validation results. Please call this API after the training is completed to get the complete validation results.

### HTTP request

`POST https://{endpoint}/v3/{name=projects/*/locations/*/agents/*/flows/*}:validate`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The flow to validate. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dialogflow.flows.validate`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "languageCode": string
    }  
  
Fields  
---  
`languageCode` |  `string` If not specified, the agent's default language is used.  
  
### Response body

If successful, the response body contains an instance of `[FlowValidationResult](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/FlowValidationResult)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dialogflow`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
