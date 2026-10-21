---
url: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/measure-how-long-security-analysts-take-to-close-or-raise-a-case/
title: Monitor case response and closure metrics \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:32:50.942976+00:00
---

# Monitor case response and closure metrics  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/measure-how-long-security-analysts-take-to-close-or-raise-a-case/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Monitor case response and closure metrics

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

**Note:** This document applies both to SOAR standalone customers and Google SecOps unified customers using the legacy cases experience. 

This document explains how to measure case handling time in Google Security Operations using dashboards. You can track how long it takes to complete case-related processes, with breakdowns by attributes, such as **stage** or **priority**.

The following example demonstrates how to create a dashboard table widget that displays the average case handling times, by case priority, for analysts working in the default environment:

  1. Go to **SOAR Dashboards**.
  2. Click  add **Add Widget**.
  3. In the **Widget Settings** dialog, enter **Case Handling Time** as the **Title** , and then choose a widget width.
  4. Under **Chart Type** , select **Table** (the default is **Pie Chart**).
  5. Configure the **Table** settings as follows:
     * **Number of** = `Cases`
     * **Calculate field** = `Handling avg time`
     * **Axis A** = `Environment`
     * **Axis B** = `Priority`
  6. Click **Create**. The new widget appears on the dashboard and shows the average time analysts take to handle cases in the default environment, grouped by case priority.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
