---
url: https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.standardOffers
title: REST Resource: projects.locations.services.standardOffers \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:10:25.804447+00:00
---

# REST Resource: projects.locations.services.standardOffers  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.standardOffers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ APIs and Reference ](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference)



Send feedback 

#  REST Resource: projects.locations.services.standardOffers Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: StandardOffer
    * JSON representation
  * PriceModel
    * JSON representation
  * FlatFeeSubscription
    * JSON representation
  * Usage
    * JSON representation
  * SkuList
    * JSON representation
  * SkuGroupList
    * JSON representation
  * Methods



## Resource: StandardOffer

Message describing the StandardOffer resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "effectiveTime": string,
      "expireTime": string,
      "serviceLevel": string,
      "serviceLevelTitle": string,
      "priceModel": {
        object ([PriceModel](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.standardOffers#PriceModel))
      },
    
      // Union field term can be only one of the following:
      "termDurationMonths": integer
      // End of list of possible types for union field term.
    }  
  
Fields  
---  
`name` |  `string` Identifier. Name of resource.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Creation time of the offer.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Last update time of the offer.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`effectiveTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Effective time of the offer. Prior to this time, the offer cannot be purchased or used as the base standard offer of a private offer.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`expireTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Expire time of the offer. An offer is expired if its expire time is in the past. An expired standard offer cannot be purchased or used as the base standard offer of a private offer.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`serviceLevel` |  `string` Output only. Identifier that distinguishes between different service levels of the same product that constitute distinct offerings to customers with different pricing.The service levels of a product are also referred to in some cases as the product's 'plans', and the `serviceLevel` value is referred to in some cases as the "plan ID".Multiple non-expired standard offers can share the same service level when they are subscription offers for different term durations.  
`serviceLevelTitle` |  `string` Output only. Title of the service level.Not included for `STANDARD_OFFER_VIEW_BASIC`.  
`priceModel` |  `object (`[PriceModel](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.standardOffers#PriceModel)`)` Output only. Price model of the offer.  
Union field `term`. Term of the offer. Applicable only to subscription offers. `term` can be only one of the following:  
`termDurationMonths` |  `integer` Output only. Term duration of the offer in months. Applicable only to offers with a subscription price model. Additional forms of offer term may be added in the future.  
  
## PriceModel

Price model of the offer.

JSON representation  
---  
      
    
    {
      "usage": {
        object ([Usage](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.standardOffers#Usage))
      },
    
      // Union field subscription can be only one of the following:
      "flatFee": {
        object ([FlatFeeSubscription](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.standardOffers#FlatFeeSubscription))
      }
      // End of list of possible types for union field subscription.
    }  
  
Fields  
---  
`usage` |  `object (`[Usage](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.standardOffers#Usage)`)` Output only. Price configurations for the usage part.  
Union field `subscription`. Price configurations for the subscription part. `subscription` can be only one of the following:  
`flatFee` |  `object (`[FlatFeeSubscription](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.standardOffers#FlatFeeSubscription)`)` Output only. Price configurations for the flat fee subscription.  
  
## FlatFeeSubscription

Price configurations for flat fee subscriptions.

JSON representation  
---  
      
    
    {
      "sku": string
    }  
  
Fields  
---  
`sku` |  `string` Output only. Flat fee subscription SKU for the offer.  
  
## Usage

Price configurations for the usage part.

JSON representation  
---  
      
    
    {
    
      // Union field skus can be only one of the following:
      "skuList": {
        object ([SkuList](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.standardOffers#SkuList))
      },
      "skuGroupList": {
        object ([SkuGroupList](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.standardOffers#SkuGroupList))
      }
      // End of list of possible types for union field skus.
    }  
  
Fields  
---  
Union field `skus`. The SKUs that the offer's usage fees are charged against. `skus` can be only one of the following:  
`skuList` |  `object (`[SkuList](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.standardOffers#SkuList)`)` Output only. The offer's usage fees are charged against these SKUs.  
`skuGroupList` |  `object (`[SkuGroupList](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.standardOffers#SkuGroupList)`)` Output only. The offer's usage fees are charged against the SKUs in these groups.  
  
## SkuList

A collection of SKUs.

JSON representation  
---  
      
    
    {
      "skus": [
        string
      ]
    }  
  
Fields  
---  
`skus[]` |  `string` Output only. List of SKUs by name.  
  
## SkuGroupList

A collection of SkuGroups.

JSON representation  
---  
      
    
    {
      "skuGroups": [
        string
      ]
    }  
  
Fields  
---  
`skuGroups[]` |  `string` Output only. List of SkuGroups by name.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.standardOffers/get)`

|  Gets details of a single StandardOffer.  
  
### `[list](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.standardOffers/list)`

|  Lists StandardOffers for the given parent.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-13 UTC."],[],[]] 
