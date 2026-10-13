---
url: https://docs.cloud.google.com/php/docs/reference/cloud-private-catalog/latest/V1beta1.SearchProductsRequest
title: Google Cloud Private Catalog V1beta1 Client - Class SearchProductsRequest (0.7.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:49:29.044576+00:00
---

# Google Cloud Private Catalog V1beta1 Client - Class SearchProductsRequest (0.7.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-private-catalog/latest/V1beta1.SearchProductsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Private Catalog V1beta1 Client - Class SearchProductsRequest (0.7.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.3 (latest)  0.6.3  0.5.3  0.4.6  0.3.3  0.2.13 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Private Catalog V1beta1 Client class SearchProductsRequest.

Request message for [PrivateCatalog.SearchProducts](https://docs.cloud.google.com/php/docs/reference/cloud-private-catalog/latest/V1beta1.Client.PrivateCatalogClient#_Google_Cloud_PrivateCatalog_V1beta1_Client_PrivateCatalogClient__searchProducts__).

Generated from protobuf message `google.cloud.privatecatalog.v1beta1.SearchProductsRequest`

## Namespace

Google \ Cloud \ PrivateCatalog \ V1beta1

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ resource` |  `string`   
Required. The name of the resource context. See [SearchCatalogsRequest.resource](https://docs.cloud.google.com/php/docs/reference/cloud-private-catalog/latest/V1beta1.SearchCatalogsRequest#_Google_Cloud_PrivateCatalog_V1beta1_SearchCatalogsRequest__getResource__) for details.  
`↳ query` |  `string`   
The query to filter the products. The supported queries are: * * List products of all catalogs: empty * * List products under a catalog: `parent=catalogs/{catalog}` * * Get a product by name: `name=catalogs/{catalog}/products/{product}`  
`↳ page_size` |  `int`   
The maximum number of entries that are requested.  
`↳ page_token` |  `string`   
A pagination token returned from a previous call to SearchProducts that indicates where this listing should continue from.  
  
### getResource

Required. The name of the resource context. See [SearchCatalogsRequest.resource](https://docs.cloud.google.com/php/docs/reference/cloud-private-catalog/latest/V1beta1.SearchCatalogsRequest#_Google_Cloud_PrivateCatalog_V1beta1_SearchCatalogsRequest__getResource__) for details.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setResource

Required. The name of the resource context. See [SearchCatalogsRequest.resource](https://docs.cloud.google.com/php/docs/reference/cloud-private-catalog/latest/V1beta1.SearchCatalogsRequest#_Google_Cloud_PrivateCatalog_V1beta1_SearchCatalogsRequest__getResource__) for details.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getQuery

The query to filter the products.

The supported queries are:

  * List products of all catalogs: empty
  * List products under a catalog: `parent=catalogs/{catalog}`
  * Get a product by name: `name=catalogs/{catalog}/products/{product}`



**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setQuery

The query to filter the products.

The supported queries are:

  * List products of all catalogs: empty
  * List products under a catalog: `parent=catalogs/{catalog}`
  * Get a product by name: `name=catalogs/{catalog}/products/{product}`



**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageSize

The maximum number of entries that are requested.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setPageSize

The maximum number of entries that are requested.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageToken

A pagination token returned from a previous call to SearchProducts that indicates where this listing should continue from.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setPageToken

A pagination token returned from a previous call to SearchProducts that indicates where this listing should continue from.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
