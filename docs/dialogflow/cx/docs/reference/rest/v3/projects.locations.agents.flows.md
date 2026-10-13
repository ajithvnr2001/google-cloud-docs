---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows
title: REST Resource: projects.locations.agents.flows \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:06.538847+00:00
---

# REST Resource: projects.locations.agents.flows  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  REST Resource: projects.locations.agents.flows Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Flow
    * JSON representation
  * MultiLanguageSettings
    * JSON representation
  * Methods



## Resource: Flow

Flows represents the conversation flows when you build your chatbot agent.

A flow consists of many pages connected by the transition routes. Conversations always start with the built-in Start Flow (with an all-0 ID). Transition routes can direct the conversation session from the current flow (parent flow) to another flow (sub flow). When the sub flow is finished, Dialogflow will bring the session back to the parent flow, where the sub flow is started.

Usually, when a transition route is followed by a matched intent, the intent will be "consumed". This means the intent won't activate more transition routes. However, when the followed transition route moves the conversation session into a different flow, the matched intent can be carried over and to be consumed in the target flow.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "transitionRoutes": [
        {
          object ([TransitionRoute](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/TransitionRoute))
        }
      ],
      "eventHandlers": [
        {
          object ([EventHandler](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/EventHandler))
        }
      ],
      "transitionRouteGroups": [
        string
      ],
      "nluSettings": {
        object ([NluSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/NluSettings))
      },
      "advancedSettings": {
        object ([AdvancedSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/AdvancedSettings))
      },
      "knowledgeConnectorSettings": {
        object ([KnowledgeConnectorSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/KnowledgeConnectorSettings))
      },
      "inputParameterDefinitions": [
        {
          object ([ParameterDefinition](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ParameterDefinition))
        }
      ],
      "outputParameterDefinitions": [
        {
          object ([ParameterDefinition](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ParameterDefinition))
        }
      ],
      "multiLanguageSettings": {
        object ([MultiLanguageSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows#MultiLanguageSettings))
      },
      "locked": boolean
    }  
  
Fields  
---  
`name` |  `string` The unique identifier of the flow. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>`.  
`displayName` |  `string` Required. The human-readable name of the flow.  
`description` |  `string` The description of the flow. The maximum length is 500 characters. If exceeded, the request is rejected.  
`transitionRoutes[]` |  `object (`[TransitionRoute](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/TransitionRoute)`)` A flow's transition routes serve two purposes:

  * They are responsible for matching the user's first utterances in the flow.
  * They are inherited by every page's [transition routes][Page.transition_routes] and can support use cases such as the user saying "help" or "can I talk to a human?", which can be handled in a common way regardless of the current page. Transition routes defined in the page have higher priority than those defined in the flow.

TransitionRoutes are evaluated in the following order:

  * TransitionRoutes with intent specified.
  * TransitionRoutes with only condition specified.

TransitionRoutes with intent specified are inherited by pages in the flow.  
`eventHandlers[]` |  `object (`[EventHandler](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/EventHandler)`)` A flow's event handlers serve two purposes:

  * They are responsible for handling events (e.g. no match, webhook errors) in the flow.
  * They are inherited by every page's [event handlers][Page.event_handlers], which can be used to handle common events regardless of the current page. Event handlers defined in the page have higher priority than those defined in the flow.

Unlike `[transitionRoutes](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows#Flow.FIELDS.transition_routes)`, these handlers are evaluated on a first-match basis. The first one that matches the event get executed, with the rest being ignored.  
`transitionRouteGroups[]` |  `string` A flow's transition route group serve two purposes:

  * They are responsible for matching the user's first utterances in the flow.
  * They are inherited by every page's [transition route groups][Page.transition_route_groups]. Transition route groups defined in the page have higher priority than those defined in the flow.

Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/transitionRouteGroups/<TransitionRouteGroupID>` or `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/transitionRouteGroups/<TransitionRouteGroupID>` for agent-level groups.  
`nluSettings` |  `object (`[NluSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/NluSettings)`)` NLU related settings of the flow.  
`advancedSettings` |  `object (`[AdvancedSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/AdvancedSettings)`)` Hierarchical advanced settings for this flow. The settings exposed at the lower level overrides the settings exposed at the higher level.  
`knowledgeConnectorSettings` |  `object (`[KnowledgeConnectorSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/KnowledgeConnectorSettings)`)` Optional. Knowledge connector configuration.  
`inputParameterDefinitions[]` |  `object (`[ParameterDefinition](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ParameterDefinition)`)` Optional. Defined structured input parameters for this flow.  
`outputParameterDefinitions[]` |  `object (`[ParameterDefinition](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ParameterDefinition)`)` Optional. Defined structured output parameters for this flow.  
`multiLanguageSettings` |  `object (`[MultiLanguageSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows#MultiLanguageSettings)`)` Optional. Multi-lingual agent settings for this flow.  
`locked` |  `boolean` Indicates whether the flow is locked for changes. If the flow is locked, modifications to the flow will be rejected.  
  
## MultiLanguageSettings

Settings for multi-lingual agents.

JSON representation  
---  
      
    
    {
      "enableMultiLanguageDetection": boolean,
      "supportedResponseLanguageCodes": [
        string
      ]
    }  
  
Fields  
---  
`enableMultiLanguageDetection` |  `boolean` Optional. Enable multi-language detection for this flow. This can be set only if [agent level multi language setting][Agent.enable_multi_language_training] is enabled.  
`supportedResponseLanguageCodes[]` |  `string` Optional. Agent will respond in the detected language if the detected language code is in the supported resolved languages for this flow. This will be used only if multi-language training is enabled in the `[agent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents#Agent.FIELDS.enable_multi_language_training)` and multi-language detection is enabled in the `[flow](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows#MultiLanguageSettings.FIELDS.enable_multi_language_detection)`. The supported languages must be a subset of the languages supported by the agent.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows/create)`

|  Creates a flow in the specified agent.  
  
### `[delete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows/delete)`

|  Deletes a specified flow.  
  
### `[export](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows/export)`

|  Exports the specified flow to a binary file.  
  
### `[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows/get)`

|  Retrieves the specified flow.  
  
### `[getValidationResult](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows/getValidationResult)`

|  Gets the latest flow validation result.  
  
### `[import](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows/import)`

|  Imports the specified flow to the specified agent from a binary file.  
  
### `[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows/list)`

|  Returns the list of all flows in the specified agent.  
  
### `[patch](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows/patch)`

|  Updates the specified flow.  
  
### `[train](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows/train)`

|  Trains the specified flow.  
  
### `[validate](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows/validate)`

|  Validates the specified flow and creates or updates validation results.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-30 UTC."],[],[]] 
