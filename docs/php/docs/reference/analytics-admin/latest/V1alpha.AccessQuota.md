---
url: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AccessQuota
title: Google Analytics Admin V1alpha Client - Class AccessQuota (0.34.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:54:46.924668+00:00
---

# Google Analytics Admin V1alpha Client - Class AccessQuota (0.34.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AccessQuota

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Analytics Admin V1alpha Client - Class AccessQuota (0.34.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.34.3 (latest)  0.33.0  0.32.0  0.31.3  0.30.0  0.29.1  0.28.1  0.27.0  0.26.0  0.25.2  0.24.2  0.23.0  0.22.5  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Analytics Admin V1alpha Client class AccessQuota.

Current state of all quotas for this Analytics property. If any quota for a property is exhausted, all requests to that property will return Resource Exhausted errors.

Generated from protobuf message `google.analytics.admin.v1alpha.AccessQuota`

## Namespace

Google \ Analytics \ Admin \ V1alpha

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ tokens_per_day` |  `[AccessQuotaStatus](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AccessQuotaStatus)`   
Properties can use 250,000 tokens per day. Most requests consume fewer than 10 tokens.  
`↳ tokens_per_hour` |  `[AccessQuotaStatus](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AccessQuotaStatus)`   
Properties can use 50,000 tokens per hour. An API request consumes a single number of tokens, and that number is deducted from all of the hourly, daily, and per project hourly quotas.  
`↳ concurrent_requests` |  `[AccessQuotaStatus](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AccessQuotaStatus)`   
Properties can use up to 50 concurrent requests.  
`↳ server_errors_per_project_per_hour` |  `[AccessQuotaStatus](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AccessQuotaStatus)`   
Properties and cloud project pairs can have up to 50 server errors per hour.  
`↳ tokens_per_project_per_hour` |  `[AccessQuotaStatus](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AccessQuotaStatus)`   
Properties can use up to 25% of their tokens per project per hour. This amounts to Analytics 360 Properties can use 12,500 tokens per project per hour. An API request consumes a single number of tokens, and that number is deducted from all of the hourly, daily, and per project hourly quotas.  
  
### getTokensPerDay

Properties can use 250,000 tokens per day. Most requests consume fewer than 10 tokens.

**Returns**  
---  
**Type** | **Description**  
`[AccessQuotaStatus](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AccessQuotaStatus)|null` |   
  
### hasTokensPerDay

### clearTokensPerDay

### setTokensPerDay

Properties can use 250,000 tokens per day. Most requests consume fewer than 10 tokens.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[AccessQuotaStatus](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AccessQuotaStatus)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getTokensPerHour

Properties can use 50,000 tokens per hour. An API request consumes a single number of tokens, and that number is deducted from all of the hourly, daily, and per project hourly quotas.

**Returns**  
---  
**Type** | **Description**  
`[AccessQuotaStatus](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AccessQuotaStatus)|null` |   
  
### hasTokensPerHour

### clearTokensPerHour

### setTokensPerHour

Properties can use 50,000 tokens per hour. An API request consumes a single number of tokens, and that number is deducted from all of the hourly, daily, and per project hourly quotas.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[AccessQuotaStatus](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AccessQuotaStatus)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getConcurrentRequests

Properties can use up to 50 concurrent requests.

**Returns**  
---  
**Type** | **Description**  
`[AccessQuotaStatus](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AccessQuotaStatus)|null` |   
  
### hasConcurrentRequests

### clearConcurrentRequests

### setConcurrentRequests

Properties can use up to 50 concurrent requests.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[AccessQuotaStatus](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AccessQuotaStatus)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getServerErrorsPerProjectPerHour

Properties and cloud project pairs can have up to 50 server errors per hour.

**Returns**  
---  
**Type** | **Description**  
`[AccessQuotaStatus](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AccessQuotaStatus)|null` |   
  
### hasServerErrorsPerProjectPerHour

### clearServerErrorsPerProjectPerHour

### setServerErrorsPerProjectPerHour

Properties and cloud project pairs can have up to 50 server errors per hour.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[AccessQuotaStatus](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AccessQuotaStatus)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getTokensPerProjectPerHour

Properties can use up to 25% of their tokens per project per hour. This amounts to Analytics 360 Properties can use 12,500 tokens per project per hour. An API request consumes a single number of tokens, and that number is deducted from all of the hourly, daily, and per project hourly quotas.

**Returns**  
---  
**Type** | **Description**  
`[AccessQuotaStatus](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AccessQuotaStatus)|null` |   
  
### hasTokensPerProjectPerHour

### clearTokensPerProjectPerHour

### setTokensPerProjectPerHour

Properties can use up to 25% of their tokens per project per hour. This amounts to Analytics 360 Properties can use 12,500 tokens per project per hour. An API request consumes a single number of tokens, and that number is deducted from all of the hourly, daily, and per project hourly quotas.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[AccessQuotaStatus](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AccessQuotaStatus)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
