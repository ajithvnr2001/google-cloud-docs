---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/topic-modeling/
title: How-to: Topic modeling operations \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:51.107146+00:00
---

# How-to: Topic modeling operations  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/topic-modeling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  How-to: Topic modeling operations Stay organized with collections  Save and categorize content based on your preferences. 

Follow the instructions in this guide to learn how to perform operations such as create, fine-tune, and deploy a topic model.

## Before you begin

  1. Complete the instructions on the [before you begin](https://docs.cloud.google.com/gemini-enterprise-cx/insights/before-you-begin) page.
  2. Ensure the roles assigned to your [service account](https://docs.cloud.google.com/iam/docs/service-accounts) allow _write_ access to the project that you intend to use for topic modeling and _read_ access to the Cloud Storage API.

The following two roles provide write access:

     * Project > Owner
     * Project > Editor



### Data recommendations for conversation import

V2 models can work with small datasets, as long as they obey the following guidelines:

  * Use a minimum of 100 conversations, each with at least 5 back-and-forth turns between an agent and a customer.
  * We recommend using between 1,000 and 10,000 conversations for optimal results.



You can provide conversation data as either audio files or JSON-formatted text files. For details on the format and instructions for uploading conversation data to Cloud Storage, see the [conversation data reference](https://docs.cloud.google.com/gemini-enterprise-cx/insights/conversation-data-format).

After you import conversation data, you can [list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/list-conversations-api) and [filter](https://docs.cloud.google.com/gemini-enterprise-cx/insights/filtering) the conversations using the API.

## Create a topic model

Follow these instructions to create your topic model.

### Console

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `resourcemanager.projects.get`
  * `contactcenterinsights.issueModels.create`



Follow these steps to create a topic model from the Customer Experience Insights console:

  1. Go to the CX Insights console, sign in with your Google Account, and select your project.

[CX Insights console](https://ccai.cloud.google.com/insights)

  2. Click model_training **Topic models** > **\+ Create New**.

  3. Enter the **Model display name** and select a **Model size**.

  4. Optional: Choose a language from the **Language** list to train a non-English model. CX Insights supports French, German, Italian, Spanish, and Portuguese. This automatically filters conversations of the selected language to use during training.

  5. Click **Continue**.

  6. Choose whether to import all or filter your conversations. If you chose **Filter imported conversations** , select a filter, then click **Continue**.

  7. Optional: Choose an **Industry template** , then click **Continue**.

  8. Enter or upload custom topics.

  9. Click **Start Training** to begin training a new topic model.




### REST API

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `contactcenterinsights.issueModels.create`



Follow these steps to create a topic model from the CX Insights API:

  1. Call the `create` method on the [`issueModel`](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.issueModels) resource.
  2. Send a creation request to the CX Insights API with a model definition.
  3. In addition to a display name and training data configuration, you must include the model type `TYPE_V2` in your request.
  4. You can optionally specify the `language_code` field in the request to train a model for a specific language.



### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your project ID.
  * MODEL_NAME: A human-readable name for the new issue model.

**Note:** All the examples are using the global Customer Experience Insights instance. Refer to [Regionalization](https://docs.cloud.google.com/gemini-enterprise-cx/insights/docs/regionalization) for instructions on using regional instances. 

HTTP method and URL: 
    
    
    POST https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/issueModels

Request JSON body: 
    
    
    {
      "display_name": "my new test model",
      "input_data_config": {
          "filter": "medium=\"CHAT\"",
          "custom_taxonomy": {
            "taxonomy_entries": [
              {
                "display_name": "reschedule car service"
              },
              {
                "display_name": "problem with windshield wipers"
              }
            ]
          },
          "industry": "auto",
          "issue_granularity": "STANDARD"
       },
       "model_type": "TYPE_V2",
       "language_code": "en-US"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/issueModels"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/issueModels" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/us-central1/operations/OPERATION_ID"
    }
    

### Operation status

Creating a topic model is a long-running operation, which means two things:

  1. You can't create a topic model during a conversation with an end user at runtime.
  2. Topic model creation is a lengthy process and depends on the number of conversations in your training dataset. A job containing the minimum number of 1,000 conversations can take up to an hour or more to complete.



Despite these limitations, you can [poll the status of the operation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/long-running-operations) to see if it has completed.

## Fine-tune a topic model

Use the CX Insights console to modify your topic list to improve future topic assignments.

### Add or edit topics

You can change your topic list by adding topics to cover areas the model doesn't already represent. Follow these steps to add a topic:

  1. From the **Topic Models** page, click one of your topic models > **Add topic**.
  2. Enter a **Topic Name** and **Topic Description** , then click **Done**.

**Note:** See [best practices](https://docs.cloud.google.com/gemini-enterprise-cx/insights/topic-modeling-bp#add_edit_topic) for topic names and descriptions.



You can also update topic names or descriptions to better describe the subjects of conversations that should match or better suit the business use case. Follow these steps to edit a topic name or description:

  1. From your topic list, go to the topic and click more_vert > edit **Edit topic**.
  2. Enter the name and description, then click **Done**.



### Remove a topic

In the CX Insights console, follow these steps to remove a topic from the final topic list and the topic inference results.

  1. Select your CX Insights enabled project.
  2. Click model_training **Topic Models** and select a topic model.
  3. Navigate to the topic and click more_vert > do_not_disturb_on **Remove topic**.

**Note:** After removing a topic, you need to reanalyze previously labeled conversations to overwrite the previous analysis result.

## Deploy a topic model

Follow these steps to deploy your topic model from the CX Insights console, so you can use it to analyze future conversations.

  1. From the CX Insights console, click model_training **Topic Models**.
  2. Navigate to the topic model and click more_vert > **Deploy**.



## Re-analyze a conversation

To apply a new change to an existing analysis, follow these steps to re-analyze the conversation in the CX Insights console.

  1. Click news **Conversation Hub**.
  2. Choose one option: 
     * To re-analyze a single conversation, select a conversation from the list and click **Re-analyze**.
     * For bulk analysis, navigate to **Conversation History** , set a conversation filter to **Analysis Status = Has been analyzed** , then click **Analyze**.



## Infer topics

With real-time topic inference, you can use a previously created topic model during a conversation to infer topics in real time. Follow these steps to use the CX Insights API to infer a topic for an end user utterance at runtime.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `contactcenterinsights.analyses.create`



  1. Call the `create` method of the [`analyses`](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.analyses#resource:-analysis) resource.
  2. To run all annotators, call the `create` method without specifying an annotator selector.
  3. The topic inference result is in the [`analysisResult`](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.analyses#analysisresult) resource.



## Undeploy a topic model

If you need to make changes to a deployed topic model before using it to analyze new conversations, you can use the CX Insights API to undeploy it.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `contactcenterinsights.issueModels.undeploy`



  1. Call the `undeploy` method of the [`issueModel`](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.issueModels#resource:-issuemodel) resource.



Undeploying a model is a long-running operation, and you can [poll the status of the operation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/long-running-operations) to see if it has completed.

## Delete a topic model

Lastly, you can use the CX Insights API to delete a topic model.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `contactcenterinsights.issueModels.delete`



  1. Call the `delete` method of the [`issueModel`](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.issueModels#resource:-issuemodel) resource.



Deleting a topic model is also a long-running operation, so you can [poll its status](https://docs.cloud.google.com/gemini-enterprise-cx/insights/long-running-operations) to find out if it has completed.

## What's next

  * [Topic modeling best practices](https://docs.cloud.google.com/gemini-enterprise-cx/insights/topic-modeling-bp)
  * [Export and import a topic model](https://docs.cloud.google.com/gemini-enterprise-cx/insights/topic-modeling-export-import)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
