---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-auto-resize/
title: Automatic node resizing \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:21:01.472690+00:00
---

# Automatic node resizing  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-auto-resize/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Automatic node resizing Stay organized with collections  Save and categorize content based on your preferences. 

In Google Distributed Cloud, you can enable automatic node resizing for a cluster. Resizing means that the CPU and memory resources assigned to a node are adjusted.

If automatic node resizing is enabled for an admin cluster, the add-on nodes in the admin cluster are resized according to the total number of nodes in the admin cluster. For each user cluster, there are one or more control-plane nodes in the admin cluster. So as you create more user clusters, the total number of nodes in the admin cluster increases, and the add-on nodes in the admin cluster are automatically increased in size.

If automatic node resizing is enabled for a user cluster the control-plane nodes for the user cluster are resized according to the number of nodes in the user cluster. So as you add more worker nodes to the user cluster, the control-plane nodes are increased in size. Recall that the control-plane nodes for the user cluster are in the admin cluster.

A [highly available (HA) user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#masternode-replicas-field), user cluster has three control-plane nodes in the admin cluster, and a non-HA user cluster has one control-plane node in the admin cluster. Resizing a node requires that the node be re-created. So when the control-plane node for a non-HA user cluster is resized, there might be a small amount of downtime.

On [advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enable-advanced-cluster-field), automatic node resizing is supported in Google Distributed Cloud version 1.33 and higher but isn't supported in version 1.31 and 1.32.

## Enable node resizing for the add-on nodes of an admin cluster

Do the steps in this section only if your admin cluster has add-on nodes. Whether an admin cluster has add-on nodes depends on the specific configuration and version as follows:

  * **Non-HA admin clusters** : Non-HA admin clusters have one control plane node and two add-on nodes.
  * **HA admin clusters** : 
    * Version 1.16 and lower: HA admin clusters have three control plane nodes and two add-on nodes.
    * Version 1.28 and higher: HA admin clusters don't have add-on nodes. The three nodes are all control plane nodes.



To determine if your cluster has add-on nodes, run the following command:
    
    
    kubectl get nodes --kubeconfig ADMIN_CLUSTER_KUBECONFIG'
    

Replace `ADMIN_CLUSTER_KUBECONFIG` with the path of your admin cluster kubeconfig file.

If your cluster has add-on nodes, enable node resizing for the add-on nodes, as follows:

In your [admin cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#addonnode-autoresize-enabled-field), set `addonNode.autoResize.enabled` to `true`:
    
    
    addonNode:
      autoResize:
        enabled: true
    

For a new admin cluster, complete the instructions in [Creating an admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-cluster).

For an existing admin cluster:
    
    
    gkectl update admin --config ADMIN_CLUSTER_CONFIG --kubeconfig ADMIN_CLUSTER_KUBECONFIG
    

Replace the following:

  * ADMIN_CLUSTER_CONFIG: the path of your admin cluster configuration file

  * ADMIN_CLUSTER_KUBECONFIG: the path of your admin cluster kubeconfig file




## Enable node resizing for the control-plane nodes of a user cluster

In your [user cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#masternode-autoresize-enabled-field), set `masterNode.autoResize.enabled` to `true`:
    
    
    masterNode:
      autoResize:
        enabled: true
    

For a new user cluster, complete the instructions in [Creating a user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster).

For an existing cluster:
    
    
    gkectl update cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG
    

Replace the following:

  * ADMIN_CLUSTER_KUBECONFIG: the path of your admin cluster kubeconfig file

  * USER_CLUSTER_CONFIG: the path of your user cluster configuration file




After automatic node resizing is enabled for a user cluster, any attempt to change the CPU or memory of a control-plane node by running `gkectl update` is rejected. If you want to use `gkectl update` to change the CPU or memory of a user cluster control-plane node, you must disable automatic node resizing.

## Disable node resizing for the add-on nodes of an admin cluster

In your [admin](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#addonnode-autoresize-enabled-field) cluster configuration file, set `addonNode.autoResize.enabled` to `false`:
    
    
    addonNode:
      autoResize:
        enabled: false
    

Update the cluster:
    
    
    gkectl update admin --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config ADMIN_CLUSTER_CONFIG
    

## Disable node resizing for the control-plane nodes of a user cluster

In your [user cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#masternode-autoresize-enabled-field), set `masterNode.autoResize.enabled` to `false`:
    
    
    masterNode:
      autoResize:
        enabled: false
    

Update the cluster:
    
    
    gkectl update cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG
    

When you disable automatic node resizing for a user cluster, the CPU and memory for the control-plane nodes are reconciled to match the CPU and memory values specified in the user cluster configuration file.

## Logs and events

To find the name of the auto resizing Pod:
    
    
    kubectl --kubeconfig ADMIN_KUBECONFIG describe deployment auto-resize-controller
    

The name of the Pod has the form `auto-resize-controller-xxxxx`.

To see the logs from the auto resizing Pod:
    
    
    kubectl --kubeconfig ADMIN_KUBECONFIG logs AUTO_RESIZE_POD_NAME
    

The auto resizing controller generates events on the MachineDeployment objects to give visibility into decisions and actions relevant to resizing.

To find the names of the MachineDeployments:
    
    
    kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG get machinedeployments --all-namespaces
    

To see the events:
    
    
    kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG describe machinedeployment USER_CONTROL_PLANE_NODE_MACHINE_DEPLOYMENT
    kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG describe machinedeployment ADMIN_ADDON_NODE_MACHINE_DEPLOYMENT
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
