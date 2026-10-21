---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade/
title: Upgrade clusters \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:30.118529+00:00
---

# Upgrade clusters  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Upgrade clusters Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



When you install a new version of `bmctl`, you can upgrade your existing clusters that were created with an earlier version. Upgrading a cluster to the latest Google Distributed Cloud version brings added features and fixes to your cluster. It also ensures that your cluster remains [supported](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support). You can upgrade admin, hybrid, standalone, or user clusters with the `bmctl upgrade cluster` command, or you can use `kubectl`.

To learn more about the upgrade process, see [Lifecycle and stages of cluster upgrades](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade-lifecycle).

**Note:** When upgrading Google Distributed Cloud from a version with a security patch to the next minor release, we recommend you upgrade to the highest patch version available to ensure you have the latest security patches. Always review the release notes before upgrading so you are aware of what has changed, including security fixes and known issues. Downgrading to a lower cluster version isn't supported.

## Plan your upgrade

This section contains information and links to information that you should consider before you upgrade a cluster.

### Best practices

For information to help you prepare for a cluster upgrade, see [Best practices for Anthos clusters on bare metal cluster upgrades](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade-best-practices).

### Upgrade preflight checks

Preflight checks are run as part of the cluster upgrade to validate cluster status and node health. The cluster upgrade doesn't proceed if the preflight checks fail. For more information on preflight checks, see [Understand preflight checks](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/preflight).

You can check if the clusters are ready for an upgrade by running the preflight check before running the upgrade. For more information, see [Preflight checks for upgrades](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/preflight#preflight_checks_for_upgrades).

### Known issues

For information about potential problems related to cluster upgrades, see [Anthos clusters on bare metal known issues](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/known-issues) and select the **Upgrades and updates** problem category.

## Configure upgrade options

Before you start a cluster upgrade, you can configure the following upgrade options that control how the upgrade process works:

  * Selective worker node pool upgrades: upgrade specific worker node pools separately from the rest of the cluster.

  * Parallel upgrades: configure the upgrade process to upgrade groups of nodes or node pools simultaneously.




These options can reduce the risk of disruptions to critical applications and services and significantly reduce overall upgrade time. These options are especially useful for large clusters with numerous nodes and node pools running important workloads. For more information about what these options do and how to use them, see the following sections.

### Selective worker node pool upgrades

By default, the cluster upgrade operation upgrades every node and node pool in the cluster. A cluster upgrade can be disruptive and time consuming, as it results in each node being drained and all associated pods being restarted/rescheduled. This section describes how you can include or exclude select worker node pools for a cluster upgrade to minimize workload disruption. This feature applies to user, hybrid, and standalone clusters only, since admin clusters don't allow worker node pools.

You might use selective node pool upgrades in the following situations:

  * **To pick up security fixes without disrupting workloads:** You can upgrade just your control plane nodes (and load balancer nodes) to apply Kubernetes vulnerability fixes without disrupting your worker node pools.

  * **To confirm proper operation of an upgraded subset of worker nodes before upgrading all worker nodes:** You can upgrade your worker node pools selectively to ensure that workloads are running properly on an upgraded node pool before you upgrade another node pool.

  * **To reduce the maintenance window:** Upgrading a large cluster can be time consuming and it's difficult to accurately predict when an upgrade will complete. Cluster upgrade time is proportional to the number of nodes being upgraded. Reducing the number of nodes being upgraded by excluding node pools reduces the upgrade time. You upgrade multiple times, but the smaller, more predictable maintenance windows may help with scheduling.




For the versioning rules for selectively upgrading worker node pools, see [Node pool versioning rules](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade-lifecycle#np_version_rules) in Lifecycle and stages of cluster upgrades.

#### Upgrade your cluster control plane and selected node pools

To selectively upgrade worker node pools in the initial cluster upgrade:

  1. For the worker node pools that you want to **include** in the cluster upgrade, make one of the following changes to the NodePool spec:

     * Set `anthosBareMetalVersion` in the NodePool spec to the cluster target upgrade version.
     * Omit the `anthosBareMetalVersion` field from the NodePool spec. or set it to the empty string. By default, worker node pools are included in cluster upgrades.
  2. For the worker node pools that you want to **exclude** from the upgrade, set `anthosBareMetalVersion` to the current (pre-upgrade) version of the cluster:

  3. Continue with your upgrade as described in Start the cluster upgrade.

The cluster upgrade operation upgrades the following nodes:

     * Cluster control plane nodes.
     * Load balancer node pool, if your cluster uses one (`spec.loadBalancer.nodePoolSpec`). By default, load balancer nodes can run regular workloads. You can't selectively upgrade a load balancer node pool, it's always included in the initial cluster upgrade.
     * Worker node pools that you haven't excluded from the upgrade.



For example, suppose that your cluster is at version 1.15.0 and has two worker node pools: `wpool01` and `wpool02`. Also, suppose that you want to upgrade the control plane and `wpool01` to 1.16.8, but you want `wpool02` to remain at version 1.15.0.

The following cluster configuration file excerpt shows how you can modify the cluster configuration to support this partial upgrade:
    
    
    ...
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: user001
      namespace: cluster-user001
    spec:
      type: user
      profile: default**  anthosBareMetalVersion: 1.16.8**
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: NodePool
    metadata:
      name: wpool01
      namespace: cluster-user001
    spec:
      clusterName: user001**  anthosBareMetalVersion: 1.16.8**
      nodes:
      - address:  10.200.0.1
      - address:  10.200.0.2
      - address:  10.200.0.3
      ...
      - address:  10.200.0.8
    
    apiVersion: baremetal.cluster.gke.io/v1
    kind: NodePool
    metadata:
      name: wpool02
      namespace: cluster-user001
    spec:
      clusterName: user001**  anthosBareMetalVersion: 1.15.0**
      nodes:
      - address:  10.200.1.1
      - address:  10.200.1.2
      - address:  10.200.1.3
      ...
      - address:  10.200.1.12
    

#### Upgrade node pools to the current cluster version

If you've excluded node pools from a cluster upgrade, you can run a cluster upgrade that brings them up to the target cluster version. Worker node pools that have been excluded from a cluster upgrade have the `anthosBareMetalVersion` field in their NodePool spec set to the previous (pre-upgrade) cluster version.

To bring worker node pools up to the current, upgraded cluster version:

  1. Edit the NodePool specs in the cluster configuration file for the worker node pools that you want to bring up to the current cluster version. Set `anthosBareMetalVersion` to the current (post-upgrade) cluster version.

If multiple worker node pools are selected for upgrade, the value of`spec.nodePoolUpgradeStrategy.concurrentNodePools` in the cluster spec determines how many node pools are upgraded in parallel, if any. If you don't want to upgrade worker node pools concurrently, select one node pool at a time for upgrade.

  2. Continue with your upgrade as described in Start the cluster upgrade.

The cluster upgrade operation upgrades only the previously excluded worker node pools for which you have set `anthosBareMetalVersion` to the current, upgraded cluster version.




For example, suppose that you upgraded your cluster to version 1.16.8, but node pool `wpool02` is still at the old, pre-upgrade cluster version 1.15.0. Workloads are running properly on the upgraded node pool, `wpool01`, so now you want to bring `wpool02` up to the current cluster version, too. To upgrade `wpool02`, you can remove the `anthosBareMetalVersion` field or set its value to the empty string.

The following cluster configuration file excerpt shows how you can modify the cluster configuration to support this partial upgrade:
    
    
    ...
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: user001
      namespace: cluster-user001
    spec:
      type: user
      profile: default**  anthosBareMetalVersion: 1.16.8**
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: NodePool
    metadata:
      name: wpool01
      namespace: cluster-user001
    spec:
      clusterName: user001**  anthosBareMetalVersion: 1.16.8**
      nodes:
      - address:  10.200.0.1
      - address:  10.200.0.2
      - address:  10.200.0.3
      ...
      - address:  10.200.0.8
    
    apiVersion: baremetal.cluster.gke.io/v1
    kind: NodePool
    metadata:
      name: wpool02
      namespace: cluster-user001
    spec:
      clusterName: user001**  anthosBareMetalVersion: ""**
      nodes:
      - address:  10.200.1.1
      - address:  10.200.1.2
      - address:  10.200.1.3
      ...
      - address:  10.200.1.12
    

### Parallel upgrades

In a typical, default cluster upgrade, each cluster node is upgraded sequentially, one after the other. This section shows you how to configure your cluster and worker node pools so that multiple nodes upgrade in parallel when you upgrade your cluster. Upgrading nodes in parallel speeds up cluster upgrades significantly, especially for clusters that have hundreds of nodes.

**Caution:** If you use managed data services, such a Portworx, to help manage stateful workloads on your clusters, we recommend that you don't use parallel upgrades.

There are two parallel upgrade strategies that you can use to speed up your cluster upgrade:

  * **Concurrent node upgrade:** you can configure your worker node pools so that multiple nodes upgrade in parallel. Parallel upgrades of nodes are configured in the NodePool spec (`spec.upgradeStrategy.parallelUpgrade`) and only nodes in a worker node pool can be upgraded in parallel. Nodes in control plane or load balancer node pools can only be upgraded one at a time. For more information, see Node upgrade strategy.

  * **Concurrent node pool upgrade:** you can configure your cluster so that multiple node pools upgrade in parallel. Only worker node pools can be upgraded in parallel. Control plane and load balancer node pools can only be upgraded one at a time.




#### Node upgrade strategy

You can configure worker node pools so that multiple nodes upgrade concurrently (`concurrentNodes`). You can also set a minimum threshold for the number of nodes able to run workloads throughout the upgrade process (`minimumAvailableNodes`). This configuration is made in the NodePool spec. For more information about these fields, see the [Cluster configuration field reference](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/cluster-config-ref#upgradestrategy).

**Important:** Parallel upgrades don't honor the [Pod Disruption Budget (PDB)](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/#pod-disruption-budgets). If your workloads are sensitive to disruptions, we recommend that you use the `minimumAvailableNodes` field. You can specify the minimum quantity of nodes that must remain available to run workloads throughout the upgrade process.

The node upgrade strategy applies to worker node pools only. You can't specify a node upgrade strategy for control plane or load balancer node pools. During a cluster upgrade, nodes in control plane and load balancer node pools upgrade sequentially, one at a time. Control plane node pools and load balancer node pools are specified in the Cluster spec (`controlPlane.nodePoolSpec.nodes` and `loadBalancer.nodePoolSpec.nodes`).

When you configure parallel upgrades for nodes, note the following restrictions:

  * The value of `concurrentNodes` can't exceed either 50 percent of the number of nodes in the node pool, or the fixed number 15, whichever is smaller. For example, if your node pool has 20 nodes, you can't specify a value greater than 10. If your node pool has 100 nodes, 15 is the maximum value you can specify.

  * When you use `concurrentNodes` together with `minimumAvailableNodes`, the combined values can't exceed the total number of nodes in the node pool. For example, if your node pool has 20 nodes and `minimumAvailableNodes` is set to 18, `concurrentNodes` can't exceed 2. Likewise, if `concurrentNodes` is set to 10, `minimumAvailableNodes` can't exceed 10.




The following example shows a worker node pool `np1` with 10 nodes. In an upgrade, nodes upgrade 5 at a time and at least 4 nodes must remain available for the upgrade to proceed:
    
    
    apiVersion: baremetal.cluster.gke.io/v1
    kind: NodePool
    metadata:
      name: np1
      namespace: cluster-cluster1
    spec:
      clusterName: cluster1
      nodes:
      - address:  10.200.0.1
      - address:  10.200.0.2
      - address:  10.200.0.3
      - address:  10.200.0.4
      - address:  10.200.0.5
      - address:  10.200.0.6
      - address:  10.200.0.7
      - address:  10.200.0.8
      - address:  10.200.0.9
      - address:  10.200.0.10 **  upgradeStrategy:
        parallelUpgrade:
          concurrentNodes: 5
          minimumAvailableNodes: 4 **
    

#### Node pool upgrade strategy

You can configure a cluster so that multiple worker node pools upgrade in parallel. The `nodePoolUpgradeStrategy.concurrentNodePools` Boolean field in the cluster spec specifies whether or not to upgrade all worker node pools for a cluster concurrently. By default (`1`), node pools upgrade sequentially, one after the other. When you set `concurrentNodePools` to `0`, every worker node pool in the cluster upgrades in parallel.

Control plane and load balancing node pools are not affected by this setting. These node pools always upgrade sequentially, one at a time. Control plane node pools and load balancer node pools are specified in the Cluster spec (`controlPlane.nodePoolSpec.nodes` and `loadBalancer.nodePoolSpec.nodes`).
    
    
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: cluster1
      namespace: cluster-cluster1
    spec:
      ...**  nodePoolUpgradeStrategy:
        concurrentNodePools: 0**
      ...
    

#### How to perform a parallel upgrade

This section describes how to configure a cluster and a worker node pool for parallel upgrades.

To perform a parallel upgrade of worker node pools and nodes in a worker node pool, do the following:

  1. Add an `upgradeStrategy` section to the NodePool spec.

You can apply this manifest separately or as part of the cluster configuration file when you perform a cluster update.

Here's an example:
         
         ---
         apiVersion: baremetal.cluster.gke.io/v1
         kind: NodePool
         metadata:
           name: np1
           namespace: cluster-ci-bf8b9aa43c16c47
         spec:
           clusterName: ci-bf8b9aa43c16c47
           nodes:
           - address:  10.200.0.1
           - address:  10.200.0.2
           - address:  10.200.0.3
           ...
           - address:  10.200.0.30**  upgradeStrategy:
             parallelUpgrade:
               concurrentNodes: 5
               minimumAvailableNodes: 10**
         

In this example, the value of the field `concurrentNodes` is `5`, which means that 5 nodes upgrade in parallel. The `minimumAvailableNodes` field is set to `10`, which means that at least 10 nodes must remain available for workloads throughout the upgrade.

**Note:** You can't specify a node upgrade strategy for control plane or load balancer node pools.
  2. Add an `nodePoolUpgradeStrategy` section to the Cluster spec in the cluster configuration file.
         
         ---
         apiVersion: v1
         kind: Namespace
         metadata:
           name: cluster-user001
         ---
         apiVersion: baremetal.cluster.gke.io/v1
         kind: Cluster
         metadata:
           name: user001
           namespace: cluster-user001
         spec:
           type: user
           profile: default
           anthosBareMetalVersion: 1.16.8
           ...**  nodePoolUpgradeStrategy:
             concurrentNodePools: 0**
           ...
         

In this example, the `concurrentNodePools` field is set to `0`, which means that all worker node pools upgrade concurrently during the cluster upgrade. The upgrade strategy for the nodes in the node pools is defined in the NodePool specs.

  3. Upgrade the cluster as described in the preceding Upgrade admin, standalone, hybrid, or user clusters section.




#### Parallel upgrade default values

Parallel upgrades are disabled by default and the fields related to parallel upgrades are mutable. At any time, you can either remove the fields or set them to their default values to disable the feature before a subsequent upgrade.

The following table lists the parallel upgrade fields and their default values:

Field | Default value | Meaning  
---|---|---  
`nodePoolUpgradeStrategy.concurrentNodePools` (Cluster spec) | `1` | Upgrade worker node pools sequentially, one after the other.  
`upgradeStrategy.parallelUpgrade.concurrentNodes` (NodePool spec) | `1` | Upgrade nodes sequentially, one after the other.  
`upgradeStrategy.parallelUpgrade.minimumAvailableNodes` (NodePool spec) | The default `minimumAvailableNodes` value depends on the value of `concurrentNodes`. 

  * If you don't specify `concurrentNodes`, then `minimumAvailableNodes` by default is 2/3 the node pool size.
  * If you do specify `concurrentNodes`, then `minimumAvailableNodes` by default is the node pool size minus `concurrentNodes`.

| Upgrade stalls once `minimumAvailableNodes` is reached and only continues once the number of available nodes is greater than `minimumAvailableNodes`.  
  
## Start the cluster upgrade

This section contains instructions for upgrading clusters.

**Note:** You should upgrade an admin cluster before upgrading any associated user clusters. However, before upgrading the admin cluster to `1.16.8`, make sure its associated user clusters are at version `1.15.0` or above. `bmctl` will emit an error if it finds any user cluster is below `1.15.0`.

###  `bmctl`

When you download and install a new version of `bmctl`, you can upgrade your admin, hybrid, standalone, and user clusters created with an earlier version. For a given version of `bmctl`, a cluster can be upgraded to the same version only.

  1. Download the latest `bmctl` as described in [Google Distributed Cloud downloads](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/downloads).

  2. Update `anthosBareMetalVersion` in the cluster configuration file to the upgrade target version.

The upgrade target version must match the version of the downloaded `bmctl` file. The following cluster configuration file snippet shows the `anthosBareMetalVersion` field updated to the latest version:
         
         ---
         apiVersion: baremetal.cluster.gke.io/v1
         kind: Cluster
         metadata:
           name: cluster1
           namespace: cluster-cluster1
         spec:
           type: admin
           # Anthos cluster version.**  anthosBareMetalVersion: 1.16.8**
         

  3. Use the `bmctl upgrade cluster` command to complete the upgrade:
         
         bmctl upgrade cluster -c CLUSTER_NAME --kubeconfig ADMIN_KUBECONFIG
         

Replace the following:

     * CLUSTER_NAME: the name of the cluster to upgrade.
     * ADMIN_KUBECONFIG: the path to the admin cluster kubeconfig file.

The cluster upgrade operation runs preflight checks to validate cluster status and node health. The cluster upgrade doesn't proceed if the preflight checks fail. For troubleshooting information, see [Troubleshoot cluster install or upgrade issues](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/create-upgrade).

When all of the cluster components have been successfully upgraded, the cluster upgrade operation performs cluster health checks. This last step verifies that the cluster is in good operating condition. If the cluster doesn't pass all health checks, they continue to run until they pass. When all health checks pass, the upgrade finishes successfully.

For more information about the sequence of events for cluster upgrades, see [Lifecycle and stages of cluster upgrades](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade-lifecycle).




###  `kubectl`

To upgrade a cluster with `kubectl`, perform the following steps:

  1. Edit the cluster configuration file to set `anthosBareMetalVersion` to the upgrade target version.

  2. To initiate the upgrade, run the following command:
         
         kubectl apply -f CLUSTER_CONFIG_PATH
         

Replace `CLUSTER_CONFIG_PATH` with the path to the edited cluster configuration file.




As with the upgrade process with `bmctl`, preflight checks are run as part of the cluster upgrade to validate cluster status and node health. If the preflight checks fail, the cluster upgrade is halted. To troubleshoot any failures, examine the cluster and related logs, since no bootstrap cluster is created. For more information, see [Troubleshoot cluster install or upgrade issues](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/create-upgrade).

Although you don't need the latest version of `bmctl` to upgrade cluters with `kubectl`, we recommend that you [download the latest `bmctl`](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/downloads). You need `bmctl` to perform other tasks, such as health checks and backups, to ensure that your cluster stays in good working order.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
