---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ssh-cluster-node/
title: Using SSH to connect to a cluster node \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:19:47.167615+00:00
---

# Using SSH to connect to a cluster node  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ssh-cluster-node/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Using SSH to connect to a cluster node Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to SSH into a Google Distributed Cloud cluster node.

This page is for IT administrators and Operators who manage the lifecycle of the underlying tech infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Limitations

The SSH keys for user and admin clusters cannot be changed or rotated after cluster creation. If your security policies require periodic SSH key rotation, recreate the cluster to establish a new SSH key.

## Before you begin

To complete these steps, you need the location of your user and admin cluster `kubeconfig` files. By default, these files are stored in the [directory where you created your admin and user clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-cluster). For more information on `kubeconfig`, see [Configuring cluster access for kubectl](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#kubeconfig) in the GKE documentation.

## Getting the IP addresses of your cluster nodes

Get the IP addresses of your user cluster nodes:
    
    
    kubectl --kubeconfig [USER_CLUSTER_KUBECONFIG] get nodes --output wide
    

where [USER_CLUSTER_KUBECONFIG] is the path of your user cluster's kubeconfig file.

Get the IP addresses of your admin cluster nodes:
    
    
    kubectl --kubeconfig [ADMIN_CLUSTER_KUBECONFIG] get nodes --output wide
    

where [ADMIN_CLUSTER_KUBECONFIG] is the path of your admin cluster's kubeconfig file.

For either command, note the `INTERNAL-IP` field. These are the node IP addresses. The `NAME` field includes the user cluster's name with an appended unique ID. For example, the node named `my-user-cluster-12345678-abcdef` is part of the user cluster named `my-user-cluster`.

## Using SSH to connect to a user cluster node

Get the SSH key for a user cluster:
    
    
    kubectl --kubeconfig [ADMIN_CLUSTER_KUBECONFIG] get secrets -n [USER_CLUSTER_NAME] ssh-keys \
    -o jsonpath='{.data.ssh\.key}' | base64 -d > \
    ~/.ssh/[USER_CLUSTER_NAME].key && chmod 600 ~/.ssh/[USER_CLUSTER_NAME].key

where:

  * [ADMIN_CLUSTER_KUBECONFIG] is the path of your admin cluster's kubeconfig file.

  * [USER_CLUSTER_NAME] is the name of your user cluster. You specified this name when [Creating a user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster).




The preceding command performs the following steps:

  * From the admin cluster, get the `ssh.key` field of a Secret named `ssh-keys` in the [USER_CLUSTER_NAME] namespace.

  * Base64 decode the key.

  * Store the decoded key in the file `~/.ssh/[USER_CLUSTER_NAME].key`.

  * Set appropriate access permissions for the key file.




Use the key to SSH into a user cluster node:
    
    
    ssh -i ~/.ssh/[USER_CLUSTER_NAME].key anthos@[USER_NODE_IP]
    

where [USER_NODE_IP] is the internal IP address of a node in your user cluster, which you gathered previously.

## Using SSH to connect to an admin cluster node

Get the SSH key for the admin cluster:
    
    
    kubectl --kubeconfig [ADMIN_CLUSTER_KUBECONFIG] get secrets -n kube-system sshkeys \
    -o jsonpath='{.data.vsphere_tmp}' | base64 -d > \
    ~/.ssh/admin-cluster.key && chmod 600 ~/.ssh/admin-cluster.key
    

where [ADMIN_CLUSTER_KUBECONFIG] is the path of the admin cluster's kubeconfig file.

The preceding command performs the following steps:

  * From the admin cluster, get the `vsphere_tmp` field of a Secret named `sshkeys` in the `kube-system` namespace.

  * Base64 decode the `vsphere_tmp` field, which is the key.

  * Store the decoded key in the file `~/.ssh/admin-cluster.key`.

  * Set appropriate access permissions for the key file.




Use the key to SSH into an admin cluster node:
    
    
    ssh -i ~/.ssh/admin-cluster.key anthos@[ADMIN_NODE_IP]
    

where [ADMIN_NODE_IP] is the internal IP address of a node in the admin cluster, which you gathered previously.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
