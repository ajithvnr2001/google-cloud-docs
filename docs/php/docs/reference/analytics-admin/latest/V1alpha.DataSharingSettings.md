---
url: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataSharingSettings
title: Google Analytics Admin V1alpha Client - Class DataSharingSettings (0.34.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:55:01.308974+00:00
---

# Google Analytics Admin V1alpha Client - Class DataSharingSettings (0.34.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataSharingSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Analytics Admin V1alpha Client - Class DataSharingSettings (0.34.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.34.3 (latest)  0.33.0  0.32.0  0.31.3  0.30.0  0.29.1  0.28.1  0.27.0  0.26.0  0.25.2  0.24.2  0.23.0  0.22.5  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Analytics Admin V1alpha Client class DataSharingSettings.

A resource message representing data sharing settings of a Google Analytics account.

Generated from protobuf message `google.analytics.admin.v1alpha.DataSharingSettings`

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
`↳ name` |  `string`   
Identifier. Resource name. Format: accounts/{account}/dataSharingSettings Example: "accounts/1000/dataSharingSettings"  
`↳ sharing_with_google_support_enabled` |  `bool`   
Allows Google technical support representatives access to your Google Analytics data and account when necessary to provide service and find solutions to technical issues. This field maps to the "Technical support" field in the Google Analytics Admin UI.  
`↳ sharing_with_google_assigned_sales_enabled` |  `bool`   
Allows Google access to your Google Analytics account data, including account usage and configuration data, product spending, and users associated with your Google Analytics account, so that Google can help you make the most of Google products, providing you with insights, offers, recommendations, and optimization tips across Google Analytics and other Google products for business. This field maps to the "Recommendations for your business" field in the Google Analytics Admin UI.  
`↳ sharing_with_google_any_sales_enabled` |  `bool`   
Deprecated. This field is no longer used and always returns false.  
`↳ sharing_with_google_products_enabled` |  `bool`   
Allows Google to use the data to improve other Google products or services. This fields maps to the "Google products & services" field in the Google Analytics Admin UI.  
`↳ sharing_with_others_enabled` |  `bool`   
Enable features like predictions, modeled data, and benchmarking that can provide you with richer business insights when you contribute aggregated measurement data. The data you share (including information about the property from which it is shared) is aggregated and de-identified before being used to generate business insights. This field maps to the "Modeling contributions & business insights" field in the Google Analytics Admin UI.  
  
### getName

Identifier. Resource name.

Format: accounts/{account}/dataSharingSettings Example: "accounts/1000/dataSharingSettings"

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Identifier. Resource name.

Format: accounts/{account}/dataSharingSettings Example: "accounts/1000/dataSharingSettings"

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSharingWithGoogleSupportEnabled

Allows Google technical support representatives access to your Google Analytics data and account when necessary to provide service and find solutions to technical issues.

This field maps to the "Technical support" field in the Google Analytics Admin UI.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setSharingWithGoogleSupportEnabled

Allows Google technical support representatives access to your Google Analytics data and account when necessary to provide service and find solutions to technical issues.

This field maps to the "Technical support" field in the Google Analytics Admin UI.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSharingWithGoogleAssignedSalesEnabled

Allows Google access to your Google Analytics account data, including account usage and configuration data, product spending, and users associated with your Google Analytics account, so that Google can help you make the most of Google products, providing you with insights, offers, recommendations, and optimization tips across Google Analytics and other Google products for business.

This field maps to the "Recommendations for your business" field in the Google Analytics Admin UI.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setSharingWithGoogleAssignedSalesEnabled

Allows Google access to your Google Analytics account data, including account usage and configuration data, product spending, and users associated with your Google Analytics account, so that Google can help you make the most of Google products, providing you with insights, offers, recommendations, and optimization tips across Google Analytics and other Google products for business.

This field maps to the "Recommendations for your business" field in the Google Analytics Admin UI.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSharingWithGoogleAnySalesEnabled

Deprecated. This field is no longer used and always returns false.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setSharingWithGoogleAnySalesEnabled

Deprecated. This field is no longer used and always returns false.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSharingWithGoogleProductsEnabled

Allows Google to use the data to improve other Google products or services.

This fields maps to the "Google products & services" field in the Google Analytics Admin UI.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setSharingWithGoogleProductsEnabled

Allows Google to use the data to improve other Google products or services.

This fields maps to the "Google products & services" field in the Google Analytics Admin UI.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSharingWithOthersEnabled

Enable features like predictions, modeled data, and benchmarking that can provide you with richer business insights when you contribute aggregated measurement data. The data you share (including information about the property from which it is shared) is aggregated and de-identified before being used to generate business insights.

This field maps to the "Modeling contributions & business insights" field in the Google Analytics Admin UI.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setSharingWithOthersEnabled

Enable features like predictions, modeled data, and benchmarking that can provide you with richer business insights when you contribute aggregated measurement data. The data you share (including information about the property from which it is shared) is aggregated and de-identified before being used to generate business insights.

This field maps to the "Modeling contributions & business insights" field in the Google Analytics Admin UI.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
