---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading/
title: Upgrade a cluster \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:32.865766+00:00
---

# Upgrade a cluster  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Upgrade a cluster Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to upgrade clusters in Google Distributed Cloud (software only) for VMware. This document provides the steps for upgrading your admin workstation, user clusters, and admin clusters. The steps for upgrading a user cluster show how to upgrade the control plane and all node pools. If you want to upgrade the user cluster control plane and node pools separately, see [Upgrade node pools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-node-pools).

This page is for IT administrators and Operators who manage the lifecycle of the underlying tech infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Before you proceed, we recommend that you review the following documentation:

  * [Upgrade overview](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-overview)   
Among other things, this document describes the supported version skew and version rules for upgrades, which have changed for 1.28 and later.

  * [Upgrade best practices](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-best-practices)  
This document provides checklists and best practices for upgrading clusters.


**Important:** Make sure you have a current backup of the admin and user clusters before starting the upgrade. For more information, see [Back up the user and admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-best-practices#back_up_the_user_and_admin_cluster).

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



## Requirements

This section provides information about version-related requirements and requirements for using the GKE On-Prem API clients (the Google Cloud console, the Google Cloud CLI, and Terraform) for upgrades.

### Version rules

The rules for upgrades depends on the cluster minor version.

  * For versions 1.30 and lower, the user cluster minor version must be greater than or equal to the admin cluster minor version. The patch version doesn't matter. For example, if a user cluster is at version 1.30.1, the admin cluster can be upgraded to a higher patch version, such as 1.30.3.

  * For versions 1.31 and higher, the admin cluster version, including the patch version, must be greater than or equal to the user cluster version. For example, if an admin cluster is at version 1.31.1, the highest version that the user cluster can be upgraded to is 1.31.1.




When you want to upgrade your clusters to version 1.31, you must first bring all your clusters to version 1.30. After all the clusters are at version 1.30, you upgrade the admin cluster to version 1.31. After that, you can upgrade the user clusters to the same 1.31 patch version as the admin cluster.

#### Version rules for `gkectl`

The version of `gkectl` that you can use for the upgrade depends on the target cluster version (that is, the version of the cluster you are upgrading to). Typically, you use the same version of `gkectl` as the cluster target version. The following rules are enforced during the upgrade:

  * The `gkectl` version can't be a lower minor version than the target minor cluster version. For example, if you are upgrading a 1.29 cluster to 1.30, you can't use `gkectl` 1.29 since that is lower than the target cluster version. Patch versions don't matter. For example, you can use `gkectl` version 1.29.0-gke.1456 to upgrade to a higher patch version, such as 1.29.1000-gke.94.

  * The `gkectl` version can't be more than two minor versions higher than the current cluster version. For example, if you are upgrading a 1.28 cluster to 1.29, the `gkectl` version can be 1.29 or 1.30. But you can't use `gkectl` version 1.31 because that is three minor versions higher than the cluster version.

  * If you are [upgrading the cluster to an advanced cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/update-or-upgrade-to-adv-cluster), the `gkectl` version **must** be the same as your target version. For example, if you are upgrading a 1.32 non-advanced cluster to 1.33.0-gke.799 advanced cluster, the `gkectl` version must be 1.33.0-gke.799.

    * Your cluster will be upgraded to advanced cluster by default in 1.33. That means for 1.32 to 1.33 upgrades, the `gkectl` version must be the same as the upgraded version.

    * This strict version requirement only applies during the transition to an advanced cluster. For all subsequent upgrades on your advanced cluster, the standard version skew rules are in effect.




If needed, see [Download `gkectl`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads#download_gkectl) to get a supported version of `gkectl`.

### Review your firewall rules

In version 1.29 and later, server-side preflight checks are enabled by default. Server-side preflight checks require additional firewall rules. In [Firewall rules for admin clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/firewall-rules#firewall_rules_for_admin_clusters), search for "Preflight checks" and make sure all required firewall rules are configured.

With server-side preflight checks, when you upgrade a user cluster using `gkectl`, the preflight checks are run on the admin cluster instead of locally on the admin workstation. Server-side preflight checks are also run on the admin cluster when you use the Google Cloud console, the Google Cloud CLI, or Terraform to upgrade a cluster.

When you upgrade an admin cluster, Google Distributed Cloud deploys a [Kubernetes in Docker](https://kind.sigs.k8s.io/) (kind) cluster to temporarily host the Kubernetes controllers needed to upgrade the admin cluster. This transient cluster is called a _bootstrap cluster_. Server-side preflight checks are run on the bootstrap cluster when you upgrade an admin cluster.

### Enable `stackdriver`

If you created the user cluster using `gkectl`, before upgrading, make sure that the [`stackdriver`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#stackdriver-section) section in your user cluster configuration file is filled in, which enables `stackdriver` (needed for logging and monitoring). If `stackdriver` isn't enabled, fill in the `stackdriver` section in the user cluster configuration file, and [update the cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/updating-general) before you upgrade.

If you created the cluster using Terraform, the Google Cloud console, or the gcloud CLI, `stackdriver` is automatically enabled.

### Enable Dataplane V2

Dataplane V2 is required to be enabled on all user clusters as of version 1.31. Before upgrading a user cluster to 1.31, perform the following steps. If you have concerns about temporarily removing the `NetworkPolicy` specification, contact Google Support.

Set [`enableDataplaneV2`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enabledataplanev2-field) to `true` in your user cluster configuration file.

If your cluster is using a `NetworkPolicy`, temporarily remove its specification from the cluster, as follows:

  1. Check whether there's any non-system `NetworkPolicy` applied to your cluster:
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get networkpolicy -A -o wide | grep -v kube-system
         

  2. If the output of the prior step was not empty, save each `NetworkPolicy` specification to a file so that you can reapply the specification after upgrading the cluster.
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get networkpolicy NETWORK_POLICY_NAME -n NETWORK_POLICY_NAMESPACE -o yaml > NETWORK_POLICY_NAME.yaml
         

Replace the following:

     * `NETWORK_POLICY_NAME`: the name of the `NetworkPolicy` that you are saving.
     * `NETWORK_POLICY_NAMESPACE`: the namespace of the `NetworkPolicy`.
  3. Delete the `NetworkPolicy`, using the following command:
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG delete networkpolicy NETWORK_POLICY_NAME -n NETWORK_POLICY_NAMESPACE
         

  4. Continue with the upgrade.

  5. After the upgrade is complete, if you removed any non-system `NetworkPolicy` specifications, then reapply them with this command:
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG apply -f NETWORK_POLICY_NAME.yaml
         




### Google API and IAM requirements

To upgrade a cluster to version 1.28 and later, you must enable `kubernetesmetadata.googleapis.com` and grant the `kubernetesmetadata.publisher` IAM role to the [logging-monitoring service account](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#logging_monitoring_service_account). These changes are required to use Cloud Monitoring.

  1. Enable `kubernetesmetadata.googleapis.com`:
         
         gcloud services enable --project PROJECT_ID  \
             kubernetesmetadata.googleapis.com
         

Replace `PROJECT_ID` with the ID of the [fleet host project](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/multiple-gcp-projects#fleet_host_project) in which the user cluster is a member. This is the project that you specified when the cluster was created. If you created the cluster using `gkectl`, this is the project ID in the `gkeConnect.projectID` field in the cluster configuration file.

  2. If your organization has set up [an allowlist](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/firewall-rules) that lets traffic from Google APIs and other addresses pass through your proxy server, add `kubernetesmetadata.googleapis.com` to the allowlist.

  3. Grant the `kubernetesmetadata.publisher` role to the logging-monitoring service account:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member "serviceAccount:SERVICE_ACCOUNT_EMAIL" \
             --role "roles/kubernetesmetadata.publisher"
         

Replace `SERVICE_ACCOUNT_EMAIL` with the email address of your logging-monitoring service account.




### Legacy features blocked on upgrades

The following legacy features are blocked during cluster upgrade to version 1.32:

  * Dataplane V1 (Calico)
  * Integrated F5 Big IP load balancer configuration
  * Non-HA admin cluster
  * Kubeception user cluster
  * Seesaw load balancer



You must [migrate your clusters to recommended features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/migrate-recommended-features) before upgrading to version 1.32.

### IAM requirements for upgrading user clusters

Skip this section if you plan to use `gkectl` for the user cluster upgrade.

If you want to use the Google Cloud console, the Google Cloud CLI, or Terraform to upgrade a user cluster, and you aren't a project owner, you must be granted the Identity and Access Management role `roles/gkeonprem.admin` on the Google Cloud project that the cluster was created in. For details on the permissions included in this role, see [GKE on-prem roles](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem) in the IAM documentation.

To use the console to upgrade the cluster, at a minimum, you also need the following:

  * `roles/container.viewer`. This role lets users view the GKE Clusters page and other container resources in the console. For details about the permissions included in this role, or to grant a role with read/write permissions, see [Kubernetes Engine roles](https://docs.cloud.google.com/iam/docs/roles-permissions/container) in the IAM documentation.

  * `roles/gkehub.viewer`. This role lets users view clusters in the console. For details about the permissions included in this role, or to grant a role with read/write permissions,see [GKE Hub roles](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub) in the IAM documentation.




## Limitations with advanced clusters

Note the following limitations if you have [advanced clusters enabled](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#enable-advanced-cluster-field):

  * When upgrading clusters from version 1.32 to 1.33, you must use `gkectl`. The GKE On-Prem API clients (the console, the gcloud CLI, and Terraform) aren't supported for this specific upgrade path but are supported for upgrades starting from version 1.33.

  * Only synchronous upgrades are supported.




## Make configuration changes either before or after an upgrade

If you need to make configuration changes to your clusters, do the [cluster update](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/updating-general) either before or after the upgrade. The only change to the cluster configuration for an upgrade should be the version. Depending on the cluster version and type, other configuration changes are either silently ignored or cause the upgrade to fail. For more information see [Remove unsupported changes to unblock upgrade](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/create-upgrade#remove_unsupported_changes_to_unblock_upgrade).

## Check available versions for cluster upgrades

Run the following command to see which versions are available for upgrade:
    
    
    gkectl version --kubeconfig ADMIN_CLUSTER_KUBECONFIG
    

Replace `ADMIN_CLUSTER_KUBECONFIG` with the path to the admin cluster's kubeconfig file.

The output shows the current version and the versions available for upgrade.

If you plan to use the console, the gcloud CLI or Terraform for the upgrade, it takes about 7 to 14 days after a release for the version to be available in the GKE On-Prem API in all Google Cloud regions. The console lists only the available versions for the user cluster upgrade. The steps for upgrading a user cluster using the gcloud CLI or Terraform include a step to run [`gcloud container vmware clusters query-version-config`](https://docs.cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/query-version-config) to get available versions for the upgrade.

## Upgrade your admin workstation

The way you upgrade your admin workstation depends on how you created it: [gkeadm](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-workstation#gkeadm) or [user-managed](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-workstation#user-managed).

### gkeadm

### Locate required files

Before you created your admin workstation, you filled in an [admin workstation configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-workstation-configuration-file) that was generated by `gkeadm create config`. The default name for this file is `admin-ws-config.yaml`.

In addition, your workstation has an information file. The default name of this file is the same as the name of your admin workstation.

Locate your admin workstation configuration file and your information file. You need them to do the upgrade steps. If these files are in your current directory and they have their default names, then you won't need to specify them when you run the upgrade commands. If these files are in another directory, or if you have changed the filenames, then you specify them by using the `--config` and `--info-file` flags.

If your output information file is missing, you can recreate it. See Recreate an information file if missing.

### Upgrade

To upgrade the admin workstation:

  1. Check the `adminWorkstation.diskGB` field in the admin workstation configuration file and make sure that the specified size is at least 100, for example:
         
         adminWorkstation:
           diskGB: 100
         

When upgrading to 1.28 and higher, 100 GB is required, and the cluster upgrade fails if the admin workstation doesn't have sufficient disk space.

  2. From your jump server, download `gkeadm`:
         
         gkeadm upgrade gkeadm --target-version TARGET_VERSION
         

Replace `TARGET_VERSION` with the version that you are upgrading to. You need to specify a complete version number in the form of `X.Y.Z-gke.N.`. For a list of the Google Distributed Cloud versions, see [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/version-history#supported-versions).

  3. Upgrade your admin workstation:
         
         gkeadm upgrade admin-workstation --config AW_CONFIG_FILE \
             --info-file INFO_FILE
         

Replace the following:

     * `AW_CONFIG_FILE`: the path of your admin workstation configuration file. You can omit this flag if the file is in your current directory and has the name `admin-ws-config.yaml`.

     * `INFO_FILE`: the path of your information file. You can omit this flag if the file is in your current directory. The default name of this file is the same as the name of your admin workstation. 




### User-managed

On your admin workstation, navigate to a directory where you want to install a new version of`gkectl`.

  1. Download `gkectl`:
         
         gcloud storage cp gs://gke-on-prem-release/gkectl/TARGET_VERSION/gkectl ./
         chmod +x gkectl
         

Replace `TARGET_VERSION` with the version that you are upgrading to. You need to specify a complete version number in the form of `X.Y.Z-gke.N.`. For a list of the Google Distributed Cloud versions, see [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/version-history#supported-versions).

  2. Download the Google Distributed Cloud bundle. Make sure the version matches the one you used to download `gkectl`:
         
         gcloud storage cp gs://gke-on-prem-release/gke-onprem-bundle/TARGET_VERSION/gke-onprem-vsphere-TARGET_VERSION.tgz ./
         




## Upgrade the admin cluster

The steps for upgrading the admin cluster vary slightly depending on the minor version you're upgrading to (the target version):

### 1.31 and higher

If the target version is 1.31 or higher, before you upgrade your user clusters to the next minor version, you need to upgrade your admin cluster. In 1.31 and higher, the admin cluster version, including the patch version, must be greater than or equal to the user cluster version. For example, if an admin cluster is at version 1.31.1, the highest version that the user cluster can be upgraded to is 1.31.1.

Run the following command on your admin workstation to import OS images to vSphere:
    
    
    gkectl prepare \
        --bundle-path /var/lib/gke/bundles/gke-onprem-vsphere-TARGET_VERSION.tgz \
        --kubeconfig ADMIN_CLUSTER_KUBECONFIG
    

Replace `ADMIN_CLUSTER_KUBECONFIG` with the path to the admin cluster's kubeconfig file.

### 1.30 and lower

If the target version is 1.30 or lower, you must upgrade all your user clusters before you upgrade your admin cluster. The admin cluster minor version must be less than or equal to the user cluster minor version. The patch version doesn't matter. For example, if a user cluster is at version 1.30.1, the admin cluster can be upgraded to a higher patch version, such as 1.30.3.

### Before you begin:

  * Always [diagnose](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose#diagnose_admin_cluster) your cluster before upgrading. Run `gkectl diagnose cluster` to ensure your admin cluster is healthy, and resolve any issues before starting the upgrade.

  * If you are upgrading to version 1.13 or higher, you must first register the admin cluster by filling out the `gkeConnect` section in the admin cluster configuration file. Run the [`gkectl` update cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/updating-general) command with the configuration file changes.

  * Make sure your `gkectl` and clusters are the appropriate version for an upgrade, and that you have downloaded the appropriate bundle. The version skew between your admin and user clusters depends on the Google Distributed Cloud version. To make sure you can upgrade your admin cluster, see [Admin and user cluster version skew](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-overview#admin_and_user_cluster_version_skew).

  * Make sure the `bundlepath` field in the [admin cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#bundlepath-field) matches the path of the bundle to which you want to upgrade.

  * About `cert-manager` installation: `cert-manager` is automatically installed on advanced clusters. When you migrate from a non-advanced cluster to an advanced cluster, the integrated `cert-manager` automatically overrides any customer-installed versions of `cert-manager`. Make sure you don't have critical custom configurations or features applied to your existing `cert-manager` before you update or upgrade to advanced clusters. For more information, see [Upgrade to `cert-manager` bundled with advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/update-or-upgrade-to-adv-cluster#upgrade-cert-manager). 

If you make any other changes to the fields in the admin cluster configuration file, these changes are ignored during the upgrade. To make those changes take effect, you must first upgrade the cluster, and then run an [update cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/updating-general) command with the configuration file changes to make other changes to the cluster.




### Perform the upgrade

### gkectl

Do the steps in this section on your admin workstation. There are two variations of the `gkectl upgrade admin` command:

  * **Asynchronous** :   
With the asynchronous variation, the command starts the upgrade and then completes. You don't need to watch the output of the command for the entire duration of the upgrade. Instead, you can periodically check on the upgrade progress by running `gkectl list admin` and `gkectl describe admin`. To use the asynchronous variation, include the `--async` flag in the command.



Requirements for asynchronous upgrade:

  * Supported only for HA admin clusters with version 1.29 or higher.
  * All user clusters must have Controlplane V2 enabled.
  * Version 1.31: Not supported on advanced clusters.
  * Version 1.32 and higher: Available on advanced clusters.

  * **Synchronous** :   
With the synchronous variation, the `gkectl upgrade admin` command outputs status messages to the admin workstation as the upgrade progresses.


**Note:** The `gkectl upgrade admin` command accepts several optional flags. For example, you can include the `--skip-validation-infra` flag to skip checking your vSphere infrastructure. If an initial attempt to upgrade a non-advanced admin cluster to an [advanced cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/update-or-upgrade-to-adv-cluster#update_or_upgrade_the_admin_cluster_to_advanced_cluster) fails, include the `--reuse-bootstrap-cluster` flag when you rerun `gkectl upgrade admin` to resume the upgrade. Don't use `--reuse-bootstrap-cluster` on the initial upgrade attempt or when upgrading an existing advanced cluster. To view all available flags, run `gkectl upgrade admin -h`.

### Asynchronous upgrade

  1. On your admin workstation, diagnose the cluster before upgrading:
         
         gkectl diagnose cluster \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         

     * If the command reports any errors or warnings, refer to [Diagnose cluster issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose#diagnose_admin_cluster) and resolve them before proceeding.
  2. Start an asynchronous upgrade:
         
         gkectl upgrade admin \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --config ADMIN_CLUSTER_CONFIG_FILE \
             --async
         

Replace the following:

     * `ADMIN_CLUSTER_KUBECONFIG`: the path to the admin cluster's kubeconfig file.

     * `ADMIN_CLUSTER_CONFIG_FILE`: the path to the admin cluster configuration file.

The preceding command completes, and you can continue to use your admin workstation while the upgrade is in progress.

  3. To see the status of the upgrade:
         
         gkectl list admin --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         

The output shows a value for the cluster `STATE`. If the cluster is still upgrading, the value of `STATE` is `UPGRADING`. For example:
         
         NAME              STATE         AGE    VERSION
         gke-admin-test    UPGRADING     9h     1.36.200-gke.118
         

The possible values for `STATE` are `RUNNING`, `UPGRADING`, `RECONCILING`, `ERROR`, and `UNKNOWN`.

  4. To get more details about the upgrade progress and cluster events:
         
         gkectl describe admin --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         

The output shows the OnPremAdminCluster custom resource for the specified admin cluster, which includes cluster status, conditions.

Click to view the example output
         
         Status:
             Cluster State:  RUNNING
             Conditions:
               Last Transition Time:    2026-08-10T20:22:58Z
               Message:                 Operator NodePool is ready
               Observed Generation:     2
               Reason:                  OperatorNodePoolReady
               Status:                  True
               Type:                    ControlPlaneReady
               Last Transition Time:    2026-08-10T20:22:59Z
               Message:                 Cluster is running
               Observed Generation:     2
               Reason:                  ClusterRunning
               Status:                  True
               Type:                    Ready
               Last Transition Time:    2026-08-10T20:23:00Z
               Message:
               Observed Generation:     2
               Reason:                  Reconciling
               Status:                  False
               Type:                    OperatorClusterKubeProxyCleanedUp
               Last Transition Time:    2026-08-10T20:22:58Z
               Message:
               Observed Generation:     2
               Reason:                  PreflightCheckPassed
               Status:                  True
               Type:                    OperatorClusterPreflightCheckSuccessful
               Last Transition Time:    2026-08-10T15:56:50Z
               Message:
               Observed Generation:     2
               Reason:                  ProvisioningStarted
               Status:                  True
               Type:                    OperatorClusterProvisioningStarted
               Last Transition Time:    2026-08-10T15:56:50Z
               Message:
               Observed Generation:     2
               Reason:                  RemoteTrackerSetupComplete
               Status:                  True
               Type:                    OperatorClusterRemoteTrackerSetupSuccessful
               Last Transition Time:    2026-08-10T15:56:50Z
               Message:
               Observed Generation:     2
               Reason:                  Reconciling
               Status:                  False
               Type:                    OperatorClusterStalled
               Last Transition Time:    2026-08-10T15:56:50Z
               Message:
               Observed Generation:     2
               Reason:                  NotPresent
               Status:                  False
               Type:                    OperatorClusterWaitingOnPendingClusterID
               Last Transition Time:    2026-08-10T20:22:59Z
               Message:                 Operator Cluster is ready
               Observed Generation:     2
               Reason:                  OperatorClusterReady
               Status:                  True
               Type:                    OperatorClusterReady
               Last Transition Time:    2026-08-10T15:56:50Z
               Message:                 Component provisioner job is completed
               Observed Generation:     2
               Reason:                  ComponentProvisionerJobCompleted
               Status:                  True
               Type:                    ComponentProvisionerSystemProfileInstalled
               Last Transition Time:    2026-08-10T15:58:20Z
               Message:                 Component provisioner job is completed
               Observed Generation:     2
               Reason:                  ComponentProvisionerJobCompleted
               Status:                  True
               Type:                    ComponentProvisionerAdminProfileInstalled
             Gke On Prem Version:       1.36.0-gke.527
             Last Gke On Prem Version:  1.35.300-gke.87
             Management Conditions:
               Last Transition Time:  2026-08-10T15:58:20Z
               Message:               Component provisioner job is completed
               Observed Generation:   2
               Reason:                ComponentProvisionerJobCompleted
               Status:                True
               Type:                  ManagementProfilesReady
               Last Transition Time:  2026-08-10T15:56:29Z
               Message:               Component provisioner job is completed
               Observed Generation:   2
               Reason:                ComponentProvisionerJobCompleted
               Status:                True
               Type:                  ComponentProvisionerSystemManagementProfileInstalled
               Last Transition Time:  2026-08-10T15:58:20Z
               Message:               Component provisioner job is completed
               Observed Generation:   2
               Reason:                ComponentProvisionerJobCompleted
               Status:                True
               Type:                  ComponentProvisionerManagementProfileInstalled
             Operator Cluster Status:
               Control Plane Node Pool Status:
                 Anthos Bare Metal Version:  1.36.0-gke.527
                 Anthos Bare Metal Versions:
                   1.36.0-gke.527:  3
                 Conditions:
                   Last Transition Time:  2026-08-10T20:18:20Z
                   Observed Generation:   11
                   Reason:                PreflightCheckPassed
                   Status:                True
                   Type:                  PreflightCheckSuccessful
                   Last Transition Time:  2026-08-10T20:22:58Z
                   Observed Generation:   11
                   Reason:                NodepoolReady
                   Status:                True
                   Type:                  Ready
                   Last Transition Time:  2026-08-10T20:22:22Z
                   Observed Generation:   11
                   Reason:                ReconciliationCompleted
                   Status:                False
                   Type:                  Reconciling
                 Gke Versions:
                   v1.36.0-gke.2800:        3
                 Last Reconciliation Time:  2026-08-10T20:25:07Z
                 Maintenance Nodes:         0
                 Managed Fields:
                   Label Keys:
                     kubernetes.googleapis.com/cluster-name
                     node.kubernetes.io/control-plane
                     node.kubernetes.io/master
                   Node Label Keys:
                     vsphere://abcdef-1:
                       onprem.gke.io/failure-domain-name
                       vmware.cluster.gke.io/machine-name
                     vsphere://abcdef-2:
                       onprem.gke.io/failure-domain-name
                       vmware.cluster.gke.io/machine-name
                     vsphere://abcdef-3:
                       onprem.gke.io/failure-domain-name
                       vmware.cluster.gke.io/machine-name
                   Taints:
                     Effect:         PreferNoSchedule
                     Key:            node-role.kubernetes.io/control-plane
                 Ready Nodes:        3
                 Ready Timestamp:    2026-08-10T15:54:01Z
                 Reconciling Nodes:  0
                 Stalled Nodes:      0
                 Unknown Nodes:      0
               Data Plane Load Balancer Status:
                 Conditions:
                   Last Transition Time:  2026-08-10T15:39:16Z
                   Observed Generation:   1
                   Reason:                ReconciliationCompleted
                   Status:                False
                   Type:                  Reconciling
                 Node Pool Location:      control-plane-nodepool
               External Manifests Conditions:
                 Last Transition Time:  2026-08-10T15:56:32Z
                 Observed Generation:   2
                 Reason:                ReconciliationCompleted
                 Status:                False
                 Type:                  Reconciling
               Gke Connect Conditions:
                 Last Transition Time:  2026-08-10T20:13:39Z
                 Observed Generation:   2
                 Reason:                AnthosBareMetalVersion
                 Status:                True
                 Type:                  1.36.0-gke.527
                 Last Transition Time:  2026-08-10T20:13:39Z
                 Observed Generation:   2
                 Reason:                ReconciliationCompleted
                 Status:                False
                 Type:                  Reconciling
               Gke Connect Dependent System Service Conditions:
                 Last Transition Time:  2026-08-10T15:56:32Z
                 Observed Generation:   2
                 Reason:                ReconciliationCompleted
                 Status:                False
                 Type:                  Reconciling
               Gke Hub Registration Status:
                 Membership:
                   Description:  description
                   Name:         name
               Gke Versions:
                 v1.36.0-gke.2800:  3
               Kernel Version Conditions:
                 Last Transition Time:  2026-08-10T15:39:23Z
                 Reason:                kernelVersionCheckPassed
                 Status:                True
                 Type:                  kernelVersionCheckSuccessful
               System Service Conditions:
                 Last Transition Time:  2026-08-10T20:12:26Z
                 Observed Generation:   2
                 Reason:                ReconciliationCompleted
                 Status:                False
                 Type:                  Reconciling
           

  5. When the upgrade is complete, `gkectl list admin` shows a `STATUS` of `RUNNING`:
         
         NAME              STATE         AGE    VERSION
         gke-admin-test    RUNNING       9h     1.36.200-gke.118
         

Also, when the upgrade is complete, `gkectl describe admin` shows a `Last GKE On Prem Version` field under `Status`. For example:
         
         Status:
           Cluster State:  RUNNING
           Last GKE On Prem Version:  1.36.0-gke.1
         




#### Troubleshoot asynchronous upgrade

For an asynchronous upgrade, the timeout duration is based on the number of nodes in the cluster. If the upgrade takes longer than the timeout duration, the cluster state is changed from `UPGRADING` to `ERROR`, with an event saying that the upgrade operation timed out. Note that the `ERROR` state here means the upgrade is taking longer than expected, but has not been terminated. The controller continues the reconciliation and keeps retrying the operation. When an upgrade is blocked or fails, you can run [ `gkectl diagnose`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose) to check for common cluster issues. Based on the result, you can decide whether to perform a manual fix or contact [Google Cloud Support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support) for further assistance. 

### Synchronous upgrade

  1. On your admin workstation, diagnose the cluster before upgrading:
         
         gkectl diagnose cluster \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         

     * If the command reports any errors or warnings, refer to [Diagnose cluster issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose#diagnose_admin_cluster) and resolve them before proceeding.
  2. Run the following command:
         
         gkectl upgrade admin \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --config ADMIN_CLUSTER_CONFIG_FILE
         

Replace the following:

     * `ADMIN_CLUSTER_KUBECONFIG`: the path to the admin cluster kubeconfig file.

     * `ADMIN_CLUSTER_CONFIG_FILE`: the path to the admin cluster configuration file.

The `gkectl upgrade` command runs preflight checks. If the preflight checks fail, the command is blocked. You must fix the failures or use the flag `--skip-preflight-check-blocking` with the command to unblock it.

  3. If you are upgrading to version 1.14.0 or higher, a new kubeconfig file is generated for the admin cluster that overwrites any existing file. To view cluster details in the file, run the following command:
         
         kubectl config view --kubeconfig ADMIN_CLUSTER_KUBECONFIG




### gcloud

Upgrade the admin cluster using the `gcloud` CLI.

  1. Update the platform version to the target version:
         
         gcloud container vmware admin-clusters update ADMIN_CLUSTER_NAME \
             --location=REGION\
             --required-platform-version=VERSION \
             --async
         

Replace the following:

     * `ADMIN_CLUSTER_NAME`: the name of your admin cluster.
     * `REGION`: the Google Cloud region where the admin cluster is managed.
     * `VERSION`: the target version you are upgrading to.

This command returns an operation ID. You can monitor the progress using `gcloud container vmware operations describe`.

  2. After you complete the platform version update, update the admin cluster version:
         
         gcloud container vmware admin-clusters update ADMIN_CLUSTER_NAME \
             --location=REGION \
             --version=VERSION \
             --async
         

This step completes the upgrade of the admin cluster to the target version.




## Upgrade a user cluster

You can use `gkectl`, the console, the gcloud CLI, or Terraform to upgrade a user cluster. For information on deciding which tool to use, see [Choose a tool to upgrade user clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-overview#choose_a_tool_to_upgrade_user_clusters).

### gkectl

## Prepare to upgrade a user cluster

Do the following steps on your admin workstation:

  1. Check if the user cluster is healthy before you begin the initial upgrade attempt. See [Diagnose cluster issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose#diagnose_user_cluster). Run `gkectl diagnose cluster` on the user cluster and resolve any issues.

  2. Do this step only if the `TARGET_VERSION` is 1.30 or lower, or if you are upgrading the user cluster to a different version from the admin cluster. Run `gkectl prepare` to import OS images to vSphere:
         
         gkectl prepare \
           --bundle-path /var/lib/gke/bundles/gke-onprem-vsphere-TARGET_VERSION.tgz \
           --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         

  3. If your cluster has a Windows node pool, run `gkectl prepare windows`, and update the `osImage` field for the node pool. For detailed instructions, see [Upgrade user cluster with Windows node pools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-guide-for-windows-server-os-node-pools#upgrade-windows-node-pools).

  4. In the user cluster configuration file, set [`gkeOnPremVersion`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#gkeonpremversion-field) to the target version of your upgrade.




### Run preflight checks

When upgrading to version 1.29 and higher, you can run the preflight checks before upgrading a user cluster:
    
    
    gkectl upgrade cluster \
        --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
        --config USER_CLUSTER_CONFIG \
        --dry-run
    

Replace `USER_CLUSTER_CONFIG` with the path to the user cluster configuration file.

With the `--dry-run` flag, `gkectl upgrade cluster` runs the preflight checks but doesn't start the upgrade process. Although earlier versions of Google Distributed Cloud run preflight checks, they can't be run separately from the upgrade. By adding the `--dry-run` flag, you can find and fix any issues that the preflight checks find with your user cluster before the upgrade.

### Run `gkectl upgrade cluster`

There are two variations of the `gkectl upgrade cluster` command:

  * **Asynchronous** : (recommended)   
With the asynchronous variation, the command starts the upgrade and then completes. You don't need to watch the output of the command for the entire duration of the upgrade. Instead, you can periodically check on the upgrade progress by running `gkectl list clusters` and `gkectl describe clusters`. To use the asynchronous variation, include the `--async` flag in the command.

    * Version 1.31: Not available on advanced clusters.
    * Version 1.32 and higher: Available on advanced clusters.
  * **Synchronous** :   
With the synchronous variation, the `gkectl upgrade cluster` command outputs status messages to the admin workstation as the upgrade progresses.




### Asynchronous upgrade

  1. Skip this step if you are upgrading to a version later than 1.16.

If you are using [prepared credentials](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#preparedsecrets-namespace-field) and a [private registry](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#privateregistry-section) for the user cluster, make sure the private registry credential is prepared before upgrading the user cluster. For information on how to prepare the private registry credential, see [Configure prepared credentials for user clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/prepared-credentials).

  2. Diagnose your cluster to make sure it is healthy:
         
         gkectl diagnose cluster \
           --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         

     * If the command reports any errors or warnings, refer to [Diagnose cluster issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose#diagnose_user_cluster) and resolve them before proceeding.
  3. On your admin workstation, start an asynchronous upgrade:
         
         gkectl upgrade cluster \
           --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
           --config USER_CLUSTER_CONFIG \
           --async
         

The preceding command completes, and you can continue to use your admin workstation while the upgrade is in progress.

  4. To see the status of the upgrade:
         
         gkectl list clusters --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         

The output shows a value for the cluster `STATE`. If the cluster is still upgrading, the value of `STATE` is `UPGRADING`. For example:
         
         NAMESPACE             NAME    READY   STATE       AGE   VERSION
         my-uc-gkeonprem-mgmt  my-uc   False   UPGRADING   9h    1.36.0-gke.1
         

The possible values for `STATE` are `UPGRADING`, `DELETING`, `UPDATING`, `RUNNING`, `RECONCILING`, `ERROR`, and `UNKNOWN`.

  5. To get more details about the upgrade progress and cluster events:
         
         gkectl describe clusters --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
           --cluster USER_CLUSTER_NAME -v 5
         

The output shows the OnPremUserCluster custom resource for the specified user cluster, which includes cluster status, conditions, and events.

Click to view the example output
         
         Status:
             Cluster State:  RUNNING
             Conditions:
               Last Transition Time:    2026-08-10T21:29:07Z
               Message:                 Cluster is running
               Observed Generation:     2
               Reason:                  ClusterRunning
               Status:                  True
               Type:                    Ready
               Last Transition Time:    2026-08-10T21:12:05Z
               Message:                 Operator NodePool is ready
               Observed Generation:     2
               Reason:                  OperatorNodePoolReady
               Status:                  True
               Type:                    ControlPlaneReady
               Last Transition Time:    2026-08-10T16:25:08Z
               Message:                 Component provisioner job is completed
               Observed Generation:     2
               Reason:                  ComponentProvisionerJobCompleted
               Status:                  True
               Type:                    ComponentProvisionerUserProfileInstalled
               Last Transition Time:    2026-08-10T21:29:07Z
               Message:                 Node pools are running
               Observed Generation:     2
               Reason:                  NodePoolsRunning
               Status:                  True
               Type:                    NodePoolsReady
               Last Transition Time:    2026-08-10T21:29:56Z
               Message:
               Observed Generation:     2
               Reason:                  Reconciling
               Status:                  False
               Type:                    OperatorClusterKubeProxyCleanedUp
               Last Transition Time:    2026-08-10T16:27:48Z
               Message:
               Observed Generation:     2
               Reason:                  PreflightCheckPassed
               Status:                  True
               Type:                    OperatorClusterPreflightCheckSuccessful
               Last Transition Time:    2026-08-10T16:27:48Z
               Message:
               Observed Generation:     2
               Reason:                  ProvisioningStarted
               Status:                  True
               Type:                    OperatorClusterProvisioningStarted
               Last Transition Time:    2026-08-10T16:27:48Z
               Message:
               Observed Generation:     2
               Reason:                  RemoteTrackerSetupComplete
               Status:                  True
               Type:                    OperatorClusterRemoteTrackerSetupSuccessful
               Last Transition Time:    2026-08-10T16:27:48Z
               Message:
               Observed Generation:     2
               Reason:                  Reconciling
               Status:                  False
               Type:                    OperatorClusterStalled
               Last Transition Time:    2026-08-10T16:27:48Z
               Message:
               Observed Generation:     2
               Reason:                  NotPresent
               Status:                  False
               Type:                    OperatorClusterWaitingOnPendingClusterID
               Last Transition Time:    2026-08-10T18:23:16Z
               Message:                 Operator Cluster is ready
               Observed Generation:     2
               Reason:                  OperatorClusterReady
               Status:                  True
               Type:                    OperatorClusterReady
             Gke On Prem Version:       1.36.0-gke.527
             Last Gke On Prem Version:  1.35.300-gke.87
             Operator Cluster Status:
               Control Plane Node Pool Status:
                 Anthos Bare Metal Version:  1.36.0-gke.527
                 Anthos Bare Metal Versions:
                   1.36.0-gke.527:  3
                 Conditions:
                   Last Transition Time:  2026-08-10T21:07:22Z
                   Observed Generation:   11
                   Reason:                PreflightCheckPassed
                   Status:                True
                   Type:                  PreflightCheckSuccessful
                   Last Transition Time:  2026-08-10T21:12:05Z
                   Observed Generation:   11
                   Reason:                NodepoolReady
                   Status:                True
                   Type:                  Ready
                   Last Transition Time:  2026-08-10T21:11:24Z
                   Observed Generation:   11
                   Reason:                ReconciliationCompleted
                   Status:                False
                   Type:                  Reconciling
                 Gke Versions:
                   v1.36.0-gke.2800:        3
                 Last Reconciliation Time:  2026-08-10T21:28:02Z
                 Maintenance Nodes:         0
                 Managed Fields:
                   Label Keys:
                     node.kubernetes.io/control-plane
                     node.kubernetes.io/master
                   Node Label Keys:
                     vsphere://abcdef-1:
                       onprem.gke.io/failure-domain-name
                       vmware.cluster.gke.io/machine-name
                     vsphere://abcdef-2:
                       onprem.gke.io/failure-domain-name
                       vmware.cluster.gke.io/machine-name
                     vsphere://abcdef-3:
                       onprem.gke.io/failure-domain-name
                       vmware.cluster.gke.io/machine-name
                 Ready Nodes:        3
                 Ready Timestamp:    2026-08-10T16:24:02Z
                 Reconciling Nodes:  0
                 Stalled Nodes:      0
                 Unknown Nodes:      0
               Data Plane Load Balancer Status:
                 Conditions:
                   Last Transition Time:  2026-08-10T16:08:47Z
                   Observed Generation:   1
                   Reason:                ReconciliationCompleted
                   Status:                False
                   Type:                  Reconciling
                 Node Pool Location:      load-balancer-nodepool
               External Manifests Conditions:
                 Last Transition Time:  2026-08-10T16:12:25Z
                 Observed Generation:   2
                 Reason:                ReconciliationCompleted
                 Status:                False
                 Type:                  Reconciling
               Gke Connect Conditions:
                 Last Transition Time:  2026-08-10T21:11:33Z
                 Observed Generation:   2
                 Reason:                AnthosBareMetalVersion
                 Status:                True
                 Type:                  1.36.0-gke.527
                 Last Transition Time:  2026-08-10T21:11:33Z
                 Observed Generation:   2
                 Reason:                ReconciliationCompleted
                 Status:                False
                 Type:                  Reconciling
               Gke Connect Dependent System Service Conditions:
                 Last Transition Time:  2026-08-10T16:25:26Z
                 Observed Generation:   2
                 Reason:                ReconciliationCompleted
                 Status:                False
                 Type:                  Reconciling
               Gke Hub Registration Status:
                 Membership:
                   Description:  description
                   Name:         name
               Gke Versions:
                 v1.36.0-gke.2800:  6
               Kernel Version Conditions:
                 Last Transition Time:  2026-08-10T16:08:53Z
                 Reason:                kernelVersionCheckPassed
                 Status:                True
                 Type:                  kernelVersionCheckSuccessful
               System Service Conditions:
                 Last Transition Time:  2026-08-10T21:04:39Z
                 Observed Generation:   2
                 Reason:                ReconciliationCompleted
                 Status:                False
                 Type:                  Reconciling
           Events:
             Type    Reason         Age   From                            Message
             ----    ------         ----  ----                            -------
             Normal  StatusChanged  58m   onprem-user-cluster-controller  OnPremUserCluster status changed:
             - New ClusterState condition: UPGRADING
             Normal  ControlPlaneUpgradeStarted  58m  onprem-user-cluster-controller  Creating or updating operator NodePool: NodePool is not ready: Condition "Ready" status "False" is not "True", reason: "Reconciling", message: "", lastTransitionTime: 2026-08-10 20:43:53 +0000 UTC
             Normal  StatusChanged               58m  onprem-user-cluster-controller  OnPremUserCluster status changed:
             - New Ready condition: False, CreateOrUpdateOperatorNodePool, Creating or updating operator NodePool: NodePool is not ready: Condition "Ready" status "False" is not "True", reason: "Reconciling", message: "", lastTransitionTime: 2026-08-10 20:43:53 +0000 UTC
             Normal  ControlPlaneUpgradeStarted  58m  onprem-user-cluster-controller  Creating or updating operator NodePool: NodePool is not ready: Condition "Ready" status "False" is not "True", reason: "Reconciling", message: "", lastTransitionTime: 2026-08-10 20:43:54 +0000 UTC
             Normal  StatusChanged               58m  onprem-user-cluster-controller  OnPremUserCluster status changed:
             - New Ready condition: False, CreateOrUpdateOperatorNodePool, Creating or updating operator NodePool: NodePool is not ready: Condition "Ready" status "False" is not "True", reason: "Reconciling", message: "", lastTransitionTime: 2026-08-10 20:43:54 +0000 UTC
             Normal  ControlPlaneUpgradeStarted  58m  onprem-user-cluster-controller  Creating or updating operator NodePool: NodePool is not ready: Condition "Ready" status "False" is not "True", reason: "Reconciling", message: "", lastTransitionTime: 2026-08-10 20:44:38 +0000 UTC
             Normal  StatusChanged               58m  onprem-user-cluster-controller  OnPremUserCluster status changed:
             - New Ready condition: False, CreateOrUpdateOperatorNodePool, Creating or updating operator NodePool: NodePool is not ready: Condition "Ready" status "False" is not "True", reason: "Reconciling", message: "", lastTransitionTime: 2026-08-10 20:44:38 +0000 UTC
             Normal  StatusChanged  56m  onprem-user-cluster-controller  OnPremUserCluster status changed:
             - New Ready condition: False, CreateOrUpdateOperatorNodePool, Creating or updating operator NodePool: NodePool is not ready: Condition "Ready" status "False" is not "True", reason: "Reconciling", message: "", lastTransitionTime: 2026-08-10 20:46:33 +0000 UTC
             Normal  StatusChanged  54m (x2 over 56m)  onprem-user-cluster-controller  OnPremUserCluster status changed:
             - New Ready condition: False, CreateOrUpdateOperatorNodePool, Creating or updating operator NodePool: NodePoolClaim is currently in the progress of rolling update: Condition "NodeRecreationUpdateInProgress" ready, reason: "NodeRecreationUpdateInProgress", message: "Cannot further mark old InventoryMachines for recreation due to MinReadyNodesRequired requirement. Current process: There are still old InventoryMachines: [ci-4b6217b4ff2afdab2be082ab3b349e66-cp-99cc4wxzvx8ww829-2 ci-4b6217b4ff2afdab2be082ab3b349e66-cp-99cc4wxzvx8ww829-1]; New ready count (0) does not match desired count (3)"
             Normal  StatusChanged  53m  onprem-user-cluster-controller  OnPremUserCluster status changed:
             - New Ready condition: False, CreateOrUpdateOperatorNodePool, Creating or updating operator NodePool: NodePool is not ready: Condition "Ready" generation 7 hasn't been observed
             Normal  StatusChanged  53m  onprem-user-cluster-controller  OnPremUserCluster status changed:
             - New Ready condition: False, CreateOrUpdateOperatorNodePool, Creating or updating operator NodePool: NodePool is not ready: Condition "Ready" status "False" is not "True", reason: "Reconciling", message: "", lastTransitionTime: 2026-08-10 20:48:58 +0000 UTC
             Normal  StatusChanged  30m (x3 over 58m)  onprem-user-cluster-controller  OnPremUserCluster status changed:
             - New Ready condition: True, ClusterRunning, Cluster is running
             Normal  ControlPlaneUpgradeFinished  30m (x3 over 58m)  onprem-user-cluster-controller  Operator NodePool is ready
             Normal  StatusChanged                29m (x9 over 47m)  onprem-user-cluster-controller  (combined from similar events): OnPremUserCluster status changed:
             - New Ready condition: False, CreateOrUpdateNodePools, Creating or updating node pools, unready node pools: [ci-4b6217b4ff2afdab2be082ab3b349e66-gke-onprem-mgmt/ci-4b6217b4ff2afdab2be082ab3b349e66], in deletion node pools: []
             Normal  NodePoolsUpgradeStarted  29m  onprem-user-cluster-controller  Creating or updating node pools, unready node pools: [ci-4b6217b4ff2afdab2be082ab3b349e66-gke-onprem-mgmt/ci-4b6217b4ff2afdab2be082ab3b349e66], in deletion node pools: []
             Normal  StatusChanged            13m  onprem-user-cluster-controller  OnPremUserCluster status changed:
             - New GKEOnPremVersion: "1.36.0-gke.527"
             - New ClusterState condition: RUNNING
             - New Ready condition: True, ClusterRunning, Cluster is running
           

  6. When the upgrade is complete, `gkectl list clusters` shows a `STATUS` of `RUNNING`:
         
         NAMESPACE             NAME    READY   STATE     AGE     VERSION
         my-uc-gkeonprem-mgmt  my-uc   True    RUNNING   9h      1.36.0-gke.1
         

Also, when the upgrade is complete, `gkectl describe clusters` shows a `Last GKE On Prem Version` field under `Status`. For example:
         
         Status:
         Cluster State:  RUNNING
         Last GKE On Prem Version:  1.36.0-gke.1
         




### Troubleshoot asynchronous upgrade

For an asynchronous upgrade, the timeout duration is based on the number of nodes in the cluster. If the upgrade takes longer than the timeout duration, the cluster state is changed from `UPGRADING` to `ERROR`, with an event saying that the upgrade operation timed out. Note that the `ERROR` state here means the upgrade is taking longer than expected, but has not been terminated. The controller continues the reconciliation and keeps retrying the operation.

Usually a timeout is the result of a deadlock caused by a PodDisruptionBudget (PDB). In that case, Pods cannot be evicted from old nodes, and the old nodes cannot be drained. If the Pod eviction takes longer than 10 minutes, we write an event to the OnPremUserCluster object. You can capture the event by running `gkectl describe clusters`. Then you can adjust the PDB to allow the node to drain. After that, the upgrade can proceed and eventually complete.

Example event:
    
    
    Warning  PodEvictionTooLong  96s (x2 over 4m7s)  onprem-user-cluster-controller
    Waiting too long(>10m0.00000003s) for (kube-system/coredns-856d6dbfdf-dl6nz) eviction.
    

In addition, when an upgrade is blocked or fails, you can run `gkectl diagnose` to check for common cluster issues. Based on the result, you can decide whether to perform a manual fix or contact the Anthos support team for further assistance.

### Synchronous upgrade

The `gkectl upgrade` command runs preflight checks. If the preflight checks fail, the command is blocked. You must fix the failures, or use the `--skip-preflight-check-blocking` flag. You should only skip the preflight checks if you are confident there are no critical failures.

Proceed with these steps on your admin workstation:

  1. Skip this step if you are upgrading to a version later than 1.16.

If you are using [prepared credentials](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#preparedsecrets-namespace-field) and a [private registry](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#privateregistry-section) for the user cluster, make sure the private registry credential is prepared before upgrading the user cluster. For information on how to prepare the private registry credential, see [Configure prepared credentials for user clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/prepared-credentials).




  1. Diagnose your cluster to make sure it is healthy:
         
         gkectl diagnose cluster   
         
               --kubeconfig ADMIN_CLUSTER_KUBECONFIG   
         
               --config USER_CLUSTER_CONFIG
           

     * If the command reports any errors or warnings, refer to [Diagnose cluster issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose#diagnose_user_cluster) and resolve them before proceeding.
     1. Upgrade the cluster:
            
            gkectl upgrade cluster \
              --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
              --config USER_CLUSTER_CONFIG
            

     2. If you are upgrading to version 1.14.0 or higher, a new kubeconfig file is generated for the user cluster that overwrites any existing file. To view cluster details in the file, run the following command:
            
            kubectl config view --kubeconfig USER_CLUSTER_KUBECONFIG




## Resume an upgrade

If a user cluster upgrade is interrupted, you can resume the user cluster upgrade by running the same upgrade command with the `--skip-validation-all` flag:
    
    
    gkectl upgrade cluster \
        --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
        --config USER_CLUSTER_CONFIG \
        --skip-validation-all
    

### Console

Upgrading a user cluster requires some changes to the admin cluster. The console automatically does the following:

  * [Enrolls the admin cluster in the GKE On-Prem API](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster) if it isn't already enrolled.

  * Downloads and deploys a bundle of components to the admin cluster. The version of the components matches the version you specify for the upgrade. These components let the admin cluster manage user clusters at that version.




To upgrade a user cluster:

  1. In the console, go to the **Google Kubernetes Engine clusters overview** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Select the Google Cloud project, and then select the cluster that you want to upgrade.

  3. In the **Details** panel, click **More details**.

  4. In the **Cluster basics** section, click edit **Upgrade**.

  5. In the **Choose target version** list, select the version that you want to upgrade to. The curated list contains only the latest patch releases.

  6. Click **Upgrade**.




Before the cluster is upgraded, preflight checks run to validate cluster status and node health. If the preflight checks pass, the user cluster is upgraded. It takes about 30 minutes for the upgrade to complete.

To view the status of the upgrade, click **Show Details** on the **Cluster Details** tab.

###  gcloud CLI 

Upgrading a user cluster requires some changes to the admin cluster. The the `gcloud container vmware clusters upgrade` command automatically does the following:

  * [Enrolls the admin cluster in the GKE On-Prem API](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster) if it isn't already enrolled.

  * Downloads and deploys a bundle of components to the admin cluster. The version of the components matches the version you specify for the upgrade. These components let the admin cluster manage user clusters at that version.




To upgrade a user cluster:

  1. Update the Google Cloud CLI components:
         
         gcloud components update
         

  2. Get a list of available versions to upgrade to:
         
         gcloud container vmware clusters query-version-config \
           --cluster=USER_CLUSTER_NAME \
           --project=PROJECT_ID \
           --location=REGION
         

The output of the command is similar to the following:
         
         versions:
         - version: 1.16.3-gke.45
         - version: 1.16.2-gke.28
         - version: 1.16.1-gke.45
         - version: 1.16.0-gke.669
         - version: 1.15.6-gke.25
         - version: 1.15.5-gke.41
         
         An Anthos version must be made available on the admin cluster ahead of the user
         cluster creation or upgrade. Versions annotated with isInstalled=true are
         installed on the admin cluster for the purpose of user cluster creation or
         upgrade whereas other version are released and will be available for upgrade
         once dependencies are resolved.
         
         To install the version in the admin cluster, run:
         $ gcloud container vmware admin-clusters update my-admin-cluster --required-platform-version=VERSION
         

You can ignore the message after the list of versions. It doesn't matter if the version that you are upgrading to is installed on the admin cluster. The `upgrade` command downloads and deploys a bundle of the components that matches the version you specify in the `upgrade` command.

  3. Upgrade the cluster.
         
         gcloud container vmware clusters upgrade USER_CLUSTER_NAME \
           --project=PROJECT_ID \
           --location=REGION \
           --version=VERSION
         

Replace VERSION with the Google Distributed Cloud version that you want to upgrade to. Specify a version from the output of the previous command. We recommend that you upgrade to the most recent patch version.

The output from the command is similar to the following:
         
         Waiting for operation [projects/example-project-12345/locations/us-west1/operations/operation-1679543737105-5f7893fd5bae9-942b3f97-75e59179] to complete.
         

In the example output, the string `operation-1679543737105-5f7893fd5bae9-942b3f97-75e59179` is the OPERATION_ID of the long-running operation. You can find out the status of the operation by running the following command in another terminal window:
         
         gcloud container vmware operations describe OPERATION_ID \
           --project=PROJECT_ID \
           --location=REGION
         




### Terraform

  1. Update the Google Cloud CLI components:
         
         gcloud components update
         

  2. If you haven't already, [enroll the admin cluster in the GKE On-Prem API](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster). After the cluster is enrolled in the GKE On-Prem API, you don't need to do this step again.

  3. Get a list of available versions to upgrade to:
         
         gcloud container vmware clusters query-version-config \
           --cluster=USER_CLUSTER_NAME \
           --project=PROJECT_ID \
           --location=REGION
         

Replace the following:

     * `USER_CLUSTER_NAME`: The name of the user cluster.

     * `PROJECT_ID`: The ID of the fleet project in which that user cluster is a member. This is the project that you specified when the cluster was created. If you created the cluster using `gkectl`, this is the project ID in the `gkeConnect.projectID` field in the cluster configuration file.

     * `REGION`: The Google Cloud region in which the GKE On-Prem API runs and stores its metadata. In the `main.tf` file that you used to create the user cluster, the region is in the `location` field of the cluster resource.

The output of the command is similar to the following:
    
    versions:
    - version: 1.16.3-gke.45
    - version: 1.16.2-gke.28
    - version: 1.16.1-gke.45
    - version: 1.16.0-gke.669
    - version: 1.15.6-gke.25
    - version: 1.15.5-gke.41
    
    An Anthos version must be made available on the admin cluster ahead of the user
    cluster creation or upgrade. Versions annotated with isInstalled=true are
    installed on the admin cluster for the purpose of user cluster creation or
    upgrade whereas other version are released and will be available for upgrade
    once dependencies are resolved.
    
    To install the version in the admin cluster, run:
    $ gcloud container vmware admin-clusters update my-admin-cluster --required-platform-version=VERSION
    

  4. Download the new version of the components and deploy them in the admin cluster:
         
         gcloud container vmware admin-clusters update ADMIN_CLUSTER_NAME \
           --project=PROJECT_ID \
           --location=REGION \
           --required-platform-version=VERSION
         

This command downloads the version of the components that you specify in `--required-platform-version` to the admin cluster, and then deploys the the components. These components let the admin cluster manage user clusters at that version.

  5. In the `main.tf` file that you used to create the user cluster, change `on_prem_version` in the cluster resource to the new version.

  6. Initialize and create the Terraform plan:
         
         terraform init
         

Terraform installs any needed libraries, such as the Google Cloud provider.

  7. Review the configuration and make changes if needed:
         
         terraform plan
         

  8. Apply the Terraform plan to create the user cluster:
         
         terraform apply
         




## Remove the full bundle

If you downloaded a full bundle, and you have successfully run `gkectl prepare` and upgraded the admin cluster and all user clusters, you should delete the full bundle to save disk space on the admin workstation. Run the following command to delete the full bundle:
    
    
    rm /var/lib/gke/bundles/gke-onprem-vsphere-TARGET_VERSION-full.tgz
    

## Resuming an admin cluster upgrade

If an admin cluster upgrade is interrupted or fails, the upgrade can be resumed if the [admin cluster checkpoint](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-cluster#managing_the_checkpointyaml_file) contains the state required to restore the state prior to the interruption.

**Warning** : Don't repair the admin master with `gkectl repair admin-master` after a failed upgrade attempt. This will cause the admin cluster to get into a bad state.

Follow these steps:

  1. Check if the admin control plane is healthy before you begin the initial upgrade attempt. See [Diagnosing cluster issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose). As discussed in that topic, run the `gkectl diagnose cluster` command for the admin cluster.

  2. If the admin control plane is unhealthy prior to the initial upgrade attempt, [repair the admin control plane](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/repair-admin-control-plane) with the `gkectl repair admin-master` command.

  3. When you rerun the upgrade command after an upgrade has been interrupted or has failed, use the same bundle and target version as you did in the previous upgrade attempt.




When you rerun the upgrade command, the resumed upgrade recreates admin cluster state from the checkpoint and reruns the entire upgrade. Starting from 1.12.0, if the admin control plane is unhealthy, the upgrade process will directly upgrade to the target version without trying to restore the admin cluster at the source version before proceeding to upgrade.

The upgrade will resume from the point where it failed or exited if the admin cluster checkpoint is available. If the checkpoint is unavailable, the upgrade will fall back to relying on the admin control plane, and therefore the admin control plane must be healthy in order to proceed with the upgrade. After a successful upgrade, the checkpoint is regenerated.

If `gkectl` exits unexpectedly during an admin cluster upgrade, the kind cluster is not cleaned up. Before you rerun the upgrade command to resume the upgrade, delete the kind cluster:
    
    
    docker stop gkectl-control-plane && docker rm gkectl-control-plane
    

After deleting the kind cluster, rerun the upgrade command again.

## Roll back an admin workstation after an upgrade

You can roll back the admin workstation to the version used before the upgrade.

During the upgrade, `gkeadm` records the version before it was upgraded in the output information file. During the rollback, `gkeadm` uses the version listed to download the older file.

To roll back your admin workstation to the previous version:
    
    
    gkeadm rollback admin-workstation --config=AW_CONFIG_FILE
    

You can omit `--config=AW_CONFIG_FILE` if your admin workstation configuration file is the default `admin-ws-config.yaml`. Otherwise, replace AW_CONFIG_FILE with the path to the admin workstation configuration file.

The rollback command performs these steps:

  1. Downloads the rollback version of `gkeadm`.
  2. Backs up the home directory of the current admin workstation.
  3. Creates a new admin workstation using the rollback version of `gkeadm`.
  4. Deletes the original admin workstation.



## Install bundle with a different version for upgrade

If you upgrade your workstation, a bundle with a corresponding version is installed there for upgrading your clusters. If you want a different version, follow these steps to install a bundle for TARGET_VERSION, which is the version to which you want to upgrade.

  1. To check the current `gkectl` and cluster versions, run this command. Use the flag `--details/-d` for more detailed information.
         
         gkectl version --kubeconfig ADMIN_CLUSTER_KUBECONFIG --details
         

The output provides information about your cluster versions.

  2. Based on the output you get, look for the following issues, and fix them as needed.

     * If the current admin cluster version is more than one minor version lower than the TARGET_VERSION, upgrade all your clusters to be one minor version lower than the TARGET_VERSION.

     * If the `gkectl` version is lower than 1.11, and you want to upgrade to 1.12.x, you will have to perform multiple upgrades. Upgrade one minor version at a time, until you get to 1.11.x, and then proceed with the instructions in this topic.

     * If the `gkectl` version is lower than the TARGET_VERSION, upgrade the admin workstation to the TARGET_VERSION.

  3. When you have determined that your `gkectl` and cluster versions are appropriate for an upgrade, download the bundle.

Check whether the bundle tarball already exists on the admin workstation.
         
         stat /var/lib/gke/bundles/gke-onprem-vsphere-TARGET_VERSION.tgz

If the bundle is not on the admin workstation, download it. 
         
         gcloud storage cp gs://gke-on-prem-release/gke-onprem-bundle/TARGET_VERSION/gke-onprem-vsphere-TARGET_VERSION.tgz /var/lib/gke/bundles/
         

  4. Install the bundle.
         
         gkectl prepare --bundle-path /var/lib/gke/bundles/gke-onprem-vsphere-TARGET_VERSION.tgz --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         

Replace ADMIN_CLUSTER_KUBECONFIG with the path of your kubeconfig file. You can omit this flag if the file is in your current directory and has the name `kubeconfig`.

**Note:** By default, the regular bundle, rather than the full bundle, is downloaded. The full bundle contains all of the container and VM images, whereas the regular bundle downloads the container and VM images from Google Cloud Platform on to the admin workstation during installation. To use the full bundle instead, the bundle path in the installation command is `gke-onprem-vsphere-TARGET_VERSION-full.tgz`.
  5. List available cluster versions, and make sure the target version is included in the available user cluster versions.
         
         gkectl version --kubeconfig ADMIN_CLUSTER_KUBECONFIG --details




You can now create a user cluster at the target version, or upgrade a user cluster to the target version.

## Troubleshooting the upgrade process

If you experience an issue when following the recommended upgrade process, follow these recommendations to resolve them. These suggestions assume that you have begun with a version 1.11.x setup, and are proceeding through the recommended upgrade process.

See also: [Troubleshooting cluster creation and upgrade](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/create-upgrade)

### Troubleshooting a user cluster upgrade issue

Suppose you find an issue with the upgrade version when upgrading a user cluster. You determine from Google Support that the issue will be fixed in an upcoming patch release. You can proceed as follows:

  1. Continue using the current version for production.
  2. Test the patch release in a non-production cluster when it is released.
  3. Upgrade all production user clusters to the patch release version when you are confident.
  4. Upgrade the admin cluster to the patch release version.



### Troubleshooting an admin cluster upgrade issue

If you encounter an issue when upgrading the admin cluster, you must contact Google Support to resolve the issue with the admin cluster.

In the meantime, with the new upgrade flow, you can still benefit from new user cluster features without being blocked by the admin cluster upgrade, which allows you to reduce the upgrade frequency of the admin cluster if you want. Your upgrade process can proceed as follows:

  1. Upgrade production user clusters to 1.12.x.
  2. Keep the admin cluster at its earlier version and continue receiving security patches.
  3. Test admin cluster upgrade from 1.11.x to 1.12.x in a test environment, and report issues if there are any;
  4. If your issue is solved by a 1.12.x patch release, you can then choose to upgrade the production admin cluster to this patch release if desired.



## Known issues for recent versions

The following known issues might affect upgrades if you are upgrading from version 1.7 or later.

See also: [Known issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/known-issues)

### Upgrading the admin workstation might fail if the data disk is nearly full

If you upgrade the admin workstation with the `gkectl upgrade admin-workstation` command, the upgrade might fail if the data disk is nearly full, because the system attempts to back up the current admin workstation locally while upgrading to a new admin workstation. If you cannot clear sufficient space on the data disk, use the `gkectl upgrade admin-workstation` command with the additional flag `--backup-to-local=false` to prevent making a local backup of the current admin workstation.

### Disruption for workloads with PodDisruptionBudgets

Upgrading clusters can cause disruption or downtime for workloads that use [PodDisruptionBudgets](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) (PDBs).

### Nodes fail to complete their upgrade process

If you have `PodDisruptionBudget` objects configured that are unable to allow any additional disruptions, node upgrades might fail to upgrade to the control plane version after repeated attempts. To prevent this failure, we recommend that you scale up the `Deployment` or `HorizontalPodAutoscaler` to allow the node to drain while still respecting the `PodDisruptionBudget` configuration.

To see all `PodDisruptionBudget` objects that do not allow any disruptions:
    
    
    kubectl get poddisruptionbudget --all-namespaces -o jsonpath='{range .items[?(@.status.disruptionsAllowed==0)]}{.metadata.name}/{.metadata.namespace}{"\n"}{end}'
    

## Appendix

### About VMware DRS rules enabled in version 1.1.0-gke.6

As of version 1.1.0-gke.6, Google Distributed Cloud automatically creates VMware [Distributed Resource Scheduler](https://www.vmware.com/products/vsphere/drs-dpm.html) (DRS) anti-affinity rules for your user cluster's nodes, causing them to be spread across at least three physical hosts in your datacenter. As of version 1.1.0-gke.6, this feature is automatically enabled for new clusters and existing clusters.

Before you upgrade, be sure that your vSphere environment meets the following conditions:

  * VMware DRS is enabled. VMware DRS requires vSphere Enterprise Plus license edition. To learn how to enable DRS, see [Enabling VMware DRS in a cluster](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-resource-management/creating-a-drs-cluster/edit-cluster-settings.html).

  * The vSphere username provided in your [credentials configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/credentials-configuration-file) has the `Host.Inventory.EditCluster` permission.

  * There are at least three physical hosts available.




If your vSphere environment does not meet the preceding conditions, you can still upgrade, but for upgrading a user cluster from 1.3.x to 1.4.x, you need to disable anti-affinity groups. For more information, see this [known issue](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/release-notes#40c10ea4) in the Google Distributed Cloud release notes.

### About downtime during upgrades

Resource | Description  
---|---  
Admin cluster | When an admin cluster is down, user cluster control planes and workloads on user clusters continue to run, unless they were affected by a failure that caused the downtime.  
User cluster control plane | Typically, you should expect no noticeable downtime to user cluster control planes. However, long-running connections to the Kubernetes API server might break and would need to be re-established. In those cases, the API caller should retry until it establishes a connection. In the worst case, there can be up to one minute of downtime during an upgrade. **Note:** If user cluster nodes are unable to reach the user control plane during the upgrade, new workloads are not scheduled to the cluster. Existing workloads are unaffected.  
User cluster nodes | If an upgrade requires a change to user cluster nodes, Google Distributed Cloud recreates the nodes in a rolling fashion, and reschedules Pods running on these nodes. You can prevent impact to your workloads by configuring appropriate [PodDisruptionBudgets](https://kubernetes.io/docs/concepts/workloads/pods/disruptions) and [anti-affinity rules](https://kubernetes.io/docs/concepts/configuration/assign-pod-node).  
  
### Re-create an information file if missing

If the output information file for your admin workstation is missing, you must re-create this file so you can then proceed with the upgrade. This file was created when you initially created your workstation, and if you have since done an upgrade, it was updated with new information.

The output information file has this format:
    
    
    Admin workstation version: GKEADM_VERSION
    Created using gkeadm version: GKEADM_VERSION
    VM name: ADMIN_WS_NAME
    IP: ADMIN_WS_IP
    SSH key used: FULL_PATH_TO_ADMIN_WS_SSH_KEY
    To access your admin workstation:
    ssh -i FULL-PATH-TO-ADMIN-WS-SSH-KEY ubuntu@ADMIN-WS-IP
    

Here is a sample output information file:
    
    
    Admin workstation version: v1.10.3-gke.49
    Created using gkeadm version: v1.10.3-gke.49
    VM name: admin-ws-janedoe
    IP: 172.16.91.21
    SSH key used: /usr/local/google/home/janedoe/.ssh/gke-admin-workstation
    Upgraded from (rollback version): v1.10.0-gke.194
    To access your admin workstation:
    ssh -i /usr/local/google/home/janedoe/.ssh/gke-admin-workstation ubuntu@172.16.91.21
    

Create the file in an editor, substituting the appropriate parameters. Save the file with a filename that is the same as the VM name in the directory from which gkeadm is run. For example, if the VM name is `admin-ws-janedoe`, save the file as `admin-ws-janedoe`.

## What's next

  * gcloud CLI reference documentation

    * [`gcloud container vmware clusters`](https://docs.cloud.google.com/sdk/gcloud/reference/container/vmware/clusters)
    * [`gcloud container vmware node-pools`](https://docs.cloud.google.com/sdk/gcloud/reference/container/vmware/node-pools)
    * [gcloud container vmware admin-clusters](https://cloud.google.com/sdk/gcloud/reference/container/vmware/admin-clusters)
  * Terraform reference documentation

    * [`google_gkeonprem_vmware_cluster`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gkeonprem_vmware_cluster)
    * [`google_gkeonprem_vmware_node_pool`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gkeonprem_vmware_node_pool)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
