---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/standard-parser-support-policy/
title: Support policy for standard parsers \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:06.302786+00:00
---

# Support policy for standard parsers  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/standard-parser-support-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Support policy for standard parsers 

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

Google SecOps provides a wide range of prebuilt, out-of-the-box standard parsers to help you quickly ingest and normalize logs from various data sources. To verify platform stability, predictable performance, and high-quality data normalization, Google SecOps uses a focused support model for Standard parsers.

**Note:** The policies outlined in this document apply exclusively to Standard parsers (not Premium parsers).

## Parser support levels

Google SecOps offers the following levels of parser support:

Parser Type | Description and Support  
---|---  
**Premium parsers** | Google SecOps provides high-quality parsers from the most widely used, high-volume data sources. Google typically processes customer requests for premium parsers within a few days.  
**Standard parsers** | For other supported data sources, Google SecOps offers best-effort support. Requests for new field mappings are handled as feature requests and are part of the product backlog. To meet immediate needs, you can use the self-service parser extensions and Auto-Extraction capabilities.  
**Custom-built parsers and extensions** | Google SecOps does not offer support for these. We recommend that you manage this either independently or with assistance from Google partners.  
  
For a complete list of Premium and Standard parsers, see [Default Parser Configuration](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/default-parser-configuration).

For an overview of parsing raw logs to the Unified Data Model (UDM) format, see [Overview of log parsing](https://docs.cloud.google.com/chronicle/docs/event-processing/udm-overview).

**Note:** Google handles all requests for new prebuilt parsers as feature requests.

## Focus on Important UDM Fields

With over a million distinct fields ingested across different log formats, Google SecOps focuses its standard parser default mappings on the most critical security data.

Standard parsers are specifically scoped to map the [Important UDM Fields](https://docs.cloud.google.com/chronicle/docs/reference/important-udm-fields). These fields represent the most critical data points required for effective downstream threat detection and context. For any fields outside of this core list, we highly encourage customers to map these using our comprehensive suite of self-service tools, such as Parser Extensions and Auto-Extraction.

## Customer Support Tiers

Parser support and SLOs are differentiated based on your Google SecOps entitlement:

  * **Premium Support customers:** Customers holding an Expert or Expert+ entitlement.
  * **Standard Support customers:** Customers with Standard entitlement.



## Standard Parser Request Matrix

Google triages and processes standard parser requests based on the nature of the request and your support tier.

Request Type | Standard Customers | Expert / Expert+ Customers  
---|---|---  
Regression / Breakage (Major regressive effects on parsing) | Immediate rollback or fix. | Immediate rollback or fix.  
New parser Requests OR requests for a new log format / schema in an existing parser | Built as a default parser only if requested by >= 10 customers, or based on Google business discretion. Otherwise, the system routes the request to self-service or partner / PSO paths. | Built as a default prebuilt parser or a Google SecOps GitHub parser based on Google discretion.  
Missing/Incorrect "Important Fields" OR Incorrect "Non-Important Fields" | Handled using the parser queue and self-service tooling (Best-effort, no SLO). | Prioritized in the parser queue (6 weeks SLO); offer extensions for immediate fix if needed.  
Missing "Non-Important Fields" | Self-service only. Customers should use self-service tools (Extensions, Auto-Extraction) rather than opening support tickets. | Handle using parser queue and self-service tooling. High-touch support provided if necessary.  
**Note:** For all new parsers, the field mapping scope is strictly limited to the Important UDM Fields, plus a best-effort AI mapping for non-important fields.

## Community and GitHub parsers

To provide a richer, more vibrant ecosystem for log parsing, Google SecOps maintains a dedicated [Google SecOps GitHub](https://docs.cloud.google.com/chronicle/docs/ingestion/parsers-github) repository.

This open-source ecosystem allows partners, vendors, and the Google SecOps community to contribute and maintain parsers. This logic verifies that even niche or highly specialized commercial products can have functional parsers available for deployment.

**Low-Usage (Longtail) Prebuilt Parsers:** To maintain high performance and focus engineering efforts on the most widely utilized data sources, prebuilt parsers used by a low number of customers are transitioned into community-maintained parsers on GitHub.

  * Google releases only critical updates (breaking changes or severe normalization degradation for the majority of customers using it) to the prebuilt versions of these low-usage parsers.
  * All new, non-critical enhancements or field additions for these parsers will be contributed directly to the GitHub version. This approach will open-source these parsers and enables community contribution to the repository.
  * Customers using these parsers are highly encouraged to migrate to the GitHub version to benefit from ongoing community and Google-contributed enhancements, rather than opening support tickets for the prebuilt version.



## Comparison between the different parser variants

Criteria | Prebuilt parsers (Premium + non longtail standard parsers) | Parsers on GitHub - offloaded longtail prebuilt parsers | Parsers on GitHub - community / partner created | Custom parsers  
---|---|---|---|---  
**Ownership** | Google Owned | Initial creation by Google and then community / partner owned (depends on the parser) | Community / partner owned | Customer owned  
**Parser deployment** | Automatically deployed | The customer must pull the parser. | The customer must pull the parser. | Customer deploys  
**Changes (parser versions)** | All changes done by Google | Community / partner owned. Google can contribute code where relevant. | Changes done based on community / partner contribution | All changes done by the customer  
**Support for user requests** | Google supports the requests: Premium - all, Standard - focus on important UDM fields | Maintained by community / partner. Google can contribute code where relevant. | Fully maintained by community / partner | Fully maintained by the customer  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
