---
url: https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers/
title: REST Resource: customers \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:22:46.591156+00:00
---

# REST Resource: customers  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)



Send feedback 

#  REST Resource: customers Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Customer
    * JSON representation
  * Methods



## Resource: Customer

Entity representing a SAS customer.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "sasUserIds": [
        string
      ]
    }  
  
Fields  
---  
`name` |  `string` Output only. Resource name of the customer.  
`displayName` |  `string` Required. Name of the organization that the customer entity represents.  
`sasUserIds[]` |  `string` User IDs used by the devices belonging to this customer.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers/get)`

|  Returns a requested `[customer](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers#Customer)`.  
  
### `[list](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers/list)`

|  Returns a list of requested `[customers](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers#Customer)`.  
  
### `[patch](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers/patch)`

|  Updates an existing `[customer](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers#Customer)`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
