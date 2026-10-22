---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-rate-limits/
title: CRM API rate limits \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:53.638949+00:00
---

# CRM API rate limits  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-rate-limits/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  CRM API rate limits Stay organized with collections  Save and categorize content based on your preferences. 

The following sections explain the rate limits of the CRM API.

## APIs and your CRM

Contact Center AI Platform (CCAI Platform) call and chat adapters function within a Customer Relationship Manager (CRM) software. There are many benefits to this, including automatic case creation to record the details of interactions.

CCAI Platform is integrated through an application programming interface (API), which passes information from CCAI Platform into your CRM.

You may have other integrations already using APIs to connect to your CRM. Using an ecosystem of different apps and integrations tied together using the APIs can help drive important business objectives for your contact center.

## Limits

Each time CCAI Platform or any other application sends data to your CRM, it's referred to as an **_API call_**.

The specific CRM and level of licensing determine how many API calls you are allowed per day, as well as how many API calls you are allowed per minute. This is referred to as **_rate limiting_** *.

For example, you may have a Zendesk license that allows 400 API calls per minute and 2,500 calls per day. Some CRMs provide a dashboard that lets you to monitor usage over time to ensure integrations are running smoothly and that no one app is monopolizing your API call rate.

## Limits and CCAI Platform

The primary purpose of the CCAI Platform integration into your CRM is to record actions from calls and chats within case or ticket records. Each CCAI Platform activity that is tracked in the CRM (like contact search, case or ticket creation, and call logging) creates an API call.

This also means that if you exceed your rate limit within your CRM, you may experience calls and chats not creating cases/tickets.

Fortunately, CCAI Platform continues to create the commands to make new cases or tickets from calls and chats even if you have reached your API limit. They will queue in the system, and as soon as the CRM can accept more API calls, the queued cases or tickets will populate in your CRM.

To avoid case creation interference, ensure that you have the appropriate level of licensing to support all of your integrations, and monitor your API rate limit dashboards.

For Zendesk, CCAI Platform offers API batching to reduce the number of API calls made. Refer to [API Batching - Zendesk](https://docs.cloud.google.com/contact-center/ccai-platform/docs/zendesk#UUID-011d3721-e0ac-2084-9dc8-c4a83c0fc2a2) for more information.

**Note:** CCAI Platform does not limit the number of API calls you can request from our platform.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
