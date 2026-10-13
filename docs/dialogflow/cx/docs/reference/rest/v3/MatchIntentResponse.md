---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/MatchIntentResponse/
title: MatchIntentResponse \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:17:20.886662+00:00
---

# MatchIntentResponse  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/MatchIntentResponse/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  MatchIntentResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Response of [MatchIntent][].

JSON representation  
---  
      
    
    {
      "matches": [
        {
          object ([Match](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Match))
        }
      ],
      "currentPage": {
        object ([Page](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages#Page))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "text": string,
      "triggerIntent": string,
      "transcript": string,
      "triggerEvent": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`matches[]` |  `object (`[Match](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Match)`)` Match results, if more than one, ordered descendingly by the confidence we have that the particular intent matches the query.  
`currentPage` |  `object (`[Page](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages#Page)`)` The current `[Page](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages#Page)`. Some, not all fields are filled in this message, including but not limited to `name` and `displayName`.  
The original conversational query. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`text` |  `string` If `[natural language text](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#TextInput)` was provided as input, this field will contain a copy of the text.  
`triggerIntent` |  `string` If an `[intent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#IntentInput)` was provided as input, this field will contain a copy of the intent identifier. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/intents/<IntentID>`.  
`transcript` |  `string` If `[natural language speech audio](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#AudioInput)` was provided as input, this field will contain the transcript for the audio.  
`triggerEvent` |  `string` If an `[event](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#EventInput)` was provided as input, this field will contain a copy of the event name.  
End of mutually exclusive fields.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
