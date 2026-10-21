---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/abandon/
title: Customer abandoned details \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:24.576847+00:00
---

# Customer abandoned details  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/abandon/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Customer abandoned details Stay organized with collections  Save and categorize content based on your preferences. 

Call and chat sessions can be considered abandoned if they are terminated within a specified number of seconds from their creation.

You can configure these settings in the CCAI Platform portal by going to **Settings** > **Operation Management** and navigating to the **General** section then **Customer Abandoned Details** subsection.

## Abandoned call settings

**Ignore and exclude short abandoned call in metrics:** Abandoned calls will not affect monitoring metrics if abandoned within a certain amount of time. This removes those calls from the dashboard but they will show in reports. The following example of a chat dashboard for which areas of the dashboard will be impacted by this setting.

**Note:** With the interaction-based data model, only the setting for the time threshold will be respected since short abandoned calls don't show in dashboard data.

## Abandoned chat settings

**Ignore and exclude short abandoned chat in metrics:** Abandoned chats will not affect monitoring metrics if abandoned within a certain amount of time. This removes those calls from the dashboard but they will show in reports.

**Note:** With the interaction-based data model, only the setting for the time threshold will be respected since short abandoned calls don't show in dashboard data.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
