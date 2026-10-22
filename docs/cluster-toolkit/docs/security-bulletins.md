---
url: https://docs.cloud.google.com/cluster-toolkit/docs/security-bulletins/
title: Security bulletins \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:25:16.612825+00:00
---

# Security bulletins  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/security-bulletins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Resources ](https://docs.cloud.google.com/cluster-toolkit/docs/release-notes)



Send feedback 

#  Security bulletins Stay organized with collections  Save and categorize content based on your preferences. 

This document describes all security bulletins that are related to Cluster Toolkit. Use these bulletins to identify known vulnerabilities and apply the recommended mitigations or fixes to protect your infrastructure.

To get the latest security bulletins delivered to you, do one of the following:

  * Add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators).
  * Add the feed URL directly to your feed reader: `/feeds/cluster-toolkit-security-bulletins.xml`



## GCP-2026-062

**Published:** 2026-09-11

### Description

Description | Severity | Notes  
---|---|---  
Multiple security vulnerabilities were discovered in Slurm that affect Cluster Toolkit blueprints that reference specific image versions. These vulnerabilities affect the `slurmstepd` daemon, RPC request handling, and the accounting database.

#### What should I do?

To mitigate these vulnerabilities, upgrade to [ Cluster Toolkit version v1.103.0](https://docs.cloud.google.com/cluster-toolkit/docs/release-notes#v1.103.0) or later, which upgrades Slurm to version 25.11.8 and updates pinned image references. New deployments that use the updated blueprints automatically use the patched image versions. For existing deployments, you must destroy and recreate your Compute Engine instances or cluster by using the updated blueprint. Redeploying directly to a running cluster does not update running compute instances and can cause version mismatches.

#### What vulnerabilities are being addressed?

This bulletin resolves multiple vulnerabilities in Slurm. For more information, see the SchedMD [ Slurm 25.11 release notes](https://github.com/SchedMD/slurm/blob/slurm-25.11/CHANGELOG/slurm-25.11.md). | High | 

  * [CVE-2026-65107](https://www.cve.org/CVERecord?id=CVE-2026-65107)
  * [CVE-2026-65108](https://www.cve.org/CVERecord?id=CVE-2026-65108)
  * [CVE-2026-65109](https://www.cve.org/CVERecord?id=CVE-2026-65109)
  * [CVE-2026-65138](https://www.cve.org/CVERecord?id=CVE-2026-65138)
  * [CVE-2026-65139](https://www.cve.org/CVERecord?id=CVE-2026-65139)
  * [CVE-2026-65140](https://www.cve.org/CVERecord?id=CVE-2026-65140)
  * [CVE-2026-65165](https://www.cve.org/CVERecord?id=CVE-2026-65165)
  * [CVE-2026-65168](https://www.cve.org/CVERecord?id=CVE-2026-65168)

  
  
## GCP-2026-060

**Published:** 2026-09-07

### Description

Description | Severity | Notes  
---|---|---  
A security flaw in the Slurm `sbcast` tool (CVE-2026-65107) lets shared library files bypass security checks and can crash nodes in your cluster.

#### What should I do?

Google updated the supported OS image families (Automated Cloud Images) with patches for CVE-2026-65107 on September 5, 2026. If a node has not been recreated since September 7, 2026, then the node is vulnerable. To apply the patch, do one of the following:

  * **[Power down static nodes](https://docs.cloud.google.com/cluster-toolkit/docs/slurm/manage-static-nodes#update-images)**. Slurm recreates the node with the patched OS image when you submit new jobs.
  * **[Reconfigure a running cluster](https://docs.cloud.google.com/cluster-toolkit/docs/slurm/reconfigure-cluster#reconfigure-partitions-on-running-cluster)**. In the deployment blueprint for your cluster, ensure the image family points to the latest image and redeploy the cluster.



#### What vulnerabilities are being addressed?

Slurm CVE-2026-65107 | High |  [CVE-2026-65107](https://www.cve.org/CVERecord?id=CVE-2026-65107)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
