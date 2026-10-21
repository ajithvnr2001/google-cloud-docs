---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/maintenance-mode/
title: Put nodes into maintenance mode \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:35.619525+00:00
---

# Put nodes into maintenance mode  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/maintenance-mode/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Put nodes into maintenance mode Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/maintenance-mode)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/maintenance-mode)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



When you need to repair or maintain nodes, you should first put the nodes into maintenance mode. Putting nodes into maintenance mode safely drains their pods/workloads and excludes the nodes from pod scheduling. In maintenance mode, you can work on your nodes without a risk of disrupting pod traffic.

## How it works

Google Distributed Cloud provides a way to place nodes into maintenance mode. This approach lets other cluster components correctly know that the node is in maintenance mode. When you place a node in maintenance mode, no additional pods can be scheduled on the node, and existing pods are stopped.

Instead of using maintenance mode, you can manually use Kubernetes commands such as `kubectl cordon` and `kubectl drain` on a specific node. If you run Google Distributed Cloud version 1.12.0 (`anthosBareMetalVersion: 1.12.0`) or lower, see the known issue on [Nodes uncordoned if you don't use the maintenance mode procedure](https://cloud.google.com/anthos/clusters/docs/bare-metal/1.12/troubleshooting/known-issues#nodes-uncordoned-if-you-dont-use-the-maintenance-mode-procedure).

When you use the maintenance mode process, Google Distributed Cloud does the following:

  * [Node taints](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/) are added to specified nodes to indicate that no pods can be scheduled or executed on the nodes.

  * A 20-minute timeout is enforced to ensure nodes don't get stuck waiting for pods to stop. Pods might not stop if they are configured to [tolerate all taints](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) or they have [finalizers](https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/). Google Distributed Cloud attempts to stop all pods, but if the timeout is exceeded, the node is put into maintenance mode. This timeout prevents running pods from blocking upgrades.




## Put a node into maintenance mode

Choose the nodes you want to put into maintenance mode by specifying IP ranges for the selected nodes under `maintenanceBlocks` in your cluster configuration file. The nodes you choose must be in a ready state, and functioning in the cluster.

To put nodes into maintenance mode:

  1. Edit the cluster configuration file to select the nodes you want to put into maintenance mode.

You can edit the configuration file with an editor of your choice, or you can edit the cluster custom resource directly by running the following command:
         
         kubectl -n CLUSTER_NAMESPACE edit cluster CLUSTER_NAME

Replace the following:

     * `CLUSTER_NAMESPACE`: the namespace of the cluster.
     * `CLUSTER_NAME`: the name of the cluster.
  2. Add the `maintenanceBlocks` section to the cluster configuration file to specify either a single IP address, or an address range, for nodes you want to put into maintenance mode.

The following sample shows how to select multiple nodes by specifying a range of IP addresses:
         
         metadata:
           name: my-cluster
           namespace: cluster-my-cluster
         spec:
           maintenanceBlocks:
             cidrBlocks:
             - 172.16.128.1-172.16.128.64
         

  3. Save and apply the updated cluster configuration.

Google Distributed Cloud starts putting the nodes into maintenance mode.

  4. Run the following command to get the status of the nodes in your cluster:
         
         kubectl get nodes --kubeconfig=KUBECONFIG

The response is something like the following:
         
         NAME                       STATUS   ROLES           AGE     VERSION
         user-anthos-baremetal-01   Ready    control-plane   2d22h   v1.27.4-gke.1600
         user-anthos-baremetal-04   Ready    worker          2d22h   v1.27.4-gke.1600
         user-anthos-baremetal-05   Ready    worker          2d22h   v1.27.4-gke.1600
         user-anthos-baremetal-06   Ready    worker          2d22h   v1.27.4-gke.1600
         

Note that the nodes are still schedulable, but taints keep any pods (without an appropriate toleration) from being scheduled on the node.

  5. Run the following command to get the number of nodes in maintenance mode:
         
         kubectl get nodepools --kubeconfig ADMIN_KUBECONFIG 
         

The response should look something like the following example:
         
         NAME   READY   RECONCILING   STALLED   UNDERMAINTENANCE   UNKNOWN
         np1    3       0             0         1                  0
         

This `UNDERMAINTENANCE` column in this sample shows that one node is in maintenance mode.

Google Distributed Cloud also adds the following taints to nodes when they are put into maintenance mode:

     * `baremetal.cluster.gke.io/maintenance:NoExecute`
     * `baremetal.cluster.gke.io/maintenance:NoSchedule`



## Billing and maintenance mode

Billing for Google Distributed Cloud is based on the number of vCPUs your cluster has for Nodes capable of running workloads. When you put a Node into maintenance mode, `NoExecute` and `NoSchedule` taints are added to the Node, but they don't disable billing. After putting a node into maintenance mode, cordon the node (`kubectl cordon NODE_NAME`) to mark it as unschedulable. Once a node is marked as unschedulable, the Node and its associated vCPUs are excluded from billing.

Important: Powering down a node doesn't change its billing status. To exclude a node from billing, take one of the following actions: 

  * [Remove an individual node](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/update-clusters#add_or_remove_nodes_in_a_cluster) from a node pool
  * [Remove a node pool](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/add-remove-node-pools) from the cluster
  * Put a node into maintenance mode and cordon it to make it unschedulable



As described on the [pricing page](https://cloud.google.com/anthos/pricing), you can use `kubectl` to see the vCPU capacity (used for Anthos billing) of each of your user clusters. The command doesn't take whether or not the Node is schedulable into consideration, it provides a vCPU count per node only.

To identify the number of vCPUs per node for your user cluster:
    
    
    kubectl get nodes \
        --kubeconfig USER_KUBECONFIG \
        -o=jsonpath="{range .items[*]}{.metadata.name}{\"\t\"} \
        {.status.capacity.cpu}{\"\n\"}{end}"
    

Replace USER_KUBECONFIG with the path of the kubeconfig file for your user cluster.

## Remove a node from maintenance mode

To remove nodes from maintenance mode:

  1. Edit the cluster configuration file to clear the nodes you want to remove from maintenance mode.

You can edit the configuration file with an editor of your choice, or you can edit the cluster custom resource directly by running the following command:
         
         kubectl -n CLUSTER_NAMESPACE edit cluster CLUSTER_NAME

Replace the following:

     * `CLUSTER_NAMESPACE`: the namespace of the cluster.
     * `CLUSTER_NAME`: the name of the cluster.
  2. Either edit the IP addresses to remove specific nodes from maintenance mode or remove the `maintenanceBlocks` section remove all does from maintenance mode.

  3. Save and apply the updated cluster configuration.

  4. Use `kubectl` commands to check the status of your nodes.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
