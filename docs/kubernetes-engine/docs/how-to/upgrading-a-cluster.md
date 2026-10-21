---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster/
title: Manually upgrade a cluster's control plane or node pools \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:25:38.204876+00:00
---

# Manually upgrade a cluster's control plane or node pools  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Manually upgrade a cluster's control plane or node pools Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document explains how you can manually request an upgrade or downgrade for the control plane or nodes of a Google Kubernetes Engine (GKE) cluster. GKE automatically upgrades the version of the control plane and nodes to ensure that the cluster receives new features, bug fixes, and security patches. But, as explained in this document, you can also manually perform these upgrades yourself instead. 

For more information about how automatic and manual cluster upgrades work, see [About GKE cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades). You can also control when auto-upgrades can and can't occur by configuring [maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions).

You can manually upgrade the version as follows:

  * **Autopilot clusters** : Upgrade the control plane version.
  * **Standard clusters** : Upgrade the control plane version and the node pool version.



To upgrade a cluster, GKE updates the version that the control plane and nodes run, in separate operations. Clusters are upgraded to either a newer minor version (for example, 1.33 to 1.34) or newer patch version (for example, 1.33.4-gke.1350000 to 1.33.5-gke.1080000). A cluster's control plane and nodes don't necessarily run the same version at all times. For more information about versions, see [GKE versioning and support](https://docs.cloud.google.com/kubernetes-engine/versioning).

For more information about how cluster upgrades work, including automatic and manual upgrades, see [About GKE cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades).

New versions of GKE are [announced regularly](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes), and you can receive notice about the new versions available for each specific cluster with [cluster notifications](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications). To find specific auto-upgrade targets for clusters, [get information about a cluster's upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrade-assist#get-info).

For more information about available versions, see [Versioning](https://docs.cloud.google.com/kubernetes-engine/versioning). For more information about clusters, see [Cluster architecture](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture). For guidance on upgrading clusters, see [Best practices for upgrading clusters](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/upgrading-clusters).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have an existing Autopilot or Standard cluster. To create a new cluster, see [Create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster).



## About upgrading

A cluster's control plane and nodes are upgraded separately. The cluster's control plane and nodes don't necessarily run the same version at all times.

Cluster control planes and nodes are [upgraded](https://docs.cloud.google.com/kubernetes-engine/upgrades#automatic_cp_upgrades) on a regular basis, regardless of whether your cluster is enrolled in a [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels) or not.

### Limitations

[Alpha clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters) can't be upgraded.

### Supported versions

The [release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes) announce when new versions become available and when earlier versions are no longer available. At any time, you can list all supported cluster and node versions using this command:
    
    
    gcloud container get-server-config \
        --location=CONTROL_PLANE_LOCATION
    

Replace `CONTROL_PLANE_LOCATION` with the location (region or zone) for the control plane, such as `us-central1` or `us-central1-a`.

If your cluster is enrolled in a release channel, you can upgrade to a patch version in a different release channel with the same minor version as your control plane. For example, you can upgrade your cluster from version 1.33.4-gke.1350000 in the Regular channel to 1.33.5-gke.1162000 in the Rapid channel. For more information, refer to [Running patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions). All Autopilot clusters are enrolled in release channels.

### About downgrading

You can downgrade the version of your cluster to an earlier version in certain scenarios:

  * **Control plane patch downgrade** : to mitigate an unsuccessful cluster control plane upgrade, you can downgrade your control plane to a previous patch release if the version is an [earlier patch release within the same minor version](https://docs.cloud.google.com/kubernetes-engine/versioning#versioning_scheme). For example, if your cluster's control plane is running GKE 1.33.5-gke.1080000, you can downgrade the control plane to 1.33.4-gke.1350000, if that version is still [available](https://docs.cloud.google.com/kubernetes-engine/versioning#available_versions).
  * **Rollback during two-step control plane minor upgrade** : you can only downgrade a Kubernetes cluster control plane to an earlier minor version after the _binary upgrade_ of a two-step control plane minor upgrade with rollback safety. If GKE has already completed the second step of the two-step upgrade—the _emulated version upgrade_ —you can't roll back to the previous minor version.
  * **Node pool rollback** : you can roll back a partially completed node pool upgrade to an earlier patch release or minor version.
  * **Node pool downgrade** : you can downgrade a node pool to an earlier patch release or minor version, for example, to reverse a completed node pool upgrade that caused issues for your workloads. Ensure that you don't downgrade nodes to a version that is more than [two minor versions behind the cluster control plane version](https://kubernetes.io/releases/version-skew-policy/#supported-version-skew).



Other than the scenarios described in the previous points, you can't downgrade a cluster. You can't downgrade a cluster control plane to a previous minor version, including after a one-step control plane minor upgrade. For example, if your control plane runs GKE version 1.34, you can't downgrade to 1.33. If you attempt to do this, the following error message appears:
    
    
    ERROR: (gcloud.container.clusters.upgrade) ResponseError: code=400,
    message=Master cannot be upgraded to "1.33.4-gke.1350000": specified version is
    not newer than the current version.
    

We recommend that you [test and qualify minor version upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/upgrading-clusters#test-versions) with clusters in a testing environment when a new minor version becomes available but before the version becomes auto-upgrade target for your cluster. This is especially recommended if your cluster might be affected by significant changes in the next minor version, such as [deprecated APIs or features](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations) being removed. For more information about version availability, see [What versions are available in a channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#what_versions_are_available_in_a_channel).

## Upgrade the cluster's control plane

**Note:** You can't upgrade your cluster's control plane more than _one minor version at a time_. For example, you can upgrade a control plane from version 1.33 to 1.34, but not directly from 1.32 to 1.34. For more information, refer to [Can I skip versions during a cluster upgrade?](https://docs.cloud.google.com/kubernetes-engine/versioning#skip-versions).

GKE upgrades cluster's control planes and nodes automatically. To manage how GKE upgrades your clusters, see [Control cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#how-to-control-upgrades).

With [Autopilot clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) and [regional Standard clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/regional-clusters#about_regional_clusters), the control plane remains available during control plane upgrades. However, when you initiate a control plane upgrade for [zonal clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/configuration-overview#zonal), you can't modify the cluster's configuration until the control plane is accessible again in a few minutes. Control plane upgrades don't affect the availability of the worker nodes that your workloads run on because they remain available during control plane upgrades.

As part of managing the versions of your cluster, you can initiate a manual upgrade any time after a new version becomes available, using one of the following methods:

  * **One-step upgrade** : upgrade your control plane directly to a later minor version or patch version as quickly as possible. You can use this approach if you've already validated your cluster and workload performance on the new minor version.
  * **Two-step control plane minor upgrade with rollback safety** : upgrade your control plane to a later minor version using a two-step process where you can validate the new minor version for a period of soak time, and roll back if needed. This upgrade method is only available for upgrading to 1.33 or later, for control plane minor upgrades.



### Manually upgrade the control plane with a one-step upgrade

You can manually upgrade your Autopilot or Standard control plane using the Google Cloud console or the Google Cloud CLI.

### Console

To manually update your cluster control plane, perform the following steps:

  1. Go to the **Google Kubernetes Engine** page in Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click the name of the cluster.

  3. Under **Cluster basics** , click _edit_ **Upgrade Available** next to **Version**.

  4. Select the new version, then click **Save Changes**.




### gcloud

To see the available versions for your cluster's control plane, run the following command:
    
    
    gcloud container get-server-config \
        --location=CONTROL_PLANE_LOCATION
    

To upgrade to the default cluster version, run the following command:
    
    
    gcloud container clusters upgrade CLUSTER_NAME \
        --master \
        --location=CONTROL_PLANE_LOCATION
    

To upgrade to a specific version that is not the default, specify the `--cluster-version` flag as in the following command:
    
    
    gcloud container clusters upgrade CLUSTER_NAME \
        --master \
        --location=CONTROL_PLANE_LOCATION \
        **--cluster-version =VERSION**
    

Replace `VERSION` with the version that you want to upgrade your cluster to. You can use a specific version, such as `1.32.9-gke.1072000` or you can use a version alias, like `latest`. For more information, see [Specifying cluster version](https://docs.cloud.google.com/kubernetes-engine/versioning#specifying_cluster_version).

**Note:** If your cluster is enrolled in a release channel, the `VERSION` must be a valid minor version for the release channel, or a valid patch version in a newer release channel. All Autopilot clusters are enrolled in a release channel.

After upgrading a Standard control plane, you can upgrade its nodes. By default, Standard nodes created using the Google Cloud console have auto-upgrade enabled, so this happens automatically. Autopilot always upgrades nodes automatically.

### Two-step control plane minor upgrade with rollback safety

You can manually upgrade the control plane of your GKE Autopilot or Standard cluster to the next minor version with a two-step upgrade. GKE also performs this two-step process when performing automatic control plane minor upgrades to 1.33 or later, for clusters that aren't enrolled in a [rollout sequence](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing).

In this two step process, you can test how your cluster performs with the new minor version, known as the _binary version_ , while using the features and APIs from the previous minor version, known as the _emulated version_. During this soak time, where the control plane runs in what's known as _emulated mode_ , you can roll back to the previous minor version, if necessary. For more information about how Kubernetes allows for this type of upgrade, see [Compatibility Version For Kubernetes Control Plane Components](https://kubernetes.io/docs/concepts/cluster-administration/compatibility-version/).

Two-step upgrades work in the following way:

  1. **Binary upgrade** : GKE upgrades the control plane binary to the new minor version, but emulates the previous minor version:

     * **Emulates previous version** : the cluster runs the new binary, but continues to emulate the behavior of the previous minor version API. For example, you can call APIs that are removed in the new minor version, but are still available in the previous minor version.
     * **Test new binary** : you can test the new binaries for regressions, fixes, and performance changes before you make accessible the Kubernetes features available with the new minor version. Monitor application metrics, logs, Pod statuses, error rates, and latency.
     * **Soak the changes** : wait for 6 hours to 7 days (24 hours for auto-upgrades) to give yourself time to test and monitor. After this time, GKE performs the emulated version upgrade.
     * **Roll back or complete the upgrade** : you can roll back, if needed. Or, you can advance to the next stage if you're confident with the new minor version, don't want to wait for the soak time to complete, and are ready to start using the new features and API changes.
  2. **Emulated version upgrade** : GKE updates the emulated version to match the new binary version.

     * **Enables new features** : all new features and API changes of the new minor version are enabled.
     * **No rollback** : after this step occurs, you can't roll back to the original minor version. The upgrade is complete.



During this operation, the following limitations apply:

  * You can't initiate a one-step control plane minor upgrade.
  * You can't create or upgrade the nodes to a version that is later than the emulated version.
  * GKE doesn't perform any type of automatic upgrades to the control plane or nodes.



When GKE performs an automatic control plane minor upgrade by using this two-step process, GKE only initiates the binary upgrade and emulated version upgrade when there is no [maintenance window or exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions) preventing upgrades.

#### Start a two-step upgrade

Start a two-step upgrade by running the following command:
    
    
    gcloud beta container clusters upgrade CLUSTER_NAME \
      --location=CONTROL_PLANE_LOCATION \
      --cluster-version VERSION \
      --control-plane-soak-duration SOAK_DURATION \
      --master
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.
  * `CONTROL_PLANE_LOCATION`: the location (region or zone) for the control plane, such as `us-central1` or `us-central1-a`.
  * `VERSION`: a specific patch of the next minor version. For example, if your cluster runs 1.33, `1.34.1-gke.1829001`.
  * `SOAK_DURATION`: the time to wait in the rollback-safe stage. You can set this value for a minimum of 6 hours to a maximum of 7 days using the **Absolute duration formats** as explained in the reference for [`gcloud topic datetimes`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/topic/datetimes). For example, use `2d1h` for a soak time of two days and one hour.



#### Test the new binary during a two-step upgrade

During the soak time, validate that your cluster—with the control plane running the new binary—and the workloads perform as expected. You can do one of the following steps, depending on whether you are able to verify that the workloads are compatible with the new binary:

  * **Roll back** : if you observe an issue with your workloads running on the new binary, you can roll back to the previous minor version.
  * **Complete the upgrade** : if you have verified that your workloads run without issues on the new binary, you can complete the upgrade if you want to start using the features and APIs of the new version.
  * **Wait** : you can also wait for the soak time to elapse. After, GKE performs the emulated version upgrade, where it transitions to using the features and APIs of the new minor version.



##### Observe the in-progress upgrade

To get information about an in-progress upgrade, use one of the following resources:

  * To see details about the upgrade, follow the instructions to [get upgrades information at the cluster level](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrade-assist#get-info-cluster).
  * Use cluster notifications. GKE sends an [`UpgradeEvent`](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications#upgradeevent) notification when the _binary upgrade_ starts, and an `UpgradeInfoEvent` of the type [Upgrade operation is complete](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications#upgrade-operation-complete-notification) when the _binary upgrade_ completes and the soak time starts.
  * To see details about your cluster, including about the in-progress upgrade, run the [`gcloud container clusters describe`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/describe) command.
  * See relevant logs in Cloud Logging.



##### Roll back a two-step upgrade after the binary version upgrade

During a two-step upgrade, after the binary version upgrade is the soaking period. During this period, you can roll back to the previous minor version, if necessary. You can't roll back after GKE performs the _emulated version upgrade_.

After the rollback operation completes, your control plane runs the previous minor version as it did before you initiated the two-step upgrade.

Do the following steps to roll back, if possible:

  1. Check that you can still roll the control plane back to the previous minor version by running the gcloud CLI command at [Get upgrades information at the cluster level](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrade-assist#get-info-cluster). Determine whether you can or can't roll back by the output of the command:

     * You can roll back if there is a `rollbackSafeUpgradeStatus` section in the output. In that section, save the `previousVersion` for the `VERSION` variable in the next step. Proceed to the next step.
     * You can't roll back if there is no `rollbackSafeUpgradeStatus` section. This indicates that GKE already performed the emulated version upgrade. You can't perform the next step.
  2. If the previous step determined that rollback is possible, roll back to the previous version:
         
         gcloud container clusters upgrade CLUSTER_NAME \
           --location=CONTROL_PLANE_LOCATION \
           --cluster-version VERSION
           --master
         

The `VERSION` must be the exact patch version previously used. You saved this version in the previous step.




After you run this command and downgrade to the previous version, you can determine why your workload didn't run correctly on the new binary. If needed, you can reach out to Cloud Customer Care, providing relevant logs, error messages, and details about the validation failure that you encountered. For more information, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support).

After you've resolved the issue, you can manually upgrade again to the new minor version.

##### Complete the two-step upgrade

During the soaking period, if you've verified that the workloads run successfully with the new binary, you can skip the rest of the soak time:
    
    
    gcloud beta container clusters complete-control-plane-upgrade CLUSTER_NAME  \
      --location=CONTROL_PLANE_LOCATION
    

After you run this command, you can no longer downgrade to the previous minor version.

### Downgrade the control plane to an earlier patch version

**Note:** Before attempting to downgrade a cluster, ensure that you're already familiar with the limitations.

  1. Set a [maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) before downgrading to prevent GKE from automatically upgrading the control plane after you downgrade it.
  2. Downgrade the cluster control plane to an earlier patch version:
         
         gcloud container clusters upgrade CLUSTER_NAME \
              --master \
              --location=CONTROL_PLANE_LOCATION \
              --cluster-version=VERSION
         


**Note:** If your cluster is subscribed to a release channel, the `VERSION` must be an [available patch version](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/release-channels#viewing_the_default_and_available_versions_for_release_channels) for the release channel. All Autopilot clusters are enrolled in a release channel.

### Disabling cluster auto-upgrades

Infrastructure security is high priority for GKE, and as such [control planes are upgraded](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades) on a regular basis, and can't be disabled. However, you can apply [maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions) to control when GKE upgrades control planes and nodes.

### Check recent control plane upgrade history

For a snapshot of a cluster's recent auto-upgrade history, [get information about a cluster's upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrade-assist#get-info).

Alternatively, you can list recent operations to see when the control plane was upgraded:
    
    
    gcloud container operations list --filter="TYPE:UPGRADE_MASTER AND TARGET:CLUSTER_NAME" \
        --location=CONTROL_PLANE_LOCATION
    

## Upgrade node pools

By default, Standard node pools have [auto-upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades#node_pool_upgrades) enabled, and all Autopilot-managed node pools in Standard clusters always have auto-upgrade enabled. Node auto-upgrades help ensure that your cluster's control plane and node version remain in sync and in compliance with the [Kubernetes version skew policy](https://kubernetes.io/releases/version-skew-policy/), which helps ensure that control planes are compatible with nodes up to two minor versions earlier than the control plane. For example, Kubernetes 1.34 control planes are compatible with Kubernetes 1.32 nodes. By default, GKE automatically upgrades only one node pool at a time. To automatically upgrade multiple node pools simultaneously, you can [configure concurrent node pool upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#concurrent-upgrades) ([Preview](https://cloud.google.com/products#product-launch-stages)).

**Best practice** : 

Avoid disabling [node auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#disable) with Standard node pools so that your cluster benefits from the upgrades listed in the preceding paragraph.

With GKE Standard node pool upgrades, you can choose between three configurable upgrade strategies, including [surge upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#surge), [blue-green upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#blue-green-upgrade-strategy), and [autoscaled blue-green upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#autoscaled-blue-green-upgrade-strategy) ([Preview](https://docs.cloud.google.com/products#product-launch-stages)). Autopilot-managed node pools in Standard clusters always use surge upgrades.

For Standard node pools, [choose a strategy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies) and [use the parameters to tune the strategy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pool-upgrade-strategies) to best fit your cluster environment's needs.

### How node upgrades work

While a node is being upgraded, GKE stops scheduling new Pods onto it, and attempts to schedule its running Pods onto other nodes. This is similar to other events that re-create the node, such as enabling or disabling a feature on the node pool.

During automatic or manual node upgrades, [PodDisruptionBudgets (PDBs)](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) and [Pod termination grace period](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination) are respected for a maximum of 1 hour. If Pods running on the node can't be scheduled onto new nodes after one hour, GKE initiates the upgrade anyway. This behavior applies even if you configure your PDBs to always have all of your replicas available by setting the `maxUnavailable` field to `0` or `0%` or by setting the `minAvailable` field to `100%` or to the number of replicas. In all of these scenarios, GKE deletes the Pods after one hour so that the node deletion can happen.

**Best practice** : 

If a workload running in a Standard node pool requires more flexibility with graceful termination, use [blue-green upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#blue-green-upgrade-strategy) which provide settings for additional soak time to extend PDB checks beyond the one hour default.

To learn more about what to expect during node termination in general, see the topic about [Pods](https://kubernetes.io/docs/concepts/workloads/pods/#pod-templates).

The upgrade is only complete when all nodes have been recreated and the cluster is in the new state. When a newly-upgraded node registers with the control plane, GKE marks the node as schedulable.

New node instances run the new Kubernetes version as well as the following:

  * The [node image](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images)
  * [`kubelet`](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/)
  * [`kube-proxy`](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/)



For a node pool upgrade to be considered complete, all nodes in the node pool must be recreated. If an upgrade started but then didn't complete and is in a partially upgraded state, the node pool version might not reflect the version of all of the nodes. To learn more, see [Some node versions don't match the node pool version after an incomplete node pool upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#inconsistent-node-versions). To determine that the node pool upgrade finished, [check the node pool upgrade status](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#check-status). If the upgrade operation is beyond the retention period, then check that each individual node version matches the node pool version.

### Save your data to persistent disks before upgrading

Before upgrading a node pool, you must ensure that any data you need to keep is stored in a Pod by using [persistent volumes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes), which use [persistent disks](https://docs.cloud.google.com/compute/docs/disks#pdspecs). Persistent disks are unmounted, rather than erased, during upgrades, and their data is transferred between Pods.

The following restrictions pertain to persistent disks:

  * The nodes on which Pods are running must be Compute Engine VMs.
  * Those VMs need to be in the same Compute Engine project and zone as the persistent disk.



To learn how to add a persistent disk to an existing node instance, see [Adding or resizing zonal persistent disks](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk#create_disk) in the Compute Engine documentation.

### Manually upgrade a node pool

**Important:** Because Compute Engine instances with accelerators (GPUs or TPUs) don't support live migration, Compute Engine must shut down and re-create the nodes during host maintenance. This process can disrupt workloads such as AI/ML training or inference jobs. To minimize disruption, perform both Compute Engine host maintenance and GKE node upgrades at the same time. For more information, see [Perform host maintenance for nodes running training and inference workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/perform-host-maintenance-accelerators).

You can manually upgrade the version of a Standard node pool or Autopilot-managed node pool **in a Standard cluster**. You can match the version of the control plane or, use a previous version that is still available and is compatible with the control plane. You can manually upgrade multiple node pools in parallel, similarly to how GKE can upgrade multiple node pools in parallel if you [configure concurrent node pool upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#concurrent-upgrades).

When GKE upgrades a node pool, either manually or automatically, GKE removes any [labels you added to individual nodes using `kubectl`](https://kubernetes.io/docs/tasks/configure-pod-container/assign-pods-nodes/#add-a-label-to-a-node). Any other [types of changes to a GKE cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#types-of-changes) which recreate the nodes also remove the labels. To avoid losing labels, [apply labels to node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/update-existing-nodepools#updating_node_labels) instead.

Before you manually upgrade your node pool, consider the following conditions:

  * Upgrading a node pool may disrupt workloads running in that node pool. To avoid this, you can create a new node pool with the required version and migrate the workload. After migration, you can delete the old node pool.
  * If you upgrade a node pool with an Ingress in an errored state, the instance group does not sync. To work around this issue, first check the status using the `kubectl get ing` command. If the instance group is not synced, you can work around the problem by re-applying the manifest used to create the ingress.



You can manually upgrade your node pools to a version compatible with the control plane:

  * For Standard node pools, you can use the Google Cloud console or the Google Cloud CLI.
  * For [Autopilot-managed node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools#autopilot-node-pools), you can only use the Google Cloud CLI.




### Console

To upgrade a Standard node pool using the Google Cloud console, perform the following steps:

  1. Go to the **Google Kubernetes Engine** page in Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click the name of the cluster.

  3. On the **Cluster details** page, click the **Nodes** tab.

  4. In the **Node Pools** section, click the name of the node pool that you want to upgrade.

  5. Click _edit_ **Edit**.

  6. Click **Change** under **Node version**.

  7. Select the required version from the **Node version** drop-down list, then click **Change**.




It may take several minutes for the node version to change.

### gcloud

The following variables are used in the commands in this section:

  * `CLUSTER_NAME`: the name of the cluster of the node pool to be upgraded.
  * `NODE_POOL_NAME`: the name of the node pool to be upgraded.
  * `CONTROL_PLANE_LOCATION`: the location (region or zone) for the control plane, such as `us-central1` or `us-central1-a`.
  * `VERSION`: the Kubernetes version to which the nodes are upgraded. For example, `--cluster-version=1.34.1-gke.1293000` or `cluster-version=latest`.



Upgrade a node pool:
    
    
    gcloud container clusters upgrade CLUSTER_NAME \
      --node-pool=NODE_POOL_NAME \
      --location=CONTROL_PLANE_LOCATION
    

To specify a different version of GKE on nodes, use the optional `--cluster-version` flag:
    
    
    gcloud container clusters upgrade CLUSTER_NAME \
      --node-pool=NODE_POOL_NAME \
      --location=CONTROL_PLANE_LOCATION \
      --cluster-version VERSION
    

For more information about specifying versions, see [Versioning](https://docs.cloud.google.com/kubernetes-engine/versioning).

For more information, refer to the [`gcloud container clusters upgrade`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/upgrade) documentation.

### Downgrade node pools

You can downgrade a node pool if GKE completed the node pool upgrade. GKE can't downgrade—and can only roll back—a partially upgraded node pool. If you attempt to trigger a downgrade of a partially upgraded node pool, GKE doesn't update any of the nodes in the node pool with that operation. To check if node pool isn't completely upgraded and can only be rolled back, first [check the node pool upgrade status](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#check-status). If the upgrade was cancelled or failed, you can check that the node pool upgrade never completed by checking the nodes in the node pool to see if there are still nodes running the previous version.

If a node pool upgrade didn't complete and you want to roll back upgraded nodes to their previous version, follow the instructions to [roll back a node pool upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#rollback). If a node pool upgrade is complete and you want to reverse it because it caused issues for your workloads, you can downgrade the node pool to an earlier version by following the instructions in this section. Review the [limitations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#downgrading-limitations) before downgrading a node pool.

**Best practice** : 

Use the [blue-green node upgrade strategy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#blue-green-upgrade-strategy) if you need to optimize for risk mitigation for node pool upgrades impacting your workloads. With this strategy, you can [roll back](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#rollback-a-blue-green-upgrade) an in-progress upgrade to the original nodes if the upgrade is unsuccessful.

  1. Set a [maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) for the cluster to prevent the node pool from being automatically upgraded by GKE after being downgraded.
  2. To downgrade to an earlier version, follow the steps to [manually upgrade a node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrade_nodes) and specify an earlier version.



### Change surge upgrade parameters

For more information about changing surge upgrade parameters, see [Configure surge upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pool-upgrade-strategies#surge).

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



### Check node pool upgrade status

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

### Check node pool upgrade settings

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

## Known issues

If you have `PodDisruptionBudget` objects configured that are unable to allow any additional disruptions, node upgrades might fail to upgrade to the control plane version after repeated attempts. To prevent this failure, we recommend that you scale up the `Deployment` or `HorizontalPodAutoscaler` to allow the node to drain while still respecting the `PodDisruptionBudget` configuration.

To see all `PodDisruptionBudget` objects that do not allow any disruptions:
    
    
    kubectl get poddisruptionbudget --all-namespaces -o jsonpath='{range .items[?(@.status.disruptionsAllowed==0)]}{.metadata.name}/{.metadata.namespace}{"\n"}{end}'
    

Although automatic upgrades might encounter the issue, the automatic upgrade process forces the nodes to upgrade. However, the upgrade takes an extra hour for every node in the `istio-system` namespace that violates the PodDisruptionBudget.

## Troubleshooting

For information about troubleshooting, see [Troubleshoot cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/upgrades).

## What's next

  * Learn about [node upgrade strategies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies).
  * Learn about [cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades).
  * Learn about [node auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades).
  * Read about [maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
