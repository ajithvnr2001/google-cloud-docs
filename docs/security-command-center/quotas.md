---
url: https://docs.cloud.google.com/security-command-center/quotas/
title: Quotas and limits \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:36:59.937638+00:00
---

# Quotas and limits  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Resources ](https://docs.cloud.google.com/security-command-center/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This document contains current content limits and rate quotas for the Security Command Center API. This page will be updated to reflect any changes to these restrictions and usage limits.

## Content limits

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

The Security Command Center API enforces the following usage limits:

Content Limit | Value  
---|---  
Findings uploads | 500 MB per day  
  
## Rate quotas

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

The current API usage quotas for the Security Command Center API are as follows (and are subject to change):

Quota | Value  
---|---  
Reads per minute | 1,000  
Writes per minute | 1,000  
  
These limits apply to each Google Cloud console project and are shared across all applications and IP addresses using that project.

## Artifact guard limits

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

[Artifact guard](https://docs.cloud.google.com/security-command-center/docs/artifact-guard-overview) is subject to the following limits:

  * **Policies per parent resource** : You can define a maximum of 1,000 policies per organization or project.
  * **Vulnerability policies per parent resource** : You can define a maximum of 500 policies that target vulnerabilities within the overall limit.
  * **Policies per pipeline** : You can integrate a maximum of 100 policies per CI/CD pipeline for build-time enforcement.
  * **Updates per policy per week** : You can make a maximum of 100 updates to a policy each week.
  * **Pipeline connectors per policy** : You can associate a maximum of 100 pipeline connectors with a policy.
  * **Exempted and restricted CVEs per policy** : You can exempt or restrict a maximum of 100 CVEs per policy.
  * **Allowed and restricted packages per policy** : You can allow or restrict a maximum of 100 packages per policy.
  * **Artifact evaluation criteria** : You can evaluate images that meet the following criteria: 
    * The image must have a Package Uniform Resource Locator (pURL) object size of 100 MB or less.
    * The image can contain a maximum of 500 pURLs.
  * **API rate limit** : You can make a maximum of 1,200 API requests per minute (20 QPS) per consumer project for all methods within the artifact guard service.
  * **Service level objective (SLO)** : You can expect artifact evaluation to take approximately two minutes.



## Attack path simulation limits

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

The attack path simulation feature of Security Command Center is subject to the following limits:

  * You can define up to 100 resource value configurations in an organization
  * A high-value resource set can contain no more that 1,000 instances of high-value resources. For more information, see [Limit on resources in a high-value resource set](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#limit_on_resources_in_a_high-value_resource_set).



## Notifications

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Calls that use the Security Command Center API for notifications are subject to the following quotas:

API Call Type | Limit  
---|---  
Read Calls (`get`, `list`) | 1000 API calls per minute per organization.  
Write Calls (`create`, `update`, `delete`)  | 1000 API calls per minute per organization.  
  
The following additional limits apply to Security Command Center API notifications:

Usage | Limit  
---|---  
Number of `NotificationConfig` files | 500 per organization.  
  
## Security posture service limitations

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

The security posture service includes the following limits:

  * A maximum of 100 postures in an organization.
  * A maximum of 400 policies in a posture.
  * A maximum of 1000 posture deployments in an organization.



## Infrastructure as code validation limitations

Standard-legacy, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

The infrastructure as code (IaC) validation feature has the following limitations:

  * A maximum input file size of 2 MB or 1,000 assets.
  * A maximum output file size of 2 MB.
  * A maximum of 5 requests per minute per organization.
  * A maximum of 1,000 requests per day per organization.



## Export configurations to BigQuery

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

The following limit applies to [export configurations to BigQuery](https://docs.cloud.google.com/security-command-center/docs/how-to-analyze-findings-in-big-query):

Usage limit | Value  
---|---  
Number of export configurations to BigQuery | 500 per organization.  
  
## Custom module quotas

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Both the number of custom detection modules you can create and the number of API calls custom modules can make are subject to the quotas described in the following sections.

### Quotas for the creation of custom modules

The following table shows the quotas for the creation of custom modules.

Custom module type | Quota  
---|---  
Security Health Analytics custom modules | 100 custom modules per organization.  
  
### API call quotas for custom modules

API calls to custom module methods are also subject to quota limits. The following table shows the default quota limits for custom module API calls.

API Call Type | Limit  
---|---  
**CustomModules Read Requests** (Get, List) | 1,000 API calls per minute, per organization  
**CustomModules Write Requests** (Create, Update, Delete) | 60 API calls per minute, per organization  
**CustomModules Test Requests** | 12 API calls per minute, per organization  
  
For more information about custom modules, see the following:

  * [Overview of custom modules for Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-overview)



## Quota increases

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

If you want to transfer more than 5 GB per day or more than 1,000 reads or writes per minute, we would like to understand more about your needs and we might be able to build custom solutions. Submit a Security Command Center API Quota Request for your project in the [Google Cloud console](https://console.cloud.google.com/iam-admin/quotas).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
