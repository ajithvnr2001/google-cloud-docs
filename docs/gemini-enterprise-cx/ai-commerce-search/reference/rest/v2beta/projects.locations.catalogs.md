---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs
title: REST Resource: projects.locations.catalogs \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:24.112499+00:00
---

# REST Resource: projects.locations.catalogs  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs

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
  * MerchantCenterLinkingConfig
    * JSON representation
  * MerchantCenterLink
    * JSON representation
  * MerchantCenterFeedFilter
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
        object ([ProductLevelConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs#ProductLevelConfig))
      },
      "merchantCenterLinkingConfig": {
        object ([MerchantCenterLinkingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs#MerchantCenterLinkingConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` Required. Immutable. The fully qualified resource name of the catalog.  
`displayName` |  `string` Required. Immutable. The catalog display name.This field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned.  
`productLevelConfig` |  `object (`[ProductLevelConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs#ProductLevelConfig)`)` Required. The product level configuration.  
`merchantCenterLinkingConfig` |  `object (`[MerchantCenterLinkingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs#MerchantCenterLinkingConfig)`)` The Merchant Center linking configuration. After a link is added, the data stream from Merchant Center to Cloud Retail will be enabled automatically. The requester must have access to the Merchant Center account in order to make changes to this field.  
  
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
`ingestionProductType` |  `string` The type of `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product)`s allowed to be ingested into the catalog. Acceptable values are:

  * `primary` (default): You can ingest `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product)`s of all types. When ingesting a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product)`, its type will default to `[Product.Type.PRIMARY](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.PRIMARY)` if unset.
  * `variant` (incompatible with Retail Search): You can only ingest `[Product.Type.VARIANT](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.VARIANT)` `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product)`s. This means `[Product.primary_product_id](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product.FIELDS.primary_product_id)` cannot be empty.

If this field is set to an invalid value other than these, an INVALID_ARGUMENT error is returned.If this field is `variant` and `[merchantCenterProductIdField](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs#ProductLevelConfig.FIELDS.merchant_center_product_id_field)` is `itemGroupId`, an INVALID_ARGUMENT error is returned.See [Product levels](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/catalog#product-levels) for more details.  
`merchantCenterProductIdField` |  `string` Which field of [Merchant Center Product](https://docs.cloud.google.com/bigquery-transfer/docs/merchant-center-products-schema) should be imported as `[Product.id](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product.FIELDS.id)`. Acceptable values are:

  * `offerId` (default): Import `offerId` as the product ID.
  * `itemGroupId`: Import `itemGroupId` as the product ID. Notice that Retail API will choose one item from the ones with the same `itemGroupId`, and use it to represent the item group.

If this field is set to an invalid value other than these, an INVALID_ARGUMENT error is returned.If this field is `itemGroupId` and `[ingestionProductType](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs#ProductLevelConfig.FIELDS.ingestion_product_type)` is `variant`, an INVALID_ARGUMENT error is returned.See [Product levels](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/catalog#product-levels) for more details.  
  
## MerchantCenterLinkingConfig

Configures Merchant Center linking. Links contained in the config will be used to sync data from a Merchant Center account to a Cloud Retail branch.

JSON representation  
---  
      
    
    {
      "links": [
        {
          object ([MerchantCenterLink](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs#MerchantCenterLink))
        }
      ]
    }  
  
Fields  
---  
`links[]` |  `object (`[MerchantCenterLink](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs#MerchantCenterLink)`)` Links between Merchant Center accounts and branches.  
  
## MerchantCenterLink

Represents a link between a Merchant Center account and a branch. After a link is established, products from the linked Merchant Center account are streamed to the linked branch.

JSON representation  
---  
      
    
    {
      "merchantCenterAccountId": string,
      "branchId": string,
      "destinations": [
        string
      ],
      "regionCode": string,
      "languageCode": string,
      "feeds": [
        {
          object ([MerchantCenterFeedFilter](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs#MerchantCenterFeedFilter))
        }
      ]
    }  
  
Fields  
---  
`merchantCenterAccountId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. The linked [Merchant Center account ID](https://developers.google.com/shopping-content/guides/accountstatuses). The account must be a standalone account or a sub-account of a MCA.  
`branchId` |  `string` The branch ID (e.g. 0/1/2) within this catalog that products from merchantCenterAccountId are streamed to. When updating this field, an empty value will use the currently configured default branch. However, changing the default branch later on won't change the linked branch here.A single branch ID can only have one linked Merchant Center account ID.  
`destinations[]` |  `string` String representing the destination to import for, all if left empty. List of possible values is given in [Included destination](https://support.google.com/merchants/answer/7501026). List of allowed string values: "Shopping_ads", "Buy_on_google_listings", "Display_ads", "Local_inventory _ads", "Free_listings", "Free_local_listings" NOTE: The string values are case sensitive.  
`regionCode` |  `string` Region code of offers to accept. 2-letter Uppercase ISO 3166-1 alpha-2 code. List of values can be found [here](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry) under the `region` tag. If left blank no region filtering will be performed.Example value: `US`.  
`languageCode` |  `string` Language of the title/description and other string attributes. Use language tags defined by [BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). ISO 639-1.This specifies the language of offers in Merchant Center that will be accepted. If empty no language filtering will be performed.Example value: `en`.  
`feeds[]` |  `object (`[MerchantCenterFeedFilter](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs#MerchantCenterFeedFilter)`)` Criteria for the Merchant Center feeds to be ingested via the link. All offers will be ingested if the list is empty. Otherwise the offers will be ingested from selected feeds.  
  
## MerchantCenterFeedFilter

Merchant Center Feed filter criterion.

JSON representation  
---  
      
    
    {
      "primaryFeedId": string,
      "dataSourceId": string,
      "primaryFeedName": string
    }  
  
Fields  
---  
`primaryFeedId  
**(deprecated)**` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` This item is deprecated!Merchant Center primary feed ID. Deprecated: use dataSourceId instead.  
`dataSourceId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` AFM data source ID.  
`primaryFeedName` |  `string` Merchant Center primary feed name. The name is used for the display purposes only.  
  
## Methods  
  
---  
  
### `[completeQuery](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs/completeQuery)`

|  Completes the specified prefix with keyword suggestions.  
  
### `[exportAnalyticsMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs/exportAnalyticsMetrics)`

|  Exports analytics metrics.  
  
### `[getAttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs/getAttributesConfig)`

|  Gets an `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#AttributesConfig)`.  
  
### `[getCompletionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs/getCompletionConfig)`

|  Gets a `[CompletionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/CompletionConfig)`.  
  
### `[getConversationalSearchCustomizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs/getConversationalSearchCustomizationConfig)`

|  Returns the conversational search customization config for a given catalog.  
  
### `[getDefaultBranch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs/getDefaultBranch)`

|  Get which branch is currently default branch set by `[CatalogService.SetDefaultBranch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs/setDefaultBranch#google.cloud.retail.v2beta.CatalogService.SetDefaultBranch)` method under a specified parent catalog.  
  
### `[getGenerativeQuestionFeature](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs/getGenerativeQuestionFeature)`

|  Manages overal generative question feature state -- enables toggling feature on and off.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs/list)`

|  Lists all the `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs#Catalog)`s associated with the project.  
  
### `[patch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs/patch)`

|  Updates the `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs#Catalog)`s.  
  
### `[setDefaultBranch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs/setDefaultBranch)`

|  Set a specified branch id as default branch.  
  
### `[updateAttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs/updateAttributesConfig)`

|  Updates the `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#AttributesConfig)`.  
  
### `[updateCompletionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs/updateCompletionConfig)`

|  Updates the `[CompletionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/CompletionConfig)`s.  
  
### `[updateConversationalSearchCustomizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs/updateConversationalSearchCustomizationConfig)`

|  Updates the conversational search customization config for a given catalog.  
  
### `[updateGenerativeQuestion](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs/updateGenerativeQuestion)`

|  Allows management of individual questions.  
  
### `[updateGenerativeQuestionFeature](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs/updateGenerativeQuestionFeature)`

|  Manages overal generative question feature state -- enables toggling feature on and off.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
