---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/EventHandler/
title: EventHandler \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:30.213006+00:00
---

# EventHandler  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/EventHandler/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  EventHandler Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



An event handler specifies an `[event](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/EventHandler#FIELDS.event)` that can be handled during a session. When the specified event happens, the following actions are taken in order:

  * If there is a `[`triggerFulfillment`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/EventHandler#FIELDS.trigger_fulfillment)` associated with the event, it will be called.
  * If there is a `[`targetPage`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/EventHandler#FIELDS.target_page)` associated with the event, the session will transition into the specified page.
  * If there is a `[`targetFlow`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/EventHandler#FIELDS.target_flow)` associated with the event, the session will transition into the specified flow.

JSON representation  
---  
      
    
    {
      "name": string,
      "event": string,
      "triggerFulfillment": {
        object ([Fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "targetPage": string,
      "targetFlow": string,
      "targetPlaybook": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Output only. The unique identifier of this event handler.  
`event` |  `string` Required. The name of the event to handle.  
`triggerFulfillment` |  `object (`[Fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment)`)` The fulfillment to call when the event occurs. Handling webhook errors with a fulfillment enabled with webhook could cause infinite loop. It is invalid to specify such fulfillment for a handler handling webhooks.  
The target to transition to, either a page in the same host flow (the flow that owns this `[TransitionRoute](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/TransitionRoute)`), or another flow in the same agent. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`targetPage` |  `string` The target page to transition to. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/pages/<PageID>`.  
`targetFlow` |  `string` The target flow to transition to. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>`.  
`targetPlaybook` |  `string` The target playbook to transition to. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>`.  
End of mutually exclusive fields.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
