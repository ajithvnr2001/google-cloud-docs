---
url: https://docs.cloud.google.com/php/docs/reference/cloud-dataform/latest/V1beta1.WorkflowTriggerConfig
title: Google Cloud Dataform V1beta1 Client - Class WorkflowTriggerConfig (0.17.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:31:32.996074+00:00
---

# Google Cloud Dataform V1beta1 Client - Class WorkflowTriggerConfig (0.17.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-dataform/latest/V1beta1.WorkflowTriggerConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Dataform V1beta1 Client - Class WorkflowTriggerConfig (0.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.0 (latest)  0.16.0  0.15.3  0.12.0  0.11.0  0.10.1  0.9.2  0.8.1  0.7.0  0.6.0  0.5.1  0.4.7  0.3.0  0.2.3  0.1.6 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Dataform V1beta1 Client class WorkflowTriggerConfig.

Represents a trigger configuration for a workflow.

Generated from protobuf message `google.cloud.dataform.v1beta1.WorkflowTriggerConfig`

## Namespace

Google \ Cloud \ Dataform \ V1beta1

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ condition` |  `int`   
Optional. The condition to use when triggering the workflow.  
`↳ workflow_triggers` |  `array<[WorkflowTrigger](https://docs.cloud.google.com/php/docs/reference/cloud-dataform/latest/V1beta1.WorkflowTrigger)>`   
Required. The trigger definitions to invoke a workflow.  
`↳ min_execution_duration` |  `Google\Protobuf\Duration`   
Optional. Minimum duration between two consecutive executions. If not specified, the workflow will be executed every time trigger conditions are met and there is no ongoing workflow execution.  
`↳ max_wait_duration` |  `Google\Protobuf\Duration`   
Optional. The effective maximum wait time duration for the trigger condition to be met. If not specified, the workflow won't be triggered until conditions are met.  
`↳ recent_trigger_evaluation_records` |  `array<[TriggerEvaluationRecord](https://docs.cloud.google.com/php/docs/reference/cloud-dataform/latest/V1beta1.TriggerEvaluationRecord)>`   
Output only. Records of the 10 most recent trigger evaluations, ordered in descending order of `evaluation_time`. Updated whenever the service evaluates the trigger conditions (via polling or upon receiving a push event).  
`↳ last_successful_evaluation_time` |  `Google\Protobuf\Timestamp`   
Output only. The timestamp of the last successful trigger evaluation.  
  
### getCondition

Optional. The condition to use when triggering the workflow.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [Condition](https://docs.cloud.google.com/php/docs/reference/cloud-dataform/latest/V1beta1.WorkflowTriggerConfig.Condition).  
  
### setCondition

Optional. The condition to use when triggering the workflow.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [Condition](https://docs.cloud.google.com/php/docs/reference/cloud-dataform/latest/V1beta1.WorkflowTriggerConfig.Condition).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getWorkflowTriggers

Required. The trigger definitions to invoke a workflow.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[WorkflowTrigger](https://docs.cloud.google.com/php/docs/reference/cloud-dataform/latest/V1beta1.WorkflowTrigger)>` |   
  
### setWorkflowTriggers

Required. The trigger definitions to invoke a workflow.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[WorkflowTrigger](https://docs.cloud.google.com/php/docs/reference/cloud-dataform/latest/V1beta1.WorkflowTrigger)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMinExecutionDuration

Optional. Minimum duration between two consecutive executions. If not specified, the workflow will be executed every time trigger conditions are met and there is no ongoing workflow execution.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Duration|null` |   
  
### hasMinExecutionDuration

### clearMinExecutionDuration

### setMinExecutionDuration

Optional. Minimum duration between two consecutive executions. If not specified, the workflow will be executed every time trigger conditions are met and there is no ongoing workflow execution.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Duration`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMaxWaitDuration

Optional. The effective maximum wait time duration for the trigger condition to be met. If not specified, the workflow won't be triggered until conditions are met.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Duration|null` |   
  
### hasMaxWaitDuration

### clearMaxWaitDuration

### setMaxWaitDuration

Optional. The effective maximum wait time duration for the trigger condition to be met. If not specified, the workflow won't be triggered until conditions are met.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Duration`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getRecentTriggerEvaluationRecords

Output only. Records of the 10 most recent trigger evaluations, ordered in descending order of `evaluation_time`. Updated whenever the service evaluates the trigger conditions (via polling or upon receiving a push event).

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[TriggerEvaluationRecord](https://docs.cloud.google.com/php/docs/reference/cloud-dataform/latest/V1beta1.TriggerEvaluationRecord)>` |   
  
### setRecentTriggerEvaluationRecords

Output only. Records of the 10 most recent trigger evaluations, ordered in descending order of `evaluation_time`. Updated whenever the service evaluates the trigger conditions (via polling or upon receiving a push event).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[TriggerEvaluationRecord](https://docs.cloud.google.com/php/docs/reference/cloud-dataform/latest/V1beta1.TriggerEvaluationRecord)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getLastSuccessfulEvaluationTime

Output only. The timestamp of the last successful trigger evaluation.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasLastSuccessfulEvaluationTime

### clearLastSuccessfulEvaluationTime

### setLastSuccessfulEvaluationTime

Output only. The timestamp of the last successful trigger evaluation.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
