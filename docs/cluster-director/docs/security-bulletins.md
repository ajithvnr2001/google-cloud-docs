---
url: https://docs.cloud.google.com/cluster-director/docs/security-bulletins/
title: Security bulletins \u00a0|\u00a0 Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:41:59.038216+00:00
---

# Security bulletins  |  Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/security-bulletins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Resources ](https://docs.cloud.google.com/cluster-director/docs/resources)



Send feedback 

#  Security bulletins Stay organized with collections  Save and categorize content based on your preferences. 

This document describes all security bulletins that are related to Cluster Director. Use these bulletins to identify known vulnerabilities and apply the recommended mitigations or fixes to protect your infrastructure.

To get the latest security bulletins delivered to you, do one of the following:

  * Add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators).
  * Add the feed URL directly to your feed reader: `https://cloud.google.com/feeds/cluster-director-security-bulletins.xml`



## GCP-2026-060

**Published:** 2026-09-04

### Description

Description | Severity | Notes  
---|---|---  
A security flaw in the Slurm `sbcast` tool (CVE-2026-65107) lets shared library files bypass security checks and can crash nodes in your cluster.

#### What should I do?

Google updated the default OS image families (NVIDIA driver version 580) for Cluster Director on August 27, 2026, to resolve CVE-2026-65107. Other OS images families (NVIDIA driver version 570) won't receive this patch. For more information, see [Image family release notes](https://docs.cloud.google.com/cluster-director/docs/image-family-release-notes).  To protect your clusters, complete the following steps:

  1. Verify the OS image family that your compute and login nodes use.
  2. Based on the OS image family, do one of the following: 
     * **Default OS image family (NVIDIA driver version 580)** : if your compute or login nodes haven't been recreated since August 27, 2026, then recreate the nodes to apply the patch. To recreate the nodes, use one of the following methods: 
       * [ Delete and recreate nodes](https://docs.cloud.google.com/cluster-director/docs/workloads/configure-slurm#power-down-nodes)
       * [ Modify a cluster property that recreates nodes](https://docs.cloud.google.com/cluster-director/docs/manage/modify-cluster)
     * **Non-default OS image family (NVIDIA driver version 570)** : if your compute or login nodes use a non-default OS image family, then [update the nodes to use a default OS image family](https://docs.cloud.google.com/cluster-director/docs/manage/modify-cluster).
**Note** : You don't need to take any action for the controller node. Because Cluster Director manages the controller node, Google updated the node with the necessary patches. 



#### What vulnerabilities are being addressed?

Slurm CVE-2026-65107 | High |  [CVE-2026-65107](https://www.cve.org/CVERecord?id=CVE-2026-65107)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
