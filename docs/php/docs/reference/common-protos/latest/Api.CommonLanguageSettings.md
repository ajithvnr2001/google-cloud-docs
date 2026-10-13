---
url: https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.CommonLanguageSettings
title: Google API Common Protos Client - Class CommonLanguageSettings (4.14.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:39:21.736634+00:00
---

# Google API Common Protos Client - Class CommonLanguageSettings (4.14.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.CommonLanguageSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google API Common Protos Client - Class CommonLanguageSettings (4.14.3) Stay organized with collections  Save and categorize content based on your preferences. 

4.14.3 (latest)  4.14.1  4.13.0  4.12.5  4.11.0  4.10.0  4.9.0  4.8.3 

Reference documentation and code samples for the Google API Common Protos Client class CommonLanguageSettings.

Required information for every language.

Generated from protobuf message `google.api.CommonLanguageSettings`

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
`↳ reference_docs_uri` |  `string`   
Link to automatically generated reference documentation. Example: <https://cloud.google.com/nodejs/docs/reference/asset/latest>  
`↳ destinations` |  `int[]`   
The destination where API teams want this client library to be published.  
`↳ selective_gapic_generation` |  `[SelectiveGapicGeneration](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.SelectiveGapicGeneration)`   
Configuration for which RPCs should be generated in the GAPIC client. Note: This field should not be used in most cases.  
  
### getReferenceDocsUri

Link to automatically generated reference documentation. Example: <https://cloud.google.com/nodejs/docs/reference/asset/latest>

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setReferenceDocsUri

Link to automatically generated reference documentation. Example: <https://cloud.google.com/nodejs/docs/reference/asset/latest>

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDestinations

The destination where API teams want this client library to be published.

**Returns**  
---  
**Type** | **Description**  
`[Google\Protobuf\RepeatedField](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.RepeatedField.html)<int>` |   
  
### setDestinations

The destination where API teams want this client library to be published.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int[]`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSelectiveGapicGeneration

Configuration for which RPCs should be generated in the GAPIC client.

Note: This field should not be used in most cases.

**Returns**  
---  
**Type** | **Description**  
`[SelectiveGapicGeneration](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.SelectiveGapicGeneration)|null` |   
  
### hasSelectiveGapicGeneration

### clearSelectiveGapicGeneration

### setSelectiveGapicGeneration

Configuration for which RPCs should be generated in the GAPIC client.

Note: This field should not be used in most cases.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[SelectiveGapicGeneration](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.SelectiveGapicGeneration)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
