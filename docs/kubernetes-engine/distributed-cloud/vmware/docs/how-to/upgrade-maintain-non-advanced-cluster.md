---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-maintain-non-advanced-cluster/
title: Upgrade a version 1.32 non-advanced cluster and keep it as non-advanced \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:19:39.260296+00:00
---

# Upgrade a version 1.32 non-advanced cluster and keep it as non-advanced  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-maintain-non-advanced-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Upgrade a version 1.32 non-advanced cluster and keep it as non-advanced Stay organized with collections  Save and categorize content based on your preferences. 

By default, a non-advanced cluster will be upgraded to an advanced cluster automatically when you upgrade to version 1.33. Although we recommend that you upgrade a non-advanced cluster to an advanced cluster, if you need to upgrade from 1.32 to 1.33 and keep the cluster as non-advanced, follow the steps in this document.

Keeping a cluster as non-advanced is supported only for upgrading from version 1.32 to 1.33. When you upgrade a non-advanced cluster from version 1.33 to 1.34, the cluster is always converted to an advanced cluster.

See the following for more information:

  * For information on upgrading to version 1.32 and earlier, see [Upgrade a cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading).

  * For information on upgrading a non-advanced cluster to an advanced cluster, see [Update or upgrade a cluster to an advanced cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/update-or-upgrade-to-adv-cluster).




## Prerequisites

  * The `gkectl` version must be the same as the target cluster version.

    * If needed, see [Download `gkectl`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads#download_gkectl) to get a supported version of `gkectl`.
  * Always [diagnose](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose) your cluster before updating or upgrading.

  * Make sure your clusters use only [recommended features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/migrate-recommended-features).

  * You must upgrade the admin cluster before you upgrade any user clusters.




## Upgrade the admin cluster

  1. [Upgrade your admin workstation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#upgrade_awstation) if needed.

  2. Import OS images to vSphere:
         
         gkectl prepare \
             --bundle-path BUNDLE_PATH \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --advanced-cluster=false
         

Replace the following:

     * `BUNDLE_PATH`: the path of the bundle file. This file is on your admin workstation in `/var/lib/gke/bundles/`. For example:
           
           /var/lib/gke/bundles/gke-onprem-vsphere-1.33.0-gke.799-full.tgz
           

     * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file.

  3. Set `enableAdvancedCluster` in your [admin cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#enable-advanced-cluster-field) to `false`.

  4. Make sure the `bundlepath` field in the [admin cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#bundlepath-field) matches the path of the bundle to which you want to upgrade.

  5. Upgrade the admin cluster and keep it as a non-advanced cluster:
         
         gkectl upgrade admin \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --config ADMIN_CLUSTER_CONFIG
         

Replace the following:

     * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file.
     * `ADMIN_CLUSTER_CONFIG`: the path of the admin cluster configuration file.

The command will rollout recreate all the nodes in the admin cluster. With the rollout recreate deployment strategy, the nodes are upgraded one at a time. During the node upgrade, the VM is deleted and then recreated with the new version.




## Upgrade the user cluster

**Important:** Make sure the admin cluster has already been upgraded.

  1. Import OS images to vSphere:
         
         gkectl prepare \
             --bundle-path BUNDLE_PATH \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --advanced-cluster=false
         

Replace the following:

     * `BUNDLE_PATH`: the path of the bundle file. This file is on your admin workstation in `/var/lib/gke/bundles/`. For example:
           
           /var/lib/gke/bundles/gke-onprem-vsphere-1.33.0-gke.799-full.tgz
           

     * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file.

  2. Set `enableAdvancedCluster` in your [user cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enable-advanced-cluster-field) to `false`.

  3. Make sure the `gkeOnPremVersion` field in the [user cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#gkeonpremversion-field) matches the target version of your upgrade.

  4. Upgrade the user cluster and keep it as a non-advanced cluster:
         
         gkectl upgrade cluster \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --config USER_CLUSTER_CONFIG
         

Replace the following:

     * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file.
     * `USER_CLUSTER_CONFIG`: the path of the user cluster configuration file.

The command will recreate all the nodes in the user cluster.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
