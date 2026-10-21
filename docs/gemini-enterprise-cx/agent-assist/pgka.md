---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/pgka/
title: Proactive generative knowledge assist \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:44:16.207158+00:00
---

# Proactive generative knowledge assist  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/pgka/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Proactive generative knowledge assist Stay organized with collections  Save and categorize content based on your preferences. 

Proactive generative knowledge assist follows an ongoing conversation and proactively provides search query suggestions and answers. Proactive generative knowledge assist supports search context, multiple suggested queries, and you can customize initiating events.

## Search context

Proactive generative knowledge assist generates a search query and context. It extracts information from the conversation as key-value pairs to improve the search context and provide better answers to the search query. 

You can also disable the search context. In some scenarios, you can opt out of using search context and only use the query itself. Control this with the `disable_query_search_context` field. When this field is set to `true`, Proactive generative knowledge assist generates the search context but doesn't add it to the search query, which is sent to the knowledge base.

## Multiple suggested queries

Proactive generative knowledge assist can generate multiple relevant queries for different topics discussed in a conversation. It uses the primary query for automatic knowledge search and provides additional queries in the response for the agent to use if needed.

## Customize event initiation

By default, a `CUSTOMER_MESSAGE` initiates suggestions from Proactive generative knowledge assist. To define which event initiates a new Proactive generative knowledge assist suggestion, choose one of the following value options for the `suggestion_trigger_event` field.

  * `CUSTOMER_MESSAGE`: Keep the default message received from the end user.
  * `AGENT_MESSAGE`: A message is sent by the human agent.
  * `END_OF_UTTERANCE`: Proactive generative knowledge assist detects the end of a user utterance.



## Implement Proactive generative knowledge assist

Follow these steps to start using Proactive generative knowledge assist.

### Step 1: Create a conversation profile

[Create a conversation profile](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-profile) using the [Agent Assist console](https://agentassist.cloud.google.com/) or the API. We recommend that you create a conversation profile using the Agent Assist console.

### Console

  1. Enable the **Generative knowledge assist** suggestion type and link it to the flow-based data store agent or playbook-based data store agent from the previous step. This enables the flow-based data store agent or playbook-based data store agent to proactively provide query and answer suggestions and answer manual search queries from your human agents.
  2. Optional: Use the **Show all suggested queries for conversation** checkbox to have the flow-based data store agent or playbook-based data store agent show all these queries, even when there is not an answer found from your knowledge documents. This is intended for testing which queries can be pulled from the ongoing conversation.
  3. Optional: Use the **Load proactive answers asynchronously** checkbox to only get query suggestions. You can manually submit the suggested query to the [SearchKnowledge](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.suggestions/searchKnowledge) API and automatically submit in the Agent Assist console simulator and UI modules.![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/images/gka-conversation-profile.png)



### API

The following steps create a [ConversationProfile](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversationProfiles) with a [HumanAgentAssistantConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversationProfiles#ConversationProfile.HumanAgentAssistantConfig) object. You can also perform these actions using the [Agent Assist console](https://agentassist.cloud.google.com/).

To create a conversation profile, call the create method on the [ConversationProfile](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversationProfiles) resource and update the `baseline_model_version`.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your project ID
  * LOCATION_ID: the ID for your location
  * AGENT_ID: your flow-based data store agent or playbook-based data store agent ID from the previous step

The following is a JSON example of a conversation profile configuration with baseline model 2.0: 
    
    
     {
      "name": "projects/PROJECT_ID/locations/LOCATION/conversationProfiles/PROFILE_ID",
      "human_agent_assistant_config": {
        "human_agent_suggestion_config": {
          "feature_configs": [
            {
              "suggestion_feature": {
                "type": "KNOWLEDGE_ASSIST"
              },
              "query_config": {
                "dialogflow_query_source": {
                  "agent": "projects/PROJECT_ID/locations/LOCATION/agents/AGENT_ID"
                }
              },
              "conversation_model_config": {
                "baseline_model_version": "2.0"
              }
            "disable_query_search_context": false,
        "enableQuerySuggestionWhenNoAnswer": false,
        "suggestion_trigger_event": "END_OF_UTTERANCE",
            }
          ]
        }
      }
    }
         

### Step 2: Handle conversations at runtime

Proactive generative knowledge assist processes conversations at runtime to proactively provide search query suggestions based on the current conversation context and the answer.

#### Create a conversation

First, you must create a [conversation](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/basics#conversations):

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

For more information, see the [Agent Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    

#### Create a user-participant

Add user- and agent-[participants](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/basics#participants) to the conversation to see suggestions. First, add the user-participant to the conversation:

### REST

To create a user-participant, call the `create` method on the [`Participant`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants) resource.

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
    

The path segment after `participants` contains your new user-participant ID. 

### Python

For more information, see the [Agent Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    

#### Create an agent-participant

Add an agent-participant to the conversation:

### REST

To create an agent-participant, call the `create` method on the [`Participant`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants) resource.

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
    

The path segment after `participants` contains your new human agent-participant ID. 

### Python

For more information, see the [Agent Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    

#### Add and analyze a message from the agent

Each time either participant types a message in the conversation, you need to send that message to the API for processing. The data store agent bases its suggestions on analysis of human agent and user messages. In the following example, the human agent starts the conversation by asking "How may I help you?"

No suggestions are returned yet in the response.

### REST

To add and analyze a human agent message in the conversation, call the `analyzeContent` method on the [`Participant`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants) resource.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your project ID
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
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/conversations/CONVERSATION_ID/participants/PARTICIPANT_ID:analyzeContent"

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
      }
    }
    

### Python

For more information, see the [Agent Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    

#### Add a message from the user for suggestions

In response to the agent, the user asks, "When can I get my return refund?" This time, the API response contains a suggested query and the generative AI answer based on the knowledge documents.

### REST

To add and analyze a user message for the conversation, call the `analyzeContent` method on the [`Participant`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants) resource.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your project ID
  * CONVERSATION_ID: your conversation ID
  * PARTICIPANT_ID: your end-user participant ID



HTTP method and URL: 
    
    
    POST https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/conversations/CONVERSATION_ID/participants/PARTICIPANT_ID:analyzeContent

Request JSON body: 
    
    
    {
      "textInput": {
        "text": "When can I get my return refund?",
        "languageCode": "en-US"
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/conversations/CONVERSATION_ID/participants/PARTICIPANT_ID:analyzeContent"

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
        -Uri "https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/conversations/CONVERSATION_ID/participants/PARTICIPANT_ID:analyzeContent" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "message": {
        "name": "projects/PROJECT_ID/conversations/CONVERSATION_ID/messages/MESSAGE_ID",
        "content": "When can I get my return refund?",
        "languageCode": "en-US",
        "participant": "PARTICIPANT_ID",
        "participantRole": "END_USER",
        "createTime": "2020-02-13T00:07:35.925Z"
      },
      "humanAgentSuggestionResults": [
        {
          "suggestKnowledgeAssistResponse": {
            "knowledgeAssistAnswer": {
              "suggestedQuery": {
                "queryText": "Refund processing time"
              },
              "suggestedQueryAnswer": {
                "answerText": "After your return is processed, you receive your refund in 7 days. The refund amount should be for the full value of the items returned, but doesn't include shipping & service fees.",
                "generativeSource": {
                  "snippets": [
                    {
                      "title": "Returns & refunds - Help",
                      "uri": "https://example.com/",
                      "text": "When the package with your return arrives at the seller's return center, it may take up to 7 additional business days to process. Check the status of your refund with the return tracking number found on your orders page."
                    }
                  ]
                },
              },
              "answerRecord": "projects/PROJECT_ID/answerRecords/ANSWER_RECORD_ID"
            },
          }
        }
      ]
    }
    

### Python

For more information, see the [Agent Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    

#### Complete the conversation

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

For more information, see the [Agent Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    

#### Simulator

You can test your flow-based data store agent or playbook-based data store agent in the [Agent Assist simulator](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/simulator).

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/images/generative-knowledge-assist-proactive-simulator.png)

In the preceding example, the flow-based data store agent provides the following suggestions:

  * **Suggested query** : _Refund processing time_.
  * **Generative AI generated answer** : _After your return is processed, you receive your refund in 7 days. The refund amount should be for the full value of the items returned, but doesn't include shipping & service fees._
  * **Title of the relevant knowledge document** : _Returns & refunds - Help_.



### Step 3: Pub/Sub suggestion notifications

You can set the `notificationConfig` field when creating a conversation profile to receive notifications for suggestions. This option uses [Pub/Sub](https://docs.cloud.google.com/pubsub/docs) to send suggestion notifications to your application as the conversation proceeds and new suggestions become available.

If you're integrating through the [`AnalyzeContent`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants/analyzeContent) API, you have the option to enable the `disable_high_latency_features_sync_delivery` config in [`ConversationProfile`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles) to ensure that the `AnalyzeContent` API will respond, without waiting for the Proactive generative knowledge assist suggestions, and deliver the suggestions through Pub/Sub.

You can also enable this configuration from the Agent Assist console.

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/images/pubsub-disablesynchdelivery.png)

### Access data through Customer Experience Insights

Alternatively, your Proactive generative knowledge assist generated queries and answers are automatically populated to Customer Experience Insights. To access this data there, follow the instructions at [Enable Dialogflow runtime integration](https://docs.cloud.google.com/contact-center/insights/docs/enable-dialogflow-runtime-integration).

## Send feedback

For the steps to send feedback, go to [Send feedback to Agent Assist](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/feedback#generative_knowledge_assist).

### Answer agent questions

The following is an example JSON request for sending feedback about answering agent questions.
    
    
    {
     "name": "projects/PROJECT_ID/locations/LOCATION_ID/answerRecords/ANSWER_RECORD_ID",
     "answerFeedback": {
       "displayed": true
       "clicked": true
       "correctnessLevel": "FULLY_CORRECT"
       "agentAssistantDetailFeedback": {
         "knowledgeSearchFeedback": {
           "answerCopied": true
           "clickedUris": [
             "url_1",
             "url_2",
             "url_3",
           ]
         }
       }
     }
    }

### Proactively suggest Q&A

The following is an example JSON request for sending feedback about proactive suggestions.
    
    
    {
     "name": "projects/PROJECT_ID/locations/LOCATION_ID/answerRecords/ANSWER_RECORD_ID",
     "answerFeedback": {
       "displayed": true
       "clicked": true
       "correctnessLevel": "FULLY_CORRECT"
       "agentAssistantDetailFeedback": {
         "knowledgeAssistFeedback": {
           "answerCopied": true
           "clickedUris": [
             "url_1",
             "url_2",
             "url_3",
           ]
         }
       }
     }
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
