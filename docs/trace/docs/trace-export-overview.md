---
url: https://docs.cloud.google.com/trace/docs/trace-export-overview/
title: Trace data exports overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:40:37.751906+00:00
---

# Trace data exports overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/trace-export-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Guides ](https://docs.cloud.google.com/trace/docs/overview)



Send feedback 

#  Trace data exports overview Stay organized with collections  Save and categorize content based on your preferences. 

**Caution** : As of February 18, 2026, the export of span data to BigQuery by using Cloud Trace sinks is [deprecated](https://docs.cloud.google.com/stackdriver/docs/deprecations). Sinks used to export spans to BigQuery will be removed on or after February 18, 2027. You can't create or modify trace sinks. For information about how to view your span data in BigQuery, see [Migrate to Observability Analytics](https://docs.cloud.google.com/trace/docs/analytics-migrate). 

**Beta**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page provides a conceptual overview of exporting trace data using Cloud Trace. You might want to export trace data for the following reasons:

  * To store trace data for a period longer than the default retention period of 30 days.
  * To let you use BigQuery tools to analyze your trace data. For example, using BigQuery, you can identify span counts and quantiles. For information on the query used to generate the following table, see [HipsterShop query](https://docs.cloud.google.com/trace/docs/trace-export-bigquery#hipstershop-query).

![Display the response to the previous query.](https://docs.cloud.google.com/static/trace/images/show-quantiles-12-02.png)


**Note:** Only trace spans ingested through the Cloud Trace API are eligible for export. Trace spans emitted by Google Cloud services or ingested through the Telemetry API are unsupported.

## How exports work

Exporting involves creating a _sink_ for a Google Cloud project. A _sink_ defines a BigQuery dataset as the destination.

You can create a sink by using the Cloud Trace API or by using the Google Cloud CLI.

## Sink properties and terminology

Sinks are defined for a Google Cloud project and have the following properties:

  * **Name** : A name for the sink. For example, a name might be:
        
        "projects/PROJECT_NUMBER/traceSinks/my-sink"
        

where `PROJECT_NUMBER` is the sink's Google Cloud project number and `my-sink` is the sink identifier.

  * **Parent** : The resource in which you create the sink. The parent must be a Google Cloud project:
        
        "projects/PROJECT_ID"
        

The `PROJECT_ID` can either be a Google Cloud project identifier or number.

  * **Destination** : A single place to send trace spans. Trace supports exporting traces to BigQuery. The destination can be sink's Google Cloud project or any other Google Cloud project that is in the same organization.

For example, a valid destination is:
        
        bigquery.googleapis.com/projects/DESTINATION_PROJECT_NUMBER/datasets/DATASET_ID
        

where `DESTINATION_PROJECT_NUMBER` is the Google Cloud project number of the destination, and `DATASET_ID` is the BigQuery dataset identifier.

  * **Writer Identity** : A service account name. The export destination's owner must give this service account permissions to write to the export destination. When exporting traces, Trace adopts this identity for authorization. For increased security, new sinks get a unique service account:
        
        export-PROJECT_NUMBER-GENERATED_VALUE@gcp-sa-cloud-trace.iam.gserviceaccount.com
        

where `PROJECT_NUMBER` is your Google Cloud project number, in Hex, and `GENERATED_VALUE` is a randomly generated value.

You don't create, own, or manage the service account that is identified by the writer identity of a sink. When you create a sink, Trace creates the service account that the sink requires. This service account isn't included in the list of service accounts for your project until it has at least one Identity and Access Management binding. You add this binding when you configure a sink destination.

For information on using the writer identity, see [destination permissions](https://docs.cloud.google.com/trace/docs/trace-export-configure#dest-auth).




## How sinks work

Every time a trace span arrives in a project, Trace exports a copy of the span.

Traces that Trace received before the sink was created cannot be exported.

## Access control

To create or modify a sink, you must have one of the following Identity and Access Management roles:

  * Trace Admin
  * Trace User
  * Project Owner
  * Project Editor



For more information, see [Access control](https://docs.cloud.google.com/logging/docs/access-control).

To export traces to a destination, the sink's writer service account must be permitted to write to the destination. For more information about writer identities, see Sink properties on this page.

## Quotas and limits

Cloud Trace utilizes the [BigQuery streaming API](https://docs.cloud.google.com/bigquery/quotas#streaming_inserts) to send trace spans to the destination. Cloud Trace batches API calls. Cloud Trace doesn't implement a retry or throttling mechanism. Trace spans might not be exported successfully if the amount of data exceeds the destination quotas.

For details on BigQuery quotas and limits, see [Quotas and limits](https://docs.cloud.google.com/bigquery/quotas).

## Pricing

Exporting traces doesn't incur Cloud Trace charges. However, you might incur BigQuery charges. See [BigQuery pricing](https://cloud.google.com/bigquery/pricing) for more information.

### Estimating your costs

BigQuery charges for data ingestion and storage. To estimate your monthly BigQuery costs, do the following:

  1. Estimate the total number of trace spans that are ingested in a month.

For information about how to view usage, see [View usage by billing account](https://docs.cloud.google.com/stackdriver/estimating-bills#billing-acct-usage).

  2. Estimate the streaming requirements based on the number of trace spans ingested.

Each span is written to a table row. Each row in BigQuery requires at least 1024 bytes. Therefore, a _lower bound_ on your BigQuery streaming requirements is to assign 1024 bytes to each span. For example, if your Google Cloud project ingested 200 spans, then those spans require at least 20,400 bytes for the streaming insert.

  3. Use the [Pricing calculator](https://cloud.google.com/products/calculator/) to estimate your BigQuery costs due to storage, streaming inserts, and queries.




### Viewing and managing your BigQuery usage

You can use Metrics Explorer to view your BigQuery usage. You can also create an alerting policy that notifies you if your BigQuery usage exceeds predefined limits. The following table contains the settings to create an alerting policy. You can use the settings in the target pane table when creating a chart or when using [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).

To create an alerting policy that triggers when the ingested [BigQuery](https://docs.cloud.google.com/bigquery/docs) metrics exceed a user-defined level, use the following settings.

#### Steps to create an [alerting policy](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui#create-policy).

To create an alerting policy, do the following:

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. If you haven't created your notification channels and if you want to be notified, then click **Edit Notification Channels** and add your notification channels. Return to the **Alerting** page after you add your channels. 
  3. From the **Alerting** page, select **Create policy**.
  4. To select the resource, metric, and filters, expand the **Select a metric** menu and then use the values in the **New condition** table: 
     1. Optional: To limit the menu to relevant entries, enter the resource or metric name in the filter bar. 
     2. Select a **Resource type**. For example, select **VM instance**.
     3. Select a **Metric category**. For example, select **instance**.
     4. Select a **Metric**. For example, select **CPU Utilization**.
     5. Select **Apply**.
  5. Click **Next** and then configure the alerting policy trigger. To complete these fields, use the values in the **Configure alert trigger** table. 
  6. Click **Next**.
  7. Optional: To add notifications to your alerting policy, click **Notification channels**. In the dialog, select one or more notification channels from the menu, and then click **OK**.

To be notified when alerts are opened and closed, check **Notify on alert closure**. By default, notifications are sent only when alerts are opened.

  8. Optional: Update the **Alert autoclose duration**. This field determines when Monitoring closes alerts in the absence of metric data.
  9. Optional: Click **Documentation** , and then add any information that you want included in a notification message.
  10. Click **Alert name** and enter a name for the alerting policy.
  11. Click **Create Policy**.

**New condition**  
Field |   
Value  
---|---  
**Resource and Metric** | In the **Resources** menu, select **BigQuery Dataset**.  
In the **Metric categories** menu, select **Storage**.  
Select a metric from the **Metrics** menu. Metrics specific to usage include `Stored bytes`, `Uploaded bytes`, and `Uploaded bytes billed`. For a full list of available metrics, see [BigQuery metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b#gcp-bigquery).   
**Filter** | **project_id** : Your Google Cloud project ID.  
**dataset_id** : Your dataset ID.  
**Across time series  
Time series group by** | **dataset_id** : Your dataset ID.  
**Across time series  
Time series aggregation** | `sum`  
  
**Rolling window** | `1 m`  
  
**Rolling window function** | `mean`  
**Configure alert trigger**  
Field |   
Value  
---|---  
**Condition type** | `Threshold`  
**Alert trigger** | `Any time series violates`  
**Threshold position** | `Above threshold`  
**Threshold value** | You determine the acceptable value.  
**Retest window** | `1 minute`  
  
## What's next

To configure a sink, see [Exporting traces](https://docs.cloud.google.com/trace/docs/trace-export-configure).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
