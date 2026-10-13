---
url: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.AutoMLImageTrainingJob
title: Class AutoMLImageTrainingJob (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:26:29.411671+00:00
---

# Class AutoMLImageTrainingJob (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.AutoMLImageTrainingJob

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AutoMLImageTrainingJob (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0  1.153.1  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.116.0  1.115.0  1.114.0  1.113.0  1.112.0  1.111.0  1.110.0  1.109.0  1.108.0  1.107.0  1.106.0  1.105.0  1.104.0  1.103.0  1.102.0  1.101.0  1.100.0  1.99.0  1.98.0  1.97.0  1.96.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.1  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.39.0  1.38.1  1.37.0  1.36.4  1.35.0  1.34.0  1.33.1  1.32.0  1.31.1  1.30.1  1.29.0  1.28.1  1.27.1  1.26.1  1.25.0  1.24.1  1.23.0  1.22.1  1.21.0  1.20.0  1.19.1  1.18.3  1.17.1  1.16.1  1.15.1  1.14.0  1.13.1  1.12.1  1.11.0  1.10.0  1.9.0  1.8.1  1.7.1  1.6.2  1.5.0  1.4.3  1.3.0  1.2.0  1.1.1  1.0.1  0.9.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1 
    
    
    AutoMLImageTrainingJob(
        display_name: typing.Optional[str] = None,
        prediction_type: str = "classification",
        multi_label: bool = False,
        model_type: str = "CLOUD",
        base_model: typing.Optional[google.cloud.aiplatform.models.Model] = None,
        incremental_train_base_model: typing.Optional[
            google.cloud.aiplatform.models.Model
        ] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        training_encryption_spec_key_name: typing.Optional[str] = None,
        model_encryption_spec_key_name: typing.Optional[str] = None,
        checkpoint_name: typing.Optional[str] = None,
        trainer_config: typing.Optional[typing.Dict[str, str]] = None,
        metric_spec: typing.Optional[typing.Dict[str, str]] = None,
        parameter_spec: typing.Optional[
            typing.Dict[
                str,
                typing.Union[
                    google.cloud.aiplatform.hyperparameter_tuning.DoubleParameterSpec,
                    google.cloud.aiplatform.hyperparameter_tuning.IntegerParameterSpec,
                    google.cloud.aiplatform.hyperparameter_tuning.CategoricalParameterSpec,
                    google.cloud.aiplatform.hyperparameter_tuning.DiscreteParameterSpec,
                ],
            ]
        ] = None,
        search_algorithm: typing.Optional[str] = None,
        measurement_selection: typing.Optional[str] = None,
    )

Creates an AutoML image training job.

Use the `AutoMLImageTrainingJob` class to create, train, and return an image model. For more information about working with image data models in Vertex AI, see [Image data](https://cloud.google.com/vertex-ai/docs/training-overview#image_data).

For an example of how to use the `AutoMLImageTrainingJob` class, see the tutorial in the [AutoML image classification](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/migration/sdk-automl-text-classification-batch-prediction.ipynb) notebook on GitHub.

## Parameters  
  
---  
**Name** | **Description**  
`display_name` |  `str`   
Optional. The user-defined name of the training pipeline. The name must contain 128 or fewer UTF-8 characters.  
`prediction_type` |  `str`   
The type of prediction the model produces. Valid values are: `classification` to predict one of multiple target values that are selected from each row. `object_detection` to predict a value based on its relation to other values. `object_detection` is available only for columns that contain semantically numeric values. For example, columns might contain numeric values stored as an integer, float, or string.  
`multi_label` |  `bool = False`   
Required. If `false`, a single-label (multi-class) model is trained (i.e. assuming that for each image just up to one annotation may be applicable). If `true`, a multi-label model is trained. If you pass in `true`, it's assumed multiple annotations might apply to each image. Multi-label models are supported only when `prediction_type` is set to `classification`. If `multi_label` is `true` and `prediction_type` is `object_detection`, then then `multi_label` is ignored. The default value is `false`.  
`model_type` |  `str = "CLOUD"`   
Required. The type of model to create. The following are the valid values: `CLOUD` \- The default for image classification. This model type is deigned to work in Google Cloud and can't be exported. `CLOUD_1` \- This model type is deigned to work in Google Cloud and can't be exported. This model type is expected to have higher prediction accuracy than `CLOUD`. `CLOUD_HIGH_ACCURACY_1` \- The default for image object detection. This model type is deigned to work in Google Cloud and can't be exported. It's designed to have a higher latency and a higher prediction quality than other cloud model types. `CLOUD_LOW_LATENCY_1` \- This model type is deigned to work in Google Cloud and can't be exported. It's also designed to have low latency, but might might lower prediction quality than other cloud model types. `MOBILE_TF_LOW_LATENCY_1` \- This model type is deigned to work in Google Cloud and can be exported as a TensorFlow or Core ML model for use on a mobile or edge device. It's also designed to have to have low latency, but might have lower prediction quality than other mobile models types. `MOBILE_TF_VERSATILE_1` \- This model type is deigned to work in Google Cloud and can be exported as a TensorFlow or Core ML model for use on a mobile or edge device. `MOBILE_TF_HIGH_ACCURACY_1` \- This model type is deigned to work in Google Cloud and can be exported as a TensorFlow or Core ML model for use on a mobile or edge device. It's designed to have a higher latency, but should also have a higher prediction quality than other mobile model types. `EFFICIENTNET` \- This model type is available in the Vertex Model Garden image classification training with customizable hyperparameters. It's deigned to work in Google Cloud and can't be exported. `VIT` \- This model type is available in the Vertex Model Garden image classification training with customizable hyperparameters. Best tailored to be used within Google Cloud, and cannot be exported externally. `MAXVIT` \- This model type is available in the Vertex Model Garden image classification training with customizable hyperparameters. It's deigned to work in Google Cloud and can't be exported. `COCA` \- This model type is available in the Vertex Model Garden image classification training with customizable hyperparameters. It's deigned to work in Google Cloud and can't be exported. `SPINENET` \- This model type is available in the Vertex Model Garden image object detection training with customizable hyperparameters. It's deigned to work in Google Cloud and can't be exported. `YOLO` \- This model type is available in the Vertex Model Garden image object detection training with customizable hyperparameters. It's deigned to work in Google Cloud and can't be exported.  
`base_model` |  `typing.Optional[google.cloud.aiplatform.models.Model]`   
Optional[models.Model] = Optional. You can specify a `base_model` for image classification models only. If it is specified, the new model is trained based on the `base_model`. Otherwise, the new model is trained from scratch. The base model must be in the same Google Project and region as the new model to train, and it must have the same `model_type`.  
`incremental_train_base_model` |  `typing.Optional[google.cloud.aiplatform.models.Model]`   
Optional[models.Model] = Optional. You can specify an `incremental_train_base_model` for image classification models and object detection models only. If specified, the new model is incrementally trained using an existing model as the starting point. This can reduce the training time. If not specified, the new model is trained from scratch. The model specified in `incremental_train_base_model` model must be in the same Google Project and region as the new model to train, and it must have the same `prediction_type` and `model_type`.  
`project` |  `str`   
Optional. The Google Cloud region where this where the training runs. This region overrides the region that was set by `aiplatform.init`.  
`location` |  `str`   
Optional. Location to run training in. Overrides location set in aiplatform.init.  
`credentials` |  `auth_credentials.Credentials`   
Optional. The credentials that are used to train the model. These credentials override the credentials set by `aiplatform.init`.  
`labels` |  `Dict[str, str]`   
Optional. Labels with user-defined metadata to organize your training pipelines. The maximum length of a key and value is 64 unicode characters. Labels and keys can contain only lowercase letters, numeric characters, underscores, and dashes. International characters are allowed. For more information and examples of using labels, see [Using labels to organize Google Cloud Platform resources](https://goo.gl/xmQnxf).  
`training_encryption_spec_key_name` |  `Optional[str]`   
Optional. The Cloud KMS resource identifier of the customer managed encryption key used to protect the training pipeline. The key has the following format: `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`. The key needs to be in the same region as where the compute resource is created. If set, the key secures the training pipeline and overrides the key set using `aiplatform.init`. The model trained by this training pipeline is also secured by this key if `model_encryption_spec_key_name` is not set separately.  
`model_encryption_spec_key_name` |  `Optional[str]`   
Optional. The Cloud KMS resource identifier of the customer managed encryption key used to protect the model. The key has the following format: `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`. The key needs to be in the same region as where the compute resource is created. If set, the key secures the trained model and overrides the key set using `aiplatform.init`.  
`checkpoint_name` |  `typing.Optional[str]`   
Optional[str] = Optional. The field is reserved for Model Garden model training and is based on the provided pre-trained model checkpoint. `checkpoint_name` is needed only when `model_type` is set to `EFFICIENTNET`, `VIT`, `COCA`, `SPINENET`, or `YOLO`.  
`trainer_config` |  `typing.Optional[typing.Dict[str, str]]`   
Optional[Dict[str, str]] = None, Optional. A field that's used with the Model Garden model training when passing customized configs for the trainer. The following is an example that uses all `trainer_config` parameters: 
    
    
    py trainer_config = { 'global_batch_size': '8', 'learning_rate': '0.001', 'optimizer_type': 'sgd', 'optimizer_momentum': '0.9', 'train_steps': '10000', 'accelerator_count': '1', 'anchor_size': '8', -- IOD only } 

`trainer_config` is required for only Model Garden models when `model_type` is `EFFICIENTNET`, `VIT`, `COCA`, `SPINENET`, or `YOLO`.  
`metric_spec` |  `typing.Optional[typing.Dict[str, str]]`   
Dict[str, str] Required. A dictionary that represents metrics use for optimization. The dictionary key is the `metric_id` that's reported by your training job and can be 'loss' or 'accuracy'. The dictionary value is the optimization goal of the metric, and can be 'minimize' or 'maximize'. The following is an example of a `metric_spec`: `metric_spec = {'loss': 'minimize', 'accuracy': 'maximize'}`. `metric_spec` is required for only Model Garden models when `model_type` is `EFFICIENTNET`, `VIT`, `COCA`, `SPINENET`, or `YOLO`.  
`parameter_spec` |  `Dict[str, hpt._ParameterSpec]`   
Required. A dictionary representing parameters to use for optimization. The dictionary key is the `metric_id` that's reported by your training job as a command line keyword argument. The dictionary value is the parameter specification of the metric. The following is an example of how to specify a `parameter_spec`: 
    
    
    py from google.cloud.aiplatform import hpt as hpt parameter_spec = { 'learning_rate': hpt.DoubleParameterSpec(min=1e-7, max=1, scale='linear'), } 

Supported parameter specifications can be found in `aiplatform.hyperparameter_tuning`. The following parameter specifications are supported: `Union[DoubleParameterSpec, IntegerParameterSpec, CategoricalParameterSpec, DiscreteParameterSpec]`. `parameter_spec `is required for only Model Garden models when `model_type` is `EFFICIENTNET`, `VIT`, `COCA`, `SPINENET`, or `YOLO`.  
`search_algorithm` |  `str`   
The search algorithm that's specified for the study. The search algorithm can be one of the following: `None` \- If you don't specify an algorithm, your job uses the default Vertex AI algorithm. The default algorithm applies Bayesian optimization to arrive at the optimal solution with a more effective search over the parameter space. 'grid' - A simple grid search within the feasible space. This option is particularly useful if you want to specify a quantity of trials that is greater than the number of points in the feasible space. In these cases, if you don't specify a grid search, the Vertex AI default algorithm might generate duplicate suggestions. To use grid search, all parameter specifications must be `IntegerParameterSpec`, `CategoricalParameterSpec`, or `DiscreteParameterSpec`. 'random' - A simple random search within the feasible space. `search_algorithm` is required for only Model Garden models when `model_type` is `EFFICIENTNE`T`, `VIT`, `COCA`, `SPINENET`, or `YOLO`.  
`measurement_selection` |  `str`   
Indicates which measurement to use when the service selects the final measurement from previously reported intermediate measurements. `measurement_selection` can be `best` or `last`. If you expect your measurements to monotonically improve, then choose `last`. If your system can over-train and you expect the performance to improve and then start to decline, then choose `best`. If your measurements are significantly noisy or not reproducible, then `best` is likely to be over-optimistic, so in this case `last` is the preferred option. `measurement_selection` is required for only Model Garden models when `model_type` is `EFFICIENTNET`, `VIT`, `COCA`, `SPINENET`, or `YOLO`.  
  
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
        dataset: google.cloud.aiplatform.datasets.image_dataset.ImageDataset,
        training_fraction_split: typing.Optional[float] = None,
        validation_fraction_split: typing.Optional[float] = None,
        test_fraction_split: typing.Optional[float] = None,
        training_filter_split: typing.Optional[str] = None,
        validation_filter_split: typing.Optional[str] = None,
        test_filter_split: typing.Optional[str] = None,
        budget_milli_node_hours: typing.Optional[int] = None,
        model_display_name: typing.Optional[str] = None,
        model_labels: typing.Optional[typing.Dict[str, str]] = None,
        model_id: typing.Optional[str] = None,
        parent_model: typing.Optional[str] = None,
        is_default_version: typing.Optional[bool] = True,
        model_version_aliases: typing.Optional[typing.Sequence[str]] = None,
        model_version_description: typing.Optional[str] = None,
        disable_early_stopping: bool = False,
        sync: bool = True,
        create_request_timeout: typing.Optional[float] = None,
    ) -> google.cloud.aiplatform.models.Model

Runs the AutoML Image training job and returns a model.

If training on a Vertex AI dataset, you can use one of the following split configurations: Data fraction splits: Any of `training_fraction_split`, `validation_fraction_split` and `test_fraction_split` may optionally be provided, they must sum to up to 1. If the provided ones sum to less than 1, the remainder is assigned to sets as decided by Vertex AI. If none of the fractions are set, by default roughly 80% of data will be used for training, 10% for validation, and 10% for test.
    
    
    Data filter splits:
    Assigns input data to training, validation, and test sets
    based on the given filters, data pieces not matched by any
    filter are ignored. Currently only supported for Datasets
    containing DataItems.
    If any of the filters in this message are to match nothing, then
    they can be set as '-' (the minus sign).
    If using filter splits, all of `training_filter_split`,
    `validation_filter_split` and
    `test_filter_split` must be provided.
    Supported only for unstructured Datasets.
    

**Parameters**  
---  
**Name** | **Description**  
`dataset` |  `datasets.ImageDataset`   
Required. The dataset within the same Project from which data will be used to train the Model. The Dataset must use schema compatible with Model being trained, and what is compatible should be described in the used TrainingPipeline's [training_task_definition] [google.cloud.aiplatform.v1beta1.TrainingPipeline.training_task_definition]. For tabular Datasets, all their data is exported to training, to pick and choose from.  
`training_fraction_split` |  `float`   
Optional. The fraction of the input data that is to be used to train the Model. This is ignored if Dataset is not provided.  
`validation_fraction_split` |  `float`   
Optional. The fraction of the input data that is to be used to validate the Model. This is ignored if Dataset is not provided.  
`test_fraction_split` |  `float`   
Optional. The fraction of the input data that is to be used to evaluate the Model. This is ignored if Dataset is not provided.  
`training_filter_split` |  `str`   
Optional. A filter on DataItems of the Dataset. DataItems that match this filter are used to train the Model. A filter with same syntax as the one used in DatasetService.ListDataItems may be used. If a single DataItem is matched by more than one of the FilterSplit filters, then it is assigned to the first set that applies to it in the training, validation, test order. This is ignored if Dataset is not provided.  
`validation_filter_split` |  `str`   
Optional. A filter on DataItems of the Dataset. DataItems that match this filter are used to validate the Model. A filter with same syntax as the one used in DatasetService.ListDataItems may be used. If a single DataItem is matched by more than one of the FilterSplit filters, then it is assigned to the first set that applies to it in the training, validation, test order. This is ignored if Dataset is not provided.  
`test_filter_split` |  `str`   
Optional. A filter on DataItems of the Dataset. DataItems that match this filter are used to test the Model. A filter with same syntax as the one used in DatasetService.ListDataItems may be used. If a single DataItem is matched by more than one of the FilterSplit filters, then it is assigned to the first set that applies to it in the training, validation, test order. This is ignored if Dataset is not provided.  
`budget_milli_node_hours` |  `int`   
Optional. The train budget of creating this Model, expressed in milli node hours i.e. 1,000 value in this field means 1 node hour. Defaults by `prediction_type`: `classification` \- For Cloud models the budget must be: 8,000 - 800,000 milli node hours (inclusive). The default value is 192,000 which represents one day in wall time, assuming 8 nodes are used. `object_detection` \- For Cloud models the budget must be: 20,000 - 900,000 milli node hours (inclusive). The default value is 216,000 which represents one day in wall time, assuming 9 nodes are used. The training cost of the model will not exceed this budget. The final cost will be attempted to be close to the budget, though may end up being (even) noticeably smaller - at the backend's discretion. This especially may happen when further model training ceases to provide any improvements. If the budget is set to a value known to be insufficient to train a Model for the given training set, the training won't be attempted and will error.  
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
