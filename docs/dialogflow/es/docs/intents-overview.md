---
url: https://docs.cloud.google.com/dialogflow/es/docs/intents-overview/
title: Intents \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:27.987521+00:00
---

# Intents  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/intents-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Intents Stay organized with collections  Save and categorize content based on your preferences. 

An _intent_ categorizes an end-user's intention for one conversation turn. For each agent, you define many intents, where your combined intents can handle a complete conversation. When an end-user writes or says something, referred to as an _end-user expression_ , Dialogflow matches the end-user expression to the best intent in your agent. Matching an intent is also known as _intent classification_. 

For example, you could create a weather agent that recognizes and responds to end-user questions about the weather. You would likely define an intent for questions about the weather forecast. If an end-user says "What's the forecast?", Dialogflow would match that end-user expression to the forecast intent. You can also define your intent to extract useful information from the end-user expression, like a time or location for the desired weather forecast. This extracted data is important for your system to perform a weather query for the end-user. 

![Agent extracting data from end-user expression requesting weather](https://docs.cloud.google.com/static/dialogflow/es/docs/images/intent-match-forecast.svg)

A basic intent contains the following: 

  * [**Training phrases**](https://docs.cloud.google.com/dialogflow/docs/intents-training-phrases): These are example phrases for what end-users might say. When an end-user expression resembles one of these phrases, Dialogflow matches the intent. You don't have to define every possible example, because Dialogflow's built-in machine learning expands on your list with other, similar phrases. 
  * [**Action**](https://docs.cloud.google.com/dialogflow/docs/intents-actions-parameters#actions): You can define an action for each intent. When an intent is matched, Dialogflow provides the action to your system, and you can use the action to trigger certain actions defined in your system. 
  * [**Parameters**](https://docs.cloud.google.com/dialogflow/docs/intents-actions-parameters#params): When an intent is matched at runtime, Dialogflow provides the extracted values from the end-user expression as _parameters_. Each parameter has a type, called the [entity type](https://docs.cloud.google.com/dialogflow/docs/entities-overview), which dictates exactly how the data is extracted. Unlike raw end-user input, parameters are structured data that can easily be used to perform some logic or generate responses. 
  * [**Responses**](https://docs.cloud.google.com/dialogflow/docs/intents-responses): You define text, speech, or visual responses to return to the end-user. These may provide the end-user with answers, ask the end-user for more information, or terminate the conversation. 



The following diagram shows the basic flow for intent matching and responding to the end-user: 

![Agent and intent handling an end-user expression](https://docs.cloud.google.com/static/dialogflow/es/docs/images/intent-match-respond-basic.svg)

A more complex intent may also contain the following:

  * [**Contexts**](https://docs.cloud.google.com/dialogflow/docs/contexts-overview): Dialogflow contexts are similar to natural language context. If a person says to you "they are orange", you need context in order to understand what the person is referring to. Similarly, for Dialogflow to handle an end-user expression like that, it needs to be provided with context in order to correctly match an intent.
  * [**Events**](https://docs.cloud.google.com/dialogflow/docs/events-overview): With events, you can invoke an intent based on something that has happened, instead of what an end-user communicates.



[ Previous arrow_back  Agent settings  ](https://docs.cloud.google.com/dialogflow/es/docs/agents-settings)

[ Next Create and manage intents  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/intents-manage)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
