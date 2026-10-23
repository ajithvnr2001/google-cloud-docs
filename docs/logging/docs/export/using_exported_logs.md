---
url: https://docs.cloud.google.com/logging/docs/export/using_exported_logs/
title: View logs routed to Cloud Logging buckets \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:25.693206+00:00
---

# View logs routed to Cloud Logging buckets  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/export/using_exported_logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  View logs routed to Cloud Logging buckets Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how you can find log entries that you routed to [Cloud Logging buckets](https://docs.cloud.google.com/logging/docs/store-log-entries). Log buckets are Cloud Logging storage containers in your Google Cloud projects that hold your logs data. You can create log sinks to route all, or just a subset, of your logs to any bucket in Cloud Logging. This flexibility lets you choose which Google Cloud project your logs are stored in and what other logs are stored with them.

Logs that you route to Cloud Logging buckets are available immediately.

For information about viewing logs routed to other destinations, see the following documents:

  * [Cloud Storage](https://docs.cloud.google.com/logging/docs/export/storage)


  * [BigQuery](https://docs.cloud.google.com/logging/docs/export/bigquery)


  * [Pub/Sub](https://docs.cloud.google.com/logging/docs/export/pubsub)



## Before you begin

For instructions about how to create and manage log buckets, see the following documents:

  * [Create a log bucket](https://docs.cloud.google.com/logging/docs/buckets#create_bucket)
  * [Upgrade a bucket to use Observability Analytics](https://docs.cloud.google.com/logging/docs/buckets#upgrade-bucket)



For a conceptual discussion of sinks, see [Overview of routing and storage models: Sinks](https://docs.cloud.google.com/logging/docs/routing/overview#sinks).

For instructions about how to route your logs, see [Route logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/configure_export_v2).

## View logs

To troubleshoot and view individual log entries in a log bucket, do the following:

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. In the **Action** toolbar, select **Refine scope**.
  3. On the **Refine scope** dialog, select **Log view**.
  4. Select one or more log views and then click **Apply**.

For information about how to run queries, see [Build queries in the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/building-queries).




To perform analytics on log entries stored in a log bucket that is upgraded to use Observability Analytics, do the following:

  1. In the Google Cloud console, go to the _manage_search_ **Observability Analytics** page: 

[Go to **Observability Analytics**](https://console.cloud.google.com/logs/analytics)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. In the **Log views** list, find the view, and then select **Query**. The **Query** pane is populated with a default query, which includes the log view that is queried.

You can also enter a query in the **Query** pane, or edit a displayed query.

To query all logs in a log bucket, select the `_AllLogs` view for the log bucket.

  3. In the toolbar, click **Run query**.

The query is executed and the result of the query is shown in the **Results** tab.

You can use the toolbar options to format your query, clear the query, and open the BigQuery SQL reference documentation.

For information about how to run queries, see [Query and view logs in Observability Analytics](https://docs.cloud.google.com/logging/docs/analyze/query-and-view).




## Log entries organization

Logging log entries are [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) objects. Log entries stored in a log bucket can include the `errorGroups` field. This field links a log entry to an error group that Error Reporting identifies. Logging sets this field when storing a log entry in a log bucket.

Log entries with the same log type, referred to as `[LOG_ID]` in the [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) reference, usually have the same format. The following table shows sample log entries:

### syslog

The following is an example of a Compute Engine `syslog`:
    
    
    {
      insertId: "4zymupf98ac6v"
      jsonPayload: {
        message: "Jul 15 13:36:33 my-instance dhclient[328]: DHCPACK of 10.240.0.48 from 169.254.169.254"
      }
      logName: "projects/my-gcp-project-id/logs/syslog"
      receiveTimestamp: "2024-07-15T13:36:33.400534415Z"
      resource: {
        labels: {
          instance_id: "0123456789" (instance_name: my-instance)
          project_id: "my-gcp-project-id"
          zone: "us-central1-a"
        }
        type: "gce_instance"
      }
      timestamp: "2024-07-15T13:36:33.097822178Z"
    }
    

### request_log

The App Engine `request_log` has log entries containing `protoPayload` fields which hold objects of type [`RequestLog`](https://docs.cloud.google.com/logging/docs/reference/v1beta3/rest/v1beta3/RequestLog):
    
    
    {
      httpRequest: {
        status: 200
      }
      insertId: "669525c0000d39d1eab2bb03"
      labels: {1}
      logName: "projects/my-gcp-project-id/logs/appengine.googleapis.com%2Frequest_log"
      operation: {4}
      protoPayload: {
        @type: "type.googleapis.com/google.appengine.logging.v1.RequestLog"
        appEngineRelease: "1.9.71"
        appId: "s~my-gcp-project-id"
        startTime: "2024-07-15T13:36:00.861387Z"
        ...
      }
      receiveTimestamp: "2024-07-15T13:36:01.169966997Z"
      resource: {2}
      spanId: "7925702051311044593"
      timestamp: "2024-07-15T13:36:00.861387Z"
      trace: "projects/my-gcp-project-id/traces/8a4fab4bd4fbafac2a0fa901c1485847"
      resource: {
        labels: {
          module_id: "default"
          project_id: "my-gcp-project-id"
          version_id: "20200221t133337"
          zone: "us14"
        }
        type: "gae_app"
      }
    }
    

### activity

The `activity` log is an Admin Activity [audit log](https://docs.cloud.google.com/logging/docs/audit). Its payload is a JSON representation of the [`AuditLog`](https://docs.cloud.google.com/logging/docs/audit/api/ref/rest/Shared.Types/AuditLog) type:
    
    
    {
      insertId: "dlu8qwc69c"
      labels: {
        compute.googleapis.com/root_trigger_id: "a97f30b1-45ab-4c12-9309-8e8af3bb011f"
      }
      logName: "projects/my-gcp-project-id/logs/cloudaudit.googleapis.com%2Factivity"
      operation: {
        id: "operation-1721047950764-61d48b3bf2b65-1ba1f256-82e9b5fd"
        last: true
        producer: "compute.googleapis.com"
      }
      protoPayload: {
        @type: "type.googleapis.com/google.cloud.audit.AuditLog"
        authenticationInfo: {...}
        methodName: "v1.compute.instances.insert"
        request: {...}
        requestMetadata: {...}
        resourceName: "projects/my-gcp-project-id/zones/us-central1-f/instances/my-instance"
        serviceName: "compute.googleapis.com"
      }
      receiveTimestamp: "2024-07-15T12:52:41.376292847Z"
      resource: {
      labels: {
        instance_id: "2891866457752773984" (instance_name: my-instance)
        project_id: "my-gcp-project-id"
        zone: "us-central1-f"
        }
        type: "gce_instance"
      }
      severity: "NOTICE"
      timestamp: "2024-07-15T12:52:40.965840Z"
    }
    

## Troubleshooting

If logs seem to be missing from your sink's destination or you otherwise suspect that your sink isn't properly routing logs, then see [Troubleshoot routing and sinks](https://docs.cloud.google.com/logging/docs/export/troubleshoot).

## Pricing

For pricing information, see [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing) page. If you route log data to other Google Cloud services, then see the following documents:

  * [Cloud Storage pricing](https://cloud.google.com/storage/pricing)
  * [BigQuery pricing](https://cloud.google.com/bigquery/pricing#data_ingestion_pricing)
  * [Pub/Sub pricing](https://cloud.google.com/pubsub/pricing)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
