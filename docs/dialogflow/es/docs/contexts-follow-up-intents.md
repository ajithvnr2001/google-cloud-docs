---
url: https://docs.cloud.google.com/dialogflow/es/docs/contexts-follow-up-intents/
title: Follow-up intents \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:39.644387+00:00
---

# Follow-up intents  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/contexts-follow-up-intents/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Follow-up intents Stay organized with collections  Save and categorize content based on your preferences. 

You can use _follow-up intents_ to automatically set contexts for pairs of intents. A follow-up intent is a child of its associated _parent intent._ When you create a follow-up intent, an output context is automatically added to the parent intent and an input context of the same name is added to the follow-up intent. A follow-up intent is only matched when the parent intent is matched in the previous conversational turn. You can also create multiple levels of nested follow-up intents. 

Dialogflow provides many [predefined follow-up intents](https://docs.cloud.google.com/dialogflow/docs/reference/follow-up-intent-expressions) for common end-user replies like "yes", "no", or "cancel". You can also create your own follow-up intents to handle custom replies. 

For example, a hair stylist agent might have the following nested intents. 

Intent  
name | Training  
phrase | Input  
context | Output  
context | Intent  
response  
---|---|---|---|---  
Appointment  |  Hello  |  |  appointment-followup  |  Would you like to  
make an appointment?   
⤷ Appointment - yes  |  Yes  |  appointment-followup  |  appointment-yes-followup  |  Would you like a haircut?   
⤷ Haircut - yes  |  Yes  |  appointment-yes-followup  |  |  Your appointment is set.   
⤷ Haircut - no  |  No  |  appointment-yes-followup  |  |  Goodbye.   
⤷ Appointment - no  |  No  |  appointment-followup  |  |  Goodbye.   
  
## Where to find this data

When building an agent, it is most common to use the Dialogflow ES console ([visit documentation](https://docs.cloud.google.com/dialogflow/docs/console), [open console](https://dialogflow.cloud.google.com)). The instructions below focus on using the console. To access intent data:

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
  2. Select an agent.
  3. Select **Intents** in the left sidebar menu.



If you are building an agent using the API instead of the console, see the [Intents reference](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#intents). The API field names are similar to the console field names.

## Create a follow-up intent

To create a follow-up intent:

  1. From the intent list, hover your mouse pointer over the desired parent intent.
  2. Click **Add follow-up intent**.
  3. Select one of the predefined follow-up intents, or choose **custom**. The predefined follow-up intents already include training phrases for expected end-user replies.



[ Previous arrow_back  Input and output contexts  ](https://docs.cloud.google.com/dialogflow/es/docs/contexts-input-output)

[ Next Manage contexts  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/contexts-manage)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
