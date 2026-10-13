---
url: https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.types.Experiment
title: Class Experiment (2.8.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:05:40.721425+00:00
---

# Class Experiment (2.8.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.types.Experiment

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Experiment (2.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.8.0 (latest)  2.7.0  2.6.0  2.1.0  2.0.0  1.43.0  1.42.0  1.41.1  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.1  1.33.0  1.32.1  1.31.1  1.30.1  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.0  1.20.1  1.19.0  1.18.0  1.17.1  1.16.0  1.15.0  1.14.1  1.13.5  1.12.1  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.2  1.2.0  1.1.1  1.0.0  0.8.2  0.7.1  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0  0.1.1 
    
    
    Experiment(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Represents an experiment in an environment.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
The name of the experiment. Format: projects/  
`display_name` |  `str`   
Required. The human-readable name of the experiment (unique in an environment). Limit of 64 characters.   
`description` |  `str`   
The human-readable description of the experiment.   
`state` |  `[google.cloud.dialogflowcx_v3beta1.types.Experiment.State](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.types.Experiment.State)`   
The current state of the experiment. Transition triggered by Experiments.StartExperiment: DRAFT->RUNNING. Transition triggered by Experiments.CancelExperiment: DRAFT->DONE or RUNNING->DONE.   
`definition` |  `[google.cloud.dialogflowcx_v3beta1.types.Experiment.Definition](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.types.Experiment.Definition)`   
The definition of the experiment.   
`rollout_config` |  `[google.cloud.dialogflowcx_v3beta1.types.RolloutConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.types.RolloutConfig)`   
The configuration for auto rollout. If set, there should be exactly two variants in the experiment (control variant being the default version of the flow), the traffic allocation for the non-control variant will gradually increase to 100% when conditions are met, and eventually replace the control variant to become the default version of the flow.   
`rollout_state` |  `[google.cloud.dialogflowcx_v3beta1.types.RolloutState](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.types.RolloutState)`   
State of the auto rollout process.   
`rollout_failure_reason` |  `str`   
The reason why rollout has failed. Should only be set when state is ROLLOUT_FAILED.   
`result` |  `[google.cloud.dialogflowcx_v3beta1.types.Experiment.Result](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.types.Experiment.Result)`   
Inference result of the experiment.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Creation time of this experiment.   
`start_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Start time of this experiment.   
`end_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
End time of this experiment.   
`last_update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Last update time of this experiment.   
`experiment_length` |  `google.protobuf.duration_pb2.Duration`   
Maximum number of days to run the experiment. If auto-rollout is not enabled, default value and maximum will be 30 days. If auto-rollout is enabled, default value and maximum will be 6 days.   
`variants_history` |  `MutableSequence[[google.cloud.dialogflowcx_v3beta1.types.VariantsHistory](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.types.VariantsHistory)]`   
The history of updates to the experiment variants.   
  
## Classes 

### Definition
    
    
    Definition(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Definition of the experiment.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### Result
    
    
    Result(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The inference result which includes an objective metric to optimize and the confidence interval.

### State
    
    
    State(value)

The state of the experiment.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
