---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/release-notes-1144/
title: Google Distributed Cloud air-gapped 1.14.4 release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:00:06.459332+00:00
---

# Google Distributed Cloud air-gapped 1.14.4 release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/release-notes-1144/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Google Distributed Cloud air-gapped 1.14.4 release notes Stay organized with collections  Save and categorize content based on your preferences. 

## May 23, 2025

* * *

Announcement

Google Distributed Cloud (GDC) air-gapped 1.14.4 is available.  
See the [product overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/overview) to learn about the features of Distributed Cloud. 

* * *

Feature

The following new features are available: 

**Networking** :

  * Added session affinity for external load balancers. Use session affinity for ELBs to ensure that requests from the same client are consistently routed to the same backend. For more information, see [Configure external load balancers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/elb-service).



**Resource Manager** :

  * Added the capability to create asymmetrical organization configurations across zones in a GDC universe. This is a [Preview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/feature-stages#preview) feature.



**Storage** :

  * Added support for replicated storage resources such as volumes and buckets in asynchronous mode for disaster recovery scenarios. These storage resource options provide asynchronous data replication between zones in a GDC universe. For more information, see [Data protection with multi-zone storage](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/data-protection).



**Vertex AI** :

  * Added [Generative AI capabilities and Text Embedding models](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/genai/genai-overview).
  * Added the Preview feature to [translate any language into German](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vai-translation-langs#SupportedLanguages-to-German) with Vertex AI Translation. 



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

* * *

Issue

The following issues are identified: 

**Backup and restore**

  * The UI incorrectly displays a disk size as 0Mb. 

  * The backup control plane pod crashes due to insufficient memory. 




**IAM**

  * The first role binding attached to a new service identity using the GDC console does not take effect, and causes issues with all proceeding role binding additions. 



**Multi-tenancy** :

  * GDC console does not indicate node pool creation failures 



**Resource Manager** :

  * The global v1 organization's replica status reports a zonal v1 organization configuration for all zones, regardless of whether it was actually created. 



**Server:**

  * The BIOS credential rotation is stuck in the reset-requested stage. 



**Ticketing system** :

  * An RBAC error from customer networks might deny access to ServiceNow. 



**Object storage:**

  * Deleting an empty bucket from the GDC console fails. 

  * StorageGRID load balancer endpoint certificate expired. 




**Upgrade:**

  * Shared service cluster annotation is not updated after a successful cluster upgrade. 



**Virtual machines:**

  * An image import fails. 



* * *

Fixed

The following issues are fixed: 

**Cluster management** :

  * Fixed the issue where the `kub-gpu-controller` subcomponent did not reconcile for the `gdchservices` organization. 



**Networking** :

  * Fixed the issue where data plane and management ingress gateways did not reconcile. 



**Resource Manager** :

  * Fixed the issue where the failing `create-ansible-playbooks` job caused organization problems. 



**System Artifact Registry** :

  * Fixed the issue where a false alarm can be triggered in response to transient errors when reconciling the `HarborRobotAccount` resource. For more information, see [Known issues](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/known-issues/known-issues-114x#harbor-robot-account-false-alarm).



**Ticketing system** :

  * Fixed the issue where the ServiceNow MID server fails to start properly. 



* * *

Change

The following changes are identified: 

**Version updates** :

  * The Google Distributed Cloud for bare metal version is updated to 1.30.500-gke.127 to apply the latest security patches and important updates.   
  
See the [Google Distributed Cloud for bare metal 1.30.500-gke.127 release notes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/release-notes-ver-1#release_130500-gke127) for details.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
