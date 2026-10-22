---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/training/
title: Training \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:43:52.406141+00:00
---

# Training  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/training/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Training Stay organized with collections  Save and categorize content based on your preferences. 

When your agent is trained, Dialogflow CX uses your training data to build machine learning models specifically for your agent. Each flow of your agent has its own model. This training data primarily consists of intents, intent training phrases, and entities referenced in a flow; which are effectively used as machine learning data labels. However, agent models are built using parameter prompt responses, state handlers, agent settings, and many other pieces of data associated with your agent.

Whenever you change your agent, you should ensure that the agent is trained before attempting to use it. Depending on your agent settings, training may occur automatically or manually.

When training is initiated by the console, the [task indicator](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console#task) provides status for the tasks.

## Draft flow automatic training

[ML settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings#settings-ml) lets you select either a **Standard NLU** or **Advanced NLU** NLU type. A setting to enable or disable automatic training is available.

If you have disabled automatic training, you must execute manual training after you have completed updates.

## Draft flow manual training

To manually train a flow from the console, click the **Train NLU** button in the [ML settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings#settings-ml).

To manually train a flow with the API, call the `train` method for the `Flow` type. Go to the Flow API reference

**Select a protocol and version for the Flow reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Flow resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows) |  [Flow resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.flows)  
RPC |  [Flow interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.Flows) |  [Flow interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.Flows)  
C++ |  [FlowsClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1FlowsClient.html) |  Not available   
C# |  [FlowsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.FlowsClient) |  Not available   
Go |  [FlowsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_FlowsClient) |  Not available   
Java |  [FlowsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.FlowsClient) |  [FlowsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.FlowsClient)  
Node.js |  [FlowsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.FlowsClient.html) |  [FlowsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.FlowsClient.html)  
PHP |  Not available  |  Not available   
Python |  [FlowsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.flows.FlowsClient) |  [FlowsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.flows.FlowsClient)  
Ruby |  Not available  |  Not available   
  
Close

## Flow version automatic training

Whenever a new [flow version](https://docs.cloud.google.com/dialogflow/cx/docs/concept/version) is created, the new flow version is automatically trained.

To create a new flow version from the console, click the **Create** button on the [Version panel](https://docs.cloud.google.com/dialogflow/cx/docs/concept/version#manage-versions).

To create a new flow version with the API, call the `create` method for the `Version` type. Go to the Version API reference

**Select a protocol and version for the Version reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Version resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.versions) |  [Version resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.flows.versions)  
RPC |  [Version interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#versions) |  [Version interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#versions)  
C++ |  [VersionsClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1VersionsClient.html) |  Not available   
C# |  [VersionsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.VersionsClient) |  Not available   
Go |  [VersionsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_VersionsClient) |  Not available   
Java |  [VersionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.VersionsClient) |  [VersionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.VersionsClient)  
Node.js |  [VersionsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.VersionsClient.html) |  [VersionsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.VersionsClient.html)  
PHP |  Not available  |  Not available   
Python |  [VersionsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.versions.VersionsClient) |  [VersionsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.versions.VersionsClient)  
Ruby |  Not available  |  Not available   
  
Close

[ Previous arrow_back  Conversation profiles  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/conversation-profiles)

[ Next Sessions  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/session)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
