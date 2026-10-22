---
url: https://docs.cloud.google.com/binary-authorization/docs/on-prem-cloud-monitoring/
title: Monitor metrics for Distributed Cloud \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:02.706863+00:00
---

# Monitor metrics for Distributed Cloud  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/on-prem-cloud-monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  Monitor metrics for Distributed Cloud Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to use [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) for Binary Authorization for Google Distributed Cloud software. Learn more about [Distributed Cloud logging and monitoring](https://docs.cloud.google.com/anthos/gke/docs/on-prem/concepts/logging-and-monitoring).

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## Before you begin

  1. To view Binary Authorization for Distributed Cloud metrics, you must use supported environments:

     * [Distributed Cloud for bare metal](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/overview) 1.14 or later
     * [Distributed Cloud for VMware](https://docs.cloud.google.com/anthos/gke/docs/on-prem/latest/overview) 1.4 or later
  2. To use Cloud Monitoring, make sure the `stackdriver` section of your [User cluster configuration](https://docs.cloud.google.com/anthos/gke/docs/on-prem/how-to/user-cluster-configuration-file#stackdriver-section) file is filled in.




## Set up Cloud Monitoring queries for Binary Authorization

This section shows you how to access Cloud Monitoring and select the Cloud Logging project that stores your GKE cluster logs.

  1. In the **Workspace** combo box, select the project ID from the `stackdriver` section of your [User cluster configuration](https://docs.cloud.google.com/anthos/gke/docs/on-prem/how-to/user-cluster-configuration-file#stackdriver-section).

  2. View Cloud Monitoring:

In the Google Cloud console, go to **Monitoring > Metrics Explorer** or use the following button:

[Go to Monitoring](https://console.cloud.google.com/monitoring/metrics-explorer)

  3. Select the Google Cloud project that you use to store logs and metrics. You can find the Google Cloud project in the `stackdriver.projectID` field of your user cluster configuration file.

  4. Click **Query editor**.

  5. Enter a query into the query editor. You can find Binary Authorization for Distributed Cloud queries in the following sections.




## Example queries

This section provides example Prometheus Query Language (PromQL) queries you can use to monitor Binary Authorization for Distributed Cloud metrics. To learn more about PromQL, see [PromQL for Cloud Monitoring](https://docs.cloud.google.com/monitoring/promql).

### Query for rejected deployments

To view deployment requests that were rejected by the Binary Authorization enforcer, use the following query:
    
    
    {
       "__name__"="kubernetes.io/anthos/apiserver_admission_webhook_rejection_count",
       "monitored_resource"="k8s_container",
       "error_type"="no_error",
       "name"="binaryauthorization.googleapis.com"
    }
    

### Query for system failures

This section describes how to monitor for system failures that prevent normal operation of Binary Authorization for Distributed Cloud.

To monitor for system failures, use the following query:
    
    
    {
       "__name__"="kubernetes.io/anthos/apiserver_admission_webhook_rejection_count",
       "monitored_resource"="k8s_container",
       "error_type"="calling_webhook_error",
       "name"="binaryauthorization.googleapis.com"
    }
    

### Sum the number of webhook calls related to Binary Authorization

To view the total number of webhook calls relating to Binary Authorization, use the following query:
    
    
    count(
       increase({
          "__name__"="kubernetes.io/anthos/apiserver_admission_webhook_admission_duration_seconds",
          "monitored_resource"="k8s_container",
          "name"="binaryauthorization.googleapis.com"
       }[${__interval}])
    )
    

## What's next

  * [Introduction to Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)
  * [PromQL for Cloud Monitoring](https://docs.cloud.google.com/monitoring/promql)
  * [View Binary Authorization for Distributed Cloud audit log entries](https://docs.cloud.google.com/binary-authorization/docs/viewing-on-prem-logs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
