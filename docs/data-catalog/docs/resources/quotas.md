---
url: https://docs.cloud.google.com/data-catalog/docs/resources/quotas/
title: Quotas and limits \u00a0|\u00a0 Data Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:32:53.010456+00:00
---

# Quotas and limits  |  Data Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-catalog/docs/resources/quotas/

Data Catalog is deprecated and will be discontinued on June 1, 2026. For steps to transition your Data Catalog users, workloads, and content to Knowledge Catalog (formerly Dataplex Universal Catalog), see [Transition from Data Catalog to Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/transition-to-dataplex-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Catalog ](https://docs.cloud.google.com/data-catalog/docs)
  * [ Resources ](https://docs.cloud.google.com/data-catalog/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and limits for Data Catalog.

A **quota** restricts how much of a particular shared Google Cloud resource your Google Cloud project can use, including hardware, software, and network components. Quotas are part of a system that does the following:

  * Monitors your use or consumption of Google Cloud products and services.
  * Restricts your consumption of those resources for reasons including ensuring fairness and reducing spikes in usage.
  * Maintains configurations that automatically enforce prescribed restrictions.
  * Provides a means to make or request changes to the quota.



When a quota is exceeded, in most cases, the system immediately blocks access to the relevant Google resource, and the task that you're trying to perform fails. In most cases, quotas apply to each Google Cloud project and are shared across all applications and IP addresses that use that Google Cloud project.

To increase or decrease select quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/view-manage#requesting_higher_quota).

There are also **limits** on resources. These limits are unrelated to the quota system. Limits cannot be changed unless otherwise stated.

By default, quotas and limits apply on a per-project basis.

For more information about data lineage quotas, see [Quotas for Data Lineage API requests](https://docs.cloud.google.com/dataplex/docs/quotas#lineage-quotas).

## Quotas

To calculate an organization's QPM (queries per minute), Data Catalog adds together the QPM of projects in the organization.

Data Catalog uses QPM quotas to prevent service overload rather than control request workload distribution among projects. Therefore, both project and organization have the same default QPM quotas. In other words, if an organization has multiple projects and the request workload of one of them approaches the default organization (and the same project) quota, this project might impact the potential workload of the other projects in the organization.

To adjust organization and project quotas separately, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/view-manage#requesting_higher_quota).

QPM quota | Default value  
---|---  
Read | 6000  
Write | 1500  
Search | 1200  
**Note:** Listed quotas represent upper QPM bounds, and are not guaranteed.

For more information about BigQuery quotas, see [BigQuery quotas & limits](https://docs.cloud.google.com/bigquery/quotas).

## Limits

The Data Catalog API enforces limits for entries, tags, and business metadata.

### Entry limits

Limit | Value  
---|---  
Maximum number of entry groups per organization across all locations | 10k  
Maximum number of entries per organization across all locations  
(search results latency can increase when exceeded) | 100M  
Maximum number of entries per entry group | 100k  
MB per entry | 10 MB  
Maximum number of search results per page | 1000  
  
### Tag limits

Limit | Value  
---|---  
Fields per tag template | 500  
Length of a field name in a tag template | 512 bytes  
Length of a resource name for a tag template | 512 bytes  
Length of a string field in a tag template | 10,000 bytes  
Maximum number of enum values in a tag template | 100  
Maximum number of tags per entry | 1000  
Maximum sum of two numbers:  


  * Number of fields in all tags attached to an entry
  * Number of columns in the entry's optional schema

| 15,000  
Maximum number of policy tags per taxonomy | 100  
Maximum number of taxonomies per project | 40  
Maximum depth of the policy tags tree   
(100 policy tags per taxonomy still applies) | 5  
Length of a policy tag name | 200 bytes  
Number of starred entries per user | 200  
  
### Business metadata limits

Limit | Value  
---|---  
Maximum number of data stewards per data entry | 15  
Maximum size of rich text in overview, excluding image sizes | 100 KB  
Total size of rich text including images | 10 MB  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
