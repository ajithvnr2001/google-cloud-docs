---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade/
title: Upgrade clusters \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:13:38.978950+00:00
---

# Upgrade clusters  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Upgrade clusters Stay organized with collections  Save and categorize content based on your preferences. 

When you install a new version of `bmctl`, you can upgrade your existing clusters that were created with an earlier version. Upgrading a cluster to the latest Google Distributed Cloud version brings added features and fixes to your cluster. It also ensures that your cluster remains [supported](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#version-support). You can upgrade admin, hybrid, standalone, or user clusters with the `bmctl upgrade cluster` command, or you can use `kubectl`.

To learn more about the upgrade process and versioning rules, see [Lifecycle and stages of cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade-lifecycle).

This page is for Admins and architects and Operators who manage the lifecycle of the underlying tech infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

**Note:** When upgrading Google Distributed Cloud from a version with a security patch to the next minor release, we recommend you upgrade to the highest patch version available to ensure you have the latest security patches. Always review the release notes before upgrading so you are aware of what has changed, including security fixes and known issues. Downgrading to a lower cluster version isn't supported.

## Plan your upgrade

This section contains information and links to information that you should consider before you upgrade a cluster. For more information about upgrades, including versioning rules for clusters and node pools, see [Lifecycle and stages of cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade-lifecycle).

### Best practices

For information to help you prepare for a cluster upgrade, see [Best practices for Google Distributed Cloud cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade-best-practices).

### Upgrade preflight checks

Preflight checks are run as part of the cluster upgrade to validate cluster status and node health. The cluster upgrade doesn't proceed if the preflight checks fail. For more information on preflight checks, see [Understand preflight checks](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/preflight).

You can check if the clusters are ready for an upgrade by running the preflight check before running the upgrade. For more information, see [Preflight checks for upgrades](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/preflight#preflight_checks_for_upgrades).

### Known issues

For information about potential problems related to cluster upgrades, see [Google Distributed Cloud for bare metal known issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) and select the **Upgrades and updates** problem category.

## Configure upgrade options

Before you start a cluster upgrade, you can configure the following upgrade options that control how the upgrade process works:

  * Selective worker node pool upgrades: upgrade specific worker node pools separately from the rest of the cluster.

  * Parallel upgrades: configure the upgrade process to upgrade groups of nodes or node pools simultaneously.




These options can reduce the risk of disruptions to critical applications and services and significantly reduce overall upgrade time. These options are especially useful for large clusters with numerous nodes and node pools running important workloads. For more information about what these options do and how to use them, see the following sections.

### Skip upgrades

Starting with version 1.33, Google Distributed Cloud supports skip upgrades for all cluster types, letting you upgrade a cluster to a target version (1.33 or higher) that is two minor versions ahead of its current version in a single operation. For example, you can upgrade from version `1.**N**._X_` directly to version `1.**N+2**._Z_` with a single operation.

The following list shows the launch stage for this feature per version, where the version is the upgrade target version:

  * 1.34 and higher: GA
  * 1.33: [Preview](https://cloud.google.com/products#product-launch-stages)
  * 1.32 and lower: Not available



Skip upgrades help you access the latest features and fixes more quickly than with incremental upgrades. Skip upgrades can also extend the time between required upgrade operations, reducing potential disruptions. You can use skip upgrades together with other upgrade options, such as selective worker node pool upgrades and parallel upgrades.

During a skip upgrade, the system upgrades the cluster to an intermediate minor version and then immediately upgrades it to the target version. This intermediate version has implications if you use a registry mirror. For more information, see Additional requirement for registry mirrors.

Skip upgrades for clusters is in [Preview](https://cloud.google.com/products#product-launch-stages) for version 1.33. We recommend that don't perform skip upgrades from 1.31 to 1.33 with production clusters.

#### Skip upgrade prerequisites

The process for performing a skip upgrade isn't different from performing a sequential upgrade, but there are some additional prerequisites:

  1. Verify that the cluster is in a state where a skip upgrade doesn't violate [cluster and node pool version rules](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade-lifecycle#version_rules):

     * Before you start a skip upgrade for an admin or hybrid cluster, ensure that all of its managed user clusters are at the same minor version as the managing cluster.

     * Before you start a skip upgrade for a user cluster, ensure that your clusters meet the following criteria:

       * The associated managing admin or hybrid cluster is two minor versions higher than the user cluster.

       * All worker node pools for the user cluster are at the same minor version as the user cluster.

  2. Add the `preview.baremetal.cluster.gke.io/skip-minor-version-cluster-upgrade` annotation to the cluster configuration file:
         
         apiVersion: baremetal.cluster.gke.io/v1
         kind: Cluster
         metadata:
           name: baremetal-demo
           namespace: cluster-baremetal-demo
           annotations:**    preview.baremetal.cluster.gke.io/skip-minor-version-cluster-upgrade: "enable"**
         spec:
           type: user
           profile: default
           anthosBareMetalVersion:   1.36.200-gke.118
           ...
         

  3. Update `anthosBareMetalVersion` in the cluster configuration file to the upgrade target version of the skip upgrade.




As with sequential upgrades, you can start the skip upgrade with either `bmctl upgrade cluster` or `kubectl apply`.

#### Additional requirement for registry mirrors

If you pull container images from a [registry mirror](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/registry-mirror) to upgrade your cluster, your registry mirror must have the images for both the target version and the intermediate version of the skip upgrade.

To prepare your registry mirror for a skip upgrade, follow these steps:

  1. Using the version of `bmctl` that corresponds to the target version of the skip upgrade, find out what's the intermediate version for the skip upgrade:
         
         bmctl upgrade intermediate-version
         

The command response consists of the specific Google Distributed Cloud patch version that the system uses as the intermediate version during the skip upgrade. For example, for `bmctl` version 1.33.0-gke.799, the response looks like the following:
         
         1.32.200-gke.104
         

  2. Download the images packages for both the target version and the intermediate version.

For more information, see [Download the images package](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads#download_the_images_package).

  3. Push the images packages for both the target version and the intermediate version to the registry mirror before starting the skip upgrade.

Hosting container images for both the target and intermediate versions requires [additional disk space](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/registry-mirror#before_you_begin) for your registry mirror.




As with sequential upgrades, you can start the skip upgrade with either `bmctl upgrade cluster` or `kubectl apply`.

### Selective worker node pool upgrades

By default, the cluster upgrade operation upgrades every node and node pool in the cluster. A cluster upgrade can be disruptive and time consuming, as it results in each node being drained and all associated pods being restarted and rescheduled. This section describes how you can include or exclude select worker node pools for a cluster upgrade to minimize workload disruption. This feature applies to user, hybrid, and standalone clusters only, since admin clusters don't allow worker node pools.

You might use selective node pool upgrades in the following situations:

  * **To pick up security fixes without disrupting workloads:** You can upgrade just your control plane nodes (and load balancer nodes) to apply Kubernetes vulnerability fixes without disrupting your worker node pools.

  * **To confirm proper operation of an upgraded subset of worker nodes before upgrading all worker nodes:** You can upgrade your worker node pools selectively to ensure that workloads are running properly on an upgraded node pool before you upgrade another node pool.

  * **To reduce the maintenance window:** Upgrading a large cluster can be time consuming and it's difficult to accurately predict when an upgrade will complete. Cluster upgrade time is proportional to the number of nodes being upgraded. Reducing the number of nodes being upgraded by excluding node pools reduces the upgrade time. You upgrade multiple times, but the smaller, more predictable maintenance windows may help with scheduling.




#### Two minor version node pool version skew

For version 1.28 and higher clusters, a worker node pool version can be up to _two_ minor versions behind the cluster (control plane) version. With _n-2_ version skew support, you can also _skip_ a minor release version when you upgrade a worker node pool from two minor versions behind the cluster to the same minor version as the cluster.

This _n-2_ version skew support for worker node pools gives you more flexibility to plan your fleet upgrades.

For example, if you have a version 1.36 cluster, you can have worker node pools at select 1.36, 1.35, and 1.34 versions.

Before you can upgrade a cluster, all of the worker node pools must be at a version that is compatible with both the current cluster version and the target cluster version.

For example, if you have a cluster at version 1.29 and worker node pools at version 1.29, version 1.28, and version 1.16, you must upgrade the version 1.16 node pools to version 1.28 or 1.29 before you can upgrade the cluster to version 1.30.

For more information, including lists of supported worker node pool versions supported by a given cluster version (applicable for version 1.29 and earlier), see [Node pool versioning rules](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade-lifecycle#np_version_rules)

###  1.30 and higher 

In release 1.30, _n-2_ version skew support for worker node pools is GA for all cluster types. This feature is enabled by default for clusters at version 1.30.

Node pools at any patch version of the 1.28 and 1.29 minor versions can be upgraded to any patch version of 1.30, if the node pool version is the same or lower than the cluster version.

###  1.29 

In release 1.29, _n-2_ version skew support for worker node pools is GA for all cluster types. This feature is enabled by default for clusters at version 1.29.

As we transition this feature from Public Preview to GA, hybrid clusters still require the preview annotation in the following situation. If you have a version 1.28.x hybrid cluster with a version 1.16.y worker node pool, you must add the `preview.baremetal.cluster.gke.io/two-minor-version-node-pool: enable` annotation to the cluster _before_ you upgrade it to version 1.29.z:
    
    
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: baremetal-demo
      namespace: cluster-baremetal-demo
      annotations:**    preview.baremetal.cluster.gke.io/two-minor-version-node-pool: enable**
    spec:
      type: hybrid
      profile: default
      anthosBareMetalVersion: 1.28.400-gke.77
      ...
    

###  1.28 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The n-2 version skew support for worker node pools is available for [Preview](https://cloud.google.com/products/#product-launch-stages) in release 1.28. To enable this Preview capability, add the `preview.baremetal.cluster.gke.io/two-minor-version-node-pool: enable` annotation to your cluster configuration file:
    
    
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: baremetal-demo
      namespace: cluster-baremetal-demo
      annotations:**    preview.baremetal.cluster.gke.io/two-minor-version-node-pool: enable**
    spec:
    ...
    

If you don't enable this Preview capability, the maximum version skew between a worker node pool and the cluster is one minor version.

For more information about the versioning rules for selectively upgrading worker node pools, see [Node pool versioning rules](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade-lifecycle#np_version_rules) in Lifecycle and stages of cluster upgrades.

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



For example, suppose that your cluster is at version 1.35.0 and has two worker node pools: `wpool01` and `wpool02`. Also, suppose that you want to upgrade the control plane and `wpool01` to 1.36.200-gke.118, but you want `wpool02` to remain at version 1.35.0.

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
      profile: default**  anthosBareMetalVersion: 1.36.200-gke.118**
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: NodePool
    metadata:
      name: wpool01
      namespace: cluster-user001
    spec:
      clusterName: user001**  anthosBareMetalVersion: 1.36.200-gke.118**
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
      clusterName: user001**  anthosBareMetalVersion: 1.35.0**
      nodes:
      - address:  10.200.1.1
      - address:  10.200.1.2
      - address:  10.200.1.3
      ...
      - address:  10.200.1.12
    

#### Upgrade node pools to the current cluster version

If you've excluded node pools from a cluster upgrade, you can run a cluster upgrade that brings them up to the target cluster version. Worker node pools that have been excluded from a cluster upgrade have the `anthosBareMetalVersion` field in their `NodePool` spec set to the previous (pre-upgrade) cluster version.

To bring worker node pools up to the current, upgraded cluster version:

  1. Edit the `NodePool` specs in the cluster configuration file for the worker node pools that you want to bring up to the current cluster version. Set `anthosBareMetalVersion` to the current (post-upgrade) cluster version.

If multiple worker node pools are selected for upgrade, the value of`spec.nodePoolUpgradeStrategy.concurrentNodePools` in the cluster spec determines how many node pools are upgraded in parallel, if any. If you don't want to upgrade worker node pools concurrently, select one node pool at a time for upgrade.

  2. Continue with your upgrade as described in Start the cluster upgrade.

The cluster upgrade operation upgrades only the previously excluded worker node pools for which you have set `anthosBareMetalVersion` to the current, upgraded cluster version.




For example, suppose that you upgraded your cluster to version 1.36.200-gke.118, but node pool `wpool02` is still at the old, pre-upgrade cluster version 1.35.0. Workloads are running properly on the upgraded node pool, `wpool01`, so now you want to bring `wpool02` up to the current cluster version, too. To upgrade `wpool02`, you can remove the `anthosBareMetalVersion` field or set its value to the empty string.

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
      profile: default**  anthosBareMetalVersion: 1.36.200-gke.118**
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: NodePool
    metadata:
      name: wpool01
      namespace: cluster-user001
    spec:
      clusterName: user001**  anthosBareMetalVersion: 1.36.200-gke.118**
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
    

#### Roll back a node pool upgrade

There are many dependencies, such as compatibility with kubelet or plugins, that can affect the performance of your workloads. In the event that you encounter a problem after upgrading a worker node pool, you can roll back the node pool to its previous version.

This feature isn't at the same launch phase for all supported cluster versions:

###  1.30 and higher 

For version 1.30 clusters (clusters with control plane nodes at version 1.30), the node pool rollback capability is GA and enabled by default.

###  1.29 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The node pool rollback capability is available for [Preview](https://cloud.google.com/products/#product-launch-stages) for version 1.29 clusters (clusters with control plane nodes at version 1.29). While this feature is in Preview, you must add the following annotation to the `Cluster` resource to enable the feature:
    
    
    preview.baremetal.cluster.gke.io/worker-node-pool-upgrade-rollback: enable
    

###  1.28 

The node pool rollback capability isn't available for clusters at minor version 1.28 or earlier.

To roll back a node pool upgrade, use the following steps:

###  `bmctl`

When you use `bmctl` to roll back a node pool upgrade, you edit the cluster configuration file and apply your changes with the `bmctl update` command:

  1. Edit the `NodePool` specs in the cluster configuration file for the worker node pools that you want to roll back to the previous version. Set `anthosBareMetalVersion` to the previous (pre-upgrade) cluster version.
         
         ...
         ---
         apiVersion: baremetal.cluster.gke.io/v1
         kind: NodePool
         metadata:
           name: wpool01
           namespace: cluster-user001
         spec:
           clusterName: user001**  anthosBareMetalVersion: 1.35.600-gke.141**
           nodes:
           - address:  10.200.0.1
           - address:  10.200.0.2
           - address:  10.200.0.3
           ...
         

If multiple worker node pools are selected for rollback, the value of `spec.nodePoolUpgradeStrategy.concurrentNodePools` in the cluster spec determines how many node pools are rolled back in parallel. If you don't want to roll back worker node pools concurrently, select one node pool at a time for rollback or update the `nodePoolUpgradeStrategy` settings. Likewise, the value of `spec.upgradeStrategy.parallelUpgrade.concurrentNodes` in the `NodePool` spec determines how many nodes are rolled back in parallel.

  2. Use `bmctl update` to apply your `NodePool` spec changes:
         
         bmctl update cluster -c CLUSTER_NAME --kubeconfig=ADMIN_KUBECONFIG
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster you want to update.

     * `ADMIN_KUBECONFIG`: the path of the kubeconfig file of the managing cluster (admin, hybrid, or standalone).

The rollback starts automatically. The `bmctl update cluster` command exits immediately, but the rollback continues to progress. Don't perform any other operations on the cluster while the rollback is in progress.

  3. As the rollback runs, Google Distributed Cloud performs the following activities for each node:

     * Put the node into maintenance mode.
     * Run a reset job on the node to bring it to a clean state.
     * Run [machine preflight checks](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/preflight#pre_create_what) on the node.
     * Run a machine-init job on the node to reinstall it at the target rollback (pre-upgrade) version.
     * Remove the node from maintenance mode.

At the end of a successful rollback, the value of `nodePool.status.anthosBareMetalVersion` in the `NodePool` resource is set to the target rollback version.


Don't use `bmctl update` and `kubectl apply -f` interchangeably when editing the cluster configuration file. When these commands are used interchangeably, contents populated by the header of the cluster spec might be unintentionally removed. For example, you might use `bmctl update` to update the cluster configuration file to [configure a registry mirror](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/registry-mirror#create_clusters_from_the_registry_mirror). The cluster then has `spec.nodeConfig.registryMirrors` populated after reconciliation. 

If you then attempt to make changes to the cluster using the cluster configuration with the `kubectl apply -f` command, the `spec.nodeConfig.registryMirrors` populated by the reconciler on the cluster is removed. This behavior happens because the configuration doesn't exist in the cluster configuration spec, but it does in the cluster. 

###  `kubectl`

You can roll back a node pool upgrade by using `kubectl` to edit the `NodePool` resource directly:

  1. To roll back a worker node pool, open the `NodePool` resource for editing:
         
         kubectl edit nodepool NODE_POOL_NAME \
             --namespace CLUSTER_NAMESPACE \
             --kubeconfig ADMIN_KUBECONFIG
         

Replace the following:

     * `NODE_POOL_NAME`: the name of the node pool you're rolling back.

     * `CLUSTER_NAMESPACE`: the name of the namespace in which the node pool is deployed. This is the cluster namespace.

     * `ADMIN_KUBECONFIG`: the path of the kubeconfig file of the managing cluster (admin, hybrid, or standalone).

  2. Change the value of `spec.anthosBareMetalVersion` to the previous (pre-upgrade) version.
         
         ...
         ---
         apiVersion: baremetal.cluster.gke.io/v1
         kind: NodePool
         metadata:
           name: wpool01
           namespace: cluster-user001
         spec:
           clusterName: user001**  anthosBareMetalVersion: 1.35.600-gke.141**
           nodes:
           - address:  10.200.0.1
           - address:  10.200.0.2
           - address:  10.200.0.3
           ...
         

  3. Save and close the `NodePool` resource in your editor.

The rollback starts automatically. Don't perform any other operations on the cluster while the rollback is in progress.

  4. As the rollback runs, Google Distributed Cloud performs the following activities for each node:

     * Put the node into maintenance mode.
     * Run a reset job on the node to bring it to a clean state.
     * Run [machine preflight checks](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/preflight#pre_create_what) on the node.
     * Run a machine-init job on the node to reinstall it at the target rollback (pre-upgrade) version.
     * Remove the node from maintenance mode.

At the end of a successful rollback, the value of `nodePool.status.anthosBareMetalVersion` in the `NodePool` resource is set to the target rollback version.




### Parallel upgrades

In a typical, default cluster upgrade, each cluster node is upgraded sequentially, one after the other. This section shows you how to configure your cluster and worker node pools so that multiple nodes upgrade in parallel when you upgrade your cluster. Upgrading nodes in parallel speeds up cluster upgrades significantly, especially for clusters that have hundreds of nodes.

**Caution:** If you use managed data services, such a Portworx, to help manage stateful workloads on your clusters, we recommend that you don't use parallel upgrades.

There are two parallel upgrade strategies that you can use to speed up your cluster upgrade:

  * **Concurrent node upgrade:** you can configure your worker node pools so that multiple nodes upgrade in parallel. Parallel upgrades of nodes are configured in the NodePool spec (`spec.upgradeStrategy.parallelUpgrade`) and only nodes in a worker node pool can be upgraded in parallel. Nodes in control plane or load balancer node pools can only be upgraded one at a time. For more information, see Node upgrade strategy.

  * **Concurrent node pool upgrade:** you can configure your cluster so that multiple node pools upgrade in parallel. Only worker node pools can be upgraded in parallel. Control plane and load balancer node pools can only be upgraded one at a time.




#### Node upgrade strategy

You can configure worker node pools so that multiple nodes upgrade concurrently (`concurrentNodes`). You can also set a minimum threshold for the number of nodes able to run workloads throughout the upgrade process (`minimumAvailableNodes`). This configuration is made in the NodePool spec. For more information about these fields, see the [Cluster configuration field reference](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#upgradestrategy).

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
           anthosBareMetalVersion: 1.36.200-gke.118
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

**Note:** You should upgrade an admin cluster before upgrading any associated user clusters. However, before upgrading the admin cluster to `1.36.200-gke.118`, make sure its associated user clusters are at version `1.35.0` or higher. `bmctl` emits an error if it finds any user cluster is with a version lower than `1.35.0`.

###  `bmctl`

When you download and install a new version of `bmctl`, you can upgrade your admin, hybrid, standalone, and user clusters created with an earlier version. For a given version of `bmctl`, a cluster can be upgraded to the same version only.

  1. Set your user credentials as Application Default Credentials (ADC):
         
         gcloud auth application-default login
         

Follow the prompts to select your Google Account for ADC. For more information, see [Set up Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc).

  2. Download the latest `bmctl` as described in [Google Distributed Cloud downloads](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads).

  3. Update `anthosBareMetalVersion` in the cluster configuration file to the upgrade target version.

The upgrade target version must match the version of the downloaded `bmctl` file. The following cluster configuration file snippet shows the `anthosBareMetalVersion` field updated to the latest version:
         
         ---
         apiVersion: baremetal.cluster.gke.io/v1
         kind: Cluster
         metadata:
           name: cluster1
           namespace: cluster-cluster1
         spec:
           type: admin
           # Anthos cluster version.**  anthosBareMetalVersion: 1.36.200-gke.118**
         

  4. Use the `bmctl upgrade cluster` command to complete the upgrade:
         
         bmctl upgrade cluster -c CLUSTER_NAME --kubeconfig ADMIN_KUBECONFIG
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster to upgrade.
     * `ADMIN_KUBECONFIG`: the path to the admin cluster kubeconfig file.
**Note:** The `bmctl upgrade` command updates only the `anthosBareMetalVersion` value and preview annotations in the Cluster custom resource. If you want to modify other fields of the cluster spec, then use the `bmctl update` command. For more information, see [Update clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/update-clusters).

The cluster upgrade operation runs preflight checks to validate cluster status and node health. The cluster upgrade doesn't proceed if the preflight checks fail. For troubleshooting information, see [Troubleshoot cluster install or upgrade issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/create-upgrade).

When all of the cluster components have been successfully upgraded, the cluster upgrade operation performs cluster health checks. This last step verifies that the cluster is in good operating condition. If the cluster doesn't pass all health checks, they continue to run until they pass. When all health checks pass, the upgrade finishes successfully.

For more information about the sequence of events for cluster upgrades, see [Lifecycle and stages of cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade-lifecycle).




###  `kubectl`

To upgrade a cluster with `kubectl`, perform the following steps:

  1. Edit the cluster configuration file to set `anthosBareMetalVersion` to the upgrade target version.

  2. To initiate the upgrade, run the following command:
         
         kubectl apply -f CLUSTER_CONFIG_PATH
         

Replace `CLUSTER_CONFIG_PATH` with the path of the edited cluster configuration file.

As with the upgrade process with `bmctl`, preflight checks are run as part of the cluster upgrade to validate cluster status and node health. If the preflight checks fail, the cluster upgrade is halted. To troubleshoot any failures, examine the cluster and related logs, since no bootstrap cluster is created. For more information, see [Troubleshoot cluster install or upgrade issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/create-upgrade).




Although you don't need the latest version of `bmctl` to upgrade cluters with `kubectl`, we recommend that you [download the latest `bmctl`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). You need `bmctl` to perform other tasks, such as health checks and backups, to ensure that your cluster stays in good working order.

## Pause and resume upgrades

The upgrade pause and resume feature lets you pause a cluster upgrade before it finishes. When a cluster upgrade is paused, no new worker node upgrades are triggered until the upgrade is resumed.

This feature is available in ([Preview](https://cloud.google.com/products/#product-launch-stages)) for clusters with all control plane nodes at minor version 1.28 or higher. The feature is GA for clusters with all control plane nodes at minor version 1.29 or higher.

You might want to pause an upgrade for the following reasons:

  * You've detected something wrong with cluster workloads during the upgrade and you want to pause the upgrade to look into the issue

  * You have short maintenance windows, so you want to pause the upgrade in between windows




While a cluster upgrade is paused, the following operations are supported:

  * [Adding or removing nodes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/update-clusters#add_or_remove_nodes_in_a_cluster)
  * [Adding or removing node pools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/add-remove-node-pools)
  * [Increasing service network range](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/update-clusters#increase_service_network_range)
  * [Restore a cluster from a backup](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/bmctl-backup-restore#restore_a_cluster)



When a new node is added while an upgrade is paused, machine check jobs don't run on it until the upgrade is resumed and completed.

While the cluster upgrade is paused, the following cluster operations aren't supported:

  * [Rotating certificate authorities](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/ca-rotation#start_a_cluster_ca_rotation)
  * [Backing up a cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/bmctl-backup-restore#back_up_a_cluster)



You can't initiate a new cluster upgrade while an active cluster upgrade is paused.

### Enable upgrade pause and resume

###  Google Distributed Cloud 1.36 

The upgrade pause and resume feature is enabled by default for clusters with all control plane nodes at minor version 1.29 or higher.

###  Google Distributed Cloud 1.35 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

While the upgrade pause and resume capability is in Preview, you can enable it with an annotation in the Cluster resource.

To enable upgrade pause and resume, use the following steps:

  1. Add the `preview.baremetal.cluster.gke.io/upgrade-pause-and-resume` annotation to your cluster configuration file:
         
         apiVersion: baremetal.cluster.gke.io/v1
         kind: Cluster
         metadata:
           name: baremetal-demo
           namespace: cluster-baremetal-demo
           annotations:**    preview.baremetal.cluster.gke.io/upgrade-pause-and-resume: enable**
         spec:
         ...
         

  2. To apply the change, update your cluster:
         
         bmctl update cluster -c CLUSTER_NAME --kubeconfig=ADMIN_KUBECONFIG
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster you want to update.
     * `ADMIN_KUBECONFIG`: for admin, hybrid, or standalone clusters, enter the path to the cluster's kubeconfig file. For a user cluster, enter the path to the **admin** cluster's kubeconfig file.

The [`nodePoolUpgradeStrategy.pause`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#nodepoolupgradestrategy-pause) field is mutable. You can add and update it at any time.




### Pause an upgrade

You pause a cluster upgrade by setting `nodePoolUpgradeStrategy.pause` to `true` in the Cluster spec.

To pause an active cluster upgrade, use the following steps:

  1. Add `nodePoolUpgradeStrategy.pause` to the cluster configuration file and set it to `true`:
         
         apiVersion: baremetal.cluster.gke.io/v1
         kind: Cluster
         metadata:
           name: baremetal-demo
           namespace: cluster-baremetal-demo
           ...
         spec:
           ...**  nodePoolUpgradeStrategy:
             pause: true**
           ...
         

If you used `bmctl` to initiate the upgrade, you need a new terminal window to perform the next step.

  2. To apply the change, update your cluster:
         
         bmctl update CLUSTER_NAME
         

The upgrade operation is paused. No new node upgrades are triggered.

  3. If you used `bmctl` to initiate the upgrade and you're planning for a long-lasting pause, press `Control+C` to exit `bmctl`, otherwise, keep `bmctl` running.

The `bmctl` CLI doesn't detect changes in the upgrade pause status, so it doesn't exit automatically. However, when you exit `bmctl`, it stops logging upgrade progress to the `cluster-upgrade-TIMESTAMP` log file in the cluster folder on your admin workstation and to Cloud Logging. Therefore, for short pauses, you may want to keep `bmctl` running. If you leave `bmctl` running for an extended period while the upgrade is paused, it eventually times out.




### Resume a paused upgrade

You resume a paused cluster upgrade by either setting `nodePoolUpgradeStrategy.pause` to `false` in the Cluster spec or removing `nodePoolUpgradeStrategy.pause` from the spec.

To resume a cluster upgrade that's been paused, use the following steps:

  1. Set `nodePoolUpgradeStrategy.pause` to the cluster configuration file and set it to `false`:
         
         apiVersion: baremetal.cluster.gke.io/v1
         kind: Cluster
         metadata:
           name: baremetal-demo
           namespace: cluster-baremetal-demo
           ...
         spec:
           ...**  nodePoolUpgradeStrategy:
             pause: false**
           ...
         

Alternatively, you can remove the `pause` field, because it defaults to `false`.

  2. To apply the change, update your cluster:
         
         bmctl update CLUSTER_NAME
         

The upgrade operation resumes where it left off.

  3. To check the status of the upgrade, first get a list of the resources that have `anthosBareMetalVersion` in their `status`:
         
         kubectl get RESOURCE --kubeconfig ADMIN_KUBECONFIG --all_namespaces
         

Replace the following:

     * `RESOURCE`: the name of the resource that you want to get. `Cluster`, `NodePool`, and `BareMetalMachine` resources all contain `anthosBareMetalVersion` status information.

     * `ADMIN_KUBECONFIG`: the path of the admin cluster kubeconfig file.

The following sample shows the format of the response for `BareMetalMachine` custom resources. Each `BareMetalMachine` corresponds to a cluster node.
    
    NAMESPACE              NAME         CLUSTER        READY   INSTANCEID               MACHINE      ABM VERSION   DESIRED ABM VERSION
    cluster-nuc-admin001   192.0.2.52   nuc-admin001   true    baremetal://192.0.2.52   192.0.2.52   1.28.0        1.28.0
    cluster-nuc-user001    192.0.2.53   nuc-user001    true    baremetal://192.0.2.53   192.0.2.53   1.16.2        1.16.2
    cluster-nuc-user001    192.0.2.54   nuc-user001    true    baremetal://192.0.2.54   192.0.2.54   1.16.2        1.16.2
    

  4. To check the `status.anthosBareMetalVersion` (current version of the resource), retrieve details for individual resources:
         
         kubectl describe RESOURCE RESOURCE_NAME \
             --kubeconfig ADMIN_KUBECONFIG \
             --namespace CLUSTER_NAMESPACE
         

The following sample shows the `BareMetalMachine` details for the cluster node with IP address `192.0.2.53`:
         
         Name:         192.0.2.53
         Namespace:    cluster-nuc-user001
         ...
         API Version:  infrastructure.baremetal.cluster.gke.io/v1
         Kind:         BareMetalMachine
         Metadata:
           Creation Timestamp:  2023-09-22T17:52:09Z
           ...
         Spec:
           Address:                    192.0.2.53
           Anthos Bare Metal Version:  1.16.2
           ...
         Status:
           Anthos Bare Metal Version:  1.16.2
         

In this example, the node is at Google Distributed Cloud version 1.16.2.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
