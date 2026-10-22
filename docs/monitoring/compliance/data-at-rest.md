---
url: https://docs.cloud.google.com/monitoring/compliance/data-at-rest/
title: Protecting data at rest \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:57.947289+00:00
---

# Protecting data at rest  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/compliance/data-at-rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Protecting data at rest Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Monitoring encrypts all data at rest by using Google-owned and Google-managed encryption keys, and understanding where customer metadata is stored helps you prevent sensitive data exposure and meet data-security compliance requirements. Because Monitoring doesn't support customer-managed encryption keys (CMEK), this document explains where sensitive data can enter your metrics and configurations, and how to obscure or audit that data.

## Encryption of data at rest

All data at rest within Cloud Monitoring is encrypted using Google-owned and Google-managed encryption keys. For more information, see [Default encryption at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption). Cloud Monitoring doesn't support the use of [customer-managed encryption keys](https://docs.cloud.google.com/kms/docs/cmek) (CMEK) for protecting your data at rest. By default, Monitoring doesn't store sensitive data and isn't intended to be used for Personally Identifiable Information (PII) or other private customer content. You can use Monitoring to store aggregated, unidentifiable user-activity data or second-order event-based aggregated information like request counts and other similar metrics.

However, there are places in Monitoring at which you can inadvertently insert sensitive customer data. Because Cloud Monitoring stores metadata and resource labels, customer data can make its way into Monitoring when you name configurations or perform metadata actions like labeling a resource, annotating an instance, or storing custom resources by using [custom resource definitions (CRDs)](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) in Google Kubernetes Engine.

The rest of this document describes the points at which such data might be inserted and how to look for the capture of such data.

## Possible insertion points

The following table describes the points at which sensitive data might be sent to Cloud Monitoring.

| Google-generated data  
like system-defined metrics  
and built-in dashboards  | Customer-generated data  
like custom or log-based metrics  
and custom dashboards   
---|---|---  
Resource labels | Values derived from customer data, like a VM instance name, or independent of customer data, like a project number | Values containing sensitive data, such as names of not-yet-released hardware  
Metric labels | Values derived from customer data, like a VM instance name, or independent of customer data, like a project number | 

  * Keys, such as showing that a certain dimension of a piece of software exists
  * Values containing sensitive data, such as names of not-yet-released hardware

  
Data points in time series | No action possible; can't be obscured | **Time series in user-defined metrics (custom and log-based metrics) can contain sensitive customer data if your applications intentionally collect it.**  
Metric descriptors | No action possible; can't be obscured | 

  * Display names
  * Descriptions
  * Label keys, such as showing that a certain dimension of a piece of software exists

  
Alerting policies | No action possible; can't be obscured | 

  * Display names of policies and embedded conditions
  * Label keys and values used to filter alerts to certain time series
  * Information provided as documentation
  * If you have policies based on service-level objectives, their configuration might include: 
    * Display name
    * User-specified label keys and values

  
Dashboards | No action possible; can't be obscured | 

  * Display names
  * Text in items on the dashboard
  * Filters and other query dimensions used to select time-series data for charts and other items on the dashboard

  
Notification channels | No action possible; can't be obscured | 

  * Display names
  * Descriptions
  * Labels and values used to define channels

  
Resource groups | No action possible; can't be obscured | 

  * Display names
  * Filters used to designate group membership

  
Uptime checks | No action possible; can't be obscured | 

  * Display names
  * IP addresses and paths
  * Any optional content-matcher strings

  
Metrics scopes | Not applicable | Metadata only  
  
## Protecting sensitive metadata

If you want all data protected by CMEK, then you shouldn't put sensitive information in resource configurations or metadata in Google Cloud. If sensitive data must be used in resource configurations, resource metadata, or label values, we recommend that you protect it by using obscured identifiers in Google Cloud and a mapping table external to Google Cloud.

**Important:** There is no way to obscure the IP addresses, paths, and content-matcher strings used in uptime checks.

If you send sensitive time-series data to Monitoring, the only way to ensure the data is deleted is to [delete your Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). Otherwise, time-series data is deleted only after it reaches the data-retention limit, which is 24 months for user-defined metrics.

## Inspecting data to ensure compliance

You can manually inspect your data in Cloud Monitoring to ensure that it complies with your security standards.

### Configuration data

To ensure that labels and filters used in configuration artifacts like alerting policies are properly obscured, you can retrieve and inspect the configuration data. Inspect the following:

  * Alerting policies, as described in [List and get alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-api#api-list-policy). Alerting policies based on service-level objectives have filters that refer to the SLO, for example:
        
        filter: select_slo_burn_rate("projects/PROJECT_NUMBER/services/SERVICE_ID/serviceLevelObjectives/SLO_ID")
        

You can retrieve the configuration of the SLO by providing the fully qualified name of the SLO from the filter to the [`serviceLevelObjectives.get`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives/get) method.

  * Notification channels, as described in [List notification channels in a project](https://docs.cloud.google.com/monitoring/alerts/using-channels-api#api-list-channels).

  * Uptime-check configurations, as described in [Manage uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks/manage).

  * Custom dashboards, as described in [List dashboards](https://docs.cloud.google.com/monitoring/dashboards/api-dashboard#list).

  * Resource groups, by using the [`groups.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups/list) method.




### Metric data

To inspect metric data, you must consider both the metric descriptors for user-defined metrics and the time-series data written against those descriptors.

#### Metric descriptors

To ensure that the display names, descriptions, and label keys in any metric descriptors are properly obscured, inspect the descriptors, as described in [List metric descriptors](https://docs.cloud.google.com/monitoring/custom-metrics/browsing-metrics#list-metric-descriptors).

  * To search for custom metrics, use the filter: `metric.type = starts_with("custom.googleapis.com")`

  * To search for log-based metrics, use the filter: `metric.type = starts_with("logging.googleapis.com/user")`




#### Time-series data

To ensure that the time-series data itself is properly obscured, retrieve the time-series data, and inspect the values of metric and resource labels and other stored data. Pay particular attention to time-series data collected by custom metrics or log-based metrics. For information on retrieving time-series data, see [Retrieve time-series data](https://docs.cloud.google.com/monitoring/custom-metrics/reading-metrics).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
