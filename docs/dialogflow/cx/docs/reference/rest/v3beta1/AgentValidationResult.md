---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/AgentValidationResult/
title: AgentValidationResult \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:24:19.435573+00:00
---

# AgentValidationResult  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/AgentValidationResult/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  AgentValidationResult Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



The response message for `[Agents.GetAgentValidationResult](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents/getValidationResult#google.cloud.dialogflow.cx.v3beta1.Agents.GetAgentValidationResult)`.

JSON representation  
---  
      
    
    {
      "name": string,
      "flowValidationResults": [
        {
          object ([FlowValidationResult](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/FlowValidationResult))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` The unique identifier of the agent validation result. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/validationResult`.  
`flowValidationResults[]` |  `object (`[FlowValidationResult](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/FlowValidationResult)`)` Contains all flow validation results.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
