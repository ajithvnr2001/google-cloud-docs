---
url: https://docs.cloud.google.com/load-balancing/docs/security-bulletins/
title: Security bulletins for Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:44:55.848568+00:00
---

# Security bulletins for Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/security-bulletins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Resources ](https://docs.cloud.google.com/load-balancing/docs/resources)



Send feedback 

#  Security bulletins for Cloud Load Balancing Stay organized with collections  Save and categorize content based on your preferences. 

All security bulletins for Cloud Load Balancing are described here. For all security bulletins related to Google Cloud products, see [Security Bulletins](https://docs.cloud.google.com/support/bulletins).

[ Use this XML feed to subscribe to security bulletins for this page. ![Subscribe](https://docs.cloud.google.com/static/docs/images/feed-icon.png)](https://cloud.google.com/feeds/cloud-load-balancing-security-bulletins.xml)

## GCP-2025-027

**Published:** 2025-05-16

### Description

Description | Severity | Notes  
---|---|---  
A security vulnerability was detected in the classic Application Load Balancer service prior to April 26, 2025.

#### What should I do?

No customer action is required. The issue was resolved in the Classic Application Load Balancer service on April 26, 2025.

#### What vulnerabilities are being addressed?

[CVE-2025-4600](https://www.cve.org/CVERecord?id=CVE-2025-4600) allowed attackers to smuggle requests to classic Application Load Balancers due to incorrect parsing of oversized chunk bodies. When parsing the request body of an HTTP request using chunked transfer-encoding, the classic Application Load Balancer allows oversized chunk bodies. Consequently, it was feasible to hide bytes within this ignored trailing data that an upstream HTTP server might incorrectly interpret as a line terminator. This vulnerability was addressed within the classic Application Load Balancer service on April 26, 2025 through improved input validation and parsing logic.

#### We're here to help

If you have any questions or require assistance, contact [Cloud Customer Care](https://docs.cloud.google.com/support/docs/overview). | High |  [CVE-2025-4600](https://www.cve.org/CVERecord?id=CVE-2025-4600)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
