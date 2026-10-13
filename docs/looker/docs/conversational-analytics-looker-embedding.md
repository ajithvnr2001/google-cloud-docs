---
url: https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-embedding/
title: Embedding Conversational Analytics \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:40.706172+00:00
---

# Embedding Conversational Analytics  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-embedding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Embedding Conversational Analytics Stay organized with collections  Save and categorize content based on your preferences. 

You can embed the Conversational Analytics interface in a website or an application by using an HTML iframe tag just as you can with other Looker content types. The Conversational Analytics interface includes the dashboard data agent conversation pane and the **Conversations** page, where you can chat with data agents that are connected to multiple Looker Explores or chat with a standalone Explore.

Conversational Analytics supports both [private embedding](https://docs.cloud.google.com/looker/docs/private-embedding), where users are authenticated using their Looker login, and [signed embedding](https://docs.cloud.google.com/looker/docs/signed-embedding), where users are authenticated through your own application.

This page describes how to embed the Conversational Analytics interface into an iframe.

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

## Before you begin

To embed Conversational Analytics, the following requirements must be fulfilled:

  * Your instance must be Looker-hosted.
  * Users will need the same permissions that are required to use non-embedded [Conversational Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-setup#required-permissions).
  * To embed a Looker dashboard that uses a Conversational Analytics dashboard data agent, an admin must enable [dashboard data agents](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents-dashboards) [[Preview](https://cloud.google.com/products#product-launch-stages)]. On the **Gemini in Looker** admin page, under the **Enable Trusted Tester Features** setting, turn on the **Enable Dashboard Agents** setting. The **Enable Trusted Tester Features** setting must also be enabled.



### Limitations of embedding Conversational Analytics

Note the following limitations when embedding Conversational Analytics content:

[Embedded themes](https://docs.cloud.google.com/looker/docs/themes-for-embedded-dashboards-and-explores) are partially supported when you're embedding Conversational Analytics. The [General options](https://docs.cloud.google.com/looker/docs/themes-for-embedded-dashboards-and-explores#general) themes apply to Conversational Analytics interfaces. No other theming options are supported. Embedded themes are supported in the data agent conversation experience in an embedded dashboard.

## Creating the Conversational Analytics embed URL

The process to create an embed URL for Conversational Analytics is the same as for embedding other content types, such as dashboards or Looks, where you add `/embed/` after the instance name and before the content folder and content ID.

To embed a conversation with an Explore data agent or with a standalone Explore, find the non-embedded URL of the conversation or agent, and add `/embed/` before the `conversations` or `agents` folder. For example:

  * For the **Conversations** page, the embed URL will look like `https://my_looker_instance.looker.com/embed/conversations`.
  * For the **Agents** page, the embed URL will look like `https://my_looker_instance.looker.com/embed/agents`.
  * For a specific conversation, the embed URL will look like `https://my_looker_instance.looker.com/embed/conversations/c9f370ac830b4669aeb494396422004c`. In this example, `c9f370ac830b4669aeb494396422004c` is the conversation ID.
  * For a dashboard that uses a Conversational Analytics dashboard data agent [[Preview](https://cloud.google.com/products#product-launch-stages)], the embed URL will look like `https://my_looker_instance.looker.com/embed/dashboards/1`.



### Private embedding of Conversational Analytics

For private embedding, create an iframe and use the Conversational Analytics embed URL as your iframe source, as shown in the following example:
    
    
      <iframe
          src="https://my_looker_instance.looker.com/embed/conversations/c9f370ac830b4669aeb494396422004c"
          width="1000"
          height="2000"
          frameborder="0">
      </iframe>
    

Then embed the iframe in your web page or application.

### Signed embedding of Conversational Analytics

The process for signed embedding of Conversational Analytics is the same as for other content types. Use the Conversational Analytics embed URL when [coding the signed embed URL](https://docs.cloud.google.com/looker/docs/signed-embedding#manually_coding_the_signed_embed_url).

Embed users will need the proper permissions to [use Conversational Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-setup#required-permissions), such as `chat_with_explore` or `chat_with_agent`. As a result, you will have to add those permissions to the [signed embed URL](https://docs.cloud.google.com/looker/docs/signed-embedding#creating_the_embed_url).

You can add a [URL parameter](https://docs.cloud.google.com/looker/docs/signed-embedding#parameters) to make the ![](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/chat_spark/default/24px.svg) Gemini spark that opens the data agent conversation pane from a dashboard visible or hidden to users. By default, the option to start a conversation with a dashboard data agent is visible to users who have permissions to interact with dashboard agents. To hide the Gemini spark from a specific dashboard and remove the ability to start a conversation with a dashboard data agent, add the `ca_chat=false` parameter to the signed embed URL. For example: `https://my_looker_instance.looker.com/embed/dashboards/1?ca_chat=false`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
