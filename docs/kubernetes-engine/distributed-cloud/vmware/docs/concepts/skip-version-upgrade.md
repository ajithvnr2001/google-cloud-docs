---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/skip-version-upgrade/
title: Skip a version when upgrading node pools \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:21:31.278268+00:00
---

# Skip a version when upgrading node pools  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/skip-version-upgrade/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Skip a version when upgrading node pools Stay organized with collections  Save and categorize content based on your preferences. 

In version 1.29 and higher, Google Distributed Cloud allows a user cluster's control plane to be up to two minor versions higher than the node pools in the cluster. For example, if a user cluster's control plane is at 1.29, the node pools in the cluster can be at version 1.16, 1.28, or 1.29. Additionally, Google Distributed Cloud lets you skip one minor version when upgrading node pools. Using the previous example, you can upgrade node pools that are at version 1.16 directly to version 1.29 and skip the upgrade to 1.28. Skipping a minor version when upgrading node pools is referred to as a _skip-version upgrade_.

This page explains some of the benefits of a skip-version upgrade and provides steps on how to perform a skip-version upgrade by making configuration file changes and running `gkectl upgrade cluster`.

This page is for IT administrators and Operators who manage the lifecycle of the underlying tech infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks). This page assumes that you are somewhat familiar with planning and executing Google Distributed Cloud upgrades as described in the following:

  * [Upgrade overview](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-overview)

  * [Upgrade best practices](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-best-practices)

  * [Upgrade a cluster or a node pool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading)




## Limitations

Skip-version upgrades has the following limitations:

  * Skip-version upgrades are supported for Ubuntu and COS node pools, but not for Windows node pools.

  * Version 1.31: this feature isn't available on [advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enable-advanced-cluster-field).

  * Version 1.32 and higher: this feature is available on advanced clusters.

  * Load balancer node pools (node pools with `enableLoadBalancer: true`) don't support skip-version upgrades or version skew. The version of a load balancer node pool must match the cluster version.

  * Because of [Kubernetes constraints](https://kubernetes.io/releases/version-skew-policy/), a user cluster's control plane must be upgraded one minor version at a time. Note, however, that upgrading only the control plane takes significantly less time and is less risky than upgrading node pools where your workloads run.




## Benefits of skip-version upgrades

This section describes some benefits of using skip-version upgrades.

### Easier to keep your clusters in a supported version

A new Google Distributed Cloud minor version is released every four months, and each minor version has a one-year support window. For your clusters to stay within the supported window, you must perform a minor version upgrade approximately every four months, as shown in the following:

Dec | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | Jan | Feb | Mar  
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---  
1.14 |  |  |  |  |  |  |  |  |  |  | Upgrade |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   
|  |  |  | 1.15 |  |  |  |  |  |  |  |  |  |  | Upgrade |  |  |  |  |  |  |  |  |  |  |  |   
|  |  |  |  |  |  |  | 1.16 |  |  |  |  |  |  |  |  |  |  | Upgrade |  |  |  |  |  |  |  |   
|  |  |  |  |  |  |  |  |  |  |  | 1.28 |  |  |  |  |  |  |  |  |  | Upgrade |  |  |  |  |   
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 1.29 |  |  |  |  |  |  |  |  |  | Upgrade |   
  
This requirement imposes challenges when you need a long validation window to verify a new minor version and a short maintenance window to upgrade your clusters to the new minor version. To overcome these challenges, you can use a skip-version upgrade, which allows your clusters to stay within the supported window by upgrading a cluster every eight months instead of every four months. The following table shows how skipping the upgrade for version 1.15 means you only upgrade after eight months instead of four.

Dec | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | Jan | Feb | Mar  
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---  
1.14 |  |  |  |  |  |  |  |  |  |  | Upgrade |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   
|  |  |  | 1.15 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   
|  |  |  |  |  |  |  | 1.16 |  |  |  |  |  |  |  |  |  |  | Upgrade |  |  |  |  |  |  |  |   
|  |  |  |  |  |  |  |  |  |  |  | 1.28 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 1.29 |  |  |  |  |  |  |  |  |  |  |   
  
Skipping over one minor version when upgrading your node pools reduces the number of upgrades required to stay on a supported version. Additionally, you don't need to qualify the skipped minor version because it is only used by the control plane temporarily.

### Shorter maintenance window

With a skip-version upgrade, you don't need to enlarge your maintenance window. Skipping a minor version when upgrading node pools takes the same amount of time as upgrading the node pools to the next minor version because each node in a node pool is drained and recreated once. Therefore, a skip-version upgrade saves time overall and reduces workload disruption.

### Summary

In summary, a skip-version upgrade provides the following benefits:

  * Get clusters to a supported version: Google Distributed Cloud supports the three most recent minor versions. If your clusters are on an unsupported version, depending on the cluster version, skipping a minor version when upgrading node pools could get your clusters to a supported version with fewer upgrades.

  * Save time: Skipping a minor version when upgrading node pools takes the same amount of time as upgrading the node pools to the next minor version. Therefore, a skip-version upgrade takes approximately half the time of upgrading node pools twice. Similarly, with a skip-version upgrade, you have just one validation window, compared to two with regular upgrades.

  * Reduce disruptions: Longer spans between upgrades and less time spent upgrading and validating means that your workloads run longer with fewer disruptions.




## Controlling the control plane and node pool versions during an upgrade

**Caution:** Version skew between the control plane and the node pool is **NOT** supported when [upgrading non-advanced clusters to advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/update-or-upgrade-to-adv-cluster). Clusters will be automatically upgraded to advanced clusters in 1.33.

In the user cluster configuration file, the field [nodePools[i].gkeOnPremVersion](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#nodepool-gkeonpremversion-field) allows a specific node pool to use a different version than the top level [gkeOnPremVersion](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#gkeonpremversion-field) field. By changing the value of the `nodePools[i].gkeOnPremVersion` field, you control when a node pool is upgraded when you run `gkectl upgrade cluster`. If you don't include `nodePools[i].gkeOnPremVersion` in the configuration file, or if you set the field to an empty string, node pools are upgraded to the same target version that you specify in `gkeOnPremVersion`.

## Version rules

The rules for upgrades depends on the cluster minor version.

  * For versions 1.30 and lower, the user cluster minor version must be greater than or equal to the admin cluster minor version. The patch version doesn't matter. For example, if a user cluster is at version 1.30.1, the admin cluster can be upgraded to a higher patch version, such as 1.30.3.

  * For versions 1.31 and higher, the admin cluster version, including the patch version, must be greater than or equal to the user cluster version. For example, if an admin cluster is at version 1.31.1, the highest version that the user cluster can be upgraded to is 1.31.1.




When you want to upgrade your clusters to version 1.31, you must first bring all your clusters to version 1.30. After all the clusters are at version 1.30, you upgrade the admin cluster to version 1.31. After that, you can upgrade the user clusters to the same 1.31 patch version as the admin cluster.

## Skip-version upgrade sequence

The sequence in which you upgrade admin and user clusters depends on the cluster version that you are upgrading to, referred to as the _target version_ :

### 1.32 and higher

Use this sequence if the target version is 1.32 or higher. Suppose your user cluster control plane and all node pools are at minor version `1.N`. At a high level, upgrading your cluster from `1.N` to `1.N+2` using a skip-version upgrade works as follows:

  1. Upgrade the admin cluster from version `1.N` to an intermediate version, `1.N+1`.
  2. Upgrade the admin cluster from the intermediate version, `1.N+1` to the target version `1.N+2`. 
  3. Upgrade only the user cluster control plane from the source version, `1.N`, to an intermediate version, `1.N+1`. Leave the node pools at the source version. The intermediate version is needed because the control plane must be upgraded one minor version at a time. 
  4. Upgrade the control plane and the node pools to the target version, `1.N+2`. 



### 1.31

Use this special sequence if the user cluster is at version 1.29, which means the target version is 1.31. When a user cluster is at version 1.29, an admin cluster that manages the user cluster could be at version 1.27, 1.28, or 1.29. 

  1. If your admin cluster is at version 1.27, upgrade it to 1.28.
  2. If your admin cluster is at version 1.28, upgrade it to 1.29.
  3. Upgrade only the user cluster control plane from the source version, 1.29, to an intermediate version, 1.30. Leave the node pools at the source version. The intermediate 1.30 version is needed because the control plane must be upgraded one minor version at a time.
  4. Upgrade the admin cluster from version 1.29 to the intermediate version, 1.30.
  5. Upgrade the admin cluster to the target version, 1.31.
  6. Upgrade the user cluster control plane and the node pools to the target version, 1.31.



### 1.30 and lower

Use this sequence if the target version is 1.30 or lower.

Suppose your user cluster control plane and all node pools are at minor version `1.N`. At a high level, upgrading your cluster from `1.N` to `1.N+2` using a skip-version upgrade works as follows:

  1. Upgrade only the control plane from the source version, `1.N`, to an intermediate version `1.N+1`. Leave the node pools at the source version. The intermediate version is needed because the control plane must be upgraded one minor version at a time. 
  2. Upgrade the control plane and the node pools to the target version `1.N+2`. 



## Perform a skip-version upgrade

This section provides the steps for performing a skip-version upgrade.

### Before you begin

  1. Make sure the current version (the source version) of the cluster is at version 1.16 or higher. Be sure to check the version of the control plane (`gkeOnPremVersion`) and all node pools (`nodePools[i].gkeOnPremVersion`).

  2. In version 1.29 and later, server-side preflight checks are enabled by default. Make sure to [review your firewall rules](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#google_api_and_iam_requirements) to make any needed changes.

  3. To upgrade to version 1.28 and later, you must enable `kubernetesmetadata.googleapis.com` and grant the `kubernetesmetadata.publisher` IAM role to the [logging-monitoring service account](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#logging_monitoring_service_account). For details, see [Google API and IAM requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#google_api_and_iam_requirements).




### Perform the upgrade

### 1.31

Use this special sequence if the user cluster is at version 1.29, which means the target version is 1.31. This sequence is needed because the version rules changed in version 1.31.

When a user cluster is at version 1.29, an admin cluster that manages the user cluster could be at version 1.27, 1.28, or 1.29.

  1. If your admin cluster is at version 1.27, follow the steps to [upgrade your admin workstation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#upgrade_awstation) and [upgrade your admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#upgrade_admin_cluster) to version 1.28.

  2. If your admin cluster is at version 1.28, follow the steps to [upgrade your admin workstation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#upgrade_awstation) and [upgrade your admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#upgrade_admin_cluster) to version 1.29.

  3. To save space on your admin workstation, remove the downloaded bundle(s):
         
         rm /var/lib/gke/bundles/gke-onprem-vsphere-*.tgz
         




When the admin cluster and all user clusters are at version 1.29, you can start the skip version upgrade.

  1. Define the source version (1.29), an intermediate version (1.30), and the target version (1.31) in the following placeholder variables. All versions must be the full version number in the form `x.y.z-gke.N` such as `1.29.700-gke.110`.

Version |   
---|---  
Get the current user cluster's 1.29 version. This is the source version. | `SOURCE_VERSION`  
Pick an [intermediate 1.30 version](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/version-history). | `INTERMEDIATE_VERSION`  
Pick the 1.31 target version. Select the [ recommended patch](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/version-and-upgrade-support#google_cloud_distributed) from the 1.31 minor version. | `TARGET_VERSION`  
  2. [Upgrade your admin workstation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#upgrade_awstation) to the intermediate 1.30 version, `INTERMEDIATE_VERSION`. Wait for a message indicating the upgrade was successful.

  3. Install the corresponding bundle:
         
         gkectl prepare \
             --bundle-path /var/lib/gke/bundles/gke-onprem-vsphere-INTERMEDIATE_VERSION.tgz \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         

  4. [Upgrade your admin workstation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#upgrade_awstation) again, but this time to the target 1.31 version, `TARGET_VERSION`. Wait for a message indicating the upgrade was successful.

  5. Install the corresponding bundle:
         
         gkectl prepare \
             --bundle-path /var/lib/gke/bundles/gke-onprem-vsphere-TARGET_VERSION.tgz \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         

  6. Upgrade only the user cluster control plane to the intermediate version as follows:

     1. Make the following changes in the user cluster configuration file:

        * Set the `gkeOnPremVersion` field to the intermediate version, `INTERMEDIATE_VERSION`.

        * Set all the node pool versions in `nodePools[i].gkeOnPremVersion` to the source version, `SOURCE_VERSION`.

After updating your configuration file, it should look similar to the following:
    
    gkeOnPremVersion: INTERMEDIATE_VERSION
    ...
    nodePools:
    - name: pool-1
      gkeOnPremVersion: SOURCE_VERSION
      ...
    - name: pool-2
      gkeOnPremVersion: SOURCE_VERSION
      ...
    

     2. Upgrade the control plane:
            
            gkectl upgrade cluster \
                --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
                --config USER_CLUSTER_CONFIG_FILE
            

Replace `USER_CLUSTER_CONFIG` with the path of your user cluster configuration file.

  7. Set the `bundlePath` field in the admin cluster configuration file to the intermediate 1.30 version of the bundle:
         
         bundlePath="/var/lib/gke/bundles/gke-onprem-vsphere-INTERMEDIATE_VERSION.tgz"
         

  8. Upgrade the admin cluster to the intermediate 1.30 version:
         
         gkectl upgrade admin \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --config ADMIN_CLUSTER_CONFIG_FILE
         

  9. Set the `bundlePath` field in the admin cluster configuration file to the target 1.31 version of the bundle:
         
         bundlePath="/var/lib/gke/bundles/gke-onprem-vsphere-TARGET_VERSION.tgz"

  10. Upgrade the admin cluster to the target 1.31 version:
         
         gkectl upgrade admin \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --config ADMIN_CLUSTER_CONFIG_FILE
         

  11. Upgrade the control plane and the node pools to the target version as follows:

     1. Make the following changes in the user cluster configuration file:

        * Set the `gkeOnPremVersion` field to the target version, `TARGET_VERSION`.

        * Set all `nodePools[i].gkeOnPremVersion` to an empty string.

After updating your configuration file, it should look similar to the following:
    
    gkeOnPremVersion: TARGET_VERSION
    ...
    nodePools:
    - name: pool-1
      gkeOnPremVersion: ""
      ...
    - name: pool-2
      gkeOnPremVersion: ""
      ...
    

     2. Upgrade the control plane and the node pools:
            
            gkectl upgrade cluster \
                --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
                --config USER_CLUSTER_CONFIG_FILE
            




### 1.30 and lower

Use this sequence if the target version is 1.30 or lower.

  1. Define the source version (`1.N`), the intermediate version (`1.N+1`), and the target version (`1.N+2`) in the following placeholder variables. All versions must be the full version number in the form `x.y.z-gke.N` such as `1.16.11-gke.25`.

Version |   
---|---  
Get the current cluster version. This is the source version (`1.N`). | `SOURCE_VERSION`  
Pick an [intermediate version](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/version-history) (`1.N+1`). | `INTERMEDIATE_VERSION`  
Pick the target version (`1.N+2`). Select the [ recommended patch](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/version-and-upgrade-support#google_cloud_distributed) from the target minor version. | `TARGET_VERSION`  
  2. [Upgrade your admin workstation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#upgrade_awstation) to the intermediate version, `INTERMEDIATE_VERSION`. Wait for a message indicating the upgrade was successful.

  3. Install the corresponding bundle:
         
         gkectl prepare \
             --bundle-path /var/lib/gke/bundles/gke-onprem-vsphere-INTERMEDIATE_VERSION.tgz \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         

Replace `ADMIN_CLUSTER_KUBECONFIG` with the path of your admin cluster `kubeconfig` file.

  4. [Upgrade your admin workstation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#upgrade_awstation) again, but this time to the target version, `TARGET_VERSION`. Wait for a message indicating the upgrade was successful.

  5. Install the corresponding bundle:
         
         gkectl prepare \
             --bundle-path /var/lib/gke/bundles/gke-onprem-vsphere-TARGET_VERSION.tgz \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         

  6. Upgrade only the control plane to the intermediate version as follows:

     1. Make the following changes in the user cluster configuration file:

        * Set the `gkeOnPremVersion` field to the intermediate version, `INTERMEDIATE_VERSION`.

        * Set all the node pool versions in `nodePools[i].gkeOnPremVersion` to the source version, `SOURCE_VERSION`.

After updating your configuration file, it should look similar to the following:
    
    gkeOnPremVersion: INTERMEDIATE_VERSION
    ...
    nodePools:
    - name: pool-1
      gkeOnPremVersion: SOURCE_VERSION
      ...
    - name: pool-2
      gkeOnPremVersion: SOURCE_VERSION
      ...
    

     2. Upgrade the control plane:
            
            gkectl upgrade cluster \
                --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
                --config USER_CLUSTER_CONFIG_FILE
            

Replace `USER_CLUSTER_CONFIG` with the path of your user cluster configuration file.

  7. Upgrade the control plane and the node pools to the target version as follows:

     1. Make the following changes in the user cluster configuration file:

        * Set the `gkeOnPremVersion` field to the target version, `TARGET_VERSION`.

        * Set all `nodePools[i].gkeOnPremVersion` to an empty string.

After updating your configuration file, it should look similar to the following:
    
    gkeOnPremVersion: TARGET_VERSION
    ...
    nodePools:
    - name: pool-1
      gkeOnPremVersion: ""
      ...
    - name: pool-2
      gkeOnPremVersion: ""
      ...
    

     2. Upgrade the control plane and the node pools:
            
            gkectl upgrade cluster \
                --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
                --config USER_CLUSTER_CONFIG_FILE
            




If you don't have any other user clusters to upgrade, remove the bundles from your admin workstation to save space:
    
    
    rm /var/lib/gke/bundles/gke-onprem-vsphere-*.tgz
    

## What's next

  * [Creating and managing node pools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/managing-node-pools)
  * [Configure node pool update policy](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-pool-update-policy)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
