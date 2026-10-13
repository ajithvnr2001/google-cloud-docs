---
url: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.ExperimentRun
title: Class ExperimentRun (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:26:40.450335+00:00
---

# Class ExperimentRun (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.ExperimentRun

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ExperimentRun (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0  1.153.1  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.116.0  1.115.0  1.114.0  1.113.0  1.112.0  1.111.0  1.110.0  1.109.0  1.108.0  1.107.0  1.106.0  1.105.0  1.104.0  1.103.0  1.102.0  1.101.0  1.100.0  1.99.0  1.98.0  1.97.0  1.96.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.1  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.39.0  1.38.1  1.37.0  1.36.4  1.35.0  1.34.0  1.33.1  1.32.0  1.31.1  1.30.1  1.29.0  1.28.1  1.27.1  1.26.1  1.25.0  1.24.1  1.23.0  1.22.1  1.21.0  1.20.0  1.19.1  1.18.3  1.17.1  1.16.1  1.15.1  1.14.0  1.13.1  1.12.1  1.11.0  1.10.0  1.9.0  1.8.1  1.7.1  1.6.2  1.5.0  1.4.3  1.3.0  1.2.0  1.1.1  1.0.1  0.9.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1 
    
    
    ExperimentRun(
        run_name: str,
        experiment: typing.Union[
            google.cloud.aiplatform.metadata.experiment_resources.Experiment, str
        ],
        *,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None
    )

A Vertex AI Experiment run.

## Properties 

### credentials

The credentials used to access this experiment run.

### location

The location that this experiment is located in.

### name

This run's name used to identify this run within it's Experiment.

### project

The project that this experiment run is located in.

### resource_id

The resource ID of this experiment run's Metadata context.

The resource ID is the final part of the resource name: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{resource ID}`

### resource_name

This run's Metadata context resource name.

In the format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}`

### state

The state of this run.

## Methods 

### ExperimentRun
    
    
    ExperimentRun(
        run_name: str,
        experiment: typing.Union[
            google.cloud.aiplatform.metadata.experiment_resources.Experiment, str
        ],
        *,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None
    )
    
    
    my_run = aiplatform.ExperimentRun('my-run', experiment='my-experiment')
    

**Parameters**  
---  
**Name** | **Description**  
`run_name` |  `str`   
Required. The name of this run.  
`experiment` |  `Union[experiment_resources.Experiment, str]`   
Required. The name or instance of this experiment.  
`project` |  `str`   
Optional. Project where this experiment run is located. Overrides project set in aiplatform.init.  
`location` |  `str`   
Optional. Location where this experiment run is located. Overrides location set in aiplatform.init.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials used to retrieve this experiment run. Overrides credentials set in aiplatform.init.  
  
### __init_subclass__
    
    
    __init_subclass__(
        *,
        experiment_loggable_schemas: typing.Tuple[
            google.cloud.aiplatform.metadata.experiment_resources._ExperimentLoggableSchema
        ],
        **kwargs
    )

Register the metadata_schema for the subclass so Experiment can use it to retrieve the associated types.

usage:

class PipelineJob(..., experiment_loggable_schemas= (_ExperimentLoggableSchema(title='system.PipelineRun'), )

### assign_backing_tensorboard
    
    
    assign_backing_tensorboard(
        tensorboard: typing.Union[
            google.cloud.aiplatform.tensorboard.tensorboard_resource.Tensorboard, str
        ],
    )

Assigns tensorboard as backing tensorboard to support timeseries metrics logging for this run.

**Parameter**  
---  
**Name** | **Description**  
`tensorboard` |  `Union[aiplatform.Tensorboard, str]`   
Required. Tensorboard instance or resource name.  
  
### associate_execution
    
    
    associate_execution(
        execution: google.cloud.aiplatform.metadata.execution.Execution,
    )

Associate an execution to this experiment run.

**Parameter**  
---  
**Name** | **Description**  
`execution` |  `aiplatform.Execution`   
Execution to associate to this run.  
  
### create
    
    
    create(
        run_name: str,
        *,
        experiment: typing.Optional[
            typing.Union[
                google.cloud.aiplatform.metadata.experiment_resources.Experiment, str
            ]
        ] = None,
        tensorboard: typing.Optional[
            typing.Union[
                google.cloud.aiplatform.tensorboard.tensorboard_resource.Tensorboard, str
            ]
        ] = None,
        state: google.cloud.aiplatform_v1.types.execution.Execution.State = State.RUNNING,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None
    ) -> google.cloud.aiplatform.metadata.experiment_run_resource.ExperimentRun

Creates a new experiment run in Vertex AI Experiments.
    
    
    my_run = aiplatform.ExperimentRun.create('my-run', experiment='my-experiment')
    

**Parameters**  
---  
**Name** | **Description**  
`run_name` |  `str`   
Required. The name of this run.  
`experiment` |  `Union[aiplatform.Experiment, str]`   
Optional. The name or instance of the experiment to create this run under. If not provided, will default to the experiment set in `aiplatform.init`.  
`tensorboard` |  `Union[aiplatform.Tensorboard, str]`   
Optional. The resource name or instance of Vertex Tensorboard to use as the backing Tensorboard for time series metric logging. If not provided, will default to the the backing tensorboard of parent experiment if set. Must be in same project and location as this experiment run.  
`state` |  `aiplatform.gapic.Execution.State`   
Optional. The state of this run. Defaults to RUNNING.  
`project` |  `str`   
Optional. Project where this experiment will be created. Overrides project set in aiplatform.init.  
`location` |  `str`   
Optional. Location where this experiment will be created. Overrides location set in aiplatform.init.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials used to create this experiment. Overrides credentials set in aiplatform.init.  
  
### delete
    
    
    delete(*, delete_backing_tensorboard_run: bool = False)

Deletes this experiment run.

Does not delete the executions, artifacts, or resources logged to this run.

**Parameter**  
---  
**Name** | **Description**  
`delete_backing_tensorboard_run` |  `bool`   
Optional. Whether to delete the backing tensorboard run that stores time series metrics for this run.  
  
### end_run
    
    
    end_run(
        *,
        state: google.cloud.aiplatform_v1.types.execution.Execution.State = State.COMPLETE
    )

Ends this experiment run and sets state to COMPLETE.

**Parameter**  
---  
**Name** | **Description**  
`state` |  `aiplatform.gapic.Execution.State`   
Optional. Override the state at the end of run. Defaults to COMPLETE.  
  
### get
    
    
    get(
        run_name: str,
        *,
        experiment: typing.Optional[
            typing.Union[
                google.cloud.aiplatform.metadata.experiment_resources.Experiment, str
            ]
        ] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None
    ) -> typing.Optional[
        google.cloud.aiplatform.metadata.experiment_run_resource.ExperimentRun
    ]

Gets experiment run if one exists with this run_name.

**Parameters**  
---  
**Name** | **Description**  
`run_name` |  `str`   
Required. The name of this run.  
`experiment` |  `Union[experiment_resources.Experiment, str]`   
Optional. The name or instance of this experiment. If not set, use the default experiment in `aiplatform.init`  
`project` |  `str`   
Optional. Project where this experiment run is located. Overrides project set in aiplatform.init.  
`location` |  `str`   
Optional. Location where this experiment run is located. Overrides location set in aiplatform.init.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials used to retrieve this experiment run. Overrides credentials set in aiplatform.init.  
  
### get_artifacts
    
    
    get_artifacts() -> typing.List[google.cloud.aiplatform.metadata.artifact.Artifact]

Get the list of artifacts associated to this run.

### get_classification_metrics
    
    
    get_classification_metrics() -> (
        typing.List[typing.Dict[str, typing.Union[str, typing.List]]]
    )

Get all the classification metrics logged to this run.
    
    
    my_run = aiplatform.ExperimentRun('my-run', experiment='my-experiment')
    metric = my_run.get_classification_metrics()[0]
    print(metric)
    ## print result:
        {
            "id": "e6c893a4-222e-4c60-a028-6a3b95dfc109",
            "display_name": "my-classification-metrics",
            "labels": ["cat", "dog"],
            "matrix": [[9,1], [1,9]],
            "fpr": [0.1, 0.5, 0.9],
            "tpr": [0.1, 0.7, 0.9],
            "thresholds": [0.9, 0.5, 0.1]
        }
    

### get_executions
    
    
    get_executions() -> (
        typing.List[google.cloud.aiplatform.metadata.execution.Execution]
    )

Get the List of Executions associated to this run

### get_experiment_models
    
    
    get_experiment_models() -> (
        typing.List[
            google.cloud.aiplatform.metadata.schema.google.artifact_schema.ExperimentModel
        ]
    )

Get all ExperimentModel associated to this experiment run.

### get_logged_custom_jobs
    
    
    get_logged_custom_jobs() -> typing.List[google.cloud.aiplatform.jobs.CustomJob]

Get all CustomJobs associated to this experiment run.

### get_logged_pipeline_jobs
    
    
    get_logged_pipeline_jobs() -> (
        typing.List[google.cloud.aiplatform.pipeline_jobs.PipelineJob]
    )

Get all PipelineJobs associated to this experiment run.

### get_metrics
    
    
    get_metrics() -> typing.Dict[str, typing.Union[float, int, str]]

Get the summary metrics logged to this run.

### get_params
    
    
    get_params() -> typing.Dict[str, typing.Union[float, int, str]]

Get the parameters logged to this run.

### get_state
    
    
    get_state() -> google.cloud.aiplatform_v1.types.execution.Execution.State

The state of this run.

### get_time_series_data_frame
    
    
    get_time_series_data_frame() -> pd.DataFrame

Returns all time series in this Run as a DataFrame.

**Returns**  
---  
**Type** | **Description**  
`pd.DataFrame` | Time series metrics in this Run as a Dataframe.  
  
### list
    
    
    list(
        *,
        experiment: typing.Optional[
            typing.Union[
                google.cloud.aiplatform.metadata.experiment_resources.Experiment, str
            ]
        ] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None
    ) -> typing.List[
        google.cloud.aiplatform.metadata.experiment_run_resource.ExperimentRun
    ]

List the experiment runs for a given aiplatform.Experiment.
    
    
    my_runs = aiplatform.ExperimentRun.list(experiment='my-experiment')
    

**Parameters**  
---  
**Name** | **Description**  
`experiment` |  `Union[aiplatform.Experiment, str]`   
Optional. The experiment name or instance to list the experiment run from. If not provided, will use the experiment set in aiplatform.init.  
`project` |  `str`   
Optional. Project where this experiment is located. Overrides project set in aiplatform.init.  
`location` |  `str`   
Optional. Location where this experiment is located. Overrides location set in aiplatform.init.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials used to retrieve this experiment. Overrides credentials set in aiplatform.init.  
  
### log
    
    
    log(
        *,
        pipeline_job: typing.Optional[
            google.cloud.aiplatform.pipeline_jobs.PipelineJob
        ] = None
    )

Log a Vertex Resource to this experiment run.
    
    
    my_run = aiplatform.ExperimentRun('my-run', experiment='my-experiment')
    my_job = aiplatform.PipelineJob(...)
    my_job.submit()
    my_run.log(my_job)
    

**Parameter**  
---  
**Name** | **Description**  
`pipeline_job` |  `aiplatform.PipelineJob`   
Optional. A Vertex PipelineJob.  
  
### log_classification_metrics
    
    
    log_classification_metrics(
        *,
        labels: typing.Optional[typing.List[str]] = None,
        matrix: typing.Optional[typing.List[typing.List[int]]] = None,
        fpr: typing.Optional[typing.List[float]] = None,
        tpr: typing.Optional[typing.List[float]] = None,
        threshold: typing.Optional[typing.List[float]] = None,
        display_name: typing.Optional[str] = None
    ) -> (
        google.cloud.aiplatform.metadata.schema.google.artifact_schema.ClassificationMetrics
    )

Create an artifact for classification metrics and log to ExperimentRun. Currently supports confusion matrix and ROC curve.
    
    
    my_run = aiplatform.ExperimentRun('my-run', experiment='my-experiment')
    classification_metrics = my_run.log_classification_metrics(
        display_name='my-classification-metrics',
        labels=['cat', 'dog'],
        matrix=[[9, 1], [1, 9]],
        fpr=[0.1, 0.5, 0.9],
        tpr=[0.1, 0.7, 0.9],
        threshold=[0.9, 0.5, 0.1],
    )
    

**Parameters**  
---  
**Name** | **Description**  
`labels` |  `List[str]`   
Optional. List of label names for the confusion matrix. Must be set if 'matrix' is set.  
`matrix` |  `List[List[int]`   
Optional. Values for the confusion matrix. Must be set if 'labels' is set.  
`fpr` |  `List[float]`   
Optional. List of false positive rates for the ROC curve. Must be set if 'tpr' or 'thresholds' is set.  
`tpr` |  `List[float]`   
Optional. List of true positive rates for the ROC curve. Must be set if 'fpr' or 'thresholds' is set.  
`threshold` |  `List[float]`   
Optional. List of thresholds for the ROC curve. Must be set if 'fpr' or 'tpr' is set.  
`display_name` |  `str`   
Optional. The user-defined name for the classification metric artifact.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | if 'labels' and 'matrix' are not set together or if 'labels' and 'matrix' are not in the same length or if 'fpr' and 'tpr' and 'threshold' are not set together or if 'fpr' and 'tpr' and 'threshold' are not in the same length  
  
### log_metrics
    
    
    log_metrics(metrics: typing.Dict[str, typing.Union[float, int, str]])

Log single or multiple Metrics with specified key and value pairs.

Metrics with the same key will be overwritten.
    
    
    my_run = aiplatform.ExperimentRun('my-run', experiment='my-experiment')
    my_run.log_metrics({'accuracy': 0.9, 'recall': 0.8})
    

**Parameter**  
---  
**Name** | **Description**  
`metrics` |  `Dict[str, Union[float, int, str]]`   
Required. Metrics key/value pairs.  
**Exceptions**  
---  
**Type** | **Description**  
`TypeError` | If keys are not str or values are not float, int, or str.  
  
### log_model
    
    
    log_model(
        model: typing.Union[sklearn.base.BaseEstimator, xgb.Booster, tf.Module],
        artifact_id: typing.Optional[str] = None,
        *,
        uri: typing.Optional[str] = None,
        input_example: typing.Union[list, dict, pd.DataFrame, np.ndarray] = None,
        display_name: typing.Optional[str] = None,
        metadata_store_id: typing.Optional[str] = "default",
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        staging_bucket: typing.Optional[str] = None
    ) -> google.cloud.aiplatform.metadata.schema.google.artifact_schema.ExperimentModel

Saves a ML model into a MLMD artifact and log it to this ExperimentRun.

Supported model frameworks: sklearn, xgboost, tensorflow.

Example usage: model = LinearRegression() model.fit(X, y) aiplatform.init( project="my-project", location="my-location", staging_bucket="gs://my-bucket", experiment="my-exp" ) with aiplatform.start_run("my-run"): aiplatform.log_model(model, "my-sklearn-model")

**Parameters**  
---  
**Name** | **Description**  
`model` |  `Union["sklearn.base.BaseEstimator", "xgb.Booster", "tf.Module"]`   
Required. A machine learning model.  
`artifact_id` |  `str`   
Optional. The resource id of the artifact. This id must be globally unique in a metadataStore. It may be up to 63 characters, and valid characters are `[a-z0-9_-]`. The first character cannot be a number or hyphen.  
`uri` |  `str`   
Optional. A gcs directory to save the model file. If not provided, `gs://default-bucket/timestamp-uuid-frameworkName-model` will be used. If default staging bucket is not set, a new bucket will be created.  
`input_example` |  `Union[list, dict, pd.DataFrame, np.ndarray]`   
Optional. An example of a valid model input. Will be stored as a yaml file in the gcs uri. Accepts list, dict, pd.DataFrame, and np.ndarray The value inside a list must be a scalar or list. The value inside a dict must be a scalar, list, or np.ndarray.  
`display_name` |  `str`   
Optional. The display name of the artifact.  
`metadata_store_id` |  `str`   
Optional. The <metadata_store_id> portion of the resource name with the format: projects/123/locations/us-central1/metadataStores/<metadata_store_id>/artifacts/<resource_id> If not provided, the MetadataStore's ID will be set to "default".  
`project` |  `str`   
Optional. Project used to create this Artifact. Overrides project set in aiplatform.init.  
`location` |  `str`   
Optional. Location used to create this Artifact. Overrides location set in aiplatform.init.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials used to create this Artifact. Overrides credentials set in aiplatform.init.  
`staging_bucket` |  `str`   
Optional. The staging bucket used to save the model. If not provided, the staging bucket set in aiplatform.init will be used. A staging bucket or uri is required for saving a model.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | if model type is not supported.  
`RuntimeError` | If staging bucket was not set using aiplatform.init and a staging bucket or uri was not passed in.  
  
### log_params
    
    
    log_params(params: typing.Dict[str, typing.Union[float, int, str]])

Log single or multiple parameters with specified key value pairs.

Parameters with the same key will be overwritten.
    
    
    my_run = aiplatform.ExperimentRun('my-run', experiment='my-experiment')
    my_run.log_params({'learning_rate': 0.1, 'dropout_rate': 0.2})
    

**Parameter**  
---  
**Name** | **Description**  
`params` |  `Dict[str, Union[float, int, str]]`   
Required. Parameter key/value pairs.  
**Exceptions**  
---  
**Type** | **Description**  
`TypeError` | If key is not str or value is not float, int, str.  
  
### log_time_series_metrics
    
    
    log_time_series_metrics(
        metrics: typing.Dict[str, float],
        step: typing.Optional[int] = None,
        wall_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = None,
    )

Logs time series metrics to backing TensorboardRun of this Experiment Run.
    
    
    run.log_time_series_metrics({'accuracy': 0.9}, step=10)
    

**Parameters**  
---  
**Name** | **Description**  
`metrics` |  `Dict[str, Union[str, float]]`   
Required. Dictionary of where keys are metric names and values are metric values.  
`step` |  `int`   
Optional. Step index of this data point within the run. If not provided, the latest step amongst all time series metrics already logged will be used.  
`wall_time` |  `timestamp_pb2.Timestamp`   
Optional. Wall clock timestamp when this data point is generated by the end user. If not provided, this will be generated based on the value from time.time()  
**Exceptions**  
---  
**Type** | **Description**  
`RuntimeError` | If current experiment run doesn't have a backing Tensorboard resource.  
  
### update_state
    
    
    update_state(state: google.cloud.aiplatform_v1.types.execution.Execution.State)

Update the state of this experiment run.
    
    
    my_run = aiplatform.ExperimentRun('my-run', experiment='my-experiment')
    my_run.update_state(state=aiplatform.gapic.Execution.State.COMPLETE)
    

**Parameter**  
---  
**Name** | **Description**  
`state` |  `aiplatform.gapic.Execution.State`   
State of this run.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
