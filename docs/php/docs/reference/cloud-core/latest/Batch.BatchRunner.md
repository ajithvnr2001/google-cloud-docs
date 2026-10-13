---
url: https://docs.cloud.google.com/php/docs/reference/cloud-core/latest/Batch.BatchRunner
title: Google Cloud PHP shared dependency, providing functionality useful to all components. Client - Class BatchRunner (1.74.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:21:43.748836+00:00
---

# Google Cloud PHP shared dependency, providing functionality useful to all components. Client - Class BatchRunner (1.74.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-core/latest/Batch.BatchRunner

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud PHP shared dependency, providing functionality useful to all components. Client - Class BatchRunner (1.74.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.74.0 (latest)  1.73.5  1.72.4  1.71.2  1.70.0  1.69.0  1.68.2  1.67.0  1.66.0  1.65.0  1.64.3  1.63.0  1.62.3  1.61.0  1.60.1  1.59.1  1.58.2  1.53.0  1.52.11  1.51.2  1.50.0  1.49.3  1.48.1 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud PHP shared dependency, providing functionality useful to all components. Client class BatchRunner.

A class for executing jobs in batch.

## Namespace

Google \ Cloud \ Core \ Batch

## Methods 

### __construct

Determine internal implementation and loads the configuration.

**Parameters**  
---  
**Name** | **Description**  
`configStorage` |  `[ConfigStorageInterface](https://docs.cloud.google.com/php/docs/reference/cloud-core/latest/Batch.ConfigStorageInterface)`   
[optional] The ConfigStorage object to use. **Defaults to** null. This is only for testing purpose.  
`processor` |  `[ProcessItemInterface](https://docs.cloud.google.com/php/docs/reference/cloud-core/latest/Batch.ProcessItemInterface)`   
[optional] The processor object to use. **Defaults to** null. This is only for testing purpose.  
  
### registerJob

Register a job for batch execution.

**Parameters**  
---  
**Name** | **Description**  
`identifier` |  `string`   
Unique identifier of the job.  
`func` |  `callable`   
Any Callable except for Closure. The callable should accept an array of items as the first argument.  
`options` |  `array`   
Configuration options.  
`↳ batchSize` |  `int`   
The size of the batch.  
`↳ callPeriod` |  `float`   
The period in seconds from the last execution to force executing the job.  
`↳ numWorkers` |  `int`   
The number of child processes. It only takes effect with the [BatchDaemon](https://docs.cloud.google.com/php/docs/reference/cloud-core/latest/Batch.BatchDaemon).  
`↳ bootstrapFile` |  `string`   
A file to load before executing the job. It's needed for registering global functions.  
**Returns**  
---  
**Type** | **Description**  
`bool` | true on success, false on failure  
  
### submitItem

Submit an item.

**Parameters**  
---  
**Name** | **Description**  
`identifier` |  `string`   
Unique identifier of the job.  
`item` |  `mixed`   
It needs to be serializable.  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getJobFromId

Get the job with the given identifier.

**Parameter**  
---  
**Name** | **Description**  
`identifier` |  `string`   
Unique identifier of the job.  
**Returns**  
---  
**Type** | **Description**  
`[BatchJob](https://docs.cloud.google.com/php/docs/reference/cloud-core/latest/Batch.BatchJob)|null` |   
  
### getJobFromIdNum

Get the job with the given numeric id.

**Parameter**  
---  
**Name** | **Description**  
`idNum` |  `int`   
A numeric id of the job.  
**Returns**  
---  
**Type** | **Description**  
`[BatchJob](https://docs.cloud.google.com/php/docs/reference/cloud-core/latest/Batch.BatchJob)|null` |   
  
### getJobs

Get all the jobs.

**Returns**  
---  
**Type** | **Description**  
`array<[BatchJob](https://docs.cloud.google.com/php/docs/reference/cloud-core/latest/Batch.BatchJob)>` |   
  
### loadConfig

Load the config from the storage.

**Returns**  
---  
**Type** | **Description**  
`bool` | true on success  
  
### getProcessor

Gets the item processor.

**Returns**  
---  
**Type** | **Description**  
`[ProcessItemInterface](https://docs.cloud.google.com/php/docs/reference/cloud-core/latest/Batch.ProcessItemInterface)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
