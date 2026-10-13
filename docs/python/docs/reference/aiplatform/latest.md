---
url: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/
title: Vertex AI SDK for Python \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:59:09.143035+00:00
---

# Vertex AI SDK for Python  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Vertex AI SDK for Python Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0  1.153.1  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.116.0  1.115.0  1.114.0  1.113.0  1.112.0  1.111.0  1.110.0  1.109.0  1.108.0  1.107.0  1.106.0  1.105.0  1.104.0  1.103.0  1.102.0  1.101.0  1.100.0  1.99.0  1.98.0  1.97.0  1.96.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.1  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.39.0  1.38.1  1.37.0  1.36.4  1.35.0  1.34.0  1.33.1  1.32.0  1.31.1  1.30.1  1.29.0  1.28.1  1.27.1  1.26.1  1.25.0  1.24.1  1.23.0  1.22.1  1.21.0  1.20.0  1.19.1  1.18.3  1.17.1  1.16.1  1.15.1  1.14.0  1.13.1  1.12.1  1.11.0  1.10.0  1.9.0  1.8.1  1.7.1  1.6.2  1.5.0  1.4.3  1.3.0  1.2.0  1.1.1  1.0.1  0.9.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1 

## Gemini API and Generative AI on Vertex AI

**NOTE** : For Gemini API and Generative AI on Vertex AI, please reference [Vertex Generative AI SDK for Python](https://cloud.google.com/vertex-ai/generative-ai/docs/reference/python/latest)

* * *

[![image](https://img.shields.io/badge/support-ga-gold.svg)](https://github.com/googleapis/google-cloud-python/blob/main/README.rst#general-availability) [![image](https://img.shields.io/pypi/v/google-cloud-aiplatform.svg)](https://pypi.org/project/google-cloud-aiplatform/) [![image](https://img.shields.io/pypi/pyversions/google-cloud-aiplatform.svg)](https://pypi.org/project/google-cloud-aiplatform/) [![image](https://storage.googleapis.com/cloud-devrel-public/python-aiplatform/badges/sdk-unit-tests.svg)](https://storage.googleapis.com/cloud-devrel-public/python-aiplatform/badges/sdk-unit-tests.html) [![image](https://storage.googleapis.com/cloud-devrel-public/python-aiplatform/badges/sdk-system-tests.svg)](https://storage.googleapis.com/cloud-devrel-public/python-aiplatform/badges/sdk-system-tests.html) [![image](https://storage.googleapis.com/cloud-devrel-public/python-aiplatform/badges/sdk-sample-tests.svg)](https://storage.googleapis.com/cloud-devrel-public/python-aiplatform/badges/sdk-sample-tests.html)

[Vertex AI](https://cloud.google.com/vertex-ai/docs): Google Vertex AI is an integrated suite of machine learning tools and services for building and using ML models with AutoML or custom code. It offers both novices and experts the best workbench for the entire machine learning development lifecycle.

  * [Client Library Documentation](https://cloud.google.com/python/docs/reference/aiplatform/latest)

  * [Product Documentation](https://cloud.google.com/vertex-ai/docs)




## Quick Start

In order to use this library, you first need to go through the following steps:

  1. [Select or create a Cloud Platform project.](https://console.cloud.google.com/project)

  2. [Enable billing for your project.](https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project)

  3. [Enable the Vertex AI API.](https://cloud.google.com/vertex-ai/docs/start/use-vertex-ai-python-sdk)

  4. [Setup Authentication.](https://googleapis.dev/python/google-api-core/latest/auth.html)




### Installation

Install this library in a [virtualenv](https://virtualenv.pypa.io/en/latest/) using pip. [virtualenv](https://virtualenv.pypa.io/en/latest/) is a tool to create isolated Python environments. The basic problem it addresses is one of dependencies and versions, and indirectly permissions.

With [virtualenv](https://virtualenv.pypa.io/en/latest/), it’s possible to install this library without needing system install permissions, and without clashing with the installed system dependencies.

#### Mac/Linux
    
    
    pip install virtualenv
    virtualenv <your-env>
    source <your-env>/bin/activate
    <your-env>/bin/pip install google-cloud-aiplatform
    

#### Windows
    
    
    pip install virtualenv
    virtualenv <your-env>
    <your-env>\Scripts\activate
    <your-env>\Scripts\pip.exe install google-cloud-aiplatform
    

#### Supported Python Versions

Python >= 3.8

#### Deprecated Python Versions

Python <= 3.7.

The last version of this library compatible with Python 3.6 is google-cloud-aiplatform==1.12.1.

### Overview

This section provides a brief overview of the Vertex AI SDK for Python. You can also reference the notebooks in [vertex-ai-samples](https://github.com/GoogleCloudPlatform/vertex-ai-samples/tree/main/notebooks/community/sdk) for examples.

All publicly available SDK features can be found in the `google/cloud/aiplatform` directory. Under the hood, Vertex SDK builds on top of GAPIC, which stands for Google API CodeGen. The GAPIC library code sits in `google/cloud/aiplatform_v1` and `google/cloud/aiplatform_v1beta1`, and it is auto-generated from Google’s service proto files.

For most developers’ programmatic needs, they can follow these steps to figure out which libraries to import:

  1. Look through `google/cloud/aiplatform` first – Vertex SDK’s APIs will almost always be easier to use and more concise comparing with GAPIC

  2. If the feature that you are looking for cannot be found there, look through `aiplatform_v1` to see if it’s available in GAPIC

  3. If it is still in beta phase, it will be available in `aiplatform_v1beta1`




If none of the above scenarios could help you find the right tools for your task, please feel free to open a github issue and send us a feature request.

#### Importing

Vertex AI SDK resource based functionality can be used by importing the following namespace:
    
    
    from google.cloud import aiplatform
    

#### Initialization

Initialize the SDK to store common configurations that you use with the SDK.
    
    
    aiplatform.init(
        # your Google Cloud Project ID or number
        # environment default used is not set
        project='my-project',
    
        # the Vertex AI region you will use
        # defaults to us-central1
        location='us-central1',
    
        # Google Cloud Storage bucket in same region as location
        # used to stage artifacts
        staging_bucket='gs://my_staging_bucket',
    
        # custom google.auth.credentials.Credentials
        # environment default credentials used if not set
        credentials=my_credentials,
    
        # customer managed encryption key resource name
        # will be applied to all Vertex AI resources if set
        encryption_spec_key_name=my_encryption_key_name,
    
        # the name of the experiment to use to track
        # logged metrics and parameters
        experiment='my-experiment',
    
        # description of the experiment above
        experiment_description='my experiment description'
    )
    

#### Datasets

Vertex AI provides managed tabular, text, image, and video datasets. In the SDK, datasets can be used downstream to train models.

To create a tabular dataset:
    
    
    my_dataset = aiplatform.TabularDataset.create(
        display_name="my-dataset", gcs_source=['gs://path/to/my/dataset.csv'])
    

You can also create and import a dataset in separate steps:
    
    
    from google.cloud import aiplatform
    
    my_dataset = aiplatform.TextDataset.create(
        display_name="my-dataset")
    
    my_dataset.import_data(
        gcs_source=['gs://path/to/my/dataset.csv'],
        import_schema_uri=aiplatform.schema.dataset.ioformat.text.multi_label_classification
    )
    

To get a previously created Dataset:
    
    
    dataset = aiplatform.ImageDataset('projects/my-project/location/us-central1/datasets/{DATASET_ID}')
    

Vertex AI supports a variety of dataset schemas. References to these schemas are available under the `aiplatform.schema.dataset` namespace. For more information on the supported dataset schemas please refer to the [Preparing data docs](https://cloud.google.com/ai-platform-unified/docs/datasets/prepare).

#### Training

The Vertex AI SDK for Python allows you train Custom and AutoML Models.

You can train custom models using a custom Python script, custom Python package, or container.

**Preparing Your Custom Code**

Vertex AI custom training enables you to train on Vertex AI datasets and produce Vertex AI models. To do so your script must adhere to the following contract:

It must read datasets from the environment variables populated by the training service:
    
    
    os.environ['AIP_DATA_FORMAT']  # provides format of data
    os.environ['AIP_TRAINING_DATA_URI']  # uri to training split
    os.environ['AIP_VALIDATION_DATA_URI']  # uri to validation split
    os.environ['AIP_TEST_DATA_URI']  # uri to test split
    

Please visit [Using a managed dataset in a custom training application](https://cloud.google.com/vertex-ai/docs/training/using-managed-datasets) for a detailed overview.

It must write the model artifact to the environment variable populated by the training service:
    
    
    os.environ['AIP_MODEL_DIR']
    

**Running Training**
    
    
    job = aiplatform.CustomTrainingJob(
        display_name="my-training-job",
        script_path="training_script.py",
        container_uri="us-docker.pkg.dev/vertex-ai/training/tf-cpu.2-2:latest",
        requirements=["gcsfs==0.7.1"],
        model_serving_container_image_uri="us-docker.pkg.dev/vertex-ai/prediction/tf2-cpu.2-2:latest",
    )
    
    model = job.run(my_dataset,
                    replica_count=1,
                    machine_type="n1-standard-4",
                    accelerator_type='NVIDIA_TESLA_K80',
                    accelerator_count=1)
    

In the code block above my_dataset is managed dataset created in the Dataset section above. The model variable is a managed Vertex AI model that can be deployed or exported.

## AutoMLs

The Vertex AI SDK for Python supports AutoML tabular, image, text, video, and forecasting.

To train an AutoML tabular model:
    
    
    dataset = aiplatform.TabularDataset('projects/my-project/location/us-central1/datasets/{DATASET_ID}')
    
    job = aiplatform.AutoMLTabularTrainingJob(
      display_name="train-automl",
      optimization_prediction_type="regression",
      optimization_objective="minimize-rmse",
    )
    
    model = job.run(
        dataset=dataset,
        target_column="target_column_name",
        training_fraction_split=0.6,
        validation_fraction_split=0.2,
        test_fraction_split=0.2,
        budget_milli_node_hours=1000,
        model_display_name="my-automl-model",
        disable_early_stopping=False,
    )
    

## Models

To get a model:
    
    
    model = aiplatform.Model('/projects/my-project/locations/us-central1/models/{MODEL_ID}')
    

To upload a model:
    
    
    model = aiplatform.Model.upload(
        display_name='my-model',
        artifact_uri="gs://python/to/my/model/dir",
        serving_container_image_uri="us-docker.pkg.dev/vertex-ai/prediction/tf2-cpu.2-2:latest",
    )
    

To deploy a model:
    
    
    endpoint = model.deploy(machine_type="n1-standard-4",
                            min_replica_count=1,
                            max_replica_count=5
                            machine_type='n1-standard-4',
                            accelerator_type='NVIDIA_TESLA_K80',
                            accelerator_count=1)
    

Please visit [Importing models to Vertex AI](https://cloud.google.com/vertex-ai/docs/general/import-model) for a detailed overview:

## Model Evaluation

The Vertex AI SDK for Python currently supports getting model evaluation metrics for all AutoML models.

To list all model evaluations for a model:
    
    
    model = aiplatform.Model('projects/my-project/locations/us-central1/models/{MODEL_ID}')
    
    evaluations = model.list_model_evaluations()
    

To get the model evaluation resource for a given model:
    
    
    model = aiplatform.Model('projects/my-project/locations/us-central1/models/{MODEL_ID}')
    
    # returns the first evaluation with no arguments, you can also pass the evaluation ID
    evaluation = model.get_model_evaluation()
    
    eval_metrics = evaluation.metrics
    

You can also create a reference to your model evaluation directly by passing in the resource name of the model evaluation:
    
    
    evaluation = aiplatform.ModelEvaluation(
      evaluation_name='projects/my-project/locations/us-central1/models/{MODEL_ID}/evaluations/{EVALUATION_ID}')
    

Alternatively, you can create a reference to your evaluation by passing in the model and evaluation IDs:
    
    
    evaluation = aiplatform.ModelEvaluation(
      evaluation_name={EVALUATION_ID},
      model_id={MODEL_ID})
    

## Batch Prediction

To create a batch prediction job:
    
    
    model = aiplatform.Model('/projects/my-project/locations/us-central1/models/{MODEL_ID}')
    
    batch_prediction_job = model.batch_predict(
      job_display_name='my-batch-prediction-job',
      instances_format='csv',
      machine_type='n1-standard-4',
      gcs_source=['gs://path/to/my/file.csv'],
      gcs_destination_prefix='gs://path/to/my/batch_prediction/results/',
      service_account='my-sa@my-project.iam.gserviceaccount.com'
    )
    

You can also create a batch prediction job asynchronously by including the sync=False argument:
    
    
    batch_prediction_job = model.batch_predict(..., sync=False)
    
    # wait for resource to be created
    batch_prediction_job.wait_for_resource_creation()
    
    # get the state
    batch_prediction_job.state
    
    # block until job is complete
    batch_prediction_job.wait()
    

## Endpoints

To create an endpoint:
    
    
    endpoint = aiplatform.Endpoint.create(display_name='my-endpoint')
    

To deploy a model to a created endpoint:
    
    
    model = aiplatform.Model('/projects/my-project/locations/us-central1/models/{MODEL_ID}')
    
    endpoint.deploy(model,
                    min_replica_count=1,
                    max_replica_count=5,
                    machine_type='n1-standard-4',
                    accelerator_type='NVIDIA_TESLA_K80',
                    accelerator_count=1)
    

To get predictions from endpoints:
    
    
    endpoint.predict(instances=[[6.7, 3.1, 4.7, 1.5], [4.6, 3.1, 1.5, 0.2]])
    

To undeploy models from an endpoint:
    
    
    endpoint.undeploy_all()
    

To delete an endpoint:
    
    
    endpoint.delete()
    

## Pipelines

To create a Vertex AI Pipeline run and monitor until completion:
    
    
    # Instantiate PipelineJob object
    pl = PipelineJob(
        display_name="My first pipeline",
    
        # Whether or not to enable caching
        # True = always cache pipeline step result
        # False = never cache pipeline step result
        # None = defer to cache option for each pipeline component in the pipeline definition
        enable_caching=False,
    
        # Local or GCS path to a compiled pipeline definition
        template_path="pipeline.json",
    
        # Dictionary containing input parameters for your pipeline
        parameter_values=parameter_values,
    
        # GCS path to act as the pipeline root
        pipeline_root=pipeline_root,
    )
    
    # Execute pipeline in Vertex AI and monitor until completion
    pl.run(
      # Email address of service account to use for the pipeline run
      # You must have iam.serviceAccounts.actAs permission on the service account to use it
      service_account=service_account,
    
      # Whether this function call should be synchronous (wait for pipeline run to finish before terminating)
      # or asynchronous (return immediately)
      sync=True
    )
    

To create a Vertex AI Pipeline without monitoring until completion, use submit instead of run:
    
    
    # Instantiate PipelineJob object
    pl = PipelineJob(
        display_name="My first pipeline",
    
        # Whether or not to enable caching
        # True = always cache pipeline step result
        # False = never cache pipeline step result
        # None = defer to cache option for each pipeline component in the pipeline definition
        enable_caching=False,
    
        # Local or GCS path to a compiled pipeline definition
        template_path="pipeline.json",
    
        # Dictionary containing input parameters for your pipeline
        parameter_values=parameter_values,
    
        # GCS path to act as the pipeline root
        pipeline_root=pipeline_root,
    )
    
    # Submit the Pipeline to Vertex AI
    pl.submit(
      # Email address of service account to use for the pipeline run
      # You must have iam.serviceAccounts.actAs permission on the service account to use it
      service_account=service_account,
    )
    

## Explainable AI: Get Metadata

To get metadata in dictionary format from TensorFlow 1 models:
    
    
    from google.cloud.aiplatform.explain.metadata.tf.v1 import saved_model_metadata_builder
    
    builder = saved_model_metadata_builder.SavedModelMetadataBuilder(
              'gs://python/to/my/model/dir', tags=[tf.saved_model.tag_constants.SERVING]
          )
    generated_md = builder.get_metadata()
    

To get metadata in dictionary format from TensorFlow 2 models:
    
    
    from google.cloud.aiplatform.explain.metadata.tf.v2 import saved_model_metadata_builder
    
    builder = saved_model_metadata_builder.SavedModelMetadataBuilder('gs://python/to/my/model/dir')
    generated_md = builder.get_metadata()
    

To use Explanation Metadata in endpoint deployment and model upload:
    
    
    explanation_metadata = builder.get_metadata_protobuf()
    
    # To deploy a model to an endpoint with explanation
    model.deploy(..., explanation_metadata=explanation_metadata)
    
    # To deploy a model to a created endpoint with explanation
    endpoint.deploy(..., explanation_metadata=explanation_metadata)
    
    # To upload a model with explanation
    aiplatform.Model.upload(..., explanation_metadata=explanation_metadata)
    

## Cloud Profiler

Cloud Profiler allows you to profile your remote Vertex AI Training jobs on demand and visualize the results in Vertex AI Tensorboard.

To start using the profiler with TensorFlow, update your training script to include the following:
    
    
    from google.cloud.aiplatform.training_utils import cloud_profiler
    ...
    cloud_profiler.init()
    

Next, run the job with with a Vertex AI TensorBoard instance. For full details on how to do this, visit <https://cloud.google.com/vertex-ai/docs/experiments/tensorboard-overview>

Finally, visit your TensorBoard in your Google Cloud Console, navigate to the “Profile” tab, and click the Capture Profile button. This will allow users to capture profiling statistics for the running jobs.

### Next Steps

  * Read the [Client Library Documentation](https://cloud.google.com/python/docs/reference/aiplatform/latest) for Vertex AI API to see other available methods on the client.

  * Read the [Vertex AI API Product documentation](https://cloud.google.com/vertex-ai/docs) to learn more about the product and see How-to Guides.

  * View this [README](https://github.com/googleapis/google-cloud-python/blob/main/README.rst) to see the full list of Cloud APIs that we cover.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
