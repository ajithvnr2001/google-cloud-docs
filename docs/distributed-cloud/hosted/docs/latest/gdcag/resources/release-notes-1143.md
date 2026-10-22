---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/release-notes-1143/
title: Google Distributed Cloud air-gapped 1.14.3 release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:00:13.876138+00:00
---

# Google Distributed Cloud air-gapped 1.14.3 release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/release-notes-1143/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Google Distributed Cloud air-gapped 1.14.3 release notes Stay organized with collections  Save and categorize content based on your preferences. 

## February 28, 2025

* * *

Google Distributed Cloud (GDC) air-gapped 1.14.3 is available.  
See the [product overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/overview) to learn about the features of Distributed Cloud. 

* * *

The following new features are available: 

**Backup and restore** :

  * Added the ability to create scoped VM backups and restores to target specific VM workloads. Create these VM backups manually, or create backup plans that automatically perform backups on a schedule you define. For more information, see [Overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/backup-plans/vm-scope-overview). 
  * Added VM fine-grained restores that let you restore specific VM and VM disk resources. For more information, see [Create a fine-grained restore](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/restore-backup/create-fine-grained-restore). 
  * Added cluster fine-grained restores which let you restore a subset of resources from a cluster backup. This feature provides the flexibility to refine the restore scope defined in the restore plan. For more information, see [Create a fine-grained restore](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/restore-backup/create-fine-grained-restore). 



**Billing** :

  * Added the ability to upload monthly billing costs to the Argentum console. 



**DNS** :

  * You can now create and manage your own public and private DNS zones to suit the needs of your applications and services. Within a DNS zone, you can create DNS records. Different types of DNS records serve different purposes, such as directing traffic, defining mail servers, and verifying ownership. For more information, see [About DNS zones and records](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/dns-overview).



**Firewall** :

  * Added the ability to configure NTP PANW authentication on GDC firewalls using symmetric keys. 



**IAM** :

  * IAM APIs that control identity providers, service accounts, and role bindings are global by default, spanning all zones in a GDC universe. For more information, see [Permissions control for a multi-zone universe](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/permissions).



**Marketplace** :

  * Neo4j is available in the GDC air-gapped marketplace. Neo4j is an open-source, NoSQL, built-in graph database that provides an ACID-compliant transactional backend for your applications. 
  * MariaDB Operator is available in the GDC air-gapped marketplace. MariaDB Operator uses supported Docker images to provide a fleet management and HA/DR solution for MariaDB Enterprise Server and MaxScale. 
  * HashiCorp Vault (BYOL) is available in the Google Distributed Cloud air-gapped marketplace. HashiCorp Vault is an identity-based secrets and encryption management system. 
  * Apache Kafka on Confluent Platform (BYOL) is available in the GDC air-gapped marketplace. Confluent Platform is a solution that allows real-time access, storage, and management of continuous data streams. 
  * Redis Software for Kubernetes (BYOL) is available in the GDC air-gapped marketplace. Redis is the world's fastest in-memory database for building and scaling fast applications. 



**MHS** :

  * The Managed Harbor Service (MHS) now includes Harbor backup and restore. Configure backups and create restores for Harbor instances. For more information, see [Overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/harbor-backup-overview). 
  * Added the MHS credential helper that lets you use your GDC identity to sign in to the Docker or Helm CLI. For more information, see [Sign in to Docker and Helm](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/configure-docker-authentication). 
  * Added the ability to scan all of the artifacts in a Harbor instance. For more information, see [Scan for vulnerabilities](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/scan-vulnerabilities). 



**Logging** :

  * The Loki pod crashes or is OOMKilled during WAL replay. 

  * Scraping failure for `log-collector` and `oplogs-forwarder`. 




**Monitoring** :

  * Added support for cross-zone querying and monitoring in visualization dashboards. For more information, see [Query and view metrics](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/query-and-view-metrics) and [Query and view logs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/query-and-view-logs). 

  * An OCLCM noisy alert can be ignored. 

  * The system metrics pipeline is down. 

  * `MON-A0001_fast` and `MON-A0001_slow` alerts are firing in org clusters 




**Networking** :

  * Use multi-zone internal and external load balancers to distribute traffic for VM and pod workloads. For more information, see [Overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/expose-services).

  * Configure interconnect resources to establish physically dedicated connectivity to external private networks. For more information, see the interconnect [Overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/interconnects/interconnect-overview). 

  * Configure an internal or external load balancer for pod and VM workloads using the Networking KRM API or gdcloud CLI. For more information, see [Manage load balancers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/expose-services).

  * Use [zonal and global project network policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/pnp-overview) to establish connectivity between projects and organizations.

  * Create [intra-project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/intra-project-traffic#create-workload-level-intra) and [cross-project workload-level network policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/cross-project-traffic#egress-workload-level-cross-project) to define specific access rules for individual VMs and pods within a project and between projects.




**Resource Manager** :

  * Projects are global resources by default that span all zones in a GDC universe. For more information, see the [Multi-zone overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/mz-overview).



**Virtual machines** :

  * Added the ability to [enable virtual trusted platform module (vTPM)](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/secure-vms/secure-boot#enable-vtpm) when securely booting a VM.

  * Added the following images to the [GDC-provided VM image list](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-a-vm/supported-vm-images): 

    * Ubuntu 24.04 golden image 
    * SUSE CHost 15.5 bring your own (BYO) image 
    * Windows 10 bring your own (BYO) image 
  * Added the ability to perform [VM disk expansion](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/expand-vm-disks) on `VirtualMachineDisk` partitions. 

  * Added the ability to [Create a VM instance with a specified IP address and subnet](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-a-vm/create-and-start#create-vm-with-ip). 

  * Added the ability to [View and maintain VM metadata](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/view-and-maintain-metadata). 

  * Added new [N4-highmem VM machine](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/view-vm-machine-type) family support. 




* * *

Updated the Rocky OS image version to 20250124 to apply the latest security patches and important updates. 

The following security vulnerabilities are fixed:

  * [CVE-2022-3787](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3787)
  * [CVE-2022-27635](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27635)
  * [CVE-2022-40964](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-40964)
  * [CVE-2022-46329](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-46329)
  * [CVE-2023-20569](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20569)
  * [CVE-2023-20584](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20584)
  * [CVE-2023-20592](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20592)
  * [CVE-2023-20593](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20593)
  * [CVE-2023-27536](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27536)
  * [CVE-2023-28321](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28321)
  * [CVE-2023-28322](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28322)
  * [CVE-2023-31315](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-31315)
  * [CVE-2023-31346](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-31346)
  * [CVE-2023-31356](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-31356)
  * [CVE-2023-37920](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-37920)
  * [CVE-2023-38546](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38546)
  * [CVE-2023-46218](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-46218)
  * [CVE-2024-10041](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-10041)
  * [CVE-2024-10963](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-10963)
  * [CVE-2024-22365](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-22365)
  * [CVE-2024-2398](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-2398)
  * [CVE-2024-5535](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-5535)
  * [CVE-2024-52530](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-52530)
  * [CVE-2024-52532](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-52532)



* * *

The following issues are identified: 

**Backup and restore**

  * Editing a `RestorePlan` from the GDC console is broken. 

  * Agent and control plane pods might restart if they run out of memory, affecting system stability. 

  * GDC Service Level Objective (SLO) metrics and alerts for backup and restore are not enabled by default due to missing custom resource definitions. 

  * Retention policies are not applied to imported backups. 

  * Partial VM backups fail. 

  * Clean up orphaned backup resources after user or service cluster deletion. 

  * `VirtualMachineRestore` deletion is not supported through CLI or UI. 

  * The restore process for a resource, such as a database clone or user workload restore, gets stuck and eventually times out due to a pending persistent volume claim. 




**Cluster management**

  * The `kub-gpu-controller` subcomponent does not reconcile for the `gdchservices` organization. 

  * Removing obsolete node pools from standard clusters fails. Standard clusters are in private preview and might not be available to all customers. 




**Database services**

  * Soft-deleted database clusters get stuck in a `DBClusterReconciling` state when deleted immediately after creation. 

  * The `gdcloud stop database` command takes a long time to complete. 




**DNS**

  * A false DNS alert is fired suggesting `GlobalCustomerRootDNSServerNotReachable`. 



**Firewall**

  * Legacy firewall rules might block organization to root admin traffic after upgrade. 

  * The organization is not reachable through the global UI console DNS. 

  * After the `OCITTopology` custom resource is deployed, the connectivity between OIR and GDC management plane and data plane becomes broken. 

  * Cross-zone cross-organization traffic is blocked by default by GDC firewalls. 

  * After an `AttachmentGroup` is deployed, if the `identifier` field in that `AttachmentGroup` object is the same as `orgName`, the firewall fails to parse this object and the firewall config update gets stuck. 




**Inventory**

  * The inventory audit fails to reconcile. 



**Hardware security module** :

  * Deactivated trial licenses are still detectable in CipherTrust Manager, triggering false expiration warnings. 

  * An issue occurs where HSMs fail with a `ValidateNetworkConfig` error after boot-up. This error prevents the HSM custom resources from entering a `Ready` state. 

  * A file descriptor leak causes a `ServicesNotStarted` error. 




**Health** :

  * The system potentially triggers more than 30 false alarms about SLO alerts across multiple components because of an issue with SLO API labeling. 



**Identity and access management** :

  * A `CustomRole` resource that includes a `zonalRules` section might not grant permissions reliably. 

  * An OPA Gatekeeper trust issue after a root CA rotation prevents IAM role creation in new projects. 

  * Role bindings fail if generated IAM role binding names exceed 63 characters. 

  * Project Service Accounts (PSA) cannot assign IAM role bindings to itself or other PSAs with the `organization-iam-admin` role. 

  * New projects experience delays with predefined role creation. 

  * Application operators can't grant themselves access to roles in the infra cluster. 

  * Existing service accounts tokens become invalid. 




**Infrastructure as Code (IAC)**

  * A subcomponent fails to reconcile due to a missing namespace. 
  * The IAC ConfigSync metric collection fails. 
  * The IAC root sync fails. 



**Key management system** :

  * KMS servers might experience performance issues and `OOMKilling` under heavy workloads. 

  * When the `kms-rootkey-controller` memory usage exceeds the `1100Mi` limit, the controller enters a `CrashLoopBackOff` due to an `OOMKilled` status. 

  * KMS configured to use a CTM root key does not failover when an HSM is unavailable. 

  * KMS pods in the root organization might crash due to audit logs filling ephemeral storage. 




**Load balancers** :

  * Global load balancer creation fails due to insufficient IP addresses in global subnets. 
  * The load balancer objects are not entering a `Ready` state. 
  * Modifying load balancers once they have been configured is not yet supported. 

  * The global `BackendService` resource doesn't reject incorrect zone names. 

  * A webhook error can occur for both zonal and global load balancers. 




**MHS** :

  * After a Managed Harbor Service (MHS) backup and restore operation, the CLI secrets become invalid for the restored Harbor instance and need to be created again. 
  * When multiple Harbor instances exist in different user projects, the backup and restore operations compete for role-based access controls and experience a high failure rate. 
  * Backup size is not implemented for Harbor backup and restore. In the GDC console, the **SizeBytes** field shows a value of `0` and the **Size** column shows a value of 0 MB. 
  * When viewing the **Harbor Container Registry** page in the GDC console, users without the necessary Harbor Instance Admin permission see an error message when retrieving backup resources. 
  * The database password rotation is stuck. 



**Monitoring** :

  * The AlertManager webhook fails to send alerts and incident notifications for some clusters. 
  * Incidents are occasionally duplicated upon creation. 
  * Two monitoring false alerts are open in the root admin cluster. 
  * A reconciliation error alert can be ignored. 
  * The root admin controller manager shows a high error rate. 
  * The KUB monitoring dashboards show no data. 
  * The permissions are misconfigured for an observability debugger role. 
  * A Grafana debugger role is missing. 
  * Project deletion is stuck due to dashboard and data source pending finalizers. 
  * Metrics from KSM are not visible to PAs. 
  * `MON-A0001_fast` and `MON-A0001_slow` alerts are firing in org clusters 



**Multi-zone** :

  * When a zone is inaccessible, the GDC console displays an authentication error. 

  * Listing zones using the gdcloud CLI is not available by default. 

  * There can be intermittent sign in errors when accessing the global GDC console URL. 




**Object storage:**

  * StorageGRID load balancer endpoint certificate expired. 



**Networking** :

  * Configuring Border Gateway Protocol (BGP) with a 4-byte Autonomous System Number (ASN) on network switches leads to configuration failures. 

  * Enabling node-to-node IP address security (IPsec) encryption at runtime for an existing organization might cause network packet drops and connection timeouts. 

  * Node is not reachable on the Data Network. 

  * The network experiences a drop of around 50% in cross-zone traffic between nodes. 

  * `StatefulSet` pod rollouts might cause connectivity issues. 

  * Global anycast traffic is blocked by overly restrictive Access Control Lists (ACLs). 

  * The `allow-all-egress` project network policy (PNP) does not allow traffic to system endpoints. 

  * The `pnet-cross-zone-availability` SLO dashboard doesn't show any metrics in Grafana. 

  * Data plane and management ingress gateways fail to reconcile. 

  * The project network policy page in the GDC console does not support the `projectSelector` field in the ProjectNetworkPolicy API. 

  * Network switch configuration changes are not being committed. 




**Operations Suite Infrastructure Core Services (OIC)** :

  * The jumphost performs poorly. 



**Operating system** :

  * The OS NodeUpgrade might get stuck in the `NodeOSInPlaceUpgradePostProcessingCompleted` step. 
  * The OS NodeUpgrade might get stuck at package server creation. 

  * During a `gdcloud storage cp` or a `gdcloud system container-registry load-oci` operation from an OIC workstation, there is a slight chance that access to `org-infra` is lost followed by `org-mgmt`'s `kube-api` going down. 




**Resource Manager** :

  * Projects cannot be deleted from the GDC console. 

  * When creating a customer organization, the job `create-ansible-playbooks` that creates required Ansible playbooks fails. 

  * Organization deactivation doesn't decommission all resources provisioned for the organization. 




**Storage** :

  * Data unavailability across zones in the dual-zone buckets. 

  * Pods fail to mount due to a Trident `mkfs.ext4` error. 

  * The node upgrade is blocked. 

  * `file_block_zombie_luns_present` alert fires constantly. 

  * Noisy alerts in the StorageGRID Management console. 




**System Artifact Registry** :

  * Harbor artifact replication jobs get stuck. 

  * A false alarm can be triggered in response to transient errors when reconciling the `HarborRobotAccount` resource. 

  * There is a false alarm for the SAR-R0003 alert. 




**Ticketing system** :

  * The ServiceNow MID server fails to start properly. 

  * An RBAC error from customer networks might deny access to ServiceNow. 




**Upgrade** :

  * The support report fails. 

  * Ingester remains unhealthy and is not automatically forgotten after upgrade 




**Vertex AI** :

  * Vertex AI pre-trained models and workbooks are not enabled in version 1.14.3, but will be available in 1.14.4.



**Virtual Machines**

  * `VMDisk` might display an incorrect status of Phase: `InProgress` even when the underlying disk operations finish and the disk is ready for use. 

  * When you create a Windows VM using the gdcloud CLI CLI `gdcloud compute instances create`, the VM fails to boot due to the default BIOS boot type `bios` and missing secure boot flags. 




* * *

The following issues are fixed: 

**Harbor** :

  * Fixed the issue where the nodepool is stuck in a state of `Provisioning`. For more information, see [Known issues](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/known-issues/known-issues-113x#registry-mirror-not-deleted).



* * *

The following changes are identified: 

**Core** :

  * The requirements to interact with the org admin cluster and system cluster in several service workflows have been removed. The Management API server, which is available for managing all non-container workloads and services, serves as the replacement for all affected service workflows.

  * The global API server is provided by default for customer-managed resources that are designed for global deployment across a GDC universe. For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers).




**Marketplace** :

  * The **Marketplace Viewer** role permissions are restricted to view the available services only, with no access to the installed instances or their configurations. To view the configuration of running instances, users need the Marketplace Editor (`marketplace-editor`) role. 

  * A list of [Marketplace service images](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/mkt-images-1143) is available.




**Resource Manager** :

  * Removed the capability to attach a Kubernetes cluster when creating a project in the GDC console. You must attach Kubernetes clusters to a project from the **Kubernetes Engine > Clusters** page. For more information, see [Create a project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-a-project).



**Version updates** :

  * The Google Distributed Cloud for bare metal version is updated to 1.30.400-gke.133 to apply the latest security patches and important updates.   
  
See the [Google Distributed Cloud for bare metal 1.30.400-gke.133 release notes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/release-notes-ver#release_130300-gke133) for details.



**Virtual machines** :

  * Updated the Performance Test as a Service (PTaaS) documentation to include new names and descriptions for the available benchmarks in PTaaS. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
