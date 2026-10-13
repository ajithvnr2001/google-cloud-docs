---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/upgrade-kubernetes-overview/
title: Kubernetes upgrade overview \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:27:44.344415+00:00
---

# Kubernetes upgrade overview  |  AlloyDB Omni using the container orchestrator: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/upgrade-kubernetes-overview/

This page documents AlloyDB Omni version **18.1.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/overview)



Send feedback 

#  Kubernetes upgrade overview Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.1.0keyboard_arrow_down

  * [ Current (18.3.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/upgrade-kubernetes-overview)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/upgrade-kubernetes-overview)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/upgrade-kubernetes-overview)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/upgrade-kubernetes-overview)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/upgrade-kubernetes-overview)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/upgrade-kubernetes-overview)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/upgrade-kubernetes-overview)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/upgrade-kubernetes-overview)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/upgrade-kubernetes-overview)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/upgrade-kubernetes-overview)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/upgrade-kubernetes-overview)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/upgrade-kubernetes-overview)

This page describes options and use cases for upgrading the AlloyDB Omni Kubernetes operator and the AlloyDB Omni database on Kubernetes. Keeping your AlloyDB Omni installation up to date is essential for security, stability, and access to new features. 

The upgrade process involves the following components:

  * The AlloyDB Omni Kubernetes operator
  * The database cluster

**Important:** You must upgrade the AlloyDB Omni Kubernetes operator before you upgrade the AlloyDB Omni database on Kubernetes. The AlloyDB Omni Kubernetes operator is the control plane that manages your database clusters, and the database upgrade processes rely on having the latest operator version installed.

## Upgrade options

Depending on your needs and environment, you have the following upgrade options:

Upgrade type | Description | When to use it  
---|---|---  
**[Operator upgrade](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/upgrade-kubernetes-operator-version) ** | Upgrade the version of the AlloyDB Omni Kubernetes operator, for example, from 1.4.0 to 1.5.0. | You must upgrade your AlloyDB Omni Kubernetes operator before you can perform database version upgrades. You also must upgrade your operator to get the latest features and fixes for the AlloyDB Omni Kubernetes operator.  
**[Minor database version upgrade](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/upgrade-kubernetes-database-minor-version) ** | Upgrade your database to a newer minor version, for example, from PostgreSQL 15.7.1 to 15.12.0. These upgrades include bug fixes, security patches, and performance improvements. | The minor database upgrade is part of regular maintenance that keeps your database clusters healthy and secure. For high availability (HA) clusters, this process is designed to be low-downtime.  
**[Major database version upgrade](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/upgrade-kubernetes-database-major-version) ** | Upgrade your database to a new major version, for example, from PostgreSQL 15 to 16. | You perform a major version upgrade to take advantage of significant new features and capabilities introduced in the new database version. The major database version upgrade requires careful planning.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
