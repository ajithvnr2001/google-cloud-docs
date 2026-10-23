---
url: https://docs.cloud.google.com/recaptcha/docs/monitor-agents/
title: Monitor agent traffic \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:43:50.891273+00:00
---

# Monitor agent traffic  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/monitor-agents/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Monitor agent traffic Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to use the Google Cloud Fraud Defense (the evolution of reCAPTCHA) **Agent overview** dashboard to monitor and analyze agentic traffic on your site.

The **Agent overview** dashboard helps you visualize how AI agents and automated tools interact with your site. By distinguishing legitimate and verified agents from unverified or potentially abusive ones, you can refine your security policies without disrupting valuable automated traffic like shopping assistants or search indexers.

**Note:** Fraud Defense continually expands its identification infrastructure. As the list of recognized agents grows, your dashboard automatically captures more data, providing increasingly granular visibility into the automated traffic on your site. If your dashboard shows **No verified agent traffic detected yet** , your traffic does not originate from the tracked list of verified identities.

## Agent verification methods

Fraud Defense classifies agentic traffic using the following verification methods:

  * **Web Bot Auth (WBA):** A cryptographic standard that augments or replaces conventional IP-based verification. WBA allows automated agents to cryptographically sign their requests, proving their identity independently of their source IP address.
  * **User-Agent and IP-based agent identity:** A method in web security and fraud defense for identifying and verifying automated agents (like bots, crawlers, and scripts) by examining two primary pieces of information in their HTTP requests: the User-Agent string and the source IP address.



## The Agent overview dashboard

The **Agent overview** dashboard provides a summary of agentic activity over a selected time period. It includes the following components:

  * **Performance scorecards:** High-level metrics that summarizes the total volume of verified and suspected agent sessions, as well as the number of distinct verified agents detected.
  * **Traffic chart:** A time-series chart that displays session volume. You can use chart toggles to switch between the following views: 
    * **Verified agents:** A stacked bar chart that breaks down traffic by specific, confirmed agent identities. This view shows the top individual agents and the remaining agents in the **Other verified agents** category.
    * **Suspected agents:** An aggregated view of automated traffic that exhibits agentic behavior but lacks official verification.
  * **Time filters:** Options to view data for the **Last 30 days** or **This month**.



## Understand agent metrics

To help you analyze your traffic, the dashboard categorizes activity using the following definitions:

  * **Verified agent sessions:** The total number of sessions initiated by officially verified AI agents. A session represents a single Fraud Defense-protected interaction. Fraud Defense confirms the identity and source of these agents, for example, using cryptographic techniques, to ensure they are accountable. Monitoring this metric helps you track the volume of trusted automation acting on behalf of users or services.
  * **Suspected agent sessions:** The total number of sessions initiated by suspected AI agents. These are sessions that self-declare as agents, such as through HTTP headers, or exhibit agentic behavior, but whose identity can't be officially verified by Fraud Defense.
  * **Unique verified agents:** The count of distinct agent identities verified by Fraud Defense. Identity verification ensures agents are accountable and helps you distinguish specific, legitimate tools from generalized automated abuse.



## What's next

  * [Monitor reCAPTCHA keys](https://docs.cloud.google.com/recaptcha/docs/monitor-keys).
  * [Interpret assessments for websites](https://docs.cloud.google.com/recaptcha/docs/interpret-assessment-website).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
