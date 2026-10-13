---
url: https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest/v1beta/billingAccounts.skus
title: REST Resource: billingAccounts.skus \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:28:05.745989+00:00
---

# REST Resource: billingAccounts.skus  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest/v1beta/billingAccounts.skus

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/billing/docs/apis)



Send feedback 

#  REST Resource: billingAccounts.skus Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: BillingAccountSku
    * JSON representation
  * ProductTaxonomy
    * JSON representation
  * TaxonomyCategory
    * JSON representation
  * GeoTaxonomy
    * JSON representation
  * Global
  * Regional
    * JSON representation
  * Region
    * JSON representation
  * MultiRegional
    * JSON representation
  * Type
  * Methods



## Resource: BillingAccountSku

Encapsulates a stock keeping unit (`SKU`) visible to a `billing account`. A SKU distinctly identifies a resource that you can purchase. For a list of available SKUs, see [SKUs](https://cloud.google.com/skus).

JSON representation  
---  
      
    
    {
      "name": string,
      "skuId": string,
      "displayName": string,
      "billingAccountService": string,
      "productTaxonomy": {
        object ([ProductTaxonomy](https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest/v1beta/billingAccounts.skus#ProductTaxonomy))
      },
      "geoTaxonomy": {
        object ([GeoTaxonomy](https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest/v1beta/billingAccounts.skus#GeoTaxonomy))
      }
    }  
  
Fields  
---  
`name` |  `string` Resource name for the `BillingAccountSku`. Example: "billingAccounts/012345-567890-ABCDEF/skus/AA95-CD31-42FE".  
`skuId` |  `string` Unique identifier for the SKU. It is the string after the collection identifier "skus/" Example: "AA95-CD31-42FE".  
`displayName` |  `string` Description of the `BillingAccountSku`. Example: "A2 Instance Core running in Hong Kong".  
`billingAccountService` |  `string` `BillingAccountService` that the `BillingAccountSku` belongs to.  
`productTaxonomy` |  `object (`[ProductTaxonomy](https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest/v1beta/billingAccounts.skus#ProductTaxonomy)`)` List of product categories that apply to the `BillingAccountSku`.  
`geoTaxonomy` |  `object (`[GeoTaxonomy](https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest/v1beta/billingAccounts.skus#GeoTaxonomy)`)` Geographic metadata that applies to the `BillingAccountSku`.  
  
## ProductTaxonomy

Encapsulates product categories, such as `Serverless`, `Cloud Run`, `TaskQueue`, and others.

JSON representation  
---  
      
    
    {
      "taxonomyCategories": [
        {
          object ([TaxonomyCategory](https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest/v1beta/billingAccounts.skus#TaxonomyCategory))
        }
      ]
    }  
  
Fields  
---  
`taxonomyCategories[]` |  `object (`[TaxonomyCategory](https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest/v1beta/billingAccounts.skus#TaxonomyCategory)`)` All product categories that the `billing account SKU` belong to.  
  
## TaxonomyCategory

Encapsulates a product category.

JSON representation  
---  
      
    
    {
      "category": string
    }  
  
Fields  
---  
`category` |  `string` Name of the product category.  
  
## GeoTaxonomy

Encapsulates geographic metadata, such as regions and multi-regions like `us-east4` or `European Union`.

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest/v1beta/billingAccounts.skus#Type)),
    
      // Union field metadata can be only one of the following:
      "globalMetadata": {
        object ([Global](https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest/v1beta/billingAccounts.skus#Global))
      },
      "regionalMetadata": {
        object ([Regional](https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest/v1beta/billingAccounts.skus#Regional))
      },
      "multiRegionalMetadata": {
        object ([MultiRegional](https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest/v1beta/billingAccounts.skus#MultiRegional))
      }
      // End of list of possible types for union field metadata.
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest/v1beta/billingAccounts.skus#Type)`)` Type of geographic taxonomy associated with the `billing account SKU`.  
Union field `metadata`.`metadata` can be only one of the following:  
`globalMetadata` |  `object (`[Global](https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest/v1beta/billingAccounts.skus#Global)`)` Global geographic metadata with no regions.  
`regionalMetadata` |  `object (`[Regional](https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest/v1beta/billingAccounts.skus#Regional)`)` Regional geographic metadata with 1 region.  
`multiRegionalMetadata` |  `object (`[MultiRegional](https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest/v1beta/billingAccounts.skus#MultiRegional)`)` Multi-regional geographic metadata with 2 or more regions.  
  
## Global

This type has no fields.

Encapsulates a global geographic taxonomy.

## Regional

Encapsulates a regional geographic taxonomy.

JSON representation  
---  
      
    
    {
      "region": {
        object ([Region](https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest/v1beta/billingAccounts.skus#Region))
      }
    }  
  
Fields  
---  
`region` |  `object (`[Region](https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest/v1beta/billingAccounts.skus#Region)`)` Google Cloud region associated with the regional geographic taxonomy.  
  
## Region

Encapsulates a Google Cloud region.

JSON representation  
---  
      
    
    {
      "region": string
    }  
  
Fields  
---  
`region` |  `string` Description of a Google Cloud region. Example: "us-west2".  
  
## MultiRegional

Encapsulates a multi-regional geographic taxonomy.

JSON representation  
---  
      
    
    {
      "regions": [
        {
          object ([Region](https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest/v1beta/billingAccounts.skus#Region))
        }
      ]
    }  
  
Fields  
---  
`regions[]` |  `object (`[Region](https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest/v1beta/billingAccounts.skus#Region)`)` Google Cloud regions associated with the multi-regional geographic taxonomy.  
  
## Type

Different types of geographic taxonomy.

Enums  
---  
`TYPE_UNSPECIFIED` | Default value. Unspecified type.  
`TYPE_GLOBAL` | Global geographic taxonomy with no regions.  
`TYPE_REGIONAL` | Regional geographic taxonomy with 1 region.  
`TYPE_MULTI_REGIONAL` | Multi-regional geographic taxonomy with 2 or more regions.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest/v1beta/billingAccounts.skus/get)`

|  Gets a SKU visible to a `billing account`.  
  
### `[list](https://docs.cloud.google.com/billing/docs/reference/pricing-api/rest/v1beta/billingAccounts.skus/list)`

|  Lists SKUs visible to a `billing account`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
