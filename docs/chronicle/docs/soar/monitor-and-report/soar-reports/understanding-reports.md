---
url: https://docs.cloud.google.com/chronicle/docs/soar/monitor-and-report/soar-reports/understanding-reports/
title: Explore legacy SOAR reports \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:19:49.670939+00:00
---

# Explore legacy SOAR reports  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/monitor-and-report/soar-reports/understanding-reports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Explore legacy SOAR reports

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

**Caution:** For all Google Security Operations instances provisioned after August 6, 2025, you can no longer use Looker for SOAR Reports in Google SecOps tenants. Use [Dashboards](https://docs.cloud.google.com/chronicle/docs/reports/native-dashboards) instead. 

This document explains the role of reports in Google Security Operations and how they can be used to track performance, justify investments, and maintain transparency. Reports are valuable for demonstrating Return on Investment (ROI) to upper management, ensuring accountability to customers, and keeping colleagues informed. They also provide clear, data-driven insights that support better decision-making. 

For a comprehensive reference of the data fields used for report mapping, see [Siemplify Search Everything database](https://docs.cloud.google.com/chronicle/docs/reference/soar-bq-schema-reference). 

Google SecOps provides analysts with predefined reports and the option to create custom ones. You can export and import reports to other platforms. 

The predefined reports include:

  * **Management – SOC Status** : A high-level overview of security operations for leadership.
  * **Management – Closed Cases** : A summary of resolved cases for performance tracking.
  * **Tier 1 – Open Cases** : A view of ongoing cases for Tier 1 analysts.
  * **ROI – Analysts Benchmark** : Metrics for evaluating analyst productivity and ROI.



## Manage and work with reports

You can generate, schedule, customize, and manage reports in Google SecOps to monitor SOC performance and demonstrate ROI. 

### Generate a report

  1. Go to **Dashboards & Reports > SOAR Reports.**
  2. Click **Generate** under the **Generate Report** column. 
  3. In the **Generate report** dialog, select one or more of the following: **Environments** , **Time Frame** , **File type** (PDF or Word). 
  4. Click **Download**.  




### Schedule a report

  1. Select the report you want to schedule.
  2. Select the **Scheduler** tab and click  add **Add**.   

  3. In the **New Schedule** dialog, click the **Enable** toggle to turn on scheduling and enter the required information. 
  4. Click **Save**.



### Add a new report

  1. Click  add  **Add new template**. 
  2. In the **New report template** dialog, enter a name, and select a **Category** from the menu.
  3. Click **Create**.



The new report appears in the list of reports.

### Edit a report

  1. In the list of reports, select the report you want to edit.
  2. Select the **Edit** tab and click  add **Add**.
  3. Choose a format for your report: **Editor** , **Pie Chart** , **Table** , or **Vertical Bar**. A dialog appears based on the selected format. 
  4. Enter the required information.
**Note:** When you select **Alerts** or **Cases** , it affects the available options in other fields. For example, if you choose the **Pie Chart** format, the report is based on alerts from products where the case was closed as **malicious** and the root cause was an **external attack**.
  5. Click **Save**.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
