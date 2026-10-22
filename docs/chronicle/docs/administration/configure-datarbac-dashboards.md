---
url: https://docs.cloud.google.com/chronicle/docs/administration/configure-datarbac-dashboards/
title: Control access to dashboards \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:16.842267+00:00
---

# Control access to dashboards  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/administration/configure-datarbac-dashboards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Control access to dashboards

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how Google Security Operations administrators can assign scopes to dashboards. The Dashboards feature of Google Security Operations is built from charts populated using YARA-L 2.0 properties. Scopes assigned to a user determine the results that appear on a user's dashboard. Data RBAC implementation may vary based on the data source in the chart query. For more information, see [Events, entity graph, and IoC matches](https://docs.cloud.google.com/chronicle/docs/reports/native-dashboards#events_entity_graph_and_ioc_matches).

To understand how data RBAC works, see [Overview of Data RBAC](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-overview).

## Before you begin

  * Review the core concepts of data RBAC, including access types, user roles, the function of labels and scopes, and the impact of data RBAC on Google SecOps features. For details about data RBAC, see [Data RBAC overview](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-overview).

  * Onboard your Google SecOps instance. For more information, see [Onboard a Google SecOps instance](https://docs.cloud.google.com/chronicle/docs/onboard).

  * Confirm you have the [required roles](https://docs.cloud.google.com/chronicle/docs/onboard#configure_data_access_control) to manage Identity and Access Management permissions.




### Grant user access to Dashboards

To grant a user or group access to Dashboards, follow these steps:

  1. In the Google Cloud console, click **IAM** > **Grant Access**.

  2. In the **New principals** field, enter the email address for the user or group. To simplify management, we recommend to grant roles to Google groups, not individual users.

  3. In the **Select a role** list, search for "Chronicle SIEM", and then select the required predefined or custom role. For example, **Chronicle SIEM Restricted Viewer**.

  4. If you assigned a scoped role (like **Restricted Viewer**), you must also assign the user to a specific Log Scope to filter their data view. For more information, see [Configure data access control using Log Scopes](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-overview#access-control-with-scopes-labels).

  5. Click **Save**.




The user now has the granted permissions for all dashboards they're authorized to see within the project.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
