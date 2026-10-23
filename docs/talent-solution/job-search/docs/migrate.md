---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/migrate/
title: Migrate to CTS Job Search v4 from a previous version \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:34:54.862329+00:00
---

# Migrate to CTS Job Search v4 from a previous version  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/migrate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Guides ](https://docs.cloud.google.com/talent-solution/job-search/docs/basics)



Send feedback 

#  Migrate to CTS Job Search v4 from a previous version Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

Cloud Talent Solution v4 is the latest version in General Availability (GA). Cloud Talent Solution v4 consolidates features from several previous versions ( [v3](https://docs.cloud.google.com/talent-solution/job-search/v3/docs), [v3p1beta1](https://docs.cloud.google.com/talent-solution/job-search/v3/docs), and [v4beta1](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs). With the release of v4, all previous versions (v3, v3p1beta1, and v4beta1) are now deprecated. Calls to deprecated versions (v3p1beta1, v4beta1, and v3) will be unsuccessful starting **October 14, 2021**.

## Functionality changes

Some critical functional changes between v4 and older versions are outlined in the table below. For a complete picture of functionality changes we recommend that you review the [release notes](https://docs.cloud.google.com/talent-solution/docs/release-notes).

Functional changes | Older versions | v4  
---|---|---  
[Multi-tenancy support](https://docs.cloud.google.com/talent-solution/job-search/docs/tenants) | Supported starting from v4beta1. Both tenant and non-tenant paths are supported in v4beta1. | **Tenant path is now required.** To migrate from non-tenant path to tenant path, use the [listTenants](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants/list) API to find the tenant and add it to tenant path.  
[Batch operations](https://docs.cloud.google.com/talent-solution/job-search/docs/batch) | Batch Operations in v3 and v3p1beta1 are synchronous. v4beta1 upgrades the BatchCreate and BatchUpdate to asynchronous operations. | **BatchDelete is added as a Batch Operation** , and all Batch Operations continue to be asynchronous.  
[Histogram Facets](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/HistogramFacets?hl=en) | Supported in v3 and v3p1beta1. Starting from v4beta1 `HistogramFacets` is not supported and is replaced by [Histogram Query](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/HistogramQuery), which offers more flexibility by using an expression. | Only [Histogram Query](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/HistogramQuery) is supported (same as v4beta1).  
`CompanyName` | The field is called `companyName` in v3 and v3p1beta1 and renamed to `company` in v4beta1. | The field name is [`company`](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs) (same as v4beta1).  
[`requirePreciseResultSize`](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs/search#request-body) | Deprecated in v3, v3p1beta1, and v4beta1. | **Deleted from v4** because all search calls now return precise results.  
[`estimatedTotalSize`](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/SearchJobsResponse) |  | **Deleted from v4** because all search calls now return precise results and this field has the same value as `totalSize`.  
[`CommuteMethod`](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/JobQuery#commutemethod) | Walking and cycling were Beta options in v4beta1. They will remain Beta features **only available in v4beta1** until approximately Q1 2021, at which time these features will be generally available and included in v4. | `COMMUTE_METHOD_UNSPECIFIED`, `DRIVING`, and `TRANSIT` are the only `CommuteMethod` options available in v4 until Q1 2021.  
[`SearchJobsRequest.max_page_size`](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs/search#request-body) | Named `SearchJobsRequest.page_size` in all previous versions. | Renamed to `max_page_size` in v4.  
[`SearchJobsForAlertRequest.max_page_size`](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs/searchForAlert#request-body) | Named `SearchJobsForAlertRequest.page_size` in all previous versions. | Renamed to `max_page_size` in v4.  
`Tenant.usage_type` | The `Tenant.usage_type` field was added in v4beta1. | This field has been removed in v4. Data within a tenant is only used to improve search quality within that tenant.  
  
## New additions by version

See the table below for net-new functionality you’ll gain by upgrading from a previous version to v4. For example, if you’re currently using v3, you’ll be able to unlock all of the below functionality by upgrading to v4.

v3p1beta1 (includes v3 features) | v4p1beta1 (includes v3p1beta1 features | v4 (includes v4beta1 features)  
---|---|---  
[New histogram expressions](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/histogram-expression) | [Improvement of commute-based search](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/commute-search) | [Batch operations](https://docs.cloud.google.com/talent-solution/job-search/docs/batch) (BatchDelete)  
[Custom ranking](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/custom-ranking) | [Improvement of feedback mechanism](https://docs.cloud.google.com/talent-solution/job-search/docs/events) | [gRPC](https://www.grpc.io/faq/) (required)  
[Beta client library](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/beta-client-libraries) | [Multi-tenancy support](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/tenants) |   
| [Batch operations](https://docs.cloud.google.com/talent-solution/job-search/docs/batch) (BatchCreate and BatchUpdate) |   
| [gRPC](https://www.grpc.io/faq/) (optional) |   
  
## gRPC client library

Starting with Cloud Talent Solution v4, only [gRPC-based](https://www.grpc.io/faq/) client libraries will be supported. gRPC client libraries are high performance RPC frameworks that can run in any environment and include both REST and RPC interfaces. You will be provided Cloud Talent Solution-generated client libraries supported in various languages (Java, Python, Nodejs, C#, PHP, Ruby) to consume the APIs.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
