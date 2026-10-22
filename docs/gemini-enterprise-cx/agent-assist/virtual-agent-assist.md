---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/virtual-agent-assist/
title: Virtual Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:45.277961+00:00
---

# Virtual Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/virtual-agent-assist/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Virtual Agent Assist Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** This feature has limited access. Contact your Google Cloud representative to access private GA features.

This how-to guide walks you through the process of enabling the **Virtual Agent Assist** feature by calling the API directly. The Virtual Agent Assist assistant follows the conversation and uses a [Dialog Flow virtual agent](https://docs.cloud.google.com/dialogflow/docs/agents-overview) to provide workflow support to human agents and detect intents for data analysis.

If you prefer, you can use the [Agent Assist console](https://agentassist.cloud.google.com) to train a model and test its performance using the simulator. See the [Virtual Agent Assist console tutorial](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/priv/virtual-agent-console) for instructions.

**Note:** Be aware that all runtime operations must be carried out by calling the API directly.

## Before you begin

Before you can enable Virtual Agent Assist you must have already implemented one or more Agent Assist features to use with the virtual agent. Smart Reply, FAQ Assist, Article Suggestion, and Smart Compose can be used alone with Virtual Agent Assist or in any combination. The following links take you to the relevant documentation for implementation details.

  * [Smart Reply](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/smart-reply)
  * [FAQ Assist](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/faq)
  * [Article Suggestion](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/article-suggestion)
  * [Smart Compose](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/smart-compose)



## Create a conversation

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
    
    

## Create an end-user participant

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
    
    

## Create a human agent participant

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
    
    

## Add a message from the end-user and get suggestions

To add and analyze an end-user message for the conversation, call the [`analyzeContent`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversations.participants/analyzeContent) method on the [`Participant`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversations.participants.suggestions) resource. The response includes a `dialogflowAssistAnswers` field containing the following data:

  * `fulfillmentText`: Contains a suggested response. You can configure your system to present this suggestion to the human agent.
  * `answer record`: A unique ID for the suggestion.



## Select the suggestion

When a human agent receives a suggestion, they can accept it as-is or edit it before passing it on to the end-user. To select a suggestion, call [`analyzeContent`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversations.participants/analyzeContent) again using the human agent participant. Set the `suggestionInput` field to your selected settings and provide the `answer record` you received earlier. The `text override` field should contain the actual text sent to the end-user. The following is an example of configuring the `suggestionInput` field:
    
    
    {
      "answerRecord": "answer-record",
      "textOverride": {
        "text" : "Yes, there will be ponies.",
        "languageCode": "en-US"
      }
    }
    

## Complete the conversation

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
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
