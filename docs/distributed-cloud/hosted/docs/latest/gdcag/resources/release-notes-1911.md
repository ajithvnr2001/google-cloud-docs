---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/release-notes-1911/
title: Google Distributed Cloud air-gapped release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:00.132331+00:00
---

# Google Distributed Cloud air-gapped release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/release-notes-1911/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Google Distributed Cloud air-gapped release notes Stay organized with collections  Save and categorize content based on your preferences. 

## March 08, 2024 [GDC 1.9.11]

* * *

Announcement

Google Distributed Cloud air-gapped 1.9.11 is now released.

See the [product overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/overview) to learn about the features of Google Distributed Cloud air-gapped.

* * *

Security

Updated Canonical Ubuntu OS image version to v20240212 to apply the latest security patches and important updates. To take advantage of the bug and security vulnerability fixes, you must upgrade all nodes with each release. The following security vulnerabilities are fixed:

  * [CVE-2020-26570](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-26570)
  * [CVE-2020-26571](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-26571)
  * [CVE-2020-26572](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-26572)
  * [CVE-2020-28493](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-28493)
  * [CVE-2023-2953](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2953)
  * [CVE-2023-6004](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6004)
  * [CVE-2023-6040](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6040)
  * [CVE-2023-6918](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6918)
  * [CVE-2023-6931](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6931)
  * [CVE-2023-6932](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6932)
  * [CVE-2023-43040](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-43040)
  * [CVE-2023-45863](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45863)
  * [CVE-2023-51764](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51764)
  * [CVE-2024-0553](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0553)
  * [CVE-2024-22195](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-22195)
  * [CVE-2024-22365](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-22365)



* * *

Security

The following container image security vulnerabilities are fixed:

  * [CVE-2023-46219](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-46219)



* * *

Fixed

**Monitoring** :

  * The issue with the `anthos-prometheus-k8s` LogMon resource regularly filling up its persistent volume, causing Prometheus to crash loop, is fixed by reducing default metrics retention time to 24 hours.




**Upgrade** :

  * The issue with the upgrade getting stuck at `AdminClusterHealth` postflight check is fixed.




* * *

Issue

**VM backup and restore** :

  * Role-based access control (RBAC) and schema settings in the VM manager is stopping users from starting VM backup and restore processes. 



* * *

Change

**Version update** : 

  * The Debian-based image version is updated to bullseye-v1.4.3-gke.11.




**Important:** To access the URLs listed on this page, you must connect to the internet. The URLs are provided to access outside of your air-gapped environment.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
