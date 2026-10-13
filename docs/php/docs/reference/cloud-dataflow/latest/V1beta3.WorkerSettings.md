---
url: https://docs.cloud.google.com/php/docs/reference/cloud-dataflow/latest/V1beta3.WorkerSettings
title: Google Cloud Dataflow V1beta3 Client - Class WorkerSettings (0.11.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:14:43.551266+00:00
---

# Google Cloud Dataflow V1beta3 Client - Class WorkerSettings (0.11.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-dataflow/latest/V1beta3.WorkerSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Dataflow V1beta3 Client - Class WorkerSettings (0.11.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.3 (latest)  0.10.0  0.9.3  0.8.2  0.7.1  0.6.6  0.5.1  0.4.1  0.3.10 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Dataflow V1beta3 Client class WorkerSettings.

Provides data to pass through to the worker harness.

Generated from protobuf message `google.dataflow.v1beta3.WorkerSettings`

## Namespace

Google \ Cloud \ Dataflow \ V1beta3

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ base_url` |  `string`   
The base URL for accessing Google Cloud APIs. When workers access Google Cloud APIs, they logically do so via relative URLs. If this field is specified, it supplies the base URL to use for resolving these relative URLs. The normative algorithm used is defined by RFC 1808, "Relative Uniform Resource Locators". If not specified, the default value is "<http://www.googleapis.com/>"  
`↳ reporting_enabled` |  `bool`   
Whether to send work progress updates to the service.  
`↳ service_path` |  `string`   
The Cloud Dataflow service path relative to the root URL, for example, "dataflow/v1b3/projects".  
`↳ shuffle_service_path` |  `string`   
The Shuffle service path relative to the root URL, for example, "shuffle/v1beta1".  
`↳ worker_id` |  `string`   
The ID of the worker running this pipeline.  
`↳ temp_storage_prefix` |  `string`   
The prefix of the resources the system should use for temporary storage. The supported resource type is: Google Cloud Storage: storage.googleapis.com/{bucket}/{object} bucket.storage.googleapis.com/{object}  
  
### getBaseUrl

The base URL for accessing Google Cloud APIs.

When workers access Google Cloud APIs, they logically do so via relative URLs. If this field is specified, it supplies the base URL to use for resolving these relative URLs. The normative algorithm used is defined by RFC 1808, "Relative Uniform Resource Locators". If not specified, the default value is "<http://www.googleapis.com/>"

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setBaseUrl

The base URL for accessing Google Cloud APIs.

When workers access Google Cloud APIs, they logically do so via relative URLs. If this field is specified, it supplies the base URL to use for resolving these relative URLs. The normative algorithm used is defined by RFC 1808, "Relative Uniform Resource Locators". If not specified, the default value is "<http://www.googleapis.com/>"

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getReportingEnabled

Whether to send work progress updates to the service.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setReportingEnabled

Whether to send work progress updates to the service.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getServicePath

The Cloud Dataflow service path relative to the root URL, for example, "dataflow/v1b3/projects".

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setServicePath

The Cloud Dataflow service path relative to the root URL, for example, "dataflow/v1b3/projects".

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getShuffleServicePath

The Shuffle service path relative to the root URL, for example, "shuffle/v1beta1".

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setShuffleServicePath

The Shuffle service path relative to the root URL, for example, "shuffle/v1beta1".

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getWorkerId

The ID of the worker running this pipeline.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setWorkerId

The ID of the worker running this pipeline.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getTempStoragePrefix

The prefix of the resources the system should use for temporary storage.

The supported resource type is: Google Cloud Storage: storage.googleapis.com/{bucket}/{object} bucket.storage.googleapis.com/{object}

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setTempStoragePrefix

The prefix of the resources the system should use for temporary storage.

The supported resource type is: Google Cloud Storage: storage.googleapis.com/{bucket}/{object} bucket.storage.googleapis.com/{object}

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
