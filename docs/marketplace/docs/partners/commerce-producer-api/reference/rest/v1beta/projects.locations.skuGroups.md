---
url: https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.skuGroups
title: REST Resource: projects.locations.skuGroups \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:16.151016+00:00
---

# REST Resource: projects.locations.skuGroups  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.skuGroups

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ APIs and Reference ](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference)



Send feedback 

#  REST Resource: projects.locations.skuGroups Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: SkuGroup
    * JSON representation
  * Methods



## Resource: SkuGroup

Message describing SkuGroup resource

JSON representation  
---  
      
    
    {
      "name": string,
      "skus": [
        string
      ],
      "cloudBillingSkus": [
        string
      ]
    }  
  
Fields  
---  
`name` |  `string` Output only. Identifier. Name of the SkuGroup.  
`skus[]` |  `string` Output only. Partner SKUs included in the SkuGroup. Format: `projects/{project}/locations/{location}/services/{service}/skus/{sku}`  
`cloudBillingSkus[]` |  `string` Output only. Google SKUs included in the SkuGroup.Used for partner products sold by Google, such as Premium Operating System Images sold for use in Compute Engine. This is not common. SKUs of this type are not present on this API and can instead be found on the Cloud Billing API or at <https://cloud.google.com/skus>.Format: `services/{service}/skus/{sku}`  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.skuGroups/get)`

|  Gets details of a single SkuGroup.  
  
### `[list](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.skuGroups/list)`

|  Lists SkuGroups for the given parent.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-13 UTC."],[],[]] 
