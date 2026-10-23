---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades/
title: Auto-upgrading nodes \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:17.493256+00:00
---

# Auto-upgrading nodes  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Auto-upgrading nodes Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to configure node auto-upgrades in Google Kubernetes Engine (GKE).

**Note:** For GKE Autopilot clusters, node auto-upgrades are enabled by default and can't be overridden.

## Overview

_Node auto-upgrades_ help you keep the [nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#nodes) in your [cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture) up-to-date with the cluster control plane version when your control plane is [updated on your behalf](https://docs.cloud.google.com/kubernetes-engine/upgrades#automatic_cp_upgrades). When you create a new cluster or node pool with the Google Cloud console or the `gcloud` command, node auto-upgrade is enabled by default.

You can learn more about [cluster and node upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades).

Node auto-upgrades provide several benefits:

  * **Lower management overhead:** You don't have to manually track and update your nodes when the control plane is upgraded on your behalf.
  * **Better security:** Sometimes new binaries are released to fix a security issue. With auto-upgrades, GKE automatically ensures that security updates are applied and kept up to date.
  * **Ease of use:** Provides an automatic way to keep your nodes up to date with the latest Kubernetes features.



Node pools with auto-upgrades enabled are scheduled for upgrades when they meet the selection criteria (announced in the [release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes)). Rollouts are phased across multiple weeks to help ensure cluster and fleet stability. When the upgrade is performed, nodes are drained and re-created to match the current control plane version. Modifications on the boot disk of a node VM don't persist across node re-creations. To preserve modifications across node re-creation, use a [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/).

Node auto-upgrade is not available for [Alpha clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters). If you are using a cluster with Windows Server node pools, review [Upgrading Windows Server node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster-windows#upgrading_windows_server_node_pools) before enabling node auto-upgrade.

**Note:** Enabling auto-upgrades does not cause your nodes to upgrade immediately. For more information, see [Cluster and node upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades#node_pool_upgrades).**Important:** Because Compute Engine instances with accelerators (GPUs or TPUs) don't support live migration, Compute Engine must shut down and re-create the nodes during host maintenance. This process can disrupt workloads such as AI/ML training or inference jobs. To minimize disruption, perform both Compute Engine host maintenance and GKE node upgrades at the same time. For more information, see [Perform host maintenance for nodes running training and inference workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/perform-host-maintenance-accelerators).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have an existing Standard cluster. When you create a new cluster with the Google Cloud console or the Google Cloud CLI command, node auto-upgrade is enabled by default. To create a Standard cluster, see [Create a regional cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster).



## Check the state of auto-upgrade for an existing node pool

Node auto-upgrades are enabled, by default, for node pools.

### As set by maintenance exclusions

You can disable node auto-upgrades for all node pools in a cluster by using a [cluster maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#scope_of_maintenance_to_exclude) with the scope of "No minor or node upgrades". Or, if you have a cluster where you want to disable auto-upgrades for some, but not all, node pools, use a [node pool maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#node-pool-exclusions). You can use either of these types of exclusions if your cluster is enrolled in a release channel. To see whether you've configured these exclusions already, [view a cluster's maintenance policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#viewing-maintenance-policy).

### As set by the node auto-upgrades field

Although it's a legacy configuration and not recommended, you can also disable node auto-upgrades by configuring the `autoUpgrade` field for individual node pools. You can check whether auto-upgrade is enabled or disabled for a node pool with this field by using the Google Cloud console or the `gcloud` command.

### gcloud

To check the state of auto-upgrade for a node pool, run the following command:
    
    
    gcloud container node-pools describe NODE_POOL_NAME \
      --cluster CLUSTER_NAME \
      --location CONTROL_PLANE_LOCATION
    

Replace the following:

  * `NODE_POOL_NAME`: the name of the node pool.
  * `CLUSTER_NAME`: the name of the cluster that contains the node pool.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.



Look for the `autoUpgrade` field in the output to see whether auto-upgrades are enabled or disabled for the node pool.
    
    
    management:
      autoUpgrade: true
    

### Console

To check the state of auto-upgrade for a node pool, perform the following:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to view.

  3. Click the **Nodes** tab.

  4. Under **Node Pools** , click the name of the node pool you want to view.

  5. On the **Node pool details** page, under **Management** , view the value of the **Auto-upgrade** field.




## Enable node auto-upgrades for an existing node pool

When you create a new cluster with the Google Cloud console or the `gcloud` command, node auto-upgrade is enabled by default.

You can enable node auto-upgrade if it's disabled. Note that this doesn't affect the configuration of maintenance exclusions, which are the recommended way to prevent GKE from auto-upgrading nodes. For more control over when nodes can be auto-upgraded, consider configuring [maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions).

Use the following instructions to enable node auto-upgrades:

### gcloud

To enable auto-upgrades for an existing node pool, run the following command:
    
    
    gcloud container node-pools update NODE_POOL_NAME \
        --cluster CLUSTER_NAME \
        --location CONTROL_PLANE_LOCATION \
        --enable-autoupgrade
    

Replace the following:

  * `NODE_POOL_NAME`: the name of the node pool.
  * `CLUSTER_NAME`: the name of the cluster that contains the node pool.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.



### Console

To enable auto-upgrades for an existing node pool, perform the following steps:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify.

  3. Click the **Nodes** tab.

  4. Under **Node Pools** , click the name of the node pool you want to modify.

  5. On the **Node pool details** page, click _edit_ **Edit**.

  6. Under **Management** , select the **Enable auto-upgrade** checkbox.

  7. Click **Save**.




## Check the status of node upgrades

You can check the status of an upgrade using [`gcloud container operations`](https://docs.cloud.google.com/sdk/gcloud/reference/container/operations).

View a list of every running and completed operation in the cluster from the last 12 days if there's fewer than 5,000 operations, or the last 5,000 operations:
    
    
    gcloud container operations list \
        --location=CONTROL_PLANE_LOCATION
    

Each operation is assigned an _operation ID_ and an operation type as well as start and end times, target cluster, and status. The list appears similar to the following example:
    
    
    NAME                              TYPE                ZONE           TARGET              STATUS_MESSAGE  STATUS  START_TIME                      END_TIME
    operation-1505407677851-8039e369  CREATE_CLUSTER      us-west1-a     my-cluster                          DONE    20xx-xx-xxT16:47:57.851933021Z  20xx-xx-xxT16:50:52.898305883Z
    operation-1505500805136-e7c64af4  UPGRADE_CLUSTER     us-west1-a     my-cluster                          DONE    20xx-xx-xxT18:40:05.136739989Z  20xx-xx-xxT18:41:09.321483832Z
    operation-1505500913918-5802c989  DELETE_CLUSTER      us-west1-a     my-cluster                          DONE    20xx-xx-xxT18:41:53.918825764Z  20xx-xx-xxT18:43:48.639506814Z
    

To get more information about a specific operation, specify the operation ID as shown in the following command:
    
    
    gcloud container operations describe OPERATION_ID \
        --location=CONTROL_PLANE_LOCATION
    

For example:
    
    
    gcloud container operations describe operation-1507325726639-981f0ed6
    endTime: '20xx-xx-xxT21:40:05.324124385Z'
    name: operation-1507325726639-981f0ed6
    operationType: UPGRADE_CLUSTER
    selfLink: https://container.googleapis.com/v1/projects/.../kubernetes-engine/docs/zones/us-central1-a/operations/operation-1507325726639-981f0ed6
    startTime: '20xx-xx-xxT21:35:26.639453776Z'
    status: DONE
    targetLink: https://container.googleapis.com/v1/projects/.../kubernetes-engine/docs/zones/us-central1-a/clusters/...
    zone: us-central1-a
    

If the upgrade was cancelled or failed and is partially completed, you can [resume](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/update-existing-nodepools#resume) or [roll back](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/update-existing-nodepools#rollback) the upgrade.

## Check node pool upgrade settings

You can see details on the node upgrade strategy being used for your node pools using the [`gcloud container node-pools describe`](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/describe) command. For blue-green upgrades, the command also returns the [current phase](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#phases-of-blue-green-upgrades) of the upgrade.

Run the following command:
    
    
    gcloud container node-pools describe NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION
    

Replace the following:

  * `NODE_POOL_NAME`: the name of the node pool to describe.
  * `CLUSTER_NAME`: the name of the cluster of the node pool to describe.
  * `CONTROL_PLANE_LOCATION`: the location (region or zone) for the control plane, such as `us-central1` or `us-central1-a`.



This command will output the current upgrade settings. The following example shows the output if you are using the blue-green upgrade strategy.
    
    
    upgradeSettings:
      blueGreenSettings:
        nodePoolSoakDuration: 1800s
        standardRolloutPolicy:
          batchNodeCount: 1
          batchSoakDuration: 10s
      strategy: BLUE_GREEN
    

If you are using the blue-green upgrade strategy, the output also includes details about the blue-green upgrade settings and its current intermediate phase. The following example shows what this might look like:
    
    
    updateInfo:
      blueGreenInfo:
        blueInstanceGroupUrls:
        - https://www.googleapis.com/compute/v1/projects/{PROJECT_ID}/zones/{LOCATION}/instanceGroupManagers/{BLUE_INSTANCE_GROUP_NAME}
        bluePoolDeletionStartTime: {BLUE_POOL_DELETION_TIME}
        greenInstanceGroupUrls:
        - https://www.googleapis.com/compute/v1/projects/{PROJECT_ID}/zones/{LOCATION}/instanceGroupManagers/{GREEN_INSTANCE_GROUP_NAME} 
        greenPoolVersion: {GREEN_POOL_VERSION}
        phase: DRAINING_BLUE_POOL
    

## Disable node auto-upgrades

You can disable node auto-upgrade for an existing node pool, if you need to manually manage node upgrades for that node pool. If you want to disable node auto-upgrades for all node pools in a cluster, we recommend that you use a [cluster maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#scope_of_maintenance_to_exclude) with the scope of "No minor or node upgrades". If you have a cluster where you want to disable auto-upgrades for some, but not all, node pools, use a [node pool maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#node-pool-exclusions). You can use either of these types of exclusions if your cluster is enrolled in a release channel.

Although we don't recommend this method, you can alternatively follow the instructions in this section to disable node auto-upgrades for an individual node pool.

Understand the following considerations before disabling node auto-upgrades.

### Considerations before disabling node auto-upgrades

If you disable node auto-upgrades for a node pool by using any of the available methods, GKE does not update the version of the nodes except for [updating to the next minor version at the end of support](https://docs.cloud.google.com/kubernetes-engine/versioning#auto-upgrades-end-of-support). Opting out of node auto-upgrades also does not block GKE from upgrading your cluster's control plane.

#### Disabling prevents version updates, but not all maintenance tasks

Disabling node auto-upgrades only prevents GKE from updating the version of the nodes, but does not prevent GKE from initiating other maintenance tasks. For example, even with node auto-upgrades disabled, triggering [IP address rotation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-rotation), [Cloud DNS](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-dns#enable_scope_dns_in_an_existing_cluster), [enabling network policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy), or [PSC migration](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#December_12_2022) on a cluster re-creates all nodes. To control the timing of maintenance, use [Maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions).

#### Disabling means responsibility of control plane-nodes compatibility

If you disable node auto-upgrade for a node pool, you are responsible for ensuring that the cluster's nodes run a version compatible with the cluster's control plane version, adhering to the [GKE version skew policy](https://docs.cloud.google.com/kubernetes-engine/versioning#version-skew). Disabling node auto-upgrades only prevents node pools from being upgraded until [the end of standard support](https://docs.cloud.google.com/kubernetes-engine/versioning#end-of-standard-support). GKE upgrades nodes that are running an unsupported version after the version has reached the end of support to ensure cluster health.

For details regarding the timing of the end of support, see the [Estimated schedule for release channels](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule#schedule-for-release-channels). Nodes running unsupported versions might not be upgraded immediately upon version end of support, and actual timing can vary at Google's discretion.

#### Disabling does not stop ongoing operations

Disabling node auto-upgrades does not stop or cancel any ongoing upgrades to nodes in node pools. To cancel or stop ongoing upgrades, follow [Cancelling a node upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#cancel). Canceling a node upgrade can be helpful in situations where you find workloads are failing on upgraded nodes and you want to prevent further disruption.

If the upgrade is fully completed for the entire node pool, then the upgrade can't be rolled back or cancelled. To downgrade the node pool, see [Downgrading node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#downgrading_nodes).

### Disable node auto-upgrades for an existing node pool

If you need to disable node auto-upgrades for one existing node pool, we recommend that you use a [node pool maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#node-pool-exclusions). For instructions, see [Add a node pool maintenance exclusion for an existing node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#configure-node-pool-maintenance-exclusion-existing). If you need to disable node auto-upgrades for all node pools in a cluster, use a cluster maintenance exclusion with the scope of "No minor or node upgrades".

You can also use the following instructions, although we don't recommend it, to disable node auto-upgrades for an existing node pool.

### gcloud

To disable auto-upgrades for an existing node pool, run the following command:
    
    
    gcloud container node-pools update NODE_POOL_NAME \
        --cluster CLUSTER_NAME \
        --location CONTROL_PLANE_LOCATION \
        --no-enable-autoupgrade
    

### Console

To disable auto-upgrades for an existing node pool, perform the following steps:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify.

  3. Click the **Nodes** tab.

  4. Under **Node Pools** , click the name of the node pool you want to modify.

  5. On the **Node pool details** page, click _edit_ **Edit**.

  6. Under **Management** , clear the **Enable auto-upgrade** checkbox.

  7. Click **Save** to modify the cluster.




## Create a node pool with node auto-upgrades enabled

GKE node pools have auto-upgrades enabled by default. However, if you want to explicitly specify this default setting, use the following instructions:

### gcloud

To create a node pool with auto-upgrade enabled specify the `--enable-autoupgrade` flag in the `gcloud container node-pools create` command:
    
    
    gcloud container node-pools create NODE_POOL_NAME \
        --cluster CLUSTER_NAME \
        --location CONTROL_PLANE_LOCATION \
        --enable-autoupgrade
    

### Console

Visit [Creating a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-zonal-cluster) or [Adding and managing node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools) for instructions to create clusters and node pools.

## Receive upgrade notifications

GKE publishes upgrade notifications to [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview), providing you with a channel to receive information from GKE about your clusters.

For more information, see [Receiving cluster upgrade notifications](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-upgrade-notifications).

### Change surge upgrade parameters

To learn more about changing surge upgrade parameters, see [Configure surge upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pool-upgrade-strategies#surge).

## Exercise control during a node pool upgrade

During automatic upgrades and manually-initiated node pool upgrades, you can take the following actions.

### Configure concurrent node pool upgrades

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For clusters with many node pools, you can configure concurrent node pool upgrades to decrease the total time required to upgrade the cluster. You configure this by setting the maximum number of node pools that GKE can auto-upgrade simultaneously. In Standard clusters, this setting determines the concurrency of node upgrades for Standard node pools and Autopilot-managed node pools. In Autopilot clusters, this setting determines the concurrency of node upgrades for groups of nodes.

You can configure the concurrency limit when you create a new cluster or update an existing cluster by using the gcloud CLI. Ensure that the node pools you want to auto-upgrade concurrently have auto-upgrades enabled.

You can't enable this feature for a cluster enrolled in a [rollout sequence with custom stages](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing).

To configure concurrent node pool upgrades, run one of the following commands:

  * Create a new cluster with concurrent node pool upgrades configured:
        
        gcloud beta container clusters create CLUSTER_NAME \
            --project=PROJECT_NAME
            --location CONTROL_PLANE_LOCATION \
            --node-pool-upgrade-concurrency-config=max-count=MAX_COUNT
        

  * Update an existing cluster to concurrently upgrade node pools:
        
        gcloud beta container clusters update CLUSTER_NAME \
            --project=PROJECT_NAME \
            --location=CONTROL_PLANE_LOCATION \
            --node-pool-upgrade-concurrency-config=max-count=MAX_COUNT
        




Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.
  * `PROJECT_NAME`: the name of your project.
  * `LOCATION`: the compute location of the cluster.
  * `MAX_COUNT`: the maximum number of node pools to upgrade simultaneously. The value must be an integer between `1` and `100`. To revert to the default sequential behavior, set this value to `1`.



### Cancel a node pool upgrade

You can cancel an upgrade at any time. To learn more about what happens when you cancel a surge upgrade, see [Cancel a surge upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#cancel-a-surge-upgrade). To learn more about what happens when you cancel a blue-green upgrade, see [Cancel a blue-green upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#cancel-a-blue-green-upgrade).

  1. Get the upgrade's operation ID:
         
         gcloud container operations list \
               --location=CONTROL_PLANE_LOCATION
         

  2. Cancel the upgrade:
         
         gcloud container operations cancel OPERATION_ID \
               --location=CONTROL_PLANE_LOCATION
         




Refer to the [`gcloud container operations cancel`](https://docs.cloud.google.com/sdk/gcloud/reference/container/operations/cancel) documentation.

### Resume a node pool upgrade

You can resume an upgrade by manually initiating the upgrade again, specifying the target version from the original upgrade.

If, for example, an upgrade failed, or if you paused an ongoing upgrade, you could resume the canceled upgrade by starting the same upgrade again on the node pool, specifying the target version from the initial upgrade operation.

To learn more about what happens when you resume an upgrade, see [Resume a surge upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#resume-a-surge-upgrade) and [blue-green upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#resume-a-blue-green-upgrade).

To resume an upgrade, use the following command:
    
    
    gcloud container clusters upgrade CLUSTER_NAME \
      --node-pool=NODE_POOL_NAME \
      --location=CONTROL_PLANE_LOCATION \
      --cluster-version VERSION
    

Replace the following:

  * `NODE_POOL_NAME`: the name of the node pool for which you want to resume the node pool upgrade.
  * `CLUSTER_NAME`: the name of the cluster of the node pool for which you want to resume the upgrade.
  * `CONTROL_PLANE_LOCATION`: the location (region or zone) for the control plane, such as `us-central1` or `us-central1-a`.
  * `VERSION`: the target version of the canceled node pool upgrade.



For more information, refer to the [`gcloud container clusters upgrade`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/upgrade) documentation.

### Roll back a node pool upgrade

You can roll back a node pool to downgrade the upgraded nodes to their original state from before the node pool upgrade started.

Use the `rollback` command if an in-progress upgrade was [cancelled](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#cancel), the upgrade failed, or the upgrade is incomplete due to a [maintenance window](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#maintenance_windows) timing out. Alternatively, if you want to specify the version, follow the instructions to [downgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#downgrading_nodes) the node pool.

**Note:** You cannot roll back node pools once they have been successfully upgraded. You must [downgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#downgrading_nodes) the node pool if you need the nodes to be on the previous version.

To learn more about what happens when you roll back a node pool upgrade, see [Roll back a surge upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#rollback-a-surge-upgrade) or [Roll back a blue-green upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#rollback-a-blue-green-upgrade).

To roll back an upgrade, run the following command:
    
    
    gcloud container node-pools rollback NODE_POOL_NAME \
        --cluster CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION
    

Replace the following:

  * `NODE_POOL_NAME`: the name of the node pool for which to to roll back the node pool upgrade.
  * `CLUSTER_NAME`: the name of the cluster of the node pool for which to roll back the upgrade.
  * `CONTROL_PLANE_LOCATION`: the location (region or zone) for the control plane, such as `us-central1` or `us-central1-a`.



Refer to the [`gcloud container node-pools rollback`](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/rollback) documentation.

### Complete a node pool upgrade

**Warning:** Using the `complete-upgrade` command is only possible with [blue-green upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#blue-green-upgrade-strategy).

If you are using the blue-green upgrade strategy, you can complete a node pool upgrade during the [Soak phase](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#bg-phase-soak-node-pool), skipping the rest of the soak time.

To learn how completing a node pool upgrade works, see [Complete a node pool upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#complete-a-blue-green-upgrade).

To complete an upgrade when using the blue-green upgrade strategy, run the following command:
    
    
    gcloud container node-pools complete-upgrade NODE_POOL_NAME \
        --cluster CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION
    

Replace the following:

  * `NODE_POOL_NAME`: the name of the node pool for which you want to complete the upgrade.
  * `CLUSTER_NAME`: the name of the cluster of the node pool for which you want to complete the upgrade.
  * `CONTROL_PLANE_LOCATION`: the location (region or zone) for the control plane, such as `us-central1` or `us-central1-a`.



Refer to the [`gcloud container node-pools complete-upgrade`](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/complete-upgrade) documentation.

## What's next

  * Learn more about [node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools).
  * Learn more about [cluster and node pool upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades).
  * [Manually upgrade a cluster or node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster).
  * Learn more about [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels).
  * [Troubleshoot cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/upgrades).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
