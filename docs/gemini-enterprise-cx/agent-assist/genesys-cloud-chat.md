---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/genesys-cloud-chat/
title: Configuration for chat integration \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:45.862002+00:00
---

# Configuration for chat integration  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/genesys-cloud-chat/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Configuration for chat integration Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions for how to configure UI modules for integration with chat.

## Set up chat integration

Genesys Cloud supports two types of messaging channels: Chat V2 and Messenger. These channels are designed to enhance customer engagement and provide efficient communication between agents and customers.

Messenger and chat V2 feature real-time communication and communicate with Agent Assist, but Genesys recommends Messenger over chat V2. Messenger has more options for facilitating agent's work. For more details, see the [feature comparison](https://help.mypurecloud.com/articles/web-messaging-and-web-chat-feature-comparison/).

Integration type | Multiple conversations | Generate summaries | Asynchronous update | Unlimited timeout  
---|---|---|---|---  
Chat V2 | close | check | close | close  
Messenger | check | check | check | check  
  
## Configure the interaction widget

To use either chat V2 or Messenger integration, users must configure the interaction widget. The widget monitors ongoing conversations and transfers the discussion data to Agent Assist, which then creates recommendations based on the context.

To configure the interaction widget, follow the instructions for [setting up an interaction widget integration in Genesys Cloud](https://developer.genesys.cloud/blueprints/chat-assistant-blueprint/#setup-an-interaction-widget-integration-in-genesys-cloud).

After you install the integration widget, click the **Configuration** tab. The URL of the application must have the following replacements:

  * Replace `APPLICATION_SERVER_URL` with the URL of your UI application server.
  * Append `pcConversationID`, `gcHostOrigin`, and `gcTargeEnv` to {APPLICATION_SERVER_URL} so the full URL has the following format: 
        
        {APPLICATION_SERVER_URL}?conversationid={{pcConversationId}}&gcHostOrigin={{gcHostOrigin}}&gcTargetEnv={{gcTargetEnv}}
        




The `pcConversationId`, `gcHostOrigin`, and `gcTargetEnv` variables are used to construct the [client application](https://developer.genesys.cloud/platform/integrations/client-apps/sdk/clientapp) to communicate with Genesys cloud. Once the iframe for the client application loads, Genesys cloud populates these variables automatically.

  1. Update the **Iframe Sandbox Options** to `allow-scripts`, `allow-same-origin`, `allow-forms`, `allow-modals`, and `allow-popups`.
  2. Update the **Iframe Feature/Permissions Policy** to `clipboard-write`, `microphone`, and `display-capture`.



Example URL: 
    
    
    https://my-project.wm.r.appspot.com?conversationid={{pcConversationId}}&gcHostOrigin={{gcHostOrigin}}&gcTargetEnv={{gcTargetEnv}}

## Configure the Messenger

To set up the Genesys Cloud Messenger, follow the provided steps in this [document](https://help.mypurecloud.com/articles/deploy-messenger/). After you configure Messenger, follow these [instructions](https://help.mypurecloud.com/articles/deploy-messenger/) to deploy it. When you deploy Messenger, you can use it to communicate with your customers.

Example Messenger deployment:

During the Messenger deployment process, select the inbound architect flow that you configured earlier. This specific flow is crucial for handling incoming messages.

## Configure the inbound call flow

To test with the Genesys Cloud voice integration, set up an inbound call flow. This flow defines how Genesys Cloud will handle incoming calls, such as configuring an IVR, defining DTMF tones, and transferring the call to a queue.

Follow these steps to create an inbound call flow:

  1. Enable a [queue](https://help.mypurecloud.com/articles/create-queues/).
  2. Assign yourself to the queue.
  3. Create a [DID number](https://help.mypurecloud.com/articles/did-numbers/) for testing when calling the agent.
  4. Create [inbound call routing](https://help.mypurecloud.com/articles/add-the-inbound-call-flow/) that has the DID number assigned to it.
  5. Connect the call route to an [inbound call flow](https://help.mypurecloud.com/articles/add-the-inbound-call-flow/).



An example within an inbound call flow is to transfer the call to the Agent Assist integration queue. When a user calls the DID number and the agent has the **On Queue** toggle enabled, the call is available for an agent to pick up in Genesys Cloud. More complex queues can be configured according to business requirements.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
