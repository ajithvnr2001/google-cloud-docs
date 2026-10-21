---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/creating-clusters/create-clusters-overview/
title: Cluster creation overview \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:14.988296+00:00
---

# Cluster creation overview  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/creating-clusters/create-clusters-overview/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Cluster creation overview Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/creating-clusters/create-clusters-overview)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/creating-clusters/create-clusters-overview)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



When you have finished setting up cluster node machines, [your network](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/plan-ip-addresses), and the other [prerequisites](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/install-prereq), you're almost ready to install Distributed Cloud. The next step is to decide what kinds of clusters to create and choose which tool to use.

## Choose a cluster type

You can create different kinds of clusters in Google Distributed Cloud, including **admin** clusters (to control the resources of your clusters) and **user** clusters (to run workloads). We recommend admin and user cluster deployments if you have multiple clusters in the same data center that you want to manage from a centralized place, and for larger deployments that need isolation between different teams or between development and production workloads.

You can also run Google Distributed Cloud as a single **standalone** cluster, which serves as a user cluster and as an admin cluster. A standalone cluster supports the edge profile, which has significantly reduced system resource requirements and is recommended for edge devices with high resource constraints. In addition, Google Distributed Cloud lets you create **hybrid** clusters that combine administration tasks and workloads, as well as controlling other user clusters.

Each of these configurations has their own advantages and benefits. For more information on deciding which configuration to develop, see [Choose a deployment model](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/install-prep).

## Choose a tool to create clusters

You have your choice of tools for creating clusters and managing cluster lifecycle:

  * The command-line tool `bmctl`, which you run on your admin workstation in your on-premises data center.
  * The Google Cloud console, Google Cloud CLI, or [Terraform](https://www.terraform.io/). These standard tools use the GKE On-Prem API, which runs on Google Cloud infrastructure, and collectively they are referred to as the _GKE On-Prem API clients_.



For information on deciding which tool best suits your needs, see [Choose a tool to create clusters](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/cluster-lifecycle-management-tools).

## More information

For more information on creating and configuring clusters, see the following:

  * Admin clusters:

    * [Create admin clusters using GKE On-Prem API clients](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/creating-clusters/create-admin-cluster-api)
    * [Create admin clusters using `bmctl`](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/creating-clusters/admin-cluster-creation)
  * User clusters

    * [Create user clusters using GKE On-Prem API clients](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/creating-clusters/create-user-cluster-api)
    * [Create user clusters using `bmctl`](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/creating-clusters/user-cluster-creation)
  * [Create standalone clusters](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/creating-clusters/standalone-cluster-creation)

  * [Create hybrid clusters](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/creating-clusters/hybrid-cluster-creation)




## About the creation process

The cluster creation process includes preflight checks and machine initialization. If cluster creation fails after the machine initialization phase (even if preflight checks passed without errors), you must [delete the cluster](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/reset-nodes). This returns the node to a clean state. After deleting the cluster, you can re-attempt to create the cluster after making any needed configuration changes.

The cluster creation process runs health checks when the cluster has been created. This last step verifies that the cluster is in good operating condition. If the cluster doesn't pass all health checks, the create operation fails. When all health checks pass, the create operation finishes successfully.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
