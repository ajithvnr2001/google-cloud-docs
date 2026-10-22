---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/release-notes-10/
title: Google Distributed Cloud air-gapped appliance release notes \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:15:57.135075+00:00
---

# Google Distributed Cloud air-gapped appliance release notes  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/release-notes-10/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Google Distributed Cloud air-gapped appliance release notes Stay organized with collections  Save and categorize content based on your preferences. 

## May 30, 2025

* * *

Announcement

Google Distributed Cloud (GDC) air-gapped appliance 1.0 is generally available.  
See the [product overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/overview) to learn about the features of GDC air-gapped appliance. 

* * *

Feature

The following new features are available: 

**Identity and access management** :

  * Added support for Keycloak as an identity provider.



**Vertex AI** :

  * [Vertex AI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-overview) is generally available (GA) in GDC air-gapped appliance, offering the following pre-trained APIs: 

    * [Optical Character Recognition (OCR)](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-ocr)
    * [Speech-to-Text](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-stt)
    * [Vertex AI Translation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-translation)



**Virtual machines** :

  * Added the ability to [enable virtual trusted platform module (vTPM)](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/secure-vms/secure-boot#enable-vtpm) when securely booting a VM.

  * Added the following images to the [GDC-provided VM image list](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/create-a-vm/supported-vm-images): 

    * Ubuntu 24.04 golden image 
    * SUSE CHost 15.5 bring your own (BYO) image 
    * Windows 10 bring your own (BYO) image 
  * Added the ability to perform [VM disk expansion](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/operations-and-lifecycle/expand-vm-disks) on `VirtualMachineDisk` partitions. 

  * Added the ability to [create a VM instance with a specified IP address and subnet](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/create-a-vm/create-and-start#create-vm-with-ip). 

  * Added the ability to [view and maintain VM metadata](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/operations-and-lifecycle/view-and-maintain-metadata). 




* * *

Security

Updated the Rocky OS image version to 20250219 to apply the latest security patches and important updates. 

The following security vulnerabilities are fixed:

  * [CVE-2022-40303](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-40303)
  * [CVE-2022-40304](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-40304)
  * [CVE-2022-49043](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-49043)
  * [CVE-2023-32324](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-32324)
  * [CVE-2023-32360](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-32360)
  * [CVE-2023-33460](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-33460)
  * [CVE-2023-34241](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-34241)
  * [CVE-2024-35235](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-35235)
  * [CVE-2024-47175](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-47175)
  * [CVE-2024-52531](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-52531)



* * *

Issue

The following issues are identified: 

**Monitoring**

  * The Grafana dashboard does not launch and displays a `No healthy upstream` error after rebooting the device. 



**Storage**

  * The OTS VM does not restart automatically after an ungraceful shutdown. 



**Upgrade**

  * There is a post-upgrade failure due to an unhealthy logging pipeline. 

  * Updating the appliance to a new patch fails when the `gdcloud appliance upgrade` long running command fails with a credential helper error. 

  * There is a post-upgrade failure due to the storage cluster that is not ready. 




* * *

Change

The following changes are identified: 

**Version updates** :

  * The Google Distributed Cloud for bare metal version is updated to 1.30.500-gke.127 to apply the latest security patches and important updates.   
  
See the [Google Distributed Cloud for bare metal 1.30.500-gke.127 release notes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/release-notes-ver-1#release_130500-gke127) for details.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
