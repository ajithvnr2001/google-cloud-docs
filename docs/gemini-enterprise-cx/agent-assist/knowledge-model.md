---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-model/
title: Train a custom knowledge suggestion model \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:44.630967+00:00
---

# Train a custom knowledge suggestion model  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Train a custom knowledge suggestion model Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** This feature is no longer supported. For an alternative, use [generative knowledge assist](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/generative-knowledge-assist).

Agent Assist provides two modeling options for knowledge suggestion: a baseline model (default) and a custom model. This guide walks you through the process of training a custom model using a dataset, then deploying the model and testing its performance.

## Overview

Agent Assist has two **knowledge suggestion** features: [Article Suggestion](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/article-suggestion) (which suggests documents), and [FAQ Assist](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/faq) (which suggests answers to end-user questions). When you implement these features, Agent Assist uses a pre-trained baseline suggestion model by default. The baseline model uses information retrieval technology and does not require you to complete an explicit model training step. The custom model option uses state-of-the-art NLU (Natural Language Understanding) technology. It requires you to upload your conversation transcripts and complete an explicit model training step to build a customized NLU model. On average, custom models provide better quality suggestions than the baseline model.

## Before you begin

Complete the following before starting this guide:

  1. Enable the [Dialog Flow API](https://docs.cloud.google.com/dialogflow/docs/quick/setup) for your Google Cloud project.



## Create a knowledge base and train a custom model

In order to get suggestions from Agent Assist you must create a [knowledge base](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-base), upload your documents to the knowledge base, and configure a [conversation profile](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/basics#conversation_profiles).

The following steps outline these actions using direct API calls, using Article the Suggestion feature as an example. If you prefer, you can create a knowledge base and documents to it using [Agent Assist Console](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-base) instead.

### Create a knowledge base

Before you can begin uploading documents you must first create a knowledge base to put them in. To create a knowledge base, call the `create` method on the [`KnowledgeBase`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.knowledgeBases) type.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your GCP project ID
  * KNOWLEDGE_BASE_DISPLAY_NAME: desired knowledge base name



HTTP method and URL: 
    
    
    POST https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/knowledgeBases

Request JSON body: 
    
    
    {
      "displayName": "KNOWLEDGE_BASE_DISPLAY_NAME"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/knowledgeBases"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/knowledgeBases" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/knowledgeBases/NDA4MTM4NzE2MjMwNDUxMjAwMA",
      "displayName": "KNOWLEDGE_BASE_DISPLAY_NAME"
    }
    

The path segment after `knowledgeBases` contains your new knowledge base ID. 

### Python

To authenticate to Agent Assist, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def create_knowledge_base(project_id, display_name):
        """Creates a Knowledge base.
    
        Args:
            project_id: The GCP project linked with the agent.
            display_name: The display name of the Knowledge base."""
        from google.cloud import dialogflow_v2beta1 as dialogflow
    
        client = dialogflow.KnowledgeBasesClient()
        project_path = client.common_project_path(project_id)
    
        knowledge_base = dialogflow.KnowledgeBase(display_name=display_name)
    
        response = client.create_knowledge_base(
            parent=project_path, knowledge_base=knowledge_base
        )
    
        print("Knowledge Base created:\n")
        print("Display Name: {}\n".format(response.display_name))
        print("Name: {}\n".format(response.name))
    
    

### Create a knowledge document

You can now add documents to the knowledge base. To create a document in the knowledge base, [call the `create` method on the `Document` type](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.knowledgeBases.documents). Set [`KnowledgeType`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.agent.knowledgeBases.documents#Document.KnowledgeType) to `ARTICLE_SUGGESTION`. This example uses an [HTML file with return order information](https://storage.cloud.google.com/agent-assist-public-examples/public_article_suggestion_example_returns.html) that was uploaded to a publicly shared [Cloud Storage](https://docs.cloud.google.com/storage/docs/quickstart-console) bucket. When you set up Article Suggestion in your own system, documents must be in one of the following formats. See the [knowledge documents documentation](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-documents) for more information about document best practices.

Knowledge document formats:

  * A file stored in a Cloud Storage bucket. You can specify the path when you call the API.
  * The text contents of a document, which you can send in an API request.
  * A public URL.

**Note:** When you create a new knowledge document, it may take a few hours before the document is available for suggestions.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your GCP project ID
  * KNOWLEDGE_BASE_ID: your knowledge base ID returned from previous request
  * DOCUMENT_DISPLAY_NAME: desired knowledge document name



HTTP method and URL: 
    
    
    POST https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/knowledgeBases/KNOWLEDGE_BASE_ID/documents

Request JSON body: 
    
    
    {
      "displayName": "DOCUMENT_DISPLAY_NAME",
      "mimeType": "text/html",
      "knowledgeTypes": "ARTICLE_SUGGESTION",
      "contentUri": "gs://agent-assist-public-examples/public_article_suggestion_example_returns.html"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/knowledgeBases/KNOWLEDGE_BASE_ID/documents"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/knowledgeBases/KNOWLEDGE_BASE_ID/documents" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/operations/**ks-add_document-MzA5NTY2MTc5Mzg2Mzc5NDY4OA** "
    }
    

The response is a [long-running operation](https://docs.cloud.google.com/dialogflow/docs/how/long-running-operations), which you can poll to check for completion. 

### Python

To authenticate to Agent Assist, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def create_document(
        project_id, knowledge_base_id, display_name, mime_type, knowledge_type, content_uri
    ):
        """Creates a Document.
    
        Args:
            project_id: The GCP project linked with the agent.
            knowledge_base_id: Id of the Knowledge base.
            display_name: The display name of the Document.
            mime_type: The mime_type of the Document. e.g. text/csv, text/html,
                text/plain, text/pdf etc.
            knowledge_type: The Knowledge type of the Document. e.g. FAQ,
                EXTRACTIVE_QA.
            content_uri: Uri of the document, e.g. gs://path/mydoc.csv,
                http://mypage.com/faq.html."""
        from google.cloud import dialogflow_v2beta1 as dialogflow
    
        client = dialogflow.DocumentsClient()
        knowledge_base_path = dialogflow.KnowledgeBasesClient.knowledge_base_path(
            project_id, knowledge_base_id
        )
    
        document = dialogflow.Document(
            display_name=display_name, mime_type=mime_type, content_uri=content_uri
        )
    
        document.knowledge_types.append(
            getattr(dialogflow.Document.KnowledgeType, knowledge_type)
        )
    
        response = client.create_document(parent=knowledge_base_path, document=document)
        print("Waiting for results...")
        document = response.result(timeout=120)
        print("Created Document:")
        print(" - Display Name: {}".format(document.display_name))
        print(" - Knowledge ID: {}".format(document.name))
        print(" - MIME Type: {}".format(document.mime_type))
        print(" - Knowledge Types:")
        for knowledge_type in document.knowledge_types:
            print("    - {}".format(KNOWLEDGE_TYPES[knowledge_type]))
        print(" - Source: {}\n".format(document.content_uri))
    
    

### Create & deploy a new custom model

  1. Navigate to the [Agent Assist UI](https://agentassist.cloud.google.com/projects/ccai-ui-dev/data/datasets) and click the **Models** menu option on the far left margin of the page.

  2. The **Models** menu displays all of your models. To create a new model, click the **+Create new** button at the top right.

  3. Under **Model type** select **Article suggestion**. Enter a unique name for your new model in the **Name** field. Finally, select the name(s) of the knowledge base(s) that you want to use to train your model. When you click this field a menu appears that contains a list of all of your already-created datasets.

  4. A knowledge suggestion model is trained by using conversation datasets, the same as a Smart Reply model. Instead of surfacing word suggestions to agents like the Smart Reply feature, knowledge suggestion models will surface articles or FAQ answers.

Select as many conversation datasets as you'd like to use to train your model. Click **Create** to create your new model.

  5. The new model now appears in your list of models on the **Models** page. The new model's status will appear as **Pending** and then **Creating** until the model is trained. Training takes a day or more depending on your computing resources. To deploy your trained model, click the icon made up of 3 vertical dots that's associated with your model at the far right of the page and click **Deploy**.




## Test your custom knowledge assist model using the Agent Assist simulator

The Agent Assist simulator lets you preview your model's performance before you implement it. The simulator can be used with any Agent Assist feature. The following steps walk you through the process of testing your custom knowledge assist model using the simulator.

  1. Before you can run the simulator, you must create one or more **conversation profiles**. A conversation profile represents a trained and deployed knowledge assist model. Unlike Smart Reply models, knowledge assist models don't have an associated allowlist.

To create a conversation profile, click **Conversation profiles** in the main menu at the left side of the page.

  2. A list of your existing conversation profiles appears. If you want to use a pre-existing profile you can skip to Step 4, later. Otherwise, create a new conversation profile by clicking the **+Create new** button on the right side of the page.

  3. In the menu that appears, enter a unique name for your conversation profile in the **Display name** box. Select either **Articles** or **FAQs** (depending on which type of model you trained) from the **Suggestion type** box. You are also asked to input **Confidence threshold** and **Maximum suggestions** values. Maximum suggestions is the number of response articles or FAQ answers returned, and the confidence threshold refers to the model's level of confidence that each response is relevant to the agent's request. A higher confidence value increases the likelihood of relevant responses being returned, but can result in fewer or no responses returned if no available option meets the high threshold value. For higher accuracy and lower coverage, we recommend a confidence threshold of 0.8; for lower accuracy and higher coverage, we recommend a confidence threshold of 0.2.

Choose your **Retrieval method** (inline or Pub/Sub), whether or not to enable [sentiment analysis](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/sentiment-analysis), and whether or not to use a [Dialogflow virtual agent](https://docs.cloud.google.com/dialogflow/cx/docs) Click the **Create** button to create the conversation profile.

  4. Your conversation profile now appears in the list of profiles on the main **Conversation profiles** page. To use the simulator, click the three vertical dots to the far right of the conversation profile name that you want to test and click **Use simulator**.

  5. The window that appears provides you with input boxes for both customer and agent responses. You can use these boxes to test the Agent Assist features that you selected when you configured the conversation profile. To change which combination of feature(s) are being tested, click the **Options** button at the top right and choose your feature(s) from the **Configure view** menu that appears.

  6. Click the **Done** button at the top right to return to the main conversation profiles page.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
