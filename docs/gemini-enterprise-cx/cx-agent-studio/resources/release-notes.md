---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/resources/release-notes/
title: CX Agent Studio release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:47:21.798020+00:00
---

# CX Agent Studio release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/resources/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  CX Agent Studio release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Customer Experience Agent Studio. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/cx-agent-studio-release-notes.xml) directly. 

## October 12, 2026

Feature

[Custom voices](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/voice) are now available for voice agents.

Feature

[Modular components](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/instruction#modular-components) are now available to help create a single set of agent instructions that can handle multiple channels (telephony, web, API) and multiple modalities (voice, text).

## September 24, 2026

Feature

[Supervisor agents](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/guardrail#supervisor) are now available to monitor the performance of the active agent.

Feature

[Composite model](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/agent#composite-v1) is now available for optimizing model usage in enterprise voice agents.

Feature

[WhatsApp and Instagram](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/deploy/whatsapp) deployment options are now available.

Feature

[SecureCo deployment option](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/deploy/secureco) is now available.

Feature

[Agent-to-agent protocol tools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/a2a-protocol) are now available to communicate and coordinate tasks across remote agents.

Feature

[Agent as a tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/agent-as-tool) is now generally available.

## July 01, 2026

Feature

You can now use [traffic splitting for deployments](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/deploy/traffic-split).

## June 08, 2026

Feature

You can now [import and export evaluation data](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/evaluation#import_and_export).

## May 26, 2026

Deprecated

Gemini 2.0 models are scheduled for deprecation on June 1st. Users will be automatically upgraded to Gemini 2.5 models on or after May 29th if they haven't manually updated. This applies to "flash lite" and "flash" variants. Quotas will also be adjusted automatically.

Feature

The following new tools are available

  * [Google Maps tools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/google-maps)
  * [Confluence tools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/confluence)
  * [Jira tools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/jira)
  * [SharePoint tools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/sharepoint)



## May 08, 2026

Feature

You can now define [custom HTTP headers](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/mcp#custom-header) for MCP tools.

## April 20, 2026

Feature

You can now update settings for fallback behavior (error handling) in [agent application settings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/agent#agent-application-settings).

## April 17, 2026

Feature

You can now use [agents as tools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/agent-as-tool).

Feature

You can now execute tools either [synchronously or asynchronously](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool#execution-type).

Feature

The gemini-3.1-flash-live model is the new primary model ID for Audio-to-Audio (A2A), replacing the legacy gemini-3-flash-native-audio name to align to GDM naming convention. A dismissal banner will now appear in the console for affected projects to guide users through this change.

## April 13, 2026

Feature

You can now create static and dynamic [variables](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/variable).

## March 31, 2026

Feature

You can now create [rich response widgets](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/rich-response-widget) for rich, interactive UI elements in your user interface.

## March 27, 2026

Feature

Users can now filter conversation history by source (Simulator, Live, Eval) directly in the console to improve auditing and debugging.

Feature

Added the ability to export specific application versions through the `ExportAppRequest` API.

Change

Upgraded the Evaluation UI with "Naive Replay" modes for Golden Results, custom expectation tagging, audio recording for golden user entries, and enhanced error insights.

Change

Improved speech endpointing and fault tolerance on background noises. Also implemented a mechanism to recover the conversation from false-positive barge-in.

Change

Improved stability and reduce latency for Python code execution.

## February 04, 2026

Announcement

**Customer Experience Agent Studio is Generally Available**

Customer Experience Agent Studio (CX Agent Studio) is now Generally Available (GA). This unified platform, powered by Gemini, simplifies the creation of high-quality customer experience agents. This launch includes agents-building-agents capabilities, featuring "Start with AI," which lets developers instantly generate a starter agent and tools by providing documents and high-level instructions. This launch also delivers multimodal excellence, combining high-fidelity native audio models for natural voice personas with an out-of-the-box configurable chat messenger that supports rich multimodal interactions and customizable widgets. CX Agent Studio provides a secure, enterprise-ready environment to rapidly build, improve, and monitor your AI workforce.

**Capabilities:**

  * **Start with AI** : Accelerate development by using generative AI to build a starter agent and associated tools automatically. Simply provide your existing documentation and a set of instructions, and the platform handles the initial setup.
  * **Configurable chat messenger** : Deploy a fully functional, web-based client "out of the box" that supports text, voice, and multimodal interactions.
  * **Rich content widgets** : Customize the user experience with configurable widget templates (including product carousels, order trackers, and quick actions) to fit your brand needs.
  * **Easy deployment** : Embed the messenger into your web or mobile application with a simple HTML snippet generated directly from the **Deploy** tab.
  * **Flexible authentication** : Secure your agent with built-in support for both Token Brokers (service account-based) and OAuth 2.0 (user-based) authentication flows.
  * **Native audio models** : Create natural, brand-specific voice personas with high-fidelity audio models (powered by Chirp 3) designed to handle complex conversations with ease.
  * **Enterprise connectors** : Seamlessly integrate with essential business tools using pre-built connectors
  * **Enterprise-grade security** : Ensure that your data remains secure with robust identity management and compliance standards.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
