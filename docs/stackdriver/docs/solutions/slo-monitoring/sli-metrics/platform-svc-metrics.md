---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/sli-metrics/platform-svc-metrics/
title: Using Google Cloud platform and service metrics \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:30.098165+00:00
---

# Using Google Cloud platform and service metrics  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/sli-metrics/platform-svc-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Using Google Cloud platform and service metrics Stay organized with collections  Save and categorize content based on your preferences. 

Applications hosted in Google Cloud that take advantage of services beyond core infrastructure benefit from the observability capabilities built into these services, such as automatic integration with Cloud Monitoring and Cloud Logging.

This section reviews some of the services available in Google Cloud to host request-response and data-processing applications and describes how to use the Monitoring metrics exposed by them as SLIs. It then provides implementation examples and additional resources.

Google Cloud services are grouped into the following types:

  * Request-response services, in which customers explicitly ask a service to do some work and wait for the work to be successfully completed. These services include the following:

    * Cloud Endpoints
    * Cloud Run
    * Cloud Run functions
    * App Engine
    * Google Kubernetes Engine, including Istio on Google Kubernetes Engine

For information on implementing SLIs for these services, see [Request-response services](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/sli-metrics/req-resp-metrics).

  * Data storage and retrieval services, which store or provide data as the response to a request. These services include the following:

    * Cloud Storage
    * Bigtable
    * Spanner
    * Datastore

For information on implementing SLIs for these services, see [Data storage and retrieval services](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/sli-metrics/data-storage-metrics).

  * Data-processing services, which process data provided by customers and return the result of that processing, either as the result of a request or as a continual feed. These services include the following:

    * Dataflow
    * Managed Service for Apache Spark

For information on implementing SLIs for these services, see [Data-processing services](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/sli-metrics/data-proc-metrics).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
