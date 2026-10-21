---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/release-notes-1162/
title: Google Distributed Cloud air-gapped 1.16.2 release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:09.866522+00:00
---

# Google Distributed Cloud air-gapped 1.16.2 release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/release-notes-1162/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Google Distributed Cloud air-gapped 1.16.2 release notes Stay organized with collections  Save and categorize content based on your preferences. 

## July 27, 2026

* * *

Announcement

Google Distributed Cloud (GDC) air-gapped 1.16.2 is available.  
See the [product overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/overview) to learn about the features of Distributed Cloud. 

* * *

Feature

The following new features are available: 

**Backup and restore**

  * Added the `maxConcurrency` attribute in the `spec` field of the `ClusterBackupPlan` and `VirtualmachineBackupPlan` custom resources. For more information, see [Plan backups](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/plan-backups) and [Create a scheduled backup plan](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/backup-plans/create-scheduled-backup-plan).



**Cluster management**

  * Added support for [creating](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-standard-cluster#console), [deleting](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/delete-standard-cluster#console), [editing](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/manage-node-pools#console), and [viewing](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster#console_2) standard Kubernetes clusters in the GDC console.



**Networking**

  * Added support for [configuring explicit deny project network policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/deny-traffic) as a [Preview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/feature-stages#preview) feature to restrict connectivity between workloads and services in different projects or CIDR ranges.

  * Added support for targeting specific cluster nodes by IP address or CIDR range using the `ipBlock` field in [Kubernetes network policies for standard clusters](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/k8s-network-policy/standard-cluster-traffic#create-node-policy) and the `ipBlocks` field in [project network policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/pnp-overview#node-selection-considerations) as a [Preview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/feature-stages#preview) feature.




**Virtual machines**

  * Added a `taints` patch to the `OrganizationZonalConfig` resource for high performance computing (HPC) optimizations. 

  * Added support for [NVIDIA GPU driver installation on Windows VMs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-the-os/install-nvidia-drivers-win).




* * *

Issue

The following issues are identified: 

**Cluster management**

  * Kubernetes cluster deletion stops responding because a LUKS secret remains stuck in the terminating namespace. 



**Harbor**

  * The `gdcloud harbor backup-plans` command group is missing the `update` and `delete` commands, returning a `command not found` error when run. 



**Infrastructure as code**

  * There are reconciliation errors during an upgrade from 1.15.2 or later. 



**Inventory**

  * Incorrect data plane network bond generated on `Cell`, `Server`, and `BaremetalHostNetwork` custom resources for B300 (`d4-highgpu2-256-gdc-metal`) servers when `fe-s6p1` and `fe-s6p2` aren't ordered first in `devices.csv`. 



**Monitoring**

  * Cortex `VirtualService` and `IstioAuthorizationResource` resources, and Grafana `IstioAuthorizationResource` resources, remain in the cluster after a project is deleted. 

  * Certificate secrets are leaked when deleting a `MonitoringTarget`. 

  * The Grafana dashboard link from a standard cluster details page in the GDC console incorrectly redirects you to the `platform-obs` dashboard instead of loading data for the selected project. 

  * You can safely ignore or disable certain high-frequency alerts. 




**Security Information and Event Management (SIEM)**

  * Subcomponent `siem-aas-global` fails to reconcile in the org management plane. 



**Storage**

  * Default keep lists filter out required metrics from Grafana. 

  * Dual-zone buckets can't be deleted from the console. 




**Upgrade**

  * The `sar` preflight upgrade check fails if `gdcloud system container-registry load-oci` is run with `--trigger-signature-verification=true`, because both the command and the organization upgrade preflight check create `artifact-signature-verification` jobs in the `package-validation-system` namespace. 

  * While upgrading to 1.16.2, the `atat-invoice-export` and `atat-portfolio` subcomponents in the `root` namespace might enter a `ReconciliationError` state. 




**Vertex AI**

  * Vertex AI Service Usage dashboards display a `No data` state because the PromQL queries contain restrictive filters for NVIDIA resources and Workbench labels that might not be present in the environment. 



**Virtual machines**

  * VMs in tenant organizations that use the package repository servers of the `gdchservices` organization can't install or update packages from `pkg.org.internal` and receive `503 Service Unavailable` errors, because the `pkg-infra-cert` certificate is generated without the DNS suffix. 



**Vulnerability management**

  * During an upgrade from 1.16.1 to 1.16.2, the `lcm.private.gdc.goog/opsservices` label is removed from OIRv2 `opsservices` APIs. 



* * *

Fixed

The following issues are fixed: 

**Documentation**

  * Stale documentation shipped with the product release. 



**GDC console**

  * Documentation hosted in the GDC console shows a 404 error. 



**gdcloud CLI**

  * Running any gdcloud CLI command prints an uninitialized feature flag warning. 



**Networking**

  * Enabling Cloud NAT on a VM prevents SSH connections using the GDC console UI. 



**Network Time Protocol (NTP)**

  * When deploying OIRv2 management switches, NTP configuration and encryption might not apply to the running configuration. 



**Servers**

  * Bootstrapper installation fails during file system configuration with a `matched no disk` error. 



**Storage**

  * The ONTAP S3 event audit logging is disabled. 



**Ticketing system**

  * The `ts-app-server-1` pod restarts periodically. 



**Virtual machines**

  * VM creation with types `a3-ultragpu-8g` and `a4-ultragpu-8g` on a newly reprovisioned server fails with errors. 

  * `gpu-controller-controller-manager pod` enters an `ImagePullBackOff` state during upgrade to release 1.16.1. 




**Vulnerability management** :

  * Vulnerability management subcomponents and system `UserAccount` SSH key generation might get stuck due to a container runtime deadlock and Helm parameter cache poisoning. 



* * *

Change

The following changes are identified: 

**Version updates** :

  * The Google Distributed Cloud for bare metal version is updated to 1.32.1300-gke.46 to apply the latest security patches and important updates. 



* * *

Deprecated

The following features are deprecated: 

**Database services**

  * The Database Service for PostgreSQL is now powered by AlloyDB Omni. Database Service for AlloyDB Omni will no longer be available as a standalone managed service. Instead, customers looking to use AlloyDB Omni as a managed service should transition to the Database Service for PostgreSQL, which is powered by AlloyDB Omni. Additionally, Database Service for Oracle, a managed offering, is deprecated but the option to self-manage Oracle deployments remains fully supported. For more information on self-managing Oracle databases, refer to the [solution guides](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/db-self-managed-oracle-ref-arc). To support your planning, starting June 29, 2026 and ending on June 29, 2027, we are providing a 12-month discontinuation period for Database Service for AlloyDB Omni and Database Service for Oracle.



**Virtual machines**

  * Distributed Cloud deprecates enabling external access using `VirtualMachineExternalAccess` during VM creation in the GDC console. To manage external networking, create an External Load Balancer (ELB) for ingress and a Cloud NAT Gateway for egress.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
