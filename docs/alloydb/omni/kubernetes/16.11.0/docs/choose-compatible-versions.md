---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/choose-compatible-versions/
title: Choose compatible Kubernetes operator and database cluster versions \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 16.11.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:51:35.094160+00:00
---

# Choose compatible Kubernetes operator and database cluster versions  |  AlloyDB Omni using the container orchestrator: 16.11.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/choose-compatible-versions/

This page documents AlloyDB Omni version **16.11.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/overview)



Send feedback 

#  Choose compatible Kubernetes operator and database cluster versions Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.11.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/choose-compatible-versions)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/choose-compatible-versions)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/choose-compatible-versions)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/choose-compatible-versions)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/choose-compatible-versions)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/choose-compatible-versions)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/choose-compatible-versions)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/choose-compatible-versions)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/choose-compatible-versions)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/choose-compatible-versions)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/choose-compatible-versions)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/choose-compatible-versions)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/choose-compatible-versions)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/choose-compatible-versions)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/choose-compatible-versions)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/choose-compatible-versions)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/choose-compatible-versions)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/choose-compatible-versions)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/choose-compatible-versions)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/choose-compatible-versions)



Each version of the AlloyDB Omni Kubernetes operator is compatible with specific database clusters. A database cluster is comprised of two components:

  * **AlloyDB Omni database** : the database used with AlloyDB Omni Kubernetes operator. The current AlloyDB Omni database version is 16.11.0.
  * **Control plane agents** : each database cluster uses multiple control plane agents. Each control plane agent in a database cluster is the same version. Use the `controlPlaneAgentsVersion` parameter in the manifest file to specify the version of the control plane agents. The current control plane agents version is 1.7.0.



To learn how to upgrade the AlloyDB Omni Kubernetes operator, see [Upgrade your AlloyDB Omni Kubernetes operator](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/upgrade-kubernetes-operator-version#upgrade-operator). The update process includes specifying versions of the database and control plane agents in your manifest file.

## AlloyDB Omni Kubernetes operator version compatibility table

The following table lists the supported AlloyDB Omni Kubernetes operator versions and their compatible and recommended database cluster versions:

AlloyDB Omni Kubernetes operator version | Database cluster components  
---|---  
Database version | Control plane agents versions  
**1.7.0 (recommended)** | **18.1.0** | **1.7.0 (recommended)**  
**17.7.0** | **1.7.0 (recommended)**  
**16.11.0** | **1.7.0 (recommended)**  
**15.15.0** | **1.7.0 (recommended)**  
1.6.3 | 17.5.0 | 1.6.0, 1.6.1, 1.6.2, 1.6.3  
16.9.0 | 1.6.0, 1.6.1, 1.6.2, 1.6.3  
15.13.0 | 1.6.0, 1.6.1, 1.6.2, 1.6.3  
16.8.0 | 1.5.0  
15.12.0 | 1.5.0  
15.7.1 | 1.4.0, 1.4.1  
1.6.2 | 17.5.0 | 1.6.0, 1.6.1, 1.6.2  
16.9.0 | 1.6.0, 1.6.1, 1.6.2  
15.13.0 | 1.6.0, 1.6.1, 1.6.2  
16.8.0 | 1.5.0  
15.12.0 | 1.5.0  
15.7.1 | 1.4.0, 1.4.1  
1.6.1 | 17.5.0 | 1.6.0, 1.6.1  
16.9.0 | 1.6.0, 1.6.1  
15.13.0 | 1.6.0, 1.6.1  
16.8.0 | 1.5.0  
15.12.0 | 1.5.0  
15.7.1 | 1.4.0, 1.4.1  
1.6.0 | 17.5.0 | 1.6.0  
16.9.0 | 1.6.0  
15.13.0 | 1.6.0  
16.8.0 | 1.5.0  
15.12.0 | 1.5.0  
15.7.1 | 1.4.0, 1.4.1  
1.5.0 | 16.8.0 | 1.5.0  
15.12.0 | 1.5.0  
16.3.0 | 1.4.0, 1.4.1  
15.7.1 | 1.4.0, 1.4.1  
1.4.1 | 16.3.0 | 1.4.0, 1.4.1  
15.7.1 | 1.4.0, 1.4.1  
1.4.0 | 16.3.0 | 1.4.0  
15.7.1 | 1.4.0  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
