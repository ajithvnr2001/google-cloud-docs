---
url: https://docs.cloud.google.com/chronicle/docs/soar/monitor-and-report/soar-dashboards/dashboard-overview/
title: Legacy SOAR dashboards overview \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:19:23.259387+00:00
---

# Legacy SOAR dashboards overview  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/monitor-and-report/soar-dashboards/dashboard-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Legacy SOAR dashboards overview

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document describes the **SOAR Dashboards** page in Google Security Operations, how you can manage these dashboards, and provides an overview of specified data through the dashboard, including the various widgets. These widgets can show data for any specified SOC environment or case occurrence time. A dashboard can hold up to 12 widgets, which display data in formats, such as pie charts, bars, and tables. To display data related to your SOC status, you can [add SOAR dashboard widgets](https://docs.cloud.google.com/chronicle/docs/soar/monitor-and-report/soar-dashboards/add-dashboard-widgets). 

### Monitor activity with predefined dashboards

Google SecOps provides the following predefined, customizable dashboards to help you monitor and report SOC activities: 

  * **Playbooks dashboard** : Overview of playbook performance, including overall status, distribution, alert handling, and runtime metrics.
  * **SOC Status** : Overview of the SOC's current state, highlighting important metrics for cases, alerts, incidents, and analyst activities.



## Customize dashboards by data

You can customize a dashboard's display data by grouping widgets based on criteria, such as:

  * Analysts or playbooks associated with the case
  * Products or involved entities
  * Important or unimportant cases

**Note:** Dashboard data automatically refreshes every five minutes.

You can filter the displayed data by applying built-in filters, such as tags, case status, case priority, case stage, and case close reasons.

**Note:** Simulated alerts aren't included in the dashboard data.

### Use-case: Add a new widget to a new dashboard

This section provides the steps for adding a new widget to a new dashboard. The widget provides a pie chart, (default format) showing the top five products that contribute to attacks across all environments in the last six months. This presentation is ordered by the number of attacks in descending order. No filters are applied in this example. 

  1. Go to **Dashboards & Reports** > **SOAR Dashboards**. 
  2. Click  filter_alt  **Filter** and set the time to **Last 6 Months** and the environment as **All Environments**.
  3. Click  keyboard_arrow_down  **View all dashboards** and select  add  **Create New Dashboard**. 
  4. Enter `Attacks` as the new dashboard name and click **Create**. 
  5. In the new dashboard, click  add  **Add**. 
  6. In the **Widget Settings** dialog, enter `Top 5 Attacks by Products` as the title. 
  7. Select **Widget Width**. 
  8.   9. In the data display, **Pie Chart** is set by default. Keep this setting.
  10. Configure the **Pie Chart** fields as follows: 
     * **Number of** : Alerts 
     * **Calculate field** : Count 
     * **Group by** : Product 
     * **Number of Results** : 5 
     * **Order by** : Descending 
  11. Click **Save**.



The new widget is added to the dashboard as **Attacks**.

The pie chart displays the top five products associated with attacks across all environments in the last six months.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
