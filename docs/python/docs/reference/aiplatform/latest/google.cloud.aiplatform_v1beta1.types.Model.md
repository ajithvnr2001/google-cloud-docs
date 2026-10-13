---
url: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1beta1.types.Model
title: Class Model (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:50:43.746269+00:00
---

# Class Model (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1beta1.types.Model

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Model (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0  1.153.1  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.116.0  1.115.0  1.114.0  1.113.0  1.112.0  1.111.0  1.110.0  1.109.0  1.108.0  1.107.0  1.106.0  1.105.0  1.104.0  1.103.0  1.102.0  1.101.0  1.100.0  1.99.0  1.98.0  1.97.0  1.96.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.1  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.39.0  1.38.1  1.37.0  1.36.4  1.35.0  1.34.0  1.33.1  1.32.0  1.31.1  1.30.1  1.29.0  1.28.1  1.27.1  1.26.1  1.25.0  1.24.1  1.23.0  1.22.1  1.21.0  1.20.0  1.19.1  1.18.3  1.17.1  1.16.1  1.15.1  1.14.0  1.13.1  1.12.1  1.11.0  1.10.0  1.9.0  1.8.1  1.7.1  1.6.2  1.5.0  1.4.3  1.3.0  1.2.0  1.1.1  1.0.1  0.9.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1 
    
    
    Model(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A trained machine learning Model.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
The resource name of the Model.   
`version_id` |  `str`   
Output only. Immutable. The version ID of the model. A new version is committed when a new model version is uploaded or trained under an existing model id. It is an auto-incrementing decimal number in string representation.   
`version_aliases` |  `MutableSequence[str]`   
User provided version aliases so that a model version can be referenced via alias (i.e. `projects/{project}/locations/{location}/models/{model_id}@{version_alias}` instead of auto-generated version id (i.e. `projects/{project}/locations/{location}/models/{model_id}@{version_id})`. The format is `a-z][a-zA-Z0-9-]`{0,126}[a-z0-9] to distinguish from version_id. A default version alias will be created for the first version of the model, and there must be exactly one default version alias for a model.   
`version_create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Timestamp when this version was created.   
`version_update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Timestamp when this version was most recently updated.   
`display_name` |  `str`   
Required. The display name of the Model. The name can be up to 128 characters long and can consist of any UTF-8 characters.   
`description` |  `str`   
The description of the Model.   
`version_description` |  `str`   
The description of this version.   
`default_checkpoint_id` |  `str`   
The default checkpoint id of a model version.   
`predict_schemata` |  `[google.cloud.aiplatform_v1beta1.types.PredictSchemata](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1beta1.types.PredictSchemata)`   
The schemata that describe formats of the Model's predictions and explanations as given and returned via PredictionService.Predict and PredictionService.Explain.   
`metadata_schema_uri` |  `str`   
Immutable. Points to a YAML file stored on Google Cloud Storage describing additional information about the Model, that is specific to it. Unset if the Model does not have any additional information. The schema is defined as an OpenAPI 3.0.2 `Schema Object   
`metadata` |  `google.protobuf.struct_pb2.Value`   
Immutable. An additional information about the Model; the schema of the metadata can be found in metadata_schema. Unset if the Model does not have any additional information.   
`supported_export_formats` |  `MutableSequence[[google.cloud.aiplatform_v1beta1.types.Model.ExportFormat](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1beta1.types.Model.ExportFormat)]`   
Output only. The formats in which this Model may be exported. If empty, this Model is not available for export.   
`training_pipeline` |  `str`   
Output only. The resource name of the TrainingPipeline that uploaded this Model, if any.   
`container_spec` |  `[google.cloud.aiplatform_v1beta1.types.ModelContainerSpec](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1beta1.types.ModelContainerSpec)`   
Input only. The specification of the container that is to be used when deploying this Model. The specification is ingested upon ModelService.UploadModel, and all binaries it contains are copied and stored internally by Vertex AI. Not required for AutoML Models.   
`artifact_uri` |  `str`   
Immutable. The path to the directory containing the Model artifact and any of its supporting files. Not required for AutoML Models.   
`supported_deployment_resources_types` |  `MutableSequence[[google.cloud.aiplatform_v1beta1.types.Model.DeploymentResourcesType](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1beta1.types.Model.DeploymentResourcesType)]`   
Output only. When this Model is deployed, its prediction resources are described by the `prediction_resources` field of the Endpoint.deployed_models object. Because not all Models support all resource configuration types, the configuration types this Model supports are listed here. If no configuration types are listed, the Model cannot be deployed to an Endpoint and does not support online predictions (PredictionService.Predict or PredictionService.Explain). Such a Model can serve predictions by using a BatchPredictionJob, if it has at least one entry each in supported_input_storage_formats and supported_output_storage_formats.   
`supported_input_storage_formats` |  `MutableSequence[str]`   
Output only. The formats this Model supports in BatchPredictionJob.input_config. If PredictSchemata.instance_schema_uri exists, the instances should be given as per that schema. The possible formats are: \- `jsonl` The JSON Lines format, where each instance is a single line. Uses GcsSource. \- `csv` The CSV format, where each instance is a single comma-separated line. The first line in the file is the header, containing comma-separated field names. Uses GcsSource. \- `tf-record` The TFRecord format, where each instance is a single record in tfrecord syntax. Uses GcsSource. \- `tf-record-gzip` Similar to `tf-record`, but the file is gzipped. Uses GcsSource. \- `bigquery` Each instance is a single row in BigQuery. Uses BigQuerySource. \- `file-list` Each line of the file is the location of an instance to process, uses `gcs_source` field of the InputConfig object. If this Model doesn't support any of these formats it means it cannot be used with a BatchPredictionJob. However, if it has supported_deployment_resources_types, it could serve online predictions by using PredictionService.Predict or PredictionService.Explain.   
`supported_output_storage_formats` |  `MutableSequence[str]`   
Output only. The formats this Model supports in BatchPredictionJob.output_config. If both PredictSchemata.instance_schema_uri and PredictSchemata.prediction_schema_uri exist, the predictions are returned together with their instances. In other words, the prediction has the original instance data first, followed by the actual prediction content (as per the schema). The possible formats are: \- `jsonl` The JSON Lines format, where each prediction is a single line. Uses GcsDestination. \- `csv` The CSV format, where each prediction is a single comma-separated line. The first line in the file is the header, containing comma-separated field names. Uses GcsDestination. \- `bigquery` Each prediction is a single row in a BigQuery table, uses BigQueryDestination . If this Model doesn't support any of these formats it means it cannot be used with a BatchPredictionJob. However, if it has supported_deployment_resources_types, it could serve online predictions by using PredictionService.Predict or PredictionService.Explain.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Timestamp when this Model was uploaded into Vertex AI.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Timestamp when this Model was most recently updated.   
`deployed_models` |  `MutableSequence[[google.cloud.aiplatform_v1beta1.types.DeployedModelRef](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1beta1.types.DeployedModelRef)]`   
Output only. The pointers to DeployedModels created from this Model. Note that Model could have been deployed to Endpoints in different Locations.   
`explanation_spec` |  `[google.cloud.aiplatform_v1beta1.types.ExplanationSpec](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1beta1.types.ExplanationSpec)`   
The default explanation specification for this Model. The Model can be used for [requesting explanation][google.cloud.aiplatform.v1beta1.PredictionService.Explain] after being deployed if it is populated. The Model can be used for [batch explanation][google.cloud.aiplatform.v1beta1.BatchPredictionJob.generate_explanation] if it is populated. All fields of the explanation_spec can be overridden by explanation_spec of DeployModelRequest.deployed_model, or explanation_spec of BatchPredictionJob. If the default explanation specification is not set for this Model, this Model can still be used for [requesting explanation][google.cloud.aiplatform.v1beta1.PredictionService.Explain] by setting explanation_spec of DeployModelRequest.deployed_model and for [batch explanation][google.cloud.aiplatform.v1beta1.BatchPredictionJob.generate_explanation] by setting explanation_spec of BatchPredictionJob.   
`etag` |  `str`   
Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens.   
`labels` |  `MutableMapping[str, str]`   
The labels with user-defined metadata to organize your Models. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels.   
`encryption_spec` |  `[google.cloud.aiplatform_v1beta1.types.EncryptionSpec](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1beta1.types.EncryptionSpec)`   
Customer-managed encryption key spec for a Model. If set, this Model and all sub-resources of this Model will be secured by this key.   
`model_source_info` |  `[google.cloud.aiplatform_v1beta1.types.ModelSourceInfo](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1beta1.types.ModelSourceInfo)`   
Output only. Source of a model. It can either be automl training pipeline, custom training pipeline, BigQuery ML, or saved and tuned from Genie or Model Garden.   
`original_model_info` |  `[google.cloud.aiplatform_v1beta1.types.Model.OriginalModelInfo](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1beta1.types.Model.OriginalModelInfo)`   
Output only. If this Model is a copy of another Model, this contains info about the original.   
`metadata_artifact` |  `str`   
Output only. The resource name of the Artifact that was created in MetadataStore when creating the Model. The Artifact resource name pattern is `projects/{project}/locations/{location}/metadataStores/{metadata_store}/artifacts/{artifact}`.   
`base_model_source` |  `[google.cloud.aiplatform_v1beta1.types.Model.BaseModelSource](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1beta1.types.Model.BaseModelSource)`   
Optional. User input field to specify the base model source. Currently it only supports specifing the Model Garden models and Genie models.   
`satisfies_pzs` |  `bool`   
Output only. Reserved for future use.   
`satisfies_pzi` |  `bool`   
Output only. Reserved for future use.   
`checkpoints` |  `MutableSequence[[google.cloud.aiplatform_v1beta1.types.Checkpoint](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1beta1.types.Checkpoint)]`   
Optional. Output only. The checkpoints of the model.   
  
## Classes 

### BaseModelSource
    
    
    BaseModelSource(mapping=None, *, ignore_unknown_fields=False, **kwargs)

User input field to specify the base model source. Currently it only supports specifing the Model Garden models and Genie models.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### DeploymentResourcesType
    
    
    DeploymentResourcesType(value)

Identifies a type of Model's prediction resources.

### ExportFormat
    
    
    ExportFormat(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Represents export format supported by the Model. All formats export to Google Cloud Storage.

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
  
### OriginalModelInfo
    
    
    OriginalModelInfo(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Contains information about the original Model if this Model is a copy.

## Methods 

### Model
    
    
    Model(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A trained machine learning Model.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
