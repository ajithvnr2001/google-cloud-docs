---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/release-notes-11310/
title: Google Distributed Cloud air-gapped 1.13.10 release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:00:06.635370+00:00
---

# Google Distributed Cloud air-gapped 1.13.10 release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/release-notes-11310/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Google Distributed Cloud air-gapped 1.13.10 release notes Stay organized with collections  Save and categorize content based on your preferences. 

## May 1, 2025

* * *

Announcement

Google Distributed Cloud (GDC) air-gapped 1.13.10 is available.  
See the [product overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/overview) to learn about the features of Distributed Cloud. 

* * *

Security

Updated the Rocky OS image version to 20250312 to apply the latest security patches and important updates. 

The following security vulnerabilities are fixed:

  * [CVE-2022-49043](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-49043)
  * [CVE-2023-4191](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4191)
  * [CVE-2023-50387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-50387)
  * [CVE-2023-50868](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-50868)
  * [CVE-2024-11187](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-11187)



* * *

Issue

The following issues are identified: 

**Backup and restore**

  * Persistent volume backups might intermittently fail due to insufficient volume space for snapshots, potentially leading to volumes becoming read-only. 
  * Agent and control plane pods might restart if they run out of memory, affecting system stability. 
  * Backups might fail due to exceeding the ONTAP snapshot limit of 1023 per `PersistentVolumeClaim` (PVC) resource. 



**Networking** :

  * The `allow-all-egress` project network policy (PNP) does not allow traffic to system endpoints. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
