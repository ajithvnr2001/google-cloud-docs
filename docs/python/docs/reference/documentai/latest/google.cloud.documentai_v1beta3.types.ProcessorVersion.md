---
url: https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.ProcessorVersion
title: Class ProcessorVersion (3.16.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:10.936887+00:00
---

# Class ProcessorVersion (3.16.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.ProcessorVersion

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ProcessorVersion (3.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.16.0 (latest)  3.15.0  3.14.0  3.13.0  3.12.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.1  2.35.0  2.34.0  2.33.0  2.32.0  2.30.0  2.29.3  2.28.0  2.27.1  2.26.0  2.25.0  2.24.2  2.23.0  2.22.0  2.21.1  2.20.2  2.19.0  2.18.0  2.17.0  2.16.1  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.1  2.8.0  2.7.0  2.6.0  2.5.0  2.4.1  2.3.0  2.2.0  2.1.0  2.0.3  1.5.1  1.4.2  1.3.0  1.2.1  1.1.0  1.0.0  0.5.2  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    ProcessorVersion(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A processor version is an implementation of a processor. Each processor can have multiple versions, pretrained by Google internally or uptrained by the customer. A processor can only have one default version at a time. Its document-processing behavior is defined by that version.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. The resource name of the processor version. Format: `projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processor_version}`  
`display_name` |  `str`   
The display name of the processor version.   
`document_schema` |  `[google.cloud.documentai_v1beta3.types.DocumentSchema](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.DocumentSchema)`   
Output only. The schema of the processor version. Describes the output.   
`state` |  `[google.cloud.documentai_v1beta3.types.ProcessorVersion.State](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.ProcessorVersion.State)`   
Output only. The state of the processor version.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time the processor version was created.   
`latest_evaluation` |  `[google.cloud.documentai_v1beta3.types.EvaluationReference](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.EvaluationReference)`   
Output only. The most recently invoked evaluation for the processor version.   
`kms_key_name` |  `str`   
Output only. The KMS key name used for encryption.   
`kms_key_version_name` |  `str`   
Output only. The KMS key version with which data is encrypted.   
`google_managed` |  `bool`   
Output only. Denotes that this `ProcessorVersion` is managed by Google.   
`deprecation_info` |  `[google.cloud.documentai_v1beta3.types.ProcessorVersion.DeprecationInfo](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.ProcessorVersion.DeprecationInfo)`   
Output only. If set, information about the eventual deprecation of this version.   
`model_type` |  `[google.cloud.documentai_v1beta3.types.ProcessorVersion.ModelType](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.ProcessorVersion.ModelType)`   
Output only. The model type of this processor version.   
`satisfies_pzs` |  `bool`   
Output only. Reserved for future use.   
`satisfies_pzi` |  `bool`   
Output only. Reserved for future use.   
`gen_ai_model_info` |  `[google.cloud.documentai_v1beta3.types.ProcessorVersion.GenAiModelInfo](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.ProcessorVersion.GenAiModelInfo)`   
Output only. Information about Generative AI model-based processor versions.   
  
## Classes 

### DeprecationInfo
    
    
    DeprecationInfo(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Information about the upcoming deprecation of this processor version.

### GenAiModelInfo
    
    
    GenAiModelInfo(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Information about Generative AI model-based processor versions.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### ModelType
    
    
    ModelType(value)

The possible model types of the processor version.

### State
    
    
    State(value)

The possible states of the processor version.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
