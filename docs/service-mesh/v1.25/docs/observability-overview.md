---
url: https://docs.cloud.google.com/service-mesh/v1.25/docs/observability-overview/
title: Observability overview \u00a0|\u00a0 Cloud Service Mesh v1.25 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:40:27.285564+00:00
---

# Observability overview  |  Cloud Service Mesh v1.25  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.25/docs/observability-overview/

You are viewing archived v1.25 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.25 ](https://docs.cloud.google.com/service-mesh/v1.25/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.25/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Observability overview

Cloud Service Mesh provides _observability_ into the health and performance of your services. To obtain telemetry data, Cloud Service Mesh relies on [sidecar proxies](https://docs.cloud.google.com/service-mesh/v1.25/docs/onboarding/kubernetes-workloads#inject_sidecar_proxies) that you inject as a separate container into the same Pods as your workloads. The proxies intercept all inbound and outbound HTTP traffic to the workloads and report the data to Cloud Service Mesh. With this system, service developers don't have to instrument their code to collect telemetry data.

Cloud Monitoring and Cloud Logging are enabled in your Google Cloud project when you install Cloud Service Mesh. To report telemetry data, each sidecar proxy that is injected into your service Pods calls the Cloud Monitoring API and the Cloud Logging API. The telemetry data is automatically uploaded to the Cloud Service Mesh pages in the Google Cloud console. Note that metrics are displayed only for HTTP services on the Cloud Service Mesh pages in the Google Cloud console.

Cloud Service Mesh provides several preconfigured service dashboards in the Google Cloud console so you don't have to manually set up dashboards and charts. This detailed telemetry enables operators to observe service behavior, and empowers them to troubleshoot, maintain, and optimize their applications.

On the Cloud Service Mesh pages in the Google Cloud console, you can:

  * Get an overview of all services in your mesh, providing you critical, service-level metrics on three of the [four golden signals of monitoring](https://sre.google/sre-book/monitoring-distributed-systems/#xref_monitoring_golden-signals): latency, traffic, and errors.

  * Define, review, and set alerts against service level objectives (SLOs), which summarize your service's user-visible performance.

  * View metric charts for individual services and deeply analyze them with filtering and breakdowns, including by response code, protocol, destination pod, traffic source, and more.

  * Get detailed information about the endpoints for each service, and see how traffic is flowing between services, and what performance looks like for each communication edge.

  * Explore a service topology graph visualization that shows your mesh's services and their relationships.




## What's next

  * [Control access to Cloud Service Mesh in the Google Cloud console](https://docs.cloud.google.com/service-mesh/v1.25/docs/access-dashboard)
  * [Learn about SLOs](https://docs.cloud.google.com/service-mesh/v1.25/docs/observability/slo-overview)
  * [Create an alerting policy on an SLO](https://docs.cloud.google.com/service-mesh/v1.25/docs/observability/alert-policy-slo)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
