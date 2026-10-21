---
url: https://docs.cloud.google.com/chronicle/docs/security-bulletins/
title: Security bulletins \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:29:01.533069+00:00
---

# Security bulletins  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/security-bulletins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Support ](https://docs.cloud.google.com/chronicle/docs/secops/release-notes)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Security bulletins

This page provides all security bulletins related to Google Security Operations.

## GCP-2026-063

**Published:** 2026-09-16

### Description

Description | Severity | Notes  
---|---|---  
An Improper Privilege Management vulnerability in Google Security Operations SOAR was patched with version 6.3.85, and no customer action is needed. The vulnerability allowed an authenticated attacker to escalate privileges to system-level administrative access using a crafted internal authentication header. **What should I do?** No customer action is required. All customers have been automatically upgraded to the fixed version: 6.3.85 or higher. | Critical |  [CVE-2026-15587](https://www.cve.org/CVERecord?id=CVE-2026-15587)  
  
## GCP-2025-075

**Published:** 2025-12-07

### Description

Description | Severity | Notes  
---|---|---  
A vulnerability in the custom integrations feature of Google Security Operations SOAR could let an authenticated user with an _IDE role_ to achieve Remote Code Execution (RCE) on the server. The vulnerability was due to insufficient validation of the Python package code, allowing an attacker to upload a package with a malicious `setup.py` file. This file could then be executed during installation, compromising of the server. **What should I do?** No customer action is required. All customers have been automatically upgraded to the fixed version: 6.3.64 or higher. | High |  [CVE-2025-13428](https://www.cve.org/CVERecord?id=CVE-2025-13428)  
  
## GCP-2025-049

**Published:** 2025-09-04

### Description

Description | Severity | Notes  
---|---|---  
A critical vulnerability was found in Google Security Operations SOAR versions 6.3.54.0 and 6.3.53.2. An authenticated user with permissions to upload ZIP files (for example, when importing Use Cases) could upload a ZIP archive capable of writing files to arbitrary locations on the server's file system. The system for extracting files from ZIP archives couldn't prevent files within the archive from being written outside their intended destination folder. This is also known as a Directory Traversal or Zip Slip vulnerability.  **What should I do?** No customer action is required. All customers have been automatically upgraded to the fixed version or higher: 6.3.54.1 or 6.3.53.3 **What vulnerabilities are being addressed?** An attacker could exploit this vulnerability to overwrite application files. By overwriting a JavaScript file used by the report generation feature, an attacker could achieve Remote Code Execution (RCE) on the Google SecOps SOAR instance. The attacker could run their own code on the server. | High | [CVE-2025-9918](https://www.cve.org/CVERecord?id=CVE-2025-9918)  
  
## GCP-2023-028

**Published:** 2023-09-19

**Updated:** 2024-05-29

### Description

Description | Severity | Notes  
---|---|---  
**2024-05-29 Update** : The new feeds no longer use the shared service account, but it remains active for existing feeds to avoid service disruptions. Changes to the source in older feeds are blocked to prevent misuse of the shared service account. Customers can continue using their old feeds normally, as long as they don't change the source. 

* * *

Customers can configure Google SecOps to ingest data from customer-owned Cloud Storage buckets using an ingestion feed. Until recently, Google SecOps provided a shared service account that customers used to grant permission to the bucket. An opportunity existed such that one customer's Google SecOps instance could be configured to ingest data from another customer's Cloud Storage bucket. After performing an impact analysis, we found no current or prior exploitation of this vulnerability. The vulnerability was present in all versions of Google SecOps prior to Sept 19, 2023.  **What should I do?** As of Sept 19, 2023, Google SecOps has been updated to address this vulnerability. No customer action is required. **What vulnerabilities are being addressed?** Previously, Google SecOps provided a shared service account that customers used to grant permission to a bucket. Because different customers gave the same Google SecOps service account permission to their bucket, an exploitation vector existed that allowed one customer's feed to access a different customer's bucket when a feed was being created or modified. This exploitation vector required knowledge of the bucket URI. Now, during feed creation or modification, Google SecOps uses unique service accounts for each customer. | High |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
