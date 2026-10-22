---
url: https://docs.cloud.google.com/gemini/enterprise/docs/core-assistant/
title: Core Assistant agent \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:46:38.904355+00:00
---

# Core Assistant agent  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/core-assistant/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Core Assistant agent Stay organized with collections  Save and categorize content based on your preferences. 

Core Assistant is the Google-provided ("Made by Google") agent that handles interactions when users talk to the Gemini Enterprise engine without specifying any other agent.

Core Assistant includes monitoring and observability for tracing and monitoring of operations with user interactions and agent activity. It provides comprehensive observability into execution flow, performance, and usage metrics.

The Core Assistant agent is available automatically with Gemini Enterprise.

**Note:** Made by Google agents aren't available in the Gemini Enterprise Frontline edition.

Key characteristics of Core Assistant:

  * **Google-managed** : Entirely maintained and managed by Google; you cannot edit its configuration or change the charts and data shown.
  * **Always available** : Automatically provisioned and runs out of the box for Gemini Enterprise agents.
  * **Access** : Viewable through the Google Cloud console.



Through Core Assistant, you can access two primary observability tabs with details of your AI operations: **Traces** and **Metrics**.

## Prerequisites

Before you begin using Core Assistant, ensure you have the following:

  * The [Gemini Enterprise Admin](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) role or Google Cloud console Gemini Enterprise User role.
  * An existing Gemini Enterprise app configured.
  * For **Traces** functionality, you must turn on OpenTelemetry traces and logs in your observability settings and have the Cloud Trace User role (`roles/cloudtrace.user`). For more information, see [Manage observability settings](https://docs.cloud.google.com/gemini/enterprise/docs/manage-observability-settings). *Note: The **Metrics** functionality is default ON and does not require manual configuration or trace enablement.*



## The Traces tab

The **Traces** tab in Core Assistant provides a chronological summary of trace records showing parent-child execution span details (`Agent to Tool`, `Invoke Agent`, and `Agent to Model` actions, including `execute_tool` and `invoke_connector` operations). These records help inspect runtime execution flows, inputs, outputs, and locate latent issues.

Traces inside Core Assistant persist for **30 days** and require OpenTelemetry traces to be turned on.

For a detailed breakdown of all the fields, visual workflows (graphs and timelines), and metrics logs display in the Traces tab, see [Access traces for agents](https://docs.cloud.google.com/gemini/enterprise/docs/access-traces-and-spans#access-traces-for-agents).

## The Metrics tab

The **Metrics** tab provides an operational overview dashboard summarizing sessions, count of agent invocations, traffic, error rates, and detailed connections of tools usage.

Metrics inside Core Assistant persist for **6 weeks** (42 days), are default ON, require no configuration, and incur no extra billing costs.

For a comprehensive breakdown of each metric dashboard (Overview metrics dashboard and connected Tools latency metrics), see [Access metrics for agents](https://docs.cloud.google.com/gemini/enterprise/docs/access-metrics#access-metrics-for-agents).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
