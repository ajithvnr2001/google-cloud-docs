---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents/list/
title: Method: projects.locations.agents.intents.list \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:14.300696+00:00
---

# Method: projects.locations.agents.intents.list  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents/list/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  Method: projects.locations.agents.intents.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IntentView
  * Try it!



Returns the list of all intents in the specified agent.

### HTTP request

`GET https://{endpoint}/v3/{parent=projects/*/locations/*/agents/*}/intents`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The agent to list all intents for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dialogflow.intents.list`

  
  
### Query parameters

Parameters  
---  
`languageCode` |  `string` The language to list intents for. The following fields are language dependent:

  * `Intent.training_phrases.parts.text`

If not specified, the agent's default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used.  
`intentView` |  `enum (`[IntentView](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents/list#IntentView)`)` The resource view to apply to the returned intent.  
`pageSize` |  `integer` The maximum number of items to return in a single page. By default 100 and at most 1000.  
`pageToken` |  `string` The nextPageToken value returned from a previous list request.  
  
### Request body

The request body must be empty.

### Response body

The response message for `[Intents.ListIntents](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents/list#google.cloud.dialogflow.cx.v3.Intents.ListIntents)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "intents": [
        {
          object ([Intent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents#Intent))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`intents[]` |  `object (`[Intent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents#Intent)`)` The list of intents. There will be a maximum number of items returned based on the pageSize field in the request.  
`nextPageToken` |  `string` Token to retrieve the next page of results, or empty if there are no more results in the list.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dialogflow`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## IntentView

Represents the options for views of an intent. An intent can be a sizable object. Therefore, we provide a resource view that does not return training phrases in the response.

Enums  
---  
`INTENT_VIEW_UNSPECIFIED` | Not specified. Treated as INTENT_VIEW_FULL.  
`INTENT_VIEW_PARTIAL` | Training phrases field is not populated in the response.  
`INTENT_VIEW_FULL` | All fields are populated.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
