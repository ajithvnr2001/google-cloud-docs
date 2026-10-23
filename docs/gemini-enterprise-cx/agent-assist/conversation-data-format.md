---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-data-format/
title: Upload conversation data \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:32.796713+00:00
---

# Upload conversation data  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-data-format/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Upload conversation data Stay organized with collections  Save and categorize content based on your preferences. 

Conversation data is accepted as transcripts (Smart Reply) and transcripts plus annotation data (Summarization). In order to use Smart Reply and Summarization during runtime you must provide your own conversation data.

This page guides you through the steps required to use the public datasets as well as to format your own data for upload to Cloud Storage. You must provide your conversation data as [JSON-formatted text files](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-data-format#conversation_transcript_data).

## Smart Reply data format

Smart Reply can be used in conjunction with any Agent Assist feature, or as a stand-alone feature. In order to implement Smart Reply, you must provide Agent Assist with conversation data.

## Summarization data format

Summarization can be used in conjunction with any Agent Assist feature, or as a stand-alone feature. In order to implement Summarization, you must provide Agent Assist with conversation data that includes **annotations**. An annotation is a summary of an associated conversation transcript. Annotations are used to train a model that you can use to generate summaries for your agents at the end of each conversation with an end-user.

### Format annotations

Agent Assist Summarization custom models are trained using _conversation datasets_. A conversation dataset contains your own uploaded transcript and annotation data.

Before you can begin uploading data, you must make sure that that each conversation transcript is in [`JSON` format](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-data-format#conversation_transcript_data), has an associated annotation, and is stored in a [Google Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).

To create annotations, add expected `key` and `value` strings to the `annotation` field associated with each conversation in your dataset. For best results, annotation training data should adhere to the following guidelines:

  1. The recommended minimum number of training annotations is 1000. The enforced minimum number is 100.
  2. Training data should not contain PII.
  3. Annotations should not include any information about gender, race or age.
  4. Annotations should not use toxic or profane language.
  5. Annotations should not contain any information that can't be inferred from the corresponding conversation transcript.
  6. Each annotation can contain up to 3 sections. You can choose your own section names.
  7. Annotations should have correct spelling and grammar.



The following is an example demonstrating the format of a conversation transcript with associated annotation:
    
    
    {
      "entries": [
        {
          "text": "How can I help?",
          "role": "AGENT"
        },
        {
          "text": "I cannot login",
          "role": "CUSTOMER"
        },
        {
          "text": "Ok, let me confirm. Are you experiencing issues accessing your account",
          "role": "AGENT"
        },
        {
          "text": "Yes",
          "role": "CUSTOMER"
        },
        {
          "text": "Got it. Do you still have access to the registered email for the account",
          "role": "AGENT"
        },
        {
          "text": "Yes",
          "role": "AGENT"
        },
        {
          "text": "I have sent an email with reset steps. You can follow the instructions in the email to reset your login password",
          "role": "AGENT"
        },
        {
          "text": "That's nice",
          "role": "CUSTOMER"
        },
        {
          "text": "Is there anything else I can help",
          "role": "AGENT"
        },
        {
          "text": "No that's all",
          "role": "CUSTOMER"
        },
        {
          "text": "Thanks for calling. You have a nice day",
          "role": "AGENT"
        }
      ],
      "conversation_info": {
        "annotations": [
          {
            "annotation": {
              "conversation_summarization_suggestion": {
                "text_sections": [
                  {
                    "key": "Situation",
                    "value": "Customer was unable to login to account"
                  },
                  {
                    "key": "Action",
                    "value": "Agent sent an email with password reset instructions"
                  },
                  {
                    "key": "Outcome",
                    "value": "Problem was resolved"
                  }
                ]
              }
            }
          }
        ]
      }
    }
    

## Conversation transcript data

Text conversation data must be supplied in JSON-formatted files, where each file contains data for a single conversation. The following describes the required JSON format.

### Conversation

The top-level object for conversation data.

Field | Type | Description  
---|---|---  
conversation_info | ConversationInfo { } | Optional. Metadata for the conversation.  
entries | Entry [ ] | Required. The chronologically ordered conversation messages.  
  
### ConversationInfo

The metadata for a conversation.

Field | Type | Description  
---|---|---  
categories | Category [ ] | Optional. Custom categories for the conversation data.  
  
### Category

Conversation data category. If you provide categories with your conversation data, they will be used to identify topics in your conversations. If you do not provide categories, the system will automatically categorize conversations based on the content.

Field | Type | Description  
---|---|---  
display_name | string | Required. A display name for the category.  
  
### Entry

Data for a single conversation message.

Field | Type | Description  
---|---|---  
text | string | Required. The text for this conversation message. All text should be capitalized properly. Model quality can be significantly impacted if all letters in the text are either capitalized or lowercase. An error will be returned if this field is left empty.  
user_id | integer | Optional. A number that identifies the conversation participant. Each participant should have a single `user_id`, used repeatedly if they participate in multiple conversations.  
role | string | Required. The conversation participant role. One of: "AGENT", "CUSTOMER".  
start_timestamp_usec | integer | Optional if the conversation is only used for FAQ assist, Article Suggestion and Summarization, otherwise Required. The timestamp for the start of this conversation turn in microseconds.  
  
### Example

The following shows an example of a conversation data file.
    
    
    {
      "conversation_info":{
        "categories":[
          {
            "display_name":"Category 1"
          }
        ]
      },
      "entries": [
        {
          "start_timestamp_usec": 1000000,
          "text": "Hello, I'm calling in regards to ...",
          "role": "CUSTOMER",
          "user_id": 1
        },
        {
          "start_timestamp_usec": 5000000,
          "text": "Yes, I can answer your question ...",
          "role": "AGENT",
          "user_id": 2
        },
        ...
      ]
    }
    

## Upload conversations to Cloud Storage

You must provide your conversation data in a Cloud Storage bucket contained within your Google Cloud Platform project. When creating the bucket:

  * Be sure that you have selected the Google Cloud Platform project you use for Dialogflow.
  * Use the [Standard Storage class](https://docs.cloud.google.com/storage/docs/storage-classes#standard).
  * Set the [bucket location](https://docs.cloud.google.com/storage/docs/locations) to a location nearest to your location. You will need the location ID (for example, `us-west1`) when providing the conversation data, so take note of your choice.
  * You will also need the bucket name when providing the conversation data.



Follow the [Cloud storage quickstart](https://docs.cloud.google.com/storage/docs/quickstart-console) instructions to create a bucket and upload files.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
