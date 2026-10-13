---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs
title: REST Resource: projects.locations.catalogs \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:07.592340+00:00
---

# REST Resource: projects.locations.catalogs  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  REST Resource: projects.locations.catalogs Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Catalog
    * JSON representation
  * ProductLevelConfig
    * JSON representation
  * Methods



## Resource: Catalog

The catalog configuration.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "productLevelConfig": {
        object ([ProductLevelConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs#ProductLevelConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` Required. Immutable. The fully qualified resource name of the catalog.  
`displayName` |  `string` Required. Immutable. The catalog display name.This field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned.  
`productLevelConfig` |  `object (`[ProductLevelConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs#ProductLevelConfig)`)` Required. The product level configuration.  
  
## ProductLevelConfig

Configures what level the product should be uploaded with regards to how users will be send events and how predictions will be made.

JSON representation  
---  
      
    
    {
      "ingestionProductType": string,
      "merchantCenterProductIdField": string
    }  
  
Fields  
---  
`ingestionProductType` |  `string` The type of `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product)`s allowed to be ingested into the catalog. Acceptable values are:

  * `primary` (default): You can ingest `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product)`s of all types. When ingesting a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product)`, its type will default to `[Product.Type.PRIMARY](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.PRIMARY)` if unset.
  * `variant` (incompatible with Retail Search): You can only ingest `[Product.Type.VARIANT](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.VARIANT)` `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product)`s. This means `[Product.primary_product_id](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.primary_product_id)` cannot be empty.

If this field is set to an invalid value other than these, an INVALID_ARGUMENT error is returned.If this field is `variant` and `[merchantCenterProductIdField](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs#ProductLevelConfig.FIELDS.merchant_center_product_id_field)` is `itemGroupId`, an INVALID_ARGUMENT error is returned.See [Product levels](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/catalog#product-levels) for more details.  
`merchantCenterProductIdField` |  `string` Which field of [Merchant Center Product](https://docs.cloud.google.com/bigquery-transfer/docs/merchant-center-products-schema) should be imported as `[Product.id](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.id)`. Acceptable values are:

  * `offerId` (default): Import `offerId` as the product ID.
  * `itemGroupId`: Import `itemGroupId` as the product ID. Notice that Retail API will choose one item from the ones with the same `itemGroupId`, and use it to represent the item group.

If this field is set to an invalid value other than these, an INVALID_ARGUMENT error is returned.If this field is `itemGroupId` and `[ingestionProductType](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs#ProductLevelConfig.FIELDS.ingestion_product_type)` is `variant`, an INVALID_ARGUMENT error is returned.See [Product levels](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/catalog#product-levels) for more details.  
  
## Methods  
  
---  
  
### `[completeQuery](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/completeQuery)`

|  Completes the specified prefix with keyword suggestions.  
  
### `[exportAnalyticsMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/exportAnalyticsMetrics)`

|  Exports analytics metrics.  
  
### `[getAttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/getAttributesConfig)`

|  Gets an `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.attributesConfig#AttributesConfig)`.  
  
### `[getCompletionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/getCompletionConfig)`

|  Gets a `[CompletionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/CompletionConfig)`.  
  
### `[getConversationalSearchCustomizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/getConversationalSearchCustomizationConfig)`

|  Returns the conversational search customization config for a given catalog.  
  
### `[getDefaultBranch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/getDefaultBranch)`

|  Get which branch is currently default branch set by `[CatalogService.SetDefaultBranch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/setDefaultBranch#google.cloud.retail.v2.CatalogService.SetDefaultBranch)` method under a specified parent catalog.  
  
### `[getGenerativeQuestionFeature](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/getGenerativeQuestionFeature)`

|  Manages overal generative question feature state -- enables toggling feature on and off.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/list)`

|  Lists all the `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs#Catalog)`s associated with the project.  
  
### `[patch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/patch)`

|  Updates the `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs#Catalog)`s.  
  
### `[setDefaultBranch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/setDefaultBranch)`

|  Set a specified branch id as default branch.  
  
### `[updateAttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/updateAttributesConfig)`

|  Updates the `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.attributesConfig#AttributesConfig)`.  
  
### `[updateCompletionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/updateCompletionConfig)`

|  Updates the `[CompletionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/CompletionConfig)`s.  
  
### `[updateConversationalSearchCustomizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/updateConversationalSearchCustomizationConfig)`

|  Updates the conversational search customization config for a given catalog.  
  
### `[updateGenerativeQuestion](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/updateGenerativeQuestion)`

|  Allows management of individual questions.  
  
### `[updateGenerativeQuestionFeature](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs/updateGenerativeQuestionFeature)`

|  Manages overal generative question feature state -- enables toggling feature on and off.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
