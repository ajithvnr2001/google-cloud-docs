---
url: https://docs.cloud.google.com/php/docs/reference/cloud-modelarmor/latest/V1beta.RaiFilterSettings.RaiFilter
title: Google Cloud Model Armor V1beta Client - Class RaiFilter (0.8.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:00:11.959315+00:00
---

# Google Cloud Model Armor V1beta Client - Class RaiFilter (0.8.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-modelarmor/latest/V1beta.RaiFilterSettings.RaiFilter

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Model Armor V1beta Client - Class RaiFilter (0.8.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.3 (latest)  0.7.0  0.6.0  0.5.3  0.4.0  0.3.1  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Model Armor V1beta Client class RaiFilter.

Responsible AI filter.

Generated from protobuf message `google.cloud.modelarmor.v1beta.RaiFilterSettings.RaiFilter`

## Namespace

Google \ Cloud \ ModelArmor \ V1beta \ RaiFilterSettings

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ filter_type` |  `int`   
Required. Type of responsible AI filter.  
`↳ confidence_level` |  `int`   
Optional. Confidence level for this RAI filter. During data sanitization, if data is classified under this filter with a confidence level equal to or greater than the specified level, a positive match is reported. If the confidence level is unspecified (i.e., 0), the system will use a reasonable default level based on the `filter_type`.  
  
### getFilterType

Required. Type of responsible AI filter.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [RaiFilterType](https://docs.cloud.google.com/php/docs/reference/cloud-modelarmor/latest/V1beta.RaiFilterType).  
  
### setFilterType

Required. Type of responsible AI filter.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [RaiFilterType](https://docs.cloud.google.com/php/docs/reference/cloud-modelarmor/latest/V1beta.RaiFilterType).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getConfidenceLevel

Optional. Confidence level for this RAI filter.

During data sanitization, if data is classified under this filter with a confidence level equal to or greater than the specified level, a positive match is reported. If the confidence level is unspecified (i.e., 0), the system will use a reasonable default level based on the `filter_type`.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [DetectionConfidenceLevel](https://docs.cloud.google.com/php/docs/reference/cloud-modelarmor/latest/V1beta.DetectionConfidenceLevel).  
  
### setConfidenceLevel

Optional. Confidence level for this RAI filter.

During data sanitization, if data is classified under this filter with a confidence level equal to or greater than the specified level, a positive match is reported. If the confidence level is unspecified (i.e., 0), the system will use a reasonable default level based on the `filter_type`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [DetectionConfidenceLevel](https://docs.cloud.google.com/php/docs/reference/cloud-modelarmor/latest/V1beta.DetectionConfidenceLevel).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
