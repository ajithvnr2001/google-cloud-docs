---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Page/
title: Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::Page (v1.12.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:38:43.238521+00:00
---

# Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::Page (v1.12.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Page/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::Page (v1.12.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.12.2 (latest)  1.12.1  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.26.0  0.25.0  0.24.2  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.0  0.10.2  0.9.0  0.8.1  0.7.1  0.6.0  0.5.0  0.4.0 

Reference documentation and code samples for the Dialogflow CX V3 API class Google::Cloud::Dialogflow::CX::V3::Page.

A Dialogflow CX conversation (session) can be described and visualized as a state machine. The states of a CX session are represented by pages.

For each flow, you define many pages, where your combined pages can handle a complete conversation on the topics the flow is designed for. At any given moment, exactly one page is the current page, the current page is considered active, and the flow associated with that page is considered active. Every flow has a special start page. When a flow initially becomes active, the start page page becomes the current page. For each conversational turn, the current page will either stay the same or transition to another page.

You configure each page to collect information from the end-user that is relevant for the conversational state represented by the page.

For more information, see the [Page guide](https://cloud.google.com/dialogflow/cx/docs/concept/page).

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #advanced_settings
    
    
    def advanced_settings() -> ::Google::Cloud::Dialogflow::CX::V3::AdvancedSettings

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::AdvancedSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-AdvancedSettings)) — Hierarchical advanced settings for this page. The settings exposed at the lower level overrides the settings exposed at the higher level. 



### #advanced_settings=
    
    
    def advanced_settings=(value) -> ::Google::Cloud::Dialogflow::CX::V3::AdvancedSettings

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::AdvancedSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-AdvancedSettings)) — Hierarchical advanced settings for this page. The settings exposed at the lower level overrides the settings exposed at the higher level. 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::AdvancedSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-AdvancedSettings)) — Hierarchical advanced settings for this page. The settings exposed at the lower level overrides the settings exposed at the higher level. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — The description of the page. The maximum length is 500 characters. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — The description of the page. The maximum length is 500 characters. 



**Returns**

  * (::String) — The description of the page. The maximum length is 500 characters. 



### #display_name
    
    
    def display_name() -> ::String

**Returns**

  * (::String) — Required. The human-readable name of the page, unique within the flow. 



### #display_name=
    
    
    def display_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The human-readable name of the page, unique within the flow. 



**Returns**

  * (::String) — Required. The human-readable name of the page, unique within the flow. 



### #entry_fulfillment
    
    
    def entry_fulfillment() -> ::Google::Cloud::Dialogflow::CX::V3::Fulfillment

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::Fulfillment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Fulfillment)) — The fulfillment to call when the session is entering the page. 



### #entry_fulfillment=
    
    
    def entry_fulfillment=(value) -> ::Google::Cloud::Dialogflow::CX::V3::Fulfillment

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::Fulfillment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Fulfillment)) — The fulfillment to call when the session is entering the page. 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::Fulfillment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Fulfillment)) — The fulfillment to call when the session is entering the page. 



### #event_handlers
    
    
    def event_handlers() -> ::Array<::Google::Cloud::Dialogflow::CX::V3::EventHandler>

**Returns**

  * (::Array<[::Google::Cloud::Dialogflow::CX::V3::EventHandler](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-EventHandler)>) — Handlers associated with the page to handle events such as webhook errors, no match or no input. 



### #event_handlers=
    
    
    def event_handlers=(value) -> ::Array<::Google::Cloud::Dialogflow::CX::V3::EventHandler>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Dialogflow::CX::V3::EventHandler](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-EventHandler)>) — Handlers associated with the page to handle events such as webhook errors, no match or no input. 



**Returns**

  * (::Array<[::Google::Cloud::Dialogflow::CX::V3::EventHandler](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-EventHandler)>) — Handlers associated with the page to handle events such as webhook errors, no match or no input. 



### #form
    
    
    def form() -> ::Google::Cloud::Dialogflow::CX::V3::Form

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::Form](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Form)) — The form associated with the page, used for collecting parameters relevant to the page. 



### #form=
    
    
    def form=(value) -> ::Google::Cloud::Dialogflow::CX::V3::Form

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::Form](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Form)) — The form associated with the page, used for collecting parameters relevant to the page. 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::Form](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Form)) — The form associated with the page, used for collecting parameters relevant to the page. 



### #knowledge_connector_settings
    
    
    def knowledge_connector_settings() -> ::Google::Cloud::Dialogflow::CX::V3::KnowledgeConnectorSettings

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::KnowledgeConnectorSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-KnowledgeConnectorSettings)) — Optional. Knowledge connector configuration. 



### #knowledge_connector_settings=
    
    
    def knowledge_connector_settings=(value) -> ::Google::Cloud::Dialogflow::CX::V3::KnowledgeConnectorSettings

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::KnowledgeConnectorSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-KnowledgeConnectorSettings)) — Optional. Knowledge connector configuration. 



**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::KnowledgeConnectorSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-KnowledgeConnectorSettings)) — Optional. Knowledge connector configuration. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — The unique identifier of the page. Required for the [Pages.UpdatePage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Pages-Client#Google__Cloud__Dialogflow__CX__V3__Pages__Client_update_page_instance_ "Google::Cloud::Dialogflow::CX::V3::Pages::Client#update_page \(method\)") method. [Pages.CreatePage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Pages-Client#Google__Cloud__Dialogflow__CX__V3__Pages__Client_create_page_instance_ "Google::Cloud::Dialogflow::CX::V3::Pages::Client#create_page \(method\)") populates the name automatically. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/pages/<PageID>`. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — The unique identifier of the page. Required for the [Pages.UpdatePage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Pages-Client#Google__Cloud__Dialogflow__CX__V3__Pages__Client_update_page_instance_ "Google::Cloud::Dialogflow::CX::V3::Pages::Client#update_page \(method\)") method. [Pages.CreatePage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Pages-Client#Google__Cloud__Dialogflow__CX__V3__Pages__Client_create_page_instance_ "Google::Cloud::Dialogflow::CX::V3::Pages::Client#create_page \(method\)") populates the name automatically. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/pages/<PageID>`. 



**Returns**

  * (::String) — The unique identifier of the page. Required for the [Pages.UpdatePage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Pages-Client#Google__Cloud__Dialogflow__CX__V3__Pages__Client_update_page_instance_ "Google::Cloud::Dialogflow::CX::V3::Pages::Client#update_page \(method\)") method. [Pages.CreatePage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Pages-Client#Google__Cloud__Dialogflow__CX__V3__Pages__Client_create_page_instance_ "Google::Cloud::Dialogflow::CX::V3::Pages::Client#create_page \(method\)") populates the name automatically. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/pages/<PageID>`. 



### #transition_route_groups
    
    
    def transition_route_groups() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Ordered list of [`TransitionRouteGroups`](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-TransitionRouteGroup "Google::Cloud::Dialogflow::CX::V3::TransitionRouteGroup \(class\)") added to the page. Transition route groups must be unique within a page. If the page links both flow-level transition route groups and agent-level transition route groups, the flow-level ones will have higher priority and will be put before the agent-level ones.

    * If multiple transition routes within a page scope refer to the same intent, then the precedence order is: page's transition route -> page's transition route group -> flow's transition routes.

    * If multiple transition route groups within a page contain the same intent, then the first group in the ordered list takes precedence.

Format:`projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/transitionRouteGroups/<TransitionRouteGroupID>` or `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/transitionRouteGroups/<TransitionRouteGroupID>` for agent-level groups. 




### #transition_route_groups=
    
    
    def transition_route_groups=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Ordered list of [`TransitionRouteGroups`](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-TransitionRouteGroup "Google::Cloud::Dialogflow::CX::V3::TransitionRouteGroup \(class\)") added to the page. Transition route groups must be unique within a page. If the page links both flow-level transition route groups and agent-level transition route groups, the flow-level ones will have higher priority and will be put before the agent-level ones.

    * If multiple transition routes within a page scope refer to the same intent, then the precedence order is: page's transition route -> page's transition route group -> flow's transition routes.

    * If multiple transition route groups within a page contain the same intent, then the first group in the ordered list takes precedence.

Format:`projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/transitionRouteGroups/<TransitionRouteGroupID>` or `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/transitionRouteGroups/<TransitionRouteGroupID>` for agent-level groups. 




**Returns**

  * (::Array<::String>) — Ordered list of [`TransitionRouteGroups`](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-TransitionRouteGroup "Google::Cloud::Dialogflow::CX::V3::TransitionRouteGroup \(class\)") added to the page. Transition route groups must be unique within a page. If the page links both flow-level transition route groups and agent-level transition route groups, the flow-level ones will have higher priority and will be put before the agent-level ones.

    * If multiple transition routes within a page scope refer to the same intent, then the precedence order is: page's transition route -> page's transition route group -> flow's transition routes.

    * If multiple transition route groups within a page contain the same intent, then the first group in the ordered list takes precedence.

Format:`projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/transitionRouteGroups/<TransitionRouteGroupID>` or `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/transitionRouteGroups/<TransitionRouteGroupID>` for agent-level groups. 




### #transition_routes
    
    
    def transition_routes() -> ::Array<::Google::Cloud::Dialogflow::CX::V3::TransitionRoute>

**Returns**

  * (::Array<[::Google::Cloud::Dialogflow::CX::V3::TransitionRoute](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-TransitionRoute)>) — 

A list of transitions for the transition rules of this page. They route the conversation to another page in the same flow, or another flow.

When we are in a certain page, the TransitionRoutes are evaluated in the following order:

    * TransitionRoutes defined in the page with intent specified.
    * TransitionRoutes defined in the [transition route groups][google.cloud.dialogflow.cx.v3.Page.transition_route_groups] with intent specified.
    * TransitionRoutes defined in flow with intent specified.
    * TransitionRoutes defined in the [transition route groups][google.cloud.dialogflow.cx.v3.Flow.transition_route_groups] with intent specified.
    * TransitionRoutes defined in the page with only condition specified.
    * TransitionRoutes defined in the [transition route groups][google.cloud.dialogflow.cx.v3.Page.transition_route_groups] with only condition specified.



### #transition_routes=
    
    
    def transition_routes=(value) -> ::Array<::Google::Cloud::Dialogflow::CX::V3::TransitionRoute>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Dialogflow::CX::V3::TransitionRoute](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-TransitionRoute)>) — 

A list of transitions for the transition rules of this page. They route the conversation to another page in the same flow, or another flow.

When we are in a certain page, the TransitionRoutes are evaluated in the following order:

    * TransitionRoutes defined in the page with intent specified.
    * TransitionRoutes defined in the [transition route groups][google.cloud.dialogflow.cx.v3.Page.transition_route_groups] with intent specified.
    * TransitionRoutes defined in flow with intent specified.
    * TransitionRoutes defined in the [transition route groups][google.cloud.dialogflow.cx.v3.Flow.transition_route_groups] with intent specified.
    * TransitionRoutes defined in the page with only condition specified.
    * TransitionRoutes defined in the [transition route groups][google.cloud.dialogflow.cx.v3.Page.transition_route_groups] with only condition specified.



**Returns**

  * (::Array<[::Google::Cloud::Dialogflow::CX::V3::TransitionRoute](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-TransitionRoute)>) — 

A list of transitions for the transition rules of this page. They route the conversation to another page in the same flow, or another flow.

When we are in a certain page, the TransitionRoutes are evaluated in the following order:

    * TransitionRoutes defined in the page with intent specified.
    * TransitionRoutes defined in the [transition route groups][google.cloud.dialogflow.cx.v3.Page.transition_route_groups] with intent specified.
    * TransitionRoutes defined in flow with intent specified.
    * TransitionRoutes defined in the [transition route groups][google.cloud.dialogflow.cx.v3.Flow.transition_route_groups] with intent specified.
    * TransitionRoutes defined in the page with only condition specified.
    * TransitionRoutes defined in the [transition route groups][google.cloud.dialogflow.cx.v3.Page.transition_route_groups] with only condition specified.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
