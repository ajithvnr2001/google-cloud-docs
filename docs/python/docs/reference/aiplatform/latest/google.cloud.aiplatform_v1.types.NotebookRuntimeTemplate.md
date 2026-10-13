---
url: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.types.NotebookRuntimeTemplate
title: Class NotebookRuntimeTemplate (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:47:16.467572+00:00
---

# Class NotebookRuntimeTemplate (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.types.NotebookRuntimeTemplate

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class NotebookRuntimeTemplate (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0  1.153.1  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.116.0  1.115.0  1.114.0  1.113.0  1.112.0  1.111.0  1.110.0  1.109.0  1.108.0  1.107.0  1.106.0  1.105.0  1.104.0  1.103.0  1.102.0  1.101.0  1.100.0  1.99.0  1.98.0  1.97.0  1.96.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.1  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.39.0  1.38.1  1.37.0  1.36.4  1.35.0  1.34.0  1.33.1  1.32.0  1.31.1  1.30.1  1.29.0  1.28.1  1.27.1  1.26.1  1.25.0  1.24.1  1.23.0  1.22.1  1.21.0  1.20.0  1.19.1  1.18.3  1.17.1  1.16.1  1.15.1  1.14.0  1.13.1  1.12.1  1.11.0  1.10.0  1.9.0  1.8.1  1.7.1  1.6.2  1.5.0  1.4.3  1.3.0  1.2.0  1.1.1  1.0.1  0.9.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1 
    
    
    NotebookRuntimeTemplate(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A template that specifies runtime configurations such as machine type, runtime version, network configurations, etc. Multiple runtimes can be created from a runtime template.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
The resource name of the NotebookRuntimeTemplate.   
`display_name` |  `str`   
Required. The display name of the NotebookRuntimeTemplate. The name can be up to 128 characters long and can consist of any UTF-8 characters.   
`description` |  `str`   
The description of the NotebookRuntimeTemplate.   
`is_default` |  `bool`   
Output only. Deprecated: This field has no behavior. Use notebook_runtime_type = 'ONE_CLICK' instead. The default template to use if not specified.   
`machine_spec` |  `[google.cloud.aiplatform_v1.types.MachineSpec](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.types.MachineSpec)`   
Optional. Immutable. The specification of a single machine for the template.   
`data_persistent_disk_spec` |  `[google.cloud.aiplatform_v1.types.PersistentDiskSpec](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.types.PersistentDiskSpec)`   
Optional. The specification of [persistent disk][https://cloud.google.com/compute/docs/disks/persistent-disks] attached to the runtime as data disk storage.   
`network_spec` |  `[google.cloud.aiplatform_v1.types.NetworkSpec](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.types.NetworkSpec)`   
Optional. Network spec.   
`service_account` |  `str`   
Deprecated: This field is ignored and the "Vertex AI Notebook Service Account" (service-PROJECT_NUMBER@gcp-sa-aiplatform-vm.iam.gserviceaccount.com) is used for the runtime workload identity. See https://cloud.google.com/iam/docs/service-agents#vertex-ai-notebook-service-account for more details. For NotebookExecutionJob, use NotebookExecutionJob.service_account instead. The service account that the runtime workload runs as. You can use any service account within the same project, but you must have the service account user permission to use the instance. If not specified, the `Compute Engine default service account   
`etag` |  `str`   
Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens.   
`labels` |  `MutableMapping[str, str]`   
The labels with user-defined metadata to organize the NotebookRuntimeTemplates. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels.   
`idle_shutdown_config` |  `[google.cloud.aiplatform_v1.types.NotebookIdleShutdownConfig](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.types.NotebookIdleShutdownConfig)`   
The idle shutdown configuration of NotebookRuntimeTemplate. This config will only be set when idle shutdown is enabled.   
`euc_config` |  `[google.cloud.aiplatform_v1.types.NotebookEucConfig](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.types.NotebookEucConfig)`   
EUC configuration of the NotebookRuntimeTemplate.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Timestamp when this NotebookRuntimeTemplate was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Timestamp when this NotebookRuntimeTemplate was most recently updated.   
`notebook_runtime_type` |  `[google.cloud.aiplatform_v1.types.NotebookRuntimeType](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.types.NotebookRuntimeType)`   
Optional. Immutable. The type of the notebook runtime template.   
`shielded_vm_config` |  `[google.cloud.aiplatform_v1.types.ShieldedVmConfig](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.types.ShieldedVmConfig)`   
Optional. Immutable. Runtime Shielded VM spec.   
`network_tags` |  `MutableSequence[str]`   
Optional. The Compute Engine tags to add to runtime (see `Tagging instances   
`encryption_spec` |  `[google.cloud.aiplatform_v1.types.EncryptionSpec](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.types.EncryptionSpec)`   
Customer-managed encryption key spec for the notebook runtime.   
`software_config` |  `[google.cloud.aiplatform_v1.types.NotebookSoftwareConfig](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.types.NotebookSoftwareConfig)`   
Optional. The notebook software configuration of the notebook runtime.   
  
## Classes 

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
  
## Methods 

### NotebookRuntimeTemplate
    
    
    NotebookRuntimeTemplate(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A template that specifies runtime configurations such as machine type, runtime version, network configurations, etc. Multiple runtimes can be created from a runtime template.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
