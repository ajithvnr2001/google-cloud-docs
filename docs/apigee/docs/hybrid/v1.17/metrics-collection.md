---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/metrics-collection/
title: Metrics collection overview \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:16:09.529736+00:00
---

# Metrics collection overview  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/metrics-collection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Metrics collection overview Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.17 (latest)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/metrics-collection.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/metrics-collection.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/metrics-collection.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/metrics-collection.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/metrics-collection.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/metrics-collection.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/metrics-collection.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/metrics-collection.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/metrics-collection.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/metrics-collection.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/metrics-collection.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/metrics-collection.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/metrics-collection.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/metrics-collection.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/metrics-collection.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/metrics-collection.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/metrics-collection.html)



Apigee hybrid collects operational metrics that you can use to monitor the health of hybrid services, to set up alerts, and so on. Apigee uses Open Telemetry for metrics collection. Once collected, hybrid sends the metrics data to Cloud Operations, at which point you can use the Cloud Operations console for viewing, searching, and analyzing metrics and managing alerts.

The following diagram shows the metrics collection process:

![alt_text](https://docs.cloud.google.com/static/apigee/docs/hybrid/v1.17/images/open-telemetry-arch.png)

As you can see in this diagram, there is one Open Telemetry pod running per node, and it can run on any pod in the node. The Open Telemetry collector scrapes application metrics data from all hybrid services and sends the metrics data to Cloud Operations. You can access metrics data through the Cloud Operations console.

Metrics collection is enabled by default. To disable it, see [Configure metrics collection](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/metrics-enable).

For a list of metrics you can use to analyze proxy traffic, see [Available metrics](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/metrics-view#available_metrics).

## About metrics

Application metrics data is made available on a port as an internal Kubernetes service. Data collected by this service is scraped by the hybrid metrics collector service. You can use the [Monitoring Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer) to select metrics you want to view, such as:

  * read request count
  * read request latency
  * write request count
  * write request latency



For example, you can create a dashboard in Cloud Operations to show your metrics:

![alt_text](https://docs.cloud.google.com/static/apigee/docs/hybrid/v1.17/images/gcp-metricscharts.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
