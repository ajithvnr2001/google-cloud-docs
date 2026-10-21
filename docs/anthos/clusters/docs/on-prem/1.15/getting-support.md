---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/getting-support/
title: Getting support \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:12.855153+00:00
---

# Getting support  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/getting-support/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Getting support Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/getting-support)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



Google's primary support objective is to resolve production incidents as quickly as possible. We do this by understanding your configuration, analyzing logs and metrics, and collaborating with partners to solve incidents quickly.

Google Cloud offers a variety of support packages to accommodate your support needs. All Google Cloud Support packages include support for GKE Enterprise and Google Distributed Cloud. If you have an existing Google Cloud Support package, then you already have support for GKE Enterprise and Google Distributed Cloud.

For more information, see the [Cloud Customer Care](https://docs.cloud.google.com/support) documentation.

## Requirements for Google Distributed Cloud Support

To effectively troubleshoot business-critical incidents, you must:

  1. Check that the environment is current with the published end-of-support timeframes (see Version Support Policy below).
  2. Enable Cloud Logging and Cloud Monitoring for system components (for more details, see the Support tools section).
  3. When you open a support case, provide a configuration snapshot using the [`gkectl diagnose snapshot`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/diagnose#diagnose_snapshot) command.



## Support tools

To troubleshoot a Google Distributed Cloud incident, Google Cloud Support relies on three pieces of information:

  * Your environment's configuration
  * Logs from your admin and user clusters
  * Metrics from your admin and user clusters



### Configuration

When you open a support case, you are asked to run the `gkectl diagnose snapshot --seed-config` command and attach the resulting tarball to the support case. `gkectl diagnose snapshot --seed-config` captures information about Kubernetes and your nodes.

The tool is highly configurable and includes several predefined scenarios. You can also pass a YAML file with a customized set of information to gather. To learn more, refer to [Diagnosing Clusters](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/diagnose#diagnose_snapshot).

You can add an `excludeWords` field to your configuration file to omit sensitive or confidential information. Be sure to carefully review the information captured by the tool. Highly confidential or sensitive information should not be attached to your support case.

### Logs

When you create a new Google Distributed Cloud cluster, Cloud Logging agents are enabled by default and scoped only to system-level components. This replicates system-level logs into the Google Cloud project associated with the cluster. System-level logs are from Kubernetes pods running in one of five namespaces:

  * kube-system
  * gke-system
  * gke-connect
  * istio-system
  * config-management-system
  * knative-serving



Logs can be queried from the [Cloud Logging console](https://console.cloud.google.com/logs/viewer).

**Note:** If Cloud Logging is disabled, support is offered on best-effort basis only and could require significant additional effort from your on-site engineering team.

For more details, see [Logging and Monitoring](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/concepts/logging-and-monitoring).

### Metrics

In addition to logs, metrics are also captured by the Cloud Monitoring agent. This replicates system-level metrics into the Google Cloud project associated with the cluster. System-level metrics are from Kubernetes pods running in the same namespaces listed in Logs.

**Note:** If Cloud Monitoring is disabled, support is offered on best-effort basis only and could require significant additional effort from your on-site engineering team.

For more details, see [Logging and Monitoring](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/concepts/logging-and-monitoring).

### Google Cloud CLI and remote cluster access

If you open a support case, Cloud Customer Care may ask you for remote read-only access to your clusters to help diagnose and resolve issues more effectively. For the support team to have sufficient access to troubleshoot your cluster issue remotely:

  * Ensure that you've installed and updated to the latest version of the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud). The Google Cloud CLI must be at version 401.0.0 or higher to give Cloud Customer Care the needed permissions. We recommend that you update Google Cloud CLI regularly to pick up added permissions and other enhancements. To install the latest components of the gcloud CLI, use the [`gcloud components update`](https://docs.cloud.google.com/sdk/gcloud/reference/components/update) command.

  * Ensure the target cluster is registered and you have the project ID, membership name, and kubeconfig file.

    * To get user cluster kubeconfig, see [How to re-create user cluster kubeconfig](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/troubleshoot-cluster-creation-upgrade#re-create_missing_user_cluster_kubeconfig_file).

    * Your membership name is the same as the cluster name. To get the admin or user cluster name, you can use:
    
    gkectl list admin --kubeconfig ADMIN_CLUSTER_KUBECONFIG
    
        gkectl list clusters --kubeconfig ADMIN_CLUSTER_KUBECONFIG
    

  * To grant access to the cluster, you run a gcloud CLI command that generates and displays a set of Kubernetes role-based access control (RBAC) policies and applies them to the target cluster. See [Review the RBAC policies in advance](https://docs.cloud.google.com/anthos/docs/support/support-cluster-access#review_the_rbac_policies_in_advance).




For more information about giving Cloud Customer Care remote read-only access to your clusters, see [Google Cloud Support for your registered clusters](https://docs.cloud.google.com/anthos/docs/support/support-cluster-access).

## How we troubleshoot your environment

Here is an example of a typical support incident:

  1. Someone—for example, the cluster administrator—opens a support case via Google Cloud console or the Google Cloud Support Center, and selects _Anthos_ and _Google Distributed Cloud_ as Category and Component, respectively. They enter the information required and attach the output of `gkectl diagnose snapshot` to the case.
  2. The support case is routed to a Technical Support Engineer specializing in Google Distributed Cloud.
  3. The support engineer examines the contents of the snapshot to gain context of the environment.
  4. The support engineer examines the logs and metrics in the Google Cloud project, entering the support case ID as the business justification, which is logged internally.
  5. The support engineer responds to the case with an assessment and recommendation. The support engineer and the user continue troubleshooting until they come to a resolution.



## Collaborative Support Partners

Google maintains collaborative support relationships with select partners to deliver a more seamless support experience for Google Distributed Cloud. With these relationships, Google is able to collaborate closely with that partner on behalf of our shared customers.

To benefit from Collaborative Support, you must maintain support agreements with both Google and the partner in question.

Google currently has a collaborative support relationship in place with the partners specified on the [Collaborative Support Partners](https://cloud.google.com/terms/tssg/collab-partners) page.

Data about support issues may be shared with Collaborative Support Partners, as described in Google's [Technical Support Services Guidelines](https://cloud.google.com/terms/tssg/).

## What does Google support?

Generally, the Cloud Support team supports all software components shipped as part of Google Distributed Cloud. The table below details this further:

Google Cloud Support | Collaborative Support | Not Supported  
---|---|---  
Kubernetes and the container runtime   
| VMware vSphere (vCenter Server and ESXi)   
| VMware products beyond vSphere   
  
Canonical Ubuntu for guest/node OS   
| F5 BIG-IP load balancers   
| Customer code (see Developer Support below)   
  
vCenter controller   
| Hardware and hyper-converged infrastructure solutions as listed in the [Collaborative Support Partners](https://cloud.google.com/terms/tssg/collab-partners) page   
| Customer choice of host OS   
  
F5 controller   
|   
| Physical server, storage, and network   
  
Calico and related network policies   
|   
| External DNS, DHCP, and identity systems   
  
Ingress controller   
|   
| Calico Enterprise Edition   
  
Prometheus and Grafana   
|  |   
Stackdriver Monitoring, Stackdriver Logging, and Stackdriver agents   
|  |   
Identity federation with OIDC compliant providers   
|  |   
Hub, Connect, and the Connect Agent   
|  |   
Knative serving / Knative   
|  |   
Bundled LoadBalancer (Seesaw)   
|  |   
  
## Version Support Policy

Support for Google Distributed Cloud follows the [GKE Enterprise Version Support Policy](https://docs.cloud.google.com/anthos/docs/support/getting-support#version_support_policy). Starting with GKE Enterprise version 1.14, Google supports each Google Distributed Cloud minor version for 12 months after the initial release of the minor version, or until the release of the third subsequent minor version, whichever is longer.

The following table shows the supported and unsupported versions of this product:

Release version | Release date | End of life date*  
---|---|---  
[1.29 (latest)](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/downloads) | [April 29, 2024](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/release-notes#April_29_2024) | April 29, 2025 or 1.32 release date   
[1.28](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/downloads) | [December 14, 2023](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/release-notes#December_12_2023) | December 14, 2024 or 1.31 release date   
[1.16](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/downloads) | [August 23, 2023](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/release-notes#August_23_2023) | August 23, 2024 or 1.30 release date   
[1.15 (unsupported)](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/downloads) | [May 2, 2023](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/release-notes#May_02_2023) | May 2, 2024 or 1.29 release date   
  
*The EOL will be the later of these two dates.

**Earlier versions**

### Unsupported Google Distributed Cloud versions

Release version | Release date | End of life date  
---|---|---  
1.14  | [December 21, 2022](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/release-notes#December_21_2022) | December 21, 2023   
1.13  | [September 29, 2022](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/release-notes#September_29_2022) | August 17, 2023   
1.12  | [July 7, 2022](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/release-notes#July_07_2022) | March 29, 2023   
1.11  | [April 27, 2022](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/release-notes#April_27_2022) | December 21, 2022   
1.10  | [December 22, 2021](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/release-notes#December_22_2021) | September 22, 2022   
1.9  | [September 29, 2021](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/release-notes#September_29_2021) | June 29, 2022   
1.8  | [June 28, 2021](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.8/release-notes#June_28_2021) | March 28, 2022   
1.7  | [March 25, 2021](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/release-notes#March_25_2021) | December 25, 2021   
1.6  | [December 10, 2020](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/release-notes#December_10_2020) | September 10, 2021   
1.5  | [September 24, 2020](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.5/release-notes#September_24_2020) | June 24, 2021   
1.4  | [June 25, 2020](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.4/release-notes#June_25_2020) | March 25, 2021   
1.3  | [March 23, 2020](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.3/release-notes#March_23_2020) | December 23, 2020   
1.2  | [December 20, 2019](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.2/release-notes#December_20_2019) | September 20, 2020   
1.1  | [September 26, 2019](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.1/release-notes#September_26_2019) | June 26, 2020   
1.0  | [July 25, 2019](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.0/release-notes#July_25_2019) | April 25, 2020   
  
## Supported features

This document lists the features for Google Distributed Cloud for supported releases. The table is not intended to be an exhaustive list, but it highlights some of the benefits of upgrading your clusters to the latest supported version.

Features are listed by their product launch stage, either as Preview or General Availability. Features listed as Preview are covered by the [Pre-GA Offerings Terms](https://cloud.google.com/terms/service-terms#1) of the Google Cloud Terms of Service. Preview offerings are intended for use in test environments only and might have limited support. Changes to pre-GA products and features might not be compatible with other pre-GA versions. General Availability features are open to all customers, and are fully supported. For more information, see [Product launch stages](https://cloud.google.com/products#product-launch-stages).

For information about supported Anthos components and their compatibility, see [Anthos version and upgrade support](https://docs.cloud.google.com/anthos/docs/version-and-upgrade-support).

Feature/capability | **1.16** | **1.28** | **1.29 (latest)**  
---|---|---|---  
[Regional fleet membership](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#gkeconnect-location-field) |  | GA | GA  
[Version skew n+2 admin cluster - user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/upgrade-overview#version_skew) |  | **Preview** | GA  
[Version skew n+2 node pool - user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/upgrade-overview#version_skew) |  | **Preview** | GA  
[Max surge setting for node pool updates](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#nodepool-updatestrategy-rollingupdate-maxsurge-field) |  | **Preview** | **Preview**  
[cgroup v2 for nodes](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#nodepool-osimagetype-field) |  | **Preview** | GA  
[DSR mode for Dataplane V2](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#dataplanev2-forwardmode-field) | **Preview** | GA | GA  
[BinAuthz for Controlplane V2 user clusters](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/binary-authorization-policy) |  | GA | GA  
[Storage vMotion for SPBM clusters](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/configure-storage-policy) |  | **Preview** | **Preview**  
[User-managed admin workstation](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-admin-workstation) | **Preview** | GA | GA  
[StatefulSet CSI migration tool](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/using-statefulset-csi-migration-tool) | **Preview** | **Preview** | **Preview**  
[Seesaw to MetalLB migration](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/migrate-seesaw-metallb) | **Preview** | GA | GA  
[Disable bundled ingress](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/disable-bundled-ingress) | GA | GA | GA  
[Admin cluster prepared credentials](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/prepared-credentials-admin) | **Preview** | GA | GA  
[Storage policy for a user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/configure-storage-policy) | GA | GA | GA  
[Storage policy for an admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/configure-storage-policy) | **Preview** | GA | GA  
[Node auto repair](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/node-auto-repair) | GA | GA | GA  
[High availability admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-admin-cluster) | GA | GA | GA  
[VM-Host affinity](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/configure-vm-host-affinity) | GA | GA | GA  
[Generate configuration files from an existing cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/get-configuration-file-from-cluster) | GA | GA | GA  
[Managed Service for Prometheus system metrics collection](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/logging-and-monitoring#using-managed-service-for-prometheus) | GA | GA | GA  
[Upgrade and rollback of nodepools](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/upgrade-node-pools) | GA | GA | GA  
[Update private registry credentials](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/updating-cluster-credentials#update_private_registry_credentials) | GA | GA | GA  
[Admin cluster backup and restore with gkectl](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/back-up-and-restore-an-admin-cluster-with-gkectl) | **Preview** | **Preview** | **Preview**  
[User cluster nodepool autoscaling](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#nodepool-autoscaling-section) | GA | GA | GA  
[Cluster automatic node resizing](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/node-auto-resize) | GA | GA | GA  
[Multiple vSphere cluster support](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/install-overview#2_set_up_your_vsphere_environment) | GA | GA | GA  
[Multiple vSphere data centers support](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/install-overview#2_set_up_your_vsphere_environment) | GA | GA | GA  
[OpenID Connect (OIDC) support for authentication to clusters](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/concepts/authentication) | GA | GA | GA  
[CA certificate rotation](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/ca-rotation) | GA | GA | GA  
[Workload Identity support](https://docs.cloud.google.com/anthos/fleet-management/docs/use-workload-identity) | GA | GA | GA  
[AIS with LDAP authentication support](https://docs.cloud.google.com/anthos/identity/setup/ldap) | GA | GA | GA  
[Always-on secrets encryption without hardware security module (HSM)](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/always-on-secrets-encryption) | GA | GA | GA  
[Update vCenter CA certificates with gkectl](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/update-vcenter-certificate) | GA | GA | GA  
[Egress NAT gateway](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/egress-nat-gateway) | GA | GA | GA  
[Admin cluster fleet registration](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/admin-cluster-configuration-file#gkeconnect-section) | GA | GA | GA  
[Windows node pool support](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-guide-for-windows-server-os-node-pools) | GA | GA | GA  
[`containerd` runtime for Windows node pool](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-guide-for-windows-server-os-node-pools#set_up_containerd_support_for_windows_node_pools_preview) | GA | GA | GA  
[Container-optimized OS node pool support](https://cloud.google.com/container-optimized-os/docs/concepts/features-and-benefits) | GA | GA | GA  
[CoreDNS as the cluster DNS provider](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/configure-dns) | GA | GA | GA  
[User cluster lifecycle in the Google Cloud console](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-user-cluster-api) | GA | GA | GA  
[Admin cluster node creation with Container-optimized OS](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/admin-cluster-configuration-file#os-image-type-field) | GA | GA | GA  
[Multi-NIC capability for Pods](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/multi-nic) | GA | GA | GA  
[MetalLB load balancer option](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/bundled-load-balance-metallb) | GA | GA | GA  
[`gkectl update admin` support for enabling and disabling Cloud Logging and Cloud Monitoring](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/updating-general#enable_or_disable_logging_and_monitoring_for_the_admin_cluster) | GA | GA | GA  
Windows Dataplane V2 support  | GA | GA | GA  
Summary API metrics  | GA | GA | GA  
[`gkectl update credentials` support for updating component access service account key](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/rotating-service-account-keys) | GA | GA | GA  
[Prepared credentials for user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/prepared-credentials) | GA | GA | GA  
[Dry run upgrade of user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/upgrading#upgrade_user_cluster) |  |  | GA  
[Asynchronous upgrade of user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/upgrading#upgrade_user_cluster) | GA | GA | GA  
[Asynchronous upgrade of admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/upgrading#upgrade_admin_cluster) |  |  | GA  
[Sequential update of node pools](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#nodepoolupdatepolicy-maximumconcurrentnodepoolupdate-field) | GA | GA | GA  
[Create volume snapshot with vSphere CSI driver](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/vsphere-csi-restore-volume-snapshot) | **Preview** | **Preview** | **Preview**  
[Create user cluster with ControlPlaneV2 enabled](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-user-cluster-new-model) | GA | GA | GA  
[Storage migration with SPBM](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/storage-migration-spbm) |  | **Preview** | GA  
[Migrate a datastore to a SPBM](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/migrate-datastore-spbm) |  |  | **Preview**  
[Migrate a user cluster to Controlplane V2](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/migrate-kubeception-controlplane-v2) |  |  | **Preview**  
[Migrate to HA admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/migrate-admin-cluster-ha) |  |  | **Preview**  
[Migrate the configuration for integrated F5 BIG-IP](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/migrate-f5-manual) |  |  | **Preview**  
  
## Shared Responsibility Model

Running a business-critical production application on Google Distributed Cloud requires multiple parties to carry different responsibilities. These responsibilities are described at [GKE Enterprise shared responsibility](https://docs.cloud.google.com/anthos/docs/concepts/gke-shared-responsibility).

## Developer Support

Google does not provide support for application workloads running on Google Distributed Cloud. However, we do provide best-effort developer support to ensure your developers can easily run applications on Google Distributed Cloud. We believe that engaging earlier during development can prevent critical incidents later in the deployment.

This Developer Support is available to customers with a paid support package and is treated at a priority level 3 for an issue blocking a launch, or at priority level 4 for general consultation. In this classification, priority level 0 is the highest priority.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
