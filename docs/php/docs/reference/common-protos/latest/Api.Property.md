---
url: https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.Property
title: Google API Common Protos Client - Class Property (4.14.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:05:56.112027+00:00
---

# Google API Common Protos Client - Class Property (4.14.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.Property

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google API Common Protos Client - Class Property (4.14.3) Stay organized with collections  Save and categorize content based on your preferences. 

4.14.3 (latest)  4.14.1  4.13.0  4.12.5  4.11.0  4.10.0  4.9.0  4.8.3 

Reference documentation and code samples for the Google API Common Protos Client class Property.

Defines project properties.

API services can define properties that can be assigned to consumer projects so that backends can perform response customization without having to make additional calls or maintain additional storage. For example, Maps API defines properties that controls map tile cache period, or whether to embed a watermark in a result. These values can be set via API producer console. Only API providers can define and set these properties.

Generated from protobuf message `google.api.Property`

## Namespace

Google \ Api

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ name` |  `string`   
The name of the property (a.k.a key).  
`↳ type` |  `int`   
The type of this property.  
`↳ description` |  `string`   
The description of the property  
  
### getName

The name of the property (a.k.a key).

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

The name of the property (a.k.a key).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getType

The type of this property.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [PropertyType](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.Property.PropertyType).  
  
### setType

The type of this property.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [PropertyType](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.Property.PropertyType).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDescription

The description of the property

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDescription

The description of the property

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
