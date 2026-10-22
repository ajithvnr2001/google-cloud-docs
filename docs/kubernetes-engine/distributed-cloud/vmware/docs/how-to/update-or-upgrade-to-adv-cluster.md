---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/update-or-upgrade-to-adv-cluster/
title: Update or upgrade a cluster to an advanced cluster \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:08.626277+00:00
---

# Update or upgrade a cluster to an advanced cluster  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/update-or-upgrade-to-adv-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Update or upgrade a cluster to an advanced cluster Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to update or upgrade a cluster to an [advanced cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/advanced-clusters) from version 1.32.

**Important:** Non-advanced clusters will be upgraded to advanced cluster automatically in 1.33.

## Prerequisites

  * The `gkectl` version must be the same as the target cluster version.

    * If needed, see [Download `gkectl`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads#download_gkectl) to get a supported version of `gkectl`.
  * Always [diagnose](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose) your cluster before updating or upgrading to an advanced cluster:

    * Run `gkectl diagnose cluster` on your admin and user clusters to ensure that they are healthy.
    * If the command reports any errors or warnings, resolve them before you start the update or upgrade to an advanced cluster.
  * Make sure your clusters use only [recommended features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/migrate-recommended-features).

  * Verify your clusters don't use any [features not supported by advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/advanced-clusters#adv-clusters-feature-support) before starting the update or upgrade. If any unsupported features are active, disable them using [update](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/updating-general) first.

    * Although highly-available (HA) user clusters are required on advanced clusters, you can still update or upgrade a non-HA user cluster to an HA advanced cluster following this guide.
  * You must update or upgrade the admin cluster to an advanced cluster before you update or upgrade any user clusters.

  * About `cert-manager` installation: `cert-manager` is automatically installed on advanced clusters. When you migrate from a non-advanced cluster to an advanced cluster, the integrated `cert-manager` automatically overrides any customer-installed versions of `cert-manager`. Make sure you don't have critical custom configurations or features applied to your existing `cert-manager` before you update or upgrade to advanced clusters. For more information, see [Upgrade to `cert-manager` bundled with advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/update-or-upgrade-to-adv-cluster#upgrade-cert-manager).



## Update or upgrade the admin cluster to advanced cluster

**Caution:** If an update or upgrade to admin clusters fails, make sure you don't delete the external bootstrap cluster from the workstation. The bootstrap cluster contains all states required to resume the update or upgrade. If you need to rerun `gkectl update admin` or `gkectl upgrade admin` after a failure, you must add the `--reuse-bootstrap-cluster` (or `-r`) flag. Failure to use this flag can cause a severe issue where critical data is lost.

### Update

**Important:** Make sure your cluster version is at least 1.32.0.

  1. Diagnose your cluster to make sure it is healthy:
         
         gkectl diagnose cluster \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         

     * If the command reports any errors or warnings, refer to [Diagnose cluster issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose#diagnose_admin_cluster) and resolve them before proceeding.
  2. Prepare for the advanced cluster:
         
         gkectl prepare \
             --bundle-path BUNDLE_PATH \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --advanced-cluster
         

Replace the following:

     * `BUNDLE_PATH`: the path of the bundle file. This file is on your admin workstation in `/var/lib/gke/bundles/`. For example:
           
           /var/lib/gke/bundles/gke-onprem-vsphere-1.32.0-gke.1085-full.tgz
           

     * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file.

  3. Set `enableAdvancedCluster` in your [admin cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#enable-advanced-cluster-field) to `true`.

  4. Update the admin cluster to the advanced cluster:
         
         gkectl update admin \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --config ADMIN_CLUSTER_CONFIG
         

Replace the following:

     * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file.
     * `ADMIN_CLUSTER_CONFIG`: the path of the admin cluster configuration file.

The command will recreate all the nodes in the admin cluster.




### Upgrade

**Caution:** If your cluster is using `cos` or `cos_cgv2` as the [control plane OS image type](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#os-image-type-field) or [node pool OS image type](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#nodepool-osimagetype-field), make sure your cluster version is at least `1.32.0` before upgrading. Otherwise, make sure your cluster version is at least `1.31.100`.

  1. [Upgrade your admin workstation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#upgrade_awstation) if needed.

  2. Diagnose your cluster to make sure it is healthy:
         
         gkectl diagnose cluster \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         

     * If the command reports any errors or warnings, refer to [Diagnose cluster issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose#diagnose_admin_cluster) and resolve them before proceeding.
  3. Prepare for the advanced cluster:
         
         gkectl prepare \
             --bundle-path BUNDLE_PATH \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --advanced-cluster
         

Replace the following:

     * `BUNDLE_PATH`: the path of the bundle file. This file is on your admin workstation in `/var/lib/gke/bundles/`. For example:
           
           /var/lib/gke/bundles/gke-onprem-vsphere-1.32.0-gke.1085-full.tgz
           

     * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file.

  4. Set `enableAdvancedCluster` in your [admin cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#enable-advanced-cluster-field) to `true`.

  5. Make sure the `bundlepath` field in the [admin cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#bundlepath-field) matches the path of the bundle to which you want to upgrade.

  6. Upgrade the admin cluster to the advanced cluster:
         
         gkectl upgrade admin \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --config ADMIN_CLUSTER_CONFIG
         

Replace the following:

     * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file.
     * `ADMIN_CLUSTER_CONFIG`: the path of the admin cluster configuration file.

The command will rollout recreate all the nodes in the admin cluster. With the rollout recreate deployment strategy, the nodes are upgraded one at a time. During the node upgrade, the VM is deleted and then recreated with the new version.




After the admin cluster has been updated or upgraded to an advanced cluster:

  * Your existing non-advanced user clusters continue to function normally.

  * You can create only advanced user clusters that are managed by the advanced admin cluster.




We recommend that you upgrade all user clusters to advanced clusters soon afterward to maintain a consistent and fully-featured environment.

## Update or upgrade the user cluster to advanced cluster

**Important:** Make sure the admin cluster has already been updated or upgraded to the advanced cluster.

### Update

**Important:** Make sure your cluster version is at least 1.32.0.

  1. Diagnose your cluster to make sure it is healthy:
         
         gkectl diagnose cluster \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --cluster-name USER_CLUSTER_NAME
         

     * If the command reports any errors or warnings, refer to [Diagnose cluster issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose#diagnose_user_cluster) and resolve them before proceeding.
  2. If your user cluster control plane is not highly available (HA):

**Caution:** Due to a [known issue with the `masterNode.replicas` field](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/known-issues#nonha-to-ha-adv-update-fail), to update a version 1.32 or version 1.33 non-HA user cluster to an HA advanced cluster, your cluster must be at a version higher than 1.32.600 or higher than 1.33.100 respectively.
     1. Change [`masterNode.replicas`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#masternode-replicas-field) from 1 to 3.

     2. Add the static IP addresses for the user cluster control-plane nodes to the [`network.controlPlaneIPBlock.ips`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-controlplaneipblock-ips-section) section.

  3. Prepare for the advanced cluster:
         
         gkectl prepare \
             --bundle-path BUNDLE_PATH \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --advanced-cluster
         

Replace the following:

     * `BUNDLE_PATH`: the path of the bundle file. This file is on your admin workstation in `/var/lib/gke/bundles/`. For example:
           
           /var/lib/gke/bundles/gke-onprem-vsphere-1.32.0-gke.1085-full.tgz
           

     * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file.

  4. Set `enableAdvancedCluster` in your [user cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enable-advanced-cluster-field) to `true`.

  5. Update the user cluster to the advanced cluster:
         
         gkectl update cluster \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --config USER_CLUSTER_CONFIG
         

Replace the following:

     * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file.
     * `USER_CLUSTER_CONFIG`: the path of the user cluster configuration file.

The command will rollout recreate all the nodes in the user cluster. With the rollout recreate deployment strategy, the nodes are updated one at a time. During the node update, the VM is deleted and then recreated with the new configuration.




### Upgrade

**Caution:** If your cluster is using `cos` or `cos_cgv2` as the [control plane OS image type](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#os-image-type-field) or [node pool OS image type](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#nodepool-osimagetype-field), make sure your cluster version is at least `1.32.0` before upgrading. Otherwise, make sure your cluster version is at least `1.31.100`.

  1. Diagnose your cluster to make sure it is healthy:
         
         gkectl diagnose cluster \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --cluster-name USER_CLUSTER_NAME
         

     * If the command reports any errors or warnings, refer to [Diagnose cluster issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose#diagnose_user_cluster) and resolve them before proceeding.
  2. If your user cluster control plane is not highly available (HA):

     1. Change [`masterNode.replicas`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#masternode-replicas-field) from 1 to 3.

     2. Add the static IP addresses for the user cluster control-plane nodes to the [`network.controlPlaneIPBlock.ips`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-controlplaneipblock-ips-section) section.

  3. Prepare for the advanced cluster:
         
         gkectl prepare \
             --bundle-path BUNDLE_PATH \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --advanced-cluster
         

Replace the following:

     * `BUNDLE_PATH`: the path of the bundle file. This file is on your admin workstation in `/var/lib/gke/bundles/`. For example:
           
           /var/lib/gke/bundles/gke-onprem-vsphere-1.32.0-gke.1085-full.tgz
           

     * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file.

  4. Set `enableAdvancedCluster` in your [user cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enable-advanced-cluster-field) to `true`.

  5. Make sure the `gkeOnPremVersion` field in the [user cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#gkeonpremversion-field) matches the target version of your upgrade.

  6. Upgrade the user cluster to the advanced cluster:
         
         gkectl upgrade cluster \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --config USER_CLUSTER_CONFIG
         

Replace the following:

     * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file.
     * `USER_CLUSTER_CONFIG`: the path of the user cluster configuration file.

The command will recreate all the nodes in the user cluster.




## `cert-manager` bundled with advanced clusters

`cert-manager` is a mandatory, system-managed component in [advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/advanced-clusters).

If you use `cert-manager` without advanced clusters, check the following before you upgrade to advanced clusters:

  * There are no custom configurations or feature flags in your `cert-manager`.
  * Your `cert-manager` version is the same version or one version behind the bundled version.



### Apigee Hybrid compatibility

The bundled `cert-manager` is fully compatible with **Apigee Hybrid** workloads. When you upgrade to an advanced cluster, the installer might warn you that the existing `cert-manager` installation will be replaced. This is expected behavior that the system handles automatically.

To ensure a smooth transition for your Apigee workloads:

  * **Do not uninstall** your existing `cert-manager` manually before the upgrade.
  * **Revert customizations** : If you manage `cert-manager` using GitOps or have applied custom configurations to the `cert-manager` deployment, you must revert these customizations or suspend sync before the upgrade to avoid configuration drift and potential upgrade pauses.



### Capabilities and limitations

You can do the following with the bundled `cert-manager`:

  * Create and edit `Issuer` and `ClusterIssuer` resources.
  * Create and edit certificate resources that reference issuers and standard issuer types.
  * Create and edit standard Kubernetes resources that `cert-manager` uses.
  * Create Kubernetes Secrets containing API keys and reference them in your issuers.
  * Configure your issuers to use specific HTTP-01 or DNS-01 solvers.



You cannot customize the following in the bundled `cert-manager`:

  * Set the `deployment` or `helm` values.
  * Add command line arguments or flags to the `cert-manager` binary.
  * Change resource limits or node selectors for `cert-manager` pods.
  * Modify the installation logic of the `cert-manager` software.
  * Turn on experimental features.
  * Force `cert-manager` control plane pods to run on specific infrastructure nodes.



If you have specific constraints that prevent you from using the bundled `cert-manager`, contact [Google Cloud support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support) for assistance with advanced configuration options.

### Bundled versions

The following table lists the bundled `cert-manager` versions for each version of Google Distributed Cloud (software only) for VMware.

Google Distributed Cloud (software only) for VMware | Bundled `cert-manager` version  
---|---  
1.32 | 1.17  
1.33 | 1.18  
1.34 | 1.19  
  
## Key differences after moving to advanced clusters

Upgrading or updating your cluster to an advanced cluster introduces several key differences compared to standard clusters. Here are the major changes in advanced clusters:

  * **Resource location** : Cluster and machine resources are no longer located in user clusters. These resources are located exclusively within the admin cluster.

  * **`NodeExternalIP`** : The `NodeExternalIP` isn't set on the nodes.

  * **`cert-manager` installation**: `cert-manager` is automatically installed on advanced clusters. If you installed `cert-manager` in your cluster, updating or upgrading to advanced cluster overwrites it with the advanced cluster version.




For a comprehensive overview of feature differences, refer to the [feature comparison table](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/advanced-clusters#adv-clusters-feature-support).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
