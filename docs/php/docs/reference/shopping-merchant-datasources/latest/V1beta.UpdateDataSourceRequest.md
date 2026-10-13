---
url: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-datasources/latest/V1beta.UpdateDataSourceRequest
title: Google Shopping Merchant DataSources V1beta Client - Class UpdateDataSourceRequest (2.0.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:54:03.907881+00:00
---

# Google Shopping Merchant DataSources V1beta Client - Class UpdateDataSourceRequest (2.0.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-datasources/latest/V1beta.UpdateDataSourceRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Shopping Merchant DataSources V1beta Client - Class UpdateDataSourceRequest (2.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.0.0 (latest)  1.3.6  1.2.1  1.1.1  1.0.0  0.6.0  0.5.1  0.4.0  0.3.1  0.2.3  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Shopping Merchant DataSources V1beta Client class UpdateDataSourceRequest.

Request message for the UpdateDataSource method.

Generated from protobuf message `google.shopping.merchant.datasources.v1beta.UpdateDataSourceRequest`

## Namespace

Google \ Shopping \ Merchant \ DataSources \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ data_source` |  `[DataSource](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-datasources/latest/V1beta.DataSource)`   
Required. The data source resource to update.  
`↳ update_mask` |  `[Google\Protobuf\FieldMask](https://protobuf.dev/reference/php/api-docs/Google/Protobuf/FieldMask)`   
Required. The list of data source fields to be updated. Fields specified in the update mask without a value specified in the body will be deleted from the data source. Providing special "*" value for full data source replacement is not supported.  
  
### getDataSource

Required. The data source resource to update.

**Returns**  
---  
**Type** | **Description**  
`[DataSource](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-datasources/latest/V1beta.DataSource)|null` |   
  
### hasDataSource

### clearDataSource

### setDataSource

Required. The data source resource to update.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[DataSource](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-datasources/latest/V1beta.DataSource)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUpdateMask

Required. The list of data source fields to be updated.

Fields specified in the update mask without a value specified in the body will be deleted from the data source. Providing special "*" value for full data source replacement is not supported.

**Returns**  
---  
**Type** | **Description**  
`[Google\Protobuf\FieldMask](https://protobuf.dev/reference/php/api-docs/Google/Protobuf/FieldMask)|null` |   
  
### hasUpdateMask

### clearUpdateMask

### setUpdateMask

Required. The list of data source fields to be updated.

Fields specified in the update mask without a value specified in the body will be deleted from the data source. Providing special "*" value for full data source replacement is not supported.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Protobuf\FieldMask](https://protobuf.dev/reference/php/api-docs/Google/Protobuf/FieldMask)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### static::build

**Parameters**  
---  
**Name** | **Description**  
`dataSource` |  `[DataSource](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-datasources/latest/V1beta.DataSource)`   
Required. The data source resource to update.  
`updateMask` |  `[Google\Protobuf\FieldMask](https://protobuf.dev/reference/php/api-docs/Google/Protobuf/FieldMask)`   
Required. The list of data source fields to be updated. Fields specified in the update mask without a value specified in the body will be deleted from the data source. Providing special "*" value for full data source replacement is not supported.  
**Returns**  
---  
**Type** | **Description**  
`[UpdateDataSourceRequest](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-datasources/latest/V1beta.UpdateDataSourceRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
