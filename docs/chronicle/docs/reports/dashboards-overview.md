---
url: https://docs.cloud.google.com/chronicle/docs/reports/dashboards-overview/
title: SIEM dashboard overview \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:35.153131+00:00
---

# SIEM dashboard overview  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reports/dashboards-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# SIEM dashboard overview

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Caution:** For all Google Security Operations instances provisioned after August 06, 2025, you can no longer use [Looker](https://docs.cloud.google.com/looker/docs) to create new dashboards in Google SecOps. Use [Dashboards](https://docs.cloud.google.com/chronicle/docs/reports/native-dashboards) instead. To view the available predefined dashboards, see the [Out-of-the-box dashboards catalog](https://docs.cloud.google.com/chronicle/docs/reports/native-curated-dashboards#out-of-the-box-dashboards-catalog).

Use the Google Security Operations SIEM dashboards to view and analyze the data in Google Security Operations SIEM, including security telemetry, ingestion metrics, detections, alerts, and IoCs. These dashboards are based on the capabilities of [Looker](https://docs.cloud.google.com/looker/docs).

Google Security Operations SIEM provides you with multiple default dashboards, described in this document. You can also create [custom dashboards](https://docs.cloud.google.com/chronicle/docs/reports/create-custom-dashboard).

## Default dashboards

Click **Dashboards & Reports** > **Dashboards** to open the **Dashboards** page.

Default dashboards contain predefined visualizations of the data stored within your Google Security Operations SIEM instance. These dashboards are designed for a specific use case, such as understanding the state of the Google Security Operations SIEM data ingestion system or monitoring the threat status in your enterprise.

Each default dashboard includes a time range filter that lets you view data for a specific time period. This can be helpful when troubleshooting issues or identifying trends. For example, you can use the filter to view data for the past week or over a specific time range.

**Note:** Default dashboards can't be modified. You can make a copy of a default dashboard, and then modify the new dashboard to support a specific use case.

To ensure optimal dashboard performance, see Troubleshooting.

Google Security Operations SIEM provides the following default dashboards:

  * Main
  * Cloud Detection and Response
  * Context Aware Detections - Risk
  * [Health Hub](https://docs.cloud.google.com/chronicle/docs/reports/data-health-monitoring-and-troubleshooting-dashboard)
  * Data Ingestion and Health
  * IoC Matches
  * Rule Detections
  * User Sign In Overview



### Main dashboard

The **Main** dashboard displays information about the status of the Google Security Operations SIEM data ingestion system. It also includes a global map highlighting the geographic location of the IoCs detected within your enterprise.

You can view the following visualizations in the **Main** dashboard:

  * **Ingested Events** : the total number of events ingested.
  * **Throughput** : the volume of data that is ingested for a specific time.
  * **Alerts** : the total number of detections that have occurred over a period of time. The number of alerts displayed on the **Alerts & IoCs** page may differ, as this page shows only current alerts. For more information, see [View alerts](https://docs.cloud.google.com/chronicle/docs/investigation/alerts-iocs#view_alerts).
  * **Events Over Time** : a column chart that displays the events that occurred over a period of time.
  * **Global Threat Map - IoC IP Matches** : the location from which Indicator of Compromise (IoC) matching events occurred.

**Note:** The mapping feature is unavailable in some regions of the world.

### Cloud Detection and Response Overview dashboard

**Note:** The Cloud Detection and Response dashboard requires Security Command Center Premium.

The **Cloud Detection and Response** dashboard helps you monitor the security status of your cloud environment and investigate potential threats. The dashboard shows visualizations that help you understand the volume of data sources, rule sets, alerts, and other information.

The **Time** filter lets you filter the data by time period.

The **GCP Log Type** filter lets you filter the data by Google Cloud log type.

You can view the following visualizations in the **Cloud Detection and Response Overview** dashboard:

  * **CDIR Rulesets Enabled** : displays the percentage of Google Security Operations SIEM rule sets enabled for your cloud environment from the total rule sets provided by GCTI for Google Security Operations SIEM users. GCTI provides multiple prepackaged curated rules. You can enable or disable these rule sets.

  * **GCP Data Sources Covered** : displays the percentage of data sources covered, out of the total Google Cloud data sources available. For example, if you can ingest data by using 40 log types but you send data for only 20, the tile displays 50%.

  * **CDIR alerts** : displays the number of alerts raised from the rules within your GCTI rulesets or Cloud threats. You can use the **Time** filter to set the number of days for which this data is displayed.

  * **Recent Alerts** : displays recent alerts with their severity and risk score. You can sort the table using the **Event Timestamp Time** column and navigate to each alert for more information. It provides the number of aggregated security findings enhanced by Security Command Center. These security findings are generated by GCTI curated detection rule sets and categorized by finding type. You can use the **Time** filter to set the number of days for which this data is displayed.

  * **Alerts by Severity Over Time** : displays the total alerts by severity, trending over time. You can use the **Time** filter to set the number of days for which this data is displayed.

  * **Detection Coverage** : provides information about Google Security Operations SIEM rule sets and their status, total detections, and the date of the most recent detection. You can use the **Time** filter to set the number of days for which this data is displayed.

  * **Cloud Data Coverage** : provides information about all available Google Cloud services, parsers that cover each service, first seen event, last seen event, and the total throughput.




For more information about CDIR rule sets, see [Overview of Cloud Threats Category](https://docs.cloud.google.com/chronicle/docs/detection/cloud-threats-category).

The table is followed by graphs of all Google Cloud services with their associated data that show their ingestion trend over the following time intervals:

  * Last 24 hours
  * Last 30 days
  * Last six months



### Context Aware Detections - Risk dashboard

The **Context Aware Detections - Risk** dashboard provides insight into the current threat status of assets and users in your enterprise. It is built using fields in the **Rule Detections** explore interface.

The severity and risk score values are variables defined in each rule. For an example, see [Outcome section syntax](https://docs.cloud.google.com/chronicle/docs/yara-l/outcome-syntax). In each panel, data is sorted based on severity, and then risk score to identify users and assets most at risk.

You can view the following visualizations in the **Context Aware Detections - Risk** dashboard:

  * **Assets and Devices at Risk** : lists the top 10 assets based on the severity that you set the rule in the **Meta** > **Severity**. See [Meta section syntax](https://docs.cloud.google.com/chronicle/docs/yara-l/meta-syntax). The severity levels are **Super High** , **Critical** , **High** , **Large** , **Medium** , and **Low**. If the `hostname` value is not present in the record, then it displays the IP address.
  * **Users at Risk** : lists the top 10 users based on severity. The severity levels are **Super High** , **Critical** , **High** , **Large** , **Medium** , and **Low**. If the `username` value is not present in the record, then it displays the email ID.
  * **Aggregate Risk** : for each date, displays the total aggregated risk score.
  * **Detection Results** : displays details about the detections returned by detection engine rules. The table includes the rule name, detection ID, risk score, and severity.



### Data Ingestion and Health dashboard

The **Data Ingestion and Health** dashboard provides information about the type, volume, and health of data being ingested into your Google Security Operations SIEM tenant. You can use this dashboard to monitor for anomalies in your environment. This dashboard provides visualizations that help you understand the volume of ingested logs, ingestion errors, and other relevant information.

**Note:** The data on the **Data Ingestion and Health** dashboard refreshes every 15 minutes. Wait up to 15 minutes to view the latest information.**Note:** To monitor the operational status and health of all of your data sources and parsers, go to the [**Health Hub**](https://docs.cloud.google.com/chronicle/docs/reports/data-health-monitoring-and-troubleshooting-dashboard). It includes information about failed and irregular sources and log types, and provides context to diagnose and remediate issues.

You can view the following visualizations in the **Data Ingestion and Health** dashboard:

  * The **Global Time Filter** configured on the dashboard applies to the following visualizations: 

    * **Ingested Events Count** : displays the total number of ingested events.
    * **Log Type Distribution by Throughput** : displays the log types distribution based on the throughput.
    * **Throughput** : displays the ingestion throughput.
    * **Log Type Distribution by Events Count** : displays the log types distribution based on the number of events for each log type.
    * **Ingestion Error Count** : displays the total number of errors encountered during ingestion.
    * **Ingestion - Events by Status** : displays a table with events based on their status—sortable by column: **Date** , **Ingested Logs** , **Normalized Events** , **Parsing Errors** , **Validation Errors** , **Indexing Errors**.
    * **Burst Limit Graph - Ingestion Rate** : displays the log-ingestion hourly rate over time (see [Burst limits](https://docs.cloud.google.com/chronicle/docs/ingestion/burst-limits)).
    * **Burst Limit Graph - Quota Limit** : displays the hourly log-ingestion quota over time (see [Burst limits](https://docs.cloud.google.com/chronicle/docs/ingestion/burst-limits)).
    * **Burst Rejection Graph** : displays the hourly volume over time of logs that were rejected for exceeding the burst limit (see [Burst limits](https://docs.cloud.google.com/chronicle/docs/ingestion/burst-limits)).
    * **Ingestion - Events by Log Type** : displays events based on log type—sortable by column: **Log Type** , **Ingested Throughput** , **Ingested Logs** , **Normalized Events** , **Parsing Errors** , **Validation Errors** , **Indexing Errors**.

**Note:** The **Ingested Throughput** and **Ingested Logs** columns display `0` values for **UDM** logs if there are only [`ENTITY_RISK_CHANGE`](https://docs.cloud.google.com/chronicle/docs/detection/risk-based-alerting) events in the specified timeframe. This is because `ENTITY_RISK_CHANGE` events aren't counted in ingestion metrics, and they have no effect on billing. 
    * **Bindplane Agent Logging - Logs by Severity over Time** : displays the number of logs by severity over time. The dashboard displays this visualization only when your Google SecOps ingests logs from a Bindplane agent.

    * **Bindplane Agent Logging - Message Count** : displays the number of logs by message text—sortable by column: **Severity** , **Message** , **Total** , **First Seen** , **Last Seen**. The dashboard displays this visualization only when your Google SecOps ingests logs from a Bindplane agent.

  * The timeframes for the following visualizations are preselected and aren't affected by the **Global Time Filter** : 

    * **Recently Ingested Events** : displays recently ingested events for each log type.
    * **Daily Log Information** : displays the numbers of logs for a day for each log type.
    * **Event Count (Last 24 Hours)** and **Event Size (Last 24 Hours)** : display the event counts and the event sizes for the last 24 hours.
    * **Event Count (Last 7 Days)** and **Event Size (Last 7 Days)** : display the event counts and the event sizes for the last 7 days.
    * **Event Count (Last 3 Months)** and **Event Size (Last 3 Months)** : display the event counts and the event sizes for the last 3 months.
    * **Ingestion - Throughput Hourly** : displays the hourly ingestion throughput.
    * **Ingestion - Throughput Weekly** : displays the weekly ingestion throughput.
    * **Ingestion - Throughput (Last 6 months)** : displays the ingestion throughput over the last 6 months.
    * **Ingestion - Throughput (All-Time)** : displays the ingestion throughput per year for all the time that there is data for.
    * **Number of Days Since Host Reported an Event (Last 7 Days)** : displays the number of days since hosts reported an event (in the last 7 days).



### IoC Matches dashboard

The **IoC Matches** dashboard provides visibility into the IoCs present in your enterprise.

**Note:** The **IoC Matches** dashboard shows IoC details at the time of the IoC matching (like confidence score and severity), whereas the **IOC Matches** tab of the **[Alerts& IoCs](https://docs.cloud.google.com/chronicle/docs/investigation/alerts-iocs)** page shows the UNIX seconds value for the day bucket in which the IoC match occurred.

You can view the following visualizations in the **IoC Matches** dashboard:

  * **IoC Matches Over Time by Category** : displays the number of IoC matches based on their category.
  * **Top 10 Domains IoC indicators** : lists the top 10 domain IoC indicators and their counts.
  * **Top 10 IP IoC Indicators** : lists the top 10 IP address IoC indicators and their counts.
  * **Top 10 Assets by IoC Matches** : lists the top 10 assets by IoC matches, and their counts.
  * **Top 10 IoC matches by Category, Type, and Count** : lists the top 10 IoC matches by category, type, and their counts.
  * **Top 10 IoC Values** : lists the top 10 IoC values along with the count.
  * **Top 10 Rarely Seen Values** : lists the top 10 rarely occurring IoC matches and their counts.



The **IoC Matches** visualizations include the **Event Timestamp Filter** under **Filter-only fields**.

**Important:** We recommend that you don't filter directly on **Event Timestamp Filter**.

### Rule Detections dashboard

The **Rule Detections** dashboard provides insight into the detections returned by detection engine rules. To receive detections, you must enable rules. For more information, see [Running a rule against live data](https://docs.cloud.google.com/chronicle/docs/detection/run-rule-live-data).

You can view the following visualizations in the **Rule Detections** dashboard:

  * **Rule Detections Over Time** : displays the number of rule detections over a period of time.
  * **Rule Detections by Severity** : displays the severity of the rule detections.
  * **Rule Detections by Severity Over Time** : displays the daily count of detections by severity over time.
  * **Top 10 Rule Names by Detections** : lists the top 10 rules returning the largest number of detections.
  * **Rule Detections by Name Over Time** : displays the rules that returned detections each day and the number of detections returned.
  * **Top 10 Users by Rule Detections** : lists the top 10 user identifiers which appeared in events that triggered detections.
  * **Top 10 Asset Names by Rule Detections** : lists the top 10 asset names which appeared in events that triggered detections, such as hostname.
  * **Top 10 IPs by Rule Detections** : lists the top 10 IP addresses which appeared in events that triggered detections.



### User Sign In Overview dashboard

The **User Sign in Overview** dashboard provides insight into users logging into your enterprise. This information can be useful for tracking attempts by malicious actors to access your enterprise.

For example, you might find that a particular user has attempted to access your enterprise from a country where you don't have an office or that an specific user appears to repeatedly access an accounting application.

You can view the following visualizations in the **User Sign In Overview** dashboard:

  * **Number of Successful Sign Ins** : displays the total number of successful sign-ins.
  * **Number of Failed Sign Ins** : displays the total number of failed sign-ins.
  * **Sign Ins By Status** : displays the split of successful and failed sign-ins.
  * **Sign Ins by Status Over Time** : displays the split of successful and failed sign-ins over the time range.
  * **Top 10 Applications By Sign Ins** : displays the split of top 10 frequent applications based on the number of sign ins.
  * **Sign Ins By Application** : lists the count of sign in status for each application. The count of each application is populated based on the log data that you define in the `security_result.action` field. See [Event enumerated types](https://docs.cloud.google.com/chronicle/docs/reference/udm-field-list#securityresultaction).
  * **Top 10 Countries by Sign Ins** : displays the count of top 10 countries where users signed in from.
  * **Sign Ins by Country** : displays the count of all countries where users signed in from.
  * **Top 10 Sign Ins By IP** : displays the top 10 IP addresses where users signed in from.
  * **Sign In Location Map** : displays the locations of IP addresses where users signed in from.
  * **Top 10 Users by Sign In Status** : displays the count of sign in status for each user. The count of each application is populated based on the log data that you define in the `security_result.action` field. See [Event enumerated types](https://docs.cloud.google.com/chronicle/docs/reference/udm-field-list#securityresultaction).



## Troubleshooting

This section outlines performance expectations and provides self-service fixes for common dashboard and search issues.

### Optimize dashboard performance

To ensure your dashboards and searches remain responsive when dealing with large datasets, align your visualizations with the platform's rendering limits. The Google SecOps UI has a 10,000-row visualization limit; exceeding this threshold can cause your browser tab to stop responding, which can be confused for a platform outage.

To visualize high-volume log data effectively:

  * Always apply a **"Top N"** filter (for example, Top 10 IP addresses) to aggregate data before rendering.
  * Reduce your search time range to **15-minute or 1-hour increments** when performing raw log hunts.
  * Use the **Export to CSV** or **BigQuery** features if you require access to more than 10,000 rows.



### SOAR data source support

You can query SOAR data sources for built-in dashboards only in unified Google Security Operations environments. If you run standalone Google SecOps SIEM and SOAR projects in Google Cloud, you can't access or query SOAR datasets from the SIEM dashboard interface.

### What's next

  * [Learn how to create a custom dashboard](https://docs.cloud.google.com/chronicle/docs/reports/create-custom-dashboard)



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
