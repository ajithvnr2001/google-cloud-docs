---
url: https://docs.cloud.google.com/stackdriver/docs/observability/use-vpc-service-controls/
title: Use VPC Service Controls with Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:01.978809+00:00
---

# Use VPC Service Controls with Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/observability/use-vpc-service-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Use VPC Service Controls with Google Cloud Observability Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the [Google Cloud Observability products and services](https://docs.cloud.google.com/stackdriver/docs) that support VPC Service Controls. These controls let you set up a [service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters) to create a data transfer boundary around Google Cloud resources. For more information, see the [VPC Service Controls documentation](https://docs.cloud.google.com/vpc-service-controls/docs).

Product name | Information  
---|---  
[Cloud Logging](https://docs.cloud.google.com/logging/docs) |  Use this service to send log data to your project, to route that data, and to query that data. You can also use this service to specify where the system creates your log buckets, whether a customer-managed key encrypts the stored data, and whether that data can be accessed by using a BigQuery linked dataset. Service name: `logging.googleapis.com` For details and limitations, see [Supported products: Cloud Logging](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_logging).  
[Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) |  Use this service to send metric data to your project, and to query and visualize that data. You can also monitor your data with alerting policies. Service name: `monitoring.googleapis.com` For details and limitations, see [Supported products: Cloud Monitoring](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_monitoring).  
[Cloud Trace](https://docs.cloud.google.com/trace/docs) |  Use this service to send trace data to your project and to query that data. Service name: `cloudtrace.googleapis.com` For details and limitations, see [Supported products: Cloud Trace](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_trace).  
[Error Reporting](https://docs.cloud.google.com/error-reporting/docs) |  Use this service to identify and aggregate error information. Service name: `clouderrorreporting.googleapis.com` For details and limitations, see [Supported products: Error Reporting](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_errorreporting).  
[Observability API](https://docs.cloud.google.com/stackdriver/docs/reference/api-overview#about-obs-api) |  Use this service to manage scopes and how your data is stored. For example, you can use this API to specify where the system creates your observability buckets, to encrypt that data with a customer-managed key, and to make that data accessible through a BigQuery linked dataset. Service name: `observability.googleapis.com` For details and limitations, see [Supported products: Observability API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_observability_api).  
[Telemetry API](https://docs.cloud.google.com/stackdriver/docs/reference/api-overview#about-oltp-api) |  Use this service to send OTLP-formatted log, metric, and trace data to your project. Service name: `telemetry.googleapis.com` For details and limitations, see [Supported products: Telemetry API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_telemetry).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
