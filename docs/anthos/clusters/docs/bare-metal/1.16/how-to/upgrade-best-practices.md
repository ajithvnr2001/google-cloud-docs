---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade-best-practices/
title: Best practices for Google Distributed Cloud cluster upgrades \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:31.779875+00:00
---

# Best practices for Google Distributed Cloud cluster upgrades  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade-best-practices/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Best practices for Google Distributed Cloud cluster upgrades Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade-best-practices)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade-best-practices)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



This document describes best practices and considerations to upgrade Google Distributed Cloud. You learn how to prepare for cluster upgrades, and the best practices to follow before the upgrade. These best practices help to reduce the risks associated with cluster upgrades.

If you have multiple environments such as _test_ , _development_ , and _production_ , we recommend that you start with the least critical environment, such as _test_ , and verify the upgrade functionality. After you verify that the upgrade was successful, move on to the next environment. Repeat this process until you upgrade your production environments. This approach lets you move from one critical point to the next, and verify that the upgrade and your workloads all run correctly.

## Upgrade checklist

We recommend that you follow all of the best practices in this document. Use the following checklist to help you track your progress. Each item in the list links to a section in this document with more information:

Estimate the time commitment and plan a maintenance window for the upgrade.

Check compatibility of other GKE Enterprise components with the version you're upgrading to.

Check cluster resource utilization for the control plane and worker nodes.

Back up clusters. 

Verify clusters are configured and working properly and resolve any problems before the upgrade. 

Review user workload deployments for `Deployments`, `StatefulSets`, and `DaemonSets`.

Audit the use of webhooks.

Review the use of preview features.

Check SELinux status.

Don't change the Pod density configuration.

Make sure control plane and load balancer nodes aren't in maintenance mode.

After these checks are complete, you can start the upgrade process. Monitor the progress until all clusters are successfully upgraded.

## Plan the upgrade

Updates can be disruptive. Before you start the upgrade, plan carefully to make sure that your environment and applications are ready and prepared.

### Estimate the time commitment and plan a maintenance window

The amount of time it takes to upgrade a cluster varies depending on the number of nodes and the workload density that runs on them. To successfully complete a cluster upgrade, use a maintenance window with enough time.

To calculate a rough estimate for the upgrade, use `10 minutes * the number of nodes` for single concurrent node upgrade.

For example, if you have fifty nodes in a cluster, the total upgrade time would be about five hundred minutes: `10 minutes * 50 nodes = 500 minutes`.

### Check compatibility of other GKE Enterprise components

If your cluster runs GKE Enterprise components like Cloud Service Mesh, Config Sync, Policy Controller, or Config Controller, check the [GKE Enterprise compatibility matrix](https://docs.cloud.google.com/anthos/docs/version-and-upgrade-support) and verify the supported versions with Google Distributed Cloud before and after the upgrade.

The compatibility check is based on the admin or user cluster that Cloud Service Mesh, Config Sync, Policy Controller, or Config Controller is deployed into.

### Check cluster resource utilization

To make sure that Pods can be evacuated when the node drains and that there are enough resources in the cluster being upgraded to manage the upgrade, check the current resource usage of the cluster. To the check resource usage for your cluster, use the custom dashboards in Google Cloud Observability.

You can use commands, such as `kubectl top nodes` to get the current cluster resource usage, but dashboards can provide a more detailed view of resources being consumed over time. This resource usage data can help indicate when an upgrade would cause the least disruption, such as during weekends or evenings, depending on the running workload and use cases.

The timing for the admin cluster upgrade might be less critical than for the user clusters, because an admin cluster upgrade usually does not introduce application downtime. However, it's still important to check for available resources before you begin an admin cluster upgrade. Also, upgrading the admin cluster might imply some risk, and therefore might be recommended during less active usage periods when management access to the cluster is less critical.

#### Admin cluster control plane resources

All of the upgrade controllers and jobs run in the admin cluster control plane nodes. Check the resource consumption of these control plane nodes for available compute resources. The upgrade process typically requires 1000 millicores of CPU (1000 mCPU) and 2-3 GiB RAM for the each set of lifecycle controllers. Note that the CPU unit 'mCPU' stands for "thousandth of a core", and so 1000 millicores is the equivalent of one core on each node for each set of lifecycle controllers. To reduce the additional compute resources required during an upgrade, try to keep user clusters at the same version.

In the following example deployment, the two user clusters are at different versions than the admin cluster:

Admin cluster | User cluster 1 | User cluster 2  
---|---|---  
1.13.3 | 1.13.0 | 1.13.2  
  
A set of lifecycle controllers is deployed in the admin controller for each version in use. In this example, there are three sets of lifecycle controllers: `1.13.3`, `1.13.0`, and `1.13.2`. Each set of the lifecycle controllers consumes a total of 1000 mCPU and 3 GiB RAM. The current total resource consumption of these lifecycle controllers is 3000 mCPU and 9 GiB RAM.

If user cluster 2 is upgraded to `1.13.3`, there are now two sets of lifecycle controllers: `1.13.3` and `1.13.0`:

Admin cluster | User cluster 1 | User cluster 2  
---|---|---  
1.13.3 | 1.13.0 | 1.13.3  
  
The lifecycle controllers now consume a total 2000 mCPU and 6 GiB of RAM.

If user cluster 1 is upgraded to `1.13.3`, the fleet now all run at the same version: `1.13.3`:

Admin cluster | User cluster 1 | User cluster 2  
---|---|---  
1.13.3 | 1.13.3 | 1.13.3  
  
There is now only one set of lifecycle controllers, which consume a total 1000 mCPU and 3 GiB of RAM.

In the following example, all the user clusters are the same version. If the admin cluster is upgraded, only two sets of lifecycle controllers are used, so the compute resource consumption is reduced:

Admin cluster | User cluster 1 | User cluster 2  
---|---|---  
1.14.0 | 1.13.3 | 1.13.3  
  
In this example, the lifecycle controllers again consume a total 2000 mCPU and 6 GiB of RAM until all the user clusters are upgraded to the same version as the admin cluster.

If the control plane nodes don't have additional compute resources during the upgrade, you might see Pods such as `anthos-cluster-operator`, `capi-controller-manager`, `cap-controller-manager`, or `cap-kubeadm-bootstraper` in a `Pending` state. To resolve this problem, upgrade some of the user clusters to the same version to consolidate the versions and reduce the number of lifecycle controllers in use. If your upgrade is already stuck, you can also use `kubectl edit deployment` to edit the pending deployments to lower the CPU and RAM requests so they fit into the admin cluster control plane.

The following table details the compute resource requirements for different upgrade scenarios:

Cluster | Admin cluster resources required  
---|---  
User cluster upgrade | Upgrade to same version of other clusters: N/A  
  
Upgrade to different version of other admin or user clusters: 1000 mCPU and 3 GiB RAM  
  
User clusters in a hybrid cluster have the same resource requirements.  
Admin cluster upgrade (with user cluster) | 1000 mCPU and 3 GiB RAM  
Hybrid cluster upgrade (without user cluster) | 1000 mCPU and 3 GiB RAM surge. Resources are returned after use.   
Standalone | 200 mCPU and 1 GiB RAM surge. Resources are returned after use.  
  
### Back up clusters

Before you start an upgrade, [back up clusters using the `bmctl backup cluster` command](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/bmctl-backup-restore).

Because the backup file contains sensitive information, store the backup file securely.

### Verify clusters are configured and working properly

To check the health of a cluster before an upgrade, run `bmctl check cluster` on the cluster. The command runs advanced checks, such as to identify nodes that aren't configured properly, or that have Pods that are in a stuck state.

When you run the `bmctl upgrade cluster` command to upgrade your clusters, some preflight checks run. The upgrade process stops if these checks aren't successful. It's best to proactively identify and fix these problems with the `bmctl check cluster` command, rather than relying on the preflight checks which are there to protect clusters from any possible damage.

### Review user workload deployments

There are two areas to consider for user workloads: _draining_ and _API compatibility_.

#### Workload draining

The user workload on a node is drained during an upgrade. If the workload has a single replica or all replicas are on the same node, workload draining might cause disruption on the services running in the cluster. Run your workloads with multiple replicas. The replica number should be above the concurrent node number.

To avoid a stuck upgrade, the draining process of upgrading up to 1.16 doesn't respect pod disruption budgets (PDBs). Workloads might run in a degraded state, and the least serving replica would be `total replica number - concurrent upgrade number`.

#### API compatibility

For API compatibility, check your workload API compatibility with newer minor version of Kubernetes when doing a minor version upgrade. If needed, upgrade the workload to a compatible version. Where possible, the GKE Enterprise engineering team provides instruction to identify workloads using incompatible APIs, such as [removed Kubernetes APIs](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/deleted-apis-kubernetes).

If you use Cloud Service Mesh, Config Sync, Policy Controller, and Config Controller, or other GKE Enterprise components, check if the installed version is compatible with the new version of Google Distributed Cloud. For GKE Enterprise component version compatibility information, see [GKE Enterprise version and upgrade support](https://docs.cloud.google.com/anthos/docs/version-and-upgrade-support).

### Audit the use of webhooks

Check if your cluster has any webhooks, especially Pod resources for auditing purposes like Policy Controller. The draining process during the cluster upgrade might disrupt the Policy Controller webhook service, which can cause the upgrade to become stuck or take a long time. We recommend you temporarily disable these webhooks, or use a highly available (HA) deployment.

### Review the use of Preview features

[Preview](https://cloud.google.com/products/#product-launch-stages) features are subject to change and are provided for testing and evaluation purposes only. Don't use Preview features on your production clusters. We don't guarantee that clusters that use Preview features can be upgraded. In some cases, we explicitly block upgrades for clusters that use Preview features.

For information about breaking changes related to upgrading, see the [release notes](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/release-notes).

### Check SELinux status

If you want to enable SELinux to secure your containers, you must make sure that SELinux is enabled in `Enforced` mode on all your host machines. Starting with Google Distributed Cloud release 1.9.0 or later, you can enable or disable SELinux before or after cluster creation or cluster upgrades. SELinux is enabled by default on Red Hat Enterprise Linux (RHEL) and CentOS. If SELinux is disabled on your host machines or you aren't sure, see [Securing your containers using SELinux](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/configure-selinux) for instructions on how to enable it.

Google Distributed Cloud supports SELinux in only RHEL and CentOS systems.

### Don't change the Pod density configuration

Google Distributed Cloud supports the configuration of up to 250 maximum pods per node with `nodeConfig.PodDensity.MaxPodsPerNode`. You can configure pod density during cluster creation only. You can't update pod density settings for existing clusters. Don't try to change the pod density configuration during an upgrade.

### Make sure control plane and load balancer nodes aren't in maintenance mode

Make sure that control plane and load balancer nodes aren't under maintenance before starting an upgrade. If any node is in maintenance mode, the upgrade pauses to ensure the control plane and load balancer node pools are sufficiently available.

## What's next

  * [Upgrade clusters](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/how-to/upgrade)
  * Learn more about the [lifecycle and stages of upgrades](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/how-to/upgrade-lifecycle)
  * [Troubleshoot cluster upgrade issues](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/create-upgrade#cluster_upgrade_issues)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
