---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages
title: REST Resource: projects.locations.agents.flows.pages \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:09.726968+00:00
---

# REST Resource: projects.locations.agents.flows.pages  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  REST Resource: projects.locations.agents.flows.pages Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Page
    * JSON representation
    * Form
      * JSON representation
    * Parameter
      * JSON representation
    * FillBehavior
      * JSON representation
  * Methods



## Resource: Page

A Dialogflow CX conversation (session) can be described and visualized as a state machine. The states of a CX session are represented by pages.

For each flow, you define many pages, where your combined pages can handle a complete conversation on the topics the flow is designed for. At any given moment, exactly one page is the current page, the current page is considered active, and the flow associated with that page is considered active. Every flow has a special start page. When a flow initially becomes active, the start page page becomes the current page. For each conversational turn, the current page will either stay the same or transition to another page.

You configure each page to collect information from the end-user that is relevant for the conversational state represented by the page.

For more information, see the [Page guide](https://cloud.google.com/dialogflow/cx/docs/concept/page).

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "entryFulfillment": {
        object ([Fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment))
      },
      "form": {
        object ([Form](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages#Page.Form))
      },
      "transitionRouteGroups": [
        string
      ],
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
      "advancedSettings": {
        object ([AdvancedSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/AdvancedSettings))
      },
      "knowledgeConnectorSettings": {
        object ([KnowledgeConnectorSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/KnowledgeConnectorSettings))
      }
    }  
  
Fields  
---  
`name` |  `string` The unique identifier of the page. Required for the `[Pages.UpdatePage](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages/patch#google.cloud.dialogflow.cx.v3.Pages.UpdatePage)` method. `[Pages.CreatePage](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages/create#google.cloud.dialogflow.cx.v3.Pages.CreatePage)` populates the name automatically. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/pages/<PageID>`.  
`displayName` |  `string` Required. The human-readable name of the page, unique within the flow.  
`description` |  `string` The description of the page. The maximum length is 500 characters.  
`entryFulfillment` |  `object (`[Fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment)`)` The fulfillment to call when the session is entering the page.  
`form` |  `object (`[Form](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages#Page.Form)`)` The form associated with the page, used for collecting parameters relevant to the page.  
`transitionRouteGroups[]` |  `string` Ordered list of `[`TransitionRouteGroups`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.transitionRouteGroups#TransitionRouteGroup)` added to the page. Transition route groups must be unique within a page. If the page links both flow-level transition route groups and agent-level transition route groups, the flow-level ones will have higher priority and will be put before the agent-level ones.

  * If multiple transition routes within a page scope refer to the same intent, then the precedence order is: page's transition route -> page's transition route group -> flow's transition routes.
  * If multiple transition route groups within a page contain the same intent, then the first group in the ordered list takes precedence.

Format:`projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/transitionRouteGroups/<TransitionRouteGroupID>` or `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/transitionRouteGroups/<TransitionRouteGroupID>` for agent-level groups.  
`transitionRoutes[]` |  `object (`[TransitionRoute](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/TransitionRoute)`)` A list of transitions for the transition rules of this page. They route the conversation to another page in the same flow, or another flow.When we are in a certain page, the TransitionRoutes are evaluated in the following order:

  * TransitionRoutes defined in the page with intent specified.
  * TransitionRoutes defined in the `[transition route groups](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages#Page.FIELDS.transition_route_groups)` with intent specified.
  * TransitionRoutes defined in flow with intent specified.
  * TransitionRoutes defined in the `[transition route groups](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows#Flow.FIELDS.transition_route_groups)` with intent specified.
  * TransitionRoutes defined in the page with only condition specified.
  * TransitionRoutes defined in the `[transition route groups](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages#Page.FIELDS.transition_route_groups)` with only condition specified.

  
`eventHandlers[]` |  `object (`[EventHandler](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/EventHandler)`)` Handlers associated with the page to handle events such as webhook errors, no match or no input.  
`advancedSettings` |  `object (`[AdvancedSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/AdvancedSettings)`)` Hierarchical advanced settings for this page. The settings exposed at the lower level overrides the settings exposed at the higher level.  
`knowledgeConnectorSettings` |  `object (`[KnowledgeConnectorSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/KnowledgeConnectorSettings)`)` Optional. Knowledge connector configuration.  
  
### Form

A form is a data model that groups related parameters that can be collected from the user. The process in which the agent prompts the user and collects parameter values from the user is called form filling. A form can be added to a `[page](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages#Page)`. When form filling is done, the filled parameters will be written to the `[session](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/SessionInfo#FIELDS.parameters)`.

JSON representation  
---  
      
    
    {
      "parameters": [
        {
          object ([Parameter](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages#Page.Parameter))
        }
      ]
    }  
  
Fields  
---  
`parameters[]` |  `object (`[Parameter](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages#Page.Parameter)`)` Parameters to collect from the user.  
  
### Parameter

Represents a form parameter.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "required": boolean,
      "entityType": string,
      "isList": boolean,
      "fillBehavior": {
        object ([FillBehavior](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages#Page.FillBehavior))
      },
      "defaultValue": value,
      "redact": boolean,
      "advancedSettings": {
        object ([AdvancedSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/AdvancedSettings))
      }
    }  
  
Fields  
---  
`displayName` |  `string` Required. The human-readable name of the parameter, unique within the form.  
`required` |  `boolean` Indicates whether the parameter is required. Optional parameters will not trigger prompts; however, they are filled if the user specifies them. Required parameters must be filled before form filling concludes.  
`entityType` |  `string` Required. The entity type of the parameter. Format: `projects/-/locations/-/agents/-/entityTypes/<SystemEntityTypeID>` for system entity types (for example, `projects/-/locations/-/agents/-/entityTypes/sys.date`), or `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/entityTypes/<EntityTypeID>` for developer entity types.  
`isList` |  `boolean` Indicates whether the parameter represents a list of values.  
`fillBehavior` |  `object (`[FillBehavior](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages#Page.FillBehavior)`)` Required. Defines fill behavior for the parameter.  
`defaultValue` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` The default value of an optional parameter. If the parameter is required, the default value will be ignored.  
`redact` |  `boolean` Indicates whether the parameter content should be redacted in log. If redaction is enabled, the parameter content will be replaced by parameter name during logging. Note: the parameter content is subject to redaction if either parameter level redaction or `[entity type level redaction](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.entityTypes#EntityType.FIELDS.redact)` is enabled.  
`advancedSettings` |  `object (`[AdvancedSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/AdvancedSettings)`)` Hierarchical advanced settings for this parameter. The settings exposed at the lower level overrides the settings exposed at the higher level.  
  
### FillBehavior

Configuration for how the filling of a parameter should be handled.

JSON representation  
---  
      
    
    {
      "initialPromptFulfillment": {
        object ([Fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment))
      },
      "repromptEventHandlers": [
        {
          object ([EventHandler](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/EventHandler))
        }
      ]
    }  
  
Fields  
---  
`initialPromptFulfillment` |  `object (`[Fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment)`)` Required. The fulfillment to provide the initial prompt that the agent can present to the user in order to fill the parameter.  
`repromptEventHandlers[]` |  `object (`[EventHandler](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/EventHandler)`)` The handlers for parameter-level events, used to provide reprompt for the parameter or transition to a different page/flow. The supported events are: * `sys.no-match-<N>`, where N can be from 1 to 6 * `sys.no-match-default` * `sys.no-input-<N>`, where N can be from 1 to 6 * `sys.no-input-default` * `sys.invalid-parameter``initialPromptFulfillment` provides the first prompt for the parameter.If the user's response does not fill the parameter, a no-match/no-input event will be triggered, and the fulfillment associated with the `sys.no-match-1`/`sys.no-input-1` handler (if defined) will be called to provide a prompt. The `sys.no-match-2`/`sys.no-input-2` handler (if defined) will respond to the next no-match/no-input event, and so on.A `sys.no-match-default` or `sys.no-input-default` handler will be used to handle all following no-match/no-input events after all numbered no-match/no-input handlers for the parameter are consumed.A `sys.invalid-parameter` handler can be defined to handle the case where the parameter values have been `invalidated` by webhook. For example, if the user's response fill the parameter, however the parameter was invalidated by webhook, the fulfillment associated with the `sys.invalid-parameter` handler (if defined) will be called to provide a prompt.If the event handler for the corresponding event can't be found on the parameter, `initialPromptFulfillment` will be re-prompted.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages/create)`

|  Creates a page in the specified flow.  
  
### `[delete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages/delete)`

|  Deletes the specified page.  
  
### `[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages/get)`

|  Retrieves the specified page.  
  
### `[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages/list)`

|  Returns the list of all pages in the specified flow.  
  
### `[patch](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages/patch)`

|  Updates the specified page.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
