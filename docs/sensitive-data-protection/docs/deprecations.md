---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/deprecations/
title: Sensitive Data Protection deprecations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:11.387083+00:00
---

# Sensitive Data Protection deprecations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/deprecations/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Resources ](https://docs.cloud.google.com/sensitive-data-protection/docs/resources)



Send feedback 

#  Sensitive Data Protection deprecations Stay organized with collections  Save and categorize content based on your preferences. 

The [Google Cloud Platform Terms of Service (section "Discontinuation of Services")](https://docs.cloud.google.com/terms) defines the deprecation policy that applies to Sensitive Data Protection. The [deprecation policy](https://docs.cloud.google.com/terms/deprecation) only applies to the services, features, or products listed therein. 

After a service, feature, or product is officially deprecated, it continues to be available for at least the period of time defined in the Terms of Service. After this period of time, the service is scheduled for shutdown. 

Feature | Deprecated date | Shutdown date | Details  
---|---|---|---  
Send inspection results from Sensitive Data Protection to Data Catalog | February 3, 2025 | September 30, 2025 | Data Catalog is discontinued, and this feature is shut down. We recommend that you [send the inspection results to Knowledge Catalog](https://docs.cloud.google.com/sensitive-data-protection/docs/add-aspects-inspection-job) instead. To migrate existing job triggers that use the **Publish to Data Catalog** ([`PublishFindingsToCloudDataCatalog`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Action#publishfindingstoclouddatacatalog)) action, see [Migrate to the Publish to Dataplex Universal Catalog action](https://docs.cloud.google.com/sensitive-data-protection/docs/add-aspects-inspection-job#migrate-dataplex-catalog).  
Tag tables in Knowledge Catalog based on insights from data profiles | February 3, 2025 | September 30, 2025 | Data Catalog is discontinued, and this feature is shut down. We recommend that you [add Knowledge Catalog aspects based on insights from data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/add-aspects) instead. To migrate existing discovery configurations that use the shut-down **Send to Dataplex as tags** action, see [Migrate to the Send to Dataplex Catalog as aspects action](https://docs.cloud.google.com/sensitive-data-protection/docs/add-aspects#migrate).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
