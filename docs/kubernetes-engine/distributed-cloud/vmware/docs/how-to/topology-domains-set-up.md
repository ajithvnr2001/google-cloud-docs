---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up/
title: Set up topology domains \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:19:41.090979+00:00
---

# Set up topology domains  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Set up topology domains Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page provides an overview of topology domains and guidelines for setting them up.

Setting up a topology domain requires that you enable [advanced cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#enable-advanced-cluster-field). Note the following limitations with the advanced cluster preview:

  * You can enable advanced cluster at cluster creation time for new 1.31 clusters only.
  * After advanced cluster is enabled, you won't be able to upgrade the cluster to 1.32. Only enable advanced cluster in a test environment.



This page is for Admins and architects who define IT solutions and system architecture in accordance with company strategy, and create and manage policies related to user permissions. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Overview

A _topology domain_ is a group of cluster nodes that are considered to be part of the same logical or physical grouping such as a campus or data center. A topology domain should correspond to some underlying hardware or software that has some possibility of correlated failure. For example:

  * Software failure such as different vCenter Servers
  * Hardware failure such as different racks, different power sources, and different buildings



In Google Distributed Cloud (software only) for VMware, as part of setting up a topology domain when you create a cluster, you define a [topology label](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/vsphere-infrastructure-configuration-file#topology-domains-topology-labels). After cluster creation, the topology label is populated to labels of nodes in the topology domain.

To make use of a topology domain, you have the following options:

  * Version 1.32 and higher: Configure cluster-level default topology spread constraints. For details, see [`schedulerConfiguration`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#scheduler-configuration-section).

  * Use the Kubernetes cluster-level default constraint, `"topology.kubernetes.io/zone"`, as the key in the topology label. For more information, see [Built-in default constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/#internal-default-constraints).

  * Configure the `PodTemplate` in your Deployment, StatefulSet, or ReplicaSet, as applicable with the topology label key. In the Pod spec, you use the key in the topology label as the value for the `topologySpreadConstraints.topologyKey` field. This key lets the Kubernetes scheduler distribute Pods across the topology domain to ensure high availability and prevent over-concentration in any single area in case of failure. For more information on configuring `topologySpreadConstraints` in your Pod spec, see [Pod Topology Spread Constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/) in the Kubernetes documentation.




## Example topology domain labels

Suppose you create the following three topology domains when [creating a user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster-topology-domains#fill_in_your_vsphere_infrastructure_configuration_file):
    
    
    ...
    topologyDomains:
    - name: "topology-domain-1"
      topologyLabels:
        "topology.examplepetstore.com/zone": "zone-1"
    ...
    
    
    
    ...
    topologyDomains:
    - name: "topology-domain-2"
      topologyLabels:
        "topology.examplepetstore.com/zone": "zone-2"
    ...
    
    
    
    ...
    topologyDomains:
    - name: "topology-domain-3"
      topologyLabels:
        "topology.examplepetstore.com/zone": "zone-3"
    ...
    

After the cluster is created, you update the Pod spec, for example:
    
    
    ...
    topologySpreadConstraints:
      topologyKey: "topology.examplepetstore.com/zone"
    ...
    

At a high level, the Kubernetes scheduler uses `topology.examplepetstore.com/zone` to separate the cluster nodes into different groups, `zone-1`, `zone-2`, and `zone-3`. Then the scheduler spreads the Pods across these three node groups.

## Guidelines for Topology Domains Setup

To ensure effective use of all clusters resources by the Kubernetes scheduler, we recommend the following guidelines:

  * The topology domains need to be balanced. You should provide nearly equal amounts of CPU and RAM capacity in each topology domain.
  * Provide at least two and preferably three topology domains.
  * Don't spread by more than one topology key.
  * The nodes should have a similar size in each topology domain.
  * If you use [taints and tolerations](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-taints) for workload separation within a cluster, then each node group should meet the previous requirements.



If these guidelines aren't met, then the scheduler will still try to use the full capacity of the cluster, but it might take longer to schedule Pods, and not all Pods will get the expected spreading behavior.

## What's next

  * [Create an admin cluster for use in topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-cluster-topology-domains)
  * [Create a user cluster for use in topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster-topology-domains)
  * [vSphere infrastructure configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/vsphere-infrastructure-configuration-file)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
