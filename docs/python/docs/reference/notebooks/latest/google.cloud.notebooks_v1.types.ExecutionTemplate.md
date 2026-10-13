---
url: https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ExecutionTemplate
title: Class ExecutionTemplate (1.18.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:40:39.602735+00:00
---

# Class ExecutionTemplate (1.18.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ExecutionTemplate

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ExecutionTemplate (1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.0  1.16.0  1.15.0  1.14.0  1.13.3  1.12.0  1.11.1  1.10.5  1.9.0  1.8.0  1.7.1  1.6.1  1.5.1  1.4.4  1.3.2  1.2.1  1.1.1  1.0.0  0.4.3  0.3.2  0.2.0  0.1.2 
    
    
    ExecutionTemplate(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The description a notebook execution workload.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`scale_tier` |  `[google.cloud.notebooks_v1.types.ExecutionTemplate.ScaleTier](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ExecutionTemplate.ScaleTier)`   
Required. Scale tier of the hardware used for notebook execution. DEPRECATED Will be discontinued. As right now only CUSTOM is supported.   
`master_type` |  `str`   
Specifies the type of virtual machine to use for your training job's master worker. You must specify this field when `scaleTier` is set to `CUSTOM`. You can use certain Compute Engine machine types directly in this field. The following types are supported: \- `n1-standard-4` \- `n1-standard-8` \- `n1-standard-16` \- `n1-standard-32` \- `n1-standard-64` \- `n1-standard-96` \- `n1-highmem-2` \- `n1-highmem-4` \- `n1-highmem-8` \- `n1-highmem-16` \- `n1-highmem-32` \- `n1-highmem-64` \- `n1-highmem-96` \- `n1-highcpu-16` \- `n1-highcpu-32` \- `n1-highcpu-64` \- `n1-highcpu-96` Alternatively, you can use the following legacy machine types: \- `standard` \- `large_model` \- `complex_model_s` \- `complex_model_m` \- `complex_model_l` \- `standard_gpu` \- `complex_model_m_gpu` \- `complex_model_l_gpu` \- `standard_p100` \- `complex_model_m_p100` \- `standard_v100` \- `large_model_v100` \- `complex_model_m_v100` \- `complex_model_l_v100` Finally, if you want to use a TPU for training, specify `cloud_tpu` in this field. Learn more about the `special configuration options for training with TPU   
`accelerator_config` |  `[google.cloud.notebooks_v1.types.ExecutionTemplate.SchedulerAcceleratorConfig](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ExecutionTemplate.SchedulerAcceleratorConfig)`   
Configuration (count and accelerator type) for hardware running notebook execution.   
`labels` |  `MutableMapping[str, str]`   
Labels for execution. If execution is scheduled, a field included will be 'nbs-scheduled'. Otherwise, it is an immediate execution, and an included field will be 'nbs-immediate'. Use fields to efficiently index between various types of executions.   
`input_notebook_file` |  `str`   
Path to the notebook file to execute. Must be in a Google Cloud Storage bucket. Format: `gs://{bucket_name}/{folder}/{notebook_file_name}` Ex: `gs://notebook_user/scheduled_notebooks/sentiment_notebook.ipynb`  
`container_image_uri` |  `str`   
Container Image URI to a DLVM Example: 'gcr.io/deeplearning-platform-release/base-cu100' More examples can be found at: https://cloud.google.com/ai-platform/deep-learning-containers/docs/choosing-container   
`output_notebook_folder` |  `str`   
Path to the notebook folder to write to. Must be in a Google Cloud Storage bucket path. Format: `gs://{bucket_name}/{folder}` Ex: `gs://notebook_user/scheduled_notebooks`  
`params_yaml_file` |  `str`   
Parameters to be overridden in the notebook during execution. Ref https://papermill.readthedocs.io/en/latest/usage-parameterize.html on how to specifying parameters in the input notebook and pass them here in an YAML file. Ex: `gs://notebook_user/scheduled_notebooks/sentiment_notebook_params.yaml`  
`parameters` |  `str`   
Parameters used within the 'input_notebook_file' notebook.   
`service_account` |  `str`   
The email address of a service account to use when running the execution. You must have the `iam.serviceAccounts.actAs` permission for the specified service account.   
`job_type` |  `[google.cloud.notebooks_v1.types.ExecutionTemplate.JobType](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ExecutionTemplate.JobType)`   
The type of Job to be used on this execution.   
`dataproc_parameters` |  `[google.cloud.notebooks_v1.types.ExecutionTemplate.DataprocParameters](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ExecutionTemplate.DataprocParameters)`   
Parameters used in Dataproc JobType executions. This field is a member of `oneof`_ `job_parameters`.   
`vertex_ai_parameters` |  `[google.cloud.notebooks_v1.types.ExecutionTemplate.VertexAIParameters](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ExecutionTemplate.VertexAIParameters)`   
Parameters used in Vertex AI JobType executions. This field is a member of `oneof`_ `job_parameters`.   
`kernel_spec` |  `str`   
Name of the kernel spec to use. This must be specified if the kernel spec name on the execution target does not match the name in the input notebook file.   
`tensorboard` |  `str`   
The name of a Vertex AI [Tensorboard] resource to which this execution will upload Tensorboard logs. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}`  
  
## Classes 

### DataprocParameters
    
    
    DataprocParameters(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Parameters used in Dataproc JobType executions.

### JobType
    
    
    JobType(value)

The backend used for this execution.

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
  
### ScaleTier
    
    
    ScaleTier(value)

Required. Specifies the machine types, the number of replicas for workers and parameter servers.
    
    
        - You *must* set `ExecutionTemplate.masterType` to specify
          the type of machine to use for your master node. This is
          the only required setting.
    

### SchedulerAcceleratorConfig
    
    
    SchedulerAcceleratorConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Definition of a hardware accelerator. Note that not all combinations of `type` and `core_count` are valid. Check `GPUs on Compute Engine <https://cloud.google.com/compute/docs/gpus>`__ to find a valid combination. TPUs are not supported.

### SchedulerAcceleratorType
    
    
    SchedulerAcceleratorType(value)

Hardware accelerator types for AI Platform Training jobs.

### VertexAIParameters
    
    
    VertexAIParameters(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Parameters used in Vertex AI JobType executions.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
