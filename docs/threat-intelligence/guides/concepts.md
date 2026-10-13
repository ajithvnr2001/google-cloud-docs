---
url: https://docs.cloud.google.com/threat-intelligence/guides/concepts/
title: Key Concepts \u00a0|\u00a0 Google Threat Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:31:37.801172+00:00
---

# Key Concepts  |  Google Threat Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/threat-intelligence/guides/concepts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Threat Intelligence ](https://docs.cloud.google.com/threat-intelligence)
  * [ Guides ](https://docs.cloud.google.com/threat-intelligence/guides/concepts)



Send feedback 

#  Key Concepts Stay organized with collections  Save and categorize content based on your preferences. 

This document explains the core data structures and logic used by the Google Threat Intelligence API. To start calling the API, see the [Get Started](https://docs.cloud.google.com/threat-intelligence/guides/get-started) guide, and to see all the available methods, see the [REST API Reference](https://docs.cloud.google.com/threat-intelligence/reference/rest).

## Customer Profile

The Customer Profile is a structured data object stored within the `[projects.configurations](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations)` resource. It encapsulates the entity's characteristics used for threat matching.

A profile typically contains:

  * **Identity:** Company name, brands, and key persons.
  * **Assets:** Domains, IPs, and tech precences.
  * **Context:** Industry, geographic regions, and security considerations.



The system uses the customer profile to perform nuanced, context-aware semantic matching beyond keyword search.

## Findings vs. Alerts

The API distinguishes between raw detections and actionable incidents using two distinct resources:

### Findings

**Resource:** `[projects.findings](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.findings)`

A Finding is an immutable record of a **specific** threat detection event. It contains:

  * **Source Data:** The raw content (e.g., forum post body, file hash).
  * **Match Metadata:** Why it matched, severity, and confidence.
  * **Timestamp:** When the event was observed.



### Alerts

**Resource:** `[projects.alerts](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.alerts)`

An Alert is a mutable, stateful object that **groups one or more Findings**. It represents a security incident that requires investigation. Alerts are enriched with:

  * **Aggregated Context:** Summary of all related findings.
  * **Status:** Triage state (e.g., New, Triaged, Resolved).
  * **Severity:** Computed risk score based on the findings and relatedasset criticality.



## Threat Scenarios

Threat Scenarios organizes and groups relevant alerts together, and are the logical definitions that determine detection behavior.

Supported scenarios include:

  * **Data Leakage:** Identifying potentially sensitive data on external platforms.
  * **Initial Access Broker (IAB):** Detecting potential sale of network access.
  * **Insider Threats:** Detecting potential recruitment attempts and insider offerings.
  * **Technology Watch List:** Monitoring for mentions of specific technologies.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
