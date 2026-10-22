---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-notifications-for-health-metrics/
title: Analyze ingestion with Cloud Monitoring \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:09.413388+00:00
---

# Analyze ingestion with Cloud Monitoring  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-notifications-for-health-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Analyze ingestion with Cloud Monitoring

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Caution:** The Ingestion API and Backstory API described in this document are [deprecated](https://docs.cloud.google.com/chronicle/docs/deprecations) and will be discontinued on July 20, 2027. To ingest data into Google SecOps, use the [Chronicle API](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-methods) instead. For details on how to migrate, see [Migrate from legacy SIEM API to Chronicle API](https://docs.cloud.google.com/chronicle/docs/administration/migrate-from-legacy-api-to-chronicle-api).

This document describes how to use [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) to receive ingestion notifications. Google SecOps uses Cloud Monitoring to send the ingestion notifications. Use this feature for ingestion notifications and ingestion volume viewing. You can integrate email notifications into existing workflows. Notifications are triggered when the ingestion values reach certain predefined levels. In the Cloud Monitoring documentation, notifications are called _alerts_.

**Note:** To monitor the operational status and health of all of your data sources and parsers, go to the [**Health Hub**](https://docs.cloud.google.com/chronicle/docs/reports/data-health-monitoring-and-troubleshooting-dashboard). It includes information about failed and irregular sources and log types, and provides context to diagnose and remediate issues.

## Before you begin

  * Be familiar with [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview).

  * [Configure a Google Cloud project for Google SecOps](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-project).

  * Verify that your Identity and Access Management role includes the permissions in the role `roles/monitoring.alertPolicyEditor`. For more information about roles, see [Control access with IAM](https://docs.cloud.google.com/monitoring/access-control).

  * Familiarize yourself with creating alerting policies in Cloud Monitoring. For information about these steps, see [Create metric-threshold alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui).

  * Configure the notification channel to receive ingestion notifications as email. For information about these steps, see [Create and manage notification channels](https://docs.cloud.google.com/monitoring/support/notification-options).




## Set up ingestion notification for health metrics

To set up notifications that monitor ingestion health metrics specific to Google SecOps, do the following:

  1. In the Google Cloud console, select **Monitoring**.

  2. In the navigation pane, select **Alerting** and then click **Create policy**.

  3. On the **Select a metric** page, click **Select a metric**.

  4. In the **Select a metric** menu, click either of the following:

     * **Active** toggle to filter and display only resources and metrics with data from the last 25 hours. If you don't select this, all resource and metric types are listed.
     * **Org/folder level** toggle to monitor resources and metrics, such as consumer quota usage or BigQuery slot allocation, for your organization and folders.
  5. Select any of the following metrics:

     * Select **Chronicle Collector > Ingestion** and then select either **Total ingested log count** or **Total ingested log size**.

     * Select **Chronicle Collector > Normalizer** and then select either **Total record count** or **Total event count**.

     * Select **Chronicle Log Type > Outofband** and then select either **Total ingested log count (Feeds)** or **Total ingested log size (Feeds)**.

**Note:** To monitor your daily ingestion volume against contractual limits, use the **Total ingested log size** (`chronicle.googleapis.com/ingestion/log/bytes_count`) metric. Don't use the `chronicle.googleapis.com/ingestion/quota_limit` metric to track your daily contractual ingestion volume, for the following reasons: 
     * The `quota_limit` metric measures proximity to dynamic backend limits rather than actual ingested data volume.
     * Using `quota_limit` for daily volume alerts can cause false alarms when backend thresholds adjust.
For a recommended setup, see Set up a sample policy to monitor daily ingestion volume.
  6. Click **Apply**.




### Add a filter

  1. On the **Select a metric** page, click **Add Filter**.

     1. In the filter dialog, select the **collector_id** label, a comparator, and the filter value.

     2. Select one or more of the following filters:

        * **project_id** : ID of the Google Cloud project associated with this resource.

        * **location** : Physical location of the cluster containing the collector object. We recommend that you don't use this field. If you leave this field empty, Google SecOps can use existing information to automatically determine where to store the data.

        * **collector_id** : ID of the collector.

        * **log_type** : Name of the log type.

        * **Metric label** > **namespace** : Namespace of the log.

        * **feed_name** : Name of the feed.

        * **LogType** : Type of log.

        * **Metric label** > **event_type** : Event type determines which fields are included with the event. The event type includes values, such as `PROCESS_OPEN`, `FILE_CREATION`, `USER_CREATION`, and `NETWORK_DNS`.

        * **Metric label** > **state** : Final status of the event or log. The status is one of the following: 

          * `parsed`: The log is successfully parsed.
          * `validated`. The log is successfully validated.
          * `failed_parsing`. The log has parsing errors.
          * `failed_validation`. The log has validation errors.
          * `failed_indexing`. The log has batch indexing errors.
        * **Metric label** > **drop_reason_code** : This field is populated if the ingestion source is the Google SecOps forwarder and indicates the reason why a log was dropped during normalization.

        * **Metric label** > **ingestion_source** : The ingestion source present in the ingestion label when the logs are ingested using the Ingestion API.

     3. Select a special collector ID. The `collector_id` can also be a forwarder ID or a special ID based on the ingestion method: 

        * **aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa** :   
Represents logs from Amazon S3, Amazon SQS, Cloud Storage, Cloud Storage (event driven), Microsoft Azure Blob Storage, third-party API, and HTTP(S) files (non-API).

        * **aaaa1111-aaaa-1111-aaaa-1111aaaa1111** :   
Represents Collection agents, including Bindplane (Google Edition).

        * **aaaa1111-aaaa-1111-aaaa-1111aaaa1112** :   
Bindplane Enterprise (Google Edition).

        * **aaaa1111-aaaa-1111-aaaa-1111aaaa1113** :   
Bindplane Enterprise.

        * **aaaa1111-aaaa-1111-aaaa-1111aaaa1114** :   
Headless collector. This is a Bindplane or OpenTelemetry collector without a Bindplane management layer.

        * **aaaa1111-aaaa-1111-aaaa-1111aaaa1115** :   
Chronicle API. For more information, refer to [Ingestion methods](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-methods). 

        * **aaaa2222-aaaa-2222-aaaa-2222aaaa2222** :   
Logs ingested through the HTTPS Push method. This includes Webhooks, Amazon Kinesis Firehose, and Google Cloud Pub/Sub source type feeds.

        * **aaaa3333-aaaa-3333-aaaa-3333aaaa3333** :   
Cloud Storage logs and includes logs ingested through Event Threat Detection.

        * **aaaa4444-aaaa-4444-aaaa-4444aaaa4444** :   
Logs ingested through Azure Event Hub feed integration. This includes Microsoft Azure Event Hub source type feeds.

        * **bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb** :   
Represents all ingestion sources that use the legacy Backstory Ingestion API or Chronicle API `unstructuredlogentries` method. For more information, see [Google SecOps Ingestion API](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api) and [Ingestion methods](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-methods).

        * **cccccccc-cccc-cccc-cccc-cccccccccccc** :   
Represents all ingestion sources that use the legacy Backstory Ingestion API or Chronicle API `udmevents` method. For more information, see [Google SecOps Ingestion API](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api) and [Ingestion methods](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-methods).

        * **dddddddd-dddd-dddd-dddd-dddddddddddd** :   
Represents any log ingested through internal processes and integrations. For example, a Google Workspace built-in ingestion.

        * **eeeeeeee-eeee-eeee-eeee-eeeeeeeeeeee** :   
Represents the `collector_id` used for `CreateEntities`.

        * **Forwarders** : These have specific collector IDs which are randomly generated.

  2. In the **Transform data** section, do the following:

     1. Set the **Time series aggregation** field to **sum**.
     2. Set the **Time series group by** field to **project_id**.

**Warning:** Failure to complete this step can cause false alerts to occur. This is especially critical in multi-region Google SecOps deployments, where forwarders may generate misleading security data.
  3. Optional: Set up an alert policy with multiple conditions. To create ingestion notifications with multiple conditions within an alert policy, see [Policies with multiple conditions](https://docs.cloud.google.com/monitoring/alerts/concepts-indepth#condition-combiners).




## Google SecOps forwarder metrics and associated filters

The following table describes the available Google SecOps forwarder metrics and the associated filters.

Google SecOps forwarder metric | Filter  
---|---  
Container memory used | `log_type`, `collector_id`  
Container disk used | `log_type`, `collector_id`  
Container cpu_used | `log_type`, `collector_id`  
Log drop_count | `log_type`, `collector_id`, `input_type`, `reason`  
buffer_used | `log_type`, `collector_id`, `buffer_type`, `input_type`  
last_heartbeat | `log_type`, `collector_id`, `input_type`  
  
## Set up a sample policy to detect silent Google SecOps forwarders

The following sample policy detects all the Google SecOps forwarders and sends alerts if the Google SecOps forwarders don't send logs for 60 minutes. This may not be useful for all the Google SecOps forwarders which you want to monitor. For example, you can monitor a single log source across one or many Google SecOps forwarders with a different threshold or exclude Google SecOps forwarders based upon their frequency of reporting.

  1. In the Google Cloud console, select **Monitoring**.   
[Go to Cloud Monitoring](https://console.cloud.google.com/monitoring/alerting)  


  2. Click **Create Policy**.

  3. On the **Select a metric** page, select **Chronicle Collector > Ingestion > Total ingested log count**.

  4. Click **Apply**.

  5. In the **Transform data** section, do the following: 

     1. Set the **Rolling window** to a time of up to 1 hour*.
     2. Set the **Rolling window function** to **mean**.
     3. Set the **Time series aggregation** to **mean**.
     4. Set the **Time series group by** to **collector_id**. If this is not set to group by **collector_id** , then an alert triggers for each log source.
  6. Click **Next**.

  7. Select **Metric absence** and do the following: 

     1. Set **Alert trigger** to **Any time series violates**.
     2. Set **Trigger absence time** to a time of up to 1 hour.
     3. Enter a **name** for the condition and click **Next**.
  8. In the **Notifications and name** section, do the following:

     1. Select a notification channel in the **Use notification channel** field. We recommend that you configure multiple notification channels for redundancy purposes.
     2. Configure notifications on incident closure.
     3. Set policy user labels to an appropriate level. Use this setting to set the alert severity level for a policy.
     4. Enter any documentation you want to send as part of the alert.
     5. Enter a name for the alert policy.

**Note:** To trigger an alert in 60 minutes, set the **combined time** for the **Rolling window** and **Trigger absence time** to 1 hour.

### Add exclusions to a catch-all policy

It may be necessary to exclude certain Google SecOps forwarders from a catch-all policy because they may just have low traffic volumes, or require a more custom alert policy.

  1. In the Google Cloud console, select **Monitoring**.

  2. On the navigation page, select **Alerting** and then in the **Policies** section, select the policy you want to edit.

  3. On the **Policy details** page, click **Edit**.

  4. On the **Edit alerting policy** page, under the **Add filters** section, select **Add a filter** and do the following: 

     1. Select the **collector_id** label and the collector you want to exclude from the policy.
     2. Set the comparator to `!=` and the value to the `collector_id` you want to exclude, and click **Done**.
     3. Repeat for each collector that needs to be excluded. You can also use a regular expression to exclude multiple collectors with only a single filter if you want to use the following format:

`(?:aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa|bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb|cccccccc-cccc-cccc-cccc-cccccccccccc)`

  5. Click **Save Policy**.




## Set up a sample policy to detect silent Google SecOps collection agents

The following sample policy detects all the Google SecOps collection agents and sends alerts if the Google SecOps collection agents don't send logs for 60 minutes. This sample might not be useful for all the Google SecOps collection agents which you want to monitor. For example, you can monitor a single log source across one or many Google SecOps collection agents with a different threshold or exclude Google SecOps collection agents based upon their frequency of reporting.

  1. In the Google Cloud console, select **Monitoring**.   
[Go to Cloud Monitoring](https://console.cloud.google.com/monitoring/alerting)  


  2. Click **Create Policy**.

  3. On the **Select a metric** page, select **Chronicle Collector > Agent > Exporter Accepted Spans Count**.

  4. Click **Apply**.

  5. In the **Transform data** section, do the following:

     1. Set the **Rolling window** to up to 1 hour*.
     2. Set the **Rolling window function** to **mean**.
     3. Set the **Time series aggregation** to **mean**.
     4. Set the **Time series group by** to **collector_id**. If this is not set to group by **collector_id** , then an alert is triggered for each log source.
  6. Click **Next**.

  7. Select **Metric absence** and do the following:

     1. Set **Alert trigger** to **Any time series violates**.
     2. Set **Trigger absence time** to up to 1 hour*.
     3. Enter a **name** for the condition and click **Next**.
  8. In the **Notifications and name** section, do the following:

     1. Select a notification channel in the **Use notification channel** field. We recommend that you configure multiple notification channels for redundancy purposes.
     2. Configure notifications on incident closure.
     3. Set policy user labels to an appropriate level. This is used for setting the severity level of the alert for a policy.
     4. Enter any documentation that you would like to be sent as part of the alert.
     5. Enter a name for the alert policy.

**Note:** To trigger an alert in 60 minutes, the **combined time** for the **Rolling window** and **Trigger absence time** must be set to 1 hour.

## Set up a sample policy to detect failure of a high-availability cluster of firewall servers

The following sample policy detects when both members of an active-passive, high-availability (HA) cluster of Linux firewall servers stop reporting—indicating a failure. 

In the following sample policy, the HA cluster members are named `prod-linux-server-1` and `prod-linux-server-2`. To set up a sample policy to detect failure of a high-availability cluster of firewall servers, do the following:

  1. In the Google Cloud console, select **Monitoring**.   
[Go to Cloud Monitoring](https://console.cloud.google.com/monitoring/alerting)  


  2. Click **Create Policy**.

  3. Set the **Policy configuration mode** to **Builder**.

  4. For **Select a metric** , select **Chronicle Collector > Ingestion > Total ingested log count**.

  5. Click **Apply**.

  6. In the **Add filters** section, enter the following:

`ingestion_source one_of prod-linux-server-1, prod-linux-server-2`

  7. In the **Transform data** section, do the following:

     1. Set the **Rolling window** to **5 min**.
     2. Set the **Rolling window function** to **rate**.
     3. Set the **Time series aggregation** to **mean**.
     4. Set the **Time series group by** to **ingestion_source**.
  8. Click **Next**.

  9. From the **Condition Types** options, select **Metric absence** and do the following:

     1. Set **Alert trigger** to **All time series violate**.

**Note:** When **All time series violate** is selected, if one cluster member stops reporting, nothing happens. An alert triggers only if both cluster members stop reporting for the specified amount of time, because all time series were violated.
     2. Set **Trigger absence time** to **5 min**.

     3. Set the **Condition name** to **Linux-Active-Passive-Firewall-Cluster**. 

  10. Click **Next**.

  11. In the **Notifications and name** section, do the following:

     1. Select a notification channel in the **Use notification channel** field. We recommend that you configure multiple notification channels for redundancy purposes.
     2. Configure notifications on incident closure.
     3. Set policy user labels to an appropriate level. This is used for setting the severity level of the alert for a policy.
     4. Enter any documentation that you want to be sent as part of the alert.
     5. Enter a name for the alert policy.

**Note:** Although one alert policy can include multiple HA clusters, we recommend that you configure one alert policy per HA cluster.

## Set up a sample policy to monitor daily ingestion volume

To monitor your daily ingestion volume against contractual limits, use the **Total ingested log size** (`chronicle.googleapis.com/ingestion/log/bytes_count`) metric.

**Note:** Don't use the `chronicle.googleapis.com/ingestion/quota_limit` metric to track your daily contractual ingestion volume, for the following reasons: 

  * The `quota_limit` metric measures proximity to dynamic backend limits rather than actual ingested data volume.
  * Using `quota_limit` for daily volume alerts can cause false alarms when backend thresholds adjust.



To set up an alerting policy for daily ingestion limits, do the following:

  1. In the Google Cloud console, select **Monitoring**.

  2. Go to **Alerting** :

[Go to Cloud Monitoring](https://console.cloud.google.com/monitoring/alerting)

  3. Click **Create policy**.

  4. On the **Select a metric** page, select **Chronicle Collector > Ingestion > Total ingested log size** (`chronicle.googleapis.com/ingestion/log/bytes_count`).

  5. Click **Apply**.

  6. In the **Transform data** section, configure the following settings:

     * Set **Rolling window** to **1 day** (`86400s`).
     * Set **Rolling window function** to **sum**.
     * Set **Time series aggregation** to **sum**.
     * Set **Time series group by** to **project_id** (`resource.label."project_id"`).
  7. Click **Next**.

  8. Select **Metric threshold** as the condition type.

  9. Configure the threshold settings:

     * Set **Threshold position** to **Above threshold**.
     * Set **Threshold value** to your daily ingestion limit in bytes. For example, enter `400000000000` for 400 GB.
     * Enter a name for the condition.
  10. Click **Next**.

  11. In the **Notifications and name** section, do the following:

     * Select a notification channel in the **Use notification channel** field. For redundancy, configure multiple notification channels.
     * Configure notifications on incident closure.
     * Set policy user labels to an appropriate level. Use this setting to indicate the alert severity level for the policy.
     * Enter any documentation that you want to send as part of the alert.
     * Enter a name for the alert policy.
  12. Click **Create policy**.




## View total ingestion by log type

To view ingestion volumes by log type in Cloud Monitoring, do the following:

  1. On the **Settings** page, select **Profile**.

  2. Select your Cloud Monitoring profile.

  3. On the **Profile** page, type **Integrations** in the search bar.

  4. Select **Metrics explorer**.

  5. Click **promQL** to switch to promQL query mode.

  6. In the **Queries** field, copy the following:

`sum by (log_type) (increase(chronicle_googleapis_com:ingestion_log_bytes_count{monitored_resource="chronicle.googleapis.com/Collector"}[1h]))`

  7. Optional: Filter a specific log type, and include it in the query. 

For example, to view ingestion for the log type `GCP_CLOUDAUDIT`, the query would look like this:

`sum(increase(chronicle_googleapis_com:ingestion_log_bytes_count{monitored_resource="chronicle.googleapis.com/Collector",log_type="GCP_CLOUDAUDIT"}[1h]))`

  8. In the **Results** section, select the **Table** tab to view the summed data.

  9. Optional: Adjust the time range, as needed.




**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
