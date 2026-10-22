---
url: https://docs.cloud.google.com/dialogflow/es/docs/contexts-overview/
title: Contexts \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:39.433457+00:00
---

# Contexts  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/contexts-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Contexts Stay organized with collections  Save and categorize content based on your preferences. 

Dialogflow _contexts_ are similar to natural language context. If a person says to you "they are orange", you need context in order to understand what "they" is referring to. Similarly, for Dialogflow to handle an end-user expression like that, it needs to be provided with context in order to correctly match an intent. 

Using contexts, you can control the flow of a conversation. You can configure contexts for an intent by setting [input and output contexts](https://docs.cloud.google.com/dialogflow/docs/contexts-input-output), which are identified by string names. When an intent is matched, any configured _output contexts_ for that intent become active. While any contexts are active, Dialogflow is more likely to match intents that are configured with _input contexts_ that correspond to the currently active contexts. 

The following diagram shows an example that uses context for a banking agent. 

![Diagram of user interacting with intents and context.](https://docs.cloud.google.com/static/dialogflow/es/docs/images/contexts-overview.svg)

  1. The end-user asks for information about their checking account. 
  2. Dialogflow matches this end-user expression to the `CheckingInfo` intent. This intent has a `checking` output context, so that context becomes active. 
  3. The agent asks the end-user for the type of information they want about their checking account. 
  4. The end-user responds with "my balance". 
  5. Dialogflow matches this end-user expression to the `CheckingBalance` intent. This intent has a `checking` input context, which needs to be active to match this intent. A similar `SavingsBalance` intent may also exist for matching the same end-user expression when a `savings` context is active. 
  6. After your system performs the necessary database queries, the agent responds with the checking account balance. 



[ Previous arrow_back  Export and import entities  ](https://docs.cloud.google.com/dialogflow/es/docs/entities-export)

[ Next Input and output contexts  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/contexts-input-output)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
