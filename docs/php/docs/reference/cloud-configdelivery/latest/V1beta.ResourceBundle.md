---
url: https://docs.cloud.google.com/php/docs/reference/cloud-configdelivery/latest/V1beta.ResourceBundle
title: Google Cloud Config Delivery V1beta Client - Class ResourceBundle (0.4.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:16:46.422689+00:00
---

# Google Cloud Config Delivery V1beta Client - Class ResourceBundle (0.4.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-configdelivery/latest/V1beta.ResourceBundle

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Config Delivery V1beta Client - Class ResourceBundle (0.4.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.3 (latest)  0.3.3  0.2.1  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Config Delivery V1beta Client class ResourceBundle.

ResourceBundle represent a collection of kubernetes configuration resources.

Generated from protobuf message `google.cloud.configdelivery.v1beta.ResourceBundle`

## Namespace

Google \ Cloud \ ConfigDelivery \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ name` |  `string`   
Identifier. Name of the `ResourceBundle`. Format is `projects/{project}/locations/{location}/resourceBundle /[a-z][a-z0-9\-]{0,62}`.  
`↳ create_time` |  `Google\Protobuf\Timestamp`   
Output only. Time `ResourceBundle` was created.  
`↳ update_time` |  `Google\Protobuf\Timestamp`   
Output only. Time `ResourceBundle` was last updated.  
`↳ labels` |  `array|Google\Protobuf\Internal\MapField`   
Optional. Labels as key value pairs.  
`↳ description` |  `string`   
Optional. Human readable description of the `ResourceBundle`.  
  
### getName

Identifier. Name of the `ResourceBundle`. Format is `projects/{project}/locations/{location}/resourceBundle /[a-z][a-z0-9\-]{0,62}`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Identifier. Name of the `ResourceBundle`. Format is `projects/{project}/locations/{location}/resourceBundle /[a-z][a-z0-9\-]{0,62}`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCreateTime

Output only. Time `ResourceBundle` was created.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasCreateTime

### clearCreateTime

### setCreateTime

Output only. Time `ResourceBundle` was created.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUpdateTime

Output only. Time `ResourceBundle` was last updated.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasUpdateTime

### clearUpdateTime

### setUpdateTime

Output only. Time `ResourceBundle` was last updated.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getLabels

Optional. Labels as key value pairs.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Internal\MapField` |   
  
### setLabels

Optional. Labels as key value pairs.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array|Google\Protobuf\Internal\MapField`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDescription

Optional. Human readable description of the `ResourceBundle`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDescription

Optional. Human readable description of the `ResourceBundle`.

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

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
