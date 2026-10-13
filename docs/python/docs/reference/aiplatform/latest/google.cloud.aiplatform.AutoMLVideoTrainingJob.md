---
url: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.AutoMLVideoTrainingJob
title: Class AutoMLVideoTrainingJob (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:26:30.225491+00:00
---

# Class AutoMLVideoTrainingJob (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.AutoMLVideoTrainingJob

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AutoMLVideoTrainingJob (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0  1.153.1  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.116.0  1.115.0  1.114.0  1.113.0  1.112.0  1.111.0  1.110.0  1.109.0  1.108.0  1.107.0  1.106.0  1.105.0  1.104.0  1.103.0  1.102.0  1.101.0  1.100.0  1.99.0  1.98.0  1.97.0  1.96.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.1  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.39.0  1.38.1  1.37.0  1.36.4  1.35.0  1.34.0  1.33.1  1.32.0  1.31.1  1.30.1  1.29.0  1.28.1  1.27.1  1.26.1  1.25.0  1.24.1  1.23.0  1.22.1  1.21.0  1.20.0  1.19.1  1.18.3  1.17.1  1.16.1  1.15.1  1.14.0  1.13.1  1.12.1  1.11.0  1.10.0  1.9.0  1.8.1  1.7.1  1.6.2  1.5.0  1.4.3  1.3.0  1.2.0  1.1.1  1.0.1  0.9.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1 
    
    
    AutoMLVideoTrainingJob(
        display_name: typing.Optional[str] = None,
        prediction_type: str = "classification",
        model_type: str = "CLOUD",
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        training_encryption_spec_key_name: typing.Optional[str] = None,
        model_encryption_spec_key_name: typing.Optional[str] = None,
    )

Constructs a AutoML Video Training Job.

## Parameters  
  
---  
**Name** | **Description**  
`display_name` |  `str`   
Required. The user-defined name of this TrainingPipeline.  
`prediction_type` |  `str`   
The type of prediction the Model is to produce, one of: "classification" - A video classification model classifies shots and segments in your videos according to your own defined labels. "object_tracking" - A video object tracking model detects and tracks multiple objects in shots and segments. You can use these models to track objects in your videos according to your own pre-defined, custom labels. "action_recognition" - A video action recognition model pinpoints the location of actions with short temporal durations (`1` second).  
`model_type` |  `str`   
str = "CLOUD" Required. One of the following: "CLOUD" - available for "classification", "object_tracking" and "action_recognition" A Model best tailored to be used within Google Cloud, and which cannot be exported. "MOBILE_VERSATILE_1" - available for "classification", "object_tracking" and "action_recognition" A model that, in addition to being available within Google Cloud, can also be exported (see ModelService.ExportModel) as a TensorFlow or TensorFlow Lite model and used on a mobile or edge device with afterwards. "MOBILE_CORAL_VERSATILE_1" - available only for "object_tracking" A versatile model that is meant to be exported (see ModelService.ExportModel) and used on a Google Coral device. "MOBILE_CORAL_LOW_LATENCY_1" - available only for "object_tracking" A model that trades off quality for low latency, to be exported (see ModelService.ExportModel) and used on a Google Coral device. "MOBILE_JETSON_VERSATILE_1" - available only for "object_tracking" A versatile model that is meant to be exported (see ModelService.ExportModel) and used on an NVIDIA Jetson device. "MOBILE_JETSON_LOW_LATENCY_1" - available only for "object_tracking" A model that trades off quality for low latency, to be exported (see ModelService.ExportModel) and used on an NVIDIA Jetson device.  
`project` |  `str`   
Optional. Project to run training in. Overrides project set in aiplatform.init.  
`location` |  `str`   
Optional. Location to run training in. Overrides location set in aiplatform.init.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to run call training service. Overrides credentials set in aiplatform.init.  
`labels` |  `Dict[str, str]`   
Optional. The labels with user-defined metadata to organize TrainingPipelines. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See <https://goo.gl/xmQnxf> for more information and examples of labels.  
`training_encryption_spec_key_name` |  `Optional[str]`   
Optional. The Cloud KMS resource identifier of the customer managed encryption key used to protect the training pipeline. Has the form: `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`. The key needs to be in the same region as where the compute resource is created. If set, this TrainingPipeline will be secured by this key. Note: Model trained by this TrainingPipeline is also secured by this key if `model_to_upload` is not set separately. Overrides encryption_spec_key_name set in aiplatform.init.  
`model_encryption_spec_key_name` |  `Optional[str]`   
Optional. The Cloud KMS resource identifier of the customer managed encryption key used to protect the model. Has the form: `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`. The key needs to be in the same region as where the compute resource is created. If set, the trained Model will be secured by this key. Overrides encryption_spec_key_name set in aiplatform.init.  
  
## Properties 

### create_time

Time this resource was created.

### display_name

Display name of this resource.

### encryption_spec

Customer-managed encryption key options for this Vertex AI resource.

If this is set, then all resources created by this Vertex AI resource will be encrypted with the provided encryption key.

### end_time

Optional. The time when the training job entered the `PIPELINE_STATE_SUCCEEDED`, `PIPELINE_STATE_FAILED`, or `PIPELINE_STATE_CANCELLED` state.

### error

Optional. Detailed error information for this training job resource. Error information is created only when the state of the training job is `PIPELINE_STATE_FAILED` or `PIPELINE_STATE_CANCELLED`.

### gca_resource

The underlying resource proto representation.

### has_failed

Returns `true` if the training job failed, otherwise `false`.

### labels

User-defined labels containing metadata about this resource.

Read more about labels at <https://goo.gl/xmQnxf>

### name

Name of this resource.

### resource_name

Full qualified resource name.

### start_time

Optional. The time when the training job first entered the `PIPELINE_STATE_RUNNING` state.

### state

Current training state.

### update_time

Time this resource was last updated.

## Methods 

### cancel
    
    
    cancel() -> None

Asynchronously attempts to cancel a training job.

The server makes a best effort to cancel the job, but the training job can't always be cancelled. If the training job is canceled, its state transitions to `CANCELLED` and it's not deleted.

**Exceptions**  
---  
**Type** | **Description**  
`RuntimeError` | If this training job isn't running, then a runtime error is raised.  
  
### delete
    
    
    delete(sync: bool = True) -> None

Deletes this Vertex AI resource. WARNING: This deletion is permanent.

### done
    
    
    done() -> bool

Method indicating whether a job has completed.

### get
    
    
    get(
        resource_name: str,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    ) -> google.cloud.aiplatform.training_jobs._TrainingJob

Gets a training job using the `resource_name` that's passed in.

**Parameters**  
---  
**Name** | **Description**  
`resource_name` |  `str`   
Required. A fully-qualified resource name or ID.  
`project` |  `str`   
Optional. The name of the Google Cloud project to retrieve the training job from. This overrides the project that was set by `aiplatform.init`.  
`location` |  `str`   
Optional. The Google Cloud region from where the training job is retrieved. This region overrides the region that was set by `aiplatform.init`.  
`credentials` |  `auth_credentials.Credentials`   
Optional. The credentials that are used to upload this model. These credentials override the credentials set by `aiplatform.init`.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | A `ValueError` is raised if the task definition of the retrieved training job doesn't match the custom training task definition.  
  
### get_model
    
    
    get_model(sync=True) -> google.cloud.aiplatform.models.Model

Returns the Vertex AI model produced by this training job.

**Parameter**  
---  
**Name** | **Description**  
`sync` |  `bool`   
If set to `true`, this method runs synchronously. If `false`, this method runs asynchronously.  
**Exceptions**  
---  
**Type** | **Description**  
`RuntimeError` | A runtime error is raised if the training job failed or if a model wasn't produced by the training job.  
  
### list
    
    
    list(
        filter: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    ) -> typing.List[google.cloud.aiplatform.base.VertexAiResourceNoun]

Lists all instances of this training job resource.

The following shows an example of how to call `CustomTrainingJob.list`:
    
    
    aiplatform.CustomTrainingJob.list(
        filter='display_name="experiment_a27"',
        order_by='create_time desc'
    )
    

**Parameters**  
---  
**Name** | **Description**  
`filter` |  `str`   
Optional. An expression for filtering the results of the request. For field names, snake_case and camelCase are supported.  
`order_by` |  `str`   
Optional. A comma-separated list of fields used to sort the returned traing job resources. The defauilt sorting order is ascending. To sort by a field name in descending order, use `desc` after the field name. The following fields are supported: `display_name`, `create_time`, `update_time`.  
`project` |  `str`   
Optional. The name of the Google Cloud project to which to retrieve the list of training job resources. This overrides the project that was set by `aiplatform.init`.  
`location` |  `str`   
Optional. The Google Cloud region from where the training job resources are retrieved. This region overrides the region that was set by `aiplatform.init`.  
`credentials` |  `auth_credentials.Credentials`   
Optional. The credentials that are used to retrieve list. These credentials override the credentials set by `aiplatform.init`.  
**Returns**  
---  
**Type** | **Description**  
`List[VertexAiResourceNoun]` | A list of training job resources.  
  
### run
    
    
    run(
        dataset: google.cloud.aiplatform.datasets.video_dataset.VideoDataset,
        training_fraction_split: typing.Optional[float] = None,
        test_fraction_split: typing.Optional[float] = None,
        training_filter_split: typing.Optional[str] = None,
        test_filter_split: typing.Optional[str] = None,
        model_display_name: typing.Optional[str] = None,
        model_labels: typing.Optional[typing.Dict[str, str]] = None,
        model_id: typing.Optional[str] = None,
        parent_model: typing.Optional[str] = None,
        is_default_version: typing.Optional[bool] = True,
        model_version_aliases: typing.Optional[typing.Sequence[str]] = None,
        model_version_description: typing.Optional[str] = None,
        sync: bool = True,
        create_request_timeout: typing.Optional[float] = None,
    ) -> google.cloud.aiplatform.models.Model

Runs the AutoML Video training job and returns a model.

If training on a Vertex AI dataset, you can use one of the following split configurations: Data fraction splits: `training_fraction_split`, and `test_fraction_split` may optionally be provided, they must sum to up to 1. If none of the fractions are set, by default roughly 80% of data will be used for training, and 20% for test.
    
    
    Data filter splits:
    Assigns input data to training, validation, and test sets
    based on the given filters, data pieces not matched by any
    filter are ignored. Currently only supported for Datasets
    containing DataItems.
    If any of the filters in this message are to match nothing, then
    they can be set as '-' (the minus sign).
    If using filter splits, all of `training_filter_split`, `validation_filter_split` and
    `test_filter_split` must be provided.
    Supported only for unstructured Datasets.
    

**Parameters**  
---  
**Name** | **Description**  
`dataset` |  `datasets.VideoDataset`   
Required. The dataset within the same Project from which data will be used to train the Model. The Dataset must use schema compatible with Model being trained, and what is compatible should be described in the used TrainingPipeline's [training_task_definition] [google.cloud.aiplatform.v1beta1.TrainingPipeline.training_task_definition]. For tabular Datasets, all their data is exported to training, to pick and choose from.  
`training_fraction_split` |  `float`   
Optional. The fraction of the input data that is to be used to train the Model. This is ignored if Dataset is not provided.  
`test_fraction_split` |  `float`   
Optional. The fraction of the input data that is to be used to evaluate the Model. This is ignored if Dataset is not provided.  
`training_filter_split` |  `str`   
Optional. A filter on DataItems of the Dataset. DataItems that match this filter are used to train the Model. A filter with same syntax as the one used in DatasetService.ListDataItems may be used. If a single DataItem is matched by more than one of the FilterSplit filters, then it is assigned to the first set that applies to it in the training, validation, test order. This is ignored if Dataset is not provided.  
`test_filter_split` |  `str`   
Optional. A filter on DataItems of the Dataset. DataItems that match this filter are used to test the Model. A filter with same syntax as the one used in DatasetService.ListDataItems may be used. If a single DataItem is matched by more than one of the FilterSplit filters, then it is assigned to the first set that applies to it in the training, validation, test order. This is ignored if Dataset is not provided.  
`model_display_name` |  `str`   
Optional. The display name of the managed Vertex AI Model. The name can be up to 128 characters long and can be consist of any UTF-8 characters. If not provided upon creation, the job's display_name is used.  
`model_labels` |  `Dict[str, str]`   
Optional. The labels with user-defined metadata to organize your Models. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See <https://goo.gl/xmQnxf> for more information and examples of labels.  
`model_id` |  `str`   
Optional. The ID to use for the Model produced by this job, which will become the final component of the model resource name. This value may be up to 63 characters, and valid characters are `[a-z0-9_-]`. The first character cannot be a number or hyphen.  
`parent_model` |  `str`   
Optional. The resource name or model ID of an existing model. The new model uploaded by this job will be a version of `parent_model`. Only set this field when training a new version of an existing model.  
`is_default_version` |  `bool`   
Optional. When set to True, the newly uploaded model version will automatically have alias "default" included. Subsequent uses of the model produced by this job without a version specified will use this "default" version. When set to False, the "default" alias will not be moved. Actions targeting the model version produced by this job will need to specifically reference this version by ID or alias. New model uploads, i.e. version 1, will always be "default" aliased.  
`model_version_aliases` |  `Sequence[str]`   
Optional. User provided version aliases so that the model version uploaded by this job can be referenced via alias instead of auto-generated version ID. A default version alias will be created for the first version of the model. The format is `a-z][a-zA-Z0-9-]`{0,126}[a-z0-9]  
`model_version_description` |  `str`   
Optional. The description of the model version being uploaded by this job.  
`create_request_timeout` |  `float`   
Optional. The timeout for the create request in seconds.  
**Exceptions**  
---  
**Type** | **Description**  
`RuntimeError` | If Training job has already been run or is waiting to run.  
**Returns**  
---  
**Type** | **Description**  
`model` | The trained Vertex AI Model resource or None if training did not produce a Vertex AI Model.  
  
### to_dict
    
    
    to_dict() -> typing.Dict[str, typing.Any]

Returns the resource proto as a dictionary.

### wait
    
    
    wait()

Helper method that blocks until all futures are complete.

### wait_for_resource_creation
    
    
    wait_for_resource_creation() -> None

Waits until the resource has been created.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
