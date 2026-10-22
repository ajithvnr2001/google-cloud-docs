---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/datasets/
title: Customer Experience Insights datasets \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:48.921592+00:00
---

# Customer Experience Insights datasets  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/datasets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Customer Experience Insights datasets Stay organized with collections  Save and categorize content based on your preferences. 

Group conversations to use for testing and evaluating the results of other features, like Agent Assist summarization. These conversation groupings are called datasets. Curate your datasets by choosing conversations from your existing conversation history or uploading new conversations to Cloud Storage.

## View list

Follow these instructions to access your conversation datasets.

  1. Navigate to the [Customer Experience Insights console](https://ccai.cloud.google.com/insights/projects), sign in, and select your project.
  2. Click **Datasets**. This page displays a list of all your existing datasets.



From this page, you can perform the following additional actions:

  * Create, duplicate, or remove a dataset.
  * Add or remove conversations from a dataset.
  * View details about conversations in a dataset.



## Create

Follow these steps to create a new dataset from the **Datasets** page in the CX Insights console.

  1. Click **\+ Create**.
  2. Enter a **Name** and a brief optional **Description** of your dataset, then click **Next**.
  3. Choose from one of the following options, then follow the instructions to add conversations.



### Conversation history

  1. Select existing Customer Experience Insights conversations to include in your dataset.
  2. Choose one or more [filters](https://docs.cloud.google.com/gemini-enterprise-cx/insights/filtering#conversation_filters) to select a sample from all your conversations.
  3. Enter the date range for when the conversations took place.
  4. Choose the exact number of conversations or a percentage of all your conversations to include in your dataset.



### Upload external

  1. Upload new conversations to include in your dataset.
  2. Choose the data type: chat or voice > **Source** of your conversation data.
  3. Enter the URI for your files. You can upload files from a Cloud Storage bucket or Google Sheets.
  4. Choose your **Transcript Settings**.
  5. To upload conversation summaries, include them in a [metadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/ingest-conversations-api#metadata) JSON file with the same name as the conversation file.
  6. Optional: Enter your de-identify and inspect templates for the **Redaction settings** , then metadata source URI and any other information needed.
  7. For audio data, choose which track the agent is on.
  8. Click **Create**.



### Metadata file

Your JSON metadata file must include at least one text section with the content for each summary section. You can also include as many text sections as you want, overall summary text, and resource labels. The following example illustrates a JSON metadata file for conversation summary. This example includes a `labeled_resource` field with the generator ID and an `agent_assist_summary_label` field with `summary_text` and `text_section` fields. The `text_section` field contains the summary section name and content.
    
    
    {
        "feedback_labels": [
            {
                "labeled_resource": "projects/123/locations/us-central1/generators/123",
                "agent_assist_summary_label": {
                    "summary_text": "Overall summary",
                    "text_sections": {
                        "Section1 name": "Section1 content",
                        "Section2 name": "Section2 content"
                    }
                }
            }
        ]
    }
    

## Duplicate

Follow these steps to duplicate an existing dataset from the **Datasets** page in the [Customer Experience Insights console](https://ccai.cloud.google.com/insights/projects).

  1. Select a dataset from the list, then choose one of the following options. 
     * Click  more_vert > **Duplicate**.
     * Click **Duplicate.**
  2. Enter a **Name** and a brief **Description** for the new copy of your dataset.
  3. Click **Duplicate**.



## Remove

Follow these steps to remove a dataset from the **Datasets** page in the [Customer Experience Insights console](https://ccai.cloud.google.com/insights/projects).

  1. Select a dataset from the list and click  more_vert **More**.
  2. Click **Delete**.



## Manage conversations in a dataset

After you create a dataset, you can add or remove individual conversations in the [Customer Experience Insights console](https://ccai.cloud.google.com/insights/projects). Then follow these steps to modify your dataset.

  1. Click a dataset to view details about it.
  2. Click to **Enable dataset changes**.
  3. Click **Data** to view a list of conversations in the dataset.



After step 3, you can perform any of the following actions to modify your dataset.

### Add

Follow these steps to add more conversations to an existing dataset.

  1. Click **\+ Add data**.
  2. Choose your conversation data source: **Conversation history** or **Upload external**.
  3. Fill in the details just like for step 3 when you created the dataset.



## Remove

Follow these steps to remove one or more conversations from a dataset.

  1. Check each conversation you want to remove.
  2. Click **Delete selected**.



## View details

You can view conversation details from either the **Conversation Hub** or the **Datasets** pages in the [Customer Experience Insights console](https://ccai.cloud.google.com/insights/projects).

Follow these steps to view details about a single conversation in your dataset.

### Conversation Hub

  1. Click **Conversation Hub**.
  2. Navigate to the conversation in the list and click it.



### Datasets

  1. Click **Datasets**.
  2. Choose a dataset from the list and click **Data**.
  3. Choose a conversation from the list.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
