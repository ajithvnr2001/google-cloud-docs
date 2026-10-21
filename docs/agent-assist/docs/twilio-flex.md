---
url: https://docs.cloud.google.com/agent-assist/docs/twilio-flex/
title: Deploy Twilio Flex \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:10:53.693794+00:00
---

# Deploy Twilio Flex  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-assist/docs/twilio-flex/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Deploy Twilio Flex Stay organized with collections  Save and categorize content based on your preferences. 

The frontend portion of the Twilio integration consists of two components: Twilio functions and plugins. Functions host the HTML document and API methods needed to use Agent Assist and replace the need for hosting elsewhere. A Twilio plugin is a way to present the Agent Assist interface to the agent desktop.

## Twilio functions

The Twilio functions are serverless API endpoints that can perform work hosted by Twilio. They provide user verification, chat service tokens, and the Agent Assist interface.

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/images/twilio-functions.jpg)

## Twilio Flex plugin

Use the Flex plugin to customize user experiences and behaviors for the Flex agents and supervisors. You present the Agent Assist console to the agent within the Flex application.

## Environment variables

  1. Create a file named `.env` in the `agent-assist-functions` directory or
  2. Create a file named `.env.dev` in the `agent-assist-plugins` directory.
  3. Set the following environment variables for the plugin to function after deployment:

Name type | Context  
---|---  
`TWILIO_ACCOUNT_SID` | Find in the Twilio Flex dashboard.  
`ACCOUNT_SID` | Find in the Twilio Flex dashboard.  
`AUTH_TOKEN` | Find in the Twilio Flex dashboard.  
`TWILIO_API_KEY` | Create in the [Twilio console](https://www.twilio.com/console/runtime/api-keys/create).  
`TWILIO_API_SECRET` | Create in the [Twilio console](https://www.twilio.com/console/runtime/api-keys/create).  
`TWILIO_CHAT_SERVICE_SID` | Locate the [service SID](https://console.twilio.com/us1/develop/chat/manage/services?frameUrl=/console/chat/services).  
`PROXY_SERVER_URL` | This is the backend server URL.  
`TWILIO_CONVERSATION_PROFILE` | Find in the Twilio Flex Dashboard.  
`TWILIO_FEATURES` | This is a comma-separated list of Agent Assist suggestion features to render, such as: `SMART_REPLY`, `CONVERSATION_SUMMARIZATION`  
`TWILIO_FUNCTIONS_URL` | This is the Cloud Run URL for the backend application after you deploy the functions. Select the **Twilio Agent Assist Functions** option. Then, you should see a URL resembling twilio-agent-assist-functions-####-dev.twil.io.  
`TWILIO_DEBUG` | Show logs in the console: True, false, or left undefined.  
  
For more information regarding environment variable setup, refer to the relevant Twilio documentation.

## Deployment

Use the following script to deploy the solution to your Twilio instance:
    
    
    npm run deploy:functions #Deploys just the functions to the Twilio instance.
    npm run deploy:plugin #Deploys just the plugin to the Twilio instance, run command produced in the output to activate.
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
