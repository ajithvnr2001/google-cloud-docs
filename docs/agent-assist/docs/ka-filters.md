---
url: https://docs.cloud.google.com/agent-assist/docs/ka-filters/
title: Knowledge assist filters \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:49:28.052040+00:00
---

# Knowledge assist filters  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-assist/docs/ka-filters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Knowledge assist filters Stay organized with collections  Save and categorize content based on your preferences. 

Filters help you narrow down a search and ensure your knowledge assist generator produces useful suggestions. Filter documents in a Datastore to specify a category of documents for reference in both [generative knowledge assist (GKA)](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/generative-knowledge-assist) and [proactive generative knowledge assist (PGKA)](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/pgka). Customize safety filters on generated content to ensure PGKA suggestions are maximally helpful and minimally harmful for your business needs.

## Document filters

Filter knowledge assist documents for both GKA and PGKA with `SearchConfig`.

### Step 1: Set up Datastore with metadata

[Import with metadata](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store#with-metadata) to create a [Datastore](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store) for GKA and PGKA. You must provide metadata as one or more JSONL files, located in the higher-level folder of the content used for import.

  1. Follow the steps on the Datastore tools page to [add a Datastore to an agent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/handler#create-agent).
  2. On the [AI Applications page](https://pantheon.corp.google.com/gen-app-builder), click **Data Stores** > **\+ Create Data Store.**
  3. Navigate to **Cloud Storage** , and click **Select.**
  4. Click **File** , then enter the path to your file in Cloud Storage or click **Browse** to select your file.
  5. Navigate to **What kind of data are you importing?** and select **Linked unstructured documents (JSONL with metadata)**.
  6. Navigate to **Data import options** and select **Full**.
  7. Click **Import**.
  8. After you successfully create your Datastore, view the Documents table. The table lists each of your documents with the following details. 
     * ID
     * URI link
     * Index status
     * Actions
  9. Click **View Document** to examine a document's properties.



The following is an example JSONL file. You can also specify metadata in the `structData` field.
    
    
    { "id": "d001", "content": {"mimeType": "text/html", "uri": "gs://example-import/unstructured/first_doc.html"}, "structData": {"property0": "value0", "property1": "value1", "property2": "value2"} }
    { "id": "d002", "content": {"mimeType": "application/pdf", "uri": "gs://example-import/unstructured/second_doc.pdf"}, "structData": {"property0": "value0", "property1": "value3", "property2": "value4"} }
    

### Step 2: Configure filters

To directly apply filter values to a GKA search, call the [`SearchKnowledge`](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/generative-knowledge-assist#step_2_use_a_data_store_agent) API. You can also apply a [`SearchConfig`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/SearchConfig) field in the request, as follows. See the [Agent Search documentation](https://docs.cloud.google.com/generative-ai-app-builder/docs/introduction) for more examples of [filter expressions](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata#examples_of_filter_expressions).
    
    
    {
      "query": {
         "text": "test query"
      },
      "conversationProfile": "projects/PROJECT_ID/locations/LOCATION_ID/conversationProfiles/CONVERSATION_PROFILE_ID",
      "sessionId": "SESSION_ID",
      "conversation": "projects/PROJECT_ID/locations/LOCATION_ID/conversations/CONVERSATION_ID",
      "querySource": "AGENT_QUERY",
      "searchConfig": 
        "filterSpecs": [{
          "dataStores": ["projects/PROJECT_NUMBER/locations/LOCATION_ID/collections/default_collection/dataStores/DATASTORE_ID"],
          "filter": "property1 : ANY(\"value1\")" 
          }]
        }
      }
    }
    

To apply filter values across all knowledge search queries and suggestions within a single conversation, use [`IngestContextReferences`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.locations.conversations/ingestContextReferences) and attach the conversation ID to the `SearchKnowledge` call.

#### PGKA document filters

Apply a `SearchConfig` to PGKA calls using either the `IngestContextReferences` API or the simulator in the Agent Assist console.

### API

Call the `IngestContextReferences` API to apply a `SearchConfig` to PGKA calls.

  1. Call [`CreateConversation`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversations/create) > `IngestContextReferences`.
  2. The configuration automatically applies to all subsequent PGKA queries and answer suggestions in the same conversation.



The following example shows how to use the`IngestContextReferences` API.
    
    
    {
      "conversation": "projects/PROJECT_ID/locations/global/conversations/CONVERSATION_ID",
      "contextReferences": {
       "gka_search_config": {
          "contextContents": [{
    "content": "{ \"filterSpecs\": [{ \"dataStores\": [\"projects/PROJECT_NUMBER/locations/LOCATION_ID/collections/default_collection/dataStores/DATASTORE_ID\"], \"filter\": \"property1: ANY    (\\\"value1\\\")\" }] }",
            "contentFormat": "JSON"
          }],
          "updateMode": "OVERWRITE",
          "languageCode": "en-US"
        }
      }
    }
    

### Console

  1. Navigate to the [Agent Assist console](https://agentassist.cloud.google.com), sign in, and select your project.

[Go to console](https://agentassist.cloud.google.com/)

  2. Click **Simulator** and select your conversation profile.

  3. Click **Start** > **Inject context**.

  4. Enter your **Key** , **Content** , and select one of the following **Formats**.

     * Plain text
     * JSON
  5. Click **Save**.




The following is an example of context for the simulator.

  * **Key** : `gka_search_config`
  * **Format** : `JSON`
  * **Content** :


    
    
    { "filterSpecs": [{"dataStores" : ["projects/PROJECT_NUMBER/locations/LOCATION_ID/collections/default_collection/dataStores/DATASTORE_ID"], "filter" : "property1 : ANY(\"value1\")" }] }
    

## Safety filters

Generative features in Agent Assist have built-in responsible AI (RAI) safety filters. These filters are essential for preventing the generation of potentially harmful or inappropriate content. However, default safety levels can be too restrictive for certain industries. For example, a healthcare provider might need to respond to legitimate queries about sensitive health topics that default filters block. To align the generator's behavior with your business needs and use cases, you can customize the sensitivity of safety filters for the PGKA feature.

### Basics

There are two key components to safety filters:

  * The category of content for filtering
  * The sensitivity level of the filter



### RAI categories

You can set a sensitivity level for the following content categories:

  * **Dangerous content** : Content that refers to self harm or anything that is illegal, regulated, or dangerous.
  * **Sexually explicit** : Content that is sexually explicit or contains pornographic material.
  * **Harassment** : Content that is insulting, intimidating, or abusive.
  * **Hate speech** : Content that promotes violence or incites hatred against individuals or groups based on certain attributes.



### Sensitivity levels

For each RAI category, you can choose one of the following sensitivity thresholds:

  * `BLOCK_MOST`: Blocks a wide range of content that could potentially fall into the category.
  * `BLOCK_SOME`: Blocks content that is clearly identified as belonging to the category.
  * `BLOCK_FEW`: Blocks only the most severe instances of content for the category.
  * `BLOCK_NONE`: Disables all filters for the specified category. 



#### Default settings

If you don't provide a custom configuration for a category, proactive generative knowledge assist uses the following default sensitivity levels:

  * **Dangerous content:** `BLOCK_FEW`
  * **Sexually explicit:** `BLOCK_SOME`
  * **Harassment:** `BLOCK_SOME`
  * **Hate speech:** `BLOCK_SOME`



### Configure safety filters

Configure safety filters within your conversation profile. You can specify a sensitivity level for one or more RAI categories by adding an `rai_settings` object to the feature configuration for `KNOWLEDGE_ASSIST`. You can find safety filter settings within the `feature_configs` array for the `KNOWLEDGE_ASSIST` suggestion feature.
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/conversationProfiles/PROFILE_ID",
      "human_agent_assistant_config": {
        "human_agent_suggestion_config": {
          "feature_configs": [
            {
              "suggestion_feature": {
                "type": "KNOWLEDGE_ASSIST"
              },
              "rai_settings": {
                "rai_category_configs": [
                  {
                    "category": "DANGEROUS_CONTENT",
                    "sensitivity_level": "BLOCK_FEW"
                  },
                  {
                    "category": "HARASSMENT",
                    "sensitivity_level": "BLOCK_MOST"
                  }
                ]
              }
            }
          ]
        }
      }
    }
    
    

**Note:** You can only configure each RAI category once per `RaiSettings` object. Duplicate entries for the same category result in a configuration error.

### Configuration examples

The following examples illustrate how to increase or decrease the sensitivity level for a single category according to your business needs.

#### Example 1: Allow sensitive healthcare queries

As a healthcare provider, you want to ensure that queries about sensitive mental health topics are not blocked. You can lower the sensitivity for the dangerous content category, as follows.
    
    
    "rai_settings": {
      "rai_category_configs": [
        {
          "category": "DANGEROUS_CONTENT",
          "sensitivity_level": "BLOCK_NONE"
        }
      ]
    }
    
    

With this setting, proactive generative knowledge assist is more likely to process and provide a helpful response for a query like _What are the warning signs of suicide?_.

#### Example 2: Increase strictness

If your business wants to be extra cautious about harassment, you can increase the sensitivity for that category while leaving others at their default levels, as follows.
    
    
    "rai_settings": {
      "rai_category_configs": [
        {
          "category": "HARASSMENT",
          "sensitivity_level": "BLOCK_MOST"
        }
      ]
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
