---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-auto-repair/
title: Automatic node repair and health checking \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:19:47.238812+00:00
---

# Automatic node repair and health checking  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-auto-repair/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Automatic node repair and health checking Stay organized with collections  Save and categorize content based on your preferences. 

In Google Distributed Cloud, periodic health checking and automatic node repair are enabled by default.

The node auto repair feature continuously detects and repairs unhealthy nodes in a cluster.

Periodic health checks run every fifteen minutes. The checks are the same as the ones performed by `gkectl diagnose cluster`. The results are surfaced as logs and events on Cluster objects in the admin cluster.

Make sure that your admin and user clusters each have an extra IP address available for automatic node repair.

If [advanced cluster is enabled](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enable-advanced-cluster-field), the periodic health checks are not run as part of auto repair.

## Unhealthy node conditions when advanced cluster isn't enabled

The following conditions are indications that a node is unhealthy when [`enableAdvanceCluster`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enable-advanced-cluster-field) is `false`.

  * The node condition `NotReady` is `true` for approximately 10 minutes.

  * The machine state is `Unavailable` for approximately 10 minutes after successful creation.

  * The machine state is not `Available` for approximately 30 minutes after VM creation.

  * There is no node object (nodeRef is `nil`) corresponding to a machine in the `Available` state for approximately 10 minutes.

  * The node condition `DiskPressure` is `true` for approximately 30 minutes.




## Unhealthy node conditions when advanced cluster is enabled

The following conditions are indications that a node is unhealthy when [`enableAdvanceCluster`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enable-advanced-cluster-field) is `true`.

  * The node condition `NotReady` is `true` for approximately 10 minutes.

  * The node condition `DiskPressure` is `true` for approximately 30 minutes.




## Node repair strategy

Google Distributed Cloud initiates a repair on a node if the node meets at least one of the conditions in the preceding list.

The repair drains the unhealthy node and creates a new VM. If the node draining is unsuccessful for one hour, the repair forces the drain and safely detaches the attached Kubernetes managed disks.

If there are multiple unhealthy nodes in the same MachineDeployment, the repair is performed on only one of those nodes at a time.

The number of repairs per hour for a node pool is limited to the maximum of:

  * Three
  * Ten percent of the number of nodes in the node pool



## Enabling node repair and health checking for a new cluster

**Note:** If advanced cluster is enabled, the periodic health checks are not run as part of auto repair.

In your [admin](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#autorepair-enabled-field) or [user](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#autorepair-enabled-field) cluster configuration file, set `autoRepair.enabled` to `true`:
    
    
    autoRepair:
      enabled: true
    

Continue with the steps for creating your [admin](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-cluster) or [user](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster) cluster.

**Note:** Because the user cluster control-plane nodes are located in the admin cluster, you must follow the instructions for the admin cluster if you want auto-repair to be enabled for the user cluster control-plane nodes.

## Enabling node repair and health checking for an existing user cluster

**Note:** If advanced cluster is enabled, the periodic health checks are not run as part of auto repair.

In your [user cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#autorepair-enabled-field), set `autoRepair.enabled` to `true`:

Update the cluster:
    
    
    gkectl update cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG
    

Replace the following:

  * ADMIN_CLUSTER_KUBECONFIG: the path of your admin cluster kubeconfig file

  * USER_CLUSTER_CONFIG: the path of your user cluster configuration file




## Enabling node repair and health checking for an existing admin cluster

**Note:** If advanced cluster is enabled, the periodic health checks are not run as part of auto repair.

In your [admin cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#autorepair-enabled-field), set `autoRepair.enabled` to `true`:

Update the cluster:
    
    
    gkectl update admin --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config ADMIN_CLUSTER_CONFIG
    

Replace ADMIN_CLUSTER_CONFIG with the path of your admin cluster configuration file.

## Viewing logs from a health checker

**Note:** If advanced cluster is enabled,the periodic health checks are not run as part of auto repair. This section does not apply.

List all of the health checker Pods in the admin cluster:
    
    
    kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG get pods --all-namespaces | grep cluster-health-controller
    

The output is similar to this:
    
    
    kube-system       cluster-health-controller-6c7df455cf-zlfh7   2/2   Running
    my-user-cluster   cluster-health-controller-5d5545bb75-rtz7c   2/2   Running
    

To view the logs from a particular health checker, get the logs for the `cluster-health-controller` container in one of the Pods. For example, to get the logs for `my-user-cluster` shown in the preceding output:
    
    
    kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG --namespace my-user-cluster logs \
        cluster-health-controller-5d5545bb75-rtz7c cluster-health-controller
    

## Viewing events from a health checker

**Note:** If advanced cluster is enabled,the periodic health checks are not run as part of auto repair. This section does not apply.

List all of the Cluster objects in your admin cluster:
    
    
    kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG get clusters --all-namespaces
    

The output is similar to this:
    
    
    default            gke-admin-ldxh7   2d15h
    my-user-cluster    my-user-cluster   2d12h
    

To view the events for a particular cluster, run `kubectl describe cluster` with the `--show-events` flag. For example, to see the events for `my-user-cluster` shown in the preceding output:
    
    
    kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG --namespace my-user-cluster \
        describe --show-events cluster my-user-cluster
    

Example output:
    
    
    Events:
      Type     Reason             Age   From                                 Message
      ----     ------             ----  ----                                 -------
      Warning  ValidationFailure  17s   cluster-health-periodics-controller  validator for Pod returned with status: FAILURE, reason: 1 pod error(s).
    

## Disabling node repair and health checking for a user cluster

**Note:** If advanced cluster is enabled,the periodic health checks are not run as part of auto repair.

In your [user cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest), set `autoRepair.enabled` to `false`:

Update the cluster:
    
    
    gkectl update cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG
    

## Disabling node repair and health checking for an admin cluster

**Note:** If advanced cluster is enabled, the periodic health checks are not run as part of auto repair.

In your [admin cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#autorepair-enabled-field), set `autoRepair.enabled` to `false`:

Update the cluster:
    
    
    gkectl update admin --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config ADMIN_CLUSTER_CONFIG
    

## Debugging node auto repair when advanced cluster isn't enabled

You can investigate issues with node auto repair by describing the Machine and Node objects in the admin cluster. Here's an example:

List the machine objects:
    
    
    kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG  get machines
    

Example output:
    
    
    default     gke-admin-master-wcbrj
    default     gke-admin-node-7458969ff8-5cg8d
    default     gke-admin-node-7458969ff8-svqj7
    default     xxxxxx-user-cluster-41-25j8d-567f9c848f-fwjqt
    

Describe one of the Machine objects:
    
    
    kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG describe machine gke-admin-master-wcbrj
    

In the output, look for events from `cluster-health-controller`.

Similarly, you can list and describe node objects. For example:
    
    
    kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG get nodes
    ...
    kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG describe node gke-admin-master-wcbrj
    

## Debugging node auto repair when advanced cluster is enabled

You can investigate issues with node auto repair by describing the Machine and Node objects in the admin cluster and the corresponding cluster respectively. Here's an example:

List the machine objects:
    
    
    kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG  get machines
    

Example output:
    
    
    NAMESPACE                            NAME          NODEPOOL
    ci-1f6861fe28cac8fb390bc798927c717b  10.251.172.47 ci-1f6861fe28cac8fb390bc798927c717b-np
    ci-1f6861fe28cac8fb390bc798927c717b  10.251.173.64 ci-1f6861fe28cac8fb390bc798927c717b-cp
    ci-1f6861fe28cac8fb390bc798927c717b  10.251.173.66 ci-1f6861fe28cac8fb390bc798927c717b-cp
    ci-1f6861fe28cac8fb390bc798927c717b  10.251.174.19 ci-1f6861fe28cac8fb390bc798927c717b-np
    ci-1f6861fe28cac8fb390bc798927c717b  10.251.175.15 ci-1f6861fe28cac8fb390bc798927c717b-np
    ci-1f6861fe28cac8fb390bc798927c717b  10.251.175.30 ci-1f6861fe28cac8fb390bc798927c717b-cp
    kube-system                          10.251.172.239   gke-admin-bnbp9-cp
    kube-system                          10.251.173.39    gke-admin-bnbp9-cp
    kube-system                          10.251.173.6     gke-admin-bnbp9-cp
    

Describe the machine corresponding to the Machine object:
    
    
    kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG describe machine -n ci-1f6861fe28cac8fb390bc798927c717b 10.251.172.47
    

In the output, look for events from `auto-repair-controller`.

Similarly, you can list and describe node objects. For example:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get nodes
    ...
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG describe node ci-1f6861fe28cac8fb390bc798927c717b-np
    

## Manual node repair when advanced cluster isn't enabled

### Admin control plane node

The admin control plane node has a dedicated repair command, because the normal manual repair doesn't work for it.

Use [`gkectl repair admin-master`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/repair-admin-control-plane) to repair the admin control plane node.

### Controlplane V2 user cluster control plane node

The Controlplane V2 user cluster control plane nodes are managed differently from other nodes.

Similar to kubeception user clusters, the control plane Machine objects of Controlplane V2 user clusters are in the admin cluster. And the node auto repair is covered by the admin cluster node auto repair.

In case there are node problems that are not covered by the admin cluster node auto repair logic, or you have not enabled admin cluster node auto repair, you can do a manual repair. This deletes and re-creates the node.

  1. Get the name of the Machine object that corresponds to the node:
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG -n USER_CLUSTER_NAME get machines
         

Replace the following:

     * `ADMIN_CLUSTER_KUBECONFIG`: the path of your admin cluster kubeconfig file.
     * `USER_CLUSTER_NAME`: the target user cluster name.
  2. Add the `repair` annotation to the Machine object:
         
         kubectl annotate --kubeconfig ADMIN_CLUSTER_KUBECONFIG -n USER_CLUSTER_NAME machine MACHINE_NAME onprem.cluster.gke.io/repair-machine=true
         

Replace `MACHINE_NAME` with the name of the Machine object.

  3. Delete the Machine object:
         
         kubectl delete --kubeconfig ADMIN_CLUSTER_KUBECONFIG -n USER_CLUSTER_NAME machine MACHINE_NAME
         




Re-create the node one by one for a HA control plane, or else it might bring down the control plane unexpectedly.

**Note:** A Controlplane V2 user cluster has a copy of the control plane Machine objects in the user cluster itself. Those Machine objects are for informational purpose only. Deleting them will not take effect.

### Other nodes

**Warning:** This does not work for the admin control plane Machine object, do not use it for the admin control plane Machine object.**Warning:** This does not work for the copy of control plane Machine objects in the Controlplane V2 user clusters.

In case there are node problems that are not covered by the auto repair logic, or you have not enabled node auto repair, you can do a manual repair. This deletes and re-creates the node.

Get the name of the Machine object that corresponds to the node:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG get machines
    

Replace CLUSTER_KUBECONFIG with the path of your admin or user cluster kubeconfig file.

Add the `repair` annotation to the Machine object:
    
    
    kubectl annotate --kubeconfig CLUSTER_KUBECONFIG machine MACHINE_NAME onprem.cluster.gke.io/repair-machine=true
    

Replace MACHINE_NAME with the name of the Machine object.

Delete the Machine object:
    
    
    kubectl delete --kubeconfig CLUSTER_KUBECONFIG machine MACHINE_NAME
    

## Manual node repair when advanced cluster is enabled

### Admin control plane node

Admin control plane node manual repair is not supported

### User cluster control plane node / Worker Nodes

Get the name of the Inventory Machine object that corresponds to the node using the IP of the node to match the objects:
    
    
    kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG get inventorymachines
    

Replace the following: ADMIN_CLUSTER_KUBECONFIG: the path of your admin kubeconfig file.

Add the `force-remove` annotation to the Inventory Machine object:
    
    
    kubectl annotate --kubeconfig ADMIN_CLUSTER_KUBECONFIG inventorymachine MACHINE_NAME baremetal.cluster.gke.io/force-remove=true
    

Replace MACHINE_NAME with the name of the Machine object.

Delete the Inventory Machine object:
    
    
    kubectl delete --kubeconfig ADMIN_CLUSTER_KUBECONFIG inventorymachine MACHINE_NAME
    

Re-create the node one by one for a HA control plane, or else it might bring down the control plane unexpectedly.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
