---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/analyze-feed-activity-with-cloud-logging/
title: Analyze feed activity with Cloud Logging \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:29:07.966221+00:00
---

# Analyze feed activity with Cloud Logging  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/analyze-feed-activity-with-cloud-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Analyze feed activity with Cloud Logging

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

This guide helps security engineers and administrators monitor, debug, and troubleshoot ingestion pipelines and feeds within Google SecOps SIEM. For a broader overview of monitoring data ingestion, see [Check data ingestion health](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-overview) and [Troubleshoot data ingestion](https://docs.cloud.google.com/chronicle/docs/ingestion/troubleshooting-ingestion). This guide explains how to send, view, and query ingestion and feed activity logs in Cloud Logging. By using Cloud Logging, you can diagnose issues with log delivery—such as missing, delayed, or failing logs—and decrease the time required to resolve ingestion anomalies. This visibility into push- and pull-based ingestion mechanisms also lets you use Gemini Cloud Assist to investigate logging and metrics telemetry.

## Before you begin

**Important:** Analyzing feed activity with Cloud Logging is only supported for Google SecOps instances configured with a Bring Your Own Project (BYOP) Google Cloud project. If your instance is not configured with a BYOP project, you cannot use this feature. For more information, see [Migrate a Google SecOps instance to a BYOP project](https://docs.cloud.google.com/chronicle/docs/administration/migrate-instance-from-one-project-to-another). 

  * To get the necessary permissions to view logs, ask your administrator to grant you one of the following Identity and Access Management (IAM) roles on your project:

    * **Logs Viewer** (`roles/logging.viewer`)
    * **Private Logs Viewer** (`roles/logging.privateLogViewer`)

For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

  * Understand the cost implications. Cloud Logging is a billable service. A free tier is available as part of the Google Cloud Free Program. For more information, see [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing).




## Key terminology

  * **`chronicle-siem`** : The namespace label for logs associated with the Google SecOps ecosystem.
  * **`chronicle.googleapis.com/ingestion_activity`** : The log ID for the log stream related specifically to Google SecOps data ingestion pipelines.
  * **`storage_transfer_job`** : The resource type for logs from static feeds that use the Storage Transfer Service (STS).
  * **`storagetransfer.googleapis.com/transfer_activity`** : The log ID for STS activity logs.



## Overview of analyzing feed activity

Analyzing feed activity in Cloud Logging involves several key steps:

  1. **Accessing Logs Explorer** : Navigate to the **Logs Explorer** in the Google Cloud console and select the correct Google Cloud project. For more information, see the [Logs Explorer interface](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) documentation.
  2. **Querying logs** : Construct queries to filter logs based on various parameters, such as time ranges, namespaces, log IDs, ingestion mechanisms, feed IDs, or collector IDs. For syntax rules, see [Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language). This guide provides examples for common filtering scenarios.
  3. **Investigating specific feed types** : Learn how to query logs for feeds using different ingestion methods, including those utilizing the Storage Transfer Service (STS), which have unique log formats.
  4. **Using console tools** : Leverage built-in Google SecOps console features, like **Debug with logs** and Gemini Cloud Assist, to streamline the analysis and debugging process.
  5. **Understanding log schema** : Refer to the schema reference to understand the fields and data types within the log payloads, which helps with deeper analysis and troubleshooting.



The following sections provide detailed information to help you effectively monitor the health of your data ingestion pipelines, debug issues, and troubleshoot errors.

## View and query feed activity logs

To view and query feed activity logs, do the following:

  1. Navigate to the **Logs Explorer** page in the Google Cloud console.
  2. Select the Google Cloud project associated with your Google SecOps instance.
  3. Enter a query expression in the **Query** pane to filter the logs.
  4. Click **Run query**.



Example queries for common scenarios are shown in the next few sections.

### Filter by Google SecOps namespace

To retrieve all logs associated with the Google SecOps ecosystem, use the following query:
    
    
    labels.namespace="chronicle-siem"
    

### Filter by ingestion activity log stream

To isolate logs specifically related to data ingestion pipelines, use the following query:
    
    
    log_id("chronicle.googleapis.com/ingestion_activity")
    

### Filter by ingestion mechanism

To target logs for a specific ingestion mechanism, such as third-party APIs, use the `labels.ingestion_mechanism` field in your query:
    
    
    labels.ingestion_mechanism="Third Party API"
    

### Filter by feed ID or collector ID

To view logs for a specific ingestion feed or collector, use the `labels.feed_id` or `labels.collector_id` field. For information on configuring feeds, see [Manage data feeds](https://docs.cloud.google.com/chronicle/docs/administration/feed-management) and [Data feeds overview](https://docs.cloud.google.com/chronicle/docs/administration/feed-management-overview). For collectors, see [Log ingestion and parsing](https://docs.cloud.google.com/chronicle/docs/ingestion/log-ingestion-and-parsing):
    
    
    labels.feed_id="FEED_ID"
    

Replace `FEED_ID` with the unique identifier of your feed.
    
    
    labels.collector_id="COLLECTOR_ID"
    

Replace `COLLECTOR_ID` with the unique identifier of your collector.

### View Storage Transfer Service logs

Logs for static feeds using the Storage Transfer Service (STS) are routed from the tenant environment to your Google Cloud project and use a different resource type and log name. For general information on STS, see the [Storage Transfer Service documentation](https://docs.cloud.google.com/storage-transfer/docs/overview).

  * **Goal** : View STS log activity.   
**Action** : Run the following query: `none resource.type="storage_transfer_job" AND log_id("storagetransfer.googleapis.com/transfer_activity")`

  * **Anticipated failure** : Searching with `log_id("chronicle.googleapis.com/ingestion_activity")` won't show logs for these static feeds.

  * **Corrective step** : Use the `resource.type="storage_transfer_job"` and the specific STS `log_id`.




## Exclude specific logs using Log Router

You have full, granular control over which feed activity logs are routed to Cloud Logging. By configuring exclusion filters in your Google Cloud project, you can stop receiving specific logs, such as logs for a particular feed ID.

To create an exclusion filter and stop receiving specific logs, do the following:

  1. In the Google Cloud console, select your project.
  2. In the search box, search for **Log Router**.
  3. In the **Log Router Sinks** list, click the **More** (three-dot) menu next to the `_Default` sink, and then select **Edit sink**.
  4. On the **Edit sink** page, go to the **Choose logs to filter out of sink (optional)** section and add exclusions as needed.



For example, to filter out Storage Transfer Service (STS) logs, add an exclusion filter and provide the following filter expression:
    
    
    resource.type="storage_transfer_job"
    

If you encounter issues and want to completely disable all feed activity logging, you can open a support case and request this action. Google SecOps can disable logging entirely on their end, but this is an "all-or-nothing" action—it completely disables logs for all feeds for your account, rather than specific lines or feeds.

**Note:** Storage Transfer Service (STS) logs are a special case. Because Google SecOps does not control the upstream STS service that emits these logs, Google SecOps cannot disable them (even using a support case). To stop receiving STS logs, you must use the exclusion filter method described earlier. 

## Use console tools to debug feeds

Google SecOps provides console integrations to access activity logs:

  * **Ask Gemini Cloud Assist** : On the **Feeds** page, select **Ask Gemini Cloud Assist** to open the chat pane. You can ask questions about your feed volumes and errors. For more information, see [Gemini in Google SecOps overview](https://docs.cloud.google.com/chronicle/docs/secops/gemini-secops).
  * **Debug with logs** : On the **Feed management** page, open the action menu for a specific feed and select **Debug with logs**. This option is also available from the **View feed** page. It opens **Logs Explorer** in a new tab, pre-filtered for the selected feed ID.



## Log schema reference

Feed activity logs use a unified JSON payload structure.

### Ingestion activity log fields

Field | Data type | Description  
---|---|---  
`request_start_time` | `string` | Timestamp (RFC 3339) when the activity was initiated.  
`activity_duration` | `string` | Total elapsed duration of the activity (e.g., "1.500s").  
`transfer_id` | `string` | Unique identifier of a specific file or data transfer operation.  
`feed_id` | `string` | Unique identifier of the Google SecOps ingestion feed.  
`collector_id` | `string` | Unique identifier of the collector executing the ingestion.  
`log_type` | `string` | Format of the logs being ingested (e.g., `DUO`, `OFFICE_365`). For a list of format strings, see [Supported default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers).  
`file` | `string` | Name of the processed file or blob container (for file-based sources).  
`request_urls` | `array of strings` | Target URLs used to pull or transfer data (for API-based sources).  
`http_status_code` | `integer` | HTTP status code received from API fetch operations.  
`bytes_transferred` | `integer` | Number of raw bytes successfully transferred during the activity.  
`record_count` | `integer` | Number of individual log entries processed, pulled, or parsed.  
`activity` | `string` | Name of the task being executed (e.g., `File Processing`, `File Transfer`).  
`details` | `string` | Additional metadata or details for the ingestion activity.  
`error_details` | `object` | Detailed error information if the activity encountered a failure. See Error details fields.  
  
### Error details fields

Field | Data type | Description  
---|---|---  
`error_message` | `string` | Human-readable explanation of the error.  
`error_code` | `string` | Error code or identifier (supports numeric and descriptive string codes).  
`error_type` | `string` | Classification or category of the error.  
`is_retriable` | `boolean` | Indicates whether the operation that caused the error can be retried.  
  
### Sample log payloads

#### Successful ingestion activity log example
    
    
    {
      "request_start_time": "2026-06-30T19:00:00Z",
      "activity_duration": "0.500s",
      "transfer_id": "transfer-12345",
      "feed_id": "feed-998877",
      "collector_id": "collector-abcd",
      "log_type": "WORKDAY_AUDIT",
      "file": "audit_log_2026_06_30.json",
      "request_urls": [
        "https://api.workday.com/ccx/v1/tenant/logs"
      ],
      "http_status_code": 200,
      "bytes_transferred": 4512000,
      "record_count": 12500,
      "activity": "File Processing",
      "details": "Successfully processed and validated 12500 records from Workday."
    }
    

#### Failed ingestion activity log example
    
    
    {
      "request_start_time": "2026-06-30T19:05:00Z",
      "activity_duration": "1.200s",
      "transfer_id": "transfer-12346",
      "feed_id": "feed-998877",
      "collector_id": "collector-abcd",
      "log_type": "WORKDAY_AUDIT",
      "request_urls": [
        "https://api.workday.com/ccx/v1/tenant/logs"
      ],
      "http_status_code": 401,
      "bytes_transferred": 0,
      "record_count": 0,
      "activity": "File Transfer",
      "details": "Authorization failure during API request.",
      "error_details": {
        "error_message": "Invalid API token or credential expired.",
        "error_code": "401",
        "error_type": "AUTHORIZATION_ERROR",
        "is_retriable": true
      }
    }
    

## Troubleshooting

This section outlines limitations and common issues.

### Limitations

  * **Storage Transfer Service (STS) fields** : Logs for static feeds routed from STS use the resource type `storage_transfer_job` and log name `storagetransfer.googleapis.com/transfer_activity` instead of `chronicle.googleapis.com/ingestion_activity`.
  * **Telemetry correlation** : High-cardinality fields such as `feed_id` are included as metadata labels in logs rather than resource labels in the monitored resource definition. Gemini Cloud Assist correlation capabilities using metadata labels are subject to ongoing evaluation.



### Error remediation

Issue description | Fix  
---|---  
Missing logs for static feeds in standard queries | Ensure you query using the STS-specific resource type `storage_transfer_job` and log ID `storagetransfer.googleapis.com/transfer_activity`. See View Storage Transfer Service logs.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
