---
url: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ModelExportOutputConfig
title: Class ModelExportOutputConfig (2.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:57:30.397877+00:00
---

# Class ModelExportOutputConfig (2.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ModelExportOutputConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ModelExportOutputConfig (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.1  2.19.0  2.18.1  2.17.0  2.16.4  2.15.0  2.14.1  2.13.5  2.12.0  2.11.4  2.10.1  2.9.0  2.8.3  2.7.3  2.6.0  2.5.2  2.4.2  2.3.0  2.2.0  2.1.0  2.0.0  1.0.3  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.0 
    
    
    ModelExportOutputConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Output configuration for ModelExport Action.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`gcs_destination` |  `[google.cloud.automl_v1.types.GcsDestination](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.GcsDestination)`   
Required. The Google Cloud Storage location where the model is to be written to. This location may only be set for the following model formats: "tflite", "edgetpu_tflite", "tf_saved_model", "tf_js", "core_ml". Under the directory given as the destination a new one with name "model-export--", where timestamp is in YYYY-MM-DDThh:mm:ss.sssZ ISO-8601 format, will be created. Inside the model and any of its supporting files will be written. This field is a member of `oneof`_ `destination`.   
`model_format` |  `str`   
The format in which the model must be exported. The available, and default, formats depend on the problem and model type (if given problem and type combination doesn't have a format listed, it means its models are not exportable): \- For Image Classification mobile-low-latency-1, mobile-versatile-1, mobile-high-accuracy-1: "tflite" (default), "edgetpu_tflite", "tf_saved_model", "tf_js", "docker". \- For Image Classification mobile-core-ml-low-latency-1, mobile-core-ml-versatile-1, mobile-core-ml-high-accuracy-1: "core_ml" (default). \- For Image Object Detection mobile-low-latency-1, mobile-versatile-1, mobile-high-accuracy-1: "tflite", "tf_saved_model", "tf_js". Formats description: \- tflite - Used for Android mobile devices. \- edgetpu_tflite - Used for `Edge TPU   
`params` |  `MutableMapping[str, str]`   
Additional model-type and format specific parameters describing the requirements for the to be exported model files, any string must be up to 25000 characters long. \- For `docker` format: `cpu_architecture` \- (string) "x86_64" (default). `gpu_architecture` \- (string) "none" (default), "nvidia".   
  
## Classes 

### ParamsEntry
    
    
    ParamsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
