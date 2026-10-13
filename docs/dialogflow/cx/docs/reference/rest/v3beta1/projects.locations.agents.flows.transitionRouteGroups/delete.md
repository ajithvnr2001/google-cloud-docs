---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.flows.transitionRouteGroups/delete/
title: Method: projects.locations.agents.flows.transitionRouteGroups.delete \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:35:55.311248+00:00
---

# Method: projects.locations.agents.flows.transitionRouteGroups.delete  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.flows.transitionRouteGroups/delete/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  Method: projects.locations.agents.flows.transitionRouteGroups.delete Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Deletes the specified `[TransitionRouteGroup](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.flows.transitionRouteGroups#TransitionRouteGroup)`.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

### HTTP request

`DELETE https://{endpoint}/v3beta1/{name=projects/*/locations/*/agents/*/flows/*/transitionRouteGroups/*}`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the `[TransitionRouteGroup](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.flows.transitionRouteGroups#TransitionRouteGroup)` to delete. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/transitionRouteGroups/<TransitionRouteGroupID>` or `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/transitionRouteGroups/<TransitionRouteGroupID>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dialogflow.transitionRouteGroups.delete`

  
  
### Query parameters

Parameters  
---  
`force` |  `boolean` This field has no effect for transition route group that no page is using. If the transition route group is referenced by any page:

  * If `force` is set to false, an error will be returned with message indicating pages that reference the transition route group.
  * If `force` is set to true, Dialogflow will remove the transition route group, as well as any reference to it.

  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body is an empty JSON object.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dialogflow`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
