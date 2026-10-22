---
url: https://docs.cloud.google.com/armor/docs/managed-rules-overview/
title: Managed rules overview \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:38:34.349406+00:00
---

# Managed rules overview  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/managed-rules-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Guides ](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)



Send feedback 

#  Managed rules overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Google Cloud Armor managed rules protect your web apps and API endpoints with automatically updated security signatures. Managed rules are powered by Thales Imperva and integrate directly into Cloud Armor, simplifying your security operations. Managed rules eliminate manual signature updates and reduce configuration drift, which lets your security team focus on development and operations.

## Key benefits

  * **Automated threat intelligence:** new signatures are curated and validated against threat feeds, providing protection against known CVEs and emerging attacks without requiring manual logic changes.
  * **Reduced operational burden:** signature updates are managed by Google Cloud, automatically rolling out to your security policies without maintenance windows.
  * **Zero-day vulnerability coverage:** emergency and time-sensitive vulnerabilities are directly patched into active rules, protecting your endpoints.
  * **Common Expression Language (CEL) integration:** these rules are evaluated natively in common custom rules with fine-grained conditional controls.



## Managed rules support

Managed rules are supported on global and regional backend security policies. For more information about supported load balancers and features, see the [Security policy overview](https://docs.cloud.google.com/armor/docs/security-policy-overview).

## Managed rules categories

**Note:** Managed rules (specifically, the `canary` and `stable` versions) evolve over time to expand coverage for additional vulnerabilities.

The following threat categories are supported by Cloud Armor managed rules:

Category name | Title | Description | Syntax reference  
---|---|---|---  
Account takeover | Account hijacking | Identifies credential stuffing, brute force, and session abuse aimed at user takeover. | `google:account_takeover:stable`  
Authentication bypass | Auth bypass attempts | Identifies requests that can be used to bypass sign-in flows, session checks, or token validation. | `google:authentication_bypass:stable`  
Automated attack | Automated threats | Identifies known scanners, exploit tools, and non-human traffic performing reconnaissance or attacks. | `google:automated_attack:stable`  
Backdoor trojan | Webshell & trojan detection | Identifies communication or execution patterns linked to webshells and known backdoors. | `google:backdoor_trojan:stable`  
Data leakage | Sensitive data exposure | Detects leaks of internal IPs, credentials, API keys, or personally identifiable information (PII). | `google:data_leakage:stable`  
DDoS | Distributed denial-of-service | Detects traffic patterns indicating volumetric or resource exhaustion attacks. | `google:ddos:stable`  
File upload | Malicious file upload | Identifies attempted uploads of malicious files like webshells, executables, or disguised payloads. | `google:file_upload:stable`  
LFI | Path traversal & LFI | Detects attempts to access restricted files by using traversal or local file inclusion techniques. | `google:lfi:stable`  
Other | Other threats | Identifies uncategorized attacks, malformed requests, and general anomaly patterns. | `google:misc:stable`  
Protocol manipulation | Protocol abuse | Identifies manipulation of protocol behavior, such as HTTP smuggling or carriage return line feed (CRLF) injection. | `google:protocol_manipulation:stable`  
RFI | Remote code/file inclusion | Identifies payloads that attempt to execute remote code or include untrusted files on the server. | `google:rfi:stable`  
Spam | Spam & abuse | Identifies form spam, comment spam, and bulk submissions by bots or scripts. | `google:spam:stable`  
SQLi | SQL injection | Identifies requests designed to manipulate SQL queries to access, modify, or destroy backend data. | `google:sqli:stable`  
SSRF | Server-side request forgery | Detects attempts to cause the server to issue internal or unauthorized outbound requests. | `google:ssrf:stable`  
XSS | Cross-site scripting | Detects script injection attempts that can hijack sessions, deface pages, or steal user data. | `google:xss:stable`  
  
## What's next

  * [Learn how to set up managed rules](https://docs.cloud.google.com/armor/docs/set-up-managed-rules)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
