---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-custom/
title: Custom entities \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:55.386574+00:00
---

# Custom entities  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-custom/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Custom entities Stay organized with collections  Save and categorize content based on your preferences. 

You can create custom entities for matching data specific to your agent. For example, you could define a `vegetable` entity type that can match the types of vegetables available for purchase with a grocery store agent.

**Note:** When building your agent, it's best to define your entities prior to adding [training phrases](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent#tp) to your intents. The console will automatically annotate your training phrases with existing entities. However, if you create entities after training phrases, you can manually annotate the phrases.

## Create custom entities

To create a custom entity:

###  Console 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Choose your Google Cloud project.
  3. Select your agent.
  4. Select the **Manage** tab.
  5. Click **Entity Types**.
  6. Click **Create**.
  7. Enter entity data.
  8. Click **Save**.



###  API 

Use the `EntityType`'s `create` method. Go to the EntityType API reference

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

  * Custom entity type display names are unique for each agent. Entity type display names should start with a letter and can contain the following: `A-Z`, `a-z`, `0-9`, `_` (underscore), `-` (dash). Entity reference and synonym values have no such limitation.



## Export and import custom entities

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can export and import entities for sharing across agents.

One of the export format options is Json package, which is a zip file that contains a hierarchy of directories and JSON files. The following describes the directory structure:

  * `entityTypes`: This directory contains your entity types. 
    * `<entity type name>`: One or more of these directories exist, and the directory names correspond to entity type display names. 
      * `entities`: This directory contains entity entry files. 
        * `<language tag>.json`: One or more of these files exist, and the file names correspond to language tags. Each file contains language-specific entity entries.
      * `<excludedPhrases>`: This directory contains [excluded phrase](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-options#exclusion) files. 
        * `<language tag>.json`: One or more of these files exist, and the file names correspond to language tags. Each file contains language-specific phrase exclusions.
      * `<entity type name>.json`: This filename corresponds to an entity type display name. The file contains entity-type-specific data not found in other files.



For example:
    
    
    folder entityTypes
     ⤷ folder Entity Type A
        ⤷ folder entities
           ⤷ insert_drive_file en.json
           ⤷ insert_drive_file en-gb.json
           ⤷ insert_drive_file en-ca.json
        ⤷ folder excludedPhrases
           ⤷ insert_drive_file en.json
           ⤷ insert_drive_file en-gb.json
           ⤷ insert_drive_file en-ca.json
        ⤷ insert_drive_file Entity Type A.json
     ⤷ folder Entity Type B
        ⤷ folder entities
           ⤷ insert_drive_file en.json
           ⤷ insert_drive_file en-gb.json
           ⤷ insert_drive_file en-ca.json
        ⤷ folder excludedPhrases
           ⤷ insert_drive_file en.json
           ⤷ insert_drive_file en-gb.json
           ⤷ insert_drive_file en-ca.json
        ⤷ insert_drive_file Entity Type B.json
    

When importing entity types, there may be merge conflicts when the display name of an entity type in your existing agent matches that of an imported entity type. You can control the merge behavior when entity type display names match by selecting one of the following:

  * **Replace existing entity types** : An imported entity type overwrites any same-named entity type in your existing agent.
  * **Merge with existing entity types** : The entity entries of an imported entity type are added to the existing entity type. If the same entity entries exist, they won't be duplicated, and the synonyms under them will be merged.
  * **Rename and import as new entity types** : The imported entity type is renamed by appending "_1" to the display name.
  * **Skip the entity types** : The existing entity type remains unchanged, and the imported entity type is ignored.



To export entity types:

###  Console 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Choose your Google Cloud project.
  3. Select your agent.
  4. Select the **Manage** tab.
  5. Click **Entity Types**.
  6. Select all the entity types you want to export.
  7. Click **Export selected entity**.
  8. Select the format and destination.
  9. Click **Submit**.



To import entity types:

###  Console 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Choose your Google Cloud project.
  3. Select your agent.
  4. Select the **Manage** tab.
  5. Click **Entity Types**.
  6. Click **Import**.
  7. Select the source and merge behavior.
  8. Click **Submit**.



## Import entity entries

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can import entity entries to an existing entity type.

The file format used for importing entity entries is the same as the format used for importing entity types. However, the import file can only contain 1 entity type and all the entries under it will be imported to the selected entity type. If the same entity entries exist, they won't be duplicated, and the synonyms under them will be merged.

To import entity entries for an entity type:

###  Console 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Choose your Google Cloud project.
  3. Select your agent.
  4. Select the **Manage** tab.
  5. Click **Entity Types**.
  6. Select an entity.
  7. Click **Import to entity**.
  8. Select a file.
  9. Click **Submit**.



[ Previous arrow_back  System entities  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-system)

[ Next Session entities  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-session)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
