---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support/
title: Getting support \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:22:12.627895+00:00
---

# Getting support  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Getting support Stay organized with collections  Save and categorize content based on your preferences. 

Google's primary support objective is to resolve production incidents as quickly as possible. We do this by understanding your configuration, analyzing logs and metrics, and collaborating with partners to solve incidents quickly.

[Cloud Customer Care](https://docs.cloud.google.com/support) offers a variety of support packages to accommodate your support needs. All Cloud Customer Care support packages include support for GKE and Google Distributed Cloud. If you have an existing Cloud Customer Care support package, then you already have support for GKE and Google Distributed Cloud.

For more information, see the [Cloud Customer Care hub](https://cloud.google.com/support-hub).

## Requirements for Google Distributed Cloud support

To effectively troubleshoot business-critical incidents, you must:

  1. Check that the environment is current with the published end-of-support timeframes. For more information, see the Version Support Policy section.
  2. Enable Cloud Logging and Cloud Monitoring for system components. For more information, see the Support tools section.
  3. When you open a support case, provide a configuration snapshot by using the [`gkectl diagnose snapshot`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/snapshots) command.



## Support tools

To troubleshoot business-critical incidents effectively, Cloud Customer Care relies on three pieces of information:

  * Your environment's configuration
  * Logs from your admin and user clusters
  * Metrics from your admin and user clusters



### Configuration

When you open a support case, you are asked to run the `gkectl diagnose snapshot --seed-config` command and attach the resulting tar file to the support case. The `gkectl diagnose snapshot --seed-config` command captures information about Kubernetes and your nodes.

The tool is highly configurable and includes several predefined scenarios. You can also pass a YAML file with a customized set of information to gather. For more information, see [Diagnosing Clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/snapshots).

Be sure to carefully review the information captured by the tool.

Do not attach highly confidential or sensitive information to your support case. You can add an `excludeWords` field to your configuration file to omit sensitive or confidential information.

### Logs

When you create a new cluster, Cloud Logging agents are enabled by default and scoped only to system-level components. This replicates system-level logs into the Google Cloud project associated with the cluster. System-level logs are from Kubernetes pods running in one of the following namespaces:

  * `kube-system`
  * `gke-system`
  * `gke-connect`
  * `istio-system`
  * `config-management-system`
  * `knative-serving`



Logs can be queried from the [Cloud Logging console](https://console.cloud.google.com/logs/viewer).

**Note:** If Cloud Logging is disabled, support is offered on best-effort basis only and could require significant additional effort from your on-site engineering team.

For more details, see [Logging and Monitoring](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/logging-and-monitoring).

### Metrics

In addition to logs, metrics are also captured by the Cloud Monitoring agent. This replicates system-level metrics into the Google Cloud project associated with the cluster. System-level metrics are from Kubernetes pods running in the same namespaces listed in Logs.

**Note:** If Cloud Monitoring is disabled, support is offered on best-effort basis only and could require significant additional effort from your on-site engineering team.

For more details, see [Logging and Monitoring](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/logging-and-monitoring).

### Google Cloud CLI and remote cluster access

If you open a support case, Cloud Customer Care might ask you for remote read-only access to your clusters to help diagnose and resolve issues more effectively. For the Cloud Customer Care to have sufficient access to troubleshoot your cluster issue remotely, do the following:

  * Ensure that you've installed and updated to the latest version of the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud). The Google Cloud CLI must be at version 401.0.0 or later to give Cloud Customer Care the needed permissions. We recommend that you update Google Cloud CLI regularly to pick up added permissions and other enhancements. To install the latest components of the gcloud CLI, use the [`gcloud components update`](https://docs.cloud.google.com/sdk/gcloud/reference/components/update) command.

  * Ensure the target cluster is registered and you have the project ID, membership name, and kubeconfig file.

    * To get the user cluster kubeconfig file, see [How to re-create user cluster kubeconfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/create-upgrade#re-create_missing_user_cluster_kubeconfig_file).

    * Your membership name is the same as the cluster name. To get the admin or user cluster name, you can use:
    
    gkectl list admin --kubeconfig ADMIN_CLUSTER_KUBECONFIG
    
        gkectl list clusters --kubeconfig ADMIN_CLUSTER_KUBECONFIG
    

  * To grant access to the cluster, you run a gcloud CLI command that generates and displays a set of Kubernetes role-based access control (RBAC) policies and applies them to the target cluster. See [Review the RBAC policies in advance](https://docs.cloud.google.com/anthos/docs/support/support-cluster-access#review_the_rbac_policies_in_advance).




For more information about giving Cloud Customer Care remote read-only access to your clusters, see [Google Cloud Support for your registered clusters](https://docs.cloud.google.com/anthos/docs/support/support-cluster-access).

## How we troubleshoot your environment

Here is an example of a typical support incident:

  1. Someone—for example, the cluster administrator—opens a support case in the Google Cloud console or with [Cloud Customer Care](https://cloud.google.com/support-hub).

     1. In the console, go to the **Support overview** page.

[Go to Support overview](https://console.cloud.google.com/support)

     2. In the **Support information** section, click **Get help**.

     3. In the **Select your product** field, enter the following:
            
            Google Distributed Cloud Virtual - vSphere (Anthos on VMWare)
            

     4. Click the item in the **Matching products** list, and then click **Select**.

     5. Enter the required information and attach the output of the `gkectl diagnose snapshot` command to the case.

  2. The support case is routed to a Technical Support Engineer specializing in Google Distributed Cloud (software only) for VMware.

  3. The support engineer examines the contents of the snapshot to gain context of the environment.

  4. The support engineer examines the logs and metrics in the Google Cloud project, entering the support case ID as the business justification, which is logged internally.

  5. The support engineer responds to the case with an assessment and recommendation. The support engineer and the user continue troubleshooting until they come to a resolution.




## Collaborative Support Partners

Google maintains collaborative support relationships with select partners to deliver a more seamless support experience. With these relationships, Google is able to collaborate closely with that partner on behalf of our shared customers.

To benefit from Collaborative Support, you must maintain support agreements with both Google and the partner in question.

Google has a collaborative support relationship in place with the partners specified on the [Collaborative Support Partners](https://cloud.google.com/terms/tssg/collab-partners) page.

Data about support issues may be shared with Collaborative Support Partners, as described in Google's [Technical Support Services Guidelines](https://cloud.google.com/terms/tssg/).

## What does Google support?

Generally, Cloud Customer Care supports all software components shipped as part of Google Distributed Cloud (software only) for VMware. The following table provides further details:

Cloud Customer Care | Collaborative Support | Not Supported  
---|---|---  
Kubernetes and the container runtime   
| VMware vSphere (vCenter Server and ESXi)   
| VMware products beyond vSphere   
  
Canonical Ubuntu for guest/node OS   
| F5 BIG-IP load balancers   
| Customer code (For more information, see the Developer Support section)   
  
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
  
  
|   
| Prometheus and Grafana   
  
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
  
## Supported features

This document lists the features for Google Distributed Cloud for supported releases. The table is not intended to be an exhaustive list, but it highlights some of the benefits of upgrading your clusters to the latest supported version.

Features are listed by their product launch stage, either as Preview or General Availability. Features listed as Preview are covered by the [Pre-GA Offerings Terms](https://cloud.google.com/terms/service-terms#1) of the Google Cloud Terms of Service. Preview offerings are intended for use in test environments only and might have limited support. Changes to pre-GA products and features might not be compatible with other pre-GA versions. General Availability features are open to all customers, and are fully supported. For more information, see [Product launch stages](https://cloud.google.com/products#product-launch-stages).

For information about supported GKE components and their compatibility, see [GKE version and upgrade support](https://docs.cloud.google.com/anthos/docs/version-and-upgrade-support).

Feature/capability | **1.34** | **1.35** | **1.36 (latest)**  
---|---|---|---  
[Advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/advanced-clusters) | GA | GA | GA  
[Topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up) | **Preview** | **Preview** | **Preview**  
[Regional fleet membership](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#gkeconnect-location-field) | GA | GA | GA  
[Version skew n+2 admin cluster - user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-overview#version_skew) | GA | GA | GA  
[Version skew n+2 node pool - user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-overview#version_skew) | GA | GA | GA  
[Max surge setting for node pool updates](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#nodepool-updatestrategy-rollingupdate-maxsurge-field) | **Preview** | **Preview** | **Preview**  
[cgroup v2 for nodes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#nodepool-osimagetype-field) | GA | GA | GA  
[DSR mode for Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#dataplanev2-forwardmode-field) | GA | GA | GA  
[BinAuthz for Controlplane V2 user clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/binary-authorization-policy) | GA | GA | GA  
[User-managed admin workstation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-workstation) | GA | GA | GA  
[StatefulSet CSI migration tool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/using-statefulset-csi-migration-tool) | GA | GA | GA  
[Disable bundled ingress](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/disable-bundled-ingress) | GA | GA | GA  
[Admin cluster prepared credentials](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/prepared-credentials-admin) | GA | GA | GA  
[Storage policy for a user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/configure-storage-policy) | GA | GA | GA  
[Storage policy for an admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/configure-storage-policy) | GA | GA | GA  
[Node auto repair](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-auto-repair) | GA | GA | GA  
[High availability admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-cluster) | GA | GA | GA  
[VM-Host affinity](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/configure-vm-host-affinity) | GA | GA | GA  
[Generate configuration files from an existing cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/get-configuration-file-from-cluster) | GA | GA | GA  
[Managed Service for Prometheus system metrics collection](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/logging-and-monitoring#using-managed-service-for-prometheus) | GA | GA | GA  
[Upgrade and rollback of nodepools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-node-pools) | GA | GA | GA  
[Update private registry credentials](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/updating-cluster-credentials#update_private_registry_credentials) | GA | GA | GA  
[Admin cluster backup and restore with gkectl](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/back-up-and-restore-an-admin-cluster-with-gkectl) | **Preview** | **Preview** | **Preview**  
[User cluster nodepool autoscaling](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#nodepool-autoscaling-section) | GA | GA | GA  
[Cluster automatic node resizing](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-auto-resize) | GA | GA | GA  
[Multiple vSphere cluster support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/install-overview#2_set_up_your_vsphere_environment) | GA | GA | GA  
[Multiple vSphere data centers support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/install-overview#2_set_up_your_vsphere_environment) | GA | GA | GA  
[OpenID Connect (OIDC) support for authentication to clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/authentication) | GA | GA | GA  
[CA certificate rotation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ca-rotation) | GA | GA | GA  
[Workload Identity support](https://docs.cloud.google.com/anthos/fleet-management/docs/use-workload-identity) | GA | GA | GA  
[AIS with LDAP authentication support](https://docs.cloud.google.com/anthos/identity/setup/ldap) | GA | GA | GA  
[Always-on secrets encryption without hardware security module (HSM)](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/always-on-secrets-encryption) | GA | GA | GA  
[Update vCenter CA certificates with gkectl](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/update-vcenter-certificate) | GA | GA | GA  
[Egress NAT gateway](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/egress-nat-gateway) | GA | GA | GA  
[Admin cluster fleet registration](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#gkeconnect-section) | GA | GA | GA  
[Windows node pool support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-guide-for-windows-server-os-node-pools) | 1 | 1 | 1  
[`containerd` runtime for Windows node pool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-guide-for-windows-server-os-node-pools#set_up_containerd_support_for_windows_node_pools_preview) | 1 | 1 | 1  
[Container-optimized OS node pool support](https://docs.cloud.google.com/container-optimized-os/docs/concepts/features-and-benefits) | GA | GA | GA  
[CoreDNS as the cluster DNS provider](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/configure-dns) | GA | GA | GA  
[User cluster lifecycle in the Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster) | GA | GA | GA  
[Admin cluster node creation with Container-optimized OS](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#os-image-type-field) | GA | GA | GA  
[Multi-NIC capability for Pods](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/multi-nic) | GA | GA | GA  
[MetalLB load balancer option](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/bundled-load-balance-metallb) | GA | GA | GA  
[`gkectl update admin` support for enabling and disabling Cloud Logging and Cloud Monitoring](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/updating-general#enable_or_disable_logging_and_monitoring_for_the_admin_cluster) | GA | GA | GA  
Windows Dataplane V2 support  | 1 | 1 | 1  
Summary API metrics  | GA | GA | GA  
[`gkectl update credentials` support for updating component access service account key](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/rotating-service-account-keys) | GA | GA | GA  
[Prepared credentials for user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/prepared-credentials) | GA | GA | GA  
[Dry run upgrade of user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#upgrade_user_cluster) | GA | GA | GA  
[Asynchronous upgrade of user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#upgrade_user_cluster) | GA | GA | GA  
[Asynchronous upgrade of admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#upgrade_admin_cluster) | GA | GA | GA  
[Sequential update of node pools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#nodepoolupdatepolicy-maximumconcurrentnodepoolupdate-field) | GA | GA | GA  
[Create volume snapshot with vSphere CSI driver](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vsphere-csi-restore-volume-snapshot) | **Preview** | **Preview** | **Preview**  
[Create user cluster with Controlplane V2 enabled](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster) | GA | GA | GA  
[Storage migration with SPBM](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/storage-migration-spbm) | GA | GA | GA  
[Migrate a datastore to a SPBM](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-datastore-spbm) | GA | GA | GA  
[Migrate a user cluster to Controlplane V2](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-kubeception-controlplane-v2) | GA | GA | GA  
  
**1** Windows Server OS node pools are deprecated in version 1.32 and will be unavailable in version 1.33 and higher. Support for Windows Server OS node pools ends May 25, 2026. We recommend that you begin migration planning immediately to ensure a smooth transition before the support period ends.

## Version Support Policy

The objective of this Version Support Policy is to give you the flexibility to schedule upgrades when it meets your business needs, while balancing the rapid evolution of both Kubernetes and Google Distributed Cloud.

Google Distributed Cloud software only follows the Kubernetes versioning scheme and release cycle. Minor releases happen approximately three times per year. Patches for each supported minor version occur approximately monthly. Like Kubernetes, Google Distributed Cloud supports the latest three minor versions concurrently.

Google supports each Google Distributed Cloud minor version for the later of:

  * 12 months after the initial release of the minor version.
  * The release of the third subsequent minor version.



For example, minor version 1.33 released on September 02, 2025. This minor version and all of its patches are supported until either September 02, 2026 or the release date of minor version 1.36, whichever date is later.

We encourage you to maintain your Google Distributed Cloud environment with the product's latest minor release and [recommended patch version](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/version-and-upgrade-support#google_cloud_distributed).

This version support policy includes:

  * Break-fix support from Cloud Customer Care.
  * CVE security vulnerabilities to Kubernetes and related components.
  * General patches to Kubernetes and related components. 
  * CVE security vulnerabilities to Ubuntu or Container-Optimized OS.
  * General patches to Ubuntu or Container-Optimized OS. 



When your version reaches end-of-life, you can continue to open cases to receive support for the following:

  * Help with technical issues.
  * Assistance with billing issues.
  * Guidance on product usage, including help with troubleshooting and testing.



Extended support can be conditionally approved as a one-time event, with version-pinning, and future upgrade timeline requirements. For additional information, reach out to the lead customer engineer for your account or the account manager. Alternatively, you can [file a support case](https://console.cloud.google.com/support) through Google Cloud console. Such requests are routed to the customer engineering group for your account.

### Support period

The following table shows the supported minor releases for Google Distributed Cloud and the earliest end-of-life (EOL) dates:

Google Distributed Cloud version | Release date | End-of-life date*  
---|---|---  
1.35 | 2026-04-29 | 2027-04-29 or 1.38 release date  
1.34 | 2025-12-11 | 2026-12-11 or 1.37 release date  
1.33 | 2025-09-02 | 2026-09-02 or 1.36 release date  
1.32 | 2025-05-06 | 2026-05-06 or 1.35 release date  
  
* The EOL will be the later of these two dates.

To learn more version compatibility for Google Distributed Cloud and related Google Cloud products, see [Version and upgrade support](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/version-and-upgrade-support).

### Versioning scheme

Google Distributed Cloud uses Kubernetes [semantic versioning](https://semver.org/) to refer to supported Kubernetes versions, but appends a GKE patch version. This results in a version number of the form: `x.y.z-gke.N`.

Kubernetes major version (x)
    Major versions are typically incremented if any backwards incompatible changes are introduced to the public API. A major version increments the Kubernetes version from `x.y` to `x+1.y`.
Kubernetes minor version (y)
    Kubernetes releases a new minor version [three times a year](https://github.com/kubernetes/kubernetes/releases). Each release cycle is approximately 15 weeks long. [Deprecated APIs](https://kubernetes.io/docs/reference/using-api/deprecation-guide/) might be removed with a new minor version. A minor version increments the Kubernetes version from `1.y` to `1.y+1`; for example, Kubernetes 1. **29** is the minor release that follows Kubernetes 1.**28**.
Google Distributed Cloud patch release (z-gke.N)
    A patch release, such as 1.28.**300-gke.131** , increments the patch version (z) by 100 and includes a `-gke.N` suffix, which indicates the build. Patch releases include security updates and bug fixes. A Google Distributed Cloud patch release version doesn't correlate to a Kubernetes patch version.

## Shared responsibility model

Running a business-critical production application on Google Distributed Cloud requires multiple parties to carry different responsibilities. These responsibilities are described at [GKE shared responsibility](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/gke-shared-responsibility).

## Developer support

Google doesn't provide support specifically for your application workloads. However, we do provide _best-effort_ developer support to ensure your developers can run applications on clusters created using Google Distributed Cloud. We believe that engaging earlier during development can prevent critical incidents later in the deployment.

This _best-effort_ developer support is available to customers with any paid support package and is treated as a P3 priority for an issue blocking a launch, or a P4 priority for general consultation. In this classification, priority level 0 is the highest priority.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
