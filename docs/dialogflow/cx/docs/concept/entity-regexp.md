---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-regexp/
title: Regexp entities \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:55.218563+00:00
---

# Regexp entities  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-regexp/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Regexp entities Stay organized with collections  Save and categorize content based on your preferences. 

Some entities need to match patterns rather than specific terms. For example, national identification numbers, IDs, license plates, and so on. With _regexp entities_ , you can provide [regular expressions](https://github.com/google/re2/wiki/Syntax) for matching.

## Compound regular expressions

Each regexp entity corresponds to a single pattern, but you can provide multiple regular expressions if they all represent variations of a single pattern. During agent training, all regular expressions of a single entity are combined with the alternation operator (`|`) to form one _compound regular expression_.

For example, if you provide the following regular expressions for a phone number:

  * `^[2-9]\d{2}-\d{3}-\d{4}$`
  * `^(1?(-?\d{3})-?)?(\d{3})(-?\d{4})$`



The compound regular expression becomes:

  * `^[2-9]\d{2}-\d{3}-\d{4}$|^(1?(-?\d{3})-?)?(\d{3})(-?\d{4})$`



The ordering of regular expressions matters. Each of the regular expressions in the compound regular expression are processed in order. Searching stops once a valid match is found. For example, for an end user expression of "Seattle":

  * `Sea|Seattle` matches "Sea"
  * `Seattle|Sea` matches "Seattle"



## Special handling for speech recognition

**Note:** Enabling [auto speech adaptation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/speech-adaptation) is recommended when using regexp entities. Also see the speech adaptation [regexp-specific guidelines](https://docs.cloud.google.com/dialogflow/cx/docs/concept/speech-adaptation#regexp-entities).

If your agent uses speech recognition (also known as audio input, speech-to-text, or STT), your regular expressions will need special handling when matching letters and numbers. A spoken end-user utterance is first processed by the speech recognizer before entities are matched. When an utterance contains a series of letters or numbers, the recognizer may pad each character with spaces. In addition, the recognizer may interpret digits in word form. For example, an end-user utterance of "My ID is 123" may be recognized as any of the following:

  * "My ID is 123"
  * "My ID is 1 2 3"
  * "My ID is one two three"



To accommodate three digit numbers, you could use the following regular expressions:
    
    
    \d{3}
    
    
    \d \d \d
    
    
    (zero|one|two|three|four|five|six|seven|eight|nine) (zero|one|two|three|four|five|six|seven|eight|nine) (zero|one|two|three|four|five|six|seven|eight|nine)

## Create a regexp entity

###  Console 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Choose your GCP project.
  3. Select your agent.
  4. Select the **Manage** tab.
  5. Click **Entity Types**.
  6. Click **Create**.
  7. Check **Regexp entities**.
  8. Complete remaining fields.
  9. Click **Save**.



###  API 

Set the `EntityType.kind` field to `KIND_REGEXP`. Go to the EntityType API reference

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

  * [Fuzzy matching](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-fuzzy) cannot be enabled for regexp entities. These features are mutually exclusive.
  * Each agent can have a maximum of 50 regexp entities.
  * The compound regular expression for an entity has a maximum length of 2000 characters.



[ Previous arrow_back  Session entities  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-session)

[ Next Fuzzy matching  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-fuzzy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
