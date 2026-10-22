---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/conversation-history/
title: Conversation history \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:37.548336+00:00
---

# Conversation history  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/conversation-history/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Conversation history Stay organized with collections  Save and categorize content based on your preferences. 

You can use the conversation history interface to browse the conversations saved by the agent application.

## Open conversation history

To open the conversation history:

  1. Open the agent builder.
  2. Open agent preview.
  3. Click the conversation history button in the agent preview title bar.



## Redaction

If Data Loss Prevention (DLP) [redaction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#redactionconfig) is enabled, it is applied before any conversation data is written to storage. This ensures that all persisted transcripts and interaction data are fully redacted at the source.

## How data is stored

Conversation data is stored _long-term_ in the following ways:

  * **Customer-owned storage** : This is data that you opt-in configure for storage in a system that you have access to. This data is stored within your Google Cloud boundary, giving you complete IAM control. The following systems are used: 
    * BigQuery for custom analytics.
    * Cloud Storage for raw audio recordings.
    * Cloud Logging for service logs.
  * **Google-managed storage** : This is data that is stored and managed by Google that you do not have access to. This data contains redacted conversation transcripts, tracing metrics (tool failure, tool latency, etc.), conversation metrics (total sessions, escalation rate, turns per session, etc. used by the [monitor dashboard](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/monitor)), and AI analysis metrics (AI aversion, abandonment rate, and [conversation outcomes](https://docs.cloud.google.com/contact-center/insights/docs/qai-basics#conversation_outcome)). The following systems are used: 
    * Spanner: Single-tenant if CMEK is used, multi-tenant otherwise, used by CX Agent Studio and CX Insights to surface conversation history.
    * BigQuery: Single-tenant instance used by CX Insights for agent performance monitoring.



Conversation data is stored _short-term_ in the following situations:

  * A memcache is used for active session management and metadata Time-to-live (TTL) is 30 minutes, after which time the data is deleted.
  * A Text-to-Speech (TTS) Memstore cache is used for voice agents to optimize output latency. TTL is 1 hour.



## Settings for controlling conversation data storage

There are several settings which allow you to control how conversation data is stored:

  * **Log your customer conversations** : If disabled, all types of long-term conversational data except BigQuery data (which you can disable separately) are disabled. This applies to both CX Agent Studio and CX Insights. Disabling this integration will impact the monitor dashboard, as no data will be stored to populate the dashboard. The data is logically isolated, regionalized to match your deployment, and retained for a configurable period (default 1 year, maximum 2 years).
  * **Improve agent performance by sharing conversation data** : This setting permits the sharing of operational metrics and system call traces with Google to accelerate troubleshooting and improve system reliability. Google enforces a strict policy that customer content shared using this toggle is _never_ used to train Google's production machine learning models.
  * **Export logs to BigQuery & Audio recording:** Routes raw interaction data and audio to your designated, self-managed Google Cloud storage resources.
  * **Enable Cloud Logging:** Streams service and operational logs to your Cloud Logging environment.
  * **Enable redaction:** Activates the DLP engine to automatically identify and scrub sensitive data before persistence.



## Google access to conversation data

Google support and engineering personnel may have controlled, just-in-time access to Google-managed operational data for critical debugging and system maintenance. However, if **Log your customer conversations** is disabled, conversational data does not exist in any Google-owned persistent storage to be accessed. Only active session metadata andTTS cache is briefly held in a 30-60 minute memcache to facilitate the live call. Customer-owned resources remain entirely under your exclusive IAM control.

Data protection is enforced through multiple layers:

  * **Redaction:** DLP redacts sensitive data before any write occurs.
  * **Access Transparency (AxT):** All Google personnel access to conversation data is logged and compliant with Access Transparency controls, allowing customers to request and review audit logs.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
