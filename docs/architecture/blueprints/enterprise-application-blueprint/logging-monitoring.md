---
url: https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/logging-monitoring/
title: Logging and monitoring \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:10.353945+00:00
---

# Logging and monitoring  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/logging-monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Logging and monitoring Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-12-13 UTC

This section describes how logging and monitoring work in the enterprise application blueprint for both the developer platform and the applications. [Google Cloud Observability for GKE](https://docs.cloud.google.com/stackdriver/docs/solutions/gke) provides Cloud Logging and Cloud Monitoring services for blueprint applications.

By default, the base source code in the application templates sends logs to `stdout`. Using `stdout` is a best practice for containerized applications because `stdout` lets the platform handle the application logs. The application code is instrumented with Prometheus client libraries to [export application-specific metrics](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#gmp-pod-monitoring). GKE automatically provides metrics for each application, including [Kube State metrics](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/kube_state_metrics), resource utilization, [SRE golden metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/app-performance-metrics#app-perf-ingest), and database instance metrics. For the developer platform team, the platform provides infrastructure, usage, and cross-application traffic metrics.

## Logging storage

Cloud Operations for GKE also lets you collect system and application logs into [central log buckets](https://docs.cloud.google.com/logging/docs/storage). The blueprint also includes a project in each environment folder that's used for storing logs. The enterprise foundation blueprint has a separate [logging project](https://docs.cloud.google.com/architecture/blueprints/security-foundations/detective-controls#centralized-logging) where the aggregate Cloud Audit Logs logs from across the entire Google Cloud organization are exported. The log types most needed by tenants are also separated by tenant. For example, an application developer who works on the `frontend` application might be granted access to only `frontend` container logs and pod logs, and only in the development and non-production environments.

The following table lists log types, locations, and access control granularity.

Access control granularity | Log types | Log storage location  
---|---|---  
Developer platform | Multi-tenant infrastructure logs | Project: `eab-infra-cicd`  
Application factory logs | Project: `eab-app-factory`  
By environment | 

  * Node
  * Cluster control plane
  * Non-tenant containers or pods

| Project: `eab-gke-{env}`Bucket: `_Default`  
  
  * Compute Engine resources that are used by GKE
  * Cloud Service Mesh traffic

| Project: `eab-gke-{env}`  
By environment and tenant | Tenant containers or pods | Project: `eab-gke-{env}`Bucket: per-tenant (scope)  
  
  * Alloy DB sessions
  * Other tenant-owned resources

| Project: `eab-app-{appname}-{env}`  
By tenant | 

  * Application builds
  * Application deploys

| Project: `eab-app-cicd-{appname}`  
  
## Application monitoring

Google Cloud Observability for GKE provides [predefined monitoring dashboards](https://docs.cloud.google.com/monitoring/dashboards) for GKE. The blueprint also enables [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus), which collects metrics from Prometheus exporters and lets you query the data globally using PromQL. PromQL means that you can use familiar tools like Grafana dashboards and PromQL-based alerts. Cloud Service Mesh is enabled to provide you with [dashboards](https://docs.cloud.google.com/service-mesh/docs/observability-overview) in the Google Cloud console to observe and troubleshoot interactions between services and across tenants. The blueprint also includes a project for a [multi-project monitoring metrics scope](https://docs.cloud.google.com/monitoring/settings).

## Threat and vulnerability monitoring

[Security Command Center](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview) provides insight into the overall security posture of the blueprint. Security Command Center Premium tier provides [Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview) for active container-based workloads in GKE. [Web Security Scanner](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview) is used to detect vulnerabilities in your internet-facing services. Web Security Scanner detects vulnerabilities by crawling an HTTP service and following all links, starting at the base URL. Web Security Scanner then exercises as many user inputs and event handlers as possible.

## What's next

  * Read about [operations for both the developer platform and applications](https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/ops-developer-platform-applications) (next document in this series).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-12-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-12-13 UTC."],[],[]] 
