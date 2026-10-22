---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-session/
title: Session entities \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:55.326332+00:00
---

# Session entities  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-session/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Session entities Stay organized with collections  Save and categorize content based on your preferences. 

A _session_ represents a conversation between a Dialogflow CX agent and an end-user. You can create special entities, called _session entities_ , or _user entities_ , during a session. Session entities can extend or replace custom entity types and only exist during the session that they were created for. All session data, including session entities, is stored by Dialogflow CX for 30 minutes.

For example, if your agent has a `@fruit` entity type that includes "pear" and "grape", that entity type could be updated to include "apple" or "orange", depending on the information your agent collects from the end-user. The updated entity type would have the "apple" or "orange" entity entry for the rest of the session.

## Managing session entities with the API

To manage session entities with the API, use the methods for the `SessionEntity` type. Go to the SessionEntityType API reference

**Select a protocol and version for the SessionEntityType reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [SessionEntityType resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions.entityTypes) |  [SessionEntityType resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.sessions.entityTypes)  
RPC |  [SessionEntityType interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.SessionEntityTypes) |  [SessionEntityType interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.SessionEntityTypes)  
C++ |  [SessionEntityTypesClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1SessionEntityTypesClient.html) |  Not available   
C# |  [SessionEntityTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SessionEntityTypesClient) |  Not available   
Go |  [SessionEntityTypesClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_SessionEntityTypesClient) |  Not available   
Java |  [SessionEntityTypesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionEntityTypesClient) |  [SessionEntityTypesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.SessionEntityTypesClient)  
Node.js |  [SessionEntityTypesClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.SessionEntityTypesClient.html) |  [SessionEntityTypesClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.SessionEntityTypesClient.html)  
PHP |  Not available  |  Not available   
Python |  [SessionEntityTypesClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.session_entity_types.SessionEntityTypesClient) |  [SessionEntityTypesClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.session_entity_types.SessionEntityTypesClient)  
Ruby |  Not available  |  Not available   
  
Close

[ Previous arrow_back  Custom entities  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-custom)

[ Next Regexp entities  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-regexp)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
