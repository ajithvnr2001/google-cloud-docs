---
url: https://docs.cloud.google.com/chronicle/docs/reports/data-health-monitoring-and-troubleshooting-dashboard/
title: Monitor health of data sources \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:29:10.391354+00:00
---

# Monitor health of data sources  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reports/data-health-monitoring-and-troubleshooting-dashboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Monitor health of data sources

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

This guide is for security engineers who want to monitor the health and status of their data ingestion, parsing, and latency within Google Security Operations. It explains how to use the Health Hub to identify, diagnose, and begin remediating issues affecting your data pipeline. By using the Health Hub, you can quickly detect and address problems, which helps maintain data quality and ensures effective security monitoring.

The Health Hub is the central location in Google SecOps for you to monitor the status and health of all configured data sources. It provides crucial information on data sources, log types, and latency—offering the context needed to diagnose and remediate data pipeline issues.

The Health Hub includes the following information:

  * Ingestion volumes and ingestion health
  * Parsing volumes from raw logs to [Unified Data Model (UDM) events](https://docs.cloud.google.com/chronicle/docs/event-processing/udm-overview)
  * Latency metrics for data sources and log types
  * Context and links to interfaces with additional relevant information and functionality
  * Irregular and failed sources and log types



The Health Hub detects irregularities and failures on a per-customer basis. It uses statistical methods with a 15-day lookback period to analyze ingestion data. Items that are marked _irregular_ identify surges or drops in data being ingested and processed by Google SecOps. An irregularity can indicate a parser problem, a vendor schema change, or a change in your data pipeline.

## Key terminology

  * **Health Hub** : The central interface within Google SecOps for monitoring the status and health of data sources.
  * **Irregular** : Describes a data source or parser exhibiting unusual surges or drops in data volume or a significant change in error rates, as detected by the irregularity-detection engine.
  * **Unified Data Model (UDM)** : A standardized data structure used within Google SecOps for representing security events.



## Before you begin

Before you use the Health Hub, confirm that you are assigned a role that includes the necessary Identity and Access Management (IAM) permissions for monitoring and reporting. If you can't access the Health Hub, contact your administrator.

### Standard predefined roles

Access to Health Hub features is generally included in the following [predefined IAM roles](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access?content_ref=roles%20chronicle%20admin%20chronicle%20api%20admin%20full%20access%20to%20google%20secops%20application%20and%20api%20services%20including%20global%20settings#overview-perm-role):

  * **Chronicle API Admin** (`roles/chronicle.admin`)
  * **Chronicle API Editor** (`roles/chronicle.editor`)
  * **Chronicle API Viewer** (`roles/chronicle.viewer`)
  * **Chronicle API Limited Viewer** (`roles/chronicle.limitedViewer`)



### Specific permission

A key permission associated with the data that's surfaced in the Health Hub (such as bytes ingested and log counts) is `chronicle.instances.report`. This permission is included in the Admin, Editor, Viewer, and Limited Viewer roles.

### Additional permissions for integrated capabilities

Because the Health Hub integrates with other Google Cloud services for alerting and deeper investigation, additional permissions might be required for full functionality:

  * **Cloud Monitoring** : To set up alerts based on the health metrics displayed in the Health Hub, users need appropriate permissions in Cloud Monitoring.
  * **Feature-specific access** : Actions like editing a feed or parser directly from the Health Hub require the corresponding edit permissions (for example, `chronicle.feeds.update` or `chronicle.parsers.activate`).



## Access the Health Hub

  * To access the Health Hub, in the side navigation menu, click **Health Hub**.



The Health Hub is a read-only [_default dashboard_](https://docs.cloud.google.com/chronicle/docs/reports/dashboards-overview) and can't be modified directly. To customize, create a copy of the Health Hub, and then modify the duplicated dashboard for your specific use case.

## Understand and use the Health Hub interface

This section describes the Health Hub interface and its components so that you can identify, diagnose, and begin remediating issues affecting your data pipeline.

The Health Hub includes the following sections:

  * Widgets
  * **Health Status Monitoring**
  * **Latency Status Monitoring**



### Health Hub widgets

The Health Hub displays the following widgets:

  * **Big number widgets** :

    * **Healthy Sources** : The number of data sources performing with no failures and no irregularities.
    * **Failed Sources** : The number of data sources that need immediate attention.
    * **Irregular Data Sources** : The number of irregular data sources and parsers.
    * **Healthy Parsers** : The number of parsers performing with no failures.
    * **Failed Parsers** : The number of parsers that need immediate attention.
    * **Irregular Parsers** : The number of parsers that are exhibiting irregular behavior.
  * **Data Source Health Overview** : A line graph showing the **Healthy** , **Irregular** , and **Failed** data-sources-per-day curves over time.

  * **Parsing Health Overview** : A line graph showing the **Healthy** , **Irregular** , and **Failed** parsers-per-day curves over time.

  * **Total Ingested Logs** : A line graph showing the **Ingested Logs** logs-per-day curve over time.

**Note:** Some ingested logs are mapped to more than one normalized log. The total parsed log count can be higher than the total ingested log count.
  * **Failing Parser by Log Type** : A line graph showing a curve for each parser with a _failed_ health status, per day over time. In this context, the _failed_ health status is due to a very low parsing-success rate.




### Monitor the health status of data sources and log types

The **Health Status Monitoring** section includes the following tables:

  * **Health Status by Data Source**
  * **Health Status by Parser**



#### Health Status by Data Source table

The **Health Status by Data Source** table includes the following columns:

Column | Description  
---|---  
**Status** | The cumulative status of the feed (**Healthy** , **Irregular** , or **Failed**), derived from data volume, configuration errors, and API errors.  
**Source Type** | The source type (ingestion mechanism)—for example, **Ingestion API** , **Feeds** , **Native Google Workspace Ingestion** , or **Azure Event Hub Feeds**.  
**Name** | The feed name.  
**Log Type** | The log type—for example, `CS_EDR`, `UDM`, `GCP_CLOUDAUDIT`, or `WINEVTLOG`.  
**Latest Issue Details** | The details about the latest issue in the specified timeframe—for example, **Failed parsing logs** , **Config credential issue** , or **Normalization issue**. The stated issue can be actionable (for example, **Incorrect Auth**) or non-actionable (for example, `Internal_error`). If the issue is non-actionable, the recommended action is to open a support case with Google SecOps. When there has been no issue in the specified timeframe, the value is empty or displays `OK`.  
**Issue Duration** | The number of days that the data source has been in an irregular or failed state. When the **Status** is **Healthy** , the value is empty or displays `N/A`.  
**Last Collected** | The timestamp of the last data collection.  
Note: The value is always the _latest_ timestamp—even if an older event is ingested later.  
**Last Ingested** | The timestamp of the last successful ingestion. Use this metric to identify whether your logs are reaching Google SecOps.  
**Config Last Updated** | The timestamp of the last change to the metric. Use this value to correlate configuration updates with observed irregularities or failures, helping you determine the root cause of ingestion problems or parsing problems.  
**View Ingestion Details** | Contains a **Dashboard** link, which opens a new tab with the **Data Health Deep Dive** dashboard. The **Data Health Deep Dive** dashboard contains additional, historical information—for deeper analysis.  
**Edit Data Source** | A link that opens a new tab with the corresponding [feed configuration](https://docs.cloud.google.com/chronicle/docs/administration/feed-management)—where you can fix configuration-related irregularities or failures.  
**Set Up Alerts** | A link, which opens a new tab with the corresponding [Cloud Monitoring](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-notifications-for-health-metrics) interface. From there you can, configure custom API-based alerts using **Status** and log-volume metrics  
  
#### Health Status by Parser table

The **Health Status by Parser** table includes the following columns:

Column | Description  
---|---  
**Status** | The cumulative status of the log type (**Healthy** , **Irregular** , or **Failed**).  
**Latest Issue Details** | The details about the latest parsing problem in the specified timeframe—for example, **Failed parsing logs** , **Config credential issue** , or **Normalization issue**. The stated issue can be actionable (for example, **Incorrect Auth**) or non-actionable (for example, `Internal_error`). If the issue is non-actionable, the recommended action is to open a support case with Google SecOps. When there has been no issue in the specified timeframe, the value is empty or displays `OK`.  
**Last Ingested** | The timestamp of the last successful ingestion. You can use this metric to determine whether logs are reaching Google SecOps.  
**Last Event Time** | The event timestamp of the last normalized log.  
Note: The value is always the _latest_ timestamp—even if an older event is ingested later.  
**Last Normalized** | The timestamp of the last parsing and normalization action for the log type. You can use this metric to determine whether raw logs are successfully transformed into [UDM events](https://docs.cloud.google.com/chronicle/docs/event-processing/udm-overview).  
**Config Last Updated** | The timestamp of the last change to the metric. Use this value to correlate configuration updates with observed irregularities or failures, helping you determine the root cause of ingestion problems or parsing problems.  
**View Parsing Details** | Contains a **Dashboard** link, which opens a new tab with the **Data Health Deep Dive** dashboard. The **Data Health Deep Dive** dashboard contains additional, historical information—for deeper analysis.  
**Edit Parser** | A link, which opens a new tab with the corresponding [parser configuration](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/default-parser-configuration)—where you can fix configuration-related irregularities or failures.  
**Set Up Alert** | A link, which opens a new tab with the corresponding [Cloud Monitoring](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-notifications-for-health-metrics) interface.  
  
### Monitor the latency status of data sources and log types

The Health Hub includes latency status monitoring to improve end-to-end visibility and help reduce the mean time to debug (MTTD) for delayed logs. Google SecOps calculates latency at both the source level and the log type level.

The **Latency Status Monitoring** section of the Health Hub includes the following tables:

  * **Latency Status by Source**
  * **Latency Status by Log Type**



#### Latency Status by Source table

The **Latency Status by Source** table displays latency metrics for each individual source (for example, [Bindplane](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent) collectors or third-party APIs) and includes the following columns:

Column | Description  
---|---  
**Source Type** | The ingestion mechanism—for example, **Ingestion API** or **Feeds**.  
**Name** | The name of the specific feed or source.  
**Log Type** | The log type—for example, `CS_EDR` or `WINEVTLOG`.  
**Source to Ingestion Latency (P95)** | The maximum time it took for 95% of the raw logs to reach Google SecOps and be ingested from the moment they were generated. This measures the delta between the event (raw log) creation time and the ingestion time.  
**SecOps Ingestion Latency (P95)** | The maximum time it took from the moment Google SecOps collected the logs until they were fully ingested. This measures the delta between the collection time and the ingestion time.  
**Polling Frequency** | For pull-based mechanisms, this indicates how often Google SecOps checks the source for new data.  
**Lookback Window** | For third-party APIs, this indicates how far back in time the system goes to fetch logs during each transfer.  
**View** | Contains a **Dashboard** link, which opens a new tab with the **Data Health Deep Dive** dashboard filtered for this specific source.  
  
#### Latency Status by Log Type table

The **Latency Status by Log Type** table displays aggregate latency metrics for each log type and includes the following columns:

Column | Description  
---|---  
**Log Type** | The log type being monitored.  
**Source to Ingestion Latency (P95)** | The overall P95 latency from event generation to ingestion for the specific log type, aggregated across all sources contributing to it.  
**View** | Contains a **Dashboard** link, which opens a new tab with the **Data Health Deep Dive** dashboard filtered for this specific log type.  
  
## Identify and investigate data ingestion and parsing issues (deep dive)

This section describes how to use the Health Hub to identify and investigate some common data ingestion and parsing issues.

**Note:** This section refers to Health Hub components and parameters, which are described in the interface section.

### Investigate feed runs and parser statuses

To investigate feed runs and parser statuses, do the following:

  1. Go to the **Health Status by Data Source** or the **Health Status by Parser** table, and go to the row with the item whose status you want to investigate. 
  2. Click the **Dashboard** link. The **Data Health Deep Dive** dashboard opens. The dashboard shows the last 2000 feed runs and last 200 parser errors for that specific row.



### Verify that logs are reaching Google SecOps

To verify whether logs are reaching Google SecOps, do the following: 

  * View the **Last Ingested** and **Last Normalized** metrics (in the **Health Status by Data Source** and **Health Status by Parser** tables respectively). These metrics confirm the last time that data was successfully delivered.
  * View the ingestion-volume metrics (per source and per log type), which show you the amount of data being ingested.



### Confirm that logs are parsed correctly

  * To confirm that logs are parsed correctly, go to the **Health Status by Parser** table and view the **Last Normalized** metric. This metric indicates when the last successful transformation from raw log into a [UDM event](https://docs.cloud.google.com/chronicle/docs/event-processing/udm-overview) occurred.



### Identify significant volume changes

To identify significant volume changes, do the following:

  * View the **Status** field, which shows your data's health (**Healthy** or **Failed**) based on data volume. 
  * View the **Total Ingested Logs** graph to identify sudden or sustained surges or drops.



### Configure alerts for failing sources

The Health Hub feeds the **Status** and log-volume metrics into Cloud Monitoring. 

To configure alerts for failing sources do the following: 

  1. In one of the Health Hub tables, click the relevant **Alerts** link to open the [Cloud Monitoring](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-notifications-for-health-metrics) interface. 
  2. Configure custom API-based alerts using **Status** and log-volume metrics.



### Infer delays in log-type ingestion

  * To infer delays in log-type ingestion, compare the **Last Event Time** and the **Last Ingested** timestamps. A delay is indicated when the **Last Event Time** is significantly behind the **Last Ingested** timestamp. The Health Hub exposes the 95th percentile of the **Last Ingested** –**Last Event Time** delta—per log type. A high value suggests a latency problem within the Google SecOps pipeline, whereas a normal value might indicate that the source is pushing old data.

**Note:** You can monitor latency also through the dedicated **Latency Status Monitoring** section and using deep dive components. 

### Review historical health trends

  * To review historical health trends, view the **Data Source Health Overview** , **Parsing Health Overview** , and **Total Ingested Logs** graphs, which show the historical trend of your data's health, letting you observe long-term patterns and irregularities.



### Identify data ingestion problems

When you suspect that data sources are failing to send logs, or if logs are not appearing in Google SecOps, do the following to verify whether data is successfully arriving and being processed:

  1. **Check for sudden volume drops** :

     * Review the **Total Ingested Logs** widget to identify sudden or sustained surges or drops in log volume over time. A significant drop may indicate a disconnected source.
     * Review **Failed** and **Irregular** data sources.
  2. **Verify data ingestion** :

     1. In the **Health status by data source** table, check the **Last Ingested** metric. This timestamp shows the last successful ingestion, which lets you determine whether logs from that specific feed or API are actively reaching Google SecOps.
     2. Compare the **Last Ingested** metric with the **Last Collected** timestamp, which indicates when Google SecOps last received an event—even if the payload was empty.
  3. **Verify log parsing and normalization** :

Even if data is ingested, you must ensure that the parsers are configured correctly and successfully parsing the logs into Unified Data Model (UDM) events. 

     1. In the **Health Status by Parser** table, view the **Last Normalized** metric to confirm when the last successful transformation from a raw log into a UDM event occurred. If the source isn't ingesting, it will be marked as **Irregular** or **Failed** in the Health Hub.

     2. For further analysis, click the **Dashboard** link in the **View Ingestion Details** column to open the **Data Health Deep Dive** dashboard.

  4. **Analyze daily ingestion events for the specific feed** :

     1. Navigate to the **Data Health Deep Dive** dashboard for the log type that you are investigating.
     2. Review the **Ingestion - Events by Status** table and check the exact number of ingested logs over the past several days. This helps confirm if the drop to zero was sudden or gradual.
     3. View the **Log Count by Feed ID** and **Log Count by Collector ID & Log Type** graphs to filter down to the single feed or collector level.
  5. **Check for burst rejections and quota limits** : If the numbers of your ingested logs are lower than expected, review the **Burst Limit Graph - Quota Limit** and the **Burst Rejection Graph**. For more information about burst limits, see [Understand quotas and burst limits](https://docs.cloud.google.com/chronicle/docs/ingestion/burst-limits).




### Investigate delayed logs

Log delays can occur either before the data reaches Google SecOps (at the log source) or somewhere within the Google SecOps ingestion pipeline.

**Note:** You can monitor latency also through the dedicated **Latency Status Monitoring** section and using deep dive components. 

To investigate delayed logs, do the following:

  1. **Compare the following timestamps to locate and measure latency** :

     * **Last Event Time** (in the **Health Status by Parser** table): The event timestamp of the last normalized log.
     * **Last Collected Time** (in the **Health Status by Data Source** table): The timestamp of the last data collection (when Google SecOps received the event).
     * **Last Ingested Time** (available in both tables): The timestamp of the last successful ingestion.
  2. **Isolate the source of the delay** :

     * **Delays at the source/network** : If there's high latency between the **Last Event Time** and the **Last Collected Time** , the issue is likely occurring on the source side.
     * **Delays in the Google SecOps pipeline** : If there's a significant delay between the **Last Collected Time** and the **Last Ingested Time** in the **Health Status by Data Source** table, the data has reached Google SecOps but is delayed during processing. High latency between collection and ingestion time usually indicates an issue within the Google SecOps pipeline, and this scenario can happen during quota breaches.

You can infer overall delays by checking if the **Last Event Time** is significantly behind the **Last Ingested** timestamp directly within the **Health Status by Parser** table.

If timestamps indicate latency between collection and ingestion, the **Data Health Deep Dive** dashboard can help visualize the flow rate and isolate irregular feed run patterns.

  3. **View ingestion throughput anomalies** :

     1. In the **Data Health Deep Dive** dashboard, review the **LogType Ingestion Rate Per Hour** or **Ingestion rate/log volume per hour** graphs.

     2. Look for unusual gaps followed by massive spikes, which typically indicate delayed batching from the collector or source.

  4. **Review feed run frequency** : Check the **Feed Run History (Last 2000 Runs)** and **Run History (Last 2000 Runs)** graphs to confirm whether the scheduled feed execution is occurring at the expected cadence.




### Identify and remediate feed and parsing errors

When logs fail to ingest or parse correctly due to configuration issues, bad credentials, or schema changes, the Health Hub flags the source or parser as **Irregular** or **Failed**.

To identify and remediate feed and parsing errors, do the following:

  1. **Identify actionable and non-actionable errors** : Look at the **Latest Issue Details** column in the **Health Status by Data Source** or **Health Status by parser** table to find details about the latest issue in the specified timeframe. The text identifies specific problems, and can help you determine whether the action is _actionable_ (you fix it) or _non-actionable_ (requires support). The text **Forbidden 403: Permission denied** is an example of an actionable error, where the auth account provided in the feed configuration lacks required permissions. The text `Internal_error` is an example of a non-actionable error. 

  2. **Do one of the following** : 

     * **If the error is a non-actionable error, open a support case with Google SecOps.**
     * **If the error is an actionable error, do the following** :

       1. **Correlate errors with recent configuration changes** : If the error is an actionable error, check whether the **Config Last Updated** timestamp is close to the **Last Ingested** timestamp. If the **Config Last Updated** timestamp is close to the **Last Ingested** timestamp, it suggests that a recent configuration update may be the cause of a failure. This correlation helps in root-cause analysis.
       2. **Identify the exact stage of failure** :

When the Health Hub shows irregular or failed statuses, the **Data Health Deep Dive** dashboard is the best place to find the exact historical error messages and pinpoint where the event breakdown is happening. 

          1. Open the **Data Health Deep Dive** dashboard and look at the **Ingestion - Events by Status** table.
          2. Compare the number of ingested logs against the specific error columns: **Parsing Errors** , **Validation Errors** , and **Indexing Errors**. This isolates whether the failure is occurring during initial parsing, UDM validation, or final indexing.
          3. **Review detailed historical parser errors** : Navigate to the **Parser Error History (Last 200 errors)** table to see a chronological log of recent issues.
       3. **Self-remediate common issues.** Use the links to edit configurations and fix common problems directly (also see Self-remediate data health issues):

          * **Incorrect authentication or credentials** : If you see authorization errors, click the **Edit Data Source** link in the **Health Status by Data Source** table, and edit the data source configuration using correct authentication credentials.
          * **Failed parsing or normalization issues** : If logs are failing to parse or map to UDM correctly, click the **Edit Parser** link in the **Health Status by Parser** table, review the parser configuration, and adjust the parser settings as necessary.
       4. **Validate your fixes** : After making adjustments, monitor the Health Hub to validate that the **Status** of the affected data sources or parsers changes to **Healthy** and that the **Latest issue details** field becomes empty or displays **OK**.




## Identify and investigate latency issues (deep dive)

This section describes how to use the Health Hub and the **Data Health Deep Dive** dashboard to isolate and investigate the root cause of delayed logs.

**Note:** This section refers to Health Hub components and parameters, which are described in the interface section.

### Investigate latency trends and isolate root causes

To investigate latency issues and determine whether delays are originating from the source or within the Google SecOps pipeline, do the following:

  1. In the Health Hub, review the **Latency Status by Log Type** table to identify any log types experiencing unusually high **Source to Ingestion Latency**.
  2. Filter the **Latency Status by Source** table by the affected log type to identify which specific sources are contributing to the latency irregularities.
  3. Click the **Dashboard** link for the affected source or log type to open the **Data Health Deep Dive** dashboard. The deep dive dashboard displays historical line graphs for P50, P90, and P95 latencies.
  4. Compare the **Source to Ingestion Latency** graph and the **SecOps Ingestion Latency** graph for the selected timeframe: 
     * **Delays in the Google SecOps pipeline** : If a spike in the **Source to Ingestion Latency** is also reflected as a spike in the **SecOps Ingestion Latency** , the delay is likely occurring during processing within Google SecOps.
     * **Delays at the source or network** : If there is a spike in the **Source to Ingestion Latency** , but the **SecOps Ingestion Latency** remains stable and unaffected, you can conclude that the delay is caused by external factors prior to reaching Google SecOps (for example, issues with the Bindplane collector backlog, or the source API).



## Self-remediate data health issues

**Note:** This section refers to Health Hub components and parameters, which are described in the interface section.

To self-remediate data health issues, do the following:

  1. Use the following table to identify the issue, cause, and perform the suggested remediation:

Issue | Cause | Suggested remediation  
---|---|---  
**Incorrect authentication** | The authentication account provided in the feed configuration lacks required permissions. | Edit the data source configuration using the **Edit Data Source** link in the **Health Status by Data Source** table and correct the authentication credentials.  
**Internal_error** | An `Internal-error`, that is, an internal system error has occurred. | Open a support case with Google SecOps.  
**Failed parsing of logs** | The system encountered issues while parsing raw logs. | Review the parser configuration. Use the **Edit Parser** link in the **Health Status by Parser** table to adjust the parser settings.  
**Configuration credentials issue** | There is a problem with the credentials used in the configuration. | Edit the data source configuration using the **Edit Data Source** link to verify and correct credentials.  
**Normalization issue** | Logs are not being successfully transformed into UDM events. | Review the parser configuration using the **Edit Parser** link and ensure logs are being correctly mapped to UDM fields.  
  2. After making changes to remediate data health issues, monitor the Health Hub to do the following:

     * Validate that the **Status** of the affected data sources or parsers changes to **Healthy** and that the **Latest Issue Details** field becomes empty or displays `OK`. 
     * Check the graphs to see whether ingestion and parsing volumes have returned to expected levels.



## Understand the irregularity-detection engine

The Health Hub uses the Google SecOps irregularity-detection engine to automatically identify significant changes in your data, letting you quickly detect and address potential problems.

The irregularity-detection engine looks back at the last 15 days of data, calculates based on the last 24 hours compared to the 15-day period, and recalculates every hour.

### Data ingestion irregularity-detection

Google SecOps analyzes daily volume changes, while considering normal weekly patterns.

The irregularity-detection engine uses the following calculations to detect unusual surges or drops in your data ingestion:

  * **Daily and weekly comparisons** : Google SecOps calculates the difference in ingestion volume between the current day and the previous day, and also the difference between the current day and the average volume over the past week.
  * **Standardization** : To understand the significance of these changes, Google SecOps standardizes them using the following z-score formula:

`z = (x<sub>i</sub> − x_bar) / stdev`

where

    * `z` is the standardized score (or z-score) for an individual difference
    * `x<sub>i</sub>` is an individual difference value
    * `x_bar` is the mean of the differences
    * `stdev` is the standard deviation of the differences
  * **Irregularity flagging** : Google SecOps flags an irregularity if both the daily and weekly standardized changes are statistically significant. Specifically, Google SecOps searches for:

    * **Drops** : Both the daily and weekly standardized differences are less than -1.645.
    * **Surges** : Both the daily and weekly standardized differences are greater than 1.645.



### Normalization ratio

When calculating the ratio of ingested events to normalized events, the irregularity-detection engine uses a combined approach to ensure that only significant drops in normalization rates are flagged. The irregularity-detection engine generates an alert only when the following two conditions are met:

  * There is a statistically significant drop in the normalization ratio compared to the previous day.
  * The drop is also significant in absolute terms, with a magnitude of 0.05 or greater.



### Parsing error irregularity detection

For errors that occur during data parsing, the irregularity-detection engine uses a ratio-based method. The irregularity-detection engine triggers an alert if the proportion of parser errors relative to the total number of ingested events increases by 5 percentage points or more compared to the previous day.

## Troubleshooting

The following items explain interface elements of the Health Hub that you may find unexpected or confusing:

  * In the table widgets of the Health Hub, when a field has no data in the selected timeframe, a dash (`-`) is displayed, which represents an empty value. For example, if a feed has been successfully pulling files but the files are empty, Google SecOps isn't ingesting data, so the **Last Ingested** time of the feed displays a dash (`-`)—and the feed displays **Healthy** , unless the volume of the ingested data is irregular.

  * The Health Hub includes historical data for all sources, including feeds that have been deleted, according to the selected time range. If a feed was deleted within the selected time range, the dashboard displays the data for the source up to the point of its deletion. If a source was deleted before the start of the selected time range, no data for that source is displayed.

  * The total parsed log count can be higher than the total ingested log count, because some ingested logs are mapped to more than one normalized log.

  * It's possible that the **Last Collected** timestamp in the **Health Status by Data Source** table is later than the **Last Ingested** timestamp. This is because the **Last Collected** timestamp denotes when Google SecOps received the event—even if the payload is empty, but for empty payloads, ingested timestamps are not recorded. 

  * It's possible that the **Last Event Time** in the **Health Status by Parser** table is later than the **Last Ingested** timestamp. This is because the **Last Event Time** denotes when Google SecOps received the event—even if the payload is empty, but for empty payloads, ingested timestamps are not recorded. 




## What's next

  * [Monitor ingestion data](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-overview)
  * [Learn more about dashboards](https://docs.cloud.google.com/chronicle/docs/reports/dashboards-overview)
  * [Learn how to create a custom dashboard](https://docs.cloud.google.com/chronicle/docs/reports/create-custom-dashboard)
  * [Use Cloud Monitoring for ingestion notifications](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-notifications-for-health-metrics)



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
