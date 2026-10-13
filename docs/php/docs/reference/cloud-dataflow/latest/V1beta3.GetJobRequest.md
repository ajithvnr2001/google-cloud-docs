---
url: https://docs.cloud.google.com/php/docs/reference/cloud-dataflow/latest/V1beta3.GetJobRequest
title: Google Cloud Dataflow V1beta3 Client - Class GetJobRequest (0.11.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:45:11.900093+00:00
---

# Google Cloud Dataflow V1beta3 Client - Class GetJobRequest (0.11.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-dataflow/latest/V1beta3.GetJobRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Dataflow V1beta3 Client - Class GetJobRequest (0.11.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.3 (latest)  0.10.0  0.9.3  0.8.2  0.7.1  0.6.6  0.5.1  0.4.1  0.3.10 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Dataflow V1beta3 Client class GetJobRequest.

Request to get the state of a Cloud Dataflow job.

Generated from protobuf message `google.dataflow.v1beta3.GetJobRequest`

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
`↳ project_id` |  `string`   
The ID of the Cloud Platform project that the job belongs to.  
`↳ job_id` |  `string`   
The job ID.  
`↳ view` |  `int`   
The level of information requested in response.  
`↳ location` |  `string`   
The [regional endpoint](https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that contains this job.  
  
### getProjectId

The ID of the Cloud Platform project that the job belongs to.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setProjectId

The ID of the Cloud Platform project that the job belongs to.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getJobId

The job ID.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setJobId

The job ID.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getView

The level of information requested in response.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [JobView](https://docs.cloud.google.com/php/docs/reference/cloud-dataflow/latest/V1beta3.JobView).  
  
### setView

The level of information requested in response.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [JobView](https://docs.cloud.google.com/php/docs/reference/cloud-dataflow/latest/V1beta3.JobView).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getLocation

The [regional endpoint](https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that contains this job.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setLocation

The [regional endpoint](https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that contains this job.

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
