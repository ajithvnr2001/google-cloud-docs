---
url: https://docs.cloud.google.com/service-health/docs/incident-communication/
title: Google Cloud incident communication \u00a0|\u00a0 Personalized Service Health \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:17.386105+00:00
---

# Google Cloud incident communication  |  Personalized Service Health  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-health/docs/incident-communication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Personalized Service Health ](https://docs.cloud.google.com/service-health/docs)
  * [ Guides ](https://docs.cloud.google.com/service-health/docs/overview)



Send feedback 

#  Google Cloud incident communication Stay organized with collections  Save and categorize content based on your preferences. 

This document outlines Google Cloud's approach to communicating incidents, including the roles of the following primary communication channels: Personalized Service Health (PSH) and the public Google Cloud Service Health (CSH) dashboard.

## Where to look for incident communications

Google Cloud provides two channels for incident communication, each with a different purpose:

  * **Personalized Service Health (PSH):** This is your primary source for service disruptions relevant to you. It provides a personalized view tailored to the specific Google Cloud products you use. We recommend integrating Personalized Service Health into your incident response process as a critical corroboration signal.

To avoid paging an on-call engineer for every Personalized Service Health event, integrate Personalized Service Health incident visibility into your team's dashboards and tools. This practice helps operators quickly determine if a suspected issue is related to a Google Cloud service disruption. [Learn more about PSH](https://docs.cloud.google.com/service-health/docs/overview).

  * **Google Cloud Service Health (CSH):** This is Google Cloud's public-facing status page, available at [status.cloud.google.com](https://status.cloud.google.com/). Google Cloud Service Health requires no login and serves as an at-a-glance health check for the entire platform, and is used to communicate broad severe incidents or when PSH itself is unavailable.




![A diagram comparing PSH to CSH communication channels. The diagram shows emerging incidents,
confirmed incidents, and broad severe incidents going to Personalized Service Health.
The diagram shows broad severe incidents going to Cloud Service Health. Listed under
Personalized Service Health, is Dashboard, API, and Cloud Logging. Listed
under Cloud Service Health is Dashboard and RSS Feed.](https://docs.cloud.google.com/service-health/images/comparison-psh-csh.png)

## Our disclosure strategy and recommendations

Deciding what to share, and where, is not an arbitrary process. It is a formal, systematic discipline based primarily on an incident's scope. The intent of these channels is to provide maximum visibility for Broad Severe Incidents while reducing the noise of incidents that are irrelevant.

  * **For Broad Severe Incidents:** Broad-scoped incidents—those impacting a large percentage of projects or widespread across multiple regions—are communicated using Google Cloud Service Health (CSH). These incidents are also communicated to affected customers using Personalized Service Health. This helps ensure the message reaches the widest possible audience for the most critical events.

  * **For other Confirmed Incidents:** For issues with a more limited scope, such as those impacting a single location, zone, or a smaller subset of projects, we will communicate relevant incidents to customers using Personalized Service Health. We aim to be comprehensively transparent, which means Service Health makes available all potentially relevant events for your services. If you need a more focused event feed, Service Health offers tools to filter and fine-tune the events that are passed through your alerts and automated workflows.

    * **Recommendation:** Configure alerts to only focus on the most critical Google Cloud services and locations, or to trigger only on events with a relevance of "Related" or "Impacted." See examples of [how to filter and fine-tune alerts](https://docs.cloud.google.com/service-health/docs/example-alerting-policies).



### Fallback Strategies for Personalized Service Health unavailability

Personalized Service Health depends on core services, such as Identity and Access Management for authentication. In a severe, widespread disruption, the very services you need to sign in might be affected.

We recommend the following fallback strategy:

  * **For manual processes:** Your runbooks should direct operators to the Google Cloud Service Health dashboard at [status.cloud.google.com](https://status.cloud.google.com/) in the event they can't access the Personalized Service Health dashboard.

  * **For automated systems:** Use the [**Service Health Status API**](https://docs.cloud.google.com/service-health/docs/service-health-disruption) to programmatically detect if Personalized Service Health is having a problem. If it is, your systems can then fall back to ingesting the public [**CSH RSS Feed**](https://status.cloud.google.com/en/feed.atom) for continued programmatic updates.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
