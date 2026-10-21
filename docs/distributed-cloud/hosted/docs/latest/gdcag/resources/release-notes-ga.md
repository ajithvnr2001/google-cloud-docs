---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/release-notes-ga/
title: Google Distributed Cloud air-gapped 1.9.1 release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:32.117461+00:00
---

# Google Distributed Cloud air-gapped 1.9.1 release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/release-notes-ga/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Google Distributed Cloud air-gapped 1.9.1 release notes Stay organized with collections  Save and categorize content based on your preferences. 

## March 21, 2023 [GDC 1.9.1 General Availability]

* * *

Announcement

Google Distributed Cloud air-gapped 1.9.1 General Availability (GA) is now released.

See the [product overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/overview) to learn about the features of Google Distributed Cloud air-gapped.

The following table lists services available in Google Distributed Cloud air-gapped.

**Artificial Intelligence & Machine Learning** | 

  * Vertex AI Optical Character Recognition (OCR)
  * Vertex AI Speech-to-Text
  * Vertex AI Translate
  * Vertex AI Workbench

  
---|---  
**Compute** | 

  * Virtual Machines
  * Kubernetes

  
**Databases** | 

  * Database Service for PostgreSQL
  * Database Service for Oracle (BYOL)

  
**Marketplace** | 

  * Dataproc container for Spark

  
**Networking** | 

  * Private networking
  * Load balancing (internal & external)
  * Network security policies
  * Network address translation (NAT)

  
**Security** | 

  * Identity and Access Management
  * Resource Manager
  * Key Management Service
  * Perimeter security

  
**Storage** | 

  * Block storage
  * Object storage
  * File storage
  * Backup service
  * Transfer appliance

  
**Other** | 

  * Observability (logging and monitoring)
  * Container Registry

  
  
* * *

Google Distributed Cloud air-gapped 1.9.1 GA introduces new predefined cluster roles for disaster recovery:

  * `dr-admin` created on a root admin cluster for an Infrastructure Operator (IO).

  * `gdch-dr-admin` created in the namespace `gdch-dr` for an IO for bucket creation.

  * `dr-restore-admin` created on an org admin cluster for an IO.

  * `dr-backup-admin` created on an org admin cluster for a Platform Administrator (PA).

  * `dr-system-admin` created in the namespace `dr-system` for a PA for bucket creation.




For details, see:

  * [Predefined identity and access roles tables for PA and AO](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/role-descriptions)



* * *

Google Distributed Cloud air-gapped 1.9.1 GA introduces a tool for generating templates for interconnect-related access control lists.

* * *

Fixed

In Google Distributed Cloud air-gapped 1.9.1 GA, the Node and Operating System component uses an auto restart on configuration feature of the VM to resolve the issue of potential failure to use a new VM disk for a VM after stopping and restarting KVM during cluster upgrade.

* * *

Fixed

In Monitoring operable component, `IMSPodImageReconciller` did not loop all projects in Artifact Registry and couldn't find images in the library project causing the `ims_unauthorized_image` alert to fire all the time.

* * *

Fixed

In Google Distributed Cloud air-gapped Private General Availability, Intrusion Detection and Prevention Systems Syslog fans-out to each organization.

* * *

Fixed

Google Distributed Cloud air-gapped 1.9.1 GA adds security rules for Border Gateway Protocol on firewalls using hairpin links CIDR and for Internet Control Message Protocol on firewalls using instance external CIDR.

* * *

Change

Updated Google Distributed Cloud version to 1.14.2-gke.11 to apply the latest security patches and important updates. 

See [Google Distributed Cloud 1.14.2 release notes](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/release-notes#March_01_2023) for details.

* * *

Change

Updated Canonical Ubuntu OS image version to 20230227 to apply the latest security patches and important updates. 

The following security vulnerabilities are fixed:

  * [CVE-2022-2601](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2601)
  * [CVE-2022-3775](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3775)
  * [CVE-2022-2601](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2601)
  * [CVE-2022-3775](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3775)



* * *

Security

The following container image security vulnerabilities are fixed:

  * [CVE-2023-0286](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0286)
  * [CVE-2023-0215](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0215)
  * [CVE-2022-4450](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4450)
  * [CVE-2022-2097](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2097)
  * [CVE-2022-32221](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32221)
  * [CVE-2022-41903](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41903)
  * [CVE-2022-23521](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23521)
  * [CVE-2022-39260](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-39260)
  * [CVE-2022-29187](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29187)
  * [CVE-2022-24765](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24765)
  * [CVE-2022-39253](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-39253)
  * [CVE-2021-46848](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46848)
  * [CVE-2022-42898](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42898)



* * *

Issue

Google Distributed Cloud air-gapped 1.9.1 has a known issue where role-based access control (RBAC) and schema settings in the VM manager is stopping users from starting VM backup and restore processes. 

* * *

Issue

Google Distributed Cloud air-gapped 1.9.0 has a known issue where remote server management software is occasionally unable to retrieve the key from HSM.

* * *

Issue

Google Distributed Cloud air-gapped 1.9.1 GA has a known issue where using the `standard-block` storage class might prevent virtual machines (VMs) from starting or restarting.

* * *

Issue

Google Distributed Cloud air-gapped 1.9.1 GA has a known issue where a compute node becomes stuck after reprovisioning a machine.

* * *

Issue

Google Distributed Cloud air-gapped 1.9.1 GA has a known issue during the Node OS upgrade where a the server is stuck in deprovisioning because `boot.ipxe` URL is invalid.

* * *

Issue

Google Distributed Cloud air-gapped 1.9.1 GA has a known issue during the Node OS upgrade where a node fails the `machine-init` job.

* * *

Issue

Google Distributed Cloud air-gapped 1.9.1 GA has a known issue where the upgrade from 1.9.0 to 1.9.1 is blocked because the `ods-fleet` add-on failed to install.

* * *

Issue

Google Distributed Cloud air-gapped 1.9.0 has a known issue in the UI that lets you select an incompatible coupling of GPU to VM type.

* * *

Issue

Google Distributed Cloud air-gapped 1.9.0 has a known issue where VMs with memory greater than 32 GB require a memory override due to an incorrect QEMU overhead calculation.

* * *

Issue

Google Distributed Cloud air-gapped 1.9.1 GA has a known issue where alerts in organization system clusters don't reach the ticketing system.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
