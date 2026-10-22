---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/pdb-violation-timeout/
title: Configure PDB violation timeout \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:21:17.974604+00:00
---

# Configure PDB violation timeout  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/pdb-violation-timeout/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Configure PDB violation timeout Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document shows how to configure a timeout value in case the draining of a cluster node is in violation of a Pod disruption budget (PDB).

When a node is drained, all Pods on the node must be terminated. By default, if the termination of a Pod is in violation of a PDB, the draining of the node is blocked.

In some situations, you might want to configure a maximum time that the draining of a node can be blocked by a PDB violation. For example, you might want to configure a timeout value before you start a cluster update or upgrade. Or you might need to configure a timeout value for a node that is currently blocked from draining by a PDB violation.

## Set a timeout value

Each node is represented by a Machine object.

List the Machine objects in the cluster:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG get machines
    

Replace CLUSTR_KUBECONIFG with the path of the cluster kubeconfig file.

Example output:
    
    
    my-node-pool-7f864959cd-cw472
    my-node-pool-7f864959cd-kh86m
    my-node-pool-7f864959cd-wtpvx
    

Open a Machine object for editing:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG edit machine MACHINE_NAME
    

Replace MACHINE_NAME with the name of the Machine object.

In the editor, add this annotation:
    
    
    onprem.cluster.gke.io/pdb-violation-timeout: TIMEOUT
    

Replace TIMEOUT with a string that specifies the duration of the timeout. Valid time units are "s", "m", "h". Examples of time values are "1h", "1h30m", "10m", and "100s".

If you set the timeout value to "0s", then PDB violations will never time out. This is the same as the default behavior.

Example:
    
    
    apiVersion: cluster.k8s.io/v1alpha1
    kind: Machine
    metadata:
      annotations:
        kubelet-version: 1.23.5-gke.1502
        onprem.cluster.gke.io/gke-on-prem-version: 1.12.0-gke.430
        vm-ip-address: 203.0.113.2
        onprem.cluster.gke.io/pdb-violation-timeout: "5m"
    

Close the editing session.

## Rolling updates

During a rolling update, a new surge machine is created first. Then the old node is drained, and after all the Pods on it have been evicted, the old Machine object and Node object are both deleted. The PDB violation timeout annotation does not persist on the newly created Machine object.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
