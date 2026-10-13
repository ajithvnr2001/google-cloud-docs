---
url: https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Execution
title: Google Cloud Workflows V1 Client - Class Execution (1.4.4) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:30.927094+00:00
---

# Google Cloud Workflows V1 Client - Class Execution (1.4.4)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Execution

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Workflows V1 Client - Class Execution (1.4.4) Stay organized with collections  Save and categorize content based on your preferences. 

1.4.4 (latest)  1.3.0  1.2.1  1.1.1  1.0.3  0.5.5  0.4.2  0.3.0  0.2.17 

Reference documentation and code samples for the Google Cloud Workflows V1 Client class Execution.

A running instance of a [Workflow](https://cloud.google.com/workflows/docs/reference/rest/v1/projects.locations.workflows).

Generated from protobuf message `google.cloud.workflows.executions.v1.Execution`

## Namespace

Google \ Cloud \ Workflows \ Executions \ V1

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ name` |  `string`   
Output only. The resource name of the execution. Format: projects/{project}/locations/{location}/workflows/{workflow}/executions/{execution}  
`↳ start_time` |  `Google\Protobuf\Timestamp`   
Output only. Marks the beginning of execution.  
`↳ end_time` |  `Google\Protobuf\Timestamp`   
Output only. Marks the end of execution, successful or not.  
`↳ duration` |  `Google\Protobuf\Duration`   
Output only. Measures the duration of the execution.  
`↳ state` |  `int`   
Output only. Current state of the execution.  
`↳ argument` |  `string`   
Input parameters of the execution represented as a JSON string. The size limit is 32KB. _Note_ : If you are using the REST API directly to run your workflow, you must escape any JSON string value of `argument`. Example: `'{"argument":"{\"firstName\":\"FIRST\",\"lastName\":\"LAST\"}"}'`  
`↳ result` |  `string`   
Output only. Output of the execution represented as a JSON string. The value can only be present if the execution's state is `SUCCEEDED`.  
`↳ error` |  `[Execution\Error](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Execution.Error)`   
Output only. The error which caused the execution to finish prematurely. The value is only present if the execution's state is `FAILED` or `CANCELLED`.  
`↳ workflow_revision_id` |  `string`   
Output only. Revision of the workflow this execution is using.  
`↳ call_log_level` |  `int`   
The call logging level associated to this execution.  
`↳ status` |  `[Execution\Status](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Execution.Status)`   
Output only. Status tracks the current steps and progress data of this execution.  
`↳ labels` |  `array|Google\Protobuf\Internal\MapField`   
Labels associated with this execution. Labels can contain at most 64 entries. Keys and values can be no longer than 63 characters and can only contain lowercase letters, numeric characters, underscores, and dashes. Label keys must start with a letter. International characters are allowed. By default, labels are inherited from the workflow but are overridden by any labels associated with the execution.  
`↳ state_error` |  `[Execution\StateError](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Execution.StateError)`   
Output only. Error regarding the state of the Execution resource. For example, this field will have error details if the execution data is unavailable due to revoked KMS key permissions.  
  
### getName

Output only. The resource name of the execution.

Format: projects/{project}/locations/{location}/workflows/{workflow}/executions/{execution}

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Output only. The resource name of the execution.

Format: projects/{project}/locations/{location}/workflows/{workflow}/executions/{execution}

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getStartTime

Output only. Marks the beginning of execution.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasStartTime

### clearStartTime

### setStartTime

Output only. Marks the beginning of execution.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEndTime

Output only. Marks the end of execution, successful or not.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasEndTime

### clearEndTime

### setEndTime

Output only. Marks the end of execution, successful or not.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDuration

Output only. Measures the duration of the execution.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Duration|null` |   
  
### hasDuration

### clearDuration

### setDuration

Output only. Measures the duration of the execution.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Duration`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getState

Output only. Current state of the execution.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [State](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Execution.State).  
  
### setState

Output only. Current state of the execution.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [State](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Execution.State).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getArgument

Input parameters of the execution represented as a JSON string.

The size limit is 32KB. _Note_ : If you are using the REST API directly to run your workflow, you must escape any JSON string value of `argument`. Example: `'{"argument":"{\"firstName\":\"FIRST\",\"lastName\":\"LAST\"}"}'`

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setArgument

Input parameters of the execution represented as a JSON string.

The size limit is 32KB. _Note_ : If you are using the REST API directly to run your workflow, you must escape any JSON string value of `argument`. Example: `'{"argument":"{\"firstName\":\"FIRST\",\"lastName\":\"LAST\"}"}'`

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getResult

Output only. Output of the execution represented as a JSON string. The value can only be present if the execution's state is `SUCCEEDED`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setResult

Output only. Output of the execution represented as a JSON string. The value can only be present if the execution's state is `SUCCEEDED`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getError

Output only. The error which caused the execution to finish prematurely.

The value is only present if the execution's state is `FAILED` or `CANCELLED`.

**Returns**  
---  
**Type** | **Description**  
`[Execution\Error](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Execution.Error)|null` |   
  
### hasError

### clearError

### setError

Output only. The error which caused the execution to finish prematurely.

The value is only present if the execution's state is `FAILED` or `CANCELLED`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Execution\Error](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Execution.Error)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getWorkflowRevisionId

Output only. Revision of the workflow this execution is using.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setWorkflowRevisionId

Output only. Revision of the workflow this execution is using.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCallLogLevel

The call logging level associated to this execution.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [CallLogLevel](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Execution.CallLogLevel).  
  
### setCallLogLevel

The call logging level associated to this execution.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [CallLogLevel](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Execution.CallLogLevel).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getStatus

Output only. Status tracks the current steps and progress data of this execution.

**Returns**  
---  
**Type** | **Description**  
`[Execution\Status](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Execution.Status)|null` |   
  
### hasStatus

### clearStatus

### setStatus

Output only. Status tracks the current steps and progress data of this execution.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Execution\Status](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Execution.Status)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getLabels

Labels associated with this execution.

Labels can contain at most 64 entries. Keys and values can be no longer than 63 characters and can only contain lowercase letters, numeric characters, underscores, and dashes. Label keys must start with a letter. International characters are allowed. By default, labels are inherited from the workflow but are overridden by any labels associated with the execution.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Internal\MapField` |   
  
### setLabels

Labels associated with this execution.

Labels can contain at most 64 entries. Keys and values can be no longer than 63 characters and can only contain lowercase letters, numeric characters, underscores, and dashes. Label keys must start with a letter. International characters are allowed. By default, labels are inherited from the workflow but are overridden by any labels associated with the execution.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array|Google\Protobuf\Internal\MapField`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getStateError

Output only. Error regarding the state of the Execution resource. For example, this field will have error details if the execution data is unavailable due to revoked KMS key permissions.

**Returns**  
---  
**Type** | **Description**  
`[Execution\StateError](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Execution.StateError)|null` |   
  
### hasStateError

### clearStateError

### setStateError

Output only. Error regarding the state of the Execution resource. For example, this field will have error details if the execution data is unavailable due to revoked KMS key permissions.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Execution\StateError](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Execution.StateError)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
