---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity/
title: Entities \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:54.989931+00:00
---

# Entities  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Entities Stay organized with collections  Save and categorize content based on your preferences. 

_Entity types_ are used to control how data from end-user input is extracted. 

Dialogflow CX provides predefined [system entities](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-system) that can match many common types of data. For example, there are system entities for matching dates, times, colors, email addresses, and so on. You can also create your own [custom entities](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-custom) for matching custom data. For example, you could define a vegetable entity that can match the types of vegetables available for purchase with a grocery store agent.

## Entity terminology

The term _entity_ is used in this documentation and in the Dialogflow CX console to describe the general concept of entities. When discussing entity details, it's important to understand more specific terms:

  * **Entity type** : Defines the type of information you want to extract from user input. For example, _vegetable_ could be the display name of an entity type. Clicking **Create** from the **Entity Types** section of the Dialogflow CX console creates an _entity type_. When using the API, the term _entity type_ refers to the `EntityType` type. Go to the EntityType API reference

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

  * **(Optional) Description** : Describes the purpose of the entity type, for example "This entity is triggered when the user mentions a vegetable". If you intend to use AI generation to auto-generate reference value synonyms, this field will be used by the model to produce higher-quality results.

  * **Entity entry** : For each entity type, there can be many _entity entries_. Each entity entry provides a set of words or phrases that are considered equivalent, a _reference value_ in the first column and one or more _synonyms_ to that reference value in the second column. For example, if _vegetable_ is an entity type, you could define these entity entries:

Reference value | Synonyms  
---|---  
scallion | scallion, green onion  
bell pepper | bell pepper, sweet pepper  
carrot | carrot  
potato | potato, tater, tuber  
  
Instead of entering entity entries and synonyms manually, you can select the **Auto-generate __ syonyms per entity** checkbox when you create a new entity entry. The default value is 3 synonyms. The AI will generate synonyms based on the reference value and entity type description and enter them in the table. Please note that the synonyms list must also include the original reference value in order to produce a match to that value.

When editing an entity type from the Dialogflow CX console, each row of the display is an _entity entry_. When using the API, the term _entity entry_ refers to the `Entity` type (`EntityType.Entity` or `EntityType_Entity` for some client library languages).

  * **Entity reference value and synonyms** : Some entity entries have multiple words or phrases that are considered equivalent, like the _scallion_ in previous example. For these entity entries, you provide one _reference value_ and one or more _synonyms_.




[ Previous arrow_back  Intents  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent)

[ Next Entity options  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-options)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
