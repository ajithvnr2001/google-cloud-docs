---
url: https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Internal.FieldOptions.FeatureSupport
title: proto library Client - Class FeatureSupport (v5.36.2) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:00:10.770929+00:00
---

# proto library Client - Class FeatureSupport (v5.36.2)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Internal.FieldOptions.FeatureSupport

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  proto library Client - Class FeatureSupport (v5.36.2) Stay organized with collections  Save and categorize content based on your preferences. 

Reference documentation and code samples for the proto library Client class FeatureSupport.

Information about the support window of a feature.

Generated from protobuf message `google.protobuf.FieldOptions.FeatureSupport`

## Namespace

Google \ Protobuf \ Internal \ FieldOptions

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ edition_introduced` |  `int`   
The edition that this feature was first available in. In editions earlier than this one, the default assigned to EDITION_LEGACY will be used, and proto files will not be able to override it.  
`↳ edition_deprecated` |  `int`   
The edition this feature becomes deprecated in. Using this after this edition may trigger warnings.  
`↳ deprecation_warning` |  `string`   
The deprecation warning text if this feature is used after the edition it was marked deprecated in.  
`↳ edition_removed` |  `int`   
The edition this feature is no longer available in. In editions after this one, the last default assigned will be used, and proto files will not be able to override it.  
`↳ removal_error` |  `string`   
The removal error text if this feature is used after the edition it was removed in.  
  
### getEditionIntroduced

The edition that this feature was first available in. In editions earlier than this one, the default assigned to EDITION_LEGACY will be used, and proto files will not be able to override it.

**Returns**  
---  
**Type** | **Description**  
`int` | one of the values in {@see \Google\Protobuf\Internal\Edition}  
  
### hasEditionIntroduced

### clearEditionIntroduced

### setEditionIntroduced

The edition that this feature was first available in. In editions earlier than this one, the default assigned to EDITION_LEGACY will be used, and proto files will not be able to override it.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
one of the values in [Google\Protobuf\Internal\Edition](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Internal.Edition)  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEditionDeprecated

The edition this feature becomes deprecated in. Using this after this edition may trigger warnings.

**Returns**  
---  
**Type** | **Description**  
`int` | one of the values in {@see \Google\Protobuf\Internal\Edition}  
  
### hasEditionDeprecated

### clearEditionDeprecated

### setEditionDeprecated

The edition this feature becomes deprecated in. Using this after this edition may trigger warnings.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
one of the values in [Google\Protobuf\Internal\Edition](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Internal.Edition)  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDeprecationWarning

The deprecation warning text if this feature is used after the edition it was marked deprecated in.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasDeprecationWarning

### clearDeprecationWarning

### setDeprecationWarning

The deprecation warning text if this feature is used after the edition it was marked deprecated in.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEditionRemoved

The edition this feature is no longer available in. In editions after this one, the last default assigned will be used, and proto files will not be able to override it.

**Returns**  
---  
**Type** | **Description**  
`int` | one of the values in {@see \Google\Protobuf\Internal\Edition}  
  
### hasEditionRemoved

### clearEditionRemoved

### setEditionRemoved

The edition this feature is no longer available in. In editions after this one, the last default assigned will be used, and proto files will not be able to override it.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
one of the values in [Google\Protobuf\Internal\Edition](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Internal.Edition)  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getRemovalError

The removal error text if this feature is used after the edition it was removed in.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasRemovalError

### clearRemovalError

### setRemovalError

The removal error text if this feature is used after the edition it was removed in.

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
