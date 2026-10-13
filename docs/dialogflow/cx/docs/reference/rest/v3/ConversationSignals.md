---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationSignals/
title: ConversationSignals \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:28.157579+00:00
---

# ConversationSignals  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationSignals/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  ConversationSignals Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * TurnSignals
    * JSON representation



This message is used to hold all the Conversation Signals data, which will be converted to JSON and exported to BigQuery.

JSON representation  
---  
      
    
    {
      "turnSignals": {
        object ([TurnSignals](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationSignals#TurnSignals))
      }
    }  
  
Fields  
---  
`turnSignals` |  `object (`[TurnSignals](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationSignals#TurnSignals)`)` Required. Turn signals for the current turn.  
  
## TurnSignals

Collection of all signals that were extracted for a single turn of the conversation.

JSON representation  
---  
      
    
    {
      "noMatch": boolean,
      "noUserInput": boolean,
      "dtmfUsed": boolean,
      "userEscalated": boolean,
      "agentEscalated": boolean,
      "reachedEndPage": boolean,
      "webhookStatuses": [
        string
      ],
      "failureReasons": [
        enum ([FailureReason](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/FailureReason))
      ],
      "sentimentScore": number,
      "sentimentMagnitude": number
    }  
  
Fields  
---  
`noMatch` |  `boolean` Whether NLU predicted NO_MATCH.  
`noUserInput` |  `boolean` Whether user provided no input.  
`dtmfUsed` |  `boolean` Whether user was using DTMF input.  
`userEscalated` |  `boolean` Whether user was specifically asking for a live agent.  
`agentEscalated` |  `boolean` Whether agent responded with LiveAgentHandoff fulfillment.  
`reachedEndPage` |  `boolean` Whether turn resulted in End Session page.  
`webhookStatuses[]` |  `string` Human-readable statuses of the webhooks triggered during this turn.  
`failureReasons[]` |  `enum (`[FailureReason](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/FailureReason)`)` Failure reasons of the turn.  
`sentimentScore` |  `number` Sentiment score of the user utterance if [sentiment](https://cloud.google.com/dialogflow/cx/docs/concept/sentiment) was enabled.  
`sentimentMagnitude` |  `number` Sentiment magnitude of the user utterance if [sentiment](https://cloud.google.com/dialogflow/cx/docs/concept/sentiment) was enabled.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
