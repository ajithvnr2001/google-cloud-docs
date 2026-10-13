---
url: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateSearchAds360LinkRequest
title: Google Analytics Admin V1alpha Client - Class CreateSearchAds360LinkRequest (0.34.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:55:00.051776+00:00
---

# Google Analytics Admin V1alpha Client - Class CreateSearchAds360LinkRequest (0.34.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateSearchAds360LinkRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Analytics Admin V1alpha Client - Class CreateSearchAds360LinkRequest (0.34.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.34.3 (latest)  0.33.0  0.32.0  0.31.3  0.30.0  0.29.1  0.28.1  0.27.0  0.26.0  0.25.2  0.24.2  0.23.0  0.22.5  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Analytics Admin V1alpha Client class CreateSearchAds360LinkRequest.

Request message for CreateSearchAds360Link RPC.

Generated from protobuf message `google.analytics.admin.v1alpha.CreateSearchAds360LinkRequest`

## Namespace

Google \ Analytics \ Admin \ V1alpha

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ parent` |  `string`   
Required. Example format: properties/1234  
`↳ search_ads_360_link` |  `[SearchAds360Link](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SearchAds360Link)`   
Required. The SearchAds360Link to create.  
  
### getParent

Required. Example format: properties/1234

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setParent

Required. Example format: properties/1234

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSearchAds360Link

Required. The SearchAds360Link to create.

**Returns**  
---  
**Type** | **Description**  
`[SearchAds360Link](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SearchAds360Link)|null` |   
  
### hasSearchAds360Link

### clearSearchAds360Link

### setSearchAds360Link

Required. The SearchAds360Link to create.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[SearchAds360Link](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SearchAds360Link)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### static::build

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `string`   
Required. Example format: properties/1234 Please see AnalyticsAdminServiceClient::propertyName() for help formatting this field.  
`searchAds360Link` |  `[SearchAds360Link](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.SearchAds360Link)`   
Required. The SearchAds360Link to create.  
**Returns**  
---  
**Type** | **Description**  
`[CreateSearchAds360LinkRequest](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.CreateSearchAds360LinkRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
