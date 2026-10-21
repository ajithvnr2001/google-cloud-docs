---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/maintenance-mode/
title: Put nodes into maintenance mode \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:21:55.602424+00:00
---

# Put nodes into maintenance mode  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/maintenance-mode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Put nodes into maintenance mode Stay organized with collections  Save and categorize content based on your preferences. 

Maintenance mode lets you repair and service nodes with minimal disruption to your workloads. When you add nodes to the `maintenanceBlocks` section of your cluster configuration, Google Distributed Cloud gracefully drains their workloads and prevents new pods from being scheduled on them. When you need to take an entire cluster offline, you can also safely shut it down and restart it.

During cluster upgrades, Google Distributed Cloud automatically uses maintenance mode to drain nodes before they are upgraded. For more information about the upgrade process, see [Lifecycle and stages of cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade-lifecycle).

## How it works

Google Distributed Cloud provides a way to place nodes into maintenance mode. This approach lets other cluster components correctly know that the node is in maintenance mode. When you place a node in maintenance mode, no additional pods can be scheduled on the node, and existing pods are stopped.

Instead of using maintenance mode, you can manually use Kubernetes commands such as `kubectl cordon` and `kubectl drain` on a specific node.

When you use the maintenance mode process, Google Distributed Cloud does the following:

###  1.29 

  * Google Distributed Cloud adds the `baremetal.cluster.gke.io/maintenance:NoSchedule` [taint](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/) to specified nodes to prevent scheduling of new pods on the node.

  * Google Distributed Cloud uses the [Eviction API](https://kubernetes.io/docs/concepts/scheduling-eviction/api-eviction/) to evict each Pod. This method of draining nodes honors PodDisruptionBudgets (PDBs). You can [configure PDBs](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) to protect your workloads by specifying a tolerable level of disruption for a set of pods using fields `minAvailable` and `maxUnavailable`. Draining nodes this way provides better protection against workload disruptions. Eviction-based node draining is available as GA for release 1.29.

  * A 20-minute timeout is enforced to ensure nodes don't get stuck waiting for pods to stop. Pods might not stop if they are configured to [tolerate all taints](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) or they have [finalizers](https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/). Google Distributed Cloud attempts to stop all pods, but if the timeout is exceeded, the node is put into maintenance mode. This timeout prevents running pods from blocking upgrades.




###  1.28 and earlier 

  * Google Distributed Cloud adds the `baremetal.cluster.gke.io/maintenance:NoSchedule` [taint](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/) to specified nodes to prevent scheduling of new pods on the node.

  * Google Distributed Cloud adds the `baremetal.cluster.gke.io/maintenance:NoExecute` taint. Acting on the `NoExecute` taint, the Google Distributed Cloud `kube-scheduler` stops pods and drains the node. This method of draining nodes doesn't honor PDBs.

  * A 20-minute timeout is enforced to ensure nodes don't get stuck waiting for pods to stop. Pods might not stop if they are configured to [tolerate all taints](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) or they have [finalizers](https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/). Google Distributed Cloud attempts to stop all pods, but if the timeout is exceeded, the node is put into maintenance mode. This timeout prevents running pods from blocking upgrades.




### Eviction-based draining

There aren't procedural changes associated with the switch to eviction-based node draining from taint-based draining. The switch affects reconciliation logic only.

This capability isn't at the same launch stage for all supported versions:

  * 1.29: GA
  * 1.28: Not available
  * 1.16: Not available



#### Draining order

Prior to release 1.29, the taint-based node draining that's performed by the Google Distributed Cloud `kube-scheduler` doesn't employ a particular algorithm to drain pods from a node. With eviction-based node draining, pods are evicted in a specific order based on priority. The eviction priority is associated with specific pod criteria as shown in the following table:

Draining order | Pod criteria (must match all) and   
---|---  
1 |  Pods matching the following criteria are evicted:

  * Pods without `spec.prorityClassName`
  * Pods that don't match any known Container Storage Interface (CSI) name
  * Pods that don't belong to a DaemonSet

  
2 |  Pods matching the following criteria are evicted:

  * Pods that belong to a DaemonSet
  * Pods don't have `PriorityClass`
  * Pods that don't match any known Container Storage Interface (CSI) name

  
3 |  Pods matching the following criteria are evicted:

  * Pods with `Spec.ProrityClassName`
  * Pods that don't match any known Container Storage Interface (CSI) name

Eviction order for matching pods is based on `PriorityClass.value`, from low to high.  
4 |  Wait for CSI to clean up the PV/PVC mounts after the pods are all evicted. Use `Node.Status.VolumesInUse` to indicate all volumes are cleaned up.  
5 |  Pods matching the following criteria are evicted:

  * Pods that match a known Container Storage Interface (CSI) name

These pods still need draining, because kubelet doesn't provide in-place upgrade compatibility.  
  
Because eviction-based node draining honors PDBs, PDB settings might block node draining in some circumstances. For troubleshooting information about node pool draining, see [Check why a node has been in the status of draining for a long time](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/create-upgrade#upgrade_long_drain).

#### Deadline for eviction-based draining

When you put nodes into maintenance mode, the system enforces a default 20-minute (1200 seconds) timeout for draining the nodes. When the timeout elapses, all Pods that don't tolerate maintenance mode are evicted and the node is put into maintenance mode. Starting with version 1.16, you can add the `baremetal.cluster.gke.io/maintenance-mode-deadline-seconds` annotation to your cluster resource to adjust the timeout duration. For example to change the timeout to 10 minutes, add the `baremetal.cluster.gke.io/maintenance-mode-deadline-seconds: "600"` annotation to your cluster resource.

Eviction-based draining can sometimes exceed the deadline specified by `maintenance-mode-deadline-seconds`. If Pods become stuck in a terminating state after the deadline is exceeded, don't use `kubectl` with the flags `--grace-period=0 --force` to forcibly delete them, as this can cause data corruption or [split-brain issues](https://en.wikipedia.org/wiki/Split-brain_\(computing\)) for stateful applications. Instead, reboot nodes with stuck stateful Pods.

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support) for more information about support resources, including the following: 

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#intro-support) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#support-tools) to help you troubleshoot, such as your environment configuration, logs, and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#what-we-support).



#### Disable eviction-based node draining

Eviction-based node draining is enabled by default for clusters at minor version 1.29 and later or clusters being upgraded to minor version 1.29 and later. If eviction-based node draining is causing problems with cluster upgrades or cluster maintenance, you can revert to taint-based node draining by adding the `baremetal.cluster.gke.io/maintenance-mode-ignore-pdb: ""` annotation to your cluster resource.

To restore the default eviction-based node draining behavior, remove the annotation completely. Setting the annotation to `false` doesn't re-enable the default behavior.

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

The output is similar to the following:
         
         NAME                STATUS   ROLES           AGE     VERSION
         user-baremetal-01   Ready    control-plane   2d22h   v1.27.4-gke.1600
         user-baremetal-04   Ready    worker          2d22h   v1.27.4-gke.1600
         user-baremetal-05   Ready    worker          2d22h   v1.27.4-gke.1600
         user-baremetal-06   Ready    worker          2d22h   v1.27.4-gke.1600
         

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




## Shut down and restart a cluster

If it becomes necessary to bring down a complete cluster, use the instructions in the following sections to shut down a cluster and bring it back up safely.

### Shut down a cluster

If you're shutting down a cluster that manages user clusters, you must shut down all managed user clusters first. The following instructions apply to all Google Distributed Cloud cluster types.

  1. Check the status of all cluster nodes:
         
         kubectl get nodes --kubeconfig CLUSTER_KUBECONFIG
         

Replace `CLUSTER_KUBECONFIG` with the path of the kubeconfig file for the cluster.

The output is similar to the following:
         
         NAME        STATUS   ROLES           AGE    VERSION
         control-0   Ready    control-plane   202d   v1.27.4-gke.1600
         control-1   Ready    control-plane   202d   v1.27.4-gke.1600
         control-2   Ready    control-plane   202d   v1.27.4-gke.1600
         worker-0    Ready    worker          202d   v1.27.4-gke.1600
         worker-1    Ready    worker          202d   v1.27.4-gke.1600
         worker-2    Ready    worker          202d   v1.27.4-gke.1600
         worker-3    Ready    worker          202d   v1.27.4-gke.1600
         worker-4    Ready    worker          154d   v1.27.4-gke.1600
         worker-5    Ready    worker          154d   v1.27.4-gke.1600
         worker-6    Ready    worker          154d   v1.27.4-gke.1600
         worker-7    Ready    worker          154d   v1.27.4-gke.1600
         worker-8    Ready    worker          154d   v1.27.4-gke.1600
         worker-9    Ready    worker          154d   v1.27.4-gke.1600
         

If the `STATUS` for a node isn't `Ready`, then we strongly recommended that you troubleshoot the node and proceed only when all nodes are `Ready`.

  2. If you're shutting down a user cluster, check the status of the admin cluster nodes:
         
         kubectl get nodes --kubeconfig ADMIN_KUBECONFIG
         

Replace `ADMIN_KUBECONFIG` with the path of the kubeconfig file for the managing cluster.

Subsequent steps have a dependency on the admin cluster. If the `STATUS` for a node isn't `Ready`, then we strongly recommended that you troubleshoot the node and proceed only when all nodes are `Ready`.

  3. Check the health of the cluster that you want to shut down:
         
         bmctl check cluster -c CLUSTER_NAME --kubeconfig ADMIN_KUBECONFIG
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster you're checking.

     * `ADMIN_KUBECONFIG`: the path of the kubeconfig file for the managing cluster.

Correct any reported problems before proceeding.

  4. For the cluster you're shutting down, ensure that all `etcd` Pods are running:
         
         kubectl get pods --kubeconfig CLUSTER_KUBECONFIG -A \
             -l component=etcd
         

Replace `CLUSTER_KUBECONFIG` with the path of the kubeconfig file for the cluster.

The output is similar to the following:
         
         NAMESPACE     NAME                   READY   STATUS    RESTARTS   AGE
         kube-system   etcd-control-0-admin   1/1     Running   0          2d22h
         kube-system   etcd-control-1-admin   1/1     Running   0          2d22h
         kube-system   etcd-control-2-admin   1/1     Running   0          2d22h
         

If the `STATUS` for a pod isn't `Running`, then we strongly recommended that you troubleshoot the pod and proceed only when all pods are `Running`.

  5. Perform a backup as described in [Back up a cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/bmctl-backup-restore#back_up_a_cluster).

It's important to take an etcd backup before shutting down your cluster so that your cluster can be restored if you encounter any issues when restarting the cluster. Etcd corruption, node hardware failures, network connectivity issues, and potentially other conditions can prevent the cluster from restarting properly.

  6. If you're shutting down a cluster with worker nodes, put the worker nodes into maintenance mode.

This step minimizes minimize the amount the writing to etcd, which reduces the likelihood that a large amount of etcd writes need to be reconciled when the cluster is restarted.

  7. Put the control plane nodes into maintenance mode.

This step prevents corrupted writes for stateful workloads during node shut down.

  8. Power down cluster nodes in the following sequence:

     1. Worker nodes
     2. Control plane load balancer nodes
     3. Control plane nodes, starting with the etcd followers and ending with the etcd leader

If you have a high availability (HA) cluster, you can find the etcd leader by using SSH to connect to each control plane node and running the following `etcdctl` command:
            
            ETCDCTL_API=3 etcdctl \
                --cacert /etc/kubernetes/pki/etcd/ca.crt \
                --cert /etc/kubernetes/pki/etcd/server.crt \
                --key /etc/kubernetes/pki/etcd/server.key \
                --write-out=table endpoint status
            

The response includes an `IS LEADER` column, which returns `true` if the node is the etcd leader.

**Note:** It's expected that the API server is down once the etcd followers are down. This is because the API server can't serve requests if the etcd cluster loses quorum, which is expected when shutting down. Etcd regains quorum once all control plane nodes are back online.



At this point, your cluster is completely shut down. After you have performed any needed maintenance, you can restart your cluster as described in the next section.

### Restart the cluster

Use the following steps to restart a cluster that's been completely powered down.

  1. Turn on node machines in the reverse order from the power down sequence.

  2. Remove the control plane nodes from maintenance mode.

For instructions, see Remove a node from maintenance mode.

**Note:** It's not necessary to take machines out of maintenance mode one at a time, but it's a good idea to start with a single node, make sure it's healthy, then slowly increase the number of nodes over time.
  3. Remove worker nodes from maintenance mode.

  4. Run cluster health checks to ensure the cluster is operating properly:
         
         bmctl check cluster -c CLUSTER_NAME --kubeconfig ADMIN_KUBECONFIG
         

  5. If a problem, such as etcd crashlooping, prevents the cluster from restarting properly, try restoring the cluster from the last known good backup. For instructions, see [Restore a cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/bmctl-backup-restore#restore_a_cluster).




## Billing and maintenance mode

Billing for Google Distributed Cloud is based on the number of vCPUs your cluster has for Nodes capable of running workloads. When you put a Node into maintenance mode, `NoExecute` and `NoSchedule` taints are added to the Node, but they don't disable billing. After putting a node into maintenance mode, cordon the node (`kubectl cordon NODE_NAME`) to mark it as unschedulable. Once a node is marked as unschedulable, the Node and its associated vCPUs are excluded from billing.

Important: Powering down a node doesn't change its billing status. To exclude a node from billing, take one of the following actions: 

  * [Remove an individual node](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/update-clusters#add_or_remove_nodes_in_a_cluster) from a node pool
  * [Remove a node pool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/add-remove-node-pools) from the cluster
  * Put a node into maintenance mode and cordon it to make it unschedulable



As described on the [pricing page](https://cloud.google.com/kubernetes-engine/pricing), you can use `kubectl` to see the vCPU capacity (used for billing) of each of your user clusters. The command doesn't take into consideration whether or not the Node is schedulable, it provides a vCPU count per node only.

To identify the number of vCPUs per node for your user cluster:
    
    
    kubectl get nodes \
        --kubeconfig USER_KUBECONFIG \
        -o=jsonpath="{range .items[*]}{.metadata.name}{\"\t\"} \
        {.status.capacity.cpu}{\"\n\"}{end}"
    

Replace USER_KUBECONFIG with the path of the kubeconfig file for your user cluster.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
