---
url: https://docs.cloud.google.com/data-fusion/docs/security-bulletins/
title: Security bulletins \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:23:28.613814+00:00
---

# Security bulletins  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/security-bulletins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Resources ](https://docs.cloud.google.com/data-fusion/docs/resources)



Send feedback 

#  Security bulletins Stay organized with collections  Save and categorize content based on your preferences. 

This page describes all security bulletins related to Cloud Data Fusion.

## GCP-2025-076

**Published** : 2025-12-08

Description | Severity | Notes  
---|---|---  
A remote code execution vulnerability, [CVE-2025-9571](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-9571), was discovered in Cloud Data Fusion. Users with permissions to upload artifacts to a Cloud Data Fusion instance could exploit this vulnerability to execute arbitrary code within the core AppFabric component. This could allow an attacker to gain control over the Cloud Data Fusion instance, potentially leading to unauthorized access to sensitive data, modification of data pipelines, and exploration of the underlying infrastructure.

#### What should I do?

Upgrade your Cloud Data Fusion instance to the General Availability (GA) version 6.11.1. You can download the necessary update from the [CDAP build repository](https://github.com/cdapio/cdap-build/releases). | High |  [CVE-2025-9571](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-9571)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
