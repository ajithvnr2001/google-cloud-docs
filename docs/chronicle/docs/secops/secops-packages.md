---
url: https://docs.cloud.google.com/chronicle/docs/secops/secops-packages/
title: Google SecOps packages overview \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:25:36.347036+00:00
---

# Google SecOps packages overview  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/secops/secops-packages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Google SecOps packages overview

Supported in:

Google SecOps 

Google Security Operations is offered in three packages: **Standard** , **Enterprise** , and **Enterprise Plus**. Each package determines the features and capabilities available to you in Google SecOps.

Additionally, Google offers Google Unified Security, which includes everything in the Google SecOps Enterprise Plus package and more.

A short description of each Google SecOps package follows:

  * **Standard** : Includes core capabilities for data ingestion, threat detection, investigation, and response. It provides 12 months of hot data retention. Google recommends this package for organizations needing foundational security operations.
  * **Enterprise** : Everything that is included in the Standard package, plus enhanced threat intelligence, user and entity behavior analytics (UEBA), and Google Cloud's generative AI assistance. Google recommends this package for organizations looking to scale their detection and response with advanced automation and AI.
  * **Enterprise Plus** : Everything that is included in the Enterprise package, plus the full power of Google Threat Intelligence Enterprise Plus, advanced data pipeline management, and extended storage options. Google recommends this package for organizations with complex environments requiring the most comprehensive threat defense and data flexibility.



The pricing for all packages is based on ingestion volume. For more information, contact a sales representative or your Google Cloud partner.

## Package comparison

The following table summarizes the features and services available in each Google SecOps package.

Feature or service | Standard | Enterprise | Enterprise+  
---|---|---|---  
|  | Includes everything in Standard | Includes everything in Enterprise  
**Base SIEM capabilities** | Included | Included | Included  
**Detection rules enabled** | 1K Single-event  
75 Multi-event  
Subset of Curated Detection Rules | 2K Single-event  
200 Multi-event  
Unlimited Curated Detection Rules | 3.5K Single-event  
400 Multi-event  
Unlimited Curated Detection Rules  
**Base SOAR capabilities** | Included | Multi-environment (MSSP) | Multi-environment (MSSP)  
**UEBA** | Not included | Included | Included  
**Applied Threat Intelligence** | Bring your own feeds | Enriched Intel with OSINT | Premium Intel (Enriched Intel w/ GTI data)  
**Google Curated Detections** | Not included | Included | Emerging and Active IR Threat Detections +  
Alert Prioritization for EDR Alerts  
**Gemini in Security Operations (AI)** | Not included | Included | Included  
**Google Threat Intelligence Enterprise Plus**  
Global threat intelligence platform. For more information, see Google Threat Intelligence Enterprise Plus. | Not included | Not included | Included  
**Google Threat Intelligence feeds**  
\- Pre-release IOCs  
\- Public IOCs |   
\- Not included  
|   
\- Not included  
\- Post processor matching, custom rules |   
\- Post processor matching, ATI rules  
\- Post processor matching, ATI rules, custom rules  
**VPC Service Controls**  
Security perimeters to protect against data exfiltration.  
In Private Preview. GA is scheduled for the end of Q1 2026. | Included | Included | Included  
**Customer-managed encryption keys (CMEKs)**  
Manage your own encryption keys for data at rest. | Not included | Not included | Included  
**Data Pipeline Management**  
Data Collection and Data Processing. | Collection using Bindplane  
Limited filtering and transforms | Advanced data processing (filter, redact, transform) in Google SecOps (cloud and on-premises data sources) | Advanced data processing in SecOps (cloud and on-premises) and using Bindplane (on-premises) plus another destination routing for 12 months  
**BigQuery Storage** | Not included | Not included | Included  
  
## Detailed package features

The following sections provide more details about the capabilities included in the Google SecOps packages.

### Standard

The **Standard** package provides the foundational layer for security operations. It lets teams to ingest telemetry from across their enterprise, normalize it into the Unified Data Model (UDM), and perform searches and investigations.

Key features include:

  * **12 months of hot data retention** : Store and search your security data for a full year at no additional cost beyond ingestion.
  * **Core detection engine** : Run up to 1,000 single-event and 75 multi-event detection rules.
  * **SOAR integrations** : Access over 300 prebuilt integrations to orchestrate your response.



### Enterprise

The **Enterprise** package adds advanced analytical layers and AI-driven productivity tools.

Key features include:

  * **Gemini in security operations** : Use natural language to search data, summarize cases, and create playbooks or detection rules.
  * **User and Entity Behavior Analytics (UEBA)** : Automatically identify anomalous behavior that might indicate compromised credentials or insider threats.
  * **Enriched OSINT** : Contextualize alerts with Google-enriched open source intelligence, including Google Safe Browsing and OSINT threat associations.



### Enterprise Plus

The **Enterprise Plus** package is the most comprehensive offering, providing premium threat intelligence and advanced data control.

Key features include:

  * **Google Threat Intelligence Enterprise Plus** : Access a unified platform that combines Google's security telemetry, VirusTotal's crowdsourced malware database, and Mandiant's frontline expertise. It provides deep context on the global threat landscape through unlimited access to threat actor profiles, vulnerabilities, and threat reports. The subscription proactively identifies external risks before they can be exploited by delivering unlimited monitoring for leaked credentials, typosquatting, and data leaks. Furthermore, it equips your team with advanced threat investigation capabilities and includes Mandiant Academy enrollments to continuously upskill your team.
  * **Advanced data pipeline** : Perform sophisticated data transformation, redaction of sensitive information, and route data to multiple destinations.
  * **Advanced BigQuery export** : Automatically provision managed BigQuery datasets for your security data, enabling complex analytics and custom reporting without managing the underlying pipeline.



## Google Unified Security

Google recommends the [Google Unified Security (GUS)](https://docs.cloud.google.com/chronicle/docs/reference/google-unified-security) package for large, strategic customers who are looking for a converged security solution to simplify their security operations, reduce costs, and proactively defend against threats. 

Google Unified Security includes:

  * Everything in Google SecOps Enterprise Plus package
  * Security Command Center Enterprise
  * Chrome Enterprise Premium
  * Mandiant Retainer
  * Mandiant Threat Defense



For more information, contact a sales representative or your Google Cloud partner.

## What's next

  * Learn how to [ingest data into Google SecOps](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-overview).
  * Understand [Google SecOps pricing](https://cloud.google.com/security/products/security-operations).
  * Explore [Gemini in Google SecOps](https://docs.cloud.google.com/chronicle/docs/secops/gemini-chronicle).



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
