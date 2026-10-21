---
url: https://docs.cloud.google.com/bigquery/docs/security-bulletins/
title: Security bulletins \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:03:07.503212+00:00
---

# Security bulletins  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/security-bulletins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Resources ](https://docs.cloud.google.com/bigquery/docs/release-notes)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Security bulletins

This page describes all security bulletins related to BigQuery.

## GCP-2026-056

**Published** : 2026-08-26

Description | Severity | Notes  
---|---|---  
An Improper Input Validation vulnerability was discovered in the [JDBC driver](https://docs.cloud.google.com/bigquery/docs/jdbc-for-bigquery) in BigQuery Data Transfer Service versions prior to May 1, 2026.

#### What should I do?

No customer action is required. This vulnerability was patched on May 1, 2026.

#### What vulnerabilities are being addressed?

An authenticated attacker could use crafted JDBC connection string parameters to achieve remote code execution in the connector container and escalate privileges in the tenant project. | Critical |  [CVE-2026-12717](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-12717)  
  
## GCP-2026-047

**Published** : 2026-07-13

Description | Severity | Notes  
---|---|---  
A Missing Authorization vulnerability was discovered in repositories in BigQuery, Dataform, and Colab Enterprise.

#### What should I do?

No customer action is required. Google has already applied mitigations to all impacted products and services.

#### What vulnerabilities are being addressed?

During repository creation, an authenticated attacker could potentially escalate their permissions and perform cross-tenant repository takeover. | Critical |  [CVE-2026-14934](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-14934)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
