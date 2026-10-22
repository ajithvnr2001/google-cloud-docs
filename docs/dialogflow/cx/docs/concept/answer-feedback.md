---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/answer-feedback/
title: Answer feedback \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:20.026746+00:00
---

# Answer feedback  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/answer-feedback/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Answer feedback Stay organized with collections  Save and categorize content based on your preferences. 

To help track agent performance, Dialogflow provides tools for collecting and analyzing end-user feedback on agent answers during a conversation.

## Enable feedback

Before collecting answer feedback, you must enable the following settings in the [general agent settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings#settings-general):

  * **Enable conversation history**
  * **Enable Answer Feedback**



## Collect feedback with Dialogflow CX Messenger

If you use [Dialogflow CX Messenger](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/dialogflow-messenger), you can enable answer feedback collection for the chat dialog by setting the following [HTML attribute](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/dialogflow-messenger#html-customize): `allow-feedback="all"`.

This will add thumbs up thumb_up and thumbs down thumb_down buttons to the user interface. During the conversation, an end-user can click these buttons to provide feedback on the agent responses. If the user selects thumbs down, they can optionally provide a reason for the negative feedback.

## Collect feedback with custom user interfaces

If you have developed a custom user interface, you can add feedback collection to your interface and call the `Sessions.submitAnswerFeedback` method. Go to the Session API reference

**Select a protocol and version for the Session reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Session resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions) |  [Session resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.sessions)  
RPC |  [Session interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.Sessions) |  [Session interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.Sessions)  
C++ |  [SessionsClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1SessionsClient.html) |  Not available   
C# |  [SessionsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SessionsClient) |  Not available   
Go |  [SessionsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_SessionsClient) |  Not available   
Java |  [SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsClient) |  [SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.SessionsClient)  
Node.js |  [SessionsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.SessionsClient.html) |  [SessionsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.SessionsClient.html)  
PHP |  Not available  |  Not available   
Python |  [SessionsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.sessions.SessionsClient) |  [SessionsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.sessions.SessionsClient)  
Ruby |  Not available  |  Not available   
  
Close

## Custom feedback data structure

You can have feedback data stored in your custom data structure filling the `answerFeedback.customRating` field in the `Sessions.submitAnswerFeedback` method.

If you use [Dialogflow CX Messenger](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/dialogflow-messenger), you can set up custom feedback collection by defining your [custom feedback component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/dialogflow-messenger#custom-feedback-component).

## Browse feedback using the Dialogflow CX console

You can access and filter feedbacks using the [Conversation history](https://docs.cloud.google.com/dialogflow/cx/docs/concept/conversation-history#browser) tool.

## Read feedback with BigQuery conversation history

You can analyze the feedback data with [BigQuery conversation history](https://docs.cloud.google.com/dialogflow/cx/docs/concept/export-bq).

If you have already created your BigQuery table, you can alter your existing table with the following SQL command if it doesn't have the required `bot_answer_feedback` column:
    
    
    ALTER TABLE <your_dataset_name>.<your_table_name>
    ADD COLUMN bot_answer_feedback JSON;
    

## Read feedback with the API

The conversation history resource contains `answerFeedback` fields that contain feedback data. See the `GetConversation` method in the RPC documentation.

[ Previous arrow_back  Audit logging  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/audit-logging)

[ Next Analytics  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/analytics)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
