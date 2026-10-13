---
url: https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows.executions_v1.types.Execution
title: Class Execution (1.24.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:56:13.675350+00:00
---

# Class Execution (1.24.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows.executions_v1.types.Execution

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Execution (1.24.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.24.0 (latest)  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.1  1.17.0  1.16.0  1.15.1  1.14.5  1.13.0  1.12.0  1.11.0  1.10.2  1.9.1  1.8.0  1.7.4  1.6.3  1.5.0  1.4.1  1.3.0  1.2.3  1.1.0  1.0.0  0.3.2  0.2.0  0.1.0 
    
    
    Execution(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A running instance of a `Workflow </workflows/docs/reference/rest/v1/projects.locations.workflows>`__.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Output only. The resource name of the execution. Format: projects/{project}/locations/{location}/workflows/{workflow}/executions/{execution}   
`start_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Marks the beginning of execution.   
`end_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Marks the end of execution, successful or not.   
`duration` |  `google.protobuf.duration_pb2.Duration`   
Output only. Measures the duration of the execution.   
`state` |  `[google.cloud.workflows.executions_v1.types.Execution.State](https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows.executions_v1.types.Execution.State)`   
Output only. Current state of the execution.   
`argument` |  `str`   
Input parameters of the execution represented as a JSON string. The size limit is 32KB. *Note*: If you are using the REST API directly to run your workflow, you must escape any JSON string value of `argument`. Example: `'{"argument":"{\"firstName\":\"FIRST\",\"lastName\":\"LAST\"}"}'`  
`result` |  `str`   
Output only. Output of the execution represented as a JSON string. The value can only be present if the execution's state is `SUCCEEDED`.   
`error` |  `[google.cloud.workflows.executions_v1.types.Execution.Error](https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows.executions_v1.types.Execution.Error)`   
Output only. The error which caused the execution to finish prematurely. The value is only present if the execution's state is `FAILED` or `CANCELLED`.   
`workflow_revision_id` |  `str`   
Output only. Revision of the workflow this execution is using.   
`call_log_level` |  `[google.cloud.workflows.executions_v1.types.Execution.CallLogLevel](https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows.executions_v1.types.Execution.CallLogLevel)`   
The call logging level associated to this execution.   
`status` |  `[google.cloud.workflows.executions_v1.types.Execution.Status](https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows.executions_v1.types.Execution.Status)`   
Output only. Status tracks the current steps and progress data of this execution.   
`labels` |  `MutableMapping[str, str]`   
Labels associated with this execution. Labels can contain at most 64 entries. Keys and values can be no longer than 63 characters and can only contain lowercase letters, numeric characters, underscores, and dashes. Label keys must start with a letter. International characters are allowed. By default, labels are inherited from the workflow but are overridden by any labels associated with the execution.   
`state_error` |  `[google.cloud.workflows.executions_v1.types.Execution.StateError](https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows.executions_v1.types.Execution.StateError)`   
Output only. Error regarding the state of the Execution resource. For example, this field will have error details if the execution data is unavailable due to revoked KMS key permissions.   
  
## Classes 

### CallLogLevel
    
    
    CallLogLevel(value)

Describes the level of platform logging to apply to calls and call responses during workflow executions.

### Error
    
    
    Error(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Error describes why the execution was abnormally terminated.

### LabelsEntry
    
    
    LabelsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
### StackTrace
    
    
    StackTrace(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A collection of stack elements (frames) where an error occurred.

### StackTraceElement
    
    
    StackTraceElement(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A single stack element (frame) where an error occurred.

### State
    
    
    State(value)

Describes the current state of the execution. More states might be added in the future.

### StateError
    
    
    StateError(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Describes an error related to the current state of the Execution resource.

### Status
    
    
    Status(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Represents the current status of this execution.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
