---
url: https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Execution.StackTraceElement
title: Google Cloud Workflows V1 Client - Class StackTraceElement (1.4.4) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:31.073656+00:00
---

# Google Cloud Workflows V1 Client - Class StackTraceElement (1.4.4)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Execution.StackTraceElement

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Workflows V1 Client - Class StackTraceElement (1.4.4) Stay organized with collections  Save and categorize content based on your preferences. 

1.4.4 (latest)  1.3.0  1.2.1  1.1.1  1.0.3  0.5.5  0.4.2  0.3.0  0.2.17 

Reference documentation and code samples for the Google Cloud Workflows V1 Client class StackTraceElement.

A single stack element (frame) where an error occurred.

Generated from protobuf message `google.cloud.workflows.executions.v1.Execution.StackTraceElement`

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
`↳ step` |  `string`   
The step the error occurred at.  
`↳ routine` |  `string`   
The routine where the error occurred.  
`↳ position` |  `[StackTraceElement\Position](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Execution.StackTraceElement.Position)`   
The source position information of the stack trace element.  
  
### getStep

The step the error occurred at.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setStep

The step the error occurred at.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getRoutine

The routine where the error occurred.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setRoutine

The routine where the error occurred.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPosition

The source position information of the stack trace element.

**Returns**  
---  
**Type** | **Description**  
`[StackTraceElement\Position](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Execution.StackTraceElement.Position)|null` |   
  
### hasPosition

### clearPosition

### setPosition

The source position information of the stack trace element.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[StackTraceElement\Position](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Execution.StackTraceElement.Position)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
