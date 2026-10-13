---
url: https://docs.cloud.google.com/dialogflow/cx/docs/quick/integration/
title: Interactions with an integration \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:32.484816+00:00
---

# Interactions with an integration  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/quick/integration/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Interactions with an integration Stay organized with collections  Save and categorize content based on your preferences. 

With an [integration](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration), end-user interactions are handled for you. You just need to build an agent, optionally implement a webhook, and configure the integration.

This guide shows you how to use the [Dialogflow CX Messenger](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/dialogflow-messenger) integration to provide a simple text chat user interface for your agent.

## Before you begin

If you don't plan on using an integration, you can skip this quickstart.

You should do the following before reading this guide:

  1. Read [flow basics](https://docs.cloud.google.com/dialogflow/cx/docs/basics).
  2. Perform [setup steps](https://docs.cloud.google.com/dialogflow/cx/docs/quick/setup).
  3. Perform steps in the [Build an agent using flows](https://docs.cloud.google.com/dialogflow/cx/docs/quick/build-agent) quickstart guide. Steps below continue working on the same agent. If you no longer have that agent, you can [download the agent](https://docs.cloud.google.com/static/dialogflow/cx/docs/data/agent-shirts-1-flow.zip) and [restore it](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#export).



## Setup

**Note:** The steps below create an integration that allows unauthenticated agent query access. See the [Dialogflow CX Messenger documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/dialogflow-messenger) for instructions to create an authenticated integration.

**Note:** Make sure [billing is enabled](https://docs.cloud.google.com/dialogflow/cx/docs/quick/setup#billing) on your project before testing the integration.

To set up unauthenticated access to your Dialogflow CX Messenger agent:

  1. Go to the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Choose your Google Cloud project.
  3. Select your agent.
  4. Select the **Manage** tab.
  5. Click **Integrations** in the left sidebar menu.
  6. Click **Connect** on **Dialogflow CX Messenger**.
  7. A configuration dialog opens.
  8. If the integration was previously setup for this agent, you will see embeddable HTML code. Regardless of whether you want what authenticated or unauthenticated, click the **Disable...** button at the bottom of the dialog, so you can reconfigure the settings in the next step.
  9. Select an **Environment**.
  10. Select **Unauthenticated API**.
  11. Select a style.
  12. Optionally restrict domain access.
  13. Click **Enable the unauthenticated API**.
  14. The dialog will show the embeddable HTML code that can be embedded on your website. Copy this code.
  15. Click **Done**.



## Embed

Paste the embed code you copied above in a webpage on your website. The `<script>` and `<df-messenger>` HTML elements should be in the `<body>` element of your page.

If you are using an authenticated integration, set the `oauth-client-id` attribute for `<df-messenger>` to your Oauth client id. And if you want to use end-users' identities for [tool authentication](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/tool#openapi_tool_api_authentication), set the `access-token-name` attribute with any name you like. Then use Bearer Token with value `$session.params.ACCESS_TOKEN_NAME` for tool authentication.

Update any other attributes that require updating.

To allow for responsive layouts, also add the following to your `<head>` element:
    
    
    <meta name="viewport" content="width=device-width, initial-scale=1">
    

Once embedded, you can interact with your agent through the webpage by clicking the chat icon in the lower right corner.

![Messenger interface screenshot](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/quick-integration.png)

## Customize

You can customize the appearance and behavior of this user interface in many ways. See the [Dialogflow CX Messenger documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/dialogflow-messenger) for more information.

[ Previous arrow_back  Create a webhook  ](https://docs.cloud.google.com/dialogflow/cx/docs/quick/webhook)

[ Next Interactions with the API  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/quick/api)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
