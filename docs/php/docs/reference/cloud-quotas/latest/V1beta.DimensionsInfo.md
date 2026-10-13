---
url: https://docs.cloud.google.com/php/docs/reference/cloud-quotas/latest/V1beta.DimensionsInfo
title: Google Cloud Quotas V1beta Client - Class DimensionsInfo (1.7.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:07:32.496372+00:00
---

# Google Cloud Quotas V1beta Client - Class DimensionsInfo (1.7.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-quotas/latest/V1beta.DimensionsInfo

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Quotas V1beta Client - Class DimensionsInfo (1.7.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.3 (latest)  1.5.5  1.4.1  1.3.1  1.2.1  1.1.1  1.0.1  0.2.3  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Quotas V1beta Client class DimensionsInfo.

The detailed quota information such as effective quota value for a combination of dimensions.

Generated from protobuf message `google.api.cloudquotas.v1beta.DimensionsInfo`

## Namespace

Google \ Cloud \ CloudQuotas \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ dimensions` |  `array|Google\Protobuf\Internal\MapField`   
The map of dimensions in key-value pairs. The key of a map entry is "region", "zone", or the name of a service-specific dimension, and the value of a map entry is the value of the dimension. If a dimension does not appear in the map of dimensions, the dimensions info applies to all the dimension values except for those that have another DimensionInfo instance configured for the specific value. For example: `{"provider" : "Example Organization"}` where `provider` is a service-specific quota dimension and `Example Organization` is the provider name.  
`↳ details` |  `[QuotaDetails](https://docs.cloud.google.com/php/docs/reference/cloud-quotas/latest/V1beta.QuotaDetails)`   
Quota details for the specified dimensions.  
`↳ applicable_locations` |  `string[]`   
The applicable regions or zones of this dimension. The field is set to ['global'] for quotas that are not per region or per zone. Otherwise, it will be set to the list of locations this dimension info is applicable to.  
  
### getDimensions

The map of dimensions in key-value pairs. The key of a map entry is "region", "zone", or the name of a service-specific dimension, and the value of a map entry is the value of the dimension. If a dimension does not appear in the map of dimensions, the dimensions info applies to all the dimension values except for those that have another DimensionInfo instance configured for the specific value.

For example: `{"provider" : "Example Organization"}` where `provider` is a service-specific quota dimension and `Example Organization` is the provider name.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Internal\MapField` |   
  
### setDimensions

The map of dimensions in key-value pairs. The key of a map entry is "region", "zone", or the name of a service-specific dimension, and the value of a map entry is the value of the dimension. If a dimension does not appear in the map of dimensions, the dimensions info applies to all the dimension values except for those that have another DimensionInfo instance configured for the specific value.

For example: `{"provider" : "Example Organization"}` where `provider` is a service-specific quota dimension and `Example Organization` is the provider name.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array|Google\Protobuf\Internal\MapField`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDetails

Quota details for the specified dimensions.

**Returns**  
---  
**Type** | **Description**  
`[QuotaDetails](https://docs.cloud.google.com/php/docs/reference/cloud-quotas/latest/V1beta.QuotaDetails)|null` |   
  
### hasDetails

### clearDetails

### setDetails

Quota details for the specified dimensions.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[QuotaDetails](https://docs.cloud.google.com/php/docs/reference/cloud-quotas/latest/V1beta.QuotaDetails)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getApplicableLocations

The applicable regions or zones of this dimension. The field is set to ['global'] for quotas that are not per region or per zone.

Otherwise, it will be set to the list of locations this dimension info is applicable to.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<string>` |   
  
### setApplicableLocations

The applicable regions or zones of this dimension. The field is set to ['global'] for quotas that are not per region or per zone.

Otherwise, it will be set to the list of locations this dimension info is applicable to.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string[]`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
