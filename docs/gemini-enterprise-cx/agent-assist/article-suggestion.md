---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/article-suggestion/
title: Article Suggestion \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:44:30.125506+00:00
---

# Article Suggestion  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/article-suggestion/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Article Suggestion Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Article suggestion will be [deprecated](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/deprecations) on April 1, 2026. As of August 21, 2025 you can no longer create new conversation profiles for this feature, and existing profiles will be removed on or after April 1, 2026. For an alternative, use [generative knowledge assist](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/generative-knowledge-assist).

The Agent Assist Article Suggestion feature follows a conversation between a human agent and an end-user and provides the human agent with relevant document suggestions. A human agent can examine these suggestions while the conversation proceeds and make a decision about which documents to read or to share with the end-user. You can use Article Suggestion to help a human agent understand and resolve end-user issues while the human agent and end-user are in a conversation.

Agent Assist provides baseline Article Suggestion models that you can use to suggest articles to your agents. Optionally, you can train a custom model using your own uploaded conversation data to improve performance. If you want to train a custom suggestion model for use with Article Suggestion, contact your Google representative.

This document walks you through the process of using the API to implement Article Suggestion and get suggestions from this feature during runtime. You have the option of using the [Agent Assist Console](https://agentassist.cloud.google.com) to test your Article Suggestion results during design-time, but you must call the API directly during runtime. See the [tutorials section](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/tutorials) for details about testing feature performance using the Agent Assist Console.

## Before you begin

Complete the following before starting this guide:

  1. Enable the [Dialogflow API](https://docs.cloud.google.com/dialogflow/docs/quick/setup) for your Google Cloud project.



## Configure a conversation profile

In order to get suggestions from Agent Assist you must create a [knowledge base](https://docs.cloud.google.com/dialogflow/docs/how/knowledge-bases) containing your uploaded documents and configure a [conversation profile](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/basics#conversation_profiles). You can also perform these actions using the [Agent Assist Console](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/tutorials) if you would prefer not to call the API directly.

### Create a knowledge base

Before you can begin uploading documents you must first create a knowledge base to put them in. To create a knowledge base, call the `create` method on the [`KnowledgeBase`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.knowledgeBases) type.

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

You can now add documents to the knowledge base. To create a document in the knowledge base, [call the `create` method on the `Document` type](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.knowledgeBases.documents). Set [`KnowledgeType`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.knowledgeBases.documents#Document.KnowledgeType) to `ARTICLE_SUGGESTION`. This example uses an [HTML file with return order information](https://storage.cloud.google.com/agent-assist-public-examples/public_article_suggestion_example_returns.html) that was uploaded to a publicly shared [Cloud Storage](https://docs.cloud.google.com/storage/docs/quickstart-console) bucket. When you set up Article Suggestion in your own system, documents must be in one of the following formats. See the [knowledge documents documentation](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-documents) for more information about document best practices.

Knowledge document formats:

  * A file stored in a Cloud Storage bucket. You can specify the path when you call the API.
  * The text contents of a document, which you can send in an API request.
  * A public URL.

**Note:** When you create a knowledge document, it can take up to one day before the document is available for suggestions.

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
    
    

### Create a conversation profile

A _conversation profile_ configures a set of parameters that control the suggestions made to an agent during a conversation. The following steps create a [`ConversationProfile`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles) with a [`HumanAgentAssistantConfig`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.HumanAgentAssistantConfig) object. You can also perform these actions using the [Agent Assist Console](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-profile) if you would prefer not to call the API directly.

We recommend that you set an initial confidence threshold of 0.44 (0.1 if you are using the legacy baseline model). You can increase the threshold beyond the recommended range if necessary. Increasing the threshold results in higher accuracy and lower coverage results (fewer suggestions); decreasing the threshold results in lower accuracy and higher coverage (more suggestions).

Inline suggestions are enabled by default. Optionally, you can [enable Cloud Pub/Sub notifications](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/pub-sub) when you configure the conversation profile.

### REST

To create a conversation profile, call the `create` method on the [`ConversationProfile`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles) resource. 

`noSmallTalk`: If `true`, suggestions will not be triggered after small talk messages (such as "hi", "how are you", and so on). If `false`, suggestions will be triggered after small talk messages.

`onlyEndUser`: If `true`, suggestions will be triggered only after end-user messages. If `false`, suggestions will be triggered after both end-user and human agent messages.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your GCP project ID
  * KNOWLEDGE_BASE_ID: your knowledge base ID



HTTP method and URL: 
    
    
    POST https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/conversationProfiles

Request JSON body: 
    
    
    {
      "name": "projects/PROJECT_ID/conversationProfiles/CONVERSATION_PROFILE_ID",
      "displayName": "my-conversation-profile-display-name",
      "humanAgentAssistantConfig": {
        "notificationConfig": {},
        "humanAgentSuggestionConfig": {
          "featureConfigs": [
            {
              "enableInlineSuggestion": true,
              "SuggestionTriggerSettings": {
                "noSmallTalk": true,
                "onlyEndUser": true,
              },
              "suggestionFeature": {
                "type": "ARTICLE_SUGGESTION"
              },
              "queryConfig": {
                "knowledgeBaseQuerySource": {
                  "knowledgeBases": [
                    "projects/PROJECT_ID/knowledgeBases/KNOWLEDGE_BASE_ID"
                  ]
                }
              }
            }
          ]
        }
      },
      "sttConfig": {},
      "languageCode": "en-US"
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

You have the option of setting security parameters to address issues such as data redaction and data retention. To do this, you must create a [`SecuritySettings`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings) resource, then link it to a conversation profile using the [`securitySettings` field](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles).

Security settings added to a conversation profile affect the behavior of Agent Assist text messages _only_. The behavior of the Dialogflow interaction history is controlled by [Dialogflow's security settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/security-settings), which you can set using the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).

## Handle conversations at runtime

### Create a conversation

When a dialog begins between an end-user and a human or virtual agent, you create a _conversation_. **In order to see suggestions, you must also create both an end-user participant and a human agent participant and add them to the conversation**. The following sections walk you through this process.

First, you must create a conversation:

### REST

To create a conversation, call the `create` method on the [`Conversation`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations) resource. 

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

To create an end-user participant, call the `create` method on the [`Participant`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants) resource.

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

To create a human agent participant, call the `create` method on the [`Participant`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants) resource.

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

To add and analyze a human agent message in the conversation, call the `analyzeContent` method on the [`Participant`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants) resource.

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

In response to the human agent, the end-user says "I want to return my order." This time, the API response contains a suggested document with its associated confidence score. Earlier in this tutorial we added [one knowledge document to the knowledge base](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/article-suggestion#create_a_knowledge_document), and that document was returned. Confidence scores range from 0 to 1; higher values indicate a higher likelihood that the document is relevant to the conversation. A snippet containing the first 100 characters of the document is also returned. The snippet can help a human agent quickly determine whether the document is useful. We recommend that you provide this information to your human agent, who might choose to share the recommended document with the end-user.

**Note:** When you integrate Article Suggestion, be aware that human agents can't click a document and see it unless you implement this capability in your own system.

### REST

To add and analyze an end-user message for the conversation, call the `analyzeContent` method on the [`Participant`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants) resource.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your GCP project ID
  * CONVERSATION_ID: your conversation ID
  * PARTICIPANT_ID: your end-user participant ID



HTTP method and URL: 
    
    
    POST https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/conversations/CONVERSATION_ID/participants/PARTICIPANT_ID:analyzeContent

Request JSON body: 
    
    
    {
      "textInput": {
        "text": "I want to return my order.",
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
        "content": "I want to return my order.",
        "languageCode": "en-US",
        "participant": "PARTICIPANT_ID",
        "participantRole": "END_USER",
        "createTime": "2020-02-13T00:07:35.925Z"
      },
      "humanAgentSuggestionResults": [
        {
          "suggestArticlesResponse": {
            "articleAnswers": [
              {
                "title": "Return an order",
                "uri": "gs://agent-assist-public-examples/public_article_suggestion_example_returns.html",
                "snippets": [
                  "\u003cb\u003eReturn\u003c/b\u003e an \u003cb\u003eorder\u003c/b\u003e. Follow the steps below for Made-up Store \u003cb\u003ereturns\u003c/b\u003e. At this time, \nwe don't offer exchanges. In most cases, you can drop off \u003cb\u003ereturns\u003c/b\u003e at any Made-up\n ..."
                ],
                "metadata": {
                  "title": "Return an order",
                  "snippet": "\n  \n\n\u003ch1\u003eReturn an order\u003c/h1\u003e \nFollow the steps below for Made-up Store returns. At this time, we do...",
                  "document_display_name": "my-kdoc"
                },
                "answerRecord": "projects/PROJECT_ID/answerRecords/ANSWER_RECORD_ID"
              }
            ],
            "latestMessage": "projects/PROJECT_ID/conversations/CONVERSATION_ID/messages/MESSAGE_ID",
            "contextSize": 2
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

To complete the conversation, call the `complete` method on the [`conversations`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations) resource. 

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

The previous sections show how to create a [`ConversationProfile`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#resource:-conversationprofile) in order to receive suggestions. The following sections outline some optional functionalities that you can implement during a conversation.

### Pub/Sub suggestion notifications

In the sections earlier, the [ConversationProfile](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles) was created with only a human agent assistant. During the conversation you needed to call the API to receive suggestions after each message was added to the conversation. If you prefer to receive notification events for suggestions, you can set the `notificationConfig` field when creating the conversation profile. This option uses [Cloud Pub/Sub](https://docs.cloud.google.com/pubsub/docs) to send suggestion notifications to your application as the conversation proceeds and new suggestions are available.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
