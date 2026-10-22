---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/best-practices/config/
title: Configuring your metrics scopes \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:55.539535+00:00
---

# Configuring your metrics scopes  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/best-practices/config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Configuring your metrics scopes Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure the metrics scopes of your Google Cloud projects for use with Google Cloud Managed Service for Prometheus.

The ideal Managed Service for Prometheus deployment is different from the typical Prometheus deployment by necessity. Prometheus is highly scoped to its own instance—which is itself typically cluster-scoped—in that rules and queries run on the Prometheus server that collects the data. Because Managed Service for Prometheus sends data to the global backend, [Monarch](https://research.google/pubs/pub50652/), queries must be configured to execute against Monarch, not the local cluster. If you are using managed collection, then the same requirement applies to rules.

![Managed Service for Prometheus uses a global backend for storage, so queries must be configured to run against that backend.](https://docs.cloud.google.com/static/stackdriver/images/gmp-architecture.png)

The data you query using Managed Service for Prometheus is determined by the Cloud Monitoring construct _metrics scope_ , regardless of how you query the data.

## Metrics scopes

A Monitoring metrics scope is a read-time-only construct that lets you query metric data belonging to multiple Google Cloud projects. Every metrics scope is hosted by a designated Google Cloud project, called the _scoping project_.

By default, a project is the scoping project for its own metrics scope, and the metrics scope contains the metrics and configuration for that project. A scoping project can have more than one monitored project in its metrics scope, and the metrics and configurations from all the monitored projects in the metrics scope are visible to the scoping project. A monitored project can also belong to more than one metrics scope.

When you query the metrics in a scoping project, and if that scoping project hosts a multi-project metrics scope, you can retrieve data from multiple projects. If your metrics scope contains all your projects, then your queries and rules evaluate globally.

For more information about scoping projects and metrics scope, see [Metrics scopes](https://docs.cloud.google.com/monitoring/settings#concept-scope). For information about configuring multi-project metrics scope, see [View metrics for multiple projects](https://docs.cloud.google.com/monitoring/settings/multiple-projects).

To minimize the complexity of your permissions model, use as few metrics scopes as possible. If you do not consider your metric data to be sensitive and it is acceptable for all users to be able to access all metrics, then use a single metrics scope that contains all your projects.

## Grouping projects together for querying

The other best-practice scenarios use the following metrics-scope configurations:

| Scope A | Scope B | Scope C  
---|---|---|---  
**Scoping project** | scoping-project-A | scoping-project-B | scoping-project-C  
**Monitored projects** | Project 1  
Project 2 | Project 3  
Project 4 | Project 1  
Project 2  
Project 3  
Project 4  
Project 5  
**IAM-permissioned group**  
(example) | Dev team A | Dev team B | SRE team  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
