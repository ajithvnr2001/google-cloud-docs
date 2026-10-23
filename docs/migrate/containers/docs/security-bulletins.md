---
url: https://docs.cloud.google.com/migrate/containers/docs/security-bulletins/
title: Security bulletins \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:31.647717+00:00
---

# Security bulletins  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/security-bulletins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Resources ](https://docs.cloud.google.com/migrate/containers/docs/resources)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Security bulletins

The following describes all security bulletins related to Migrate to Containers.

To get the latest security bulletins delivered to you, do one of the following:

  * Add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators).
  * Add the feed URL directly to your feed reader: `https://cloud.google.com/migrate-to-containers-security-bulletins.xml`



## GCP-2024-058

**Published:** 2024-10-16  
Description | Severity | Notes  
---|---|---  
Migrate to Containers for Windows versions 1.1.0 to 1.2.2 created a local `m2cuser` with administrator privileges. This posed a security risk if the `analyze` or `generate` commands were interrupted by the user or due to an internal error causing skipping the action to delete the local user `m2cuser`. 

#### What should I do?

The following versions of Migrate to Containers CLI for Windows have been updated with code to fix this vulnerability. We recommend that you manually upgrade your Migrate to Containers CLI to the following version or higher:

  * Migrate to Containers CLI for Windows 1.2.3 released on October 8, 2024 \- [ Migrate to Containers CLI release notes | Google Cloud](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli-relnotes#october_8_2024)



#### What vulnerabilities are being addressed?

The vulnerability, CVE-2024-9858, allows an attacker to gain administrator access to impacted Windows machines using the local administrator user created by the Migrate to Containers software. | Medium | [CVE-2024-9858](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-9858)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
