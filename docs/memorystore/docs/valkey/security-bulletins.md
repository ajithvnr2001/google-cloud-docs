---
url: https://docs.cloud.google.com/memorystore/docs/valkey/security-bulletins/
title: Security bulletins \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:58.271146+00:00
---

# Security bulletins  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/security-bulletins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Resources ](https://docs.cloud.google.com/memorystore/docs/valkey/resources)



Send feedback 

#  Security bulletins Stay organized with collections  Save and categorize content based on your preferences. 

This page provides information about security bulletins for Memorystore for Valkey.

## GCP-2025-061

**Published:** 2025-10-21

### Description

Description | Severity | Notes  
---|---|---  
A remote code execution vulnerability was found in open-source Valkey. As a result, all versions that [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey) supports are impacted. By default, Memorystore for Valkey instances aren't exposed to the public internet, so the risk of this vulnerability is **Low** for Memorystore for Valkey users who follow [Google Cloud's security best practices](https://docs.cloud.google.com/memorystore/docs/valkey/security-overview).

#### What should you do?

Google has started applying patches automatically, with an estimated completion date of November 6, 2025. **No action is required from you to receive this fix.** If you want to apply these patches to your Memorystore for Valkey instances earlier than November 6, 2025, then use self-service maintenance to complete the following actions:

  1. View the current maintenance version of your [Memorystore for Valkey instances](https://docs.cloud.google.com/memorystore/docs/valkey/maintenance-changelog).
  2. Verify if the version matches the latest patched versions.
  3. If the version isn't the latest maintenance version, then update your instances to the latest maintenance version using self-service maintenance for [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey/self-service-maintenance).

| Critical |  [CVE-2025-49844](https://nvd.nist.gov/vuln/detail/CVE-2025-49844)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
