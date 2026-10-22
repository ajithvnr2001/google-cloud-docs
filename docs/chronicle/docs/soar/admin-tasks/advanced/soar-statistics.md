---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/soar-statistics/
title: Manage statistics \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:55.569362+00:00
---

# Manage statistics  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/soar-statistics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage statistics

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document explains how to configure statistics tracking in Google SecOps. You can define which case and event properties (each identified by a **System Name**) are tracked for statistical analysis. By configuring these properties, you control what metadata is processed to generate case statistics, helping analysts understand trends and distributions of specific properties (such as `DeviceProduct` or `DestinationPort`) involved in security alerts.

## Add statistics

To add a new property to statistics tracking, follow these steps:

  1. Go to **SOAR Settings** > **Data Configuration** > **Statistics**.
  2. Click add**Add**.
  3. In the **Add Statistics** dialog, select a property from the **System Name** drop-down menu.
  4. Click **Save**.



## Practical application

Configuring statistics lets you optimize operations and identify trends:

  * **SOC Optimization:** Tracking common properties like `DeviceProduct` helps the SOC understand which security tools are generating the most alerts.
  * **Troubleshooting:** Tracking properties like `CategoryOutcome` can help identify if certain connectors are constantly failing or returning specific statuses.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
