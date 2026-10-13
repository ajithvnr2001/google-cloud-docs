---
url: https://docs.cloud.google.com/python/docs/reference/dataform/latest/google.cloud.dataform_v1beta1.types.WorkflowInvocationAction
title: Class WorkflowInvocationAction (0.11.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:42:37.225561+00:00
---

# Class WorkflowInvocationAction (0.11.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dataform/latest/google.cloud.dataform_v1beta1.types.WorkflowInvocationAction

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class WorkflowInvocationAction (0.11.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.4 (latest)  0.11.3  0.10.0  0.9.0  0.8.0  0.7.0  0.6.2  0.5.16  0.4.1  0.3.0  0.2.3  0.1.0 
    
    
    WorkflowInvocationAction(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Represents a single action in a workflow invocation.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`bigquery_action` |  `[google.cloud.dataform_v1beta1.types.WorkflowInvocationAction.BigQueryAction](https://docs.cloud.google.com/python/docs/reference/dataform/latest/google.cloud.dataform_v1beta1.types.WorkflowInvocationAction.BigQueryAction)`   
Output only. The workflow action's bigquery action details. This field is a member of `oneof`_ `action`.   
`notebook_action` |  `[google.cloud.dataform_v1beta1.types.WorkflowInvocationAction.NotebookAction](https://docs.cloud.google.com/python/docs/reference/dataform/latest/google.cloud.dataform_v1beta1.types.WorkflowInvocationAction.NotebookAction)`   
Output only. The workflow action's notebook action details. This field is a member of `oneof`_ `action`.   
`data_preparation_action` |  `[google.cloud.dataform_v1beta1.types.WorkflowInvocationAction.DataPreparationAction](https://docs.cloud.google.com/python/docs/reference/dataform/latest/google.cloud.dataform_v1beta1.types.WorkflowInvocationAction.DataPreparationAction)`   
Output only. The workflow action's data preparation action details. This field is a member of `oneof`_ `action`.   
`target` |  `[google.cloud.dataform_v1beta1.types.Target](https://docs.cloud.google.com/python/docs/reference/dataform/latest/google.cloud.dataform_v1beta1.types.Target)`   
Output only. This action's identifier. Unique within the workflow invocation.   
`canonical_target` |  `[google.cloud.dataform_v1beta1.types.Target](https://docs.cloud.google.com/python/docs/reference/dataform/latest/google.cloud.dataform_v1beta1.types.Target)`   
Output only. The action's identifier if the project had been compiled without any overrides configured. Unique within the compilation result.   
`state` |  `[google.cloud.dataform_v1beta1.types.WorkflowInvocationAction.State](https://docs.cloud.google.com/python/docs/reference/dataform/latest/google.cloud.dataform_v1beta1.types.WorkflowInvocationAction.State)`   
Output only. This action's current state.   
`failure_reason` |  `str`   
Output only. If and only if action's state is FAILED a failure reason is set.   
`invocation_timing` |  `google.type.interval_pb2.Interval`   
Output only. This action's timing details. `start_time` will be set if the action is in [RUNNING, SUCCEEDED, CANCELLED, FAILED] state. `end_time` will be set if the action is in [SUCCEEDED, CANCELLED, FAILED] state.   
`internal_metadata` |  `str`   
Output only. All the metadata information that is used internally to serve the resource. For example: timestamps, flags, status fields, etc. The format of this field is a JSON string. This field is a member of `oneof`_ `_internal_metadata`.   
  
## Classes 

### BigQueryAction
    
    
    BigQueryAction(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Represents a workflow action that will run against BigQuery.

### DataPreparationAction
    
    
    DataPreparationAction(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Represents a workflow action that will run a Data Preparation.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### NotebookAction
    
    
    NotebookAction(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Represents a workflow action that will run against a Notebook runtime.

### State
    
    
    State(value)

Represents the current state of a workflow invocation action.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
