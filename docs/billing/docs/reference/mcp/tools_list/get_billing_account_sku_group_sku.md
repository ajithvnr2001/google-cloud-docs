---
url: https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/get_billing_account_sku_group_sku/
title: MCP Tools Reference: cloudbilling.googleapis.com \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:57:42.011801+00:00
---

# MCP Tools Reference: cloudbilling.googleapis.com  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/get_billing_account_sku_group_sku/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/billing/docs/apis)



Send feedback 

#  MCP Tools Reference: cloudbilling.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `get_billing_account_sku_group_sku`

Gets a billing account visible SKU that is part of a billing account visible SKU group.

The following code sample shows how to use `curl` to call the `get_billing_account_sku_group_sku` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://cloudbilling.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "get_billing_account_sku_group_sku",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Request message for `GetBillingAccountSkuGroupSku`.

### GetBillingAccountSkuGroupSkuRequest

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the `billing account SKU group SKU` to retrieve. Format: billingAccounts/{billing_account}/skuGroups/{sku_group}/skus/{sku}  
  
## Output Schema

Encapsulates a SKU that is part of a `billing account SKU group`.

### BillingAccountSkuGroupSku

JSON representation  
---  
      
    
    {
      "name": string,
      "skuId": string,
      "displayName": string,
      "billingAccountService": string,
      "productTaxonomy": {
        object ([ProductTaxonomy](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_sku_group_skus#Output.Schema.ProductTaxonomy))
      },
      "geoTaxonomy": {
        object ([GeoTaxonomy](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_sku_group_skus#Output.Schema.GeoTaxonomy))
      }
    }  
  
Fields  
---  
`name` |  `string` Resource name for the `BillingAccountSkuGroupSku`. Example: "billingAccounts/012345-567890-ABCDEF/skuGroups/0e6403d1-4694-44d2-a696-7a78b1a69301/skus/AA95-CD31-42FE".  
`skuId` |  `string` Unique identifier for the SKU. It is the string after the collection identifier "skus/" Example: "AA95-CD31-42FE".  
`displayName` |  `string` Description of the `BillingAccountSkuGroupSku`. Example: "A2 Instance Core running in Hong Kong".  
`billingAccountService` |  `string` `BillingAccountService` that the `BillingAccountSkuGroupSku` belongs to.  
`productTaxonomy` |  `object (`[ProductTaxonomy](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_sku_group_skus#Output.Schema.ProductTaxonomy)`)` List of product categories that apply to the `BillingAccountSkuGroupSku`.  
`geoTaxonomy` |  `object (`[GeoTaxonomy](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_sku_group_skus#Output.Schema.GeoTaxonomy)`)` Geographic metadata that applies to the `BillingAccountSkuGroupSku`.  
  
### ProductTaxonomy

JSON representation  
---  
      
    
    {
      "taxonomyCategories": [
        {
          object ([TaxonomyCategory](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_sku_group_skus#Output.Schema.TaxonomyCategory))
        }
      ]
    }  
  
Fields  
---  
`taxonomyCategories[]` |  `object (`[TaxonomyCategory](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_sku_group_skus#Output.Schema.TaxonomyCategory)`)` All product categories that the `billing account SKU group SKU` belong to.  
  
### TaxonomyCategory

JSON representation  
---  
      
    
    {
      "category": string
    }  
  
Fields  
---  
`category` |  `string` Name of the product category.  
  
### GeoTaxonomy

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_sku_group_skus#Output.Schema.Type)),
    
      // Union field metadata can be only one of the following:
      "globalMetadata": {
        object (Global)
      },
      "regionalMetadata": {
        object ([Regional](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_sku_group_skus#Output.Schema.Regional))
      },
      "multiRegionalMetadata": {
        object ([MultiRegional](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_sku_group_skus#Output.Schema.MultiRegional))
      }
      // End of list of possible types for union field metadata.
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_sku_group_skus#Output.Schema.Type)`)` Type of geographic taxonomy associated with the `billing account SKU group SKU`.  
Union field `metadata`.`metadata` can be only one of the following:  
`globalMetadata` |  `object (`Global`)` Global geographic metadata with no regions.  
`regionalMetadata` |  `object (`[Regional](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_sku_group_skus#Output.Schema.Regional)`)` Regional geographic metadata with 1 region.  
`multiRegionalMetadata` |  `object (`[MultiRegional](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_sku_group_skus#Output.Schema.MultiRegional)`)` Multi-regional geographic metadata with 2 or more regions.  
  
### Regional

JSON representation  
---  
      
    
    {
      "region": {
        object ([Region](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_sku_group_skus#Output.Schema.Region))
      }
    }  
  
Fields  
---  
`region` |  `object (`[Region](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_sku_group_skus#Output.Schema.Region)`)` Google Cloud region associated with the regional geographic taxonomy.  
  
### Region

JSON representation  
---  
      
    
    {
      "region": string
    }  
  
Fields  
---  
`region` |  `string` Description of a Google Cloud region. Example: "us-west2".  
  
### MultiRegional

JSON representation  
---  
      
    
    {
      "regions": [
        {
          object ([Region](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_sku_group_skus#Output.Schema.Region))
        }
      ]
    }  
  
Fields  
---  
`regions[]` |  `object (`[Region](https://docs.cloud.google.com/billing/docs/reference/mcp/tools_list/list_billing_account_sku_group_skus#Output.Schema.Region)`)` Google Cloud regions associated with the multi-regional geographic taxonomy.  
  
### Type

Different types of geographic taxonomy.

Enums  
---  
`TYPE_UNSPECIFIED` | Default value. Unspecified type.  
`TYPE_GLOBAL` | Global geographic taxonomy with no regions.  
`TYPE_REGIONAL` | Regional geographic taxonomy with 1 region.  
`TYPE_MULTI_REGIONAL` | Multi-regional geographic taxonomy with 2 or more regions.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-18 UTC."],[],[]] 
