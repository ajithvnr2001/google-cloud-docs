---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/liveperson/
title: Integrate UI modules with LivePerson \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:52.966993+00:00
---

# Integrate UI modules with LivePerson  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/liveperson/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Integrate UI modules with LivePerson Stay organized with collections  Save and categorize content based on your preferences. 

This document walks you through the steps required to integrate UI modules with [LivePerson](https://www.liveperson.com/) and surface real-time suggestions. The following actions are included in this tutorial:

  1. Install the Conversational Cloud application in LivePerson.
  2. Update the missing environment variables in both servers and re-deploy them.
  3. Configure the Agent Assist widget in LivePerson.



## Before you begin

You must complete the following actions before you can begin this tutorial. Both repositories need to be deployed before the LivePerson integration will work:

  1. For access to the repository, please reach out to agent-assist-ui-modules-support@google.com.
  2. [Deploy an application server](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/liveperson-application) that will serve the Agent Assist modules UI.
  3. [Deploy a proxy server](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/liveperson-proxy) that will handle authentication and calls to the Dialogflow API.



## Install a Conversational Cloud application

You need to register your application as a Conversational Cloud application in your LivePerson account in order to integrate with LivePerson OAuth authentication. You will need to contact a LivePerson team member who can facilitate the installation. Follow the instructions for doing this in the [LivePerson documentation](https://developers.liveperson.com/conversational-cloud-applications-installing-conversational-cloud-applications.html).

The Manifest Schema that you submit to LivePerson should look similar to the following. Replace all instances of {APPLICATION_SERVER_URL} with the URL of your UI modules application server:
    
    
    {
      "client_name": "com.liveperson.GoogleAgentAssist",
      "display_name": "Agent Assist",
      "response_types": ["code"],
      "scope": "msg.consumer",
      "entry_uri": "{APPLICATION_SERVER_URL}",
      "grant_types": [
        "authorization_code",
        "client_credentials",
        "refresh_token"
      ],
      "redirect_uris": [
        "{APPLICATION_SERVER_URL}/home"
      ]
    }
    

## Update missing environment variables

Once the Conversational Cloud application has been installed, LivePerson will provide a client ID and client secret. Update the environment variables of the [application server](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/liveperson-application#configuration) and the [proxy server](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/liveperson-proxy#configuration) to include the correct values for `LP_CLIENT_ID` and `LP_CLIENT_SECRET`, then re-deploy both servers.

## Configure the LivePerson widget

To configure the LivePerson widget, follow the instructions for [adding your own widgets to the agent workspace](https://developers.liveperson.com/add-agent-widgets-add-your-own-widgets-to-the-agent-workspace.html).

The URL of the application should be in the following format, with the following replacements:

  * Replace `{APPLICATION_SERVER_URL}` with the URL of your UI application server.
  * Replace `{CONVERSATION_PROFILE_NAME}` with the name of the [Conversation Profile](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles) you would like to use (example: projects/my-project/conversationProfiles/abc123).
  * Replace `{FEATURES}` with a comma-separated list of Agent Assist features you would like the application to include. Currently supported features include: `SMART_REPLY`, `ARTICLE_SUGGESTION`, `FAQ`, and `CONVERSATION_SUMMARIZATION`. Only include features that are configured on your conversation profile.



`{APPLICATION_SERVER_URL}?conversationProfile={CONVERSATION_PROFILE_NAME}&features={FEATURES}`

Example URL:

`https://my-project.wm.r.appspot.com?conversationProfile=projects/my-project/conversationProfiles/abc123&features=ARTICLE_SUGGESTION,CONVERSATION_SUMMARIZATION`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
