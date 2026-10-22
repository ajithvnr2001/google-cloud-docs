---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-pool-update-policy/
title: Configure node pool update policy \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:21:24.468007+00:00
---

# Configure node pool update policy  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-pool-update-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Configure node pool update policy Stay organized with collections  Save and categorize content based on your preferences. 

Node pools are updated in parallel by default. This can potentially cause the following issues:

  * Quota issue

For each node pool, it will create one surge node, so that N node pools will create N surge nodes when they are updated in parallel. This may result in resource exhaustion if there is limited extra capacity for creating those surge nodes.

  * PDB deadlock issue

Draining more than one node at a time could potentially cause PDB deadlocks.




For N node pools to be updated in parallel, there must be N extra IP addresses available for the surge nodes. If your worker nodes get their IP addresses from a [DHCP server](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-ipmode-type-field), then your DHCP server must be able to provide N extra IP addresses. If your worker nodes use static IP addresses, then your [IP block file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-ipmode.ipblockfilepath-field) must contain N extra IP addresses in addition to those needed for the worker nodes.

If there aren't enough extra IP addresses available to update all N nodes in parallel, then we update as many pools as possible in parallel. As IP addresses become available, we update the remaining node pools.

This document shows how to specify a node pool update policy to configure the maximum number of nodes to be updated concurrently during node pool update, which can help avoid the two issues mentioned. 0 means preserving the current parallel behavior, which is the default value. 1 means updating the node pools sequentially.

Note that while sequential update can avoid the two issues, it could make the node pool update process take longer time than updating in parallel.

Note the following limitation with advanced clusters:

  * Version 1.31: node pool update policies aren't supported on [advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enable-advanced-cluster-field).

  * Version 1.32: node pool update policies are supported on advanced clusters.




## Configure node pool update policy

In user cluster seed config user-cluster.yaml, you can configure the node pool update to be done sequentially as follows:
    
    
    nodePoolUpdatePolicy:
      maximumConcurrentNodePoolUpdate: 1
    

The `maximumConcurrentNodePoolUpdate` can be set to an arbitrary integer value to configure the number of node pools you want to update at the same time.

The node pool update policy applies to both node pool update and upgrade, but not create. Also in case any node pool update/upgrade encountered issues and got stuck, the current behavior is that we will block there and won't move on to update next node pool.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
