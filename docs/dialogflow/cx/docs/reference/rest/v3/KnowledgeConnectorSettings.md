---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/KnowledgeConnectorSettings/
title: KnowledgeConnectorSettings \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:34.578096+00:00
---

# KnowledgeConnectorSettings  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/KnowledgeConnectorSettings/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  KnowledgeConnectorSettings Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



The Knowledge Connector settings for this page or flow. This includes information such as the attached Knowledge Bases, and the way to execute fulfillment.

JSON representation  
---  
      
    
    {
      "enabled": boolean,
      "triggerFulfillment": {
        object ([Fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment))
      },
      "dataStoreConnections": [
        {
          object ([DataStoreConnection](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/DataStoreConnection))
        }
      ],
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "targetPage": string,
      "targetFlow": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`enabled` |  `boolean` Whether Knowledge Connector is enabled or not.  
`triggerFulfillment` |  `object (`[Fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment)`)` The fulfillment to be triggered.When the answers from the Knowledge Connector are selected by Dialogflow, you can utitlize the request scoped parameter `$request.knowledge.answers` (contains up to the 5 highest confidence answers) and `$request.knowledge.questions` (contains the corresponding questions) to construct the fulfillment.  
`dataStoreConnections[]` |  `object (`[DataStoreConnection](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/DataStoreConnection)`)` Optional. List of related data store connections.  
The target to transition to, either a page in the same host flow (the flow that owns this `[KnowledgeConnectorSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/KnowledgeConnectorSettings)`), or another flow in the same agent. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`targetPage` |  `string` The target page to transition to. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/pages/<PageID>`.  
`targetFlow` |  `string` The target flow to transition to. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>`.  
End of mutually exclusive fields.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
