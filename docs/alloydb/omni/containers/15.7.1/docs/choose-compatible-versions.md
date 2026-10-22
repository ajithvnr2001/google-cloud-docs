---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/choose-compatible-versions/
title: Choose compatible Kubernetes operator and database cluster versions \u00a0|\u00a0 AlloyDB Omni for containers: 15.7.1 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:26:12.378459+00:00
---

# Choose compatible Kubernetes operator and database cluster versions  |  AlloyDB Omni for containers: 15.7.1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/choose-compatible-versions/

This page documents AlloyDB Omni version **15.7.1** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/overview)
  * [ Reference ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/choose-compatible-versions)



Send feedback 

#  Choose compatible Kubernetes operator and database cluster versions Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.7.1keyboard_arrow_down

  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/choose-compatible-versions)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/choose-compatible-versions)

Each version of the AlloyDB Omni Kubernetes operator is compatible with specific database clusters. A database cluster is comprised of two components: 

  * **AlloyDB Omni database** : the database used with AlloyDB Omni Kubernetes operator. The current AlloyDB Omni database version for PostgreSQL 15 is 15.7.1.

  * **Control plane agents** : each database cluster uses multiple control plane agents. Each control plane agent in a database cluster is the same version. Use the `controlPlaneAgentsVersion` parameter in the manifest file to specify the version of the control plane agents. The current control plane agents version is 1.4.0.




To learn how to upgrade the AlloyDB Omni Kubernetes operator, see [Upgrade your AlloyDB Omni Kubernetes operator](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/upgrade-kubernetes-operator-version#upgrade-operator). The update process includes specifying versions of the database and control plane agents in your manifest file.

## AlloyDB Omni Kubernetes operator version compatibility table

The following table lists the supported AlloyDB Omni Kubernetes operator versions and their compatible and recommended database cluster versions:

AlloyDB Omni Kubernetes operator version | Database cluster components  
---|---  
Database version | Control plane agents versions  
**1.4.0 (recommended)** | **16.3.0** | **1.4.0 (recommended)**  
**15.7.1** | **1.4.0 (recommended)**  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
