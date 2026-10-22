---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/advanced-clusters/
title: Advanced clusters \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:34.357009+00:00
---

# Advanced clusters  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/advanced-clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Advanced clusters Stay organized with collections  Save and categorize content based on your preferences. 

This document provides information about the advanced clusters feature and the implications of enabling it. The advanced clusters feature is available for Preview for version 1.31 admin clusters and user clusters. The advanced clusters feature is in GA for version 1.32 admin clusters and user clusters and higher.

Note the following differences between versions:

  * In version 1.31, the advanced cluster feature is in preview.

    * You can enable advanced cluster at cluster creation time for new 1.31 clusters only.

    * After advanced cluster is enabled, you won't be able to upgrade the cluster to 1.32. Only enable advanced cluster in a test environment.

  * In version 1.32, the advanced cluster feature is GA.

    * By default, clusters are created as advanced clusters. You have to explicitly set `enableAdvancedCluster` to `false` in the cluster configuration file if you want to create a non-advanced cluster.

    * For clusters that have the advanced clusters feature enabled, cluster upgrades are supported.

  * Starting with version 1.33, advanced clusters are the standard for all new clusters you create. If you set `enableAdvancedCluster` to `false`, cluster creation fails.

  * If you upgrade existing non-advanced clusters to version 1.33, by default, the system automatically converts them to advanced clusters. When upgrading to version 1.33, you have the option to have the cluster remain non-advanced. For details, see [Upgrade a version 1.32 non-advanced cluster and keep it as non-advanced](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-maintain-non-advanced-cluster).

  * Keeping a cluster as non-advanced is supported only for upgrades from version 1.32 to 1.33. When you upgrade a non-advanced cluster from version 1.33 to 1.34, the cluster is always converted to an advanced cluster.

  * You must use the `gkectl` command line tool to upgrade non-advanced clusters to version 1.33 or later. The GKE On-Prem API clients, Terraform, the Google Cloud console, and the gcloud CLI, aren't supported.

  * About `cert-manager` installation: `cert-manager` is automatically installed on advanced clusters. When you migrate from a non-advanced cluster to an advanced cluster, the integrated `cert-manager` automatically overrides any customer-installed versions of `cert-manager`. Make sure you don't have critical custom configurations or features applied to your existing `cert-manager` before you update or upgrade to advanced clusters. For more information, see [Upgrade to `cert-manager` bundled with advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/update-or-upgrade-to-adv-cluster#upgrade-cert-manager).

**Note:** Advanced clusters use a consolidated Google Distributed Cloud architecture by using Google Distributed Cloud for Bare Metal as the underlying framework for Google Distributed Cloud for VMware. You might see references to "bare metal" in node labels, API resources, and system tags.

This page is for Admins and architects who define IT solutions and system architecture in accordance with company strategy, and create and manage policies related to user permissions. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Consistent experience and implementation

The advanced clusters feature implements a cluster architecture that better aligns Google Distributed Cloud for VMware with the rest of the Google Distributed Cloud products. A cluster that has advanced clusters enabled has a shared platform with other Google Distributed Cloud clusters. This shared platform uses the same controllers and agents, which increases reliability and can help Google provide better support. There's also improved performance for cluster operations when advanced clusters is enabled.

The new architecture brings a consistent experience and implementation with all other Google Distributed Cloud offerings, and you can benefit from feature parity with other Google Distributed Cloud offerings in the long run.

## Access to new features

You enable advanced clusters to access the latest features and capability, such as [topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up), which gives you better control over how your workloads are distributed across your cluster nodes.

In future minor releases, advanced features, such as topology domains, are available for advanced clusters only.

## Differences when running advanced clusters

When you enable advanced clusters, some features or capabilities might not work the same as they do for clusters without the feature enabled. Some of these changes apply only while the feature is in Preview. The differences are noted throughout the documentation, where relevant.

The following table lists the features supported for Google Distributed Cloud for VMware, their availability status when advanced clusters is enabled , and any differences in behavior or use:

Make a selectionNo differencesChanges applyNot supportedNot recommendedDeprecatedFeature/capability | **1.31 Adv. clusters (Preview)** | **1.32 Not enabled** | **1.32 Advanced clusters (GA)** | **1.33 Advanced clusters (GA)** | **Differences**  
---|---|---|---|---|---  
[Advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/advanced-clusters) | **Preview** | GA | GA | GA | Not supported  
[Topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up) | **Preview** |  | **Preview** | **Preview** | Changes apply. For more information see [Set up topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up) and related cluster configuration references.  
[Regional fleet membership](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#gkeconnect-location-field) | GA | GA | GA | GA | No differences.  
[Version skew n+2 admin cluster - user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-overview#version_skew) |  | GA | GA | GA | Not recommended: Since we don't support managing a lower version preview user cluster, this feature shouldn't be used.  
[Version skew n+2 node pool - user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-overview#version_skew) |  | GA | GA | GA | Not recommended: Since we don't support managing a lower version preview user cluster, this feature shouldn't be used.  
[Max surge setting for node pool updates](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#nodepool-updatestrategy-rollingupdate-maxsurge-field) | **Preview** | **Preview** | **Preview** | **Preview** | No differences.  
[cgroup v2 for nodes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#nodepool-osimagetype-field) | GA | GA | GA | GA | No differences.  
[DSR mode for Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#dataplanev2-forwardmode-field) | GA | GA | GA | GA | No differences.  
[BinAuthz for Controlplane V2 user clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/binary-authorization-policy) | GA | GA | GA | GA | No differences.  
[User-managed admin workstation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-workstation) | GA | GA | GA | GA | No differences.  
[StatefulSet CSI migration tool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/using-statefulset-csi-migration-tool) | GA | GA | GA | GA | No differences.  
[Seesaw to MetalLB migration](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-seesaw-metallb) | GA | GA | GA | GA | No differences.  
[Disable bundled ingress](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/disable-bundled-ingress) | GA | GA | GA | GA | No differences.  
[Admin cluster prepared credentials](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/prepared-credentials-admin) |  | GA | GA | GA | No differences.  
[Storage policy for a user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/configure-storage-policy) | GA | GA | GA | GA | No differences.  
[Storage policy for an admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/configure-storage-policy) | GA | GA | GA | GA | No differences.  
[Node auto repair](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-auto-repair) | GA | GA | GA | GA | Changes apply: If advanced cluster is enabled, the periodic health checks aren't run as part of auto repair. For information and other differences, see [Automatic node repair and health checking](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-auto-repair).  
[High availability admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-cluster) | GA | GA | GA | GA | No differences.  
[VM host affinity](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/configure-vm-host-affinity) |  | GA | GA | GA | Supported on advanced clusters in version 1.32.200 and 1.33 and later. When you use [topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up), configure host groups in [`topologyDomains[i].compute.hostGroups`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/vsphere-infrastructure-configuration-file#topology-domains-compute-host-groups) in the vSphere infrastructure configuration file instead of `nodePools[i].vsphere.hostgroups` in the user cluster configuration file.  
[Generate configuration files from an existing cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/get-configuration-file-from-cluster) | GA | GA | GA | GA | No differences.  
[Google Cloud Managed Service for Prometheus system metrics collection](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/logging-and-monitoring#using-managed-service-for-prometheus) | GA | GA | GA | GA | No differences.  
[Upgrade and rollback of nodepools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-node-pools) |  | GA | GA | GA | No differences.  
[Update private registry credentials](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/updating-cluster-credentials#update_private_registry_credentials) | GA | GA | GA | GA | No differences.  
[Admin cluster backup and restore with gkectl](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/back-up-and-restore-an-admin-cluster-with-gkectl) |  | **Preview** | **Preview** | GA | Changes apply. Updated the `gkectl` command for improved restoring of admin clusters and to support backing up and restoring user clusters. For more information, see [Back up and restore advanced clusters with gkectl](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/back-up-and-restore-advanced-cluster-with-gkectl)  
[User cluster nodepool autoscaling](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#nodepool-autoscaling-section) | GA | GA | GA | GA | No differences.  
[Cluster automatic node resizing](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-auto-resize) |  | GA |  | GA | No differences.  
[Multiple vSphere cluster support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/install-overview#2_set_up_your_vsphere_environment) | GA | GA | GA | GA | No differences.  
[Multiple vSphere data centers support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/install-overview#2_set_up_your_vsphere_environment) | GA | GA | GA | GA | No differences.  
[OpenID Connect (OIDC) support for authentication to clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/authentication) | GA | GA | GA | GA | No differences.  
[CA certificate rotation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ca-rotation) |  | GA | GA | GA | No differences.  
[Workload Identity Federation support](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/use-workload-identity) | GA | GA | GA | GA | No differences.  
[AIS with LDAP authentication support](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/ldap) | GA | GA | GA | GA | No differences.  
[Always-on secrets encryption without hardware security module (HSM)](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/always-on-secrets-encryption) |  | GA | GA | GA | No differences.  
[Update vCenter CA certificates with gkectl](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/update-vcenter-certificate) | GA | GA | GA | GA | No differences.  
[Egress NAT gateway](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/egress-nat-gateway) | GA | GA | GA | GA | No differences.  
[Admin cluster fleet registration](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#gkeconnect-section) | GA | GA | GA | GA | No differences.  
[Windows node pool support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-guide-for-windows-server-os-node-pools) |  | GA |  |  | Not supported.  
[`containerd` runtime for Windows node pool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-guide-for-windows-server-os-node-pools) |  | GA |  |  | Not supported.  
[Container-Optimized OS node pool support](https://docs.cloud.google.com/container-optimized-os/docs/concepts/features-and-benefits) |  | GA | GA | GA | No differences.  
[CoreDNS as the cluster DNS provider](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/configure-dns) | GA | GA | GA | GA | No differences.  
[User cluster lifecycle in the Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster) |  | GA | **Partial support** | GA | Changes apply. For more information, see [Advanced cluster limitations](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-lifecycle-management-tools#advanced_cluster_limitations).  
[Admin cluster node creation with Container-Optimized OS](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#os-image-type-field) |  | GA | GA | GA | No differences.  
[Multi-NIC capability for Pods](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/multi-nic) | GA | GA | GA | GA | No differences.  
[MetalLB load balancer option](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/bundled-load-balance-metallb) | GA | GA | GA | GA | Changes apply. For details, see [Bundled load balancing with MetalLB](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/bundled-load-balance-metallb).  
[`gkectl update admin` support for enabling and disabling Cloud Logging and Cloud Monitoring](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/logging-and-monitoring) | GA | GA | GA | GA | No differences.  
Windows Dataplane V2 support |  | GA |  |  | Not supported.  
Summary API metrics | GA | GA | GA | GA | No differences.  
[`gkectl update credentials` support for updating component access service account key](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/rotating-service-account-keys) | **Partial support** | GA | **Partial support** | **Partial support** | Changes apply. For details about what is or isn't supported for updating credentials for advanced clusters, see [Advanced cluster differences for rotating service account keys](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/rotating-service-account-keys#adv-cluster-diffs).  
[Prepared credentials for user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/prepared-credentials) |  | GA | GA | GA | No differences.  
[Dry run upgrade of user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#upgrade_user_cluster) | GA | GA | GA | GA | No differences.  
[Asynchronous upgrade of user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#upgrade_user_cluster) | GA | GA | GA | GA | No differences.  
Dry run upgrade of admin cluster |  |  | GA | GA | No differences.  
[Asynchronous upgrade of admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#upgrade_admin_cluster) | GA | GA | GA | GA | No differences.  
[Sequential update of node pools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#nodepoolupdatepolicy-maximumconcurrentnodepoolupdate-field) |  | GA | GA | GA | No differences.  
[Create volume snapshot with vSphere CSI driver](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vsphere-csi-restore-volume-snapshot) | **Preview** | **Preview** | **Preview** | **Preview** | No differences.  
[Create user cluster with Controlplane V2 enabled](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster) | GA | GA | GA | GA | No differences.  
[Storage migration with SPBM](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/storage-migration-spbm) | GA | GA | GA | GA | No differences.  
[Migrate a datastore to a SPBM](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-datastore-spbm) | GA | GA | GA | GA | No differences.  
[Migrate a user cluster to Controlplane V2](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-kubeception-controlplane-v2) | GA | GA | GA | GA | No differences.  
[Migrate to an HA admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-admin-cluster-ha) | GA | GA | GA | GA | No differences.  
[Migrate configuration settings for F5 BIG-IP](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-f5-manual) | GA | GA | GA | GA | No differences.  
[Load balancer](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/setup-load-balance) | **Partial support** | GA | GA | GA | Changes apply. For more information, refer to the relevant load balancer and cluster configuration reference documentation.  
[Preflight checks](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/preflight-checks) | **Partial support** | GA | GA | GA | No differences.  
[Hardware requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cpu-ram-storage) | GA | GA | GA | GA | Changes apply. For details, see [CPU, RAM, and storage requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cpu-ram-storage).  
[Snapshot](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/snapshots-advanced-cluster) | GA | GA | GA | GA | No differences.  
[Private registry](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/private-registry) | GA | GA | GA | GA | Changes apply. For details about using a private registry on an advanced cluster, see [Limitations with advanced clusters and the full bundle](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/private-registry#advanced-cluster-limitation).  
IPAM, [DNS](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/configure-dns), NTP and [multi-NIC](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/multi-nic) | GA | GA | GA | GA | No differences.  
Cluster creation/upgrade/deletion | GA | GA | GA | GA | Changes apply. For more information, refer to the relevant cluster operation documentation and [ Advanced cluster limitations](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-lifecycle-management-tools#advanced_cluster_limitations).   
[Proxy](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/firewall-rules) | GA | GA | GA | GA | No differences.  
[NodePool update policy](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-pool-update-policy) |  | GA | GA | GA | No differences.  
[Diagnose](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose) |  | GA | GA | GA | Changes apply. vCenter-related checks aren't available for advanced clusters. Since there's no longer a `onprem-user-cluster-controller` controller, the [Diagnose cluster issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose) guide is obsolete for advanced clusters. For version 1.32 advanced clusters, the `gkectl diagnose cluster` command runs [health checks](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/healthchecks) for the specified cluster.  
[vSphere tags and VM tracking](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vm-track-tags) |  | GA |  | GA | No differences.  
vSphere host group |  | GA |  | GA | No differences.  
[Logging and monitoring](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/logging-and-monitoring) | GA | GA | GA | GA | No differences.  
[Anti affinity groups](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#antiaffinitygroups-enabled-field) |  | GA | GA | GA | No differences.  
Non-HA user cluster control plane |  | GA |  |  | Not supported.  
`gkectl check-config` |  | GA | GA | GA | Changes apply. Support for the command on advanced user clusters was added in the following versions: 1.32.700+, 1.33.300+, and 1.34.0 and higher.  
  
## What's next

  * Create clusters with advanced cluster enabled:

    * [Create an admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-cluster)
    * [Create a user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster)
    * [Update or upgrade a cluster to an advanced cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/update-or-upgrade-to-adv-cluster)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
