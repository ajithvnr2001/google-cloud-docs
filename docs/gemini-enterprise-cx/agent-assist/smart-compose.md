---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/smart-compose/
title: Smart compose \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:42.533658+00:00
---

# Smart compose  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/smart-compose/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Smart compose Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** This feature is no longer supported. For an alternative, use [smart reply](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/smart-reply).

The smart compose feature assists a human agent during a text chat with an end-user. It suggests phrases to complete the sentences started by the human agent. You can use this feature to implement a custom suggestion feature for your agent's chat interface.

![A human agent receives a text suggestion while typing in a chat
interface.](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/images/smart-compose-suggestion.gif) This guide walks you through implementing the Smart Compose feature by calling the API directly. If you prefer, you can use the [Agent Assist Console](https://agentassist.cloud.google.com) to train a model and test its performance using the simulator. See the [Smart Compose simulator tutorial](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/priv/smart-compose) for instructions.

See the [Smart Compose best practices documentation](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/priv/smart-compose-best-practices) for guidelines about integrating Smart Compose with your own system and improving the quality of your suggestions.

**Note:** Be aware that all runtime operations must be carried out by calling the API directly.

## Before you begin

Complete the following before reading this guide:

  1. Enable the [Dialog Flow API](https://docs.cloud.google.com/dialogflow/docs/quick/setup) for your project.



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
      "displayName": "smart_compose_assist",
      "humanAgentAssistantConfig": {
        "humanAgentSuggestionConfig": {
          "featureConfigs": [
            {
              "suggestionFeature": {
                "type": "SMART_COMPOSE"
              },
              "queryConfig": {
                "documentQuerySource": {
                  "documents": "projects/PROJECT_ID/knowledgeBases/KNOWLEDGE_BASE_ID/documents/DOCUMENT_ID"
                },
               "maxResults": "1"
              },
             "conversationModelConfig": {
               "model": "projects/PROJECT_ID/conversationModels/MODEL_ID"
             }
            }
          ]
        }
      }
    }
    

The response contains your new conversation profile ID.

## Handle conversations at runtime

When a dialog begins between an end-user and a human agent, you create a _conversation_. **In order to see suggestions, you must also create both an end-user participant and a human agent participant and add them to the conversation**. The following sections walk you through this process.

### Create a conversation

To create a conversation, call the `create` method on the [`Conversation`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations) resource.

### REST

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

You must add both end-user and human agent participants to the conversation in order to see suggestions. To create an end-user participant, call the `create` method on the [`Participant`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants) resource. Provide your conversation ID and `END_USER` for the `role` field.

### REST

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
    

The path segment after `participants` contains your new end user participant ID. 

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

To create a human agent participant, call the `create` method on the [`Participant`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants) resource. Provide your conversation ID and `HUMAN_AGENT` for the `role` field.

### REST

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

Each time either participant types a message in the conversation, you need to send that message to the API for processing. Agent Assist bases its suggestions on analysis of human agent and end-user messages. To add and analyze a human agent message for the conversation, call the `analyzeContent` method on the [`Participant`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants) resource. Provide the conversation ID and human agent participant ID.

### REST

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
          "suggestSmartRepliesResponse": {
          "smartReplyAnswers": [
              {
                "reply": "I am here to help you.",
                "confidence": 0.5,
                "answerRecord": "projects/PROJECT_ID/answerRecords/ANSWER_RECORD_ID_1"
              },
              {
                "reply": "Sorry for the wait, we have a high volume of chats right now.",
                "confidence": 0.3,
                "answerRecord": "projects/PROJECT_ID/answerRecords/ANSWER_RECORD_ID_2"
              },
              {
                "reply": "Thank you for contacting us!",
                "confidence": 0.1,
                "answerRecord": "projects/PROJECT_ID/answerRecords/ANSWER_RECORD_ID_3"
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
    
    

### Add and analyze a message from the end-user

To add and analyze an end-user message for the conversation, call the `analyzeContent` method on the [`Participant`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants) resource. Provide the conversation ID and end-user participant ID.

The response contains a message ID. Suggestions are acquired in the next step. 

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your GCP project ID
  * CONVERSATION_ID: your conversation ID
  * PARTICIPANT_ID: your end-user participant ID



HTTP method and URL: 
    
    
    POST https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/conversations/CONVERSATION_ID/participants/PARTICIPANT_ID:analyzeContent

Request JSON body: 
    
    
    {
      "textInput": {
        "text": "I want to reserve a room.",
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
        "content": "I want to reserve a room.",
        "languageCode": "en-US",
        "participant": "PARTICIPANT_ID",
        "participantRole": "END_USER",
        "createTime": "2020-02-13T00:07:35.925Z"
      },
      "humanAgentSuggestionResults": [
        {
          "suggestSmartRepliesResponse": {
          "smartReplyAnswers": [
              {
                "reply": "Where would you like to reserve a room?",
                "confidence": 0.5,
                "answerRecord": "projects/PROJECT_ID/answerRecords/ANSWER_RECORD_ID_1"
              },
              {
                "reply": "What type of rooms would you like to reserve?",
                "confidence": 0.3,
                "answerRecord": "projects/PROJECT_ID/answerRecords/ANSWER_RECORD_ID_2"
              },
              {
                "reply": "How long do you want to stay?",
                "confidence": 0.1,
                "answerRecord": "projects/PROJECT_ID/answerRecords/ANSWER_RECORD_ID_3"
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
    
    

### Get a suggestion (Optional)

You can suggestions at any time. You can optionally specify a message ID to receive suggestions based on that message. If this field is not set, suggestions are based on the latest message from either participant by default. To get suggestions, call the `suggestSmartReplies` method on the [`Suggestion`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants.suggestions) resource. Provide the conversation ID, human agent participant ID, and the a message ID from either participant (optional).

The response contains Smart Reply suggestions for the human agent.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your GCP project ID
  * CONVERSATION_ID: your conversation ID
  * PARTICIPANT_ID: your end-user participant ID



HTTP method and URL: 
    
    
    POST https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/conversations/CONVERSATION_ID/participants/PARTICIPANT_ID:analyzeContent

Request JSON body: 
    
    
    {
      "textInput": {
        "text": "I want to reserve a room.",
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
        "content": "I want to reserve a room.",
        "languageCode": "en-US",
        "participant": "PARTICIPANT_ID",
        "participantRole": "END_USER",
        "createTime": "2020-02-13T00:07:35.925Z"
      },
      "humanAgentSuggestionResults": [
        {
          "suggestSmartRepliesResponse": {
          "smartReplyAnswers": [
              {
                "reply": "Where would you like to reserve a room?",
                "confidence": 0.5,
                "answerRecord": "projects/PROJECT_ID/answerRecords/ANSWER_RECORD_ID_1"
              },
              {
                "reply": "What type of rooms would you like to reserve?",
                "confidence": 0.3,
                "answerRecord": "projects/PROJECT_ID/answerRecords/ANSWER_RECORD_ID_2"
              },
              {
                "reply": "How long do you want to stay?",
                "confidence": 0.1,
                "answerRecord": "projects/PROJECT_ID/answerRecords/ANSWER_RECORD_ID_3"
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
    
    

### Complete the conversation

To complete the conversation, call the `complete` method on the [`conversations`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations) resource. Provide the conversation ID.

### REST

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
