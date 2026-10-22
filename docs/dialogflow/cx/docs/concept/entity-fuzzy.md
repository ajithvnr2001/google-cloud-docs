---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-fuzzy/
title: Fuzzy matching \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:55.440754+00:00
---

# Fuzzy matching  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-fuzzy/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Fuzzy matching Stay organized with collections  Save and categorize content based on your preferences. 

By default, entity matching requires an exact match for one of the entity entries. This works well for single-word entity entry values and synonyms but may present a problem for multi-word values and synonyms. For example, consider a _ball_ entity that should be matched for the following end-user expression parts:

  * "ball"
  * "red ball"
  * "ball red"
  * "small ball"
  * "ball small"
  * "small red ball"
  * "small ball red"
  * "red small ball"
  * "red ball small"
  * "ball small red"
  * "ball red small"



For a match to occur, you normally need to define an entity entry value and synonyms for each of these permutations. However, with fuzzy matching enabled, the ordering of the words in a value or synonym does not matter. The following will trigger a match for all of the examples above:

  * "ball"
  * "red ball"
  * "small ball"
  * "small red ball"



## Create a fuzzy matching entity

###  Console 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Choose your GCP project.
  3. Select your agent.
  4. Select the **Manage** tab.
  5. Click **Entity Types**.
  6. Click **Create**.
  7. Check **Fuzzy matching**.
  8. Complete remaining fields.
  9. Click **Save**.



###  API 

Set the `EntityType.enableFuzzyExtraction` field to true. Go to the EntityType API reference

**Select a protocol and version for the EntityType reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [EntityType resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.entityTypes) |  [EntityType resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.entityTypes)  
RPC |  [EntityType interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.EntityTypes) |  [EntityType interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.EntityTypes)  
C++ |  [EntityTypesClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1EntityTypesClient.html) |  Not available   
C# |  [EntityTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypesClient) |  Not available   
Go |  [EntityTypesClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_EntityTypesClient) |  Not available   
Java |  [EntityTypesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.EntityTypesClient) |  [EntityTypesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.EntityTypesClient)  
Node.js |  [EntityTypesClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.EntityTypesClient.html) |  [EntityTypesClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.EntityTypesClient.html)  
PHP |  Not available  |  Not available   
Python |  [EntityTypesClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.entity_types.EntityTypesClient) |  [EntityTypesClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.entity_types.EntityTypesClient)  
Ruby |  Not available  |  Not available   
  
Close

## Limitations

The following limitations apply:

  * Fuzzy matching cannot be enabled for [regexp entities](https://docs.cloud.google.com/dialogflow/docs/entities-regexp). These features are mutually exclusive.
  * Fuzzy matching should not be enabled for entities which are used to match strict values like IDs, national identification numbers, and so on.



[ Previous arrow_back  Regexp entities  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-regexp)

[ Next Parameters  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
