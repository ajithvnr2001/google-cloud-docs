---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.flows/list/
title: Method: projects.locations.agents.flows.list \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:51:35.300278+00:00
---

# Method: projects.locations.agents.flows.list  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.flows/list/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  Method: projects.locations.agents.flows.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Returns the list of all flows in the specified agent.

### HTTP request

`GET https://{endpoint}/v3beta1/{parent=projects/*/locations/*/agents/*}/flows`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The agent containing the flows. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dialogflow.flows.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of items to return in a single page. By default 100 and at most 1000.  
`pageToken` |  `string` The nextPageToken value returned from a previous list request.  
`languageCode` |  `string` The language to list flows for. The following fields are language dependent:

  * `Flow.event_handlers.trigger_fulfillment.messages`
  * `Flow.event_handlers.trigger_fulfillment.conditional_cases`
  * `Flow.transition_routes.trigger_fulfillment.messages`
  * `Flow.transition_routes.trigger_fulfillment.conditional_cases`

If not specified, the agent's default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used.  
  
### Request body

The request body must be empty.

### Response body

The response message for `[Flows.ListFlows](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.flows/list#google.cloud.dialogflow.cx.v3beta1.Flows.ListFlows)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "flows": [
        {
          object ([Flow](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.flows#Flow))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`flows[]` |  `object (`[Flow](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.flows#Flow)`)` The list of flows. There will be a maximum number of items returned based on the pageSize field in the request.  
`nextPageToken` |  `string` Token to retrieve the next page of results, or empty if there are no more results in the list.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dialogflow`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
