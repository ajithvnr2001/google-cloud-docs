---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Evaluation.ScenarioExpectation
title: Evaluation.ScenarioExpectation \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:14:16.273941+00:00
---

# Evaluation.ScenarioExpectation  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Evaluation.ScenarioExpectation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Evaluation.ScenarioExpectation Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Evaluation.ScenarioExpectation.ToolExpectation
    * JSON representation



The expectation to evaluate the conversation produced by the simulation.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "toolExpectation": {
        object ([Evaluation.ScenarioExpectation.ToolExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Evaluation.ScenarioExpectation#Evaluation.ScenarioExpectation.ToolExpectation))
      },
      "agentResponse": {
        object ([Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Message))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The expectation to evaluate the conversation produced by the simulation. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`toolExpectation` |  `object (`[Evaluation.ScenarioExpectation.ToolExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Evaluation.ScenarioExpectation#Evaluation.ScenarioExpectation.ToolExpectation)`)` Optional. The tool call and response pair to be evaluated.  
`agentResponse` |  `object (`[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Message)`)` Optional. The agent response to be evaluated.  
End of mutually exclusive fields.  
  
## Evaluation.ScenarioExpectation.ToolExpectation

The tool call and response pair to be evaluated.

JSON representation  
---  
      
    
    {
      "expectedToolCall": {
        object ([ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolCall))
      },
      "mockToolResponse": {
        object ([ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolResponse))
      }
    }  
  
Fields  
---  
`expectedToolCall` |  `object (`[ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolCall)`)` Required. The expected tool call, with the parameters of interest specified. Any parameters not specified will be hallucinated by the LLM.  
`mockToolResponse` |  `object (`[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolResponse)`)` Required. The tool response to mock, with the parameters of interest specified. Any parameters not specified will be hallucinated by the LLM.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
