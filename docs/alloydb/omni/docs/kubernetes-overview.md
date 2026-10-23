---
url: https://docs.cloud.google.com/alloydb/omni/docs/kubernetes-overview/
title: AlloyDB Omni using the container orchestrator \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:49.457721+00:00
---

# AlloyDB Omni using the container orchestrator  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/docs/kubernetes-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/omni/docs/overview)



Send feedback 

#  AlloyDB Omni using the container orchestrator Stay organized with collections  Save and categorize content based on your preferences. 

AlloyDB Omni using the container orchestrator refers to the use of Kubernetes as an orchestrator for deploying and managing AlloyDB Omni databases. This deployment model enables automated provisioning and API-driven lifecycle management of your database deployments.

Use the container orchestrator deployment option when you need containerization and orchestration to support highly scalable and manageable database instances, particularly for modern workloads in environments like on-premises, multi-cloud, or Google Distributed Cloud.

## Use cases

The AlloyDB Omni Kubernetes operator supports the following use cases:

  * Automated provisioning and API-driven lifecycle management.
  * Configurable high availability to fine-tune failover mechanisms.
  * Sidecar support for integrating enterprise backup or monitoring agents.
  * Variable read pools for scaling read-only operations.
  * Load balancing with server-side connection pooling with PgBouncer.
  * Platform support and marketplace availability for Google Distributed Cloud and Red Hat OpenShift.
  * Cross-region disaster recovery to create standby databases in remote clusters, data centers, and regions.



You can also pair your Kubernetes deployment with the optional [AlloyDB Omni web user interface](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/install-web-ui), a self-managed web console that provides observability dashboards for cluster instances, system telemetry charts, database sizes, active database flags, columnar engine statistics, and query insights.

## Get started

  * Learn about the [AlloyDB Omni availability reference architecture](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/database-availability-reference-architecture-overview).
  * [Install the AlloyDB Omni Kubernetes operator](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/deploy-kubernetes).
  * [Install the web UI using the container orchestrator](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/install-web-ui).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
