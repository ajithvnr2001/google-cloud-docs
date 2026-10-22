---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/burst-limits/
title: Understand quotas and burst limits \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:35:25.987282+00:00
---

# Understand quotas and burst limits  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/burst-limits/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Understand quotas and burst limits

Supported in:

Google SecOps 

**Caution:** The Ingestion API is [deprecated](https://docs.cloud.google.com/chronicle/docs/deprecations) and will be discontinued on July 20, 2027. To ingest logs into Google SecOps, use the [Chronicle API](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-methods) instead. For details on how to migrate, see [Migrate from legacy SIEM API to Chronicle API](https://docs.cloud.google.com/chronicle/docs/administration/migrate-from-legacy-api-to-chronicle-api).

This document describes quotas and burst limits in Google Security Operations.

## Definition of burst limits

_Burst limits_ are a form of [_service limits_](https://docs.cloud.google.com/chronicle/docs/reference/service-limits) in Google SecOps that act as a _speed limit_ for data ingestion, designed to protect the platform's shared infrastructure from sudden, massive spikes in traffic. A burst limit restricts the rate of ingestion (measured in megabytes per second—MBps, or gigabytes per second—GBps) within a rolling five-minute window.

**Note:** For the definition of _service_ and other terms, see [SecOps Service Specific Terms](https://cloud.google.com/terms/secops/service-terms).

## How burst limits are calculated

Google SecOps assigns burst limits to your Google SecOps tenants based on your purchased annual ingestion volume (purchased capacity) according to your Google SecOps license. 

To accommodate expected variations and unplanned spikes in log traffic, your daily burst limit is provisioned as a specific range, letting you ingest between one and three times (1× to 3×) your expected daily average (calculated as your purchased annual capacity divided by 365 days). This flexible volume allowance is designed to absorb standard ingestion spikes without disrupting your operations. For example, if your purchased annual capacity is 365 TB, your expected daily average is 1 TB. Your provisioned burst limit will strictly fall within the range of 1 TB to 3 TB per day (which translates to a throughput range of roughly 12 MBps to 36 MBps). If your data ingestion consistently exceeds this provisioned 1×–3× range, an increase in your purchased annual capacity will be required.

Burst limits are enforced per Google SecOps customer tenant. 

The following table shows how burst limits correspond to different amounts of purchased capacity:

Example purchased capacity | Burst limit range | 5-minute burst limit | Ingestion at max burst limit (hourly) | Ingestion at max burst limit (daily) | Ingestion at max burst limit (annually)  
---|---|---|---|---|---  
100 TB | 3 - 10 MBps | 0.9 - 3 GB | ~34 GB | ~822 GB | 300 TB  
500 TB | 16 - 48 MBps | 4.8 - 14.4 GB | ~171 GB | ~4 TB | 1.5 PB  
1 PB | 32 - 97 MBps | 9.6 - 29 GB | ~343 GB | ~8 TB | 3 PB  
5 PB | 158 - 476 MBps | 47.4 - 143 GB | ~1.7 TB | ~41 TB | 15 PB  
30 PB | 0.96 - 2.86 GBps | 288 - 858 GB | ~10.3 TB | ~247 TB | 90 PB  
**Note:** A daily volume allowance is still subject to physical throughput constraints in the region. Although Google SecOps accommodates daily volume bursts up to the 3× limit, instantaneous data transfer rates (throughput) are actively managed to provide high availability and prevent resource starvation across the shared regional environment.

Ingestion traffic that includes extreme, sudden velocity spikes may be subject to dynamic rate limiting or temporary throttling to protect regional stability.

During these periods, data may experience ingestion delays until the spike subsides.

For ultra-high throughput requirements, see Custom capacity planning for ultra-high throughput.

## Applicability of burst limits for pull-based feeds

Google SecOps also limits pull-based ingestion to one-third (33%) of the overall burst limit per logtype (across all feeds). This limit is in place to ensure that pull-based ingestion (usually from cloud sources) doesn't exhaust your tenant's overall burst limits and starve data ingestion using push-based methods (such as using Bindplane agents, forwarders, or direct ingestion to Google SecOps APIs).

### Pull-based ingestion methods

Pull-based methods include ingestion methods (referred to as _source types_ in Google SecOps) where Google SecOps actively reaches out to the source API to fetch data. This includes the following source types that are supported on Google SecOps:

  * Third-party APIs
  * Azure Event Hub
  * Direct ingestion from Google Workspace and Google Cloud
  * Cloud Storage
  * Cloud Storage feed (event-driven)
  * Amazon S3 
  * Amazon SQS
  * Azure Blobstore
  * SFTP request
  * HTTP request



For example, if the burst limit for your tenant is set to 150 MBps, and your tenant is ingesting Okta user context logs using a third-party API connector (which is, a pull-based ingestion method), the system limits the ingestion rate of all Okta feeds combined to a maximum of [150/3 =] 50 MBps. This additional limit is applied even if your overall data ingestion rate is within your assigned burst limit.

### Exceptions to logtype-level limits

Although logtype-level limits generally apply to pull-based feeds, the following exceptions apply:

  * **HTTPS webhooks** : This ingestion method is **push** -based and not subject to logtype-level limits. It is, however, subject to the customer tenant's overall burst limit and returns a `HTTP 429` status code when a feed exceeds that limit.
  * **Azure Event Hub** : This is a **pull** -based ingestion method that is not subject to logtype-level limits.



## How burst limits are implemented

The system enforces burst limits in five-minute intervals. For example, if your burst limit is set to 50 MBps, you can ingest up to 15 GB every five minutes. If you ingest all 15 GB in the first two minutes, ingestion is blocked for the remaining three minutes of that window. This limit resets automatically at the start of the next five-minute interval.

Logtype-level limits are enforced in the same manner, but apply at the level of individual logtypes. For example, if you're allocated 5 GB for pull-based feeds every five minutes, and your total ingested data volume for any single logtype exceeds 5 GB in the first two minutes, ingestion is paused for the remaining three minutes of that window. The limit resets automatically at the start of the next five-minute interval.

### What happens to your data if your exceed your burst limits

If you exceed your burst limit, Google SecOps pauses ingestion of additional data, and the following mechanisms are triggered—depending on whether your data is getting ingested using pull-based or push-based methods:

  * **Using pull-based methods** : ingestion is buffered automatically and requires no additional configuration by you, the customer. The data remains stored in buffer storage until the limit resets and Google SecOps resumes data ingestion.
  * **Using push-based methods** : Google SecOps temporarily rejects data ingestion with an HTTP 429 "Too Many Requests" error. This signals your ingestion mechanism to pause, buffer, and retry, ensuring no data is lost.



Using push-based ingestion methods, the responsibility to buffer and retry lies with you, the customer (see Customer responsibilities for data buffering and retry).

### Burst limit rejections are not data loss

It's important to understand that burst limit rejections (HTTP 429) are _not_ data-loss events. A burst limit rejection (HTTP 429 error) is a pause in data ingestion.

By ensuring your push-based systems have adequate disk buffering and retry logic, hitting a burst limit results only in a small delay (ingestion lag), never the permanent loss of security telemetry.

Data loss only occurs if the sending system (for example, the Bindplane agent, the forwarder, or the script) ignores the burst limit rejection error and deletes the log entry instead of storing it for a retry.

## Customer responsibilities for data buffering and retry

Although Google SecOps automatically manages data buffering and retries for data being ingested using pull-based ingestion methods, you are responsible for data buffering and retrying data ingestion using push-based ingestion methods (such as HTTPS webhooks, Bindplane, forwarders, or Cribl). 

**Caution:** The forwarder is [deprecated](https://docs.cloud.google.com/chronicle/docs/deprecations). The forwarder component is being phased out of the Google SecOps platform and will reach end-of-life (EOL) in January 2027. **Apr 1, 2026** : New Google SecOps customers cannot use the forwarder component. **Jan 1, 2027** : The forwarder is officially EOL. No further patches, including security patches, will be released. **Apr 1, 2027** : Data is no longer allowed to be ingested from the forwarder component. **Google recommends using Bindplane for Google SecOps as the primary solution for log collection. For more information, see[Use Bindplane with Google SecOps](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent)**.

You need to configure your systems to automatically buffer and resend data when your burst limit is reached to handle data overflow efficiently.

The following table highlights the key differences in how Google SecOps handles data ingestion when your burst limit is reached for both types of ingestion methods:

Feature | Pull-based ingestion | Push-based ingestion  
---|---|---  
**How it works** | Google SecOps actively reaches out to the source API to fetch data. | Your systems initiate the connection and send data to Google.  
**Responsibility for data buffering and retry** | Google SecOps automatically manages buffering. When the burst limit is reached, Google SecOps pauses ingestion of additional data. The data remains stored in buffer storage until the limit resets and Google SecOps resumes fetching.  
Buffer storage only stores data for up to 90 days, after which the data is dropped. | The customer must manage buffering. When Google SecOps replies with HTTP 429, your sending system must catch this error, save the data to a local queue (disk or memory), and retry sending it later. If your sender is set to "drop on failure," data will be lost.  
**Data source types** | Third-party API, Azure Event Hub, direct ingestion from Google Workspace and Google Cloud, Cloud Storage, Cloud Storage feed (event driven), Amazon S3, Amazon SQS, Azure Blobstore, SFTP request, HTTP request. | Google SecOps forwarder, Bindplane agent, Pub/Sub, Amazon Kinesis Firehose, HTTPS webhook, direct to ingestion API.  
**User action** | Take steps to align your data ingestion volume with your purchased capacity. | Additionally, ensure that your ingestion sources are configured for data retention, buffering, and retrying.  
For more information, see [Buffering and retry configurations for push-based systems](https://docs.cloud.google.com/chronicle/docs/reference/buffering-and-retry-configurations-for-pushbased-systems).  
  
## When buffered data for pull-based feeds gets backfilled

For feeds using pull-based ingestion methods, when your burst limit window resets, Google SecOps backfills buffered data, prioritizing live data over buffered data. This mechanism ensures that your backlog of buffered data doesn't interfere with your incoming live data traffic (which can compound detection delays). 

**Note:** During the backfilling of buffered data, you might observe your buffered data flowing in parallel with your live data. 

## How to view your assigned burst limit

To ascertain the burst limit assigned to your Google SecOps tenant, do the following:

  1. In your Google SecOps console, go to **Dashboards** > **Data Ingestion and Health**.
  2. View the **Burst Limit Graph - Quota Limit**. The graph displays your assigned limit (the flat line) relative to your actual ingestion rate.



## Track if you are approaching or exceeding your burst limit

You can track utilization using the built-in dashboards or using Cloud Monitoring.

### Use Google SecOps dashboards to track if you're approaching or exceeding your burst limit

  * Go to **Dashboards** > **Data Ingestion and Health** and view the following:

    * **Ingestion rate graph** : shows your current throughput.
    * **Burst rejection graph** : shows the volume of logs rejected (HTTP 429 errors) due to exceeding the burst limit.



### Use Cloud Monitoring to track if you're approaching or exceeding your burst limit

You can use the Metrics Explorer in Google Cloud to create custom alerts. We recommend creating an ingestion alert that notifies you when the volume of the bytes ingested exceeds the burst limit threshold. 

Relevant metrics include the following:

  * **Ingested volume** : `chronicle.googleapis.com/ingestion/log/bytes_count`
  * **Rejected volume** : `chronicle.googleapis.com/ingestion/log/quota_rejected_bytes_count



#### Out-of-the-box alert policies

Google SecOps provides out-of-the-box alert policies in Cloud Monitoring that you can enable to monitor your ingestion quota.

To find and enable these policies, perform these steps:

  1. In the Google Cloud console, go to **Monitoring** > **Integrations**.
  2. Select **Chronicle Security** from the list of integrations.
  3. Click the **Alerts** tab.
  4. Review and enable the following sample alert policies: 
     * **Ingestion Quota Limit Approaching Alert Policy** : Detects if your data ingestion volume is approaching the quota limit.
     * **Ingestion Quota Rejection Alert Policy** : Detects if ingestion requests are being rejected due to insufficient ingestion quota (HTTP 429 errors).



#### Examples

The following sections contain example PromQL queries for monitoring and alerting.

##### View your burst limit usage

  * To view your burst limit usage, use the following PromQL query:

`100 * sum(rate(chronicle_googleapis_com:ingestion_log_bytes_count{monitored_resource="chronicle.googleapis.com/Collector"}[10m]))/min(min_over_time(chronicle_googleapis_com:ingestion_quota_limit{monitored_resource="chronicle.googleapis.com/Collector"}[10m]))`




##### View the number of bytes rejected after exceeding the burst limit

  * To view the number of bytes rejected after exceeding the burst limit, use the following PromQL query:

`topk(5, sum by ("collector_id","log_type")(rate({"__name__"="chronicle.googleapis.com/ingestion/log/quota_rejected_bytes_count","monitored_resource"="chronicle.googleapis.com/Collector","quota_type"="SHORT_TERM_DATA_RATE"}[${__interval}])))`




##### Trigger an alert when you reach 70% of your burst limit

  * To trigger an alert when you reach 70% of your burst limit, use the following PromQL query:

`100 * topk(5, sum by ("collector_id","log_type")(rate({"__name__"="chronicle.googleapis.com/ingestion/log/quota_rejected_bytes_count","monitored_resource"="chronicle.googleapis.com/Collector","quota_type"="SHORT_TERM_DATA_RATE"}[${__interval}]))) > 70`


**Note:** The exact query syntax may vary based on your specific monitored resource configuration.

To monitor your daily ingestion volume against contractual limits, use the **Total ingested log size** (`chronicle.googleapis.com/ingestion/log/bytes_count`) metric.

**Note:** Don't use the `chronicle.googleapis.com/ingestion/quota_limit` metric to track your daily contractual ingestion volume, for the following reasons: 

  * The `quota_limit` metric measures proximity to dynamic backend limits rather than actual ingested data volume.
  * Using `quota_limit` for daily volume alerts can cause false alarms when backend thresholds adjust.



For instructions on setting up a daily volume alert policy, see [Set up a sample policy to monitor daily ingestion volume](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-notifications-for-health-metrics#monitor-daily-ingestion-volume). For instructions on setting up other ingestion alerts, see [Analyze ingestion with Cloud Monitoring](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-notifications-for-health-metrics).

For more information about setting up ingestion alerts, see [Using Cloud Monitoring for ingestion for ingestion insights](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-notifications-for-health-metrics).

## Handle burst limit rejections caused by push-based methods

If you encounter rejection errors (HTTP 429) due to hitting your burst limit for incoming data using push-based methods, we recommend that you take the following steps:

  * **Verify buffering** : make sure that your ingestion sources are buffering data and retrying.
  * **Optimize ingestion** : review ingestion scripts and make sure they aren't sending unnecessary data or _storming_ the API with massive batches all at once. Spread out historical data uploads if possible. Filter out redundant data using the data processing pipeline feature.
  * **Wait** : for temporary spikes, it's often sufficient to wait for the five-minute window to reset and then try again.



For some example configurations, see [Buffering and retry configurations for push-based systems](https://docs.cloud.google.com/chronicle/docs/reference/buffering-and-retry-configurations-for-pushbased-systems).

## Custom capacity planning for ultra-high throughput

Notwithstanding anything described in the other sections of this document, data ingestion throughput that exceeds 3 GBps is considered as _ultra-high throughput_. If you are planning large-scale data migrations, anticipating sustained ultra-high throughput, or running architectures that consistently generate massive ingestion bursts, you must engage your account team for custom capacity provisioning.

Because dedicated regional capacity expansion can take several weeks to deploy, please notify Google Cloud support at least 90 days in advance of anticipated extreme ingestion events to make sure your throughput requirements can be addressed. 

## Frequently asked questions

The following sections provide answers to frequently asked questions.

### Can I increase my burst limit?

If you expect your data ingestion volume to permanently increase, you can increase your purchased capacity by contacting your Google SecOps sales representative.

### Can I increase the logtype-level limits for pull-based feeds?

You can increase your logtype-level limits for a specific logtype by raising a request using Google SecOps technical support in advance.

Increasing the logtype-level limit for one logtype doesn't change the limit applied to other logtypes or your overall burst limit.

### Is it possible to track my data backlog?

Not at this time.

### What are possible ways to clear my data backlog?

If you've accumulated a very large data backlog, and want to clear that backlog to free up your burst limit quota, you can do following:

  * Purchase additional capacity to increase your limits.
  * Disable specific feeds that have unexpectedly spiked in volume.
  * Request Google SecOps technical support to drop your backlog.

To drop your backlog, your data feed is temporarily disabled until all retry requests for backfilled data are successfully processed. During this time, you'll not be able to ingest any new data. 

Once your backlog is cleared, your feed is re-enabled, upon which you'll see new data flowing in. Depending on the size of your backlog, this can take anywhere from a few minutes to a few hours.




### Do burst limits also apply to data ingestion into the data processing pipeline?

The ingestion rate limits applicable to data feeds sending raw logs data into the data processing pipeline of Google SecOps are set to be higher than your tenant's burst limit.

If you exceed your burst limit, the data processing pipeline stops accepting additional requests, according to the following:

  * **Using pull-based methods** : ingestion is buffered automatically and requires no additional configuration. 
  * **Using push-based methods** : Google SecOps temporarily rejects the data with an HTTP 429 "Too Many Requests" error. 



Any data that has been transformed after the burst limit is triggered is temporarily buffered in an internal queue until the limit is reset in the subsequent five-minute window.

### What should I do if my burst limit is lower than what I contracted for?

If your burst limit is lower than what you contracted for, contact Google Support (see [Google SecOps Support](https://docs.cloud.google.com/chronicle/docs/getting-support)), and include your expected burst limit.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
