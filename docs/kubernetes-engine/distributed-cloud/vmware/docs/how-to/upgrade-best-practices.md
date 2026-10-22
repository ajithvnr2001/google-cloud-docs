---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-best-practices/
title: Best practices for Google Distributed Cloud cluster upgrades \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:02.696592+00:00
---

# Best practices for Google Distributed Cloud cluster upgrades  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Best practices for Google Distributed Cloud cluster upgrades Stay organized with collections  Save and categorize content based on your preferences. 

This document describes best practices and considerations to upgrade Google Distributed Cloud. You learn how to prepare for cluster upgrades, and the best practices to follow before the upgrade. These best practices help to reduce the risks associated with cluster upgrades.

If you have multiple environments such as _test_ , _development_ , and _production_ , we recommend that you start with the least critical environment, such as _test_ , and verify the upgrade functionality. After you verify that the upgrade was successful, move on to the next environment. Repeat this process until you upgrade your production environments. This approach lets you move from one critical point to the next, and verify that the upgrade and your workloads all run correctly.

**Note:** This document focuses on Google Distributed Cloud from versions 1.8 and later. Some commands that provide automated checks aren't available in older versions. If you run an older cluster, you must manually run some of these checks.

## Upgrade checklist

To make the upgrade process as smooth as possible, review and complete the following checks before you start to upgrade your clusters: 

Estimate the time commitment and plan a maintenance window for the upgrade.

Prepare backups for the user clusters and admin cluster.

Check for `PodDisruptionBudgets` in user clusters.

Review the available IP addresses and needs.

Check the user cluster utilization and available resources.

Check the vSphere cluster capacity for available resources such as CPU, memory, and ready times.

Check the cluster health and configuration to resolve problems before the upgrade.

Diagnose the cluster to check cluster health before upgrading to an advanced cluster.

Use Deployments to minimize application disruption.

Use a high availability load balancer pair.

Decide how to upgrade each user cluster.

Check if CA certificates need to be rotated.

**Note:** Although the `gkectl upgrade` command automatically runs some preflight checks, these checks don't substitute for manual upgrade preparations.

## Plan the upgrade

Updates can be disruptive. Before you start the upgrade, plan carefully to make sure that your environment and applications are ready and prepared. You might also need to schedule the upgrade after normal business hours when traffic is at its lightest.

### Estimate the time commitment and plan a maintenance window

By default, all node pools are upgraded in parallel. But within each node pool, the nodes are upgraded sequentially because each node must be drained and recreated. So the total time for an upgrade depends on the number of nodes in the largest node pool. To calculate a rough estimate for the upgrade time, multiply 15 minutes times the number of nodes in the largest node pool. For example, if you have 10 nodes in the largest pool, the total upgrade time would be about 15 * 10 = 150 minutes or 2.5 hours.

These are several ways to reduce upgrade time and make it easier to plan and schedule upgrades:

  * In version 1.28 and later, you can accelerate an upgrade by setting the value of [`maxSurge`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#nodepool-update-policy-updatestrategy-rolling-update-maxsurge-field) for individual node pools. When you upgrade notes with `maxSurge`, multiple nodes upgrade in the same time that it takes to upgrade a single node.

  * If your clusters are at version 1.16 or higher, you can skip a minor version when upgrading node pools. Performing a skip-version upgrade halves the time that it would take to sequentially upgrade node pools two versions. Additionally, skip-version upgrades lets you increase the time between upgrades needed to stay on a supported version. Reducing the number of upgrades reduces workload disruptions and verification time. For more information, see [Skip a version when upgrading node pools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/skip-version-upgrade). 

  * You can upgrade a user cluster's control plane separately from node pools. Having this flexibility can help you plan multiple, shorter maintenance windows instead of one long maintenance window to upgrade the entire cluster. For details, see [Upgrade node pools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-node-pools).




### Back up the user and admin cluster

Before you start an upgrade, back up your user and admin clusters.

A user cluster backup is a snapshot of the user cluster's etcd store. The etcd store contains all of the Kubernetes objects and custom objects required to manage cluster state. The snapshot contains the data required to recreate the cluster's components and workloads. For more information, see how to [back up a user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/back-up-user-cluster).

With Google Distributed Cloud version 1.8 and later, you can set up automatic backup with [clusterBackup.datastore](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#clusterbackup-datastore-field) in the admin cluster configuration file. To enable this feature in an existing cluster, edit the admin cluster configuration file and add the `clusterBackup.datastore` field, then run `gkectl update admin`.

After `clusterBackup.datastore` is enabled, your admin cluster is automatically backed up in `etcd` on the configured vSphere datastore. This backup process repeats every time there's a change to the admin cluster. When you start a cluster upgrade, a backup task runs before upgrading the cluster.

To restore an admin cluster from its backup if you have problems, see [Back up and restore an admin cluster with `gkectl`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/back-up-and-restore-an-admin-cluster-with-gkectl).

### Review the use of `PodDisruptionBudgets`

In Kubernetes, `PodDisruptionBudgets` (PDBs) can help prevent unwanted application downtime or outages. PDBs instruct the scheduler to always keep a number of Pods running while other Pods might be failing. This behavior is a useful way to provide for application availability.

  1. To check what PDBs are configured in your cluster, use the `kubectl get pdb` command:
         
         kubectl get pdb -A --kubeconfig KUBECONFIG
         

Replace `KUBECONFIG` with the name of your kubeconfig file.

The following example output shows PDBs named `istio-ingress`, `istiod`, and `kube-dns`:
         
         NAMESPACE     NAME            MIN AVAILABLE   MAX UNAVAILABLE   ALLOWED DISRUPTIONS   AGE
         gke-system    istio-ingress   1               N/A               1                     16d
         gke-system    istiod          1               N/A               1                     16d
         kube-system   kube-dns        1               N/A               1                     16d
         




In the preceding table, each PDB specifies that at least one Pod must always be available. This availability becomes critical during upgrades when nodes are drained.

Check for PDBs that can't be fulfilled. For example, you might set a minimum availability of 1, when the Deployment only features 1 replica. In this example, the draining operation is disrupted because the PDB can't be satisfied by the resource controller.

To make sure that the PDBs don't interfere with the upgrade procedure, check all PDBs on a given cluster before you start the upgrade. You might need to coordinate with the development teams and application owners to temporarily change or disable PDBs during a cluster upgrade.

Google Distributed Cloud runs a preflight check during the upgrade process to warn about PDBs. However, you should also manually verify the PDBs to ensure a smooth upgrade experience. To learn more about PDBs, see [Specifying a Disruption Budget for your Application](https://kubernetes.io/docs/tasks/run-application/configure-pdb/).

### Review the available IP addresses

The following IP address considerations apply to upgrades of user clusters and non-HA admin clusters (that is, admin clusters that aren't highly available):

  * The cluster upgrade process creates a new node and drains the resources before it deletes the old node. We recommend that you always have N+1 IP addresses for the cluster, where N is the number of nodes in the cluster. This recommendation applies only to non-HA admin clusters (which only have one control-plane node) and user clusters.

  * When using static IP addresses, the required IP addresses must be listed in the IP block files.

    * When upgrading non-HA admin clusters, add the additional IP address in the IP block file used by the admin cluster. The path to this file must be specified in the [`network.ipMode.ipBlockFilePath`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#network-ipmode.ipblockfilepath-field) field of the admin cluster configuration file.
    * When upgrading user clusters, add the additional IP address in the IP block file used by the user cluster. The path to this file must be specified in the [`network.ipMode.ipBlockFilePath`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-ipmode.ipblockfilepath-field) field of the user cluster configuration file.
  * If you use DHCP, make sure that new VMs can get additional IP leases in the applicable subnet during an upgrade.

If you need to add IP addresses, update the IP block file, then run the `gkectl update` command. For more information, see [Plan your IP addresses](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/plan-ip-addresses).

  * If you use static IP addresses and want to speed up the user cluster upgrade process, list enough IP addresses in your IP block file so that each node pool can have an extra IP address available. This approach lets the process speed up the VM addition and removal procedure as it's performed on a per node pool basis.

Although this approach is a good option to speed up user cluster upgrades, consider the resource and performance availability of your vSphere environment before you proceed.

  * If there is only one spare IP for the entire user cluster, this limitation slows the upgrade process to only one VM at a time, even when multiple node pools are used.




HA admin clusters don't require N+1 IP addresses for upgrades. The three control-plane nodes in an HA admin cluster are recreated one by one, ensuring no additional IP addresses are needed.

### Check cluster utilization

Make sure that Pods can be evacuated when the node drains and that there are enough resources in the cluster being upgraded to manage the upgrade. To check the current resource usage of the cluster, you can use custom dashboards in Google Cloud Observability, or directly on the cluster using commands such as `kubectl top nodes`.

Commands you run against the cluster show you a snapshot of the current cluster resource usage. Dashboards can provide a more detailed view of resources being consumed over time. This resource usage data can help indicate when an upgrade would cause the least disruption, such as during weekends or evenings, depending on the running workload and use cases.

The timing for the admin cluster upgrade might be less critical than for the user clusters, because an admin cluster upgrade usually does not introduce application downtime. However, it's still important to check for free resources in vSphere before you begin an admin cluster upgrade. Also, upgrading the admin cluster might imply some risk, and therefore might be recommended during less active usage periods when management access to the cluster is less critical.

For more information, see what services are impacted during a cluster upgrade.

### Check vSphere utilization

Check that there are enough resources on the underlying vSphere infrastructure. To check this resource usage, select a cluster in vCenter and review the **Summary** tab.

The summary tab shows the overall memory, CPU, and storage consumption of the entire cluster. Because Google Distributed Cloud upgrades demand additional resources, you should also check if the cluster can handle these additional resource requests.

As a general rule, your vSphere cluster must be able to support the following additional resources:

  * +1 VM per admin cluster upgrade
  * +1 VM per node pool per user cluster upgrade



For example, assume that a user cluster has 3 node pools where each node pool has nodes using 8 vCPUs and 32GB or more of RAM. Because the upgrade happens in parallel for the 3 node pools by default, the upgrade procedure consumes the following additional resources for the 3 additional surge nodes:

  * 24 vCPUs
  * 96GB of RAM
  * VM disk space + 96GB of vSwap



The upgrade process creates VMs using the vSphere clone operation. Cloning multiple VMs from a template can introduce stress to the underlying storage system in the form of rising I/O operations. The upgrade can be severely slowed down if the underlying storage subsystem is incapable of providing sufficient performance during an upgrade.

While vSphere is designed for simultaneous resource usage and has mechanisms to provide resources, even when overcommitted, we strongly recommend not overcommitting the VM memory. Memory overcommitment can lead to serious performance impacts that affect the entire cluster as vSphere provides the "missing RAM" from swapping pages out to the datastore. This behavior can lead to problems during an upgrade of a cluster, and cause performance impacts on other running VMs on the vSphere cluster.

If the available resources are already scarce, power down unneeded VMs to help satisfy these additional requirements and prevent a potential performance hit.

### Check the cluster health and configuration

Run the following tools on all clusters before the upgrade:

  * The `gkectl diagnose` command: `gkectl diagnose` ensures all clusters are healthy. The command runs advanced checks, such as to identify nodes that aren't configured properly, or that have Pods that are in a stuck state. If the `gkectl diagnose` command shows a `Cluster unhealthy` warning, fix the issues before you attempt an upgrade. For more information, see [Diagnose cluster issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose).

**Important:** Always [diagnose](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose) your cluster before upgrading to an [advanced cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/advanced-clusters). We strongly recommend running `gkectl diagnose cluster` on your admin and user clusters to ensure they are healthy, and resolving any issues before starting the upgrade.
  * The [pre-upgrade tool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/pre-upgrade-tool): in addition to checking the cluster health and configuration, the pre-upgrade tool checks for potential known issues that could happen during a cluster upgrade.




Additionally, when you are upgrading user clusters to 1.29 and higher, we recommend that you run the `gkectl upgrade cluster` command with the `--dry-run` flag. The `--dry-run` flag runs [preflight checks](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#run-preflight-checks) but doesn't start the upgrade process. Although earlier versions of Google Distributed Cloud run preflight checks, they can't be run separately from the upgrade. By adding the `--dry-run` flag, you can find and fix any issues that the preflight checks find with your user cluster before the upgrade.

### Use Deployments to minimize application disruption

As nodes need to be drained during updates, cluster upgrades can lead to application disruptions. Draining the nodes means that all running Pods must be shut down and restarted on the remaining nodes in the cluster.

If possible, your applications should use Deployments. With this approach, applications are designed to handle interruptions. Any impact should be minimal to Deployments that have multiple replicas. You can still upgrade your cluster if applications don't use Deployments.

There are also rules for Deployments to make sure that a set number of replicas always keep running. These rules are known as `PodDisruptionBudgets` (PDBs). PDBs allow you to limit the disruption to a workload when its Pods must be rescheduled for some reason, such as upgrades or maintenance on the cluster nodes, and are important to check before an upgrade.

### Use a high availability load balancer pair

If you use Seesaw as a load balancer on a cluster, the load balancers are upgraded automatically when you upgrade the cluster. This upgrade can cause a service disruption. To reduce the impact of an upgrade and an eventual load balancer failure, you can use a high-availability pair (HA pair). In this configuration, the system creates and configures two load balancer VMs so that a failover to the other peer can happen.

To increase service availability (that is, to the Kubernetes API server), we recommend that you always use an HA pair in front of the admin cluster. To learn more about Seesaw and its HA configuration, see the version 1.16 documentation [Bundled load balancing with Seesaw](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/bundled-load-balance).

To prevent a service disruption during an upgrade with an HA pair, the cluster initiates a failover before it creates the new load balancer VM. If a user cluster only uses a single load balancer instance, a service disruption occurs until the upgrade for the load balancer is complete.

We recommend that you have an HA load balancer pair if the user cluster itself is also configured to be highly available. This best practices series assumes that an HA user cluster uses an HA load balancer pair.

If you use [MetalLB](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/bundled-load-balance-metallb) as a bundled load balancer, no pre-upgrade setup is required. The load balancer is upgraded during the cluster upgrade process.

### Decide how to upgrade each user cluster

In version 1.14 and later, you can choose to upgrade a user cluster as a whole (meaning you can upgrade the control plane and all node pools in the cluster), or you can upgrade the user cluster's control plane and leave the node pools at the current version. For information on why you might want to upgrade the control plane separately, see [User cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-overview#user_cluster_upgrades).

In a multi-cluster environment, keep track of which user clusters have been upgraded and record their version number. If you decide to upgrade the control plane and node pools separately, record the version of the control plane and each node pool in each cluster.

#### Check user and admin cluster versions

### gkectl

  * To check the version of user clusters:
        
        gkectl list clusters --kubeconfig ADMIN_CLUSTER_KUBECONFIG

Replace `ADMIN_CLUSTER_KUBECONFIG` with the path of the kubeconfig file for your admin cluster.

  * To check the version of admin clusters:
        
        gkectl list admin --kubeconfig ADMIN_CLUSTER_KUBECONFIG




###  gcloud CLI 

For clusters that are [enrolled in the GKE On-Prem API](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster), you can use the gcloud CLI to get the versions of user clusters, node pools on the user cluster, and admin clusters.

  1. Ensure that you have [the latest version of the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install). Update the gcloud CLI components, if needed:
         
         gcloud components update
         

  2. Run the following commands to check versions:



  * To check the version of user clusters:
        
        gcloud container vmware clusters list \
            --project=PROJECT_ID \
            --location=-

Replace `PROJECT_ID` The project ID of your [fleet host project](https://docs.cloud.google.com/anthos/fleet-management/docs/fleet-concepts#fleet-host-project).

When you set `--location=-`, that means to list all clusters in all regions. If you need to scope down the list, set `--location` to the region you specified when you enrolled the cluster.

The output of the command includes the cluster version.

  * To check the version of admin clusters:
        
        gcloud container vmware admin-clusters list \
            --project=PROJECT_ID \
            --location=-




#### Check the version of cluster nodes:

You can use `kubectl` for to get the version of cluster nodes, but `kubectl` returns the Kubernetes version. To get the corresponding Google Distributed Cloud version for a Kubernetes version, see [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/version-history#kubernetes-and-node-kernel-versions).
    
    
    kubectl get nodes --kubeconfig USER_CLUSTER_KUBECONFIG

Replace `USER_CLUSTER_KUBECONFIG` with the path of the kubeconfig file for your user cluster.

### Check if CA certificates need to be rotated

During an upgrade, leaf certificates are rotated, but CA certificates aren't. You must manually rotate your CA certificates at least once every five years. For more information, see [Rotate user cluster certificate authorities](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ca-rotation) and [Rotate admin cluster CA certificates](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ca-rotation).

## Differences between cluster types

There are two different types of clusters:

  * User cluster
  * Admin cluster



Depending on how you create a user cluster, it might contains both worker nodes and control plane nodes (Controlplane V2) or only worker nodes (kubeception). With kubeception, the control plane for a user cluster runs on one or more nodes in an admin cluster. In both cases, in version 1.14 and later, you can upgrade a user cluster's control plane separately from the node pools that run your workloads.

### Different effects of user cluster versus admin cluster upgrades

The Google Distributed Cloud upgrade procedure involves a node drain process that removes all Pods from a node. The process creates a new VM for each drained worker node and adds it to the cluster. The drained worker nodes are then removed from VMware's inventory. During this process, any workload that runs on these nodes is stopped and restarted on other available nodes in the cluster.

Depending on the chosen architecture of the workload, this procedure might have an impact on an application's availability. To avoid too much strain on the cluster's resource abilities, Google Distributed Cloud upgrades one node at a time.

### User cluster disruption

The following table describes the impact of an in-place user cluster upgrade:

Function | Admin cluster | Non-HA user cluster | HA user cluster  
---|---|---|---  
Kubernetes API access | Not affected | Not affected | Not affected  
User workloads | Not affected | Not affected | Not affected  
PodDisruptionBudgets* | Not affected | Not affected | Not affected  
Control-plane node | Not affected | Affected | Not affected  
Pod autoscaler (VMware) | Not affected | Not affected | Not affected  
Auto repair | Not affected | Not affected | Not affected  
Node autoscaling (VMware) | Not affected | Not affected | Not affected  
Horizontal Pod autoscaling | Affected | Affected | Not affected  
  
  * * : PDBs might cause the upgrade to fail or stop.
  * **Affected** : a service disruption during the upgrade is noticeable until the upgrade is finished.
  * **Not affected** : a service disruption might occur during a very short amount of time, but is almost unnoticeable.



The user cluster control plane nodes, whether they run on the admin cluster (kubeception) or the user cluster itself (Controlplane V2), don't run any user workloads. During an upgrade, these control plane nodes are drained and then updated accordingly.

In environments with high availability (HA) control planes, upgrading a user cluster's control plane doesn't disrupt user workloads. In a HA environment, upgrading an admin cluster doesn't disrupt user workloads. For user clusters using Controlplane V2, upgrading only the control plane doesn't disrupt user workloads.

During an upgrade in a non-HA control plane environment, the control plane can't control Pod-scaling, recovery, or deployment actions. During the short disruption of the control plane during the upgrade, user workloads can be affected if they are in a scaling, deployment or recovery state. This means that rollouts will fail during an upgrade in a non-HA environment.

To improve availability and reduce disruption of production user clusters during upgrades, we recommend that you use three control plane nodes (high availability mode).

### Admin cluster disruption

The following table describes the impact of an in-place admin cluster upgrade:

Function | Admin cluster | Non-HA user cluster | HA user cluster  
---|---|---|---  
Kubernetes API access | Affected | Affected | Not affected  
User workloads | Not affected | Not affected | Not affected  
Control-plane node | Affected | Affected | Not affected  
Pod Autoscaler | Affected | Affected | Not affected  
Auto Repair | Affected | Affected | Not affected  
Node autoscaling | Affected | Affected | Not affected  
Horizontal Pod autoscaling | Affected | Affected | Not affected  
  
  * **Affected** : a service disruption during the upgrade is noticeable until the upgrade is finished.
  * **Not affected** : a service disruption might occur during a very short amount of time, but is almost unnoticeable.



## What's next

  * [Upgrade a cluster or a node pool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
