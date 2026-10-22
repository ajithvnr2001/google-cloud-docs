---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/build-your-own-genai-assist/
title: Build your own GenAI assist \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:01.325849+00:00
---

# Build your own GenAI assist  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/build-your-own-genai-assist/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Build your own GenAI assist Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Build your own GenAI assist lets you create a text generator and integrate it with Agent Assist. The text generator uses advanced large language models (LLMs), such as Text Bison and Gemini, to generate suggestions. You can use these suggestions to help the participants on either end of a customer service conversation, such as the human agents and the human users. The generator can use built-in LLM calls from Agent Assist that can be configured for most LLM tasks. To understand more about generators in Agent Assist, see [Vertex AI documentation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/overview).

## Generator inputs

The text generator requires the following inputs:

  * **Instruction** : A text to describe the task you want the text generator to perform. In Vertex AI the instruction is called a [prompt](https://docs.cloud.google.com/vertex-ai/docs/generative-ai/learn/introduction-prompt-design).

  * **Model Options** : The model choice and settings needed for optimal model performance, such as temperature, output token limit, TopK, and TopP. The generator outputs are limited by these settings. You can choose a model and set the model options when you create a generator by clicking **Model Options** , or you can use the default settings. In Vertex AI, the model options are called [parameter values](https://docs.cloud.google.com/vertex-ai/docs/generative-ai/model-reference/text).

  * **Trigger Event** : One of the following events that indicates when to initiate the generator:

    * `END_OF_UTTERANCE`: Triggers the generator after each utterance is input.
    * `MANUAL_CALL`: Triggers the generator only when you explicitly make API calls to invoke it.
    * `CUSTOMER_MESSAGE`: Triggers the generator only after each customer message.
    * `AGENT_MESSAGE`: Triggers the generator only after each agent message.



## Generator outputs

After you provide the inputs to the text generator, the Build your own GenAI assist generator provides suggestions such as article links, appropriate responses, or backend information about promotional offers. These suggestions are provided in a text format and are relevant within the context of the customer service conversation at the time they are generated.

## Use cases

This section presents three use cases as examples of how Build your own GenAI assist generators can be implemented. Your model may generate different output responses from the following examples.

### Professional rewrite

You can instruct the generator to rephrase human-agent utterances in a professional, polite, and empathetic manner before responding to customers, as follows.

  * Generator name: Professional rewrite
  * Trigger event: Agent message
  * Instruction:
        
        # TASK DESCRIPTION:
        Output the agent's response under ## LAST UTTERANCE rewritten in a professional, polite and empathetic way in EXAMPLE 4.
        - DO NOT miss any information mentioned by the original text.
        - Only output rewritten response.
        - You're provided with EXAMPLE 1-3. Follow the format.
        
        # EXAMPLE 1
        ## CONVERSATION:
        AGENT: Yo what's up it's Akshay. This is Amazon customer service. What do you want?
        
        ## LAST UTTERANCE:
        Yo what's up it's Akshay. This is Amazon customer service. What do you want?
        
        ## OUTPUT:
        Hi I'm Akshay. Thank you for choosing Amazon customer service. How can I assist you today?
        
        # EXAMPLE 2
        ## CONVERSATION:
        CUSTOMER: Hi, I'm having some trouble with my Apple Music subscription.
        AGENT: Hey, I'm [name]. I can help, I guess. What's your name and account number?
        CUSTOMER: Sure, my name is [name] and my account number is [number].
        AGENT: Alright. Checked that out. You are on Apple Music Individual plan, right?
        
        ## LAST UTTERANCE:
        Alright. Checked that out. You are on Apple Music Individual plan, right?
        
        ## OUTPUT:
        Thank you. I see that you're currently subscribed to the Apple Music Individual plan. Is that correct?
        
        # EXAMPLE 3
        ## CONVERSATION:
        AGENT: What is your order number?
        CUSTOMER: 12345
        AGENT: Hang on a sec. Looking.
        CUSTOMER: I'll wait.
        AGENT: Alright, it appears your order is not registered. Did you even submit the order?
        CUSTOMER: Let me double check. Shoot, someone canceled it. Must be the kids.
        AGENT: Yeah, watch your kids will you?
        CUSTOMER: I'm so sorry.
        AGENT: All good. Have a good one.
        
        ## LAST UTTERANCE:
        All good. Have a good one.
        
        ## OUTPUT:
        No problem. I'm glad I can help. Please have a good day!
        
        # EXAMPLE 4
        ## CONVERSATION:
        ${parameter:transcript}
        
        ## LAST UTTERANCE:
        ${parameter:transcript_last_utterance}
        
        ## OUTPUT:
        




### Customer retention

You can also instruct the generator to suggest agent responses for customer retention, such as providing product discounts, upselling or cross-selling products, and solving issues, as in the following example. The generator accesses information that you provide about discounts and offers as context references with the [`IngestContextReferences` API](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/build-your-own-genai-assist#parameters).

  * Generator name: Customer churn and retention
  * Trigger event: Customer message
  * Context references: offers 
    * One: 11% Discount
    * Nest: 5% Discount
    * New customer discount: 10%
  * Instruction:
        
        # TASK DESCRIPTION:
        You are an Agent who is helping a customer resolve an issue with complete understanding of the same.
        - Make sure you wait to understand the concern or query before making any suggestions.
        - If the customer informs about the issue, you need to ask the exact reason. If the reason is valid, you can give appropriate credit from the OFFERS section.
        - If the customer is about to cancel an order or subscription, make sure you offer something from the OFFERS section and try to retain the customer.
        - If a customer is inquiring about a new product, offer some combo for upselling another product.
        Below are two examples for detecting churn and generating suggestions for mitigation.
        The output should be a single message suggested to the agent according to the context of the conversation.
        
        # EXAMPLE 1
        Customer: Hello
        Agent: Welcome to Google. How may I help you?
        Customer: I want to cancel order.
        Agent: Sure Let me have an order ID.
        Customer: Its 123321
        Agent: I could see that you placed an order for Google Nest. May I know the reason for cancellation?
        Customer: It's available at cheaper rate now. 
        Agent: Ohh.! I see. Let me check the current price and adjust the order price. Is it okay ?
        Customer: Sure..! I can purchase the product  as long as I can get it at the discounted price. I'd definitely go with it
        Agent: Google Nest costs $200 at present. I can see that you paid $230.
        Customer: Yeah. Can you request to refund $30. I can buy it at $200.
        Agent : Sure. I have updated. You will get $30 refund once your order is delivered.
        Customer: Thanks.
        Agent : Welcome
        
        # EXAMPLE 2
        Customer: Hello
        Agent: Welcome to Google. How may I help you?
        Customer: I am having Google One Subscription. I think I may need some more space in future. 
        Agent: Okay. May I have your customer Id:
        Customer: Its 123321
        Agent: I could see that you have 100GB Plan at present. How much are you expecting to need in future?
        Customer: I think I may need 100GB or more.
        Agent: I could check that you are a loyal customer who had subscriptions since last 6 months. I can provide you 10% discount. 
        Customer: Sure..! That would be great. 
        Agent: 200GB Subscription costs $180 per annum which I can offer you at $162.
        Customer: That's cool. Thank you.
        Agent: Is there anything else I can help you with?
        Customer: No thanks.
        
        ## CONTEXT
        ${parameter:transcript}
        
        ## OFFERS
        ${parameter:offers}
        




## Create a generator

The following samples show how to create a Build your own GenAI assist text generator.

### Console

To create a generator using the [Agent Assist console](https://agentassist.cloud.google.com), do the following:

  1. In the console, go to the **Build-your-own-assist** page.

[Go to Build-your-own-assist](https://agentassist.cloud.google.com/)

  2. Click **Create**.

  3. Enter the generator's name.

  4. Select the trigger event from the list.

  5. Enter the instruction to define the task.

  6. Click **Model Options** and select a model from the list.

  7. Set your parameters or use the default settings.

  8. Click **Save** , then click **Save** again to save the generator.




### REST

To create a generator using the API, do the following:

  1. Call the `CreateGenerator` method from the [Generator](https://docs.cloud.google.com/dialogflow/es/docs/reference/rpc/google.cloud.dialogflow.v2beta1#generators) resource.
  2. Enter the generator's name in the `description` field.
  3. Enter the trigger event.
  4. Enter the instruction to define the task in [FreeFormContext.text](https://docs.cloud.google.com/dialogflow/es/docs/reference/rpc/google.cloud.dialogflow.v2beta1#freeformcontext).
  5. Enter a model name in the `published_model` field, or leave it empty to use the default model.
  6. Specify the model parameters in the `inference_parameter` field, or leave them empty to use the default values.



### Parameters

You can make an instruction contextual by marking words as parameters using the format `${parameter:<parameter_name>}`. You can also use the Data Ingestion API to import the actual value of a parameter by calling the [IngestContextReferences](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.locations.conversations/ingestContextReferences) method in a conversation. With this method, the parameters in the instruction will be replaced by their value during runtime.

The following is a JSON example of how to import the value of parameters by calling [IngestContextReferences](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.locations.conversations/ingestContextReferences):
    
    
    {
      "contextReferences": {
        "glossary": {
          "contextContents": [
            {
              "content": "east one",
              "contentFormat": "PLAIN_TEXT"
            }
          ]
        }
      }
    }

There are also some generator parameters that don't need to be ingested. These built-in parameters are the following:

  * `${parameter:transcript}`: The conversation between the agent and the user, including the very last user utterance.
  * `${parameter:transcript_last_utterance}`: The last utterance in the conversation.



At least one built-in parameter should be used in any instruction.

Whether built-in or ingested, the generator parameters are different from the model options which are set when the generator is created. The values of these generator parameters come from a conversation transcript or ingested data. On the other hand, you set the values of the model options for the generator as a whole.

## Test a generator

Within the Build your own GenAI assist console, you can test the generator in the **Test generator** section.

To test a generator in the Build your own GenAI assist console, do the following:

### Console

  1. Add a transcript of the conversation. You can either manually input utterances or upload a transcript in JSON format by clicking **upload**.
  2. To add more data that needs to be ingested, click more_vert and note_add **Add injected data**.



The Build your own GenAI assist console displays generated responses annotated with the generator's name.

### REST

To test a generator using the API, do the following:

  1. Enter the generator name in `generatorName` field.
  2. Provide conversations in the `conversationContext` field.
  3. Provide parameter values, if any, in the `contextReferences` field.
  4. Enter the trigger for generating suggestions in the`triggerEvents` field. Generated suggestions are available in the `generatorSuggestion` field.



## Conversation profile

A conversation profile defines a set of parameters that control the suggestions made during a conversation. The following steps create a [`conversationProfile`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles) resource with a [`HumanAgentAssistantConfig`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.HumanAgentAssistantConfig) object.

### Console

  1. In the [Agent Assist console](https://agentassist.cloud.google.com), go to the **Conversation profiles** page.
  2. Click **\+ Create**.
  3. Enter the display name.
  4. Select the suggestion type check_box **Build-your-own-assist**.
  5. Enter the generator's name or choose the generator's name from the list.



### REST

  1. Call the [`create` method](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles/create) from the [conversation profile resource](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles/create).
  2. Provide a name for the new conversation profile.
  3. Enter the language code.
  4. Enter the generator name in human_agent_suggestion_config.



The following is a JSON example of a conversation profile.
    
    
    {
      "displayName": "build-your-own-assist-test",
      "humanAgentAssistantConfig": {
        "humanAgentSuggestionConfig": {
          "generators": "projects/PROJECT_ID/locations/global/generators/GENERATOR_ID"
        }
      }
    }

### Verify with the simulator

You can verify the conversation profile in the [Agent Assist simulator](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/simulator). The simulator displays generated responses annotated with the generator's name.

## Test a prompt

Within the Build your own GenAI assist console, you can test a prompt with the simulator the same way that you verify a conversation profile. The generated output shown in the following image illustrates how well the `freeform-tool-test1` generator followed the example prompt.

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/images/byoa-test-prompt.png)

## Conversations at runtime

A [conversation](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations#resource:-conversation) is defined as an interaction between an agent, including _human_ agents and _virtual_ agents, and a support customer or end user. At runtime, when a dialog begins between an end user and a human agent, you create a _conversation_. In order to see suggestions, you must create both an end-user participant and a human-agent participant and add them to the conversation.

### Create a conversation

To create a conversation, do the following:

  1. Call the [`create`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations/create) method from the [`conversation resource`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations).
  2. Before using any of the request data, make the following replacements: 
     * PROJECT_ID: your project ID
     * CONVERSATION_PROFILE_ID: your conversation profile ID



HTTP method and URL: 
    
    
    POST https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/conversations

Request JSON body: 
    
    
    {
      "conversationProfile": "projects/PROJECT_ID/conversationProfiles/CONVERSATION_PROFILE_ID",
    }

Within the JSON response, the path segment after `conversations` contains your new conversation ID. The JSON response should look similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/conversations/CONVERSATION_ID",
      "lifecycleState": "IN_PROGRESS",
      "conversationProfile": "projects/PROJECT_ID/conversationProfiles/CONVERSATION_PROFILE_ID",
      "startTime": "2023-11-05T21:05:45.622Z"
    }

### Create an end-user participant

To create an end-user participant, do the following:

  1. Call the [`create`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants/create) method from the [`participants`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants) resource.
  2. Before using any of the request data, make the following replacements: 
     * PROJECT_ID: your project ID
     * CONVERSATION_ID: your conversation ID



Provide your conversation ID and "END_USER" for the role field as follows.

HTTP method and URL: 
    
    
    POST https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/conversations/CONVERSATION_ID/participants

Request JSON body: 
    
    
    {
      "role": "END_USER",
    }

Within the JSON response, the path segment after `participants` contains your new end-user participant ID. The JSON response should look similar to the following:
    
    
    {
     "name": "projects/PROJECT_ID/conversations/CONVERSATION_ID/participants/USER_PARTICIPANT_ID", "role": "END_USER"
    }

### Create a human-agent participant

To create a human-agent participant, do the following:

  1. Call the [`create`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants/create) method from the [`participants`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants) resource.
  2. Before using any of the request data, make the following replacements: 
     * PROJECT_ID: your project ID
     * CONVERSATION_ID: your conversation ID



Provide your conversation ID and `HUMAN_AGENT` role for the field as follows.

HTTP method and URL: 
    
    
    POST https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/conversations/CONVERSATION_ID/participants

Request JSON body: 
    
    
    {
      "role": "HUMAN_AGENT",
    }

Within the JSON response, the path segment after `participants` contains your new human-agent participant ID. The response should look similar to the following:
    
    
    {
    "name": "projects/PROJECT_ID/conversations/CONVERSATION_ID/participants/AGENT_PARTICIPANT_ID", "role": "HUMAN_AGENT"
    }

### Analyze message

A generator can also analyze a message within a conversation. During a conversation, you can add a message and the generator can analyze both human-agent and end-user messages with the [`analyzeContent`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants/analyzeContent#google.cloud.dialogflow.v2.Participants.AnalyzeContent) method from the [`participants`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants) resource.

To add and analyze a human-agent message, follow these steps.

  1. Call the `analyzeContent` method.
  2. Before using any of the request data, make the following replacements: 
     * PROJECT_ID: your project ID
     * CONVERSATION_ID: your conversation ID
     * PARTICIPANT_ID: your human-agent participant ID



Provide the conversation ID and human-agent participant ID. Your request should include something similar to the following:

HTTP method and URL: 
    
    
    POST https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/conversations/CONVERSATION_ID/participants/PARTICIPANT_ID:analyzeContent

Request JSON body: 
    
    
    {
      "textInput": {
        "text": "Bonjour, ici le service client d'ABC fishing, comment puis-je vous aider aujourd'hui ?",
        "languageCode": "en-US"
      }
    }

And you should receive a JSON response similar to the following:
    
    
    {
      "message": {
        "name": "projects/PROJECT_ID/conversations/CONVERSATION_ID/messages/MESSAGE_ID",
        "content": "Bonjour, ici le service client d'ABC fishing, comment puis-je vous aider aujourd'hui ?",
        "languageCode": "en-US",
        "participant": "PARTICIPANT_ID",
        "participantRole": "HUMAN_AGENT",
        "createTime": "2023-02-13T00:01:30.683Z"
      },
      "humanAgentSuggestionResults": [{
        "generateSuggestionsResponse": {
          "generatorSuggestionAnswers": [{
            "generatorSuggestion": {
              "freeFormSuggestion": {
                "response": "Hello, this is ABC fishing customer service, how can I help you today?"
              }
            },
            "sourceGenerator": "projects/PROJECT_ID/locations/global/generators/GENERATOR_ID",
            "answerRecord": "projects/PROJECT_ID/locations/global/answerRecords/ANSWER_RECORD_ID"
          }],
          "latestMessage": "projects/PROJECT_ID/locations/global/conversations/CONVERSATION_ID/messages/MESSAGE_ID"
        }
      }]
    }

To add and analyze an end-user message

  1. Call the [`analyzeContent`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants/analyzeContent#google.cloud.dialogflow.v2.Participants.AnalyzeContent) method. Don't make duplicate calls to the method if it has been called for other Agent Assist features.
  2. Before using any of the request data, make the following replacements: 
     * PROJECT_ID: your project ID
     * CONVERSATION_ID: your conversation ID
     * PARTICIPANT_ID: your human-agent participant ID



Provide the conversation ID and human-agent participant ID. Your request should include something similar to the following:

HTTP method and URL: 
    
    
    POST https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/conversations/CONVERSATION_ID/participants/PARTICIPANT_ID:analyzeContent

Request JSON body: 
    
    
    {
      "textInput": {
        "text": "Hi",
        "languageCode": "en-US"
      }
    }

And you should receive a JSON response similar to the following:
    
    
    {
      "message": {
        "name": "projects/PROJECT_ID/conversations/CONVERSATION_ID/messages/MESSAGE_ID",
        "content": "Hi",
        "languageCode": "en-US",
        "participant": "PARTICIPANT_ID",
        "participantRole": "END_USER",
        "createTime": "2020-02-13T00:07:35.925Z"
      },
      "humanAgentSuggestionResults": [{
        "generateSuggestionsResponse": {
          "generatorSuggestionAnswers": [{
            "generatorSuggestion": {
              "freeFormSuggestion": {
                "response": "Salut"
              }
            },
            "sourceGenerator": "projects/PROJECT_ID/locations/global/generators/GENERATOR_ID",
            "answerRecord": "projects/PROJECT_ID/locations/global/answerRecords/ANSWER_RECORD_ID"
          }],
          "latestMessage": "projects/PROJECT_ID/locations/global/conversations/CONVERSATION_ID/messages/MESSAGE_ID"
        }
      }]
    }

When a conversation is completed and `analyzeContent` was not used, you can use the [`batchCreate`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.entityTypes.entities/batchCreate) method from the [messages](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants.suggestions) resource to import and analyze historical messages of the conversation.

### Get suggestions

The generator also provides suggestions in response to a message at any point in a conversation. By default, the suggestions are for the latest message from either participant. You can also specify the message for which you'd like to get the suggestions. Get suggestions by default or by using one of the following resources.

#### Use included suggestions

The response of `analyzeContent` comes with suggestions. The triggered generator produces these suggestions. Your JSON request should include something similar to the following:

HTTP method and URL: 
    
    
    POST https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/conversations/CONVERSATION_ID/participants/PARTICIPANT_ID:analyzeContent

Request JSON body: 
    
    
    {
      "textInput": {
        "text": "I want to reserve a room.",
        "languageCode": "en-US"
      }
    }

#### Use the `suggestions` resource

Another approach to getting suggestions is to follow these steps.

  1. Call the [`generate`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversations.suggestions/generate) method from the [`suggestions`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversations.suggestions) resource.
  2. Before using any of the request data, make the following replacements: 
     * PROJECT_ID: your project ID
     * CONVERSATION_ID: your conversation ID
     * PARTICIPANT_ID: your human-agent participant ID



Provide the conversation ID, the latest message ID from either participant, and the trigger events. If the message ID field is not set, suggestions are based on the latest message from either participant by default. The generator associated with the trigger event will then be initiated. Your JSON request should include something similar to the following:

HTTP method and URL: 
    
    
    POST https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/conversations/CONVERSATION_IDsuggestions:generate

Request JSON body: 
    
    
    {
      "latestMessage": "projects/PROJECT_ID/conversations/CONVERSATION_IDmessages/Message_ID",
      "triggerEvents": [ "END_OF_UTTERANCE" ]
    }

#### Use the `statelessSuggestion` resource

One last approach to get suggestions is to follow these steps.

  1. Call the [`generate`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.locations.statelessSuggestion/generate) method from the [`statelessSuggestion`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.locations.statelessSuggestion) resource.
  2. Before using any of the request data, make the following replacements: 
     * PROJECT_ID: your project ID
     * LOCATION_ID: your location ID



Provide the generator, the messages of the conversation, and the context references containing ingested data. The ingested data replaces parameters in the generator's instruction. Your JSON request should look similar to the following:

HTTP method and URL: 
    
    
    https://dialogflow.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION_ID/statelessSuggestion:generate

Request JSON body:
    
    
    {
      "generator": {
        "description": "Translation",
        "triggerEvent": "END_OF_UTTERANCE",
        "freeFormContext": {
          "text": "Read the conversation between agent and customer, and the last utterance. Output the last utterance from customer by following these instructions:
          - If the last utterance from AGENT, output the utterance by translating it to English.
          - If the last utterance from CUSTOMER, output the utterance by translating it to French.
          - Specific brand names and technical terms specified under 'GLOSSARY' section, such as 'Google Home,' should remain unchanged as per the glossary guidelines.
    
    # GLOSSARY
    ${parameter:glossary}
    
    # CONVERSATION:
    ${parameter:transcript}
    
    # LAST UTTERANCE:
    ${parameter:transcript_last_utterance}
    
    # OUTPUT: "
        }
      },
      "contextReferences": {
        "glossary": {
          "contextContents": {
            "content": "east one",
            "contentFormat": "PLAIN_TEXT"
          }
        }
      },
      "conversationContext": {
        "messageEntries": [
          {
            "text": "hi",
            "languageCode": "en-US",
            "role": "END_USER",
            "createTime": {
              "seconds": "1400000000",
              "nanos": "10000000"
            }
          },
          {
            "text": "Bonjour, comment puis-je vous aider aujourd\\'hui ?",
            "languageCode": "en-US",
            "role": "HUMAN_AGENT",
            "createTime": {
              "seconds": "1400000010",
              "nanos": "10000000"
            }
          }
        ]
      },
      "triggerEvents": [
        "END_OF_UTTERANCE"
      ]
    }

## Quota limits

You can view quotas and limits for Agent Assist on the [Dialogflow quotas page](https://docs.cloud.google.com/dialogflow/quotas#agent-assist). Build your own GenAI assist includes the following quota limits:

Name | Description | Limit  
---|---|---  
Generator manager operations per minute (per region) | Limit on the number of generator manager operations that can be performed each minute, such as creating, listing or deleting generators. | 300  
Generators (per region) | Limit on the maximum number of generators you can create in a single project. | 200  
Generator suggestion operations per minute per model type (per region) | Limit on the number of generator suggestion operation requests you can receive each minute for each model type. | 10  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
