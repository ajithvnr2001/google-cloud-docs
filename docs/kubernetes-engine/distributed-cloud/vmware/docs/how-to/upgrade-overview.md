---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-overview/
title: Upgrade overview \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:22.235717+00:00
---

# Upgrade overview  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Upgrade overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of the upgrade process and version skew information for Google Distributed Cloud (software only) for VMware clusters. This information should help you plan the order in which you upgrade clusters in a multi-cluster environment. For more detailed planning information, including a checklist to help you plan the upgrade, see [Upgrade best practices](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-best-practices).

This page is for IT administrators and Operators who manage the lifecycle of the underlying tech infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

**Important:** Always [diagnose](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose) your cluster before upgrading to an [advanced cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/advanced-clusters). We strongly recommend running `gkectl diagnose cluster` on your admin and user clusters to ensure they are healthy, and resolving any issues before starting the upgrade.

## Advanced clusters differences

When [advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enable-advanced-cluster-field) are enabled, there are some differences with upgrades, particularly in the preview of advanced clusters in version 1.31. To see the upgrade differences, search this document for the word `advanced`. For a table of all differences, see [Differences when running advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-best-practices#differences_when_running_advanced_clusters).

## Automatic upgrade to advanced clusters

Note the following differences between versions:

  * When you upgrade your clusters from version 1.32 to 1.33, they are automatically converted to [advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/advanced-clusters), which uses improved architectures that provide greater flexibility and scalability. When upgrading to version 1.33, you have the option to have the cluster remain non-advanced. For details, see [Upgrade a version 1.32 non-advanced cluster and keep it as non-advanced](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-maintain-non-advanced-cluster).

  * `cert-manager` is automatically installed on advanced clusters. When you migrate from a non-advanced cluster to an advanced cluster, the `cert-manager` integrated with advanced clusters automatically overrides any existing versions of `cert-manager`. Make sure you don't have critical custom configurations or features in your existing `cert-manager` before you update or upgrade to advanced clusters. For more information, see [Upgrade to `cert-manager` bundled with advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/update-or-upgrade-to-adv-cluster#upgrade-cert-manager).

The following table lists the bundled `cert-manager` versions for each version of Google Distributed Cloud (software only) for VMware.

Google Distributed Cloud (software only) for VMware | Bundled `cert-manager` version  
---|---  
1.32 | 1.17  
1.33 | 1.18  
1.34 | 1.19  
  * Keeping a cluster as non-advanced is supported only for upgrades from version 1.32 to 1.33. When you upgrade a non-advanced cluster from version 1.33 to 1.34, the cluster is always converted to an advanced cluster.

  * You must use the `gkectl` command line tool to upgrade non-advanced clusters to version 1.33. The GKE On-Prem API clients, Terraform, the Google Cloud console, and the gcloud CLI aren't supported.

  * Validate `gkectl` version: The `gkectl` version **must** be the same as the Google Distributed Cloud software only for VMware version to which you want to upgrade. For example, if you are upgrading a 1.32 non-advanced cluster to 1.33.700-gke.71 advanced cluster, the `gkectl` version must be 1.33.700-gke.71. This strict version requirement only applies during the upgrade to an advanced cluster. For all other upgrades on your advanced cluster, [the standard version skew rules](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-overview#version_skew) are in effect.

  * Version skew not allowed: When upgrading from a non-advanced to an advanced cluster, you cannot upgrade the control plane and node pools separately. You must upgrade the control plane and all node pools to the Google Distributed Cloud software only for VMware target version at the same time. For example, if you are upgrading from a non-advanced cluster to a 1.33.700-gke.71 advanced cluster, you must upgrade the control plane and node pool versions to 1.33.700-gke.71 at the same time.


**Caution:** A [ known issue](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/known-issues#rerunning-gkectl-upgrade-admin-deletes-the-bootstrap-cluster-upgrade-to-the-advanced-clusters) where an operation fails during upgrade from a non-advanced cluster to an advanced cluster, and you rerun the `gkectl upgrade admin ` command might cause upgrades to advanced clusters to become stuck. To avoid this issue and ensure a successful upgrade, upgrade to one of the following versions: 

  * **1.32.1000-gke.57+**
  * **1.33.700-gke.71+**
  * **1.34.300-gke.59+**



## Version rules

The rules for upgrades depends on the cluster minor version.

  * For versions 1.30 and lower, the user cluster minor version must be greater than or equal to the admin cluster minor version. The patch version doesn't matter. For example, if a user cluster is at version 1.30.1, the admin cluster can be upgraded to a higher patch version, such as 1.30.3.

  * For versions 1.31 and higher, the admin cluster version, including the patch version, must be greater than or equal to the user cluster version. For example, if an admin cluster is at version 1.31.1, the highest version that the user cluster can be upgraded to is 1.31.1.




When you want to upgrade your clusters to version 1.31, you must first bring all your clusters to version 1.30. After all the clusters are at version 1.30, you upgrade the admin cluster to version 1.31. After that, you can upgrade the user clusters to the same 1.31 patch version as the admin cluster.

### Version rules for `gkectl`

The version of `gkectl` that you can use for the upgrade depends on the target cluster version (that is, the version of the cluster you are upgrading to). Typically, you use the same version of `gkectl` as the cluster target version. The following rules are enforced during the upgrade:

  * The `gkectl` version can't be a lower minor version than the target minor cluster version. For example, if you are upgrading a 1.29 cluster to 1.30, you can't use `gkectl` 1.29 since that is lower than the target cluster version. Patch versions don't matter. For example, you can use `gkectl` version 1.29.0-gke.1456 to upgrade to a higher patch version, such as 1.29.1000-gke.94.

  * The `gkectl` version can't be more than two minor versions higher than the current cluster version. For example, if you are upgrading a 1.28 cluster to 1.29, the `gkectl` version can be 1.29 or 1.30. But you can't use `gkectl` version 1.31 because that is three minor versions higher than the cluster version.

  * If you are [upgrading the cluster to an advanced cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/update-or-upgrade-to-adv-cluster), the `gkectl` version **must** be the same as your target version. For example, if you are upgrading a 1.32 non-advanced cluster to 1.33.0-gke.799 advanced cluster, the `gkectl` version must be 1.33.0-gke.799.

    * Your cluster will be upgraded to advanced cluster by default in 1.33. That means for 1.32 to 1.33 upgrades, the `gkectl` version must be the same as the upgraded version.

    * This strict version requirement only applies during the transition to an advanced cluster. For all subsequent upgrades on your advanced cluster, the standard version skew rules are in effect.




If needed, see [Download `gkectl`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads#download_gkectl) to get a supported version of `gkectl`.

For information about the version skews between admin and user clusters, see the Version skew section in this document.

### Legacy features blocked on upgrades

Dataplane V2 is required for all user clusters. Before upgrading a user cluster to version 1.31, follow the steps in [Enable Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#enable-dataplane-v2).

The following legacy features are blocked during cluster upgrade to version 1.32:

  * Integrated F5 Big IP load balancer configuration
  * Non-HA admin cluster
  * Kubeception user cluster
  * Seesaw load balancer



You must [migrate your clusters to recommended features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/migrate-recommended-features) before upgrading to version 1.32.

## Upgrade sequence

The sequence in which you upgrade admin and user clusters depends on the cluster version that you are upgrading to, referred to as the _target version_ :

### 1.31 and higher

When the target version is 1.31 or higher, you must upgrade your admin cluster _before_ you upgrade user clusters that are managed by the admin cluster. The following steps describe the upgrade sequence.

  1. Upgrade the admin workstation. We recommend that you do this even if you plan to use the Google Cloud console, Google Cloud CLI, or Terraform to upgrade user clusters.

  2. [Diagnose](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose) your admin and user clusters using `gkectl diagnose cluster` to verify they are healthy. Resolve any issues before upgrading.

  3. Upgrade the admin cluster.

  4. Upgrade the user clusters, one at a time.

     * You can optionally upgrade a user cluster's control plane separately from the node pools on the user cluster. For more information, see [Upgrade node pools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-node-pools).

       * Version 1.31: Not available on advanced clusters.
       * Version 1.32 and higher: Available on advanced clusters.
     * You can optionally skip a minor version when upgrading node pools. For more information, see [Skip a version when upgrading node pools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/skip-version-upgrade).

       * Version 1.31: Not available on advanced clusters.
       * Version 1.32 and higher: Available on advanced clusters.

After all node pools in a user cluster are at the same version as the user cluster's control plane, the user cluster is completely upgraded.




### 1.30 and lower

When the target version is 1.30 or lower, you must upgrade all user clusters _before_ you upgrade the admin cluster that manages them.

  1. Upgrade the admin workstation. We recommend that you do this even if you plan to use the Google Cloud console, Google Cloud CLI, or Terraform to upgrade user clusters.

  2. [Diagnose](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose) your admin and user clusters using `gkectl diagnose cluster` to verify they are healthy. Resolve any issues before upgrading.

  3. Upgrade the user clusters, one at a time.

     * In version 1.14 and later, you can optionally upgrade a user cluster's control plane separately from the node pools on the user cluster.

     * In version 1.16 and later, you can optionally skip a minor version when upgrading node pools. For more information, see [Skip a version when upgrading node pools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/skip-version-upgrade).

After all node pools in a user cluster are at the same version as the user cluster's control plane, the user cluster is completely upgraded.

An admin cluster can't be at a _higher_ minor version than any of the user clusters that it manages. If any of your user clusters are at the same minor version as the admin cluster, then you can't upgrade the admin cluster.

  4. When all the user clusters are at least one minor version later than the admin cluster, you can optionally upgrade the admin cluster.




The version skew and version rules for upgrades have changed in 1.28 and later. For more information, see the Version skew section in this document.

## Order in which nodes are upgraded

The order in which admin cluster control plane nodes, user cluster control plane nodes, and user cluster worker nodes are upgraded depends on the target version and whether Controlplane V2 is enabled on the user cluster.

### Controlplane V2

When Controlplane V2 is enabled, the control plane for the user cluster runs on the user cluster itself. For Controlplane V2, the user cluster control plane nodes are upgraded during the user cluster upgrade, and the admin cluster control plane nodes are upgraded during the admin cluster upgrade.

### Kubeception

When Controlplane V2 isn't enabled, the control plane for the user cluster runs on one or more nodes in the admin cluster. This configuration is referred to as kubeception. For kubeception clusters, the upgrade version determines the node upgrade behavior:

Upgrade version | Node upgrade behavior  
---|---  
1.32 and higher | Kubeception clusters aren't supported. You must [migrate all user clusters to Controlplane V2](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/migrate-recommended-features) before upgrading to 1.32.  
1.31 | 

  * The admin cluster nodes are upgraded during the admin cluster upgrade.
  * The user cluster control plane nodes are upgraded during the user cluster upgrade.

  
1.30 and lower | Both the user cluster control plane nodes and the admin cluster control plane nodes are upgraded during the admin cluster upgrade.  
  
## Admin cluster upgrades

### 1.31 and higher

When the target version is 1.31 or higher, you must upgrade the admin cluster first, and then upgrade the user clusters.

You can use either `gkectl` or the gcloud CLI to upgrade admin clusters.

### 1.30 and lower

When the target version is 1.30 or lower, upgrade all the user clusters first, and then upgrade the admin cluster. You can upgrade the admin cluster when the control plane and node pools on all user clusters are at least one minor version _higher_ than the admin cluster.

Only `gkectl` supports upgrading admin clusters. The GKE On-Prem API clients don't support upgrading admin clusters.

## User cluster upgrades

When upgrading user clusters, you can choose to upgrade the user cluster as a whole (meaning you can upgrade the control plane and all node pools in the cluster), or you can upgrade the user cluster's control plane and leave the node pools at the current version. Which approach you take depends on several factors, such as:

  * The environment (production or non-production) that the cluster is in.
  * The length of your maintenance window.
  * The version of the user cluster.



For example, in a development environment, you might want to keep the process straightforward and upgrade both the user cluster's control plane and all node pools. But in a production environment with a short maintenance window, you might want to upgrade only the control plane because that takes less time and with high availability (HA) control planes, the control plane upgrade shouldn't disrupt user workloads. When the control plane is at version 1.28 or higher, you can skip a minor version when upgrading node pools.

  * Version 1.31: Not available on advanced clusters.
  * Version 1.32 and higher: Available on advanced clusters.



### Selectively upgrade node pools

In certain situations, you might want to upgrade some, but not all of the node pools in a user cluster. For example, after upgrading the control plane, you could upgrade a node pool that has light traffic or runs your least critical workloads. After you are convinced that your workloads run correctly on the new version, you could upgrade additional node pools, until eventually all the node pools are upgraded. For more information, see [Upgrade node pools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-node-pools).

### Skip a minor version when upgrading node pools

If your clusters are at version 1.16 or higher, you can skip a minor version when upgrading node pools. Performing a skip-version upgrade halves the time that it would take to sequentially upgrade node pools two versions. Additionally, skip-version upgrades lets you increase the time between upgrades needed to stay on a supported version. Reducing the number of upgrades reduces workload disruptions and verification time. For more information, see [Skip a version when upgrading node pools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/skip-version-upgrade). 

### Choose a tool to upgrade user clusters

Google Distributed Cloud provides you a choice of tools for upgrading user clusters.

  * The command-line tool `gkectl`, which you run on your admin workstation. Before the upgrade, you modify your user cluster [configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#nodepool-gkeonpremversion-field) to set the target version for the cluster's control plane and optionally, for the node pools. You specify this file on the command line to `gkectl`.

If you have advanced cluster enabled, you must use `gkectl` for the upgrade. The GKE On-Prem API clients aren't supported on advanced clusters.

  * The Google Cloud console, Google Cloud CLI, or [Terraform](https://www.terraform.io), which you can run from any computer that has network connectivity to the GKE On-Prem API. These standard tools are clients of the [GKE On-Prem API](https://docs.cloud.google.com/anthos/clusters/docs/on-prem-api/reference/rest), which runs on Google Cloud infrastructure.

    * You can use Terraform for the upgrade only if you created the user cluster using Terraform.

    * If your user cluster was created using `gkectl`, the cluster must be enrolled in the GKE On-Prem API to use the console or the gcloud CLI for the upgrade. In 1.16 and later, clusters created using `gkectl` are enrolled in the GKE On-Prem API by default. For clusters created in earlier versions, you can [enroll the cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster) after it is created.

Even if you decide to use `gkectl` for the upgrade, you might want to enroll the cluster in the GKE On-Prem API to get information about the clusters using the console or the [gcloud CLI](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster#get_cluster_information).




The tool that you use depends on how you plan to upgrade user clusters:

  * **Upgrade the cluster as a whole** : You can use `gkectl`, the Google Cloud console, the Google Cloud CLI, or Terraform to upgrade a user cluster (the control plane together with all node pools).

  * **Upgrade only the control plane** : You can use `gkectl`, the gcloud CLI, or Terraform to upgrade a user cluster's control plane separately from the node pools. The console doesn't support upgrading only the control plane.

  * **Selectively upgrade node pools after the control plane is upgraded** : You can use `gkectl`, the gcloud CLI, or Terraform to upgrade specific node pools after the control plane is upgraded.

  * **Upgrade the control plane and one or more node pools at the same time** : Only `gkectl` supports this use case.




## Version skew

The version skew is the difference in minor versions between an admin cluster and its managed user cluster(s). In the following sections, the _user cluster version_ refers to the version of the control plane and node pools together, as a whole.

Additionally, the version skew is the difference in minor versions between a user cluster's control plane and the node pools on the user cluster.

In a multi-cluster environment, understanding the supported version skew and version rules for upgrades might help you plan the order in which you upgrade clusters.

### Admin and user cluster version skew

An admin cluster can manage user clusters that are at different versions. This capability lets you upgrade a fleet of user clusters on a schedule that works for your organization.

### 1.31 and higher

In version 1.31 and higher, the admin cluster can be up to 2 minor versions higher than its user clusters. For example, if an admin cluster is at 1.31, the user clusters managed by that admin cluster can be at 1.29, 1.30, or 1.31.

In general terms, if `1.n` is the admin cluster minor version, then the user clusters can be at `1.n-2`, `1.n-1`, or `1.n`. The admin cluster can't be upgraded to the next minor version until all user clusters are at `1.n` or `1.n-1`.

### 1.29 - 1.30

The version skew is the same as in 1.28. In 1.29, this feature transitioned to the [General Availability](https://cloud.google.com/products#product-launch-stages) stage.

In version 1.29 and higher, user clusters can be up to 2 minor versions _higher_ than their admin cluster. For example, if an admin cluster is at 1.34, the user clusters managed by that admin cluster can be at 1.34, 1.35, or 1.36.

In general terms, if `1.n` is the admin cluster minor version, then the user clusters can be at `1.n`, `1.n+1`, or `1.n+2`. User clusters at `1.n+2` can't be upgraded to the next minor version until the admin cluster is upgraded at least one minor version.

### 1.28

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

In version 1.28, user clusters can be up to 2 minor versions _higher_ than their admin cluster. For example, if an admin cluster is at 1.15, the user clusters managed by that admin cluster can be at 1.15, 1.16, or 1.28. User clusters at 1.28 can't be upgraded to 1.29 until the admin cluster is upgraded to at least 1.16.

### 1.16 and lower

In version 1.16 and lower, user clusters can only be 1 minor version _higher_ than their admin cluster. For example, if an admin cluster is at 1.15, the user clusters managed by that admin cluster can be at 1.15 or 1.16.

In general terms, if `1.n` is the admin cluster minor version, then the user clusters can be at `1.n` or `1.n+1`. User clusters can't be upgraded to the next minor version until the admin cluster is at the same minor version as the user cluster.

### User cluster control plane and worker node pool version skew

### 1.29 and higher

The version skew is the same as in 1.28. In 1.29, this feature transitioned to the [General Availability](https://cloud.google.com/products#product-launch-stages) stage.

In version 1.29 and higher, a user cluster's control plane can be up to 2 minor versions _higher_ than the worker node pools in the cluster. For example, if a user cluster's control plane is at 1.36, the worker node pools in the cluster can be at 1.34, 1.35, or 1.36.

In general terms, if `1.n` is the minor version of a user cluster control plane, the worker node pools in the cluster can be at `1.n`, `1.n-1`, or `1.n-2`. User cluster control planes can't be upgraded to the next minor version until all worker node pools are at `1.n` or `1.n-1`.

**Note:** Control plane and worker node pool version skew only applies to worker node pools. Load balancer node pools (node pools with `enableLoadBalancer: true`) must match the cluster version.

### 1.28

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

In version 1.28, a user cluster's control plane can be up to 2 minor versions _higher_ than the node pools in the cluster. For example, if a user cluster's control plane is at 1.28, the node pools in the cluster can be at 1.15, 1.16, or 1.28. User cluster control planes can't be upgraded to 1.29 until all node pools are at `1.28` or `1.16`.

### 1.16 and lower

In version 1.16 and lower, a user cluster's control plane can only be 1 minor version _higher_ than the node pools in the cluster. For example, if a user cluster's control plane is at 1.16, the node pools in the cluster can be at 1.15 or 1.16.

In general terms, if `1.n` is the minor version of a user cluster control plane, the node pools in the cluster can be at `1.n` or `1.n-1`. User clusters can't be upgraded to the next minor version until all node pools are at the same minor version as the control plane.

## Version rules for admin cluster and user cluster control plane upgrades

The version rules for admin clusters and user cluster control plane upgrades are the same. You can upgrade directly to any version that is in the same minor release or the next minor release. For example, you can upgrade from 1.36.0 to 1.36.1, or from 1.35.1 to 1.36.0. The patch versions don't affect the upgrade version rules.

If you are upgrading to a version that is not part of the next minor release, you must upgrade through one version of each minor release between your current version and your target version. Skipping a minor version isn't supported. For example, if you want to upgrade from version 1.34.x to version 1.36.x, you can't upgrade directly. You must first upgrade from 1.34.x to 1.35.x, and then upgrade to 1.36.x.

In general terms, only upgrades from `1.n` to `1.n+1` are supported for admin cluster upgrades and user cluster control plane upgrades.

## Version rules for worker node pool upgrades

In version 1.28 and later, you can skip one minor version when upgrading a worker node pool in a user cluster. For example, if a user cluster control plane is at 1.36 and a worker node pool is at 1.34, you can skip 1.35 and upgrade the worker node pool directly to 1.36. The patch versions don't affect the upgrade version rules.

In general terms, if a user cluster control plane is at `1.n`, then you can upgrade worker node pools that are at `1.n-2` directly to `1.n`. Skipping one minor version when upgrading worker node pools might reduce the amount of time than doing two worker node pool upgrades (to upgrade from `1.n-2` to `1.n-1` then to `1.n`). This is another reason why you might prefer to upgrade a user cluster's control plane separately from the worker node pools that run on the user cluster.

  * Version 1.31: Not available on advanced clusters.
  * Version 1.32 and higher: Available on advanced clusters.

**Note:** Version rules for worker node pool upgrades only apply to worker node pools. Load balancer node pools (node pools with `enableLoadBalancer: true`) must match the cluster version.

## Patch version upgrades

We recommend that you upgrade to the [latest patch version](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/version-and-upgrade-support#google_cloud_distributed) whenever possible to ensure your clusters have the latest security fixes. Patch versions don't affect the version skew and upgrade rules. For a given minor version, you can upgrade to any higher patch version. That is, you can upgrade a `1.36.**X**` version cluster to version `1.36.**Y**` as long as `**Y**` is greater than `**X**`. For example, you can upgrade from `1.35.0` to `1.35.1` and you can upgrade from `1.35.1` to `1.35.3`.

## What's next

Review Review [Upgrade best practices](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-best-practices) and create a plan for upgrading your clusters.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
