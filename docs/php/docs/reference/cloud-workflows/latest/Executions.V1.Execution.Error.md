---
url: https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Execution.Error
title: Google Cloud Workflows V1 Client - Class Error (1.4.4) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:05:54.836099+00:00
---

# Google Cloud Workflows V1 Client - Class Error (1.4.4)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Execution.Error

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Workflows V1 Client - Class Error (1.4.4) Stay organized with collections  Save and categorize content based on your preferences. 

1.4.4 (latest)  1.3.0  1.2.1  1.1.1  1.0.3  0.5.5  0.4.2  0.3.0  0.2.17 

Reference documentation and code samples for the Google Cloud Workflows V1 Client class Error.

Error describes why the execution was abnormally terminated.

Generated from protobuf message `google.cloud.workflows.executions.v1.Execution.Error`

## Namespace

Google \ Cloud \ Workflows \ Executions \ V1 \ Execution

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ payload` |  `string`   
Error message and data returned represented as a JSON string.  
`↳ context` |  `string`   
Human-readable stack trace string.  
`↳ stack_trace` |  `[StackTrace](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Execution.StackTrace)`   
Stack trace with detailed information of where error was generated.  
  
### getPayload

Error message and data returned represented as a JSON string.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setPayload

Error message and data returned represented as a JSON string.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getContext

Human-readable stack trace string.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setContext

Human-readable stack trace string.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getStackTrace

Stack trace with detailed information of where error was generated.

**Returns**  
---  
**Type** | **Description**  
`[StackTrace](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Execution.StackTrace)|null` |   
  
### hasStackTrace

### clearStackTrace

### setStackTrace

Stack trace with detailed information of where error was generated.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[StackTrace](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Execution.StackTrace)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
