---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/release-notes-1151/
title: Google Distributed Cloud air-gapped 1.15.1 release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:01:25.842267+00:00
---

# Google Distributed Cloud air-gapped 1.15.1 release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/release-notes-1151/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Google Distributed Cloud air-gapped 1.15.1 release notes Stay organized with collections  Save and categorize content based on your preferences. 

## December 5, 2025

* * *

Announcement

Google Distributed Cloud (GDC) air-gapped 1.15.1 is available.  
See the [product overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/overview) to learn about the features of Distributed Cloud. 

* * *

Feature

The following new features are available: 

**Cluster management** :

  * Added the new standard cluster configuration. Standard clusters are scoped to a single project, which gives application developers that are confined within a project direct control over how it functions. For more information, see [Kubernetes cluster configurations](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs).



**gdcloud CLI** :

  * Added support for running the gdcloud CLI from macOS and Windows operating systems. For more information, see [Available gdcloud CLI bundles](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview#cli-support).

  * Added a _lite_ version of the gdcloud CLI bundle for Linux, which provides a smaller binary with a subset of gdcloud CLI commands. For more information, see [Available gdcloud CLI bundles](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview#cli-support).




**Networking**

  * A new egress NAT functionality, Cloud NAT, has been added, which provides many more options for configuring how workloads reach outside the organization. For more information, see [Cloud NAT](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cloud-nat). The previously available nat mechanism, known as project default egress NAT, has been deprecated; users are encouraged to [migrate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/default-egress#migrate-to-cloud-nat) to Cloud NAT.

In the 1.15.1 release, the Cloud NAT role `cloud-nat-manager` has been deprecated; use `cloud-nat-developer` instead.

  * Added subnet groups to simplify IP address allocation. This new mechanism enables you to manage subnets of the same entity or same purpose as a group, simplifying the allocation of IP addresses from large sets of managed subnets. For more information, see [Subnet groups](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/subnets-overview#subnet-groups).

  * Interconnect subscription SKUs are available as a public Preview. This feature lets organizations reserve physical capacity on interconnects and associate the reservation to a billing project. The reservation is honor-based only at this time, and is not strictly enforced by the system. For more information about interconnects, see [Establish connectivity with interconnects](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/interconnects/interconnect-overview).

  * Health checks using HTTP/HTTPS protocols are now available. A health check dictates whether an endpoint is eligible to receive new requests or connections. An unhealthy endpoint, as identified by the health check, won't receive traffic through the load balancer. For more information, see [Configure health checks](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/health-checks).

  * Added support for monitoring of IP resource statistics as a Preview feature. Infrastructure Operators (IO) and Platform Administrators (PA) can view total, allocated, available, and percentage metrics for subnets from root to leaf level as well as for subnet groups. See [Query and view metrics](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/query-and-view-metrics) for guidance on how to access dashboards.

  * Newly created organizations now bypass the Intrusion Detection and Prevention System (IDPS) service for customer traffic by default. Existing organizations are not affected by this change and continue to use IDPS based on their existing configuration. 




**Platform authentication** :

  * Certificate Authority Service (CAS) supports [predefined certificate templates](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/ca-service/predefined-certificate-templates), offering ready-made templates to issue certificates for common use cases.
  * CAS supports [certificate revocation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/ca-service/revoke-cert) by publishing Certificate Revocation Lists (CRLs) that client applications can check.



**Resource Manager** :

  * Added project tags as a Preview feature. Tags let you organize projects based on business attributes. For more information, see [Tags overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/project-tags).



**Security service** :

  * Customer traffic to and from newly created organizations now bypasses IDPS inspection by default. 



**System** :

  * Published system limits that apply to GDC components. System limits are fixed values that cannot be changed. For more information, see [System limits](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/system-limits).



**Virtual machines** :

  * Added NVIDIA GPU support for VM instances, which lets you run various GPU-accelerated workloads, for example, artificial intelligence (AI). For more information, see [Create and start a VM instance with NVIDIA GPUs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-a-vm/create-vm-gpu).
  * Added H200 GPU support with the `a3-ultragpu` virtual machine family. 
  * Added [configure Tier 1 networking for VMs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/vm-config-network). VMs with Tier 1 networking configurations are useful for large, distributed compute workloads with heavy internode communications, such as high performance computing (HPC), machine learning (ML), and deep learning (DL).
  * Added the ability to [create high-performance VMs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/vm-high-mem).
  * Added [VM availability checks](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/config-resiliency) that offer insight into VM status.
  * Added the ability to manage package repositories. 



* * *

Security

Updated the Rocky OS image version to 20250924 to apply the latest security patches and important updates. 

The following security vulnerabilities are fixed:

  * [CVE-2021-47013](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-47013)
  * [CVE-2021-47670](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-47670)
  * [CVE-2022-1048](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1048)
  * [CVE-2022-1679](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1679)
  * [CVE-2022-2938](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2938)
  * [CVE-2022-3239](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3239)
  * [CVE-2022-3545](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3545)
  * [CVE-2022-3625](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3625)
  * [CVE-2022-4139](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4139)
  * [CVE-2022-4378](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4378)
  * [CVE-2022-20141](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-20141)
  * [CVE-2022-20368](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-20368)
  * [CVE-2022-28390](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-28390)
  * [CVE-2022-29581](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29581)
  * [CVE-2022-39189](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-39189)
  * [CVE-2022-41674](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41674)
  * [CVE-2022-41858](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41858)
  * [CVE-2022-45886](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-45886)
  * [CVE-2022-45919](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-45919)
  * [CVE-2022-48637](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-48637)
  * [CVE-2022-48839](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-48839)
  * [CVE-2022-48919](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-48919)
  * [CVE-2022-49011](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-49011)
  * [CVE-2022-49058](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-49058)
  * [CVE-2022-49111](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-49111)
  * [CVE-2022-49136](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-49136)
  * [CVE-2022-49291](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-49291)
  * [CVE-2022-49788](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-49788)
  * [CVE-2022-49977](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-49977)
  * [CVE-2022-49985](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-49985)
  * [CVE-2022-50020](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-50020)
  * [CVE-2022-50022](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-50022)
  * [CVE-2023-0266](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0266)
  * [CVE-2023-0386](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0386)
  * [CVE-2023-1281](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1281)
  * [CVE-2023-1829](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1829)
  * [CVE-2023-1838](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1838)
  * [CVE-2023-2124](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2124)
  * [CVE-2023-2163](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2163)
  * [CVE-2023-2235](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2235)
  * [CVE-2023-2513](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2513)
  * [CVE-2023-3090](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3090)
  * [CVE-2023-3390](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3390)
  * [CVE-2023-3567](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3567)
  * [CVE-2023-3609](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3609)
  * [CVE-2023-3611](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3611)
  * [CVE-2023-3776](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3776)
  * [CVE-2023-3812](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3812)
  * [CVE-2023-4004](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4004)
  * [CVE-2023-4128](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4128)
  * [CVE-2023-4206](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4206)
  * [CVE-2023-4207](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4207)
  * [CVE-2023-4208](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4208)
  * [CVE-2023-5178](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5178)
  * [CVE-2023-6040](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6040)
  * [CVE-2023-6546](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6546)
  * [CVE-2023-6817](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6817)
  * [CVE-2023-6931](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6931)
  * [CVE-2023-6932](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6932)
  * [CVE-2023-28466](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28466)
  * [CVE-2023-31436](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-31436)
  * [CVE-2023-32233](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-32233)
  * [CVE-2023-35001](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35001)
  * [CVE-2023-35788](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35788)
  * [CVE-2023-40283](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-40283)
  * [CVE-2023-42753](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-42753)
  * [CVE-2023-44466](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-44466)
  * [CVE-2023-45871](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45871)
  * [CVE-2023-51042](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51042)
  * [CVE-2023-51779](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51779)
  * [CVE-2023-52439](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52439)
  * [CVE-2024-1086](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-1086)
  * [CVE-2024-25742](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-25742)
  * [CVE-2024-26665](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26665)
  * [CVE-2024-26669](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26669)
  * [CVE-2024-36883](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36883)
  * [CVE-2024-36960](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36960)
  * [CVE-2024-38581](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-38581)
  * [CVE-2024-41013](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41013)
  * [CVE-2024-42094](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42094)
  * [CVE-2024-42284](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-42284)
  * [CVE-2024-43842](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43842)
  * [CVE-2024-44970](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-44970)
  * [CVE-2024-46858](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-46858)
  * [CVE-2024-50301](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-50301)
  * [CVE-2025-22004](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-22004)
  * [CVE-2025-23150](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-23150)
  * [CVE-2025-37738](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-37738)
  * [CVE-2025-37890](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-37890)
  * [CVE-2025-38001](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38001)
  * [CVE-2025-38079](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38079)
  * [CVE-2025-38086](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38086)
  * [CVE-2025-38352](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38352)
  * [CVE-2025-38380](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-38380)



* * *

Issue

The following issues are identified: 

**Resource Manager** :

  * Organization in Unknown state due to missing failover registry distributions. 



**Anthos Service Mesh**

  * ASM mesh installation is blocked due to unhealthy node preventing CNI installation. 



**Backup and restore**

  * Backup and restore operations fail due to the `back-lancer-agent-user-cp` subcomponent being in `ReconciliationError` status after an upgrade. 

  * Restores involving volumes may take longer to complete due to slow data transfer rates. 

  * The restore process for a resource, such as a database clone or user workload restore, gets stuck and eventually times out due to a pending persistent volume claim. 

  * Users cannot create VM backup plans or perform end-to-end backup and restore tasks with the GDC console. 

  * The restore operation fails for cluster backups. 




**Block storage**

  * User pod freezes during volume unmount request. 

  * A `Volume already exists` error during CloneVolume is not addressed by the Trident API. 

  * Volumes fail to attach due to the presence of inactive LUNs. 

  * A `FailedMount` error occurs during upgrades due to the inability to find the `csi.trident.netapp.io` driver. 

  * File/block storage sessions aren't recovering automatically after events such as a storage upgrade or storage controller outage. 

  * ONTAP cluster upgrade never finishes due to giveback not being completed. 




**Cluster management**

  * Cluster gets stuck in a deleting state. 

  * Kubernetes cluster is not removed after deletion. 




**Database service**

  * The `gdcloud stop database` command takes a long time to complete. 

  * If a PostgreSQL or AlloyDB Omni database cluster is stopped while high availability (HA) is enabled, it might not restart successfully. 




**Firewall**

  * Legacy firewall rules might block organization to root admin traffic after upgrade. 

  * After an `AttachmentGroup` is deployed, if the `identifier` field in that `AttachmentGroup` object is the same as `orgName`, the firewall fails to parse this object and the firewall config update gets stuck. 

  * IDPS firewall generates invalid configuration due to race condition when creating multiple organizations at the same time. 




**Harbor** :

  * The database password rotation is stuck. 

  * A full Harbor database disk leads to service unavailability. 




**Hardware security module** :

  * Deactivated trial licenses are still detectable in CipherTrust Manager, triggering false expiration warnings. 

  * A file descriptor leak causes a `ServicesNotStarted` error. 




**Health** :

  * During deployment, the `health-slo-reports-infra` subcomponent can fail to reconcile due to a missing `telex-system` namespace. 



**Identity and access management**

  * A `CustomRole` resource that includes a `zonalRules` section might not grant permissions reliably. 

  * An OPA Gatekeeper trust issue after a root CA rotation prevents IAM role creation in new projects. 




**Infrastructure as Code**

  * Attempts to sign in to GitLab using Firefox fail with an error 422. 



**Inventory**

  * The `system assets create` doesn't accept correct ports for firewall devices. 



**Key management system** :

  * KMS servers might experience performance issues and `OOMKilling` under heavy workloads. 

  * KMS configured to use a CTM root key does not failover when an HSM is unavailable. 




**Monitoring**

  * If new `KubeStateMetric` Custom Resources are created, their metrics might not show up. 

  * Cortex compaction failures can be caused by corrupted blocks, leading to various problems, including errors in Grafana metric queries, gaps in recording rules, and error logs appearing in Cortex pods. 

  * Pods stuck in Pending state due to volume node affinity conflict. 

  * "Too many outstanding requests" error message is shown when viewing dashboards in grafana. 

  * Metric time series exceeding the cardinality threshold are dropped, leading to incomplete data for some metrics. 




**Networking**

  * Enabling node-to-node IP address security (IPsec) encryption at runtime for an existing organization might cause network packet drops and connection timeouts. 

  * ForwardingRule resource deletion hangs in the `Deleting` state when the resource is in a `NotReady` state. 




**Object Storage**

  * Data unavailability across zones in the dual-zone buckets. 

  * The `ObjectStorageSite` is not ready after upgrade to 1.15.x. 

  * Object Storage bucket failed to create in new org if StorageGrid version is 11.9 or later. 

  * StorageGRID load balancer endpoint server certificates don't automatically rotate. 

  * gdcloud CLI fails to create or delete dual-zone buckets for project-level users. 

  * The OBJ-A0003 alert (audit logging failure) fires frequently and resolves on its own within an hour of firing. To reduce the noise caused by this alert, silence the alert. 

  * The bundle contains an incorrect installation version of StorageGRID, 11.8.0 instead of 11.9.0. After bootstrapping StorageGRID with version 11.8.0, you must manually upgrade to version 11.9.0.6. 




**OS** :

  * OS policy resources can be slow to reconcile when there are a large number of servers provisioned. 

  * During a `gdcloud storage cp` or a `gdcloud system container-registry load-oci` operation from an OIC workstation, there is a slight chance that access to `org-infra` is lost followed by `org-mgmt`'s `kube-api` going down. 

  * A PLATAUTH alert might trigger due to a OS rotatable secret rotation failure. 




**Platform authentication** :

  * Errors can occur when using a wildcard certificate for the infra web PKI while in BYO Cert mode. 

  * Creating excessive certificate requests might impact API server stability. 




**Resource Manager** :

  * The postflight check fails. 
  * Organization in unknown state due to missing failover registry distributions. 



**Ticketing system** :

  * An RBAC error from customer networks might deny access to ServiceNow. 

  * ServiceNow can't reach the customer OIDC IDP. 

  * Previously resolved incidents are reopened in ServiceNow. 

  * The `ts-app-server-1` pod restarts periodically. 




**Upgrades** :

  * When upgrading from 1.14.7 or earlier release to 1.15.x, for best results, we recommend the following steps:

    * Upgrade to version 1.14.7.
    * Apply hotfix2.
    * Proceed with the upgrade to 1.15.1.
  * The cluster upgrade is blocked due to a node failing to enter maintenance mode. 

  * The `siem-cluster` subcomponent is unresponsive. 




**Vertex AI** :

  * Disabling the Translation API might fail with the following error: `Failed to disable translation API: VAI3002: Failed to patch subresource: failed to patch ODSPostgresDBCluster resource`. 

  * Unable to establish connection with the Jupyter server. 

  * Endpoint CR deletion fails to remove "Online Prediction" endpoint. 




**Virtual machines** :

* VM disk provisioning gets stuck because the VMM controller can't find the existing secrets. `VirtualMachineDisk` stays in a `pending` state.

* When you create a Windows VM using the gdcloud CLI CLI `gdcloud compute instances create`, the VM fails to boot due to the default BIOS boot type `bios` and missing secure boot flags. 

* When you import a VM disk image using the `gdcloud compute images import` command or the `VirtualMachineImageImport` custom resource, the import operation gets stuck at the `JobImport` stage if the `VirtualMachineImageImport` resource name exceeds 33 characters (or 28 characters for the image name passed to the gdcloud CLI). 

**Vulnerability management** :

  * Vulnerability management subcomponents and system `UserAccount` SSH key generation might get stuck due to a container runtime deadlock and Helm parameter cache poisoning. 



* * *

Fixed

The following issues are fixed: 

**Anthos Service Mesh** :

  * Misleading alerts with critical and error severity might fire in large meshes as `controlplane_latency_slo` does not take mesh size into account. 



**Backup and restore** :

  * The backup control plane pod crashes due to insufficient memory. 



**Storage** :

  * The HA group name is too long. 

  * Fixed an issue where the `--location` and `--location-type` flags for `gdcloud storage` commands were incorrectly applied to zonal buckets; these flags are now correctly restricted to dual-zone buckets.




**Key management system** :

  * When the `kms-rootkey-controller` memory usage exceeds the `1100Mi` limit, the controller enters a `CrashLoopBackOff` due to an `OOMKilled` status. 

  * KMS pods in the root organization might crash due to audit logs filling ephemeral storage. 




* * *

Change

The following changes are identified: 

**Version updates** :

  * The Google Distributed Cloud for bare metal version is updated to 1.30.1000-gke.85 to apply the latest security patches and important updates.   
  
For more information, see the [Google Distributed Cloud for bare metal 1.30.1000 release notes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/release-notes#June_10_2025) .



* * *

Deprecated

The following features are deprecated: 

**Virtual machines** :

  * The ability to create a VM instance without specifying a machine type is deprecated. You must specify a machine type when you create an instance. For more information, see [Create and start a VM instance](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-a-vm/create-and-start).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
