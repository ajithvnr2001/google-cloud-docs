---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/silent-host-monitoring/
title: Configure silent-host monitoring \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:38.320860+00:00
---

# Configure silent-host monitoring  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/silent-host-monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure silent-host monitoring

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains the methods of how Google Security Operations _silent-host monitoring_ (_SHM_) lets you identify hosts in your environment that have gone silent. 

A _silent_ host can signal potential collector stoppages.

## Use Google Cloud Monitoring with ingestion labels for SHM

This method uses Google Cloud Monitoring to monitor log ingestion rates based on ingestion labels for SHM.

**Note:** Ingestion labels identify the parser that normalizes raw log data to structured UDM format. Essentially, any method that you use to send data to Google SecOps supports ingestion labels (such as Bindplane) and is compatible. 

This section describes how to set up this method using [Bindplane](https://bindplane.com/docs/getting-started/quickstart-guide), which includes the following steps:

  1. Configure Bindplane for SHM with Google Cloud Monitoring
  2. Configure the Google Cloud Monitoring threshold for SHM



After you set up a logs pipeline that applies ingestion labels for SHM, you can set up Google Cloud Monitoring alerts per collector—for when the ingestion rate falls below a specified threshold. You can configure the alerts to go to a variety of places outside of Google SecOps and integrate the alerts into a workflow.

Benefits of this method:

  * Monitors ingestion time, not event time.
  * Leverages Cloud Monitoring's advanced alerting capabilities. 



Downsides of this method:

  * Requires a separate configuration outside of Google SecOps.
  * Limited by the number of [ingestion labels](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-metrics-schema#ingestion_api_schema).



### Configure Bindplane for SHM with Google Cloud Monitoring

Google Security Operations Silent Host Monitoring lets you create alerts for ingestion rate changes using Google Cloud Monitoring. It generates alerts per collector and notifies you when the ingestion rate falls below your defined threshold, signaling potential collector stoppages. This feature works with the gRPC API.

The prerequisites to configure Bindplane for SHM with Google Cloud Monitoring are as follows:

  * A deployed [Bindplane server](https://bindplane.com/docs/getting-started/quickstart-guide) that is configured with a [**Google SecOps Standardization** _processor_](https://bindplane.com/docs/resources/processors/google-secops-standardization). 
  * The Google SecOps Standardization processor is configured to add a supported `log_type` and an ingestion label (for example, `ingestion_source`).



To configure Bindplane for SHM with Google Cloud Monitoring, complete the following steps:

  1. Send the hostname of the collector server as an attribute in each log entry.
  2. On the **Log** tab, select **Processors** > **Add Processors** > **Copy Field**.
  3. Configure the **Copy Field** processor: 
     * Enter a short description for the resource.
     * Choose the `Logs` telemetry type.
     * Set the `Copy From` field to `Resources`.
     * Set the `Resource field` field to `host.name`.
     * Set the `Copy To field` field to `Attributes`.
     * Set the `Attributes Field` field, for example, to `chronicle_ingestion_label["ingestion_source"]`.



## Configure the Google Cloud Monitoring threshold for SHM

Define a threshold based on your expected ingestion rate. Lower thresholds detect collector outages; higher thresholds detect upstream log gaps.

After you configure the Google Cloud Monitoring threshold for SHM, we recommend that you monitor the **Chronicle Collector** > **Ingestion** > **Total Ingestion Log Count** metric. For detailed sample-setup instructions, go to [Set up a sample policy to detect silent Google SecOps collection agents](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-notifications-for-health-metrics#detect-collect-agents).

## Use a Google SecOps dashboard for SHM

Use a Google SecOps dashboard to view daily counts for monitoring hosts that have gone silent.

This method is great for high-level daily overviews, but this method does not support alerts, and the results have a latency of up to 6 hours.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
