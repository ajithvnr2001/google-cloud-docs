---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-overview/
title: Check data ingestion health \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:39:41.430310+00:00
---

# Check data ingestion health  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Check data ingestion health

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide is for security engineers who want to monitor data ingestion health and troubleshoot issues within Google Security Operations. It explains how to [use the **Health Hub**](https://docs.cloud.google.com/chronicle/docs/reports/data-health-monitoring-and-troubleshooting-dashboard), [configure Cloud Monitoring alerts](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-notifications-for-health-metrics) to track the status of data sources and parsers, and [use silent-host monitoring (SHM)](https://docs.cloud.google.com/chronicle/docs/ingestion/silent-host-monitoring) to detect potential collector stoppages.

Using these monitoring workflows helps you identify, diagnose, and remediate data pipeline problems, distinguishing between user-fixable (actionable) and support-required (non-actionable) issues. Successful configuration ensures reliable data flow, which is crucial for effective security operations and analysis.

## Common use cases

This section covers common use cases for ingestion monitoring.

### Proactive health check

  * **Objective** : Review the status and health of all configured data sources.
  * **Value** : Detect potential ingestion problems before they impact security visibility.



### Alert response

  * **Objective** : Investigate and fix a data source or parser issue flagged by an automated alert.
  * **Value** : Minimize data loss or delays, ensuring data is available for timely threat detection and response.



## Key terminology

  * **Health Hub:** The central dashboard within Google SecOps for monitoring the status and health of all configured data sources and parsers.
  * **Cloud Monitoring:** Google Cloud service used to create alerting policies based on metrics, including those from Google SecOps ingestion.
  * **Silent-host monitoring:** Monitoring method to identify hosts in your environment that have gone silent.
  * **Actionable issue:** An ingestion problem that you can typically resolve yourself through configuration changes (for example, updating credentials).
  * **Non-actionable issue:** An ingestion problem that requires assistance from Google support to resolve (for example, an internal system error).
  * **Parser:** A component that normalizes raw log data into the Unified Data Model (UDM) structure.



## Before you begin

Ensure you have the necessary [Identity and Access Management (IAM) roles and permissions](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access#predefined-roles) to access the Google SecOps instance, view the **Health Hub** , and configure alerts in Cloud Monitoring.

## Monitor data ingestion

This section details various methods to monitor data ingestion.

### Monitor using the Health Hub

Use the [**Health Hub**](https://docs.cloud.google.com/chronicle/docs/reports/data-health-monitoring-and-troubleshooting-dashboard) to monitor overall data health at a glance and view the core health status for each feed, data source, and log type. This helps you identify irregular and failed sources and parsers without configuring custom external alerts.

  1. In the Google SecOps side navigation menu, click **Health Hub**.
  2. Review the Big Number widgets for **Failed Sources** and **Failed Parsers** to identify components requiring immediate attention.
  3. Inspect the **Health Status by Data Source** table. Check the **Latest Issue Details** column for error descriptions, such as, `Config credential issue` or `Normalization issue`.
  4. Click the **Edit Data Source** or **Edit Parser** links provided in the table to navigate directly to the respective configuration pages for remediation.
  5. Check timestamps, such as **Last Event Time** and **Last Ingested** , to verify that the data was ingested as expected.
  6. After applying a fix, monitor the **Health Hub** for the specific data source or parser to ensure the remediation was successful.



### Set up automated ingestion alerts

[Configure Monitoring](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-notifications-for-health-metrics) to trigger alerts when ingestion values reach certain predefined levels. This lets you integrate email notifications into existing workflows to proactively fix broken feeds or detect silent log sources.

  1. In the **Health Hub** , click the **Set Up Alerts** link, which directs you to the Monitoring interface.
  2. Create an alerting policy: 
     * [Select metrics](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-notifications-for-health-metrics): Choose metrics under **Chronicle Collector > Ingestion**, such as **Total ingested log count** or **Total ingested log size**.
     * Add filters for `collector_id` or `log_type` to narrow the alert scope to specific sources.
  3. To detect silent forwarders, select **Metric absence** as the condition type. Configure it to trigger an alert if logs stop flowing for a specified duration (for example, 60 minutes).



## Troubleshooting

This section details various methods to troubleshoot data ingestion issues.

### Common issues

  * **Pipeline latency:** A significant delay between the **Last Event Time** and **Last Ingested** timestamp indicates potential latency. The **Health Hub** exposes the `95th` percentile of this delta. High values suggest pipeline latency, while normal values might mean the source is sending historical data.
  * **Ingestion surges or drops:** The system uses _z-score_ standardization to flag anomalies. A drop is flagged if both daily and weekly standardized differences are less than `-1.645`.
  * **Parsing failures:** An alert is triggered if the proportion of parser errors relative to total ingested events increases by 5 percentage points or more compared to the previous day. Investigate the parser configuration using the link in the **Health Hub**.



To learn more about ways to identify data ingestion and parsing issues, see [Identify and investigate data ingestion and parsing issues](https://docs.cloud.google.com/chronicle/docs/reports/data-health-monitoring-and-troubleshooting-dashboard#identify-issues).

### Latency, service quota, and limits

  * **Data Refresh:** The information on the **Health Hub** and **Data Ingestion** dashboard refreshes approximately every 15 minutes.



### Error remediation

For a full list of error messages and solutions, see [Troubleshoot ingestion](https://docs.cloud.google.com/chronicle/docs/ingestion/troubleshooting-ingestion).

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
