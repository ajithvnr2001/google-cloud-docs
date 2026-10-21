---
url: https://docs.cloud.google.com/cluster-director/docs/slurm-controller-versions/
title: Slurm controller versions in Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:42:52.973532+00:00
---

# Slurm controller versions in Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/slurm-controller-versions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  Slurm controller versions in Cluster Director Stay organized with collections  Save and categorize content based on your preferences. 

To match your workload requirements, you can specify the Slurm version that the controller node uses when you create a cluster. This document explains the supported Slurm controller versions in Cluster Director, and the compatibility rules for the controller node and compute nodes in a cluster.

To learn more about how Cluster Director uses Slurm to handle cluster management, job scheduling, and workload orchestration, see [Slurm orchestration in Cluster Director](https://docs.cloud.google.com/cluster-director/docs/orchestration).

## Understand Slurm controller versions

When you create a cluster, Cluster Director deploys and manages the controller node in a fault-tolerant configuration. The controller node runs the Slurm control daemon ([`slurmctld`](https://slurm.schedmd.com/slurmctld.html)) and the database daemon ([`slurmdbd`](https://slurm.schedmd.com/slurmdbd.html)). You can set the Slurm controller version only by using the Google Cloud CLI or REST API.

**Caution:** You can't change the Slurm controller version after you create a cluster. If your workload requires a different version, then you must create a new cluster.

Cluster Director supports the following Slurm controller versions:

  * **26.05** : use this version for new clusters. If you don't specify a Slurm controller version when you create a cluster, then Cluster Director uses version 26.05 by default.

  * **25.05** : use this version for testing and compatibility with existing clusters.




To review which Slurm version an OS image family uses, see [Supported OS images for Cluster Director](https://docs.cloud.google.com/cluster-director/docs/os-images).

## Compute node image compatibility

Slurm requires that the compute nodes in a cluster run a Slurm version that is the same as or earlier than the version that your controller node runs. Compute nodes can't communicate with a controller node that runs an earlier Slurm version.

The following table describes the compatibility between controller versions and compute node versions:

Slurm controller version | Slurm compute node version | Supported? | Details  
---|---|---|---  
26.05 | 26.05 | Yes | The recommended configuration for new clusters.  
26.05 | 25.05 | Yes | The controller node is backward-compatible with older compute nodes.  
25.05 | 25.05 | Yes | The standard configuration for legacy clusters.  
25.05 | 26.05 | No | Attempting to create a cluster or add nodesets to an existing cluster will fail.  
  
To check the Slurm controller version before you add a nodeset to an existing cluster, [view the cluster details](https://docs.cloud.google.com/cluster-director/docs/manage/view-clusters#describe) by using the gcloud CLI or REST API, and then inspect the `orchestrator.slurm.controllerVersion` field.

## What's next

  * [Create a custom cluster](https://docs.cloud.google.com/cluster-director/docs/create/custom-cluster)

  * [Resolve Slurm controller version errors](https://docs.cloud.google.com/cluster-director/docs/troubleshoot/cluster-errors#controller-version-errors)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
