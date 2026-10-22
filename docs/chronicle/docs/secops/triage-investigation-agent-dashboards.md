---
url: https://docs.cloud.google.com/chronicle/docs/secops/triage-investigation-agent-dashboards/
title: Monitor alerts on the Triage Agent dashboard \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:43.769405+00:00
---

# Monitor alerts on the Triage Agent dashboard  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/secops/triage-investigation-agent-dashboards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Monitor alerts on the Triage Agent dashboard

Supported in:

Google SecOps 

The Triage and Investigation Agent (TIN) autonomously investigates security alerts to determine if they are true or false positives. Google SecOps integrates TIN operational data into dashboards. This integration provides critical visibility into the agent's investigations, helping you evaluate its effectiveness and understand its impact on your security posture. Additionally, these dashboards provide a clear way to monitor security token consumption for billing purposes and evaluate the value provided by the agent.

**Note:** You must have the `chronicle.investigations.settings` permission to manage agent configurations.

## Key metrics

By integrating TIN data into dashboards, you can monitor the following:

  * **Operational efficacy** : View the types of alerts the agent investigates and the final verdicts (true positive or false positive) it reaches.
  * **Efficiency gains** : Track metrics such as the time saved by using the agent for autonomous investigations.
  * **Usage monitoring** : Monitor your TIN usage to understand the value it provides to your security posture.



For more information about YARA-L 2.0 query dashboard examples for these metrics, see [Triage and Investigation Agent dashboard examples](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard#triage-investigation-agent).

## Curated dashboard for TIN

Google SecOps provides a curated dashboard that features several preset charts to track agent performance and user satisfaction. Each chart includes interactive options to help you explore the underlying data. You can export the dashboard data to a JSON file or download a report in CSV, PDF, and PNG formats. 

For more information about exporting and importing dashboards, see [Import or export a dashboard](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards#import-export-dashboards) and [Download reports](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards#download_reports).

To access this dashboard, select **Triage and Investigation Agent Metrics** from the dashboards list.

**Note:** You can view the metrics on this dashboard only if you have global data access. If you don't have the required permissions, you can see the dashboard listed but the charts display empty results. 

For more information about dashboards and the available filters, see [Manage dashboards](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards) and [Dashboard filters](https://docs.cloud.google.com/chronicle/docs/reports/native-dashboards-filters). 

### Curated dashboard details

The **Triage and Investigation Agent Metrics** curated dashboard displays the following sections:

  * Gemini investigation volume
  * Gemini investigation volume by trigger type
  * Gemini disposition trends
  * User feedback metrics
  * Token usage metrics



Each of these sections includes multiple charts that show related metrics.

#### Gemini investigation volume

  * **Gemini investigations** : Displays the number of completed Gemini investigations.

This section includes separate charts for hourly, daily, weekly, and monthly views.

  * **Daily number of investigations per alert type** : Breaks down the number of daily Gemini investigations by alert type.




#### Gemini investigation volume by trigger type

  * **Gemini investigations by trigger type** : Compares manually triggered and automatically triggered investigations.

This section includes separate charts for hourly, daily, weekly, and monthly views.




#### Gemini disposition trends

  * **Dispositions by day** : Tracks daily counts of true positive and false positive investigation verdicts.



#### User feedback metrics

**Note:** This section tracks user feedback provided through the  thumb_up  and  thumb_down icons.

  * **Disposition feedback** : Tracks user feedback for final investigation verdicts.
  * **Investigation step feedback** : Shows the proportion of positive and negative feedback for individual investigation steps.
  * **Investigation summary feedback** : Tracks user feedback for investigation summaries.
  * **Next steps feedback** : Tracks user feedback for recommended response actions.



#### Token usage metrics

  * **Daily token usage** : Displays the total number of security tokens consumed each day.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
