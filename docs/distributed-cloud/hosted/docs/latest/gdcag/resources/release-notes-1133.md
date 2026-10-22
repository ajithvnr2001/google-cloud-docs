---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/release-notes-1133/
title: Google Distributed Cloud air-gapped 1.13.3 release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:54.558541+00:00
---

# Google Distributed Cloud air-gapped 1.13.3 release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/release-notes-1133/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Google Distributed Cloud air-gapped 1.13.3 release notes Stay organized with collections  Save and categorize content based on your preferences. 

## August 30, 2024

* * *

Announcement

Google Distributed Cloud (GDC) air-gapped 1.13.3 is available.  
See the [product overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/overview) to learn about the features of Distributed Cloud. 

* * *

Feature

**Cluster management** :

  * Introduced a broader set of [Multi-Instance GPU (MIG) profiles](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-node-machines#mig-profiles) (uniform & mixed mode). You can create Google Kubernetes Engine clusters on GPU VMs (A3 VMs) with a variety of GPU slicing schemes and dynamically address the GPU resource needs of services hosting artificial intelligence (AI) workloads.



**Hardware** :

  * New DL380a servers with the latest NVIDIA Hopper H100 GPUs (2x2 NVL), paired with the newest 5th Generation Intel processors are available.



**Virtual machines** :

  * A new GPU-optimized A3 VM type is available. The A3 VM type has 4x NVIDIA H100 80GB GPUs attached, which can run your AI workloads requiring large language models up to 100B parameters.
  * Smaller A3 VM shapes are introduced, with 1x H100 80GB GPU and 2x H100 80GB GPUs attached per VM. This feature is in Preview.



**Vertex AI** :

  * Included support for [new file formats of document translation (DOC, PPT, TXT, XLS)](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/quickstart-dvs).
  * Added the API and support for [batch document translation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/quickstart-dvs).
  * Supported a new format for the accelerator type of MIG GPUs [in the resource pool for online predictions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-deploy-model).
  * Supported the language auto-detect feature for [inline translations and documents stored in buckets](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/quickstart-dvs).
  * The API platform is in the production stage.



* * *

Security

Updated the Canonical Ubuntu OS image version to 20240811 to apply the latest security patches and important updates. To take advantage of the bug and security vulnerability fixes, you must upgrade all nodes with each release. The following security vulnerabilities are fixed: 

  * [CVE-2021-20230](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20230)
  * [CVE-2022-48655](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-48655)
  * [CVE-2022-4968](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4968)
  * [CVE-2022-48674](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-48674)
  * [CVE-2023-6270](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6270)
  * [CVE-2023-6597](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6597)
  * [CVE-2023-52752](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52752)
  * [CVE-2024-0397](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0397)
  * [CVE-2024-0450](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0450)
  * [CVE-2024-0760](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0760)
  * [CVE-2024-1724](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-1724)
  * [CVE-2024-1737](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-1737)
  * [CVE-2024-1975](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-1975)
  * [CVE-2024-2201](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-2201)
  * [CVE-2024-4032](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-4032)
  * [CVE-2024-4076](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-4076)
  * [CVE-2024-5569](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-5569)
  * [CVE-2024-6655](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6655)
  * [CVE-2024-7264](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-7264)
  * [CVE-2024-23307](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-23307)
  * [CVE-2024-24861](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-24861)
  * [CVE-2024-26583](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26583)
  * [CVE-2024-26584](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26584)
  * [CVE-2024-26585](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26585)
  * [CVE-2024-26586](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26586)
  * [CVE-2024-26642](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26642)
  * [CVE-2024-26643](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26643)
  * [CVE-2024-26828](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26828)
  * [CVE-2024-26886](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26886)
  * [CVE-2024-26889](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26889)
  * [CVE-2024-26907](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26907)
  * [CVE-2024-26922](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26922)
  * [CVE-2024-26923](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26923)
  * [CVE-2024-26925](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26925)
  * [CVE-2024-26926](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26926)
  * [CVE-2024-27019](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27019)
  * [CVE-2024-29068](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-29068)
  * [CVE-2024-29069](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-29069)
  * [CVE-2024-35235](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35235)
  * [CVE-2024-36016](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-36016)
  * [CVE-2024-37370](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-37370)
  * [CVE-2024-37371](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-37371)
  * [CVE-2024-38428](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-38428)



* * *

Security

Updated the Rocky OS image version to 20240731 to apply the latest security patches and important updates.

* * *

Issue

**Billing** :

  * User fails to create `BillingAccountBinding` due to validation webhook error. 



**Block storage** :

  * Grafana pods stuck in `Init` state due to volume mount errors. 
  * There is a Trident multi-attach error. 



**Database Service** :

  * The `dbs-fleet` subcomponent has a reconciliation error when upgrading. 
  * The `DBCluster` creation fails after upgrade. 



**Identity and access management** :

  * The `gatekeeper-audit` pods in the `opa-system` namespace frequently restart. 



**Monitoring** :

  * The Cortex store gateway pods can crashloop on startup while syncing with the storage backend. The pods exceed their memory limits, causing Kubernetes to terminate them. 
  * The Kube control-plane metrics proxy pods can crashloop with image pull backoff error. 
  * A growth in WAL (write-ahead log) causes Prometheus to use a lot of memory. The system control plane VM node reports `NodeHasInsufficientMemory` and `EvictionThresholdMet` events because of this issue. 



**Networking** :

  * The switch image failed to extract or pull an image. 



**Object storage** :

  * Some object storage upgrade warnings can be ignored. 



**Operating system** :

  * Pods are stuck in a `ContainerCreating` state on a single node. 



**Physical servers** :

  * The DL380a server fails to provision. 



**Upgrade** :

  * A Helm failure during upgrade causes a series of rollbacks. 
  * When upgrading from HW2.0 and Ubuntu, the node upgrade incorrectly displays RockyLinux. 
  * The `dhcp-tftp-core-server` pod is not drained. 
  * The `OrganizationUpgrade`is stuck at node upgrade stage. 
  * Intermittent connectivity failure to external cluster VIP. 
  * Kernel fails to create container. 
  * An `Incorrect version of Trident` error appears during upgrade. 
  * During user cluster provisioning, some pods fail to be scheduled. 
  * The tenant organization upgrade fails at the preflight check stage with `ErrImagePull`. 
  * The root org upgrade is stuck on a failed signature job. 
  * During upgrade, the task for a root organization fails due to missing service accounts. 
  * Upgrade fails on `shared-service-cluster upgrade`
  * The node fails during the user cluster upgrade. 
  * The root organization upgrade fails for preflight check. 
  * There is a persistent timeout during the initial root `organizationupgrade`. 
  * The `obj-syslog-server` subcomponent fails reconciliation in the root org. 



**Virtual machines** :

  * The NVIDIA device plugin `DaemonSet` fails with the `driver rpc error` message on cluster nodes with GPUs. This issue causes GPUs to be unavailable for virtual machines and pods. 
  * System cluster VM not ready. 
  * A data volume reports that the scratch space is not found. 
  * The `obj-syslog-server` subcomponent fails reconciliation in the root org. 



**Vertex AI** :

  * The `streaming_recognize` pre-trained API function of Speech-to-Text fails because of an issue with the client library. 
  * Job status polling is not supported for the `batchTranslateDocument` API. 
  * `batchTranslateDocument` requests might cause performance issues. 
  * The first time you enable pre-trained APIs, the GDC console might show an inconsistent status after a few minutes. 
  * Translation requests with more than 250 characters can crash `translation-prediction-server` pods. 
  * The `GPUAllocation` for shared service cluster is not configured correctly. 
  * When upgrading from version 1.9.x to 1.13.3, the Operable Component Lifecycle Management (OCLCM) controller for Vertex AI subcomponents might show errors. 
  * Translation requests might generate the `RESOURCE_EXHAUSTED` error code when the system frequency limit has been exceeded. 
  * `batchTranslateDocument` requests return error `503 "Batch Document translation is not implemented` if the `enableRAG` operable parameter is not set to `true` in the cluster. 



* * *

Fixed

**Monitoring** :

  * Fixed an issue where the Prober ConfigMap gets reset to include no probe jobs. 



**Networking** :

  * Fixed an issue with a `PodCIDR` not assigned to nodes even though a `ClusterCIDRConfig` is created. 



**Operating system** :

  * Fixed an issue with the `bm-system-machine-preflight-check` Ansible job for a bare metal or VM node failing with `Either ip_tables or nf_tables kernel module must be loaded`. 



**Physical servers** :

  * Fixed an issue with the server bootstrap failing due to POST issues on the HPE server. 



**Upgrade** :

  * Fixed an issue with upgrade failing in the `iac-zoneselection-global` subcomponent. 



**Vertex AI** :

  * Fixed an issue where the `MonitoringTarget` shows a `Not Ready` status when user clusters are being created, causing pre-trained APIs to continually show an `Enabling` state in the user interface. 



* * *

Change

**Add-on Manager** : 

  * The Google Distributed Cloud for bare metal version is updated to 1.29.300-gke.185 to apply the latest security patches and important updates. 

See [Google Distributed Cloud for bare metal 1.29.300-gke.185 release notes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/release-notes-ver#release_129300-gke185) for details.




**Upgrade** : 

  * The upgrade documentation provides estimated durations for the different stages of the upgrade process.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
