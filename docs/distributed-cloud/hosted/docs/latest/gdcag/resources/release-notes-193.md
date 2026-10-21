---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/release-notes-193/
title: Google Distributed Cloud air-gapped 1.9.3 release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:31.456830+00:00
---

# Google Distributed Cloud air-gapped 1.9.3 release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/release-notes-193/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Google Distributed Cloud air-gapped 1.9.3 release notes Stay organized with collections  Save and categorize content based on your preferences. 

## April 28, 2023 [GDC 1.9.3]

* * *

Announcement

Google Distributed Cloud air-gapped 1.9.3 is now released.

See the [product overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/overview) to learn about the features of Google Distributed Cloud air-gapped.

* * *

The Google Distributed Cloud air-gapped 1.9.3 audit logging (AL) operable component introduces an enhancement for AuditLoggingTargets. Kubernetes objects created by an AuditLoggingTarget CR are now self-healed if they are updated or deleted.

* * *

Change

Updated Google Distributed Cloud version to 1.14.4-gke.4 to apply the latest security patches and important updates. 

See [ the Google Distributed Cloud release notes](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/release-notes-ver) for the latest information.

* * *

Change

The Google Distributed Cloud air-gapped 1.9.3 user interface (UI) now includes a message to inform you about the maximum worker node amount with the current control plane setting and pod CIDR option when you create a cluster. 

* * *

Security

The following container image security vulnerabilities are fixed:

  * [CVE-2021-46848](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46848)
  * [CVE-2022-1354](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1354)
  * [CVE-2022-1355](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1355)
  * [CVE-2022-2056](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2056)
  * [CVE-2022-2057](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2057)
  * [CVE-2022-2058](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2058)
  * [CVE-2022-2097](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2097)
  * [CVE-2022-23521](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23521)
  * [CVE-2022-24765](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24765)
  * [CVE-2022-2867](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2867)
  * [CVE-2022-2868](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2868)
  * [CVE-2022-2869](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2869)
  * [CVE-2022-29187](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29187)
  * [CVE-2022-32221](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32221)
  * [CVE-2022-34526](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-34526)
  * [CVE-2022-3570](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3570)
  * [CVE-2022-3597](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3597)
  * [CVE-2022-3598](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3598)
  * [CVE-2022-3599](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3599)
  * [CVE-2022-3626](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3626)
  * [CVE-2022-3627](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3627)
  * [CVE-2022-3970](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3970)
  * [CVE-2022-39253](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-39253)
  * [CVE-2022-39260 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-39260)
  * [CVE-2022-41903 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41903)
  * [CVE-2022-42898](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42898)
  * [CVE-2022-4304](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4304)
  * [CVE-2022-4450](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4450)
  * [CVE-2022-4645](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4645)
  * [CVE-2022-48281](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-48281)
  * [CVE-2023-0215](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0215)
  * [CVE-2023-0286](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0286)
  * [CVE-2023-0361](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0361)
  * [CVE-2023-0795](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0795)
  * [CVE-2023-0796](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0796)
  * [CVE-2023-0797](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0797)
  * [CVE-2023-0798](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0798)
  * [CVE-2023-0799](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0799)
  * [CVE-2023-0800](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0800)
  * [CVE-2023-0801](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0801)
  * [CVE-2023-0802](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0802)
  * [CVE-2023-0803](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0803)
  * [CVE-2023-0804](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0804)
  * [CVE-2023-26604](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-26604)



* * *

Fixed

In the Google Distributed Cloud air-gapped 1.9.3 user interface (UI) component, VM creation using UI allows disks restored from a snapshot to serve as boot disks.

* * *

Fixed

In the Google Distributed Cloud air-gapped 1.9.3 identity and access management (IAM) component, predefined roles enabled for upgrades are no longer subject to manual changes. Predefined role manifests override any manual changes.

* * *

Fixed

Google Distributed Cloud air-gapped 1.9.3 resolves the Firewall admin account lock out issue while rotating the admin credentials in the firewall (FW) component.

* * *

Fixed

Google Distributed Cloud air-gapped 1.9.3 fixes export of operational logs to Splunk in the LOG component.

* * *

Issue

Google Distributed Cloud air-gapped 1.9.3 has a known issue where role-based access control (RBAC) and schema settings in the VM manager is stopping users from starting VM backup and restore processes. 

* * *

Issue

Google Distributed Cloud air-gapped 1.9.3 has a known issue where the `vm-runtime` addon is stuck during the upgrade of the `gpu-org-system-cluster` from 1.9.1 to 1.9.2 because the `kubevm-gpu-driver-daemonset` pods are in the `CrashLoopBackOff` state.

* * *

Fixed

Google Distributed Cloud air-gapped 1.9.3 resolves an internal load balancer (ILB) services issue in the UNET component. Releases 1.9.0 - 1.9.2 contained a bug where internal load balancer (ILB) services were assigned an external IP instead of an internal IP. The impact is that the external load balancer IP pool is used more quickly as ILB services take addresses from this pool. However, the IPs assigned to ILB services were not advertised outside of the org, so the service remained internal to the org. This bug is fixed in 1.9.3 so that ILB services are assigned internal IPs.

* * *

Issue

Google Distributed Cloud air-gapped 1.9.3 has a known issue where a user cluster does not become ready in time.

* * *

Issue

Google Distributed Cloud air-gapped 1.9.3 has a known issue where an add-on installation fails.

* * *

Issue

Google Distributed Cloud air-gapped 1.9.3 has a known issue where an `OrganizationUpgrade` status does not get updated.

* * *

Issue

Google Distributed Cloud air-gapped 1.9.3 has a known issue where a user cluster upgrade fails to call webhooks.

* * *

Issue

Google Distributed Cloud air-gapped 1.9.3 has a known issue where a fleet admin controller gets stuck in a crash loop with the `Fleet admin controller manager stopped: failed to wait for auditloggingtarget caches to sync: timed out waiting for cache to be synced` error in the logs.

* * *

Issue

Google Distributed Cloud air-gapped 1.9.3 has a known issue where a system cluster does not become ready in time.

* * *

Issue

Google Distributed Cloud air-gapped 1.9.3 is unable to set AddOn selector labels for the root admin cluster.

* * *

Issue

Google Distributed Cloud air-gapped 1.9.3 has a known issue in the UI that lets you select an incompatible coupling of GPU to VM type.

* * *

Issue

Google Distributed Cloud air-gapped 1.9.3 has a known issue where VMs with memory greater than 32 GB require a memory override due to an incorrect QEMU overhead calculation.

* * *

Issue

Google Distributed Cloud air-gapped 1.9.3 has a known issue where the `kube-state-metrics` deployment crash loops.

* * *

Issue

Google Distributed Cloud air-gapped 1.9.3 has a known issue where alerts in organization system clusters don't reach the ticketing system.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
