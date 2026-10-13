---
url: https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Internal.ExtensionRangeOptions.Declaration
title: proto library Client - Class Declaration (v5.36.2) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:19:53.505423+00:00
---

# proto library Client - Class Declaration (v5.36.2)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Internal.ExtensionRangeOptions.Declaration

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  proto library Client - Class Declaration (v5.36.2) Stay organized with collections  Save and categorize content based on your preferences. 

Reference documentation and code samples for the proto library Client class Declaration.

Generated from protobuf message `google.protobuf.ExtensionRangeOptions.Declaration`

## Namespace

Google \ Protobuf \ Internal \ ExtensionRangeOptions

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ number` |  `int`   
The extension number declared within the extension range.  
`↳ full_name` |  `string`   
The fully-qualified name of the extension field. There must be a leading dot in front of the full name.  
`↳ type` |  `string`   
The fully-qualified type name of the extension field. Unlike Metadata.type, Declaration.type must have a leading dot for messages and enums.  
`↳ reserved` |  `bool`   
If true, indicates that the number is reserved in the extension range, and any extension field with the number will fail to compile. Set this when a declared extension field is deleted.  
`↳ repeated` |  `bool`   
If true, indicates that the extension must be defined as repeated. Otherwise the extension must be defined as optional.  
  
### getNumber

The extension number declared within the extension range.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### hasNumber

### clearNumber

### setNumber

The extension number declared within the extension range.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFullName

The fully-qualified name of the extension field. There must be a leading dot in front of the full name.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasFullName

### clearFullName

### setFullName

The fully-qualified name of the extension field. There must be a leading dot in front of the full name.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getType

The fully-qualified type name of the extension field. Unlike Metadata.type, Declaration.type must have a leading dot for messages and enums.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasType

### clearType

### setType

The fully-qualified type name of the extension field. Unlike Metadata.type, Declaration.type must have a leading dot for messages and enums.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getReserved

If true, indicates that the number is reserved in the extension range, and any extension field with the number will fail to compile. Set this when a declared extension field is deleted.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### hasReserved

### clearReserved

### setReserved

If true, indicates that the number is reserved in the extension range, and any extension field with the number will fail to compile. Set this when a declared extension field is deleted.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getRepeated

If true, indicates that the extension must be defined as repeated.

Otherwise the extension must be defined as optional.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### hasRepeated

### clearRepeated

### setRepeated

If true, indicates that the extension must be defined as repeated.

Otherwise the extension must be defined as optional.

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

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
