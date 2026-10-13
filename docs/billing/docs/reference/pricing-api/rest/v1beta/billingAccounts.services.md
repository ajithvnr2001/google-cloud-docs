---
url: https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest/v1beta/billingAccounts.services
title: REST Resource: billingAccounts.services \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:27:53.325847+00:00
---

# REST Resource: billingAccounts.services  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest/v1beta/billingAccounts.services

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/billing/docs/apis)



Send feedback 

#  REST Resource: billingAccounts.services Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: BillingAccountService
    * JSON representation
  * Methods



## Resource: BillingAccountService

Encapsulates a Google Cloud service visible to a `billing account`.

JSON representation  
---  
      
    
    {
      "name": string,
      "serviceId": string,
      "displayName": string
    }  
  
Fields  
---  
`name` |  `string` Resource name for the `BillingAccountService`. Example: "billingAccounts/012345-567890-ABCDEF/services/DA34-426B-A397".  
`serviceId` |  `string` Identifier for the service. It is the string after the collection identifier "services/". Example: "DA34-426B-A397".  
`displayName` |  `string` Description of the `BillingAccountService`. Example: "BigQuery", "Compute Engine".  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest/v1beta/billingAccounts.services/get)`

|  Gets a Google Cloud service visible to a `billing account`.  
  
### `[list](https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest/v1beta/billingAccounts.services/list)`

|  Lists services visible to a `billing account`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
