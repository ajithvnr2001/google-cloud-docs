---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/faq/
title: FAQ assist \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:44:30.966952+00:00
---

# FAQ assist  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/faq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  FAQ assist Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Caution:** FAQ assist will be [deprecated](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/deprecations) on April 1, 2026. As of August 21, 2025 you can no longer create new conversation profiles for this feature, and existing profiles will be removed on or after April 1, 2026. For an alternative, use [generative knowledge assist](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/generative-knowledge-assist).

FAQ Assist suggests relevant FAQ answers to human agents during a conversation with an end-user. This feature can be used to help a human agent answer common end-user questions while the human agent and end-user are in a conversation.

Agent Assist follows the conversation and parses FAQ documents stored in [knowledge bases](https://docs.cloud.google.com/dialogflow/docs/how/knowledge-bases) to suggest answers to end-user questions. A human agent can examine these suggestions while the conversation proceeds and make a decision about which suggestions to share with the end-user.

This document walks you through the process of using the API to implement FAQ Assist and get suggestions from this feature during runtime. You have the option of using the [Agent Assist console](https://agentassist.cloud.google.com) to test your Article Suggestion results during design-time, but you must call the API directly during runtime. See the [tutorials section](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/tutorials) for details about testing feature performance using the Agent Assist console.

## Before you begin

Complete the following before starting this guide:

  1. Enable the [Dialogflow API](https://docs.cloud.google.com/dialogflow/docs/quick/setup) for your Google Cloud project.



## Configure a conversation profile

In order to get suggestions from Agent Assist you must create a [knowledge base](https://docs.cloud.google.com/dialogflow/docs/how/knowledge-bases) containing your uploaded documents and configure a [conversation profile](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/basics#conversation_profiles). You can also perform these actions using the [Agent Assist Console](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/tutorials) if you would prefer not to call the API directly.

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

You can now add documents to the knowledge base. To create a document in the knowledge base, [call the `create` method on the `Document` type](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.knowledgeBases.documents). Set [`KnowledgeType`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.agent.knowledgeBases.documents#Document.KnowledgeType) to `FAQ`. This example uses the [Cloud Storage FAQ](https://docs.cloud.google.com/storage/docs/faq) document that was uploaded to a publicly shared [Cloud Storage](https://docs.cloud.google.com/storage/docs/quickstart-console) bucket. When you set up Article Suggestion in your own system, documents must be in one of the following formats. See the [knowledge documents documentation](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-documents) for more information about document best practices.

The FAQ document can be in one of three formats:

  * A public URL.
  * A Cloud Storage path to a `csv` file.
  * A `csv` file (that you will include in the API request).



If your document is in `csv` format, it must contain two columns: FAQ questions must be listed in the first column, and the answers to each question must be listed in the second column. Each FAQ question and its associated answer is called an **FAQ pair**. Make sure that the `csv` file does not contain a header row. If your document is a public URL, it must be an FAQ page listing multiple FAQ pairs.

See the [knowledge documents documentation](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-documents) for best practices information.

**Note:** When you create a knowledge document, it may take up to one day before the document is available for suggestions.

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
      "knowledgeTypes": "FAQ",
      "contentUri": "https://cloud.google.com/storage/docs/faq"
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
    
    

### Create a conversation profile

A _conversation profile_ configures a set of parameters that control the suggestions made to an agent during a conversation. The following steps create a [`ConversationProfile`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversationProfiles) with a [`HumanAgentAssistantConfig`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversationProfiles#ConversationProfile.HumanAgentAssistantConfig) object. You can also perform these actions using the [Agent Assist Console](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/tutorials) if you would prefer not to call the API directly.

Inline suggestions are enabled by default. Optionally, you can [enable Cloud Pub/Sub notifications](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/pub-sub) when you configure the conversation profile.

### REST

To create a conversation profile, call the `create` method on the [`ConversationProfile`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversationProfiles) resource. 

`noSmallTalk`: If `true`, suggestions will not be triggered after small talk messages (such as "hi", "how are you", and so on). If `false`, suggestions will be triggered after small talk messages.

`onlyEndUser`: If `true`, suggestions will be triggered only after end-user messages. If `false`, suggestions will be triggered after both end-user and human agent messages.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your GCP project ID
  * KNOWLEDGE_BASE_ID: your knowledge base ID



HTTP method and URL: 
    
    
    POST https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/conversationProfiles

Request JSON body: 
    
    
    {
      "displayName": "my-conversation-profile-display-name",
      "humanAgentAssistantConfig": {
        "humanAgentSuggestionConfig": {
          "featureConfigs": [
            {
              "suggestionFeature": {
                "type": "FAQ"
              },
              "queryConfig": {
                "knowledgeBaseQuerySource": {
                  "knowledgeBases": ["projects/PROJECT_ID/knowledgeBases/KNOWLEDGE_BASE_ID"]
                }
              },
              "enableEventBasedSuggestion": false,
              "enableInlineSuggestion": true,
              "SuggestionTriggerSettings": {
                 "noSmallTalk": true,
                 "onlyEndUser": true,
               }
            }
          ]
        }
      }
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
         "https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/conversationProfiles"

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
        -Uri "https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/conversationProfiles" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/conversationProfiles/CONVERSATION_PROFILE_ID",
      "displayName": "my-conversation-profile-display-name",
      "humanAgentAssistantConfig": {
        ...
      }
    }
    

The path segment after `conversationProfiles` contains your new conversation profile ID. 

### Python

To authenticate to Agent Assist, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def create_conversation_profile_article_faq(
        project_id,
        display_name,
        article_suggestion_knowledge_base_id=None,
        faq_knowledge_base_id=None,
    ):
        """Creates a conversation profile with given values
    
        Args: project_id:  The GCP project linked with the conversation profile.
            display_name: The display name for the conversation profile to be
            created.
            article_suggestion_knowledge_base_id: knowledge base id for article
            suggestion.
            faq_knowledge_base_id: knowledge base id for faq."""
    
        client = dialogflow.ConversationProfilesClient()
        project_path = client.common_project_path(project_id)
    
        conversation_profile = {
            "display_name": display_name,
            "human_agent_assistant_config": {
                "human_agent_suggestion_config": {"feature_configs": []}
            },
            "language_code": "en-US",
        }
    
        if article_suggestion_knowledge_base_id is not None:
            as_kb_path = dialogflow.KnowledgeBasesClient.knowledge_base_path(
                project_id, article_suggestion_knowledge_base_id
            )
            feature_config = {
                "suggestion_feature": {"type_": "ARTICLE_SUGGESTION"},
                "suggestion_trigger_settings": {
                    "no_small_talk": True,
                    "only_end_user": True,
                },
                "query_config": {
                    "knowledge_base_query_source": {"knowledge_bases": [as_kb_path]},
                    "max_results": 3,
                },
            }
            conversation_profile["human_agent_assistant_config"][
                "human_agent_suggestion_config"
            ]["feature_configs"].append(feature_config)
        if faq_knowledge_base_id is not None:
            faq_kb_path = dialogflow.KnowledgeBasesClient.knowledge_base_path(
                project_id, faq_knowledge_base_id
            )
            feature_config = {
                "suggestion_feature": {"type_": "FAQ"},
                "suggestion_trigger_settings": {
                    "no_small_talk": True,
                    "only_end_user": True,
                },
                "query_config": {
                    "knowledge_base_query_source": {"knowledge_bases": [faq_kb_path]},
                    "max_results": 3,
                },
            }
            conversation_profile["human_agent_assistant_config"][
                "human_agent_suggestion_config"
            ]["feature_configs"].append(feature_config)
    
        response = client.create_conversation_profile(
            parent=project_path, conversation_profile=conversation_profile
        )
    
        print("Conversation Profile created:")
        print("Display Name: {}".format(response.display_name))
        # Put Name is the last to make it easier to retrieve.
        print("Name: {}".format(response.name))
        return response
    
    

### (Optional) Set security settings

You have the option of setting security parameters to help address issues such as data redaction and data retention. To do this, you must create a [`SecuritySettings`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings) resource, then link it to a conversation profile using the [`securitySettings` field](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversationProfiles).

Security settings added to a conversation profile affect the behavior of Agent Assist text messages _only_. The behavior of the Dialogflow interaction history is controlled by [Dialogflow's security settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/security-settings), which you can set using the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).

## Handle conversations at runtime

### Create a conversation

When a dialog begins between an end-user and a human or virtual agent, you create a _conversation_. **In order to see suggestions, you must also create both an end-user participant and a human agent participant and add them to the conversation**. The following sections walk you through this process.

First, you must create a conversation:

### REST

To create a conversation, call the `create` method on the [`Conversation`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversations) resource. 

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Cloud project ID
  * LOCATION_ID: your location ID
  * CONVERSATION_PROFILE_ID: the ID you received when creating the conversation profile



HTTP method and URL: 
    
    
    POST https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION_ID/conversations

Request JSON body: 
    
    
    {
      "conversationProfile": "projects/PROJECT_ID/locations/LOCATION_ID/conversationProfiles/CONVERSATION_PROFILE_ID",
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
         "https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION_ID/conversations"

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
        -Uri "https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION_ID/conversations" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION_ID/conversations/CONVERSATION_ID",
      "lifecycleState": "IN_PROGRESS",
      "conversationProfile": "projects/PROJECT_ID/locations/LOCATION_ID/conversationProfiles/CONVERSATION_PROFILE_ID",
      "startTime": "2018-11-05T21:05:45.622Z"
    }
    

The path segment after `conversations` contains your new conversation ID. 

### Python

To authenticate to Agent Assist, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def create_conversation(project_id, conversation_profile_id):
        """Creates a conversation with given values
    
        Args:
            project_id:  The GCP project linked with the conversation.
            conversation_profile_id: The conversation profile id used to create
            conversation."""
    
        client = dialogflow.ConversationsClient()
        conversation_profile_client = dialogflow.ConversationProfilesClient()
        project_path = client.common_project_path(project_id)
        conversation_profile_path = conversation_profile_client.conversation_profile_path(
            project_id, conversation_profile_id
        )
        conversation = {"conversation_profile": conversation_profile_path}
        response = client.create_conversation(
            parent=project_path, conversation=conversation
        )
    
        print("Life Cycle State: {}".format(response.lifecycle_state))
        print("Conversation Profile Name: {}".format(response.conversation_profile))
        print("Name: {}".format(response.name))
        return response
    
    

### Create an end-user participant

You must add both end-user and human agent participants to the conversation in order to see suggestions. First, add the end-user participant to the conversation:

### REST

To create an end-user participant, call the `create` method on the [`Participant`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversations.participants) resource.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Cloud project ID
  * LOCATION_ID: your location ID
  * CONVERSATION_ID: your conversation ID



HTTP method and URL: 
    
    
    POST https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION_ID/conversations/CONVERSATION_ID/participants

Request JSON body: 
    
    
    {
      "role": "END_USER",
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
         "https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION_ID/conversations/CONVERSATION_ID/participants"

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
        -Uri "https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION_ID/conversations/CONVERSATION_ID/participants" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION_ID/conversations/CONVERSATION_ID/participants/PARTICIPANT_ID",
      "role": "END_USER"
    }
    

The path segment after `participants` contains your new end-user participant ID. 

### Python

To authenticate to Agent Assist, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def create_participant(project_id: str, conversation_id: str, role: str):
        from google.cloud import dialogflow_v2beta1 as dialogflow
    
        """Creates a participant in a given conversation.
    
        Args:
            project_id: The GCP project linked with the conversation profile.
            conversation_id: Id of the conversation.
            participant: participant to be created."""
    
        client = dialogflow.ParticipantsClient()
        conversation_path = dialogflow.ConversationsClient.conversation_path(
            project_id, conversation_id
        )
        if role in ROLES:
            response = client.create_participant(
                parent=conversation_path, participant={"role": role}, timeout=600
            )
            print("Participant Created.")
            print(f"Role: {response.role}")
            print(f"Name: {response.name}")
    
            return response
    
    

### Create a human agent participant

Add a human agent participant to the conversation:

### REST

To create a human agent participant, call the `create` method on the [`Participant`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversations.participants) resource.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Cloud project ID
  * LOCATION_ID: your location ID
  * CONVERSATION_ID: your conversation ID



HTTP method and URL: 
    
    
    POST https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION_ID/conversations/CONVERSATION_ID/participants

Request JSON body: 
    
    
    {
      "role": "HUMAN_AGENT",
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
         "https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION_ID/conversations/CONVERSATION_ID/participants"

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
        -Uri "https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION_ID/conversations/CONVERSATION_ID/participants" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION_ID/conversations/CONVERSATION_ID/participants/PARTICIPANT_ID",
      "role": "HUMAN_AGENT"
    }
    

The path segment after `participants` contains your new human agent participant ID. 

### Python

To authenticate to Agent Assist, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def create_participant(project_id: str, conversation_id: str, role: str):
        from google.cloud import dialogflow_v2beta1 as dialogflow
    
        """Creates a participant in a given conversation.
    
        Args:
            project_id: The GCP project linked with the conversation profile.
            conversation_id: Id of the conversation.
            participant: participant to be created."""
    
        client = dialogflow.ParticipantsClient()
        conversation_path = dialogflow.ConversationsClient.conversation_path(
            project_id, conversation_id
        )
        if role in ROLES:
            response = client.create_participant(
                parent=conversation_path, participant={"role": role}, timeout=600
            )
            print("Participant Created.")
            print(f"Role: {response.role}")
            print(f"Name: {response.name}")
    
            return response
    
    

### Add and analyze a message from the human agent

Each time either participant types a message in the conversation, you need to send that message to the API for processing. Agent Assist bases its suggestions on analysis of human agent and end-user messages. In the following example, the human agent starts the conversation by asking "How may I help you?". No suggestions are returned yet in the response.

### REST

To add and analyze a human agent message for the conversation, call the `analyzeContent` method on the [`Participant`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversations.participants) resource.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your GCP project ID
  * CONVERSATION_ID: your conversation ID
  * PARTICIPANT_ID: your human agent participant ID



HTTP method and URL: 
    
    
    POST https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/conversations/CONVERSATION_ID/participants/PARTICIPANT_ID:analyzeContent

Request JSON body: 
    
    
    {
      "textInput": {
        "text": "How may I help you?",
        "languageCode": "en-US"
      }
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
         "https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/conversations/CONVERSATION_ID/participants/PARTICIPANT_ID:analyzeContent"

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
        -Uri "https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/conversations/CONVERSATION_ID/participants/PARTICIPANT_ID:analyzeContent" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
          {
            "message": {
              "name": "projects/PROJECT_ID/conversations/CONVERSATION_ID/messages/MESSAGE_ID",
              "content": "How may I help you?",
              "languageCode": "en-US",
              "participant": "PARTICIPANT_ID",
              "participantRole": "HUMAN_AGENT",
              "createTime": "2020-02-13T00:01:30.683Z"
            },
            "humanAgentSuggestionResults": [
              {
                "suggestArticlesResponse": {
                  "latestMessage": "projects/PROJECT_ID/conversations/CONVERSATION_ID/messages/MESSAGE_ID",
                  "contextSize": 1
                }
              }
            ]
          }
        }
      ]
    }
    

### Python

To authenticate to Agent Assist, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def analyze_content_text(
        project_id: str, conversation_id: str, participant_id: str, text: str
    ):
        from google.cloud import dialogflow_v2beta1 as dialogflow
    
        """Analyze text message content from a participant.
    
        Args:
            project_id: The GCP project linked with the conversation profile.
            conversation_id: Id of the conversation.
            participant_id: Id of the participant.
            text: the text message that participant typed."""
    
        client = dialogflow.ParticipantsClient()
        participant_path = client.participant_path(
            project_id, conversation_id, participant_id
        )
        text_input = {"text": text, "language_code": "en-US"}
        response = client.analyze_content(
            participant=participant_path, text_input=text_input
        )
        print("AnalyzeContent Response:")
        print(f"Reply Text: {response.reply_text}")
    
        for suggestion_result in response.human_agent_suggestion_results:
            if suggestion_result.error is not None:
                print(f"Error: {suggestion_result.error.message}")
            if suggestion_result.suggest_articles_response:
                for answer in suggestion_result.suggest_articles_response.article_answers:
                    print(f"Article Suggestion Answer: {answer.title}")
                    print(f"Answer Record: {answer.answer_record}")
            if suggestion_result.suggest_faq_answers_response:
                for answer in suggestion_result.suggest_faq_answers_response.faq_answers:
                    print(f"Faq Answer: {answer.answer}")
                    print(f"Answer Record: {answer.answer_record}")
            if suggestion_result.suggest_smart_replies_response:
                for (
                    answer
                ) in suggestion_result.suggest_smart_replies_response.smart_reply_answers:
                    print(f"Smart Reply: {answer.reply}")
                    print(f"Answer Record: {answer.answer_record}")
    
        for suggestion_result in response.end_user_suggestion_results:
            if suggestion_result.error:
                print(f"Error: {suggestion_result.error.message}")
            if suggestion_result.suggest_articles_response:
                for answer in suggestion_result.suggest_articles_response.article_answers:
                    print(f"Article Suggestion Answer: {answer.title}")
                    print(f"Answer Record: {answer.answer_record}")
            if suggestion_result.suggest_faq_answers_response:
                for answer in suggestion_result.suggest_faq_answers_response.faq_answers:
                    print(f"Faq Answer: {answer.answer}")
                    print(f"Answer Record: {answer.answer_record}")
            if suggestion_result.suggest_smart_replies_response:
                for (
                    answer
                ) in suggestion_result.suggest_smart_replies_response.smart_reply_answers:
                    print(f"Smart Reply: {answer.reply}")
                    print(f"Answer Record: {answer.answer_record}")
    
        return response
    
    

### Add a message from the end-user and get suggestions

In response to the agent, the end-user asks "How do I sign up?". The response contains a list of suggested answers to the end-user's question as well as a confidence score for each. All answers were drawn from the single FAQ knowledge document that we [added earlier in this tutorial](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/faq#create_a_knowledge_document). The confidence threshold refers to the model's level of confidence that each FAQ suggestion is relevant to the agent's request. A higher confidence value increases the likelihood of relevant responses being returned, but can result in fewer or no responses returned if no available option meets the high threshold value. We recommend a starting confidence score value of 0.4. You can adjust this value later to improve your results if needed.

The response also includes the answer's `source`, the knowledge document that the answer came from. You should provide the suggested answers to your human agent, who might choose to provide this information to the end-user.

### REST

To add and analyze an end-user message for the conversation, call the `analyzeContent` method on the [`Participant`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversations.participants) resource.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your GCP project ID
  * CONVERSATION_ID: your conversation ID
  * PARTICIPANT_ID: your end-user participant ID



HTTP method and URL: 
    
    
    POST https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/conversations/CONVERSATION_ID/participants/PARTICIPANT_ID:analyzeContent

Request JSON body: 
    
    
    {
      "textInput": {
        "text": "How do I sign up?",
        "languageCode": "en-US"
      }
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
         "https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/conversations/CONVERSATION_ID/participants/PARTICIPANT_ID:analyzeContent"

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
        -Uri "https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/conversations/CONVERSATION_ID/participants/PARTICIPANT_ID:analyzeContent" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "message": {
        "name": "projects/PROJECT_ID/conversations/fiiJBeHnQIa6Zx_DUKNlEg/messages/Rjv8ErKYS_yIqVR9SW4CpA",
        "content": "How may I help you?",
        "languageCode": "en-US",
        "participant": "PaZQyeiTQgCOyliHkZjs0Q",
        "participantRole": "HUMAN_AGENT",
        "createTime": "1970-01-01T00:00:00Z"
      },
      "humanAgentSuggestionResults": [
        {
          "suggestFaqAnswersResponse": {
            "faqAnswers": [
              {
                "answer": "Sign up for Cloud Storage by turning on the Cloud Storage service in the Google Cloud Platform Console.",
                "confidence": 0.07266401,
                "question": "How do I sign up?",
                "source": "projects/PROJECT_ID/knowledgeBases/NjQ2MzI1MDQwNTQ2MjYzODU5Mg/documents/NTMxOTA4MTAxMzQxMjg4ODU3Ng",
                "metadata": {
                  "document_display_name": "my-document-display-name"
                },
                "answerRecord": "projects/PROJECT_ID/answerRecords/MTU0MzE0NDQwOTAwNzEyODU3NjA"
              },
              {
                "answer": "Consider storing your data in a multi-regional or dual-regional bucket location if high availability is a top requirement. This ensures that your data is stored in at least two geographically separated regions, providing continued availability even in the rare event of a region-wide outage, including ones caused by natural disasters. All data, regardless of storage class, is stored redundantly across regions in these types of locations, which allows you to use storage lifecycle management without giving up high availability.",
                "confidence": 0.06937904,
                "question": "How can I maximize the availability of my data?",
                "source": "projects/PROJECT_ID/knowledgeBases/NjQ2MzI1MDQwNTQ2MjYzODU5Mg/documents/NTMxOTA4MTAxMzQxMjg4ODU3Ng",
                "metadata": {
                  "document_display_name": "my-document-display-name"
                },
                "answerRecord": "projects/PROJECT_ID/answerRecords/MzkwMjIyOTA0NDAwMjgxNjAwMA"
              },
              {
                "answer": "From the Cloud Storage documentation click \"Send feedback\" near the top right of the page. This will open a feedback form. Your comments will be reviewed by the Cloud Storage team.",
                "confidence": 0.069021806,
                "question": "How do I give product feedback?",
                "source": "projects/PROJECT_ID/knowledgeBases/NjQ2MzI1MDQwNTQ2MjYzODU5Mg/documents/NTMxOTA4MTAxMzQxMjg4ODU3Ng",
                "metadata": {
                  "document_display_name": "my-document-display-name"
                },
                "answerRecord": "projects/PROJECT_ID/answerRecords/MTMxMjU2MDEwODA4NTc1OTE4MDg"
              },
              {
                "answer": "Read the Pricing page for detailed information on pricing, including how Cloud Storage calculates bandwidth and storage usage.",
                "confidence": 0.06681696,
                "question": "Where can I find pricing information?",
                "source": "projects/PROJECT_ID/knowledgeBases/NjQ2MzI1MDQwNTQ2MjYzODU5Mg/documents/NTMxOTA4MTAxMzQxMjg4ODU3Ng",
                "metadata": {
                  "document_display_name": "my-document-display-name"
                },
                "answerRecord": "projects/PROJECT_ID/answerRecords/ODUxMzkxNTA2MjQzMDIwMzkwNA"
              },
              {
                "answer": "Use Object Versioning. The Object Versioning feature keeps an archived version of an object whenever you overwrite or delete the live version. If you accidentally delete an object, you can copy an archived version of it back to the live version. It's recommended that you use Object Versioning in conjunction with Object Lifecycle Management. Doing so ensures that you don't have multiple, unnecessary copies of an object, which are each subject to storage costs. Caution: Object Versioning does not protect your data if you delete the entire bucket. As an alternative, use object holds. When you place an object hold on an object, it cannot be deleted or overwritten.",
                "confidence": 0.06453417,
                "question": "How do I protect myself from accidental data deletion?",
                "source": "projects/PROJECT_ID/knowledgeBases/NjQ2MzI1MDQwNTQ2MjYzODU5Mg/documents/NTMxOTA4MTAxMzQxMjg4ODU3Ng",
                "metadata": {
                  "document_display_name": "my-document-display-name"
                },
                "answerRecord": "projects/PROJECT_ID/answerRecords/MTc3MzcyODcwOTkyODQ5Nzk3MTI"
              },
              {
                "answer": "You can share an individual object with a user or group by adding an entry to that object's access control list (ACL) that grants the user or group READ permission. For step-by-step instructions, see Changing ACLs.",
                "confidence": 0.06336816,
                "question": "I want to let someone download an individual object. How do I do that?",
                "source": "projects/PROJECT_ID/knowledgeBases/NjQ2MzI1MDQwNTQ2MjYzODU5Mg/documents/NTMxOTA4MTAxMzQxMjg4ODU3Ng",
                "metadata": {
                  "document_display_name": "my-document-display-name"
                },
                "answerRecord": "projects/PROJECT_ID/answerRecords/MTAxOTkyNTI4MjQ4NTY5ODU2MA"
              },
              {
                "answer": "You can simply install and use the Google Cloud CLI to download the data, even without a Google account. You do not need to activate Cloud Storage or turn on billing for this purpose. You also do not need to create credentials or authenticate to Cloud Storage.",
                "confidence": 0.061990723,
                "question": "I am just trying to download or access some data that is available to the public. How can I do that?",
                "source": "projects/PROJECT_ID/knowledgeBases/NjQ2MzI1MDQwNTQ2MjYzODU5Mg/documents/NTMxOTA4MTAxMzQxMjg4ODU3Ng",
                "metadata": {
                  "document_display_name": "my-document-display-name"
                },
                "answerRecord": "projects/PROJECT_ID/answerRecords/MTAyNDMyOTczMTkzNDA0NzQzNjg"
              },
              {
                "answer": "Certain types of content are not allowed on this service; please refer to the Terms of Services and Platform Policies for details. If you believe a piece of content is in violation of our policies, report it here (select See more products, then Google Cloud Storage & Cloud Bigtable).",
                "confidence": 0.060459033,
                "question": "I believe some content hosted on your service is inappropriate, how do I report it?",
                "source": "projects/PROJECT_ID/knowledgeBases/NjQ2MzI1MDQwNTQ2MjYzODU5Mg/documents/NTMxOTA4MTAxMzQxMjg4ODU3Ng",
                "metadata": {
                  "document_display_name": "my-document-display-name"
                },
                "answerRecord": "projects/PROJECT_ID/answerRecords/NTYzMTYxMTMwMDkxMzA4NjQ2NA"
              },
              {
                "answer": "For most common Cloud Storage operations, you only need to specify the relevant bucket's name, not the project associated with the bucket. In general, you only need to specify a project identifier when creating a bucket or listing buckets in a project. For more information, see When to specify a project. To find which project contains a specific bucket: If you are searching over a moderate number of projects and buckets, use the Google Cloud Platform Console, select each project, and view the buckets it contains. Otherwise, go to the storage.bucket.get page in the API Explorer and enter the bucket's name in the bucket field. When you click Authorize and Execute, the associated project number appears as part of the response. To get the project name, use the project number in the following terminal command: gcloud projects list | grep [PROJECT_NUMBER]",
                "confidence": 0.05914715,
                "question": "I created a bucket, but don't remember which project I created it in. How can I find it?",
                "source": "projects/PROJECT_ID/knowledgeBases/NjQ2MzI1MDQwNTQ2MjYzODU5Mg/documents/NTMxOTA4MTAxMzQxMjg4ODU3Ng",
                "metadata": {
                  "document_display_name": "my-document-display-name"
                },
                "answerRecord": "projects/PROJECT_ID/answerRecords/MTQ4NTQ5ODMzMzc3Njc4NjIyNzI"
              },
              {
                "answer": "Cloud Storage is designed for 99.999999999% (11 9's) annual durability, which is appropriate for even primary storage and business-critical applications. This high durability level is achieved through erasure coding that stores data pieces redundantly across multiple devices located in multiple availability zones. Objects written to Cloud Storage must be redundantly stored in at least two different availability zones before the write is acknowledged as successful. Checksums are stored and regularly revalidated to proactively verify that the data integrity of all data at rest as well as to detect corruption of data in transit. If required, corrections are automatically made using redundant data. Customers can optionally enable object versioning to add protection against accidental deletion.",
                "confidence": 0.05035359,
                "question": "How durable is my data in Cloud Storage?",
                "source": "projects/PROJECT_ID/knowledgeBases/NjQ2MzI1MDQwNTQ2MjYzODU5Mg/documents/NTMxOTA4MTAxMzQxMjg4ODU3Ng",
                "metadata": {
                  "document_display_name": "my-document-display-name"
                },
                "answerRecord": "projects/PROJECT_ID/answerRecords/MzMyNTc2ODI5MTY5OTM5MjUxMg"
              }
            ],
            "latestMessage": "projects/PROJECT_ID/conversations/fiiJBeHnQIa6Zx_DUKNlEg/messages/Rjv8ErKYS_yIqVR9SW4CpA",
            "contextSize": 1
          }
        }
      ]
    }

### Python

To authenticate to Agent Assist, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def analyze_content_text(
        project_id: str, conversation_id: str, participant_id: str, text: str
    ):
        from google.cloud import dialogflow_v2beta1 as dialogflow
    
        """Analyze text message content from a participant.
    
        Args:
            project_id: The GCP project linked with the conversation profile.
            conversation_id: Id of the conversation.
            participant_id: Id of the participant.
            text: the text message that participant typed."""
    
        client = dialogflow.ParticipantsClient()
        participant_path = client.participant_path(
            project_id, conversation_id, participant_id
        )
        text_input = {"text": text, "language_code": "en-US"}
        response = client.analyze_content(
            participant=participant_path, text_input=text_input
        )
        print("AnalyzeContent Response:")
        print(f"Reply Text: {response.reply_text}")
    
        for suggestion_result in response.human_agent_suggestion_results:
            if suggestion_result.error is not None:
                print(f"Error: {suggestion_result.error.message}")
            if suggestion_result.suggest_articles_response:
                for answer in suggestion_result.suggest_articles_response.article_answers:
                    print(f"Article Suggestion Answer: {answer.title}")
                    print(f"Answer Record: {answer.answer_record}")
            if suggestion_result.suggest_faq_answers_response:
                for answer in suggestion_result.suggest_faq_answers_response.faq_answers:
                    print(f"Faq Answer: {answer.answer}")
                    print(f"Answer Record: {answer.answer_record}")
            if suggestion_result.suggest_smart_replies_response:
                for (
                    answer
                ) in suggestion_result.suggest_smart_replies_response.smart_reply_answers:
                    print(f"Smart Reply: {answer.reply}")
                    print(f"Answer Record: {answer.answer_record}")
    
        for suggestion_result in response.end_user_suggestion_results:
            if suggestion_result.error:
                print(f"Error: {suggestion_result.error.message}")
            if suggestion_result.suggest_articles_response:
                for answer in suggestion_result.suggest_articles_response.article_answers:
                    print(f"Article Suggestion Answer: {answer.title}")
                    print(f"Answer Record: {answer.answer_record}")
            if suggestion_result.suggest_faq_answers_response:
                for answer in suggestion_result.suggest_faq_answers_response.faq_answers:
                    print(f"Faq Answer: {answer.answer}")
                    print(f"Answer Record: {answer.answer_record}")
            if suggestion_result.suggest_smart_replies_response:
                for (
                    answer
                ) in suggestion_result.suggest_smart_replies_response.smart_reply_answers:
                    print(f"Smart Reply: {answer.reply}")
                    print(f"Answer Record: {answer.answer_record}")
    
        return response
    
    

### Complete the conversation

When the conversation ends, use the API to complete the conversation.

### REST

To complete the conversation, call the `complete` method on the [`conversations`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversations) resource. 

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your GCP project ID
  * CONVERSATION_ID: the ID you received when creating the conversation



HTTP method and URL: 
    
    
    POST https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/conversations/CONVERSATION_ID:complete

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/conversations/CONVERSATION_ID:complete"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/conversations/CONVERSATION_ID:complete" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/conversations/CONVERSATION_ID",
      "lifecycleState": "COMPLETED",
      "conversationProfile": "projects/PROJECT_ID/conversationProfiles/CONVERSATION_PROFILE_ID",
      "startTime": "2018-11-05T21:05:45.622Z",
      "endTime": "2018-11-06T03:50:26.930Z"
    }
    

### Python

To authenticate to Agent Assist, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def complete_conversation(project_id, conversation_id):
        """Completes the specified conversation. Finished conversations are purged from the database after 30 days.
    
        Args:
            project_id: The GCP project linked with the conversation.
            conversation_id: Id of the conversation."""
    
        client = dialogflow.ConversationsClient()
        conversation_path = client.conversation_path(project_id, conversation_id)
        conversation = client.complete_conversation(name=conversation_path)
        print("Completed Conversation.")
        print("Life Cycle State: {}".format(conversation.lifecycle_state))
        print("Conversation Profile Name: {}".format(conversation.conversation_profile))
        print("Name: {}".format(conversation.name))
        return conversation
    
    

## API request options

The previous sections show how to create a [`ConversationProfile`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversationProfiles#resource:-conversationprofile) in order to receive suggestions. The following sections outline some optional functionalities that you can implement during a conversation.

### Pub/Sub suggestion notifications

In the sections earlier, the [ConversationProfile](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversationProfiles) was created with only a human agent assistant. During the conversation you needed to call the API to receive suggestions after each message was added to the conversation. If you prefer to receive notification events for suggestions, you can set the `notificationConfig` field when creating the conversation profile. This option uses [Cloud Pub/Sub](https://docs.cloud.google.com/pubsub/docs) to send suggestion notifications to your application as the conversation proceeds and new suggestions are available.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
