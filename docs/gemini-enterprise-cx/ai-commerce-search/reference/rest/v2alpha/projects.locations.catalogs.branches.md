---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches
title: REST Resource: projects.locations.catalogs.branches \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:14:48.103806+00:00
---

# REST Resource: projects.locations.catalogs.branches  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  REST Resource: projects.locations.catalogs.branches Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Branch
    * JSON representation
  * ProductCountStatistic
    * JSON representation
  * ProductCountScope
  * QualityMetric
    * JSON representation
  * Methods



## Resource: Branch

A data branch that stores all instances of `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`s.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "isDefault": boolean,
      "lastProductImportTime": string,
      "productCountStats": [
        {
          object ([ProductCountStatistic](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches#ProductCountStatistic))
        }
      ],
      "qualityMetrics": [
        {
          object ([QualityMetric](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches#QualityMetric))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Immutable. Full resource name of the branch, such as `projects/*/locations/global/catalogs/default_catalog/branches/branchId`.  
`displayName` |  `string` Output only. Human readable name of the branch to display in the UI.  
`isDefault` |  `boolean` Output only. Indicates whether this branch is set as the default branch of its parent catalog.  
`lastProductImportTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp of last import through `[ProductService.ImportProducts](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/import#google.cloud.retail.v2alpha.ProductService.ImportProducts)`. Empty value means no import has been made to this branch.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`productCountStats[]` |  `object (`[ProductCountStatistic](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches#ProductCountStatistic)`)` Output only. Statistics for number of products in the branch, provided for different `[scopes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches#ProductCountScope)`.This field is not populated in `[BranchView.BRANCH_VIEW_BASIC](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/BranchView#ENUM_VALUES.BRANCH_VIEW_BASIC)` view.  
`qualityMetrics[]` |  `object (`[QualityMetric](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches#QualityMetric)`)` Output only. The quality metrics measured among products of this branch.See `[QualityMetric.requirement_key](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches#QualityMetric.FIELDS.requirement_key)` for supported metrics. Metrics could be missing if failed to retrieve.This field is not populated in `[BranchView.BRANCH_VIEW_BASIC](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/BranchView#ENUM_VALUES.BRANCH_VIEW_BASIC)` view.  
  
## ProductCountStatistic

A statistic about the number of products in a branch.

JSON representation  
---  
      
    
    {
      "scope": enum ([ProductCountScope](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches#ProductCountScope)),
      "counts": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`scope` |  `enum (`[ProductCountScope](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches#ProductCountScope)`)` [ProductCountScope] of the [counts].  
`counts` |  `map (key: string, value: string ([int64](https://developers.google.com/discovery/v1/type-format) format))` The number of products in `[scope](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches#ProductCountStatistic.FIELDS.scope)` broken down into different groups.The key is a group representing a set of products, and the value is the number of products in that group. Note: keys in this map may change over time.Possible keys: * "primary-in-stock", products have `[Product.Type.PRIMARY](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.PRIMARY)` type and `[Product.Availability.IN_STOCK](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Availability.ENUM_VALUES.IN_STOCK)` availability.

  * "primary-out-of-stock", products have `[Product.Type.PRIMARY](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.PRIMARY)` type and `[Product.Availability.OUT_OF_STOCK](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Availability.ENUM_VALUES.OUT_OF_STOCK)` availability.
  * "primary-preorder", products have `[Product.Type.PRIMARY](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.PRIMARY)` type and `[Product.Availability.PREORDER](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Availability.ENUM_VALUES.PREORDER)` availability.
  * "primary-backorder", products have `[Product.Type.PRIMARY](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.PRIMARY)` type and `[Product.Availability.BACKORDER](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Availability.ENUM_VALUES.BACKORDER)` availability.
  * "variant-in-stock", products have `[Product.Type.VARIANT](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.VARIANT)` type and `[Product.Availability.IN_STOCK](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Availability.ENUM_VALUES.IN_STOCK)` availability.
  * "variant-out-of-stock", products have `[Product.Type.VARIANT](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.VARIANT)` type and `[Product.Availability.OUT_OF_STOCK](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Availability.ENUM_VALUES.OUT_OF_STOCK)` availability.
  * "variant-preorder", products have `[Product.Type.VARIANT](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.VARIANT)` type and `[Product.Availability.PREORDER](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Availability.ENUM_VALUES.PREORDER)` availability.
  * "variant-backorder", products have `[Product.Type.VARIANT](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.VARIANT)` type and `[Product.Availability.BACKORDER](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Availability.ENUM_VALUES.BACKORDER)` availability.
  * "price-discounted", products have [Product.price_info.price] < [Product.price_info.original_price].

  
  
## ProductCountScope

Scope of what products are included for this count.

Enums  
---  
`PRODUCT_COUNT_SCOPE_UNSPECIFIED` | Default value for enum. This value is not used in the API response.  
`ALL_PRODUCTS` | Scope for all existing products in the branch. Useful for understanding how many products there are in a branch.  
`LAST_24_HOUR_UPDATE` | Scope for products created or updated in the last 24 hours.  
  
## QualityMetric

Metric measured on a group of `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`s against a certain quality requirement. Contains the number of products that pass the check and the number of products that don't.

JSON representation  
---  
      
    
    {
      "requirementKey": string,
      "qualifiedProductCount": integer,
      "unqualifiedProductCount": integer,
      "suggestedQualityPercentThreshold": number,
      "unqualifiedSampleProducts": [
        {
          object ([Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product))
        }
      ]
    }  
  
Fields  
---  
`requirementKey` |  `string` The key that represents a quality requirement rule.Supported keys: * "has-valid-uri": product has a valid and accessible `[uri](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.uri)`.

  * "available-expire-time-conformance": `[Product.available_time](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.available_time)` is early than "now", and `[Product.expire_time](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.expire_time)` is greater than "now".
  * "has-searchable-attributes": product has at least one `[attribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.attributes)` set to searchable.
  * "has-description": product has non-empty `[description](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.description)`.
  * "has-at-least-bigram-title": Product `[title](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.title)` has at least two words. A comprehensive title helps to improve search quality.
  * "variant-has-image": the `[variant](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.VARIANT)` products has at least one `[image](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.images)`. You may ignore this metric if all your products are at `[primary](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.PRIMARY)` level.
  * "variant-has-price-info": the `[variant](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.VARIANT)` products has `[priceInfo](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.price_info)` set. You may ignore this metric if all your products are at `[primary](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.PRIMARY)` level.
  * "has-publish-time": product has non-empty `[publishTime](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.publish_time)`.

  
`qualifiedProductCount` |  `integer` Number of products passing the quality requirement check. We only check searchable products.  
`unqualifiedProductCount` |  `integer` Number of products failing the quality requirement check. We only check searchable products.  
`suggestedQualityPercentThreshold` |  `number` Value from 0 to 100 representing the suggested percentage of products that meet the quality requirements to get good search and recommendation performance. 100 * (qualifiedProductCount) / (qualifiedProductCount + unqualifiedProductCount) should be greater or equal to this suggestion.  
`unqualifiedSampleProducts[]` |  `object (`[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`)` A list of a maximum of 100 sample products that do not qualify for this requirement.This field is only populated in the response to `[BranchService.GetBranch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches/get#google.cloud.retail.v2alpha.BranchService.GetBranch)` API, and is always empty for `[BranchService.ListBranches](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches/list#google.cloud.retail.v2alpha.BranchService.ListBranches)`.Only the following fields are set in the `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`.

  * `[Product.name](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.name)`
  * `[Product.id](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.id)`
  * `[Product.title](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.title)`

  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches/get)`

|  Retrieves a `[Branch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches#Branch)`.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches/list)`

|  Lists all instances of `[Branch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches#Branch)` under the specified parent `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs#Catalog)`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
