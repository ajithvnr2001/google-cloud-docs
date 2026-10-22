---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/overview/
title: AlloyDB Omni using the container orchestrator overview \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 16.13.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:39:58.908369+00:00
---

# AlloyDB Omni using the container orchestrator overview  |  AlloyDB Omni using the container orchestrator: 16.13.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/overview/

This page documents AlloyDB Omni version **16.13.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/overview)



Send feedback 

#  AlloyDB Omni using the container orchestrator overview Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.13.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/overview)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/overview)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/overview)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/overview)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/overview)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/overview)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/overview)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/overview)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/overview)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/overview)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/overview)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/overview)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/overview)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/overview)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/overview)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/overview)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/overview)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/overview)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/overview)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/overview)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/overview)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/overview)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/overview)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/overview)

AlloyDB Omni for Kubernetes lets you run a powerful, PostgreSQL-compatible database within your own Kubernetes environment. It packages the high-performance AlloyDB for PostgreSQL database into a container, managed by a Kubernetes operator, which simplifies deployment and operations. 

This approach benefits users by providing the advanced features of AlloyDB Omni—such as being more than twice as fast for transactional workloads and up to 100 times faster for analytical queries than standard PostgreSQL—while using Kubernetes for automated management, scaling, and portability across different environments like data centers or private clouds.

Use AlloyDB Omni for Kubernetes when you need a high-performance, scalable PostgreSQL database but you can't use a fully managed cloud service due to regulatory requirements or data sovereignty, or you need to operate in disconnected environments. AlloyDB Omni for Kubernetes is also well-suited for modernizing legacy databases without committing to a full cloud migration, while still benefiting from cloud-native operational practices.

## AlloyDB Omni for Kubernetes use cases

Choose AlloyDB Omni for Kubernetes when you need one or more of the following capabilities:

  * Automated provisioning and API-driven lifecycle management.
  * Configurable high availability (HA) to fine-tune failover mechanisms.
  * Sidecar support for integrating enterprise backup or monitoring agents.
  * Variable read pools for scaling read-only operations.
  * Load balancing with server-side connection pooling (PgBouncer).
  * Platform support and marketplace availability for Google Distributed Cloud and OpenShift.
  * Cross-region disaster recovery (DR) to create standby databases in remote clusters, data centers, and regions.



## How it works

AlloyDB Omni uses Kubernetes through a dedicated AlloyDB Omni Kubernetes operator to automate the deployment and management of AlloyDB Omni instances in a Kubernetes cluster.

The following describes how AlloyDB Omni for Kubernetes works:

  1. Operator deployment: the AlloyDB Omni operator is installed into your Kubernetes cluster, which can be on Google Cloud (GKE), AWS (EKS), Azure (AKS), [OpenShift](https://catalog.redhat.com/en/software/container-stacks/detail/6837eb3b9137db6941d32436#overview), or on-premises.
  2. Custom Resources: the AlloyDB Omni operator defines Kubernetes Custom Resource Definitions (CRDs), including [`DBCluster`](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/reference/kubernetes-crds-1.6.0/dbcluster). Users interact with AlloyDB Omni by creating and managing these [`DBCluster`](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/reference/kubernetes-crds-1.6.0/dbcluster) custom resources using standard Kubernetes tools like `kubectl`.
  3. Lifecycle management: the AlloyDB Omni operator looks for these custom resources and automates the complex tasks involved in the lifecycle management of an AlloyDB Omni database instance.

This database lifecycle includes the following Day 0 and Day 1 operations:

     * Provisioning: setting up the database instance based on the [`DBCluster`](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/reference/kubernetes-crds-1.6.0/dbcluster) specification, including custom port configurations and sidecar container integration.
     * High availability: configuring and managing failover mechanisms, multi-zone topology spread, and read pool scaling to ensure database availability.
     * Disaster recovery: enabling features like cross-region DR with standby databases and rewind trigger functionality.
     * Backups: managing automated backup processes, including reliable backups from standby instances.
     * Updates: handling low-downtime maintenance (LDTM) for minor version upgrades and resource scaling.
     * Security: integrating features like Active Directory for authentication and Transparent Data Encryption (TDE) for data at rest.
  4. Automation: using the AlloyDB Omni operator, you get API-driven lifecycle management for AlloyDB Omni, simplifying operations and allowing you to manage your database instances in a declarative way, consistent with other Kubernetes applications.




The AlloyDB Omni operator is available through different packaging, including Helm Charts and OLM bundles for Kubernetes and OpenShift. For more information, see [Available AlloyDB Omni download and installation options](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/available-download-install-options).

## What's next

  * Learn about the [AlloyDB Omni availability reference architecture](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/database-availability-reference-architecture-overview)
  * [Choose compatible Kubernetes operator and database cluster versions](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/choose-compatible-versions).
  * Choose an [AlloyDB for PostgreSQL download or installation option](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/available-download-install-options).
  * [Install AlloyDB Omni on Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/deploy-kubernetes).
  * [Subscribe to AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/run-alloydb-omni-production#subscribe).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
