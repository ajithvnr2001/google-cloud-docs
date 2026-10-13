---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig/batchRemoveCatalogAttributes/
title: Method: projects.locations.catalogs.attributesConfig.batchRemoveCatalogAttributes \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:26.629891+00:00
---

# Method: projects.locations.catalogs.attributesConfig.batchRemoveCatalogAttributes  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig/batchRemoveCatalogAttributes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Method: projects.locations.catalogs.attributesConfig.batchRemoveCatalogAttributes Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Removes all specified `[CatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#CatalogAttribute)`s from the `[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#AttributesConfig)`.

### HTTP request

`POST https://retail.googleapis.com/v2beta/{attributesConfig=projects/*/locations/*/catalogs/*/attributesConfig}:batchRemoveCatalogAttributes`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`attributesConfig` |  `string` Required. The attributes config resource shared by all catalog attributes being deleted. Format: `projects/{projectNumber}/locations/{locationId}/catalogs/{catalogId}/attributesConfig`  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "attributeKeys": [
        string
      ]
    }  
  
Fields  
---  
`attributeKeys[]` |  `string` Required. The attribute name keys of the `[CatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#CatalogAttribute)`s to delete. A maximum of 1000 catalog attributes can be deleted in a batch.  
  
### Response body

Response of the `[CatalogService.BatchRemoveCatalogAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig/batchRemoveCatalogAttributes#google.cloud.retail.v2beta.CatalogService.BatchRemoveCatalogAttributes)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "deletedCatalogAttributes": [
        string
      ],
      "resetCatalogAttributes": [
        string
      ]
    }  
  
Fields  
---  
`deletedCatalogAttributes[]` |  `string` Catalog attributes that were deleted. Only pre-loaded `[catalog attributes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#CatalogAttribute)` that are neither `[in use](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#CatalogAttribute.FIELDS.in_use)` by products nor predefined can be deleted.  
`resetCatalogAttributes[]` |  `string` Catalog attributes that were reset. `[Catalog attributes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#CatalogAttribute)` that are either `[in use](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.attributesConfig#CatalogAttribute.FIELDS.in_use)` by products or are predefined attributes cannot be deleted; however, their configuration properties will reset to default values upon removal request.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `attributesConfig` resource:

  * `retail.attributesConfigs.batchRemoveCatalogAttributes`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
