---
url: https://docs.cloud.google.com/network-intelligence-center/docs/network-services-monitoring/metrics-reference/
title: Metrics reference \u00a0|\u00a0 Network Intelligence Center - Network Services Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:08:54.703992+00:00
---

# Metrics reference  |  Network Intelligence Center - Network Services Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/network-services-monitoring/metrics-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Network Services Monitoring ](https://docs.cloud.google.com/network-intelligence-center/docs/network-services-monitoring)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/network-services-monitoring/overview)



#  Metrics reference Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes the metrics and metadata labels that Network Services Monitoring uses to visualize service communication paths, identify high-throughput services, and analyze connection health.

## Network metrics

Network Services Monitoring uses the following network metrics (Layer 4).

Metric | Kind | Description  
---|---|---  
`networkservices.googleapis.com/proxy.network.connection.count` | UpDownCounter | Number of network connections managed by the proxy  
`networkservices.googleapis.com/proxy.network.connection.duration` | Histogram | Distribution of connection duration, from establishment to closure  
`networkservices.googleapis.com/proxy.network.connection.resets` | Counter | Cumulative count of connections terminated through a reset (RST) packet  
`networkservices.googleapis.com/proxy.network.connection.timeouts` | Counter | Cumulative count of network connections terminated by the proxy due to a timeout  
`networkservices.googleapis.com/proxy.network.errors` | Counter | Cumulative count of internal errors detected by the proxy  
`networkservices.googleapis.com/proxy.network.io` | Counter | Cumulative number of bytes transmitted and received by the proxy  
`networkservices.googleapis.com/proxy.network.tls.handshake.errors` | Counter | Cumulative count of failed TLS handshakes  
  
Use the following strategies to analyze network metrics:

  * To determine network throughput for a resource, monitor the `proxy.network.io` metric.
  * To identify network errors, timeouts, resets, or failed TLS handshakes, monitor the `proxy.network.errors`, `proxy.network.connection.timeouts`, `proxy.network.connection.resets`, and `proxy.network.tls.handshake.errors` metrics.



## App Hub metadata labels

If a resource is registered in App Hub, the following labels are automatically added to the preceding metrics to identify the source and destination resources:

  * **Source metadata:**
    * `apphub_source_application_container`
    * `apphub_source_application_id`
    * `apphub_source_application_location`
    * `apphub_source_service_criticality_type`
    * `apphub_source_service_environment_type`
    * `apphub_source_service_id`
    * `apphub_source_workload_criticality_type`
    * `apphub_source_workload_environment_type`
    * `apphub_source_workload_id`
  * **Destination metadata:**
    * `apphub_destination_application_container`
    * `apphub_destination_application_id`
    * `apphub_destination_application_location`
    * `apphub_destination_service_criticality_type`
    * `apphub_destination_service_environment_type`
    * `apphub_destination_service_id`
    * `apphub_destination_workload_criticality_type`
    * `apphub_destination_workload_environment_type`
    * `apphub_destination_workload_id`



## What's next

  * Register services and workloads in [App Hub](https://docs.cloud.google.com/app-hub/docs/overview)
  * [Investigate applications, services, and workloads](https://docs.cloud.google.com/monitoring/docs/application-monitoring) in Application Monitoring



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
