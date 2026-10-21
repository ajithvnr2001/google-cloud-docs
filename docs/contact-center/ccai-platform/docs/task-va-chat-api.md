---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/task-va-chat-api/
title: Use virtual task assistants with the chat API platform \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:33:55.612666+00:00
---

# Use virtual task assistants with the chat API platform  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/task-va-chat-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Use virtual task assistants with the chat API platform Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to incorporate virtual task assistants into chat sessions using a custom app built using the chat API platform. After a human agent transfers a chat session to a virtual task assistant, the virtual task assistant can communicate a message to the end-user without the human agent seeing it. This lets you automate processes like collecting sensitive information or performing data lookups while protecting the end-user's privacy.

## Workflow for a virtual task assistant participating in a chat session

Here's the workflow for a virtual task assistant participating in a chat session using a custom app:

  1. A human agent transfers a chat session in a custom chat app to a virtual task assistant.
  2. The chat app sends the end-user's message using a `POST` request to the following endpoint. Authenticate using [basic authentication](https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api#basic_authentication).
         
         https://YOUR_CCAAS_HOST/apps/api/v1/chats/CHAT_ID/message
         

Replace the following:

     * `YOUR_CCAAS_HOST`: your Contact Center AI Platform (CCAI Platform) host

     * `CHAT_ID`: the chat ID

**Request body**

The following is an example of a request body:
    
    {
      "from_user_id": 12345,
      "message": {
        "type": "text",
        "content": {
          "text": "Example response from an end-user."
        }
      }
    }
    

  3. If the system detects an active virtual task assistant, it routes the message directly to the virtual task assistant. The message is designated as a `server_message` type, which hides it from the human agent to protect end-user privacy. If the system doesn't detect an active virtual task assistant, it routes the message to an available human agent.

  4. When a virtual task assistant sends a response, your webhook endpoint receives a `message_received` event. This webhook payload contains the message from the virtual task assistant in the `server_message` property, so you don't need to make another API call to get the message. For more information, see [Chat platform API Guide](https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-platform-api-guide).

**Example webhook payload**

The following is an example webhook payload:
         
         {
           "event_type": "message_received",
           "timestamp": "2025-09-25T14:30:00Z",
           "chat_id": 37,
           "body": {
             "sender": {
               "id": 71,
               "type": "task_virtual_agent",
               "status": "connected"
             },
             "message": {
               "type": "server_message",
               "message_id": 1,
               "visibility": "task_virtual_agent"
             },
             "server_message": {
               "content": {
                 "type": "text",
                 "content": "Thank you. Please enter the 6-digit code sent to your device."
               }
             }
           }
         }
         

  5. When the virtual task assistant completes its task, it transfers the chat session back to the human agent.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
