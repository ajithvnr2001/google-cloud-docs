---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/release-notes-1913/
title: Google Distributed Cloud air-gapped 1.9.13 release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:33:01.520656+00:00
---

# Google Distributed Cloud air-gapped 1.9.13 release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/release-notes-1913/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Google Distributed Cloud air-gapped 1.9.13 release notes Stay organized with collections  Save and categorize content based on your preferences. 

## May 10, 2024

* * *

Announcement

Google Distributed Cloud air-gapped 1.9.13 is released.

See the [product overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/overview) to learn about the features of Google Distributed Cloud air-gapped.

* * *

Security

Updated Canonical Ubuntu OS image version to 20240402 to apply the latest security patches and important updates. To take advantage of the bug and security vulnerability fixes, you must upgrade all nodes with each release. The following security vulnerabilities are fixed: 

  * [CVE-2022-28948](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-28948)
  * [CVE-2023-0340](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0340)
  * [CVE-2023-1523](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1523)
  * [CVE-2023-4408](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4408)
  * [CVE-2023-4641](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4641)
  * [CVE-2023-5517](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5517)
  * [CVE-2023-6228](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6228)
  * [CVE-2023-6277](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6277)
  * [CVE-2023-6516](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6516)
  * [CVE-2023-6915](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6915)
  * [CVE-2023-22995](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-22995)
  * [CVE-2023-23000](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-23000)
  * [CVE-2023-23004](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-23004)
  * [CVE-2023-48733](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-48733)
  * [CVE-2023-50387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-50387)
  * [CVE-2023-50782](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-50782)
  * [CVE-2023-50868](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-50868)
  * [CVE-2023-51779](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51779)
  * [CVE-2023-51781](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51781)
  * [CVE-2023-51782](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51782)
  * [CVE-2023-52356](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52356)
  * [CVE-2024-0565](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0565)
  * [CVE-2024-0646](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0646)
  * [CVE-2024-2398](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-2398)
  * [CVE-2024-22667](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-22667)
  * [CVE-2024-24806](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-24806)
  * [CVE-2024-24855](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-24855)
  * [CVE-2024-28085](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-28085)



* * *

Security

Fixed vulnerabilities in the GDC console where strict transport security was not enforced. 

* * *

Security

Fixed a vulnerability with the remote Red Hat host for the ticketing system missing security updates.

* * *

Issue

**Platform authentication** :

  * Newly created orgs can't reach the server data IPs. All `cplb-init` and `storage-ipsec-config-bm-XXXXX` jobs display the follow message: `Failed to connect to the host via ssh: ssh: connect to host 10.1.18.X port 22: Connection timed out`. 



**Upgrade** :

  * An upgrade fails on `atat-webhooks` add-on while upgrading from 1.9.12 to 1.9.13. 
  * The Node OS upgrade on tenant org bare metal fails while upgrading from 1.9.12 to 1.9.13. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
