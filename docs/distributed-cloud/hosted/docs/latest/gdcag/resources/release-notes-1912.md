---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/release-notes-1912/
title: Google Distributed Cloud air-gapped release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:08.211056+00:00
---

# Google Distributed Cloud air-gapped release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/release-notes-1912/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Google Distributed Cloud air-gapped release notes Stay organized with collections  Save and categorize content based on your preferences. 

## April 8, 2024 [GDC 1.9.12]

* * *

Announcement

Google Distributed Cloud air-gapped 1.9.12 is now released.

See the [product overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/overview) to learn about the features of Google Distributed Cloud air-gapped.

* * *

Security

Updated Canonical Ubuntu OS image version to 20240317 to apply the latest security patches and important updates. To take advantage of the bug and security vulnerability fixes, you must upgrade all nodes with each release. The following security vulnerabilities are fixed: 

  * [CVE-2020-28493](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-28493)
  * [CVE-2022-44840](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-44840)
  * [CVE-2022-45703](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-45703)
  * [CVE-2022-47007](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-47007)
  * [CVE-2022-47008](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-47008)
  * [CVE-2022-47010](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-47010)
  * [CVE-2022-47011](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-47011)
  * [CVE-2023-0340](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0340)
  * [CVE-2023-2953](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2953)
  * [CVE-2023-4408](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4408)
  * [CVE-2023-4641](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4641)
  * [CVE-2023-5517](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5517)
  * [CVE-2023-6004](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6004)
  * [CVE-2023-6040](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6040)
  * [CVE-2023-6228](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6228)
  * [CVE-2023-6277](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6277)
  * [CVE-2023-6516](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6516)
  * [CVE-2023-6606](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6606)
  * [CVE-2023-6915](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6915)
  * [CVE-2023-6918](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6918)
  * [CVE-2023-6931](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6931)
  * [CVE-2023-6932](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-6932)
  * [CVE-2023-22995](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-22995)
  * [CVE-2023-43040](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-43040)
  * [CVE-2023-45863](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45863)
  * [CVE-2023-48733](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-48733)
  * [CVE-2023-50782](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-50782)
  * [CVE-2023-50868](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-50868)
  * [CVE-2023-51764](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51764)
  * [CVE-2023-51779](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51779)
  * [CVE-2023-51781](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51781)
  * [CVE-2023-51782](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51782)
  * [CVE-2023-52356](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52356)
  * [CVE-2024-0553](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0553)
  * [CVE-2024-0565](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0565)
  * [CVE-2024-0646](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0646)
  * [CVE-2024-21626](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21626)
  * [CVE-2024-22195](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-22195)
  * [CVE-2024-22365](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-22365)
  * [CVE-2024-24806](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-24806)



* * *

Security

The following container image security vulnerabilities are fixed:

  * [CVE-2021-38561](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-38561)
  * [CVE-2021-41617](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-41617)
  * [CVE-2022-32149](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32149)
  * [CVE-2022-41723](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41723)
  * [CVE-2022-41724](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41724)
  * [CVE-2022-41725](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41725)
  * [CVE-2023-3446](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3446)
  * [CVE-2023-3817](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3817)
  * [CVE-2023-3978](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3978)
  * [CVE-2023-24532](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24532)
  * [CVE-2023-24534](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24534)
  * [CVE-2023-24536](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24536)
  * [CVE-2023-24537](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24537)
  * [CVE-2023-24538](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24538)
  * [CVE-2023-24539](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24539)
  * [CVE-2023-24540](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24540)
  * [CVE-2023-29400](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29400)
  * [CVE-2023-29402](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29402)
  * [CVE-2023-29403](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29403)
  * [CVE-2023-29404](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29404)
  * [CVE-2023-29405](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29405)
  * [CVE-2023-29406](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29406)
  * [CVE-2023-29409](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29409)
  * [CVE-2023-39318](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39318)
  * [CVE-2023-39319](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39319)
  * [CVE-2023-39323](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39323)
  * [CVE-2023-39325](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39325)
  * [CVE-2023-39326](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39326)
  * [CVE-2023-44487](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-44487)
  * [CVE-2023-45285](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45285)
  * [CVE-2023-45287](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45287)
  * [CVE-2023-48795](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-48795)
  * [CVE-2023-51385](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51385)
  * [CVE-2024-24786](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-24786)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
