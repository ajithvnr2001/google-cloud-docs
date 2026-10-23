---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/remove-static-ip-addresses/
title: Remove static IP addresses from a cluster \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:44.444518+00:00
---

# Remove static IP addresses from a cluster  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/remove-static-ip-addresses/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Remove static IP addresses from a cluster Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to remove static IP addresses from a cluster in Google Distributed Cloud.

When you create a cluster that uses [static IP addresses](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster#network) for the nodes, you specify a set of IP addresses in an [IP block file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ip-block-file). If you later realize that you specified more IP addresses than necessary, you can remove some of the IP addresses from the cluster.

## Remove IP addresses from a user cluster

Ensure that you will have enough IP addresses remaining after the removal. You need one IP address for each cluster node plus an additional IP address to be used for a temporary node during upgrades. For example, if you have three cluster nodes, then you will need to have four IP addresses remaining after the removal.

Follow these steps:

  1. The admin cluster has an OnPremUserCluster custom resource for each associated user cluster. In the admin cluster, edit the OnPremUserCluster custom resource for your user cluster:
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG edit onpremusercluster USER_CLUSTER_NAME \
             --namespace USER_CLUSTER_NAME-gke-onprem-mgmt
         

Replace the following:

     * ADMIN_CLUSTER_KUBECONFIG: the path of the admin cluster kubeconfig file
     * USER_CLUSTER_NAME: the name of your user cluster
  2. Remove selected IP addresses from the `ipBlocks` section:
         
         network:
           ...
           ipMode:
             ipBlocks:
             - gateway: 198.51.100.254
               ips:
               - hostname: user-host1
                 ip: 198.51.100.1
               - hostname: user-host2
                 ip: 198.51.100.2
               - hostname: user-host3
                 ip: 198.51.100.3
               - hostname: user-host4
                 ip: 198.51.100.4
               - hostname: user-host5
                 ip: 198.51.100.5
               netmask: 255.255.255.0
             type: static
         

  3. Close the editing session.

  4. In your user cluster, view all of the Machine objects in the default namespace:
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get machines --output yaml
         

  5. Delete all of the Machine objects that use one of the removed IP addresses. For example, suppose you removed the address 198.51.100.1, and you discover that the `my-node-pool-1234` Machine object uses that address:
         
         Name:         my-node-pool-1234
         Namespace:    default
         Labels:       kubernetes.googleapis.com/cluster-name=my-cluster
                       kubernetes.googleapis.com/cluster-namespace=default
                       ...
         Annotations:  ...
                       vm-ip-address: 198.51.100.1
         

Then you must remove the `my-node-pool-1234` Machine object.
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG delete machine my-node-pool-1234
         

  6. After a a few minutes, view the cluster node addresses:
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get nodes --output wide
         

  7. Verify that removed IP addresses do not appear in the output. For example:
         
         myhost2   Ready ... 198.51.100.2
         myhost3   Ready ... 198.51.100.3
         myhost4   Ready ... 198.51.100.4
         




## Remove IP addresses from an admin cluster

Ensure that you will have enough IP addresses remaining after the removal. You need one IP address for the admin cluster control-plane node, two addresses for add-on nodes, and an additional IP address to be used for a temporary node during upgrades. Also, for each associated user cluster, you need either one or three addresses for the user cluster control plane. Each high-availability (HA) user cluster requires three nodes in the admin cluster for the control plane of the user cluster. Each non-HA user cluster requires one node in the admin cluster for the control plane of the user cluster.

For example, suppose your admin cluster is associated with one HA user cluster and one non-HA user cluster. Then after the removal, you must have eight IP addresses remaining to accommodate the following nodes:

  * Admin cluster control-plane node
  * Two add-on nodes
  * Three nodes for the control plane of the HA user cluster
  * One node for the control plane of the non-HA user cluster
  * A temporary node to be used during upgrades



Follow these steps:

  1. Determine the IP address that is being used for the control-plane node of the admin cluster:
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG get nodes --output wide
         

In the output, find the node listed as the control plane. Make a note of its IP address.
         
         gke-admin-master-hdn4z   Ready   control-plane,master … 198.51.100.101
         ...
         

  2. In the admin cluster, edit the OnPremAdminCluster custom resource:
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG edit onpremadmincluster --namespace kube-system
         

Replace ADMIN_CLUSTER_KUBECONFIG with the path of the admin cluster kubeconfig file.

  3. Remove selected IP addresses from the `ipBlocks` section. Make sure that you do not remove the IP address that is being used for the control-plane node of the admin cluster.
         
         network:
           ...
           ipMode:
             ipBlocks:
             - gateway: 198.51.100.254
               ips:
               - hostname: admin-host1
                 ip: 198.51.100.101
               - hostname: admin-host2
                 ip: 198.51.100.102
               - hostname: admin-host3
                 ip: 198.51.100.103
               - hostname: admin-host4
                 ip: 198.51.100.104
               - hostname: admin-host5
                 ip: 198.51.100.105
               - hostname: admin-host6
                 ip: 198.51.100.106
               - hostname: admin-host7
                 ip: 198.51.100.107
               - hostname: admin-host8
                 ip: 198.51.100.108
               - hostname: admin-host9
                 ip: 198.51.100.109
               netmask: 255.255.255.0
             type: static
         

  4. Close the editing session.

  5. In your admin cluster, view all of the Machine objects in the default namespace:
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG get machines --output yaml
         

  6. Delete all of the Machine objects that use one of the removed IP addresses. For example, suppose you removed the address 198.51.100.102, and you discover that the `gke-admin-node-` Machine object uses that address:
         
         Name:         gke-admin-node-5678
         Namespace:    default
         ...
         Status:
         Addresses:
         Address:       198.51.100.102
         Type:          ExternalIP
         ...
         

Then you must remove the `gke-admin-node-5678` Machine object.
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG delete machine gke-admin-node-5678
         

  7. View the cluster node addresses:
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG get nodes --output wide
         

  8. Verify that removed IP addresses do not appear in the output. For example:
         
         gke-admin-master-hdn4z  Ready  control-plane,master  198.51.100.101
         gke-admin-node-abcd   Ready ... 198.51.100.103
         gke-admin-node-efgh   Ready ... 198.51.100.104
         my-user-cluster-ijkl  Ready ... 198.51.100.105
         my-user-cluster-mnop  Ready ... 198.51.100.106
         my-user-cluster-qrst  Ready ... 198.51.100.107
         my-user-cluster-uvwx  Ready ... 198.51.100.108
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
