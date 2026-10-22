---
url: https://docs.cloud.google.com/certificate-manager/docs/v2/cloud-monitoring/
title: Monitor resources using Cloud Monitoring \u00a0|\u00a0 Certificate Manager (2nd gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:22.106872+00:00
---

# Monitor resources using Cloud Monitoring  |  Certificate Manager (2nd gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/v2/cloud-monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager)
  * [ Certificate Manager (2nd gen) ](https://docs.cloud.google.com/certificate-manager/docs/v2/overview)



Send feedback 

#  Monitor resources using Cloud Monitoring Stay organized with collections  Save and categorize content based on your preferences. 

****

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can monitor various operations on resources in Certificate Manager (2nd gen) using [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs). This document lists the metrics that you can use to track your certificate inventory and walks you through how to view them and create alerting policies.

## Certificate Manager metrics

The metrics for Certificate Manager (2nd gen) are as follows:

The "metric type" strings in this table must be prefixed with `certificatemanager.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`map/entries` GA ** _(project)_**   
Certificate map entries   
`GAUGE`, `INT64`, `1`   
**[certificatemanager.googleapis.com/CertificateMap](https://docs.cloud.google.com/monitoring/api/resources#tag_certificatemanager.googleapis.com/CertificateMap)** |  _Current number of map entries inside certificate map. Sampled every 60 seconds. After sampling, data is not visible for up to 3600 seconds._   
`is_primary`: Shows whether map entry is configured as primary.   
`project/certificates` GA ** _(project)_**   
Certificates   
`GAUGE`, `INT64`, `1`   
**[certificatemanager.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_certificatemanager.googleapis.com/Project)** |  _Current number of certificates. Sampled every 60 seconds. After sampling, data is not visible for up to 3600 seconds._   
`scope`: Certificate scope, one of [DEFAULT, EDGE_CACHE].   
`type`: Certificate type, one of [MANAGED, SELF_MANAGED].   
`is_active`: Shows whether certificate is used in serving.   
`project/v2/active_certificates` BETA ** _(project)_**   
Active Certificates   
`GAUGE`, `INT64`, `1`   
**[certificatemanager.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_certificatemanager.googleapis.com/Project)** |  _Current number of active certificates. For this metric, the sampling period is a reporting period, not a measurement period. Measurements are initiated every 3600 seconds. Measurements that take longer than 3600 seconds to complete will delay the start of the next measurement attempt. The last measured value is repeated until the next measurement completes. Sampled every 3600 seconds._   
`authority_type`: The type of CA that issued the certificate, one of [Private, Public].   
`key_algorithm`: The algorithm of the key used to sign the certificate.   
`key_usage_profile`: The use case based on the key usages of the certificate.   
`resource_types`: Shows the associated GCP resource types.   
`project/v2/certificate_expiration` BETA ** _(project)_**   
Certificate Expiration   
`GAUGE`, `DISTRIBUTION`, `s`   
**[certificatemanager.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_certificatemanager.googleapis.com/Project)** |  _The distribution of the seconds left until the notAfter time of long-lived certificates with lifetime greater than 72 hours. For this metric, the sampling period is a reporting period, not a measurement period. Measurements are initiated every 3600 seconds. Measurements that take longer than 3600 seconds to complete will delay the start of the next measurement attempt. The last measured value is repeated until the next measurement completes. Sampled every 3600 seconds._  
`project/v2/certificate_observance_event_count` BETA ** _(project)_**   
Certificate Observance Event Count   
`DELTA`, `INT64`, `1`   
**[certificatemanager.googleapis.com/Project](https://docs.cloud.google.com/monitoring/api/resources#tag_certificatemanager.googleapis.com/Project)** |  _Count of times a new certificate is observed._   
`authority_type`: The type of CA that issued the certificate, one of [Private, Public].   
`key_algorithm`: The algorithm of the key used to sign the certificate.   
`key_usage_profile`: The use case based on the key usages of the certificate.   
  
Table generated at 2026-10-14 20:24:33 UTC.

For more information about monitored resources, see [Monitored resource types](https://docs.cloud.google.com/monitoring/api/resources#tag_certificatemanager.googleapis.com).

## View metrics in Monitoring

To view the metrics for a monitored resource by using the Metrics Explorer, do the following:

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or the app-enabled folder's management project.
  3. In the **Metric** element, expand the **Select a metric** menu, enter `Certificate Manager` in the filter bar, and then use the submenus to select a specific resource type and metric: 
     1. In the **Active resources** menu, select <a href="/monitoring/api/resources#tag_certificatemanager.googleapis.com" 

> **Certificate Manager**.

     2. To select a metric, use the **Active metric categories** and **Active metrics** menus. For a list of metrics, see [**certificatemanager metrics**](https://docs.cloud.google.com/monitoring/api/metrics_gcp#certificatemanager). 
     3. Click **Apply**.
  4. To add filters, which remove time series from the query results, use the [**Filter** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option).

  5. To combine time series, use the menus on the [**Aggregation** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#select_display). For example, to display the CPU utilization for your VMs, based on their zone, set the first menu to **Mean** and the second menu to **zone**.

All time series are displayed when the first menu of the **Aggregation** element is set to **Unaggregated**. The default settings for the **Aggregation** element are determined by the metric type you selected.

  6. For quota and other metrics that report one sample per day, do the following: 
     1. In the **Display** pane, set the **Widget type** to **Stacked bar chart**.
     2. Set the time period to at least one week.



## Create an alerting policy

To monitor your Certificate Manager resources, create alerting policies. Alerting policies notify you by email, SMS, or downstream tools when a particular metric passes a specified threshold.

You can create alerting policies to monitor the values of metrics and to notify you when those metrics violate a condition. 

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. If you haven't created your notification channels and if you want to be notified, then click **Edit Notification Channels** and add your notification channels. Return to the **Alerting** page after you add your channels. 
  3. From the **Alerting** page, select **Create policy**.
  4. To select the metric, expand the **Select a metric** menu and then do the following: 
     1. To limit the menu to relevant entries, enter `Certificate Manager` into the filter bar. If there are no results after you filter the menu, then disable the **Show only active resources & metrics** toggle. 
     2. For the **Resource type** , select <a href="/monitoring/api/resources#tag_certificatemanager.googleapis.com" 

> **Certificate Manager**.

     3. For the **Metric category** , select **Certificate**.
     4. For the **Metric** , select a metric from the [**list of certificate manager metrics**](https://docs.cloud.google.com/monitoring/api/metrics_gcp#certificatemanager).
     5. Select **Apply**.
  5. Click **Next**.
  6. The settings in the **Configure alert trigger** page determine when the alert is triggered. Select a condition type and, if necessary, specify a threshold. For more information, see [Create metric-threshold alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui). 
  7. Click **Next**.
  8. Optional: To add notifications to your alerting policy, click **Notification channels**. In the dialog, select one or more notification channels from the menu, and then click **OK**.
  9. Optional: Update the **Alert autoclose duration**. This field determines when Monitoring closes alerts in the absence of metric data.
  10. Optional: Click **Documentation** , and then add any information that you want included in a notification message.
  11. Click **Alert name** and enter a name for the alerting policy.
  12. Click **Create Policy**.

For more information, see [Alerting overview](https://docs.cloud.google.com/monitoring/alerts). 

## What's next

  * [Audit logging](https://docs.cloud.google.com/certificate-manager/docs/v2/audit-logging)
  * [Troubleshoot issues](https://docs.cloud.google.com/certificate-manager/docs/v2/troubleshoot)
  * [Quotas and limits](https://docs.cloud.google.com/certificate-manager/docs/v2/quotas-and-limits)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
