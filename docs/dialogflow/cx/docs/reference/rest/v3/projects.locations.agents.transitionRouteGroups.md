---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.transitionRouteGroups
title: REST Resource: projects.locations.agents.transitionRouteGroups \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:23.174823+00:00
---

# REST Resource: projects.locations.agents.transitionRouteGroups  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.transitionRouteGroups

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  REST Resource: projects.locations.agents.transitionRouteGroups Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: TransitionRouteGroup
    * JSON representation
  * Methods



## Resource: TransitionRouteGroup

A TransitionRouteGroup represents a group of `[`TransitionRoutes`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/TransitionRoute)` to be used by a `[Page](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages#Page)`.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "transitionRoutes": [
        {
          object ([TransitionRoute](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/TransitionRoute))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` The unique identifier of the transition route group. `[TransitionRouteGroups.CreateTransitionRouteGroup](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.transitionRouteGroups/create#google.cloud.dialogflow.cx.v3.TransitionRouteGroups.CreateTransitionRouteGroup)` populates the name automatically. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/transitionRouteGroups/<TransitionRouteGroupID>` .  
`displayName` |  `string` Required. The human-readable name of the transition route group, unique within the flow. The display name can be no longer than 30 characters.  
`transitionRoutes[]` |  `object (`[TransitionRoute](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/TransitionRoute)`)` Transition routes associated with the `[TransitionRouteGroup](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.transitionRouteGroups#TransitionRouteGroup)`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.transitionRouteGroups/create)`

|  Creates an `[TransitionRouteGroup](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.transitionRouteGroups#TransitionRouteGroup)` in the specified flow.  
  
### `[delete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.transitionRouteGroups/delete)`

|  Deletes the specified `[TransitionRouteGroup](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.transitionRouteGroups#TransitionRouteGroup)`.  
  
### `[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.transitionRouteGroups/get)`

|  Retrieves the specified `[TransitionRouteGroup](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.transitionRouteGroups#TransitionRouteGroup)`.  
  
### `[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.transitionRouteGroups/list)`

|  Returns the list of all transition route groups in the specified flow.  
  
### `[patch](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.transitionRouteGroups/patch)`

|  Updates the specified `[TransitionRouteGroup](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.transitionRouteGroups#TransitionRouteGroup)`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
