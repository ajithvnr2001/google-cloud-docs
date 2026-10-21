---
url: https://docs.cloud.google.com/chronicle/docs/detection/ueba-getting-started/
title: Identify unusual behavior and entity risk \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:09:34.291183+00:00
---

# Identify unusual behavior and entity risk  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/ueba-getting-started/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Identify unusual behavior and entity risk

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

Learn how to use the **Risk Analytics dashboard** to identify unusual behavior and understand the potential risk that entities pose to your enterprise. On systems that use role-based access control (RBAC), only users with global scope can access risk analytics. For more information, see [User roles](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-overview#user-roles). 

The Risk Analytics dashboard consists of the following sections:

  * **Behavioral Analytics** : lists entities according to [Google Security Operations Entities risk scores](https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-dashboard#entity_count_risk_score_and_entities_table) risk scores.
  * **[Watchlist](https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-dashboard#add_a_watchlist)** : lists entities according to internal enterprise risk calculations. 



A [Risk Calculation window](https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-dashboard#adjust_the_risk_calculation_window) at the top right changes the calculated risk score displayed in the Risk Analytics dashboard. You can change this setting depending on the type of attack you are searching. For example, brute force attacks are more visible by setting the **Risk Calculation Window** to **24 Hours**. To see long-term attack, set the **Risk Calculation Window** to **7 days**. 

You can view historical risk scores by selecting a specific date and time in the date selector next to the **Risk Calculation Window**. This displays the entity risks calculated for the 24-hour or 7-day window, ending at the chosen date and time.

## Before you begin

To navigate to the Risk Analytics dashboard, follow these steps:

  1. In the navigation bar, click **Detection**.
  2. From **Detection** , click **Risk Analytics**.



## Behavioral Analytics

Behavioral Analytics consists of:

The **Behavioral Analytics** page consists of:

  * **Summary Metrics** section: a top-level view of the **Risk Analytics** dashboard that lets you investigate risk entities based on Google SecOps entity risk modeling. You can view up to 10,000 entities in the summary.
  * **Entities** : a table that complements the existing risk score used for tracking an entity's risk over time, as a metric for detection use cases, and as investigative context. Also called _entity risk metrics_ , an entity is a contextual representation of elements in your environment. Examples for entities are user accounts, servers, laptops or phones. You can drill down to each entity by clicking the entity name. This will take you to the **Entity Analytics** page.



For more information about entities, see [Logical objects: Event and Entity](https://docs.cloud.google.com/chronicle/docs/event-processing/udm-overview#logical_objects_event_and_entity). For more information on how risk scores are calculated, see [Risk score calculation](https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-overview#risk_score_calculation).

## Entity Analytics

The **Entity Analytics** page consists of an **Event range** window at the top right corner, a **Findings Timeline** section, and a detailed **Findings** table. 

### Select a time range to analyze risks

  1. In the **Event range** window, select a time range of up to 90 days ("Last 3 months").
  2. For **Selection** , click **View analytics for Selection**. This opens a sidebar that shows you the analytics associated with this entity within the selected time range. Each analytic displays an aggregate of all the analytic values within the time range. 
  3. Click **View more** to open the corresponding Alerts or Detection view. When detected, an analytic includes a list of related alerts and detections that can be examined further.



### View composite detections

The **Detections** table displays all detections for an entity that occurred within the selected time range. An alert is a [composite detection](https://docs.cloud.google.com/chronicle/docs/detection/composite-detections) when:

  * The **Inputs** column shows **Detection** as a source.

  * The **Detection type** column displays an **Alert** or **Detection** label with a number next to it (for example, `Alert (3)`).




This indicates that a detection, or a chain of detections, triggered the alert, rather than raw events or entities alone.

You can view and analyze these underlying detections in the **Detections** table by using the following features:

  * Expand rows to view nested detections, associated event data, and related entity information.

  * Customize your view by using the column manager to select and arrange columns in the table.




For more information, see [Investigate an alert](https://docs.cloud.google.com/chronicle/docs/investigation/investigate-alert).

## Use Cases

Here are a few use cases for the Risk Analytics dashboard.

### Use case 1: High download volume

A high download volume of data poses the risk of confidential information leaking. Google SecOps calculates high risk score numbers for entities with high download volumes.

### Use case 2: Suspicious number of failed login attempts

Suspicious numbers of failed login attempts indicate that a hacker or malware is attempting to gain access to a user account. Google SecOps will calculate high risk score numbers for entities with suspicious numbers of failed login attempts. However, if this is done internally, as part of penetration testing, you can [modify the entity risk score](https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-dashboard#modify_an_entity_risk_score).

### Use case 3: Dialog message impersonating Google

A dialog message impersonating Google asking to update the Chrome Browser is attempting to gain access to user accounts. Google SecOps calculates high risk score numbers for entities where these dialog messages are detected in the code.

## What's next

  * [Modify an entity risk score](https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-dashboard#modify_an_entity_risk_score)
  * [Investigate an asset](https://docs.cloud.google.com/chronicle/docs/investigation/investigate-asset)



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
