---
url: https://docs.cloud.google.com/php/docs/reference/cloud-gke-hub/latest/ConfigManagement.V1.SyncError
title: Google Cloud Gke Hub V1 Client - Class SyncError (1.4.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:00:34.107068+00:00
---

# Google Cloud Gke Hub V1 Client - Class SyncError (1.4.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-gke-hub/latest/ConfigManagement.V1.SyncError

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Gke Hub V1 Client - Class SyncError (1.4.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.4.3 (latest)  1.3.1  1.2.2  1.1.0  1.0.6  0.10.0  0.9.5  0.8.2  0.7.1  0.6.3  0.5.6 

Reference documentation and code samples for the Google Cloud Gke Hub V1 Client class SyncError.

An ACM created error representing a problem syncing configurations

Generated from protobuf message `google.cloud.gkehub.configmanagement.v1.SyncError`

## Namespace

Google \ Cloud \ GkeHub \ ConfigManagement \ V1

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ code` |  `string`   
An ACM defined error code  
`↳ error_message` |  `string`   
A description of the error  
`↳ error_resources` |  `array<[ErrorResource](https://docs.cloud.google.com/php/docs/reference/cloud-gke-hub/latest/ConfigManagement.V1.ErrorResource)>`   
A list of config(s) associated with the error, if any  
  
### getCode

An ACM defined error code

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setCode

An ACM defined error code

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getErrorMessage

A description of the error

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setErrorMessage

A description of the error

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getErrorResources

A list of config(s) associated with the error, if any

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[ErrorResource](https://docs.cloud.google.com/php/docs/reference/cloud-gke-hub/latest/ConfigManagement.V1.ErrorResource)>` |   
  
### setErrorResources

A list of config(s) associated with the error, if any

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[ErrorResource](https://docs.cloud.google.com/php/docs/reference/cloud-gke-hub/latest/ConfigManagement.V1.ErrorResource)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
