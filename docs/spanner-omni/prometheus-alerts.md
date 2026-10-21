---
url: https://docs.cloud.google.com/spanner-omni/prometheus-alerts/
title: Use Prometheus alerts to monitor Spanner Omni \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:28:44.375656+00:00
---

# Use Prometheus alerts to monitor Spanner Omni  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner-omni/prometheus-alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner Omni ](https://docs.cloud.google.com/spanner-omni)
  * [ Guides ](https://docs.cloud.google.com/spanner-omni/overview)



Send feedback 

#  Use Prometheus alerts to monitor Spanner Omni Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the Prometheus alerts available for Spanner Omni. Use these alerts to monitor the status and performance of your Spanner Omni deployment.

## TrueTime alerts

Use the following alerts to monitor the status of TrueTime in your deployment:

Alert | Severity | Duration | Description  
---|---|---|---  
`TrueTimeUnavailable` | critical | 1 minute | TrueTime is unavailable for more than 1 minute.  
`ClockSlaViolation` | critical | 1 minute | A server has violated the clock service level agreement (SLA).  
  
## CPU alerts

Use the following alerts to monitor the CPU utilization of your deployment:

Alert | Severity | Duration | Description  
---|---|---|---  
`SpannerHighCPUUtilization` | warning | 5 minutes | Overall CPU utilization has been higher than 65% for more than 5 minutes.  
  
## Storage alerts

Use the following alerts to monitor the storage utilization of your deployment:

Alert | Severity | Duration | Description  
---|---|---|---  
`SpannerStorageUtilizationWarning` | warning | 5 minutes | Spanner Omni storage on a server is high (80%).  
`SpannerStorageUtilizationCritical` | critical | 5 minutes | Spanner Omni storage on a server is high (90%).  
`SpannerStoragePerVCPUTooHigh` | warning | 5 minutes | The storage per vCPU is exceeding 500 GB.  
  
## What's next

  * [Use Grafana dashboards to monitor Spanner Omni](https://docs.cloud.google.com/spanner-omni/grafana-dashboards).

  * [Add encryption to a Spanner Omni Kubernetes deployment](https://docs.cloud.google.com/spanner-omni/deploy-encryption-kubernetes).

  * [Add encryption to a Spanner Omni VM deployment](https://docs.cloud.google.com/spanner-omni/deploy-encryption-vms).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
