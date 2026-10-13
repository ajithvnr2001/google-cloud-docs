---
url: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform
title: Package aiplatform (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:19:27.500500+00:00
---

# Package aiplatform (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package aiplatform (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0  1.153.1  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.116.0  1.115.0  1.114.0  1.113.0  1.112.0  1.111.0  1.110.0  1.109.0  1.108.0  1.107.0  1.106.0  1.105.0  1.104.0  1.103.0  1.102.0  1.101.0  1.100.0  1.99.0  1.98.0  1.97.0  1.96.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.1  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.39.0  1.38.1  1.37.0  1.36.4  1.35.0  1.34.0  1.33.1  1.32.0  1.31.1  1.30.1  1.29.0  1.28.1  1.27.1  1.26.1  1.25.0  1.24.1  1.23.0  1.22.1  1.21.0  1.20.0  1.19.1  1.18.3  1.17.1  1.16.1  1.15.1  1.14.0  1.13.1  1.12.1  1.11.0  1.10.0  1.9.0  1.8.1  1.7.1  1.6.2  1.5.0  1.4.3  1.3.0  1.2.0  1.1.1  1.0.1  0.9.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1 

API documentation for `aiplatform` package.

## Classes 

### [Artifact](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.Artifact)

Metadata Artifact resource for Vertex AI

### [AutoMLForecastingTrainingJob](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.AutoMLForecastingTrainingJob)

Class to train AutoML forecasting models.

The `AutoMLForecastingTrainingJob` class uses the AutoML training method to train and run a forecasting model. The `AutoML` training method is a good choice for most forecasting use cases. If your use case doesn't benefit from the `Seq2seq` or the `Temporal fusion transformer` training method offered by the [`SequenceToSequencePlusForecastingTrainingJob`](https://cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.SequenceToSequencePlusForecastingTrainingJob) and [`TemporalFusionTransformerForecastingTrainingJob`]<https://cloud.google.com/python/docs/reference/aiplatform/latest/>[google.cloud.aiplatform.TemporalFusionTransformerForecastingTrainingJob](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.TemporalFusionTransformerForecastingTrainingJob)) classes respectively, then `AutoML` is likely the best training method for your forecasting predictions.

For sample code that shows you how to use `AutoMLForecastingTrainingJob` see the [Create a training pipeline forecasting sample](https://github.com/googleapis/python-aiplatform/blob/8ddc062669044ac0889d9f27c93a8b36c1140433/samples/model-builder/create_training_pipeline_forecasting_sample.py) on GitHub.

### [AutoMLImageTrainingJob](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.AutoMLImageTrainingJob)

Creates an AutoML image training job.

Use the `AutoMLImageTrainingJob` class to create, train, and return an image model. For more information about working with image data models in Vertex AI, see [Image data](https://cloud.google.com/vertex-ai/docs/training-overview#image_data).

For an example of how to use the `AutoMLImageTrainingJob` class, see the tutorial in the [AutoML image classification](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/migration/sdk-automl-text-classification-batch-prediction.ipynb) notebook on GitHub.

### [AutoMLTabularTrainingJob](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.AutoMLTabularTrainingJob)

Constructs a AutoML Tabular Training Job.

Example usage:

job = training_jobs.AutoMLTabularTrainingJob( display_name="my_display_name", optimization_prediction_type="classification", optimization_objective="minimize-log-loss", column_specs={"column_1": "auto", "column_2": "numeric"}, labels={'key': 'value'}, )

### [AutoMLTextTrainingJob](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.AutoMLTextTrainingJob)

Constructs a AutoML Text Training Job.

### [AutoMLVideoTrainingJob](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.AutoMLVideoTrainingJob)

Constructs a AutoML Video Training Job.

### [BatchPredictionJob](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.BatchPredictionJob)

Retrieves a BatchPredictionJob resource and instantiates its representation.

### [CustomContainerTrainingJob](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.CustomContainerTrainingJob)

Class to launch a Custom Training Job in Vertex AI using a Container.

### [CustomJob](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.CustomJob)

Vertex AI Custom Job.

### [CustomPythonPackageTrainingJob](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.CustomPythonPackageTrainingJob)

Class to launch a Custom Training Job in Vertex AI using a Python Package.

Use the `CustomPythonPackageTrainingJob` class to use a Python package to launch a custom training pipeline in Vertex AI. For an example of how to use the `CustomPythonPackageTrainingJob` class, see the tutorial in the [Custom training using Python package, managed text dataset, and TensorFlow serving container](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/sdk/SDK_Custom_Training_Python_Package_Managed_Text_Dataset_Tensorflow_Serving_Container.ipynb) notebook.

### [CustomTrainingJob](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.CustomTrainingJob)

Class to launch a Custom Training Job in Vertex AI using a script.

Takes a training implementation as a python script and executes that script in Cloud Vertex AI Training.

### [DeploymentResourcePool](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.DeploymentResourcePool)

Retrieves a DeploymentResourcePool.

### [Endpoint](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.Endpoint)

Retrieves an endpoint resource.

### [EntityType](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.EntityType)

Public managed EntityType resource for Vertex AI.

### [Execution](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.Execution)

Metadata Execution resource for Vertex AI

### [Experiment](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.Experiment)

Represents a Vertex AI Experiment resource.

### [ExperimentRun](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.ExperimentRun)

A Vertex AI Experiment run.

### [Feature](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.Feature)

Managed feature resource for Vertex AI.

### [Featurestore](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.Featurestore)

Managed featurestore resource for Vertex AI.

### [HyperparameterTuningJob](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.HyperparameterTuningJob)

Vertex AI Hyperparameter Tuning Job.

### [ImageDataset](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.ImageDataset)

A managed image dataset resource for Vertex AI.

Use this class to work with a managed image dataset. To create a managed image dataset, you need a datasource file in CSV format and a schema file in YAML format. A schema is optional for a custom model. You put the CSV file and the schema into Cloud Storage buckets.

Use image data for the following objectives:

  * Single-label classification. For more information, see [Prepare image training data for single-label classification](https://cloud.google.com/vertex-ai/docs/image-data/classification/prepare-data#single-label-classification).
  * Multi-label classification. For more information, see [Prepare image training data for multi-label classification](https://cloud.google.com/vertex-ai/docs/image-data/classification/prepare-data#multi-label-classification).
  * Object detection. For more information, see [Prepare image training data for object detection](https://cloud.google.com/vertex-ai/docs/image-data/object-detection/prepare-data).



The following code shows you how to create an image dataset by importing data from a CSV datasource file and a YAML schema file. The schema file you use depends on whether your image dataset is used for single-label classification, multi-label classification, or object detection.
    
    
    my_dataset = aiplatform.ImageDataset.create(
        display_name="my-image-dataset",
        gcs_source=['gs://path/to/my/image-dataset.csv'],
        import_schema_uri=['gs://path/to/my/schema.yaml']
    )
    

### [MatchingEngineIndex](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.MatchingEngineIndex)

Matching Engine index resource for Vertex AI.

### [MatchingEngineIndexEndpoint](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.MatchingEngineIndexEndpoint)

Matching Engine index endpoint resource for Vertex AI.

### [Model](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.Model)

Retrieves the model resource and instantiates its representation.

### [ModelDeploymentMonitoringJob](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.ModelDeploymentMonitoringJob)

Vertex AI Model Deployment Monitoring Job.

This class should be used in conjunction with the Endpoint class in order to configure model monitoring for deployed models.

### [ModelEvaluation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.ModelEvaluation)

Retrieves the ModelEvaluation resource and instantiates its representation.

### [PipelineJob](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.PipelineJob)

Retrieves a PipelineJob resource and instantiates its representation.

### [PipelineJobSchedule](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.PipelineJobSchedule)

Retrieves a PipelineJobSchedule resource and instantiates its representation.

### [PrivateEndpoint](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.PrivateEndpoint)

Represents a Vertex AI PrivateEndpoint resource.

Read more [about private endpoints in the documentation.](https://cloud.google.com/vertex-ai/docs/predictions/using-private-endpoints)

### [SequenceToSequencePlusForecastingTrainingJob](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.SequenceToSequencePlusForecastingTrainingJob)

Class to train Sequence to Sequence (Seq2Seq) forecasting models.

The `SequenceToSequencePlusForecastingTrainingJob` class uses the `Seq2seq+` training method to train and run a forecasting model. The `Seq2seq+` training method is a good choice for experimentation. Its algorithm is simpler and uses a smaller search space than the `AutoML` option. `Seq2seq+` is a good option if you want fast results and your datasets are smaller than 1 GB.

For sample code that shows you how to use `SequenceToSequencePlusForecastingTrainingJob`, see the [Create a training pipeline forecasting Seq2seq sample](https://github.com/googleapis/python-aiplatform/blob/8ddc062669044ac0889d9f27c93a8b36c1140433/samples/model-builder/create_training_pipeline_forecasting_seq2seq_sample.py) on GitHub.

### [TabularDataset](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.TabularDataset)

A managed tabular dataset resource for Vertex AI.

Use this class to work with tabular datasets. You can use a CSV file, BigQuery, or a pandas [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) to create a tabular dataset. For more information about paging through BigQuery data, see [Read data with BigQuery API using pagination](https://cloud.google.com/bigquery/docs/paging-results). For more information about tabular data, see [Tabular data](https://cloud.google.com/vertex-ai/docs/training-overview#tabular_data).

The following code shows you how to create and import a tabular dataset with a CSV file.
    
    
    my_dataset = aiplatform.TabularDataset.create(
        display_name="my-dataset", gcs_source=['gs://path/to/my/dataset.csv'])
    

Contrary to unstructured datasets, creating and importing a tabular dataset can only be done in a single step.

If you create a tabular dataset with a pandas [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html), you need to use a BigQuery table to stage the data for Vertex AI:
    
    
    my_dataset = aiplatform.TabularDataset.create_from_dataframe(
        df_source=my_pandas_dataframe,
        staging_path=f"bq://{bq_dataset_id}.table-unique"
    )
    

### [TemporalFusionTransformerForecastingTrainingJob](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.TemporalFusionTransformerForecastingTrainingJob)

Class to train Temporal Fusion Transformer (TFT) forecasting models.

The `TemporalFusionTransformerForecastingTrainingJob` class uses the Temporal Fusion Transformer (TFT) training method to train and run a forecasting model. The TFT training method implements an attention-based deep neural network (DNN) model that uses a multi-horizon forecasting task to produce predictions.

For sample code that shows you how to use `TemporalFusionTransformerForecastingTrainingJob, see the [Create a training pipeline forecasting temporal fusion transformer sample](https://github.com/googleapis/python-aiplatform/blob/8ddc062669044ac0889d9f27c93a8b36c1140433/samples/model-builder/create_training_pipeline_forecasting_tft_sample.py) on GitHub.

### [Tensorboard](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.Tensorboard)

Managed tensorboard resource for Vertex AI.

### [TensorboardExperiment](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.TensorboardExperiment)

Managed tensorboard resource for Vertex AI.

### [TensorboardRun](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.TensorboardRun)

Managed tensorboard resource for Vertex AI.

### [TensorboardTimeSeries](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.TensorboardTimeSeries)

Managed tensorboard resource for Vertex AI.

### [TextDataset](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.TextDataset)

A managed text dataset resource for Vertex AI.

Use this class to work with a managed text dataset. To create a managed text dataset, you need a datasource file in CSV format and a schema file in YAML format. A schema is optional for a custom model. The CSV file and the schema are accessed in Cloud Storage buckets.

Use text data for the following objectives:

  * Classification. For more information, see [Prepare text training data for classification](https://cloud.google.com/vertex-ai/docs/text-data/classification/prepare-data).
  * Entity extraction. For more information, see [Prepare text training data for entity extraction](https://cloud.google.com/vertex-ai/docs/text-data/entity-extraction/prepare-data).
  * Sentiment analysis. For more information, see [Prepare text training data for sentiment analysis](Prepare text training data for sentiment analysis).



The following code shows you how to create and import a text dataset with a CSV datasource file and a YAML schema file. The schema file you use depends on whether your text dataset is used for single-label classification, multi-label classification, or object detection.
    
    
    my_dataset = aiplatform.TextDataset.create(
        display_name="my-text-dataset",
        gcs_source=['gs://path/to/my/text-dataset.csv'],
        import_schema_uri=['gs://path/to/my/schema.yaml'],
    )
    

### [TimeSeriesDataset](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.TimeSeriesDataset)

A managed time series dataset resource for Vertex AI.

Use this class to work with time series datasets. A time series is a dataset that contains data recorded at different time intervals. The dataset includes time and at least one variable that's dependent on time. You use a time series dataset for forecasting predictions. For more information, see [Forecasting overview](https://cloud.google.com/vertex-ai/docs/tabular-data/forecasting/overview).

You can create a managed time series dataset from CSV files in a Cloud Storage bucket or from a BigQuery table.

The following code shows you how to create a `TimeSeriesDataset` with a CSV file that has the time series dataset:
    
    
    my_dataset = aiplatform.TimeSeriesDataset.create(
        display_name="my-dataset",
        gcs_source=['gs://path/to/my/dataset.csv'],
    )
    

The following code shows you how to create with a `TimeSeriesDataset` with a BigQuery table file that has the time series dataset:
    
    
    my_dataset = aiplatform.TimeSeriesDataset.create(
        display_name="my-dataset",
        bq_source=['bq://path/to/my/bigquerydataset.train'],
    )
    

### [TimeSeriesDenseEncoderForecastingTrainingJob](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.TimeSeriesDenseEncoderForecastingTrainingJob)

Class to train Time series Dense Encoder (TiDE) forecasting models.

The `TimeSeriesDenseEncoderForecastingTrainingJob` class uses the Time-series Dense Encoder (TiDE) training method to train and run a forecasting model. TiDE uses a [multi-layer perceptron](https://arxiv.org/abs/2304.08424) (MLP) to provide the speed of forecasting linear models with covariates and non-linear dependencies. For more information about TiDE, see [Recent advances in deep long-horizon forecasting](https://blog.research.google/2023/04/recent-advances-in-deep-long-horizon.html) and this [TiDE blog post](https://cloud.google.com/blog/products/ai-machine-learning/vertex-ai-forecasting).

### [VideoDataset](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.VideoDataset)

A managed video dataset resource for Vertex AI.

Use this class to work with a managed video dataset. To create a video dataset, you need a datasource in CSV format and a schema in YAML format. The CSV file and the schema are accessed in Cloud Storage buckets.

Use video data for the following objectives:

Classification. For more information, see Classification schema files. Action recognition. For more information, see Action recognition schema files. Object tracking. For more information, see Object tracking schema files. The following code shows you how to create and import a dataset to train a video classification model. The schema file you use depends on whether you use your video dataset for action classification, recognition, or object tracking.
    
    
    my_dataset = aiplatform.VideoDataset.create(
        gcs_source=['gs://path/to/my/dataset.csv'],
        import_schema_uri=['gs://aip.schema.dataset.ioformat.video.classification.yaml']
    )
    

## Packages Functions 

### autolog
    
    
    autolog(disable=False)

Enables autologging of parameters and metrics to Vertex Experiments.

After calling `aiplatform.autolog()`, any metrics and parameters from model training calls with supported ML frameworks will be automatically logged to Vertex Experiments.

Using autologging requires setting an experiment and experiment_tensorboard.

**Parameter**  
---  
**Name** | **Description**  
`disable` | `bool`  
Optional. Whether to disable autologging. Defaults to False. If set to True, this resets the MLFlow tracking URI to its previous state before autologging was called and remove logging filters.  
  
### end_run
    
    
    end_run(
        state: google.cloud.aiplatform_v1.types.execution.Execution.State = State.COMPLETE,
    )

Ends the the current experiment run.
    
    
    aiplatform.start_run('my-run')
    ...
    aiplatform.end_run()
    

### end_upload_tb_log
    
    
    end_upload_tb_log()

Ends the current TensorBoard uploader
    
    
    aiplatform.start_upload_tb_log(...)
    ...
    aiplatform.end_upload_tb_log()
    

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
  
### get_experiment_model
    
    
    get_experiment_model(
        artifact_id: str,
        *,
        metadata_store_id: str = "default",
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None
    ) -> google.cloud.aiplatform.metadata.schema.google.artifact_schema.ExperimentModel

Retrieves an existing ExperimentModel artifact given an artifact id.

**Parameters**  
---  
**Name** | **Description**  
`artifact_id` | `str`  
Required. An artifact id of the ExperimentModel artifact.  
`metadata_store_id` | `str`  
Optional. MetadataStore to retrieve Artifact from. If not set, metadata_store_id is set to "default". If artifact_id is a fully-qualified resource name, its metadata_store_id overrides this one.  
`project` | `str`  
Optional. Project to retrieve the artifact from. If not set, project set in aiplatform.init will be used.  
`location` | `str`  
Optional. Location to retrieve the Artifact from. If not set, location set in aiplatform.init will be used.  
`credentials` | `auth_credentials.Credentials`  
Optional. Custom credentials to use to retrieve this Artifact. Overrides credentials set in aiplatform.init.  
  
### get_pipeline_df
    
    
    get_pipeline_df(pipeline: str) -> pd.DataFrame

Returns a Pandas DataFrame of the parameters and metrics associated with one pipeline.

### init
    
    
    init(
        *,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        experiment: typing.Optional[str] = None,
        experiment_description: typing.Optional[str] = None,
        experiment_tensorboard: typing.Optional[
            typing.Union[
                str,
                google.cloud.aiplatform.tensorboard.tensorboard_resource.Tensorboard,
                bool,
            ]
        ] = None,
        staging_bucket: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        encryption_spec_key_name: typing.Optional[str] = None,
        network: typing.Optional[str] = None,
        service_account: typing.Optional[str] = None,
        api_endpoint: typing.Optional[str] = None,
        api_key: typing.Optional[str] = None,
        api_transport: typing.Optional[str] = None,
        request_metadata: typing.Optional[typing.Sequence[typing.Tuple[str, str]]] = None
    )

Updates common initialization parameters with provided options.

**Parameters**  
---  
**Name** | **Description**  
`project` | `str`  
The default project to use when making API calls.  
`location` | `str`  
The default location to use when making API calls. If not set defaults to us-central-1.  
`experiment` | `str`  
Optional. The experiment name.  
`experiment_description` | `str`  
Optional. The description of the experiment.  
`experiment_tensorboard` | `Union[str, tensorboard_resource.Tensorboard, bool]`  
Optional. The Vertex AI TensorBoard instance, Tensorboard resource name, or Tensorboard resource ID to use as a backing Tensorboard for the provided experiment. Example tensorboard resource name format: "projects/123/locations/us-central1/tensorboards/456" If `experiment_tensorboard` is provided and `experiment` is not, the provided `experiment_tensorboard` will be set as the global Tensorboard. Any subsequent calls to aiplatform.init() with `experiment` and without `experiment_tensorboard` will automatically assign the global Tensorboard to the `experiment`. If `experiment_tensorboard` is ommitted or set to `True` or `None` the global Tensorboard will be assigned to the `experiment`. If a global Tensorboard is not set, the default Tensorboard instance will be used, and created if it does not exist. To disable creating and using Tensorboard with `experiment`, set `experiment_tensorboard` to `False`. Any subsequent calls to aiplatform.init() should include this setting as well.  
`staging_bucket` | `str`  
The default staging bucket to use to stage artifacts when making API calls. In the form gs://...  
`credentials` | `google.auth.credentials.Credentials`  
The default custom credentials to use when making API calls. If not provided credentials will be ascertained from the environment.  
`encryption_spec_key_name` | `Optional[str]`  
Optional. The Cloud KMS resource identifier of the customer managed encryption key used to protect a resource. Has the form: `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`. The key needs to be in the same region as where the compute resource is created. If set, this resource and all sub-resources will be secured by this key.  
`network` | `str`  
Optional. The full name of the Compute Engine network to which jobs and resources should be peered. E.g. "projects/12345/global/networks/myVPC". Private services access must already be configured for the network. If specified, all eligible jobs and resources created will be peered with this VPC.  
`service_account` | `str`  
Optional. The service account used to launch jobs and deploy models. Jobs that use service_account: BatchPredictionJob, CustomJob, PipelineJob, HyperparameterTuningJob, CustomTrainingJob, CustomPythonPackageTrainingJob, CustomContainerTrainingJob, ModelEvaluationJob.  
`api_endpoint` | `str`  
Optional. The desired API endpoint, e.g., us-central1-aiplatform.googleapis.com  
`api_key` | `str`  
Optional. The API key to use for service calls. NOTE: Not all services support API keys.  
`api_transport` | `str`  
Optional. The transport method which is either 'grpc' or 'rest'. NOTE: "rest" transport functionality is currently in a beta state (preview).  
  
### log
    
    
    log(
        *,
        pipeline_job: typing.Optional[
            google.cloud.aiplatform.pipeline_jobs.PipelineJob
        ] = None
    )

Log Vertex AI Resources to the current experiment run.
    
    
    aiplatform.start_run('my-run')
    my_job = aiplatform.PipelineJob(...)
    my_job.submit()
    aiplatform.log(my_job)
    

**Parameter**  
---  
**Name** | **Description**  
`pipeline_job` | `pipeline_jobs.PipelineJob`  
Optional. Vertex PipelineJob to associate to this Experiment Run.  
  
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
        credentials: typing.Optional[google.auth.credentials.Credentials] = None
    ) -> google.cloud.aiplatform.metadata.schema.google.artifact_schema.ExperimentModel

Saves a ML model into a MLMD artifact and log it to this ExperimentRun.

Supported model frameworks: sklearn, xgboost, tensorflow.

Example usage:
    
    
        model = LinearRegression()
        model.fit(X, y)
        aiplatform.init(
            project="my-project",
            location="my-location",
            staging_bucket="gs://my-bucket",
            experiment="my-exp"
        )
        with aiplatform.start_run("my-run"):
            aiplatform.log_model(model, "my-sklearn-model")
    

**Parameters**  
---  
**Name** | **Description**  
`model` | `Union["sklearn.base.BaseEstimator", "xgb.Booster", "tf.Module"]`  
Required. A machine learning model.  
`artifact_id` | `str`  
Optional. The resource id of the artifact. This id must be globally unique in a metadataStore. It may be up to 63 characters, and valid characters are `[a-z0-9_-]`. The first character cannot be a number or hyphen.  
`uri` | `str`  
Optional. A gcs directory to save the model file. If not provided, `gs://default-bucket/timestamp-uuid-frameworkName-model` will be used. If default staging bucket is not set, a new bucket will be created.  
`input_example` | `Union[list, dict, pd.DataFrame, np.ndarray]`  
Optional. An example of a valid model input. Will be stored as a yaml file in the gcs uri. Accepts list, dict, pd.DataFrame, and np.ndarray The value inside a list must be a scalar or list. The value inside a dict must be a scalar, list, or np.ndarray.  
`display_name` | `str`  
Optional. The display name of the artifact.  
`metadata_store_id` | `str`  
Optional. The <metadata_store_id> portion of the resource name with the format: projects/123/locations/us-central1/metadataStores/<metadata_store_id>/artifacts/<resource_id> If not provided, the MetadataStore's ID will be set to "default".  
`project` | `str`  
Optional. Project used to create this Artifact. Overrides project set in aiplatform.init.  
`location` | `str`  
Optional. Location used to create this Artifact. Overrides location set in aiplatform.init.  
`credentials` | `auth_credentials.Credentials`  
Optional. Custom credentials used to create this Artifact. Overrides credentials set in aiplatform.init.  
  
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
  
### save_model
    
    
    save_model(
        model: typing.Union[sklearn.base.BaseEstimator, xgb.Booster, tf.Module],
        artifact_id: typing.Optional[str] = None,
        *,
        uri: typing.Optional[str] = None,
        input_example: typing.Union[list, dict, pd.DataFrame, np.ndarray] = None,
        tf_save_model_kwargs: typing.Optional[typing.Dict[str, typing.Any]] = None,
        display_name: typing.Optional[str] = None,
        metadata_store_id: typing.Optional[str] = "default",
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        staging_bucket: typing.Optional[str] = None
    ) -> google.cloud.aiplatform.metadata.schema.google.artifact_schema.ExperimentModel

Saves a ML model into a MLMD artifact.

Supported model frameworks: sklearn, xgboost, tensorflow.

Example usage: aiplatform.init(project="my-project", location="my-location", staging_bucket="gs://my-bucket") model = LinearRegression() model.fit(X, y) aiplatform.save_model(model, "my-sklearn-model")

**Parameters**  
---  
**Name** | **Description**  
`model` | `Union["sklearn.base.BaseEstimator", "xgb.Booster", "tf.Module"]`  
Required. A machine learning model.  
`artifact_id` | `str`  
Optional. The resource id of the artifact. This id must be globally unique in a metadataStore. It may be up to 63 characters, and valid characters are `[a-z0-9_-]`. The first character cannot be a number or hyphen.  
`uri` | `str`  
Optional. A gcs directory to save the model file. If not provided, `gs://default-bucket/timestamp-uuid-frameworkName-model` will be used. If default staging bucket is not set, a new bucket will be created.  
`input_example` | `Union[list, dict, pd.DataFrame, np.ndarray]`  
Optional. An example of a valid model input. Will be stored as a yaml file in the gcs uri. Accepts list, dict, pd.DataFrame, and np.ndarray The value inside a list must be a scalar or list. The value inside a dict must be a scalar, list, or np.ndarray.  
`tf_save_model_kwargs` | `Dict[str, Any]`  
Optional. A dict of kwargs to pass to the model's save method. If saving a tf module, this will pass to "tf.saved_model.save" method. If saving a keras model, this will pass to "tf.keras.Model.save" method.  
`display_name` | `str`  
Optional. The display name of the artifact.  
`metadata_store_id` | `str`  
Optional. The <metadata_store_id> portion of the resource name with the format: projects/123/locations/us-central1/metadataStores/<metadata_store_id>/artifacts/<resource_id> If not provided, the MetadataStore's ID will be set to "default".  
`project` | `str`  
Optional. Project used to create this Artifact. Overrides project set in aiplatform.init.  
`location` | `str`  
Optional. Location used to create this Artifact. Overrides location set in aiplatform.init.  
`credentials` | `auth_credentials.Credentials`  
Optional. Custom credentials used to create this Artifact. Overrides credentials set in aiplatform.init.  
`staging_bucket` | `str`  
Optional. The staging bucket used to save the model. If not provided, the staging bucket set in aiplatform.init will be used. A staging bucket or uri is required for saving a model.  
  
### start_execution
    
    
    start_execution(
        *,
        schema_title: typing.Optional[str] = None,
        display_name: typing.Optional[str] = None,
        resource_id: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = None,
        schema_version: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        resume: bool = False,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None
    ) -> google.cloud.aiplatform.metadata.execution.Execution

Create and starts a new Metadata Execution or resumes a previously created Execution.

To start a new execution:
    
    
    with aiplatform.start_execution(schema_title='system.ContainerExecution', display_name='trainer) as exc:
      exc.assign_input_artifacts([my_artifact])
      model = aiplatform.Artifact.create(uri='gs://my-uri', schema_title='system.Model')
      exc.assign_output_artifacts([model])
    

To continue a previously created execution:
    
    
    with aiplatform.start_execution(resource_id='my-exc', resume=True) as exc:
        ...
    

**Parameters**  
---  
**Name** | **Description**  
`schema_title` | `str`  
Optional. schema_title identifies the schema title used by the Execution. Required if starting a new Execution.  
`resource_id` | `str`  
Optional. The <resource_id> portion of the Execution name with the format. This is globally unique in a metadataStore: projects/123/locations/us-central1/metadataStores/<metadata_store_id>/executions/<resource_id>.  
`display_name` | `str`  
Optional. The user-defined name of the Execution.  
`schema_version` | `str`  
Optional. schema_version specifies the version used by the Execution. If not set, defaults to use the latest version.  
`metadata` | `Dict`  
Optional. Contains the metadata information that will be stored in the Execution.  
`description` | `str`  
Optional. Describes the purpose of the Execution to be created.  
`metadata_store_id` | `str`  
Optional. The <metadata_store_id> portion of the resource name with the format: projects/123/locations/us-central1/metadataStores/<metadata_store_id>/artifacts/<resource_id> If not provided, the MetadataStore's ID will be set to "default".  
`project` | `str`  
Optional. Project used to create this Execution. Overrides project set in aiplatform.init.  
`location` | `str`  
Optional. Location used to create this Execution. Overrides location set in aiplatform.init.  
`credentials` | `auth_credentials.Credentials`  
Optional. Custom credentials used to create this Execution. Overrides credentials set in aiplatform.init.  
  
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
  
### start_upload_tb_log
    
    
    start_upload_tb_log(
        tensorboard_experiment_name: str,
        logdir: str,
        tensorboard_id: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        experiment_display_name: typing.Optional[str] = None,
        run_name_prefix: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        allowed_plugins: typing.Optional[typing.FrozenSet[str]] = None,
    )

Continues to listen for new data in the logdir and uploads when it appears.

Note that after calling `start_upload_tb_log()` your thread will kept alive even if an exception is thrown. To ensure the thread gets shut down, put any code after `start_upload_tb_log()` and before `end_upload_tb_log()` in a `try` statement, and call `end_upload_tb_log()` in `finally`.
    
    
    Sample usage:
    aiplatform.init(location='us-central1', project='my-project')
    aiplatform.start_upload_tb_log(tensorboard_id='123',tensorboard_experiment_name='my-experiment',logdir='my-logdir')
    
    try:
      # your code here
    finally:
      aiplatform.end_upload_tb_log()
    

**Parameters**  
---  
**Name** | **Description**  
`tensorboard_experiment_name` | `str`  
Required. Name of this tensorboard experiment. Unique to the given projects/{project}/locations/{location}/tensorboards/{tensorboard_id}.  
`logdir` | `str`  
Required. path of the log directory to upload  
`tensorboard_id` | `str`  
Optional. TensorBoard ID. If not set, tensorboard_id in aiplatform.init will be used.  
`project` | `str`  
Optional. Project the TensorBoard is in. If not set, project set in aiplatform.init will be used.  
`location` | `str`  
Optional. Location the TensorBoard is in. If not set, location set in aiplatform.init will be used.  
`experiment_display_name` | `str`  
Optional. The display name of the experiment.  
`run_name_prefix` | `str`  
Optional. If present, all runs created by this invocation will have their name prefixed by this value.  
`description` | `str`  
Optional. String description to assign to the experiment.  
`allowed_plugins` | `FrozenSet[str]`  
Optional. List of additional allowed plugin names.  
  
### upload_tb_log
    
    
    upload_tb_log(
        tensorboard_experiment_name: str,
        logdir: str,
        tensorboard_id: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        experiment_display_name: typing.Optional[str] = None,
        run_name_prefix: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        verbosity: typing.Optional[int] = 1,
        allowed_plugins: typing.Optional[typing.FrozenSet[str]] = None,
    )

upload only the existing data in the logdir and then return immediately
    
    
    Sample usage:
    aiplatform.init(location='us-central1', project='my-project')
    aiplatform.upload_tb_log(tensorboard_id='123',tensorboard_experiment_name='my-experiment',logdir='my-logdir')
    

**Parameters**  
---  
**Name** | **Description**  
`tensorboard_experiment_name` | `str`  
Required. Name of this tensorboard experiment. Unique to the given projects/{project}/locations/{location}/tensorboards/{tensorboard_id}  
`logdir` | `str`  
Required. The location of the TensorBoard logs that resides either in the local file system or Cloud Storage  
`tensorboard_id` | `str`  
Optional. TensorBoard ID. If not set, tensorboard_id in aiplatform.init will be used.  
`project` | `str`  
Optional. Project the TensorBoard is in. If not set, project set in aiplatform.init will be used.  
`location` | `str`  
Optional. Location the TensorBoard is in. If not set, location set in aiplatform.init will be used.  
`experiment_display_name` | `str`  
Optional. The display name of the experiment.  
`run_name_prefix` | `str`  
Optional. If present, all runs created by this invocation will have their name prefixed by this value.  
`description` | `str`  
Optional. String description to assign to the experiment.  
`verbosity` | `str`  
Optional. Level of verbosity, an integer. Supported value: 0 - No upload statistics is printed. 1 - Print upload statistics while uploading data (default).  
`allowed_plugins` | `FrozenSet[str]`  
Optional. List of additional allowed plugin names.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
