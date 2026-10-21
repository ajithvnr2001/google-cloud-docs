---
url: https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features/
title: Manage web app features \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:16:10.702311+00:00
---

# Manage web app features  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Manage web app features Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure the feature management settings for your Gemini Enterprise web app using the Google Cloud console. You can control the features that are available for your end users.

## Before you begin

Make sure you have the following:

  * The [Gemini Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.agentspaceAdmin) IAM role (`roles/discoveryengine.agentspaceAdmin`).

  * An existing Gemini Enterprise web app. For information about creating a new app, see [Create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app).




## Configure feature controls

To configure the features available in your web app, follow these steps:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click the name of the app that you want to configure.

  3. Click **Configurations** and then click the **Feature Management** tab.

  4. You can turn on or turn off the following features in the web app:

Feature control | Description  
---|---  
**Enable Agent Gallery** |  When enabled, the web app shows the **Agent Gallery**. For more information, see [Browse agents with Agent Gallery](https://docs.cloud.google.com/gemini/enterprise/docs/agent-gallery).   
**Enable chat agents** |  When enabled, users can build and use custom chat agents. For more information, see [Chat agent overview](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/chat-agents).   
**Enable workflows** |  When enabled, users can create and run custom workflows. For more information, see [Workflows overview](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/workflows).   
**Enable model selector** |  When enabled, users can select the Gemini or partner model that they want to use in the web app.   
**Enable Gemini Notebook** |  When enabled, users can use Gemini Notebook Enterprise in the web app. For more information, see [Use Gemini Notebook Enterprise within Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/access-notebooklm).   
**Enable session sharing** |  When enabled, users can share Gemini Enterprise conversations with other users.   
**Enable memory and customization** |  When enabled, Gemini Enterprise uses past conversations and saved memory settings to generate personalized and relevant responses.   
**Enable Canvas** |  When enabled, users can create, edit, and export files in an interactive editor next to their chat conversation. For more information, see [Create and edit documents and slides in Canvas](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas).   
**Enable projects** |  When enabled, users can create and use collaborative projects in the web app. For more information, see [Create and manage projects](https://docs.cloud.google.com/gemini/enterprise/docs/projects).   
**Enable image generation** |  When enabled, users can generate images in the web app. You can also choose the image model you want your users to use.   
  
Available models include: 
     * **Gemini 3 Pro image (Nano Banana Pro)** : This model is generally available (GA) and is turned off by default. It is only available in the Global region.  A warning is displayed if an end user attempts to use the Gemini 3 Pro image model in a region other than Global. The user can accept the terms and proceed. 
     * **Gemini 3.1 Flash image (Nano Banana 2)** : This model is generally available (GA) and is turned off by default. If an administrator turned on this model during the Public Preview, it remains turned on in GA too. 
     * **Gemini 2.5 Flash image** : The system defaults to this model if you don't make any selection.   
**Enable video generation** |  When enabled, users can generate videos in the web app.   
**Enable OneDrive upload** |  When enabled, users can upload files to the assistant from Microsoft OneDrive as a data source.   
**Enable talk to content** |  When enabled, users can navigate to the **Sources** referenced in an answer, add documents to the conversation by clicking the add icon next to a source, and then ask questions about the content of the documents.   
**Enable speech-to-text** |  When enabled, users can dictate their prompts into the web app, using the mic icon in the chat box. For more information, see [Use your voice to chat](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-chat#voice-chat).   
**Enable Google Drive upload** |  When enabled, users can upload files to the assistant from Google Drive as a data source.   
**Include cross-domain documents** |  You can enable the **Include cross-domain documents** feature for an existing app, even if you didn't enable it during app creation. When enabled, users can search and access documents from outside your organization using the [Google Drive data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gdrive/set-up-data-store).   
  
Enabling this feature increases exposure to security risks, such as prompt injection from external documents and potential manipulation of search results.   
**Enable welcome emails** |  When enabled, users receive a welcome email the first time they sign in to the web app.   
**Enable skills** |  When enabled, users can create and use skills in the web app. For more information, see [Create and manage skills](https://docs.cloud.google.com/gemini/enterprise/docs/skills).   
**Enable skill sharing** |  When enabled, users can share custom skills with other users using the Gemini Enterprise app. To enable this, you must turn on **Enable skills**. If you don't also turn on the **Enable skill sharing without admin approval** setting, administrators must review and approve pending skill share requests. For more information, see [Create and manage skills](https://docs.cloud.google.com/gemini/enterprise/docs/skills).   
**Enable skill sharing without admin approval** |  When enabled, users on your team can share and use custom skills without administrator approval when using the Gemini Enterprise app. To enable this setting, you must turn on **Enable skills** and **Enable skill sharing**.  Review and approve pending sharing requests before turning on this feature to prevent users from having to resubmit the sharing requests.  For more information, see [Create and manage skills](https://docs.cloud.google.com/gemini/enterprise/docs/skills).   
**Enable agent sharing** |  When enabled, users can share agents created using Workflow Builder with other users using the Gemini Enterprise app. For more information, see [Share an agent](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/share-chat-agent). If you use Okta or Microsoft Entra ID as a third-party identity provider with Workforce Identity Federation, [configure SCIM](https://docs.cloud.google.com/gemini/enterprise/docs/configure-identity-provider#configure_workforce_id_federation) to enable autocomplete of email addresses (and group names) when users share agents.  
**Enable agent sharing without admin approval** |  When enabled, users on your team can share and use agents created using Workflow Builder without administrator approval when using the Gemini Enterprise app.  
Note: Review and approve pending sharing requests before turning on this feature to prevent users from having to resubmit the sharing requests. For more information, see [Share an agent](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/share-chat-agent).   
**Enable End Users to share with Groups** |  When enabled, users can share custom agents with groups in the organization. Whether the administrator must approve sharing depends on the **Enable agent sharing without admin approval** setting. For more information, see [Share an agent](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/share-chat-agent). If you use Okta or Microsoft Entra ID as a third-party identity provider with Workforce Identity Federation, [configure SCIM](https://docs.cloud.google.com/gemini/enterprise/docs/configure-identity-provider#configure_workforce_id_federation) to enable autocomplete of group names (and email addresses) when users share agents.  
**Model availability** |  You can select the models that users can use in the web app. To enable model selection, you must turn on the **Enable model selector** toggle.  The following Gemini and partner models are available: 
     * **Gemini models** : Gemini 4 Argon, Gemini 3.8 Flash, Gemini 3.7 Flash, Gemini 3.6 Flash, Gemini 3.5 Flash, Gemini 3.1 Pro, and Gemini 2.5 Pro. For more information, see Enable Gemini models. 
     * **Partner models** : Anthropic models—Claude Opus 5.5 and Claude Sonnet 5.5. For more information, see Enable third-party models.   



## Enable Gemini models

You can control which Gemini models users can select in the Gemini Enterprise web app. To let users choose a model in the web app, make sure that the **Enable model selector** toggle is turned on in the **Feature Management** tab.

### Available Gemini models

The following Gemini models are available in the web app:

Model | Default state | Supported locations and notes  
---|---|---  
**Gemini 4 Argon** |  Turned off in `global`, `us`, and `eu` (defaults to on beginning October 27, 2026)  |  To make Gemini 4 Argon available to users, click the **Gemini 4 Argon** toggle to the on position. For unsupported in-country regions, confirm the warning dialog to route traffic to the `global` endpoint. For more information, see [Data residency for Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/locations).   
**Gemini 3.8 Flash** |  Turned on in `global`, `us`, and `eu`, and in `sg` and `europe-west2` |  If you don't want users to use Gemini 3.8 Flash, click the **Gemini 3.8 Flash** toggle to the off position. For unsupported in-country regions, click the **Gemini 3.8 Flash** toggle to the on position and confirm the warning dialog to route traffic to the `global` endpoint.   
**Gemini 3.7 Flash** | Turned off |  To let users use Gemini 3.7 Flash, click the **Gemini 3.7 Flash** toggle to the on position. For unsupported in-country regions, you must also confirm a warning dialog to route traffic to the `global` endpoint.   
**Gemini 3.6 Flash** | Turned off |  To let users use Gemini 3.6 Flash, click the **Gemini 3.6 Flash** toggle to the on position. For unsupported in-country regions, you must also confirm a warning dialog to route traffic to the `global` endpoint.   
**Gemini 3.5 Flash** | Turned on |  For some models in General Availability (GA) in the Gemini Enterprise app, such as Gemini 3.5 Flash, you can't turn the toggle off.   
**Gemini 3.1 Pro** | Turned off |  Available in Limited Availability if supported in your region. To let users use Gemini 3.1 Pro, click the **Gemini 3.1 Pro** toggle to the on position. For more information about known limitations, see [Using Gemini 3.1 Pro in Limited Availability](https://docs.cloud.google.com/gemini/enterprise/docs/known-limitations#using-gemini-3-preview).   
**Gemini 2.5 Pro** | Turned on in `global`, `us`, and `eu` |  If you don't want users to use Gemini 2.5 Pro, click the **Gemini 2.5 Pro** toggle to the off position. Gemini 2.5 Pro isn't available in in-country regions (`ca`, `asia-northeast1`, `in`, `sg`, and `europe-west2`). For more information, see [Data residency for Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/locations).   
  
### Turn on or turn off a Gemini model

To turn on or turn off a Gemini model in the web app, follow these steps:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click the name of the app that you want to configure.

  3. Click **Configurations** and then click the **Feature Management** tab.

  4. Go to the **Gemini model availability** section.

  5. Click the toggle for the Gemini model that you want to turn on or turn off.

If you turn on a model in an unsupported in-country region, confirm the warning dialog to route traffic to the `global` endpoint.

  6. Click **Save**.




The changes take effect after a few minutes.

## Enable third-party models

In addition to Gemini models, you can let users chat with third-party models, such as Anthropic models—Claude Opus 5.5 and Claude Sonnet 5.5—in the Gemini Enterprise web app. You pay for third-party model usage per token, on a pay-as-you-go basis.

### Available third-party models

The following third-party models are available in the web app:

Model | Publisher | Supported locations  
---|---|---  
[Claude Opus 5.5](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/opus-5-5) | Anthropic | `global`, `us`, and `eu`  
[Claude Sonnet 5.5](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/sonnet-5-5) | Anthropic | `global`, `us`, and `eu`  
  
Anthropic models—Claude Opus 5.5 and Claude Sonnet 5.5—are turned off by default in the `global`, `us`, and `eu` regions. To make them available to end users, turn them on by enabling billing and accepting the terms of service. For more information about regional support, see [Data residency for Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/locations).

Third-party models aren't available in the Gemini Enterprise Starter edition. They also aren't available for in-country regions.

### Before you begin

Before you turn on a third-party model, make sure that the following requirements are met:

  * You have the [Gemini Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.agentspaceAdmin) IAM role (`roles/discoveryengine.agentspaceAdmin`).

  * If you have a subscription, **Pay-as-you-go usage above quota** is turned on for your project. You must turn it on separately for each edition, such as Gemini Enterprise Standard and Gemini Enterprise Plus. For more information, see [Configure overages](https://docs.cloud.google.com/gemini/enterprise/docs/configure-overages).

  * The **Enable model selector** toggle is turned on in the **Feature Management** tab, so that users can select the model in the web app.




We recommend that you [set a monthly spend limit](https://docs.cloud.google.com/gemini/enterprise/docs/configure-overages#set-spend-limit) and [budgets in Cloud Billing](https://docs.cloud.google.com/billing/docs/how-to/budgets) to control costs. For pricing information, see [Claude pricing](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-overages#claude-pricing).

**Note:** If you have negotiated pricing or a custom contract, the prices might differ from the published prices. Refer to your agreement for exact pricing.

### Turn on a third-party model

To make a third-party model available to users in the web app, follow these steps:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click the name of the app that you want to configure.

  3. Click **Configurations** and then click the **Feature Management** tab.

  4. Go to the **Enable third-party models** section.

  5. In the section for the publisher, click the toggle for the model that you want to turn on.

The **_Model_ pricing** dialog appears. The dialog describes how the model is charged and checks whether **Pay-as-you-go usage above quota** is turned on for your project.

  6. In the **_Model_ pricing** dialog, do one of the following:

     * If pay-as-you-go usage is available for your project, click **Enable**.
     * If **Pay-as-you-go usage above quota** isn't turned on, click **Go to Usage & spend** to turn it on, and then return to this procedure. The model toggle is turned off.
     * If your project's billing account isn't eligible for **Pay-as-you-go usage above quota** , you can't turn on the model. Click **Cancel** and contact your billing administrator.
  7. If the **Terms of service** dialog appears, read the terms for the model. Go to the end of the terms, and then click **Agree**.

You accept the terms of service once for each project and model family. For example, after you accept the terms for Claude Opus 5.5 in a project, the **Terms of service** dialog doesn't appear again when you turn on that model in other apps in the same project.

If you click **Cancel** , the model toggle is turned off.

  8. Click **Save**.

  9. In the **Important billing info** dialog, review the billing information, and then click **I understand**.


**Note:** When you enable a Claude model for the first time, allow up to 15 minutes for the change to take effect. After the model is available, users can select it from the **Model** selector.

### Turn off a third-party model

To stop users from using a third-party model, follow these steps:

  1. In the **Feature Management** tab, go to the **Enable third-party models** section.

  2. Click the toggle for the model to the off position.

  3. Click **Save**.




The model is removed from the model selector in the web app after a few minutes.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
