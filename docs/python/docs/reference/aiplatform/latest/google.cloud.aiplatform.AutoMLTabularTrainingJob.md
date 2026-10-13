---
url: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.AutoMLTabularTrainingJob
title: Class AutoMLTabularTrainingJob (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:26:28.643620+00:00
---

# Class AutoMLTabularTrainingJob (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.AutoMLTabularTrainingJob

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AutoMLTabularTrainingJob (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0  1.153.1  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.116.0  1.115.0  1.114.0  1.113.0  1.112.0  1.111.0  1.110.0  1.109.0  1.108.0  1.107.0  1.106.0  1.105.0  1.104.0  1.103.0  1.102.0  1.101.0  1.100.0  1.99.0  1.98.0  1.97.0  1.96.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.1  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.39.0  1.38.1  1.37.0  1.36.4  1.35.0  1.34.0  1.33.1  1.32.0  1.31.1  1.30.1  1.29.0  1.28.1  1.27.1  1.26.1  1.25.0  1.24.1  1.23.0  1.22.1  1.21.0  1.20.0  1.19.1  1.18.3  1.17.1  1.16.1  1.15.1  1.14.0  1.13.1  1.12.1  1.11.0  1.10.0  1.9.0  1.8.1  1.7.1  1.6.2  1.5.0  1.4.3  1.3.0  1.2.0  1.1.1  1.0.1  0.9.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1 
    
    
    AutoMLTabularTrainingJob(
        display_name: str,
        optimization_prediction_type: str,
        optimization_objective: typing.Optional[str] = None,
        column_specs: typing.Optional[typing.Dict[str, str]] = None,
        column_transformations: typing.Optional[
            typing.List[typing.Dict[str, typing.Dict[str, str]]]
        ] = None,
        optimization_objective_recall_value: typing.Optional[float] = None,
        optimization_objective_precision_value: typing.Optional[float] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        training_encryption_spec_key_name: typing.Optional[str] = None,
        model_encryption_spec_key_name: typing.Optional[str] = None,
    )

Constructs a AutoML Tabular Training Job.

Example usage:

job = training_jobs.AutoMLTabularTrainingJob( display_name="my_display_name", optimization_prediction_type="classification", optimization_objective="minimize-log-loss", column_specs={"column_1": "auto", "column_2": "numeric"}, labels={'key': 'value'}, )

## Parameters  
  
---  
**Name** | **Description**  
`display_name` |  `str`   
Required. The user-defined name of this TrainingPipeline.  
`optimization_prediction_type` |  `str`   
The type of prediction the Model is to produce. "classification" - Predict one out of multiple target values is picked for each row. "regression" - Predict a value based on its relation to other values. This type is available only to columns that contain semantically numeric values, i.e. integers or floating point number, even if stored as e.g. strings.  
`optimization_objective` |  `str`   
Optional. Objective function the Model is to be optimized towards. The training task creates a Model that maximizes/minimizes the value of the objective function over the validation set. The supported optimization objectives depend on the prediction type, and in the case of classification also the number of distinct values in the target column (two distint values -> binary, 3 or more distinct values -> multi class). If the field is not set, the default objective function is used. Classification (binary): "maximize-au-roc" (default) - Maximize the area under the receiver operating characteristic (ROC) curve. "minimize-log-loss" - Minimize log loss. "maximize-au-prc" - Maximize the area under the precision-recall curve. "maximize-precision-at-recall" - Maximize precision for a specified recall value. "maximize-recall-at-precision" - Maximize recall for a specified precision value. Classification (multi class): "minimize-log-loss" (default) - Minimize log loss. Regression: "minimize-rmse" (default) - Minimize root-mean-squared error (RMSE). "minimize-mae" - Minimize mean-absolute error (MAE). "minimize-rmsle" - Minimize root-mean-squared log error (RMSLE).  
`column_specs` |  `Dict[str, str]`   
Optional. Alternative to column_transformations where the keys of the dict are column names and their respective values are one of AutoMLTabularTrainingJob.column_data_types. When creating transformation for BigQuery Struct column, the column should be flattened using "." as the delimiter. Only columns with no child should have a transformation. If an input column has no transformations on it, such a column is ignored by the training, except for the targetColumn, which should have no transformations defined on. Only one of column_transformations or column_specs should be passed. If none of column_transformations or column_specs is passed, the local credentials being used will try setting column_specs to "auto". To do this, the local credentials require read access to the GCS or BigQuery training data source.  
`column_transformations` |  `List[Dict[str, Dict[str, str]]]`   
Optional. Transformations to apply to the input columns (i.e. columns other than the targetColumn). Each transformation may produce multiple result values from the column's value, and all are used for training. When creating transformation for BigQuery Struct column, the column should be flattened using "." as the delimiter. Only columns with no child should have a transformation. If an input column has no transformations on it, such a column is ignored by the training, except for the targetColumn, which should have no transformations defined on. Only one of column_transformations or column_specs should be passed. Consider using column_specs as column_transformations will be deprecated eventually. If none of column_transformations or column_specs is passed, the local credentials being used will try setting column_transformations to "auto". To do this, the local credentials require read access to the GCS or BigQuery training data source.  
`optimization_objective_recall_value` |  `float`   
Optional. Required when maximize-precision-at-recall optimizationObjective was picked, represents the recall value at which the optimization is done. The minimum value is 0 and the maximum is 1.0.  
`optimization_objective_precision_value` |  `float`   
Optional. Required when maximize-recall-at-precision optimizationObjective was picked, represents the precision value at which the optimization is done. The minimum value is 0 and the maximum is 1.0.  
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
  
### get_auto_column_specs
    
    
    get_auto_column_specs(
        dataset: google.cloud.aiplatform.datasets.tabular_dataset.TabularDataset,
        target_column: str,
    ) -> typing.Dict[str, str]

Returns a dict with all non-target columns as keys and 'auto' as values.

Example usage:

column_specs = training_jobs.AutoMLTabularTrainingJob.get_auto_column_specs( dataset=my_dataset, target_column="my_target_column", )

**Parameters**  
---  
**Name** | **Description**  
`dataset` |  `datasets.TabularDataset`   
Required. Intended dataset.  
`target_column` |  `str`   
Required. Intended target column.  
  
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
        dataset: google.cloud.aiplatform.datasets.tabular_dataset.TabularDataset,
        target_column: str,
        training_fraction_split: typing.Optional[float] = None,
        validation_fraction_split: typing.Optional[float] = None,
        test_fraction_split: typing.Optional[float] = None,
        predefined_split_column_name: typing.Optional[str] = None,
        timestamp_split_column_name: typing.Optional[str] = None,
        weight_column: typing.Optional[str] = None,
        budget_milli_node_hours: int = 1000,
        model_display_name: typing.Optional[str] = None,
        model_labels: typing.Optional[typing.Dict[str, str]] = None,
        model_id: typing.Optional[str] = None,
        parent_model: typing.Optional[str] = None,
        is_default_version: typing.Optional[bool] = True,
        model_version_aliases: typing.Optional[typing.Sequence[str]] = None,
        model_version_description: typing.Optional[str] = None,
        disable_early_stopping: bool = False,
        export_evaluated_data_items: bool = False,
        export_evaluated_data_items_bigquery_destination_uri: typing.Optional[str] = None,
        export_evaluated_data_items_override_destination: bool = False,
        additional_experiments: typing.Optional[typing.List[str]] = None,
        sync: bool = True,
        create_request_timeout: typing.Optional[float] = None,
    ) -> google.cloud.aiplatform.models.Model

Runs the training job and returns a model.

If training on a Vertex AI dataset, you can use one of the following split configurations: Data fraction splits: Any of `training_fraction_split`, `validation_fraction_split` and `test_fraction_split` may optionally be provided, they must sum to up to 1. If the provided ones sum to less than 1, the remainder is assigned to sets as decided by Vertex AI. If none of the fractions are set, by default roughly 80% of data will be used for training, 10% for validation, and 10% for test.
    
    
    Predefined splits:
    Assigns input data to training, validation, and test sets based on the value of a provided key.
    If using predefined splits, `predefined_split_column_name` must be provided.
    Supported only for tabular Datasets.
    
    Timestamp splits:
    Assigns input data to training, validation, and test sets
    based on a provided timestamps. The youngest data pieces are
    assigned to training set, next to validation set, and the oldest
    to the test set.
    Supported only for tabular Datasets.
    

**Parameters**  
---  
**Name** | **Description**  
`dataset` |  `datasets.TabularDataset`   
Required. The dataset within the same Project from which data will be used to train the Model. The Dataset must use schema compatible with Model being trained, and what is compatible should be described in the used TrainingPipeline's [training_task_definition] [google.cloud.aiplatform.v1beta1.TrainingPipeline.training_task_definition]. For tabular Datasets, all their data is exported to training, to pick and choose from.  
`target_column` |  `str`   
Required. The name of the column values of which the Model is to predict.  
`training_fraction_split` |  `float`   
Optional. The fraction of the input data that is to be used to train the Model. This is ignored if Dataset is not provided.  
`validation_fraction_split` |  `float`   
Optional. The fraction of the input data that is to be used to validate the Model. This is ignored if Dataset is not provided.  
`test_fraction_split` |  `float`   
Optional. The fraction of the input data that is to be used to evaluate the Model. This is ignored if Dataset is not provided.  
`predefined_split_column_name` |  `str`   
Optional. The key is a name of one of the Dataset's data columns. The value of the key (either the label's value or value in the column) must be one of {`training`, `validation`, `test`}, and it defines to which set the given piece of data is assigned. If for a piece of data the key is not present or has an invalid value, that piece is ignored by the pipeline. Supported only for tabular and time series Datasets.  
`timestamp_split_column_name` |  `str`   
Optional. The key is a name of one of the Dataset's data columns. The value of the key values of the key (the values in the column) must be in RFC 3339 `date-time` format, where `time-offset` = `"Z"` (e.g. 1985-04-12T23:20:50.52Z). If for a piece of data the key is not present or has an invalid value, that piece is ignored by the pipeline. Supported only for tabular and time series Datasets. This parameter must be used with training_fraction_split, validation_fraction_split, and test_fraction_split.  
`weight_column` |  `str`   
Optional. Name of the column that should be used as the weight column. Higher values in this column give more importance to the row during Model training. The column must have numeric values between 0 and 10000 inclusively, and 0 value means that the row is ignored. If the weight column field is not set, then all rows are assumed to have equal weight of 1.  
`budget_milli_node_hours` |  `int`   
Optional. The train budget of creating this Model, expressed in milli node hours i.e. 1,000 value in this field means 1 node hour. The training cost of the model will not exceed this budget. The final cost will be attempted to be close to the budget, though may end up being (even) noticeably smaller - at the backend's discretion. This especially may happen when further model training ceases to provide any improvements. If the budget is set to a value known to be insufficient to train a Model for the given training set, the training won't be attempted and will error. The minimum value is 1000 and the maximum is 72000.  
`model_display_name` |  `str`   
Optional. If the script produces a managed Vertex AI Model. The display name of the Model. The name can be up to 128 characters long and can be consist of any UTF-8 characters. If not provided upon creation, the job's display_name is used.  
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
`disable_early_stopping` |  `bool`   
Required. If true, the entire budget is used. This disables the early stopping feature. By default, the early stopping feature is enabled, which means that training might stop before the entire training budget has been used, if further training does no longer brings significant improvement to the model.  
`export_evaluated_data_items` |  `bool`   
Whether to export the test set predictions to a BigQuery table. If False, then the export is not performed.  
`export_evaluated_data_items_bigquery_destination_uri` |  `string`   
Optional. URI of desired destination BigQuery table for exported test set predictions. Expected format: `bq://<project_id>:<dataset_id>:` If not specified, then results are exported to the following auto-created BigQuery table: `<project_id>:export_evaluated_examples_<model_name>_<yyyy_MM_dd'T'HH_mm_ss_SSS'Z'>.evaluated_examples` Applies only if [export_evaluated_data_items] is True.  
---|---  
`export_evaluated_data_items_override_destination` |  `bool`   
Whether to override the contents of [export_evaluated_data_items_bigquery_destination_uri], if the table exists, for exported test set predictions. If False, and the table exists, then the training job will fail. Applies only if [export_evaluated_data_items] is True and [export_evaluated_data_items_bigquery_destination_uri] is specified.  
`additional_experiments` |  `List[str]`   
Optional. Additional experiment flags for the automl tables training.  
`sync` |  `bool`   
Whether to execute this method synchronously. If False, this method will be executed in concurrent Future and any downstream object will be immediately returned and synced when the Future has completed.  
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
