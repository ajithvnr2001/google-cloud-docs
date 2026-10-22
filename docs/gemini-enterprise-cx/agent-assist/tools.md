---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/tools/
title: OpenAPI and Integration Connectors tools \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:55.642244+00:00
---

# OpenAPI and Integration Connectors tools  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/tools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  OpenAPI and Integration Connectors tools Stay organized with collections  Save and categorize content based on your preferences. 

You can use Agent Assist features along with external APIs and data sources. Google Cloud provides OpenAPI and Integration Connectors tools to facilitate your Agent Assist integrations.

## OpenAPI tools

[OpenAPI](https://www.openapis.org/) tools enable the connection between Agent Assist features and external APIs. This connection allows Agent Assist features to read and write information from multiple sources. To create an OpenAPI tool, you must provide an OpenAPI schema that describes the external APIs you want to connect with.

## Integration Connectors tool

Use [Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs/overview) to connect Google Cloud to a variety of data sources. Connector tools allow Agent Assist features to use Integration Connectors to read and write those data sources.

## Before you begin

To set up the environment to create OpenAPI and Integration Connectors tools, enter your project ID and region, then run the following code.
    
    
    CLOUDSDK_CORE_PROJECT=YOUR_PROJECT_ID
    REGION=YOUR_REGION
    API_VERSION=v2beta1
    API_ENDPOINT=https://${REGION}-dialogflow.googleapis.com/${API_VERSION}
    
    function gcurl () {
            curl -H "Authorization: Bearer "$(gcloud auth print-access-token) -H "X-Goog-User-Project: ${CLOUDSDK_CORE_PROJECT}" -H "Content-Type: application/json; charset=utf-8" "$@"
    }

## Create an OpenAPI tool

To use an OpenAPI tool, you must first request its creation and save the tool resource name.

### Step 1: Request to create tool

Follow these steps to request to create an OpenAPI tool.

  1. Customize the code as follows: 
     1. Within a single project, use a `tool_key` value that's unique among all your tools.
     2. Enter your own OpenAPI schema in the `open_api_spec.text_schema` field.
  2. Run the following customized code. 
         
         $ cat > create-tool-request.json << _EOF_
         {
           "tool_key": "UNIQUE_KEY",
           "description": "TOOL_DESCRIPTION",
           "display_name": "TOOL_DISPLAY_NAME",
           "open_api_spec": {
             "text_schema": "Your-Schema"
           }
         }
         _EOF_
         
         
         
         $ gcurl -X POST ${API_ENDPOINT}/projects/${CLOUDSDK_CORE_PROJECT}/locations/${REGION}/tools -d @create-tool-request.json | tee create-tool-response.json
         




If successful, the API returns the newly created tool, which contains the resource name, as shown in the following example.
    
    
    {
      "name": "projects/Your-Project-ID/locations/Your-Region/tools/Tool-ID",
      "toolKey": "UNIQUE_KEY",
      "description": "TOOL_DESCRIPTION",
      "createTime": "2025-06-02T18:11:38.999174724Z",
      "updateTime": "2025-06-02T18:11:38.999174724Z",
      "displayName": "TOOL_DISPLAY_NAME",
      "openApiSpec": {
        "textSchema": "Your-Schema"
      }
    }
    

### Step 2: Save the tool resource name

Save the tool resource name in an environment variable for later use. The following is an example template for the tool resource environment variable.
    
    
    TOOL_RESOURCE=$(cat create-tool-response.json | jq .name | tr -d '"')
    

## AI coach with an OpenAPI tool

You can use an OpenAPI tool with the [AI coach](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/tools_data_store) feature to access extra information from outside of Google Cloud. That external information can then be used to generate suggestions that help contact center agents.

### Step 1: Create a generator

The following example creates a generator with the tool resource environment variable.
    
    
    $ cat > create-generator-request.json << _EOF_
    {"agent_coaching_context":{"instructions":[{"agent_action":"help customer by using the tool to find information from library of congress","condition":"The customer asks about library of congress","description":"agent coaching test","display_name":"Search for information"}],"overarching_guidance":"Help customer with questions"},"description":"prober-generate-suggestions-with-agent-coaching-generator","inference_parameter":{"max_output_tokens":256,"temperature":0},"tools":["${TOOL_RESOURCE}"],"trigger_event":"CUSTOMER_MESSAGE"}
    _EOF_
    
    $ gcurl -X POST ${API_ENDPOINT}/projects/${CLOUDSDK_CORE_PROJECT}/locations/${REGION}/generators -d @create-generator-request.json | tee create-generator-response.json
    
    _EOF_
    
    $ gcurl -X POST ${API_ENDPOINT}/projects/${CLOUDSDK_CORE_PROJECT}/locations/${REGION}/generators -d @create-generator-request.json | tee create-generator-response.json
    

You should receive a response that looks like the following example of an AI coach generator.
    
    
    {
      "name": "projects/Your-Project-ID/locations/Your-Region/generators/Generator-ID",
      "description": "example-generator",
      "inferenceParameter": {
        "maxOutputTokens": 256,
        "temperature": 0
      },
      "triggerEvent": "CUSTOMER_MESSAGE",
      "createTime": "2025-06-02T18:30:51.021461728Z",
      "updateTime": "2025-06-02T18:30:51.021461728Z",
      "agentCoachingContext": {
        "instructions": [
          {
            "displayName": "Search for information",
            "condition": "The customer asks about library of congress",
            "agentAction": "help customer by using the tool to find information from library of congress"
          }
        ],
        "version": "1.5",
        "overarchingGuidance": "Help customer with questions"
      },
      "tools": [
        "projects/Your-Project-ID/locations/Your-Region/tools/Tool-ID"
      ]
    }
    

#### Save the generator resource name

Save it as an environment variable for later use, as in the following example.
    
    
    GENERATOR_RESOURCE=$(cat create-generator-response.json | jq .name | tr -d '"')

### Step 2: Create a conversation profile

Run the following code to create a conversation profile.
    
    
    $ cat > create-conversation-profile-request.json << _EOF_
    {"displayName":"prober-generate-suggestions-with-agent-coaching-generator","humanAgentAssistantConfig":{"humanAgentSuggestionConfig":{"generators":["${GENERATOR_RESOURCE}"]}}}
    _EOF_
    
    $ gcurl -X POST ${API_ENDPOINT}/projects/${CLOUDSDK_CORE_PROJECT}/locations/${REGION}/conversationProfiles -d @create-conversation-profile-request.json | tee create-conversation-profile-response.json
    

You should receive a response like the following.
    
    
    {
      "name": "projects/Your-Project-ID/locations/Your-Region/conversationProfiles/Conversation-Profile-ID",
      "displayName": "prober-generate-suggestions-with-agent-coaching-generator",
      "humanAgentAssistantConfig": {
        "humanAgentSuggestionConfig": {
          "generators": [
            "projects/Your-Project-ID/locations/Your-Region/generators/Generator-ID"
          ]
        }
      },
      "languageCode": "en-US",
      "createTime": "2025-06-02T18:40:39.940318Z",
      "updateTime": "2025-06-02T18:40:39.940318Z",
      "projectNumber": "${project_number}"
    }

#### Save the conversation profile resource name

Save this name as an environment variable, like the following example.
    
    
    CONVERSATION_PROFILE_RESOURCE=$(cat create-conversation-profile-response.json | jq .name | tr -d '"')
    

### Step 3: Create a conversation

Run the following code to create a conversation.
    
    
    $ cat > create-conversation-request.json << _EOF_
    {"conversationProfile":"${CONVERSATION_PROFILE_RESOURCE}"}
    _EOF_
    
    $ gcurl -X POST ${API_ENDPOINT}/projects/${CLOUDSDK_CORE_PROJECT}/locations/${REGION}/conversations -d @create-conversation-request.json | tee create-conversation-response.json
    

You should receive a response like the following.
    
    
    {
      "name": "projects/Your-Project-ID/locations/Your-Region/conversations/Conversation-ID",
      "lifecycleState": "IN_PROGRESS",
      "conversationProfile": "projects/Your-Project-ID/locations/Your-Region/conversationProfiles/Conversation-Profile-ID",
      "startTime": "2025-06-02T18:43:40.818123Z",
      "conversationStage": "HUMAN_ASSIST_STAGE",
      "source": "ONE_PLATFORM_API",
      "initialConversationProfile": {
        "name": "projects/Your-Project-ID/locations/Your-Region/conversationProfiles/Conversation-Profile-ID",
        "displayName": "prober-generate-suggestions-with-agent-coaching-generator",
        "humanAgentAssistantConfig": {
          "humanAgentSuggestionConfig": {
            "generators": [
              "projects/Your-Project-ID/locations/Your-Region/generators/Generator-ID"
            ]
          }
        },
        "languageCode": "en-US"
      },
      "projectNumber": "${project_number}",
      "initialGeneratorContexts": {
        "projects/Your-Project-ID/locations/Your-Region/generators/Generator-ID": {
          "generatorType": "AGENT_COACHING",
          "generatorVersion": "1.5"
        }
      }
    }
    

#### Save conversation resource name

Save this name as an environment variable for later use. Your variable should have the following format.
    
    
    CONVERSATION_RESOURCE=$(cat create-conversation-response.json | jq .name | tr -d '"') 

### Step 4: Create an end user

Run the following code to create an end user.
    
    
    $ cat > create-end-user-request.json << _EOF_
    {"role":"END_USER"}
    _EOF_
    
    $ gcurl -X POST ${API_ENDPOINT}/${CONVERSATION_RESOURCE}/participants -d @create-end-user-request.json | tee create-end-user-response.json
    

You should receive a response like the following.
    
    
    {
      "name": "projects/Your-Project-ID/locations/Your-Region/conversations/Conversation-ID/participants/End-User-Participant-ID",
      "role": "END_USER"
    }

#### Save end user resource name

Save the end user resource name as an environment variable like the following. 
    
    
    END_USER_RESOURCE=$(cat create-end-user-response.json | jq .name | tr -d '"')

### Step 5: Create a human agent

Run the following code to create a human agent.
    
    
    $ cat > create-human-agent-request.json << _EOF_
    {"role":"HUMAN_AGENT"}
    _EOF_
    
    $ gcurl -X POST ${API_ENDPOINT}/${CONVERSATION_RESOURCE}/participants -d @create-human-agent-request.json | tee create-human-agent-response.json
    

You should receive a response like the following.
    
    
    {
      "name": "projects/Your-Project-ID/locations/Your-Region/conversations/Conversation-IDHuman-Agent-Participant-ID",
      "role": "HUMAN_AGENT"
    }
    

#### Save the human agent resource name

Save the human agent resource name as an environment variable like the following.
    
    
    HUMAN_AGENT_RESOURCE=$(cat create-human-agent-response.json | jq .name | tr -d '"')

### Step 6: Send text to AI coach

Run the following code to send text to the AI coach with the `AnalyzeContent` method.
    
    
    cat > analyze-content-1-request.json << _EOF_
    {"text_input":{"languageCode":"en-US","text":"Can you search library of congress for the latest trends"}}
    _EOF_
    
    gcurl -X POST "${API_ENDPOINT}/${END_USER_RESOURCE}:analyzeContent" -d @analyze-content-1-request.json | tee analyze-content-1-response.json
    

### Step 7: Verify the tool call

Run the following code to verify the tool call.
    
    
    cat analyze-content-1-response.json| jq ".humanAgentSuggestionResults[0].generateSuggestionsResponse.generatorSuggestionAnswers[0].generatorSuggestion.toolCallInfo"
    

You should receive a response like the following.
    
    
    [
      {
        "toolCall": {
          "tool": "projects/Your-Project-ID/locations/Your-Region/tools/Tool-ID",
          "action": "search",
          "inputParameters": {
            "q": "latest trends",
            "fo": "json",
            "tool_description": "A generic search endpoint that might be available across various LoC APIs. The structure of the results will vary.\n",
            "at": "trending_content"
          },
          "createTime": "2025-06-02T18:56:53.882479179Z"
        },
        "toolCallResult": {
          "tool": "projects/Your-Project-ID/locations/Your-Region/tools/MjM0NTU3NDk2MTM5NTAwNzQ4OQ",
          "action": "search",
          "content": ""}]}",
          "createTime": "2025-06-02T18:56:54.289367086Z"
        }
      }
    ]

### Step 8: (Optional) Delete resources

To delete resources that you created in previous steps, run the following code.

### Conversation profile
    
    
    gcurl -X DELETE ${API_ENDPOINT}/${CONVERSATION_PROFILE_RESOURCE}
    

### Generator
    
    
    gcurl -X DELETE ${API_ENDPOINT}/${GENERATOR_RESOURCE}
    

### OpenAPI tool
    
    
    gcurl -X DELETE ${API_ENDPOINT}/${TOOL_RESOURCE}
    

## Create an Integration Connectors tool

You can set up [Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs/setup-integration-connectors) using the Google Cloud console. Follow these steps to create an Agent Assist Integration Connectors tool based on a BigQuery connector.

### Step 1: Create a BigQuery connector tool

Before you create an Integration Connectors tool, go to the [Google Cloud console](https://console.cloud.google.com/) and create a [BigQuery Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs/connectors/bigquery/configure).

### Step 2: Request to create Integration Connectors tool

Run the following code to request to create a tool. For the `connector_spec.name` field, use the resource name of your BigQuery connector.
    
    
    cat > create-connector-tool-request.json << _EOF_
    {
      "tool_key": "order_tool",
      "description": "order bigquery connector tool",
      "display_name": "order bigquery connector tool",
      "connector_spec": {
        "name": "projects/Your-Project-ID/locations/Your-Region/connections/Your-Connector-ID",
        "actions": [
                                 {
                                   "entityOperation": {
                                     "entityId": "Orders",
                                     "operation": "LIST"
                                   }
                                 }, {
                                   "entityOperation": {
                                     "entityId": "Orders",
                                     "operation": "GET"
                                   }
                                 }
                               ]
      }
    }
    _EOF_
    
    
    gcurl -X POST ${API_ENDPOINT}/projects/${CLOUDSDK_CORE_PROJECT}/locations/${REGION}/tools -d @create-connector-tool-request.json | tee create-connector-tool-response.json
    

You should receive a response that looks like the following.
    
    
    {
      "name": "projects/Your-Project-ID/locations/Your-Region/tools/Tool-ID",
      "toolKey": "order_tool",
      "description": "order bigquery connector tool",
      "createTime": "2025-06-03T19:29:55.896178942Z",
      "updateTime": "2025-06-03T19:29:55.896178942Z",
      "connectorSpec": {
        "name": "projects/Your-Project-ID/locations/Your-Region/connections/order-bigquery-connector",
        "actions": [
          {
            "entityOperation": {
              "entityId": "Orders",
              "operation": "LIST"
            }
          },
          {
            "entityOperation": {
              "entityId": "Orders",
              "operation": "GET"
            }
          }
        ]
      },
      "displayName": "order bigquery connector tool"
    }
    

## What's next

For a complete list of the Integration Connectors tools that Agent Assist supports, see the [Dialogflow Connector tools](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/tool#connector) list.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
