---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/conversation-data-format/
title: Conversation data format \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:22.854301+00:00
---

# Conversation data format  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/conversation-data-format/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Conversation data format Stay organized with collections  Save and categorize content based on your preferences. 

Customer Experience Insights uses conversation data that you upload to a Cloud Storage bucket. You can provide your conversation data to the API as either [audio](https://docs.cloud.google.com/gemini-enterprise-cx/insights/ingest-conversations-api#audio) or [text](https://docs.cloud.google.com/gemini-enterprise-cx/insights/ingest-conversations-api#transcripts) files.

## Conversation transcript data

Your text files include the following details.

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

Conversation data category. If you provide categories with your conversation data, they will be used to identify topics in your conversations. If you don't provide categories, the system will automatically categorize conversations based on the content.

Field | Type | Description  
---|---|---  
display_name | string | Required. A display name for the category.  
  
### Entry

Data for a single conversation message.

Field | Type | Description  
---|---|---  
text | string | Required. The text for this conversation message.  
user_id | integer | Required. A number that identifies the conversation participant. Each participant should have a single `user_id`, used repeatedly if they participate in multiple conversations.  
role | string | Required. The conversation participant role. One of: "AGENT", "AUTOMATED_AGENT", "CUSTOMER", "END_USER".  
start_timestamp_usec | integer | Required. The timestamp for the start of this conversation turn in microseconds of UTC time since Unix epoch.  
  
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
        }
      ]
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
