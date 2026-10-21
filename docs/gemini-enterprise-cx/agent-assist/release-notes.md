---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/release-notes/
title: Agent Assist release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:04:14.904617+00:00
---

# Agent Assist release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Agent Assist release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Agent Assist. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/agent-assist-release-notes.xml) directly. 

## October 12, 2026

Feature

[Gemini transcribe live](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/gemini-transcribe-live) is generally available. Live transcription converts streaming audio to text in real time to deliver quick, reliable intermediate transcriptions for live conversations.

The `model_id` field in `GeminiAsrConfig` remains in preview. Leave `model_id` unset to use the default Gemini transcribe live model.

## September 30, 2026

Feature

Agent Assist offers [companion agent](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/companion-agent-overview) in General Availability (GA). Companion agent unifies real-time agent assistance into a single interface that operates in both **proactive** and **on-demand** modes:

  * **Proactive guidance** : Monitors live customer conversations to surface context-aware next-best-action recommendations and follow configured instructions.
  * **On-demand assistant (`StreamingReactiveCompanionSuggestions`)**: Enables human agents to ask natural-language questions in an interactive panel and receive streamed, source-cited answers grounded in conversation context.
  * **Tool execution and grounding** : Connects to [data store tools, OpenAPI tools, custom tools, and Grounding with Google Search](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/companion-agent-tools) to retrieve live data and automate tasks, with built-in human-in-the-loop confirmation for state-modifying actions.



Companion agent is available across supported Agent Assist [regions](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/regionalization) with default resource allocation and token [quotas](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/quotas#companion-agent).

## September 01, 2026

Feature

Agent Assist offers [Gemini Transcribe Live](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/gemini-transcribe-live) in preview, which converts streaming audio to text in real time to deliver quick, reliable intermediate transcriptions for live conversations.

## June 17, 2026

Feature

Agent Assist offers the following [UI module integrations with Agent Assist for Salesforce](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/aaforsalesforce-setup):

  * [Chat](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/aaforsalesforce-chat)
  * [Voice with Twilio Flex](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/aaforsalesforce-voice-twilio)
  * [Voice with Nice CXone](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/aaforsalesforce-voice-nice)
  * [Voice with Genesys CX Cloud](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/aaforsalesforce-voice-genesys)



## June 10, 2026

Change

Agent Assist offers [Proactive generative knowledge assist](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/pgka) V2 in GA. This version supports rich search context, multiple suggested queries, and granular control over triggering events.

## June 01, 2026

Feature

Agent Assist offers [summarization with custom sections 6.0](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/summarization-with-custom-sections) in GA. The 6.0 version is powered by `gemini-3.5-flash` and available in all Agent Assist [regions](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/regionalization).

Change

Agent Assist offers summarization autoevaluation with more rubrics for evaluating completeness. This update also explains the use of N/A in the overall performance view.

[Summarization autoevaluation](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/summarization-autoeval-metrics) is available in the following additional regions:

  * us-east1
  * northamerica-northeast1
  * eu-west1
  * eu-west2
  * eu-west3
  * eu-west4
  * asia-southeast1
  * asia-northeast1
  * asia-south1
  * australia-southeast1



## March 23, 2026

Feature

Agent Assist offers [Gemini Enterprise for Customer Experience tools for AI coach](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/tool-integration-for-ai-coach) in GA. These tools enable virtual agents to connect with external systems to retrieve, update, format, or analyze information.

## January 10, 2026

Change

Agent Assist offers [sentiment analysis version 3](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/sentiment-analysis) in GA. Sentiment analysis V3 analyzes individual messages with conversation context and can even analyze an audio stream to provide precise end user sentiment scores.

## January 05, 2026

Change

Agent Assist offers a [best practices guide](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/summarization-autoeval-bp) for summarization automatic evaluation.

## December 22, 2025

Feature

Agent Assist offers a UI connector to integrate with [Nice CXOne Voice](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/salesforce-voice-nice) for Salesforce. This integration provides agent suggestions for Salesforce customers using NICE CXOne for their voice channel.

## October 29, 2025

Feature

Agent Assist offers [summarization with custom sections 5.0](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/summarization-with-custom-sections) in GA. 5.0 is available in all Agent Assist [regions](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/regionalization).

## October 20, 2025

Feature

Agent Assist offers summarization automatic evaluation in GA. This feature assesses the quality of AI-generated summaries based on accuracy, completeness, and adherence. [Summarization autoevaluation](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/summarization-autoeval-metrics) is available in the following regions:

  * us-central1
  * us-west1
  * global



## October 09, 2025

Feature

[OpenAPI and Integration Connectors tools](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/tools) are generally available in Agent Assist. Google Cloud enables the use of this external API and data source to improve Agent Assist integrations.

Feature

Agent Assist offers [AI coach](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ai-coach-overview) in GA. AI coach automatically suggests responses to an agent during a customer service conversation. AI coach is available in all Google Cloud [languages](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/languages) and [regions](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/regionalization).

Feature

Agent Assist offers the following functions in addition to [generative knowledge assist](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/generative-knowledge-assist) features:

  * Apply [document and safety filters](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ka-filters).
  * [Configure Pub/Sub notifications](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/pubsub-notifications) for empty suggestions.
  * [Troubleshoot knowledge assist features](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/troubleshoot-ka).



## October 01, 2025

Deprecated

[Smart compose](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/smart-compose) is no longer in use and will be permanently removed in October 2025. Refer to [Generative smart reply](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/priv/generative-smart-reply) for an alternative.

## September 23, 2025

Feature

Agent Assist offers a bidirectional API for next-generation audio and multi-modal experiences in both Conversational Agents and Agent Assist. The [`BiDiStreamingAnalyzeContent` API](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/bidi-stream-api) facilitates the streaming of audio data and returns either transcripts or human agent suggestions to you.

## September 09, 2025

Feature

Agent assist offers [summarization automatic evaluation](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/summarization-autoeval-guide) in preview. This feature evaluates the quality of AI-generated summaries based on the following three metrics:

  * Accuracy
  * Completeness
  * Adherence



## August 21, 2025

Deprecated

[Article suggestion](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/article-suggestion) and [FAQ Assist](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/faq) are no longer in use and you can't create new conversation profiles for them. These two features will be permanently removed on April 1, 2026. Refer to [Generative knowledge assist](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/generative-knowledge-assist) for an alternative.

## July 28, 2025

Feature

Agent Assist offers the [Twilio UI module V3](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/twilio). This version provides an upgraded integration.

## July 11, 2025

Change

Google Cloud provides quotas for using Agent Assist APIs. Each feature uses specific APIs, which have their own [quotas](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/quotas).

## June 13, 2025

Feature

Agent Assist offers summarization with custom sections V4.0 in GA. [V4.0](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/summarization-with-custom-sections) uses gemini-2.0-flash and supports a concise summary for situation and action.

## April 25, 2025

Change

[Summarization with custom sections](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/summarization-with-custom-sections), [generative knowledge assist, and proactive generative knowledge assist](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/generative-knowledge-assist) are available in the following [regions](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/regionalization): 

  * northamerica-northeast1 (Montreal)
  * northamerica-northeast2 (Toronto)
  * europe-west4 (Eemshaven)
  * europe-west6 (Zurich)
  * asia-southeast2 (Jakarta)
  * me-west1 (Tel Aviv)



Feature

[UI Modules container V2](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules-container-documentation) uses a reactive display with dynamic panels and a unified feed of suggestions to ensure the most impactful suggestions and key tools are always accessible to an agent. This version also offers greater integration flexibility.

## April 11, 2025

Feature

Agent Assist offers a UI Connector with Salesforce to [integrate with voice conversations](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/salesforce-voice).

## March 19, 2025

Feature

Agent Assist offers Vertex extensions for [Build your own assist (BYOA)](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/priv/agent-coaching-extension) in preview. Enable BYOA to access remote APIs with Vertex LLM extensions.

Feature

Build your own Gen AI Assist is available in preview. [BYOA](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/build-your-own-genai-assist) is available in all customer engagement suite regions and offers the following:

  * Foundation models
  * Gemini access
  * New trigger events based on agent and customer messages



## March 14, 2025

Change

Agent Assist offers a new version of summarization with custom sections in preview. [Summarization with custom sections V4.0](https://cloud.google.com/gemini-enterprise-cx/agent-assist/summarization-with-custom-sections) uses gemini-2.0-flash and supports concise summary for situation and action.

## January 28, 2025

Feature

Customer Managed Encryption Key (CMEK) is available in GA for all Agent Assist features. [CMEK](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/cmek) lets you control details of your data encryption keys, view audit logs, and control key lifecycles.

## December 18, 2024

Feature

[Pub/Sub intermediate transcription](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/pubsub-intermediate-transcription) is available in preview. With this feature you can accomplish the following:

  * Show intermediate transcripts in your Agent Assist UI module.
  * Populate additional information to support audio integration.



## December 16, 2024

Feature

Agent Assist offers a native UI Connector with Genesys Cloud to [integrate with voice conversations](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/genesys-cloud-voice).

## December 13, 2024

Announcement

Agent Assist infobot offers support for new [languages](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/languages) in GA.

## November 21, 2024

Feature

[Summarization with custom sections V3.1](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/summarization-with-custom-sections) is generally available. V3.1 provides the following improvements on V3.0:

  * Higher quality summarizations
  * Improved latency



## November 13, 2024

Feature

Agent Assist offers a UI Connector with Salesforce to [integrate with chat conversations](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/salesforce).

## October 23, 2024

Feature

(Proactive) Generative knowledge assist offers [additional functions and supports more languages](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/generative-knowledge-assist).

## October 02, 2024

Feature

Agent Assist offers a native UI Connector with Twilio Flex to [integrate with voice conversations](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/twilio-siprec).

## October 01, 2024

Feature

Agent Assist offers Live transcription adaptation in preview, which [recognizes certain phrases more frequently than others](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/adaptation-model-guide) to improve transcription quality.

## September 26, 2024

Change

Agent Assist offers a new version of summarization with custom sections in preview. Summarization with custom sections V3.1 reduces latency and improves quality from V3.0.

## August 12, 2024

Change

Customer Manager Encryption Key support is available in preview [for all Agent Assist features in regionalized environments](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/cmek#limits), including all generative AI features.

## July 08, 2024

Change

Agent Assist offers a new version of summarization with custom sections in preview. Summarization with custom sections V3.0 reduces latency from V2.1.

## June 14, 2024

Feature

(Proactive) generative knowledge assist is generally available. 

  * Generative knowledge assist [provides answers to agent questions](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/generative-knowledge-assist#answer_questions_from_your_human_agents).
  * Proactive generative knowledge assist [automatically suggests questions an agent might ask and provides the answers](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/pgka).



## June 12, 2024

Feature

The Agent Assist integration backend's public [github repository](https://github.com/GoogleCloudPlatform/agent-assist-integrations/tree/HEAD/aa-integration-backend) includes a mechanism for [authentication customization and support for authenticating agents](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/backend-module-install#customize_the_user_authentication_method) with the following providers: Twilio, Genesys Cloud, and Salesforce.

## June 03, 2024

Feature

Agent Assist offers a native UI Connector with Twilio Flex to [integrate with chat conversations](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/twilio).

Feature

Agent Assist offers a native UI Connector with Genesys Cloud to [integrate with chat conversations](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/genesys-cloud-app).

## May 30, 2024

Feature

Agent Assist offers summarization with custom sections V2.1 as a GA feature. See the [Summarization documentation](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/summarization-with-custom-sections) for details.

## March 29, 2024

Change

Agent Assist offers version 2.0 of summarization with custom sections. Summarization with custom sections V2.0 offers the following changes to V1.0:

  * Handling of long transcripts
  * Handling of conversations between a human user and a virtual agent
  * Changed outputs of two predefined sections: Resolution and Customer satisfaction
  * Increased latency



## December 08, 2023

Feature

Agent Assist now offers Summarization with custom sections as a preview feature. Summarization with custom sections is optimized only for conversations between two humans and the predefined sections are identical to those in [Summarization V2 baseline](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/summarization-with-custom-sections).

## November 30, 2022

Feature

The Agent Assist [Smart Reply feature](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/smart-reply) now supports French (Canada) in addition to English (United states). See the [language support page](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/languages) for details.

## November 15, 2022

Feature

Agent Assist has launched backend modules as a GA feature. Backend modules is an out-of-the-box solution that provides an effective backend infrastructure, making integrating Agent Assist with your agent system faster and easier. See the backend modules [basics](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/backend-basics) and [integration guide](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/backend-module-install) for details.

Feature

The Agent Assist console is now GA. The console now also includes built-in workflow tutorials that walk you through creating a dataset, training and testing a model, and creating a conversation profile. Sample datasets and demo models are now provided as well. To see the new console tutorials, navigate to the [console](https://agentassist.cloud.google.com) and click **Get started** under the feature you'd like to test.

Feature

Agent Assist now supports [sentiment analysis](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/sentiment-analysis) of voice data as a private preview feature. For more information, see the Agent Assist [private features documentation](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/priv). To gain access to the private documentation, please contact your Google representative.

Feature

Agent Assist now supports CCAI Transcription as a GA feature. CCAI Transcription allows you to convert streaming audio data into text transcripts in real time, allowing you to implement Agent Assist features for use with voice data. See the [documentation](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/transcription) for details.

## September 01, 2022

Feature

Agent Assist now offers summarization in preview. Summarization allows you to automatically provide your agents with summaries after each conversation has ended. See the [summarization documentation](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/summarization-with-custom-sections) for details.

Feature

Agent Assist offers regionalized data residency. When you specify a region, your data-at-rest will be confined to the specified geographic region or location. See the [regionalization and data residency documentation](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/regionalization) for a list of supported regions and more information.

## July 12, 2022

Feature

Agent Assist now offers UI Modules as a public Preview feature. UI Modules are an out-of-the-box option for integrating Agent Assist features into your agent UI system. For more information, see the [UI Modules documentation](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/modules-overview).

## February 28, 2022

Announcement

Agent Assist is now GA. GA status applies to the following features:

  * [Article Suggestion](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/article-suggestion)
  * [Smart Reply](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/smart-reply)
  * [Agent Assist Simulator](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/simulator)
  * [Sentiment Analysis](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/sentiment-analysis)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
