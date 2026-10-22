---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-level/
title: Data application levels \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:10.568205+00:00
---

# Data application levels  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-level/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Data application levels Stay organized with collections  Save and categorize content based on your preferences. 

Dialogflow CX data is applied at different levels, depending on the type of data. For example, NLU settings are applied at the flow version level. This means that each flow version can have its own NLU settings. The following describes the levels:

Level | Data  
---|---  
Project (applies to all agents, environments, and flow versions in the project) | [Security settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/security-settings) (although each agent can select different settings defined for the project)  
  
[Location settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region)  
Agent (applies to all environments and flow versions in the agent) | All [agent settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings), except [flow-specific settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow#settings)  
Environment | None  
Flow version | A snapshot of all agent resources (intents, entities, webhooks, and so on), all flow resources (pages), and all [flow settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow#settings)  
  
[ Previous arrow_back  Versions and environments  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/version)

[ Next Detect intent  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/how/detect-intent-stream)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
