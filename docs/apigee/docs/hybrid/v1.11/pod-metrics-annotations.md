---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/pod-metrics-annotations/
title: Pod metrics annotations details \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:37:07.538010+00:00
---

# Pod metrics annotations details  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/pod-metrics-annotations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Pod metrics annotations details Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.11 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.11 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/pod-metrics-annotations.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/pod-metrics-annotations.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/pod-metrics-annotations.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/pod-metrics-annotations.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/pod-metrics-annotations.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/pod-metrics-annotations.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/pod-metrics-annotations.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/pod-metrics-annotations.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/pod-metrics-annotations.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/pod-metrics-annotations.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/pod-metrics-annotations.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/pod-metrics-annotations.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/pod-metrics-annotations.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/pod-metrics-annotations.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/pod-metrics-annotations.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/pod-metrics-annotations.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/pod-metrics-annotations.html)



##  Overview 

Apigee hybrid uses the industry-standard Prometheus add-on for metrics collection. All Apigee hybrid runtime plane applications expose an HTTP(s) endpoint that a [Prometheus](https://prometheus.io/) server can scrape. The Metrics are formatted in [OpenCensus](https://opencensus.io/introduction/) format. 

You can use your own metrics collection and reporting service, keeping in mind that Apigee hybrid metrics are formatted in OpenCensus for scraping by a Prometheus server. 

The following table lists port number and endpoint where hybrid exposes metrics for scraping for each runtime plane pods. 

Apigee component name | Port number | Metrics endpoint  
---|---|---  
Cassandra | `7070` | `/metrics`  
Connect Agent | `7070` | `/metrics`  
Mart | `8843` | `/v1/mart/metrics`  
Redis | `8001` | `/stats/promethues`  
Runtime | `8843` | `/v1/server/metrics`  
Synchronizer | `8843` | `/v1/sync/metrics`  
UDCA | `7070` | `/v1/server/metrics`  
Watcher | `8843` | `/metricz`  
  
###  Example 

The following example shows collecting metrics on the Runtime component from the command line: 
    
    
    kubectl -n apigee port-forward RUNTIME_POD_NAME 8843:8843
    curl -k https://0:8843/v1/server/metrics?type="prometheus"

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
