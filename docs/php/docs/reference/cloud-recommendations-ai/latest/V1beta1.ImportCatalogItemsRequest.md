---
url: https://docs.cloud.google.com/php/docs/reference/cloud-recommendations-ai/latest/V1beta1.ImportCatalogItemsRequest
title: Google Cloud Recommendation Engine V1beta1 Client - Class ImportCatalogItemsRequest (0.10.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:35:57.564860+00:00
---

# Google Cloud Recommendation Engine V1beta1 Client - Class ImportCatalogItemsRequest (0.10.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-recommendations-ai/latest/V1beta1.ImportCatalogItemsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Recommendation Engine V1beta1 Client - Class ImportCatalogItemsRequest (0.10.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.3 (latest)  0.9.3  0.8.2  0.7.7  0.6.4  0.5.0  0.4.12 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Recommendation Engine V1beta1 Client class ImportCatalogItemsRequest.

Request message for Import methods.

Generated from protobuf message `google.cloud.recommendationengine.v1beta1.ImportCatalogItemsRequest`

## Namespace

Google \ Cloud \ RecommendationEngine \ V1beta1

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ parent` |  `string`   
Required. `projects/1234/locations/global/catalogs/default_catalog`  
`↳ request_id` |  `string`   
Optional. Unique identifier provided by client, within the ancestor dataset scope. Ensures idempotency and used for request deduplication. Server-generated if unspecified. Up to 128 characters long. This is returned as google.longrunning.Operation.name in the response.  
`↳ input_config` |  `[InputConfig](https://docs.cloud.google.com/php/docs/reference/cloud-recommendations-ai/latest/V1beta1.InputConfig)`   
Required. The desired input location of the data.  
`↳ errors_config` |  `[ImportErrorsConfig](https://docs.cloud.google.com/php/docs/reference/cloud-recommendations-ai/latest/V1beta1.ImportErrorsConfig)`   
Optional. The desired location of errors incurred during the Import.  
  
### getParent

Required. `projects/1234/locations/global/catalogs/default_catalog`

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setParent

Required. `projects/1234/locations/global/catalogs/default_catalog`

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getRequestId

Optional. Unique identifier provided by client, within the ancestor dataset scope. Ensures idempotency and used for request deduplication.

Server-generated if unspecified. Up to 128 characters long. This is returned as google.longrunning.Operation.name in the response.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setRequestId

Optional. Unique identifier provided by client, within the ancestor dataset scope. Ensures idempotency and used for request deduplication.

Server-generated if unspecified. Up to 128 characters long. This is returned as google.longrunning.Operation.name in the response.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getInputConfig

Required. The desired input location of the data.

**Returns**  
---  
**Type** | **Description**  
`[InputConfig](https://docs.cloud.google.com/php/docs/reference/cloud-recommendations-ai/latest/V1beta1.InputConfig)|null` |   
  
### hasInputConfig

### clearInputConfig

### setInputConfig

Required. The desired input location of the data.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[InputConfig](https://docs.cloud.google.com/php/docs/reference/cloud-recommendations-ai/latest/V1beta1.InputConfig)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getErrorsConfig

Optional. The desired location of errors incurred during the Import.

**Returns**  
---  
**Type** | **Description**  
`[ImportErrorsConfig](https://docs.cloud.google.com/php/docs/reference/cloud-recommendations-ai/latest/V1beta1.ImportErrorsConfig)|null` |   
  
### hasErrorsConfig

### clearErrorsConfig

### setErrorsConfig

Optional. The desired location of errors incurred during the Import.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[ImportErrorsConfig](https://docs.cloud.google.com/php/docs/reference/cloud-recommendations-ai/latest/V1beta1.ImportErrorsConfig)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### static::build

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `string`   
Required. `projects/1234/locations/global/catalogs/default_catalog` Please see CatalogServiceClient::catalogName() for help formatting this field.  
`requestId` |  `string`   
Optional. Unique identifier provided by client, within the ancestor dataset scope. Ensures idempotency and used for request deduplication. Server-generated if unspecified. Up to 128 characters long. This is returned as google.longrunning.Operation.name in the response.  
`inputConfig` |  `[InputConfig](https://docs.cloud.google.com/php/docs/reference/cloud-recommendations-ai/latest/V1beta1.InputConfig)`   
Required. The desired input location of the data.  
`errorsConfig` |  `[ImportErrorsConfig](https://docs.cloud.google.com/php/docs/reference/cloud-recommendations-ai/latest/V1beta1.ImportErrorsConfig)`   
Optional. The desired location of errors incurred during the Import.  
**Returns**  
---  
**Type** | **Description**  
`[ImportCatalogItemsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-recommendations-ai/latest/V1beta1.ImportCatalogItemsRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
