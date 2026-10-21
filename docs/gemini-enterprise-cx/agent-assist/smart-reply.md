---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/smart-reply/
title: Smart Reply \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:06:08.833953+00:00
---

# Smart Reply  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/smart-reply/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Smart Reply Stay organized with collections  Save and categorize content based on your preferences. 

Smart Reply follows a conversation between a human agent and an end user and surfaces suggested responses to the human agent. Suggested responses are calculated by a custom model that has been trained on your own conversation data.

This document walks you through the process of using the API to implement Smart Reply and get suggestions from this feature. If preferred, you have the option of using the [Agent Assist console](https://agentassist.cloud.google.com) to upload your data, train a model, and test your Smart Reply results during design-time. To see Smart Reply suggestions during runtime, you must call the API directly. See the [Smart Reply tutorial](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/tutorials) for details about training a model and testing its performance using the Agent Assist Console.

Agent Assist also provides publicly-available conversation data as well as a pre-trained model and allowlist. You can use these resources to see how Smart Reply works or test your integration before uploading your own data. See the [conversation data format documentation](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-data-format#smart_reply_data_format) for more information.

**Note:** To see if the Smart Reply feature is available for your language, see the [language support page](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/languages).

## Before you begin

Complete the following before starting this guide:

  1. [Create a conversation dataset](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-dataset) using your own transcript data.
  2. [Train a Smart Reply model](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/model-training) using your conversation dataset(s).



## Personal Identifying Information and children's data

When you send data to this API, the API attempts to redact all personally-identifiable information (PII). If you need to ensure that the model doesn't include PII, you should sanitize your data before sending it to the API. Replace the redacted words with placeholders such as `REDACTED_NUMBER` or `REDACTED_NAME` rather than simply removing them. 

Also, if your data contains information collected from children, you should remove the children's data before sending it to the API. 

## Train and deploy a model

Agent Assist Smart Reply models are trained using _conversation datasets_. A conversation dataset contains your own uploaded transcript data. This section walks you through the process of creating a conversation dataset, uploading your conversation data to it, and training and deploying a model. You can also perform these actions using the [Agent Assist Console](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-dataset) if you would prefer not to call the API directly.

### Create a conversation dataset

Before you can begin uploading conversation transcripts you must first create a conversation dataset to put them in. Call the `create` method on the [`ConversationDataset`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationDatasets) resource to create a conversation dataset.

The response contains a conversation dataset ID.

### Import conversation transcripts to your conversation dataset

Upload your chat conversation data to your conversation dataset so that it can be processed by Agent Assist. Make sure that a transcript of each conversation is in [`JSON` format](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-data-format) and stored in a [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets). A conversation dataset must contain at least 30,000 conversations, otherwise model training will fail. As a general rule, the more conversations you have the better your model quality will be. We recommend uploading at least 3 months of conversations to sufficiently cover as many use cases as possible. The maximum number of messages in a conversation dataset is 1,000,000.

Call the `importConversationData` method on the [`ConversationDataset`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationDatasets) resource to import your conversations.

Required fields:

  * The conversation dataset ID that you created previously.
  * The `inputConfig` path leads to your conversation transcript data in a Cloud Storage bucket.



The response is a [long-running operation](https://docs.cloud.google.com/dialogflow/docs/how/long-running-operations), which you can poll to check for completion.

### Create a conversation model

Call the `create` method on the [`ConversationModel`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels) resource to create a conversation model. This action also creates the model's [allowlist](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/smart-reply#manage_an_allowlist).

Required fields:

  * In `datasets`, provide a single dataset using the conversation dataset ID you created previously.
  * Set `smartReplyModelMetadata` to an empty object, or populate the field to override the default.



The response is a [long-running operation](https://docs.cloud.google.com/dialogflow/docs/how/long-running-operations), which you can poll to check for completion. Once completed, the model ID and allowlist ID will be included in the metadata for the operation.

  * Model ID: `name`
  * Allowlist ID: `smart_reply_model_metadata.associated_allowlist_info.document`



### Deploy the conversation model

Call the `deploy` method on the [`ConversationModel`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels) resource to deploy the conversation model.

Required field:

  * Use `conversationModels`: Enter the conversation model ID you created previously.



## Manage an allowlist

Each model has an allowlist associated with it, which is automatically created when you create a conversation model. The allowlist contains all responses, generated from your conversation dataset(s), that can be surfaced to a human agent at runtime. This section describes allowlist creation and management. You can also perform these actions using the [Agent Assist Console](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/model-training) if you would prefer not to call the API directly.

### Export the allowlist contents to a `CSV` file

Model creation automatically creates an allowlist that's associated with the new model. The allowlist is a Document resource with a unique ID. The ID is returned in `smart_reply_model_metadata.associated_allowlist_info.document` when a model is created. In order to review and make changes to messages on the allowlist, you must export it to a Cloud Storage bucket.

Call the `export` method on the [`Document`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.knowledgeBases.documents) resource to export the document to a `CSV` file in a Cloud Storage bucket. The `smart_messaging_partial_update` field is optional but affects how you will be able to [update this allowlist](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/smart-reply#update_the_allowlist) in the future. If set to `true`, the exported `CSV` file will include a column that contains a unique ID for each message. You can use the message ID to only update specified messages instead of the entire document. If `smart_messaging_partial_update` is set to `false` or not set, the extra column won't appear in the file, and any updates to the allowlist will require an update to the entire document.

Required field:

  * The `gcsDestination` path goes to your Cloud Storage bucket.



The response is a [long-running operation](https://docs.cloud.google.com/dialogflow/docs/how/long-running-operations), which you can poll to check for completion. Afterward, the `CSV` file you provided in the request is populated with response candidates.

### Review the allowlist

The generated allowlist contains responses that were automatically generated by Smart Reply based on your conversation data. You can now review and update those responses as needed. Download the `CSV` file from your Cloud Storage bucket, edit it to suit your needs, and upload the file back to the Cloud Storage bucket. Only responses on the allowlist can be surfaced to human agents.

If you edit any responses we recommend that you edit only for spelling and grammar, and don't change the meaning of the message. The more the edited text deviates from the meaning in the model, the less likely that message is to be surfaced.

You also can create new messages if needed. Similarly to edited messages, created messages are less likely to be surfaced during runtime.

### Update the allowlist

After you have finished updating the `CSV` file, you can use it to update the `Document` resource. You can choose to update the entire allowlist or only specified messages. To update only specified messages, you must have set `smart_messaging_partial_update` to `true` when you [exported the allowlist](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/smart-reply#export_the_allowlist_contents_to_a_csv_file). If you have already done this, use the automatically generated column in the exported `CSV` file to indicate the messages to be updated.

Call the `reload` method on the [`Document`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.knowledgeBases.documents) resource to update the allowlist. To update only specified messages, set `smart_messaging_partial_update` to `true` in the `ReloadDocumentRequest`. To update the entire allowlist, leave `smart_messaging_partial_update` unset or set to `false`.

Required fields:

  * The `gcsSource` is the Cloud Storage path to the `CSV` file.
  * For `name`, use the allowlist resource name generated when you [created a conversation model](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/smart-reply#create_a_conversation_model).



Example request:
    
    
    {
      "name":"projects/project-id/knowledgeBases/knowledge-base-id/documents/allowlist-id",
      "gcsSource" {
          "uri": "gs://revised_smart_reply_allowlist_path"
       }
    }

## Evaluate a trained model's performance

You can test a model's performance after you have deployed the model and created an allowlist for it. You must also provide a **test dataset**. The responses generated by the trained Smart Reply model and its associated allowlist will be compared to actual agent messages in the test dataset. The test dataset should be made up of real-world conversation data but must not contain any of the data in the conversation dataset that you used to train the model. For example, given 1 month's worth of conversation traffic, you could use 3 weeks of conversation data to create a conversation dataset and the remaining 1 week's data to create the test dataset. A test dataset should contain a minimum of 1000 conversations, but as a general rule the evaluation metrics will be more reliable with more conversations in the test dataset. Test dataset format is the same as [conversation dataset format](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-data-format).

To create a new model evaluation, call the `CreateConversationModelEvaluation` method on a `ConversationModel` resource. This method returns a longrunning operation. You can poll the operation to check its state, which will return one of `INITIALIZING`, `RUNNING`, `SUCCEEDED`, `CANCELLED`, `FAILED`.

Required fields:

  * `InputDataset`: The test dataset that will be used to test the model's performance.
  * `allowlist_document`: The allowlist associated with the Smart Reply model to be tested.



A `ConversationModelEvaluation` resource is returned when the longrunning operation has completed. Two metrics are included:

  * `allowlist_coverage`: The percentage of agent messages in the test dataset that are covered by the allowlist.
  * `recall`: The percentage of agent messages in the test dataset that are contained in the allowlist **and** appear in the top 3 suggestions surfaced by the Smart Reply model.



## Configure a conversation profile

A _conversation profile_ configures a set of parameters that control the suggestions made to an agent during a conversation. The following steps create a [`ConversationProfile`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles) with a [`HumanAgentAssistantConfig`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.HumanAgentAssistantConfig) object. You can also perform these actions using the [Agent Assist Console](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-profile) if you would prefer not to call the API directly.

### Create a conversation profile

To create a conversation profile, call the `create` method on the [`ConversationProfile`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles) resource. Provide your knowledge base ID, document ID, project ID, and model ID.

The following is a JSON example: 
    
    
    {
      "displayName":"smart_reply_assist",
      "humanAgentAssistantConfig":{
        "humanAgentSuggestionConfig":{
          "featureConfigs":[
            {
              "suggestionFeature": { "type":"SMART_REPLY" },
              "queryConfig": {
                "documentQuerySource":{
                  "documents": ["projects/PROJECT_ID/knowledgeBases/KNOWLEDGE_BASE_ID/documents/DOCUMENT_ID"]
                  },
                    "maxResults": 3
                  },
                }
              },
              "conversationModelConfig":{
                "model": "projects/PROJECT_ID/conversationModels/MODEL_ID"
              }
            }
          ]
        }
      }
    }
    

We recommend that you set the `SuggestionFeatureConfig.enable_inline_suggestion` value. If this value is true, later calls to `AnalyzeContent` will result in responses with a list of suggestions. 

The response contains your new conversation profile ID.

See [generative smart reply](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/priv/generative-smart-reply) for instructions on how to configure a conversation profile, handle conversations at runtime, test your results, and send feedback to Agent Assist.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
