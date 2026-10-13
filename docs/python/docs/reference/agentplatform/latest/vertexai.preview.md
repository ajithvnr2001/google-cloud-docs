---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview
title: Package preview (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:19.774065+00:00
---

# Package preview (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package preview (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 

API documentation for `preview` package.

## Packages 

### [tuning](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.tuning)

API documentation for `tuning` package.

### [reasoning_engines](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.reasoning_engines)

API documentation for `reasoning_engines` package.

## Modules 

### [generative_models](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.generative_models)

Classes for working with the Gemini models.

### [language_models](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.language_models)

Classes for working with language models.

### [vision_models](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.vision_models)

Classes for working with vision models.

## Packages Functions 

### end_run
    
    
    end_run(
        state: google.cloud.aiplatform_v1.types.execution.Execution.State = State.COMPLETE,
    )

Ends the the current experiment run.
    
    
    aiplatform.start_run('my-run')
    ...
    aiplatform.end_run()
    

### get_experiment_df
    
    
    get_experiment_df(
        experiment: typing.Optional[str] = None, *, include_time_series: bool = True
    ) -> pd.DataFrame

Returns a Pandas DataFrame of the parameters and metrics associated with one experiment.

Example:
    
    
    aiplatform.init(experiment='exp-1')
    aiplatform.start_run(run='run-1')
    aiplatform.log_params({'learning_rate': 0.1})
    aiplatform.log_metrics({'accuracy': 0.9})
    
    aiplatform.start_run(run='run-2')
    aiplatform.log_params({'learning_rate': 0.2})
    aiplatform.log_metrics({'accuracy': 0.95})
    
    aiplatform.get_experiment_df()
    

Will result in the following DataFrame:
    
    
    experiment_name | run_name      | param.learning_rate | metric.accuracy
    exp-1           | run-1         | 0.1                 | 0.9
    exp-1           | run-2         | 0.2                 | 0.95
    

**Parameters**  
---  
**Name** | **Description**  
`experiment` | `str`  
Name of the Experiment to filter results. If not set, return results of current active experiment.  
`include_time_series` | `bool`  
Optional. Whether or not to include time series metrics in df. Default is True. Setting to False will largely improve execution time and reduce quota contributing calls. Recommended when time series metrics are not needed or number of runs in Experiment is large. For time series metrics consider querying a specific run using get_time_series_data_frame.  
  
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

Create an artifact for classification metrics and log to ExperimentRun. Currently support confusion matrix and ROC curve.
    
    
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
`labels` | `List[str]`  
Optional. List of label names for the confusion matrix. Must be set if 'matrix' is set.  
`matrix` | `List[List[int]`  
Optional. Values for the confusion matrix. Must be set if 'labels' is set.  
`fpr` | `List[float]`  
Optional. List of false positive rates for the ROC curve. Must be set if 'tpr' or 'thresholds' is set.  
`tpr` | `List[float]`  
Optional. List of true positive rates for the ROC curve. Must be set if 'fpr' or 'thresholds' is set.  
`threshold` | `List[float]`  
Optional. List of thresholds for the ROC curve. Must be set if 'fpr' or 'tpr' is set.  
`display_name` | `str`  
Optional. The user-defined name for the classification metric artifact.  
  
### log_metrics
    
    
    log_metrics(metrics: typing.Dict[str, typing.Union[float, int, str]])

Log single or multiple Metrics with specified key and value pairs.

Metrics with the same key will be overwritten.
    
    
    aiplatform.start_run('my-run', experiment='my-experiment')
    aiplatform.log_metrics({'accuracy': 0.9, 'recall': 0.8})
    

**Parameter**  
---  
**Name** | **Description**  
`metrics` | `Dict[str, Union[float, int, str]]`  
Required. Metrics key/value pairs.  
  
### log_params
    
    
    log_params(params: typing.Dict[str, typing.Union[float, int, str]])

Log single or multiple parameters with specified key and value pairs.

Parameters with the same key will be overwritten.
    
    
    aiplatform.start_run('my-run')
    aiplatform.log_params({'learning_rate': 0.1, 'dropout_rate': 0.2})
    

**Parameter**  
---  
**Name** | **Description**  
`params` | `Dict[str, Union[float, int, str]]`  
Required. Parameter key/value pairs.  
  
### log_time_series_metrics
    
    
    log_time_series_metrics(
        metrics: typing.Dict[str, float],
        step: typing.Optional[int] = None,
        wall_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = None,
    )

Logs time series metrics to to this Experiment Run.

Requires the experiment or experiment run has a backing Vertex Tensorboard resource.
    
    
    my_tensorboard = aiplatform.Tensorboard(...)
    aiplatform.init(experiment='my-experiment', experiment_tensorboard=my_tensorboard)
    aiplatform.start_run('my-run')
    
    # increments steps as logged
    for i in range(10):
        aiplatform.log_time_series_metrics({'loss': loss})
    
    # explicitly log steps
    for i in range(10):
        aiplatform.log_time_series_metrics({'loss': loss}, step=i)
    

**Parameters**  
---  
**Name** | **Description**  
`metrics` | `Dict[str, Union[str, float]]`  
Required. Dictionary of where keys are metric names and values are metric values.  
`step` | `int`  
Optional. Step index of this data point within the run. If not provided, the latest step amongst all time series metrics already logged will be used.  
`wall_time` | `timestamp_pb2.Timestamp`  
Optional. Wall clock timestamp when this data point is generated by the end user. If not provided, this will be generated based on the value from time.time()  
  
### start_run
    
    
    start_run(
        run: str,
        *,
        tensorboard: typing.Optional[
            typing.Union[
                google.cloud.aiplatform.tensorboard.tensorboard_resource.Tensorboard, str
            ]
        ] = None,
        resume=False
    ) -> google.cloud.aiplatform.metadata.experiment_run_resource.ExperimentRun

Start a run to current session.
    
    
    aiplatform.init(experiment='my-experiment')
    aiplatform.start_run('my-run')
    aiplatform.log_params({'learning_rate':0.1})
    

Use as context manager. Run will be ended on context exit:
    
    
    aiplatform.init(experiment='my-experiment')
    with aiplatform.start_run('my-run') as my_run:
        my_run.log_params({'learning_rate':0.1})
    

Resume a previously started run:
    
    
    aiplatform.init(experiment='my-experiment')
    with aiplatform.start_run('my-run', resume=True) as my_run:
        my_run.log_params({'learning_rate':0.1})
    

**Parameters**  
---  
**Name** | **Description**  
`run` | `str`  
Required. Name of the run to assign current session with.  
`resume` | `bool`  
Whether to resume this run. If False a new run will be created.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
