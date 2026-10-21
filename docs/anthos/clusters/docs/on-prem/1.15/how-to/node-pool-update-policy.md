---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/node-pool-update-policy/
title: Configure node pool update policy \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:11:58.607101+00:00
---

# Configure node pool update policy  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/node-pool-update-policy/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Configure node pool update policy Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/node-pool-update-policy)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/node-pool-update-policy)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



Node pools are updated in parallel by default. This can potentially causing two issues:

  * Quota issue

For each node pool, it will create one surge node, so that N node pools will create N surge nodes when they are updated in parallel. This may result in resource exhaustion if there is limited extra capacity for creating those surge nodes.

  * PDB deadlock issue

Draining more than one node at a time could potentially cause PDB deadlocks.




This doc shows how to specify a node pool update policy to configure the maximum number of nodes to be updated concurrently during node pool update, which can help avoid the two issues mentioned. 0 means preserving the current parallel behavior, which is the default value. 1 means updating the node pools sequentially.

Note that while sequential update can avoid the two issues, it could make the node pool update process take longer time than updating in parallel.

## Configure node pool update policy

In user cluster seed config user-cluster.yaml, you can configure the node pool update to be done sequentially as follows:
    
    
    nodePoolUpdatePolicy:
      maximumConcurrentNodePoolUpdate: 1
    

The `maximumConcurrentNodePoolUpdate` can be set to an arbitrary integer value to configure the number of node pools you want to update at the same time.

The node pool update policy applies to both node pool update and upgrade, but not create. Also in case any node pool update/upgrade encountered issues and got stuck, the current behavior is that we will block there and won't move on to update next node pool.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
