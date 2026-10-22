---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/release-notes-1124/
title: Google Distributed Cloud air-gapped 1.12.4 release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:00:11.933559+00:00
---

# Google Distributed Cloud air-gapped 1.12.4 release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/release-notes-1124/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Google Distributed Cloud air-gapped 1.12.4 release notes Stay organized with collections  Save and categorize content based on your preferences. 

## August 26, 2024

* * *

Announcement

Google Distributed Cloud (GDC) air-gapped 1.12.4 is available.  
See the [product overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/overview) to learn about the features of Distributed Cloud.

* * *

Security

Updated the Canonical Ubuntu OS image version to 20240621 to apply the latest security patches and important updates. To take advantage of the bug and security vulnerability fixes, you must upgrade all nodes with each release. The following security vulnerabilities are fixed: 

  * [CVE-2015-1197](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-1197)
  * [CVE-2016-9840](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-9840)
  * [CVE-2016-9841](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-9841)
  * [CVE-2018-25032](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-25032)
  * [CVE-2020-26570](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-26570)
  * [CVE-2020-26571](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-26571)
  * [CVE-2020-26572](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-26572)
  * [CVE-2021-47063](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-47063)
  * [CVE-2021-47070](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-47070)
  * [CVE-2022-28948](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-28948)
  * [CVE-2022-37434](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-37434)
  * [CVE-2022-48622](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-48622)
  * [CVE-2023-0340](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0340)
  * [CVE-2023-2861](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2861)
  * [CVE-2023-3164](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3164)
  * [CVE-2023-1523](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1523)
  * [CVE-2023-4408](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4408)
  * [CVE-2023-4421](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4421)
  * [CVE-2023-4641](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4641)
  * [CVE-2023-5517](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5517)
  * [CVE-2023-5388](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5388)
  * [CVE-2023-6135](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6135)
  * [CVE-2023-6228](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6228)
  * [CVE-2023-6277](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6277)
  * [CVE-2023-6516](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6516)
  * [CVE-2023-6915](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6915)
  * [CVE-2023-7207](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-7207)
  * [CVE-2023-22655](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-22655)
  * [CVE-2023-22995](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-22995)
  * [CVE-2023-23000](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-23000)
  * [CVE-2023-23004](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-23004)
  * [CVE-2023-24023](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24023)
  * [CVE-2023-28746](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28746)
  * [CVE-2023-38575](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38575)
  * [CVE-2023-39368](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39368)
  * [CVE-2023-43490](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-43490)
  * [CVE-2023-45733](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45733)
  * [CVE-2023-45745](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45745)
  * [CVE-2023-46103](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-46103)
  * [CVE-2023-46838](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-46838)
  * [CVE-2023-47233](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-47233)
  * [CVE-2023-47855](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-47855)
  * [CVE-2023-48733](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-48733)
  * [CVE-2023-50387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-50387)
  * [CVE-2023-50782](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-50782)
  * [CVE-2023-50868](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-50868)
  * [CVE-2023-51779](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51779)
  * [CVE-2023-51781](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51781)
  * [CVE-2023-51782](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51782)
  * [CVE-2023-52356](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52356)
  * [CVE-2023-52530](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52530)
  * [CVE-2023-52600](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52600)
  * [CVE-2023-52603](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52603)
  * [CVE-2024-0565](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0565)
  * [CVE-2024-0607](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0607)
  * [CVE-2024-0646](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0646)
  * [CVE-2024-1086](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-1086)
  * [CVE-2024-1441](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-1441)
  * [CVE-2024-2398](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-2398)
  * [CVE-2024-2494](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-2494)
  * [CVE-2024-2496](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-2496)
  * [CVE-2024-2961](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-2961)
  * [CVE-2024-3094](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-3094)
  * [CVE-2024-3651](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-3651)
  * [CVE-2024-4453](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-4453)
  * [CVE-2024-5197](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-5197)
  * [CVE-2024-22667](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-22667)
  * [CVE-2024-23851](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-23851)
  * [CVE-2024-24806](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-24806)
  * [CVE-2024-24855](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-24855)
  * [CVE-2024-26581](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26581)
  * [CVE-2024-26589](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26589)
  * [CVE-2024-26614](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26614)
  * [CVE-2024-26622](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26622)
  * [CVE-2024-26712](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26712)
  * [CVE-2024-26733](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26733)
  * [CVE-2024-28085](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-28085)
  * [CVE-2024-28182](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-28182)
  * [CVE-2024-28834](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-28834)
  * [CVE-2024-33599](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-33599)
  * [CVE-2024-33600](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-33600)
  * [CVE-2024-33601](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-33601)
  * [CVE-2024-33602](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-33602)
  * [CVE-2024-34064](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-34064)
  * [CVE-2024-34397](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-34397)
  * [CVE-2024-37535](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-37535)



* * *

Security

The following container image security vulnerabilities are fixed:

  * [CVE-2023-5981](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5981)
  * [CVE-2024-0553](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0553)
  * [CVE-2024-24786](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-24786)



* * *

Security

Fixed vulnerabilities in the GDC console where strict transport security was not enforced. 

* * *

Security

Fixed a vulnerability with Microsoft Visual Studio Code in Operations Suite Infrastructure (OI) by updating Microsoft Visual Studio Code to version 1.88.1.

* * *

Issue

**Backup and restore** :

  * Persistent volumes that are backed up cannot be deleted. 



**Billing** :

  * The `bil-storage-system-cluster` subcomponent fails to reconcile due to stale jobs. 



**Block storage** :

  * Grafana pods stuck in `Init` state due to volume mount errors. 



**DNS** :

  * Org creation fails because DNS traffic to the root admin node ages out. 



**Istio** :

  * The `istio-eastwestgateway` deployment in the `istio-system` namespace is stuck. 



**Logging** :

  * The write-ahead log (WAL) can fill the persistent volume (PV) if a Loki pod cannot connect to the storage bucket for hours. 



**Networking**

  * A `PodCIDR` is not assigned to nodes even though a `ClusterCIDRConfig` is created. 
  * The`machine-init` job fails during upgrade. 



**Object storage** :

  * The creation of a new org gets stuck on the `VMImageDistributing` state. 
  * Some object storage upgrade warnings can be ignored. 



**Operations Suite Infrastructure (OI)** :

  * The Fluent Bit installer path is incorrect. 
  * The Nessus installer path is incorrect. 



**Performance** :

  * The `perf-ptaas` subcomponent fails to reconcile due to failure to transfer ownership. 



**Physical servers** :

  * The server bootstrap fails. 
  * The server's iLO can't connect to key manager.




**Upgrade** :

  * The management IP of a server is unreachable during upgrade. 
  * A provisioned server might fail to boot and get stuck at retrieving encryption keys. 
  * There is an issue with ongoing reconciliation in a subcomponent. 
  * When upgrading from 1.12.2 to 1.12.4, the `file-netapp-trident` subcomponent is stuck on the deletion of `StorageClasses`. 
  * An `ansibleplaybook` is not upgraded as part of the cluster upgrade. 
  * The IAM preflight check fails. 
  * The version number for `storagecluster` is not displayed during upgrade. 
  * `OrganizationUpgrade` status is `Unknown`, after an upgrade is completed. 
  * The `opa gatekeeper` subcomponent upgrade fails. 
  * Jobs are scheduled continuously. 
  * The `file-netapp-trident` subcomponent upgrade has a `Reconciliation ongoing` status. 
  * The system cluster cluster worker node upgrade fails to generate the delta between `manifest` and `snapshot`. 
  * `kubelet` fails to remove `cgroup` for pods with spamming logs. 
  * A healthy upstream for the ticketing system is not available. 



**Vertex AI** :

  * The `MonitoringTarget` shows a `Not Ready` status when user clusters are being created, causing pre-trained APIs to continually show an `Enabling` state in the user interface. 



* * *

Fixed

**Backup and restore** :

  * Fixed an issue where alerts for a backup repository may fire even when the repository is healthy. 



**Block storage** :

  * Fixed an issue where HSM certificates in the `StorageClusterReconciler` are not parsed correctly. 
  * Fixed an issue where performance storage classes don't have LUKS encryption enabled. 



**Cluster management** :

  * Fixed an issue where user clusters with Kubernetes version 1.27.x might have node pools that fail to initialize. 



**Hardware security module** :

  * Fixed an issue where a rotatable secret for hardware security modules is in an unknown state. 



**Identity and access management**

  * Fixed an issue where running the elevated access script added a duplicate entry in the `kustomization.yaml` file. 



**Monitoring** :

  * Fixed an issue where the `mon-common` subcomponent doesn't deploy the Istio Telemetry object on the `mon-system` namespace. 
  * Fixed an issue where the metrics storage class is incorrectly defined in the configuration. 
  * Fixed an issue where the Prober ConfigMap gets reset to include no probe jobs. 



**NTP server** :

  * Fixed an issue with the NTP server having unsynchronized time. 



**Physical servers** :

  * Fixed an issue where the server bootstrap fails due to a nil pointer dereference. 



**Resource Manager** :

  * Fixed an issue where `ProjectRoleBinding` custom resources were propagating to Kubernetes clusters that weren't ready. 



**Ticketing system** :

  * Fixed an issue where the ticketing system has no healthy upstream. 



**Upgrade** :

  * Fixed an issue where the OS upgrade could prematurely fail due to a short reboot policy period. 
  * Fixed an issue where the `HSMupgrade` fails during upgrade. 
  * Fixed an issue where the `file-observability` subcomponent fails on the `org-1-system-cluster` during upgrade. 



**Virtual machine management:**

  * Fixed an issue where the `VirtualMachineDisk` custom resource showed the `Failed` state after provisioning the underlying storage successfully. 
  * Fixed an issue where cluster provisioning in VM disks took a lengthy time to complete. 
  * Fixed an issue where a `VMRuntime` might not be ready due to a `network-controller-manager` installation failure. 



* * *

Change

**Add-on Manager** : 

  * The Google Distributed Cloud version is updated to 1.28.500-gke.120 to apply the latest security patches and important updates. 

See the [Google Distributed Cloud 1.28.500-gke.120 release notes](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/release-notes-ver-1#release_128500-gke120) for details.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
