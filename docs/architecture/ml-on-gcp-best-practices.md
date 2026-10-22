---
url: https://docs.cloud.google.com/architecture/ml-on-gcp-best-practices/
title: Best practices for implementing machine learning on Google Cloud \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:33.655378+00:00
---

# Best practices for implementing machine learning on Google Cloud  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/ml-on-gcp-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Best practices for implementing machine learning on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-09-09 UTC

This document introduces best practices for implementing machine learning (ML) on Google Cloud, with a focus on custom-trained models based on your data and code. It provides recommendations on how to develop a custom-trained model throughout the ML workflow, including key actions and links for further reading.

The document describes these stages in the ML workflow:

  1. **ML development** : Design, experiment, and develop a model prototype to solve a business problem.
  2. **Data preparation** : Clean noise from raw data and engineer features to ensure the model receives high-quality, high-signal input.
  3. **ML training** : Run training scripts against a dataset to optimize model parameters and adjust hyperparameters until a performance metric meets your requirements.
  4. **Model deployment and serving** : Deploy the model to a production environment to provide user access through an API or container.
  5. **ML workflow orchestration** : Automate the end-to-end pipeline that schedules the ML workflow from data ingestion to deployment.
  6. **Artifact organization** : Log and version every dataset, model file, and configuration in a centralized registry.
  7. **Model monitoring** : Use dashboards to track the model's live performance and performance drift.



The document is not an exhaustive list of recommendations; its goal is to help data scientists and ML architects understand the scope of activities involved in using ML on Google Cloud and plan accordingly. And while ML development alternatives like [AutoML](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training-overview) are mentioned in [Use recommended tools and products](https://docs.cloud.google.com/architecture/ml-on-gcp-best-practices#use-recommended-tools-and-products), this document focuses primarily on custom-trained models.

Before following the best practices in this document, we recommend that you read [Introduction to Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning).

This document assumes the following:

  * You are primarily using Google Cloud services; hybrid and on-premises approaches are not addressed in this document.
  * You plan to collect training data and store it in Google Cloud.
  * You have an intermediate-level knowledge of ML, big data tools, and data preprocessing, as well as a familiarity with [Cloud Storage](https://docs.cloud.google.com/storage/docs), [BigQuery](https://docs.cloud.google.com/bigquery/docs), and [Google Cloud](https://cloud.google.com/training) fundamentals.



If you are new to ML, check out Google's [ML Crash Course](https://developers.google.com/machine-learning/crash-course).

## Use recommended tools and products

The following table lists recommended tools and products for each phase of the ML workflow as outlined in this document:

ML workflow step | Recommended tools and products  
---|---  
[ML environment setup](https://docs.cloud.google.com/architecture/ml-on-gcp-best-practices#machine-learning-environment-setup) | 

  * [Agent Platform SDK for Python](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/client-libraries#python)
  * [Colab Enterprise](https://docs.cloud.google.com/colab/docs/introduction)
  * [Gemini Enterprise Agent Platform Workbench instances](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/introduction)
  * [Terraform](https://www.terraform.io/)

  
[ML development](https://docs.cloud.google.com/architecture/ml-on-gcp-best-practices#machine-learning-development) | 

  * [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction)
  * [Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction)
  * [Agent Platform Workbench instances](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/introduction)
  * [Label data](https://docs.cloud.google.com/vertex-ai/docs/workbench/instances/introduction)
  * [Agent Platform Feature Store](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/overview)
  * [Vertex AI TensorBoard](https://docs.cloud.google.com/vertex-ai/docs/experiments/tensorboard-introduction)
  * [Gemini Enterprise Agent Platform Managed Training](https://docs.cloud.google.com/vertex-ai/docs/training/custom-training)
  * [Experiments on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/intro-vertex-ai-experiments)
  * [AutoML](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training-overview)
  * [Tabular Workflow for End-to-End AutoML](https://docs.cloud.google.com/vertex-ai/docs/tabular-data/tabular-workflows/e2e-automl)
  * [ML in BigQuery](https://docs.cloud.google.com/bigquery/docs/bqml-introduction)
  * [Vertex AI Vizier](https://docs.cloud.google.com/vertex-ai/docs/vizier/overview)

  
[Data preparation](https://docs.cloud.google.com/architecture/ml-on-gcp-best-practices#data-processing) | 

  * [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction)
  * [Dataflow (Apache Beam)](https://docs.cloud.google.com/dataflow/docs)
  * [Managed Service for Apache Spark (Apache Spark)](https://docs.cloud.google.com/dataproc/docs)
  * [Knowledge Catalog (Data Catalog)](https://docs.cloud.google.com/dataplex/docs/introduction)

  
[ML training](https://docs.cloud.google.com/architecture/ml-on-gcp-best-practices#operationalized-training) | 

  * [PyTorch](https://pytorch.org/tutorials/recipes/recipes/saving_and_loading_a_general_checkpoint.html)
  * [TensorFlow](https://www.tensorflow.org/overview)
  * [XGBoost](https://xgboost.readthedocs.io/stable/)
  * [scikit-learn](https://scikit-learn.org/stable/)
  * [Feature Store](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/overview)
  * [Gemini Enterprise Agent Platform Pipelines](https://docs.cloud.google.com/vertex-ai/docs/pipelines)
  * [Gemini Enterprise Agent Platform Managed Training](https://docs.cloud.google.com/vertex-ai/docs/training/create-model-custom-training)
  * [Model evaluation in Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/evaluation/introduction)

  
[Model deployment and serving](https://docs.cloud.google.com/architecture/ml-on-gcp-best-practices#model-deployment-and-serving) | 

  * [Gemini Enterprise Agent Platform Inference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/overview)
  * [Feature Store](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/overview)
  * [Agent Platform Vector Search](https://docs.cloud.google.com/vertex-ai/docs/vector-search/overview)
  * [Streaming import](https://docs.cloud.google.com/vertex-ai/docs/featurestore/ingesting-stream)
  * [Custom prediction routines](https://docs.cloud.google.com/vertex-ai/docs/predictions/custom-prediction-routines)
  * [VM cohosting](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/model-co-hosting)
  * [TensorFlow Enterprise](https://docs.cloud.google.com/tensorflow-enterprise/docs/overview)
  * [Manage BigQuery ML models](https://docs.cloud.google.com/bigquery/docs/create_vertex)

  
[ML workflow orchestration](https://docs.cloud.google.com/architecture/ml-on-gcp-best-practices#machine-learning-workflow-orchestration) | 

  * [Agent Platform Pipelines](https://docs.cloud.google.com/vertex-ai/docs/pipelines)

  
[Artifact organization](https://docs.cloud.google.com/architecture/ml-on-gcp-best-practices#artifact-organization) | 

  * [Vertex ML Metadata](https://docs.cloud.google.com/vertex-ai/docs/ml-metadata/introduction)
  * [Model Registry on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-registry/introduction)

  
[Model monitoring](https://docs.cloud.google.com/architecture/ml-on-gcp-best-practices#model-monitoring) | 

  * [Vertex Explainable AI](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/overview)
  * [Model Monitoring on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/overview)
  * [Model monitoring with BigQuery ML](https://docs.cloud.google.com/bigquery/docs/model-monitoring-overview)

  
Managed-open source platforms | 

  * [Ray on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/open-source/ray)

  
  
Google offers [AutoML](https://docs.cloud.google.com/vertex-ai/docs/start/automl-model-types), [forecasting with Agent Platform](https://docs.cloud.google.com/vertex-ai/docs/tabular-data/forecasting/overview), and [BigQuery ML](https://docs.cloud.google.com/bigquery/docs/bqml-introduction) as prebuilt training routine alternatives to Agent Platform custom-trained model solutions. The following table provides recommendations about when to use these options for Agent Platform.

ML environment |  Description |  Choose this environment if...  
---|---|---  
BigQuery ML |  BigQuery ML brings together data, infrastructure, and predefined model types into a single system. | 

  * All of your data is contained in BigQuery.
  * You are comfortable with SQL.
  * The set of [models available in BigQuery ML](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create#model_type) matches the problem you are trying to solve. 

  
AutoML (in the context of Agent Platform) |  AutoML provides training routines for common problems like image classification and tabular regression. Nearly all aspects of training and serving a model, like choosing an architecture, hyperparameter tuning, and provisioning machines, are handled for you. | 

  * Your data and problem match one of the formats with data types and model objectives that AutoML supports. The model can be served from Google Cloud or deployed to an external device. See [Train and use your own models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training-overview#automl) and [Training an AutoML Edge model using Google Cloud console](https://docs.cloud.google.com/vertex-ai/docs/training/automl-edge-console).
  * For text, video, or tabular models, your model can tolerate inference latencies > 100ms. You can also train AutoML tabular models from the [BigQuery ML](https://docs.cloud.google.com/bigquery/docs/bqml-introduction) environment. 

  
Agent Platform custom trained models |  Vertex lets you run your own custom training routines and deploy models of any type on serverless architecture. Agent Platform offers additional services, like hyperparameter tuning and monitoring, to make it easier to develop a model. See [Choose a custom training method](https://docs.cloud.google.com/vertex-ai/docs/training/custom-training-methods). | 

  * Your problem does not match the criteria listed in this table for BigQuery ML or AutoML.
  * You are already running training on-premises or on another cloud platform, and you need consistency across the platforms. 

  
  
## ML environment setup

We recommend that you use the following best practices when you set up your ML environment:

  * [Use Agent Platform Workbench instances for experimentation and development](https://docs.cloud.google.com/architecture/ml-on-gcp-best-practices#use-notebooks-for-experimentation-and-development).
  * [Create a Agent Platform Workbench instance for each team member](https://docs.cloud.google.com/architecture/ml-on-gcp-best-practices#create-a-notebooks-instance-for-each-team-member).
  * [Store your ML resources and artifacts based on your corporate policy](https://docs.cloud.google.com/architecture/ml-on-gcp-best-practices#store-ml-resources-and-artifacts).
  * [Use Agent Platform SDK for Python](https://docs.cloud.google.com/architecture/ml-on-gcp-best-practices#use-vertex-sdk-for-python).



### Use Agent Platform Workbench instances for experimentation and development

Regardless of your tooling, we recommend that you use [Agent Platform Workbench instances](https://docs.cloud.google.com/vertex-ai/docs/workbench/instances/introduction) for experimentation and development, including writing code, starting jobs, running queries, and checking status. Agent Platform Workbench instances let you access all of Google Cloud's data and AI services in a simple, reproducible way.

Agent Platform Workbench instances also give you a secure set of software and access patterns right out of the box. It is a common practice to customize Google Cloud properties like network and Identity and Access Management, and software (through a container) associated with a Agent Platform Workbench instance. For more information, see [Introduction to Agent Platform](https://docs.cloud.google.com/vertex-ai/docs/start/introduction-unified-platform) and [Introduction to Agent Platform Workbench instances](https://docs.cloud.google.com/vertex-ai/docs/workbench/instances/introduction).

Alternatively, you can use [Colab Enterprise](https://docs.cloud.google.com/colab/docs/introduction), which is a collaborative managed notebook environment that uses the security and compliance capabilities of Google Cloud.

### Create a Agent Platform Workbench instance for each team member

[Create a Agent Platform Workbench instance](https://docs.cloud.google.com/vertex-ai/docs/workbench/instances/create) for each member of your data science team. If a team member is involved in multiple projects, especially projects that have different dependencies, we recommend using multiple instances, treating each instance as a virtual workspace. Note that you can stop Agent Platform Workbench instances when they are not being used.

### Store your ML resources and artifacts based on your corporate policy

The simplest access control is to store both your raw and Agent Platform resources and artifacts, such as datasets and models, in the same Google Cloud project. More typically, your corporation has policies that control access. In cases where your resources and artifacts are stored across projects, you can configure your corporate cross-project access control with Identity and Access Management (IAM).

### Use Vertex AI SDK for Python

Use [Agent Platform SDK for Python](https://docs.cloud.google.com/vertex-ai/docs/python-sdk/use-vertex-ai-python-sdk-ref), a Pythonic way to use Agent Platform for your end-to-end model building workflows, which works seamlessly with your favorite ML frameworks including PyTorch, TensorFlow, XGBoost, and scikit-learn.

Alternatively, you can use the Google Cloud console, which supports the functionality of Agent Platform as a user interface through the browser.

## ML development

We recommend the following best practices for ML development:

**Best practices** : 

Prepare training data.  
Store structured and semi-structured data in BigQuery.  
Store image, video, audio and unstructured data on Cloud Storage.  
Use Agent Platform Feature Store with structured data.  
Use Vertex AI TensorBoard and Experiments on Gemini Enterprise Agent Platform for analyzing experiments.  
Train a model within a Agent Platform Workbench instance for small datasets.  
Maximize your model's predictive accuracy with hyperparameter tuning.  
Use a Agent Platform Workbench instance to understand your models.  
Use feature attributions to gain insights into model predictions.  


_ML development_ addresses preparing the data, experimenting, and evaluating the model. When solving a ML problem, it is typically necessary to build and compare many different models to figure out what works best.

Typically, data scientists train models using different architectures, input data sets, hyperparameters, and hardware. Data scientists evaluate the resulting models by looking at aggregate performance metrics like accuracy, precision, and recall on test datasets. Finally, data scientists evaluate the performance of the models against particular subsets of their data, different model versions, and different model architectures.

### Prepare training data

The data used to train a model can originate from any number of systems, for example, logs from an online service system, images from a local device, or documents scraped from the web.

Regardless of your data's origin, extract data from the source systems and convert to the format and storage (separate from the operational source) optimized for ML training. For more information on preparing training data for use with Agent Platform, see [Train and use your own models](https://docs.cloud.google.com/vertex-ai/docs/datasets/datasets).

### Store structured and semi-structured data in BigQuery

If you're working with structured or [semi-structured](https://en.wikipedia.org/wiki/Semi-structured_data) data, we recommend that you store all data in BigQuery, following [BigQuery's recommendation](https://docs.cloud.google.com/bigquery/docs/tables-intro) for project structure. In most cases, you can store intermediate, processed data in BigQuery as well. For maximum speed, it's better to store materialized data instead of using views or subqueries for training data.

Read data out of BigQuery using the BigQuery Storage API. For artifact tracking, consider using a managed tabular dataset. The following table lists Google Cloud tools that make it easier to use the API:

If you're using... |  Use this Google Cloud tool  
---|---  
TensorFlow for Keras |  [tf.data.dataset reader for BigQuery](https://towardsdatascience.com/how-to-read-bigquery-data-from-tensorflow-2-0-efficiently-9234b69165c8)  
TFX |  [BigQuery client](https://www.tensorflow.org/io/tutorials/bigquery)  
Dataflow |  [Google BigQuery I/O Connector](https://beam.apache.org/documentation/io/built-in/google-bigquery/)  
Any other framework (such as PyTorch, XGBoost, or scikit-learn) |  [Importing models in BigQuery](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-onnx)  
  
### Store image, video, audio and unstructured data on Cloud Storage

Store these data in large container formats on Cloud Storage. This applies to sharded TFRecord files if you're using TensorFlow, or Avro files if you're using any other framework.

Combine many individual images, videos, or audio clips into large files, as this will improve your read and write throughput to Cloud Storage. Aim for files of at least 100mb, and between 100 and 10,000 shards.

To enable data management, use Cloud Storage buckets and directories to group the shards. For more information, see [Product overview of Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction).

### Use data labeling services with the Google Cloud console

You can create and import training data through the Agent Platform page in the Google Cloud console. By using the [prompt and tuning](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning) capabilities of Gemini, you can manage text data with customized classification, entity extraction, and sentiment analysis. There are also data labeling solutions on the Google Cloud console Marketplace, such as [Labelbox](https://docs.cloud.google.com/architecture/partners/model-development-data-labeling-labelbox-google-cloud) and [Snorkel Flow](https://console.cloud.google.com/marketplace/browse).

### Use Agent Platform Feature Store with structured data

You can use [Feature Store](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/overview) to create, maintain, share, and serve ML features in a central location. It's optimized to serve workloads that need low latency, and lets you store feature data in a BigQuery table or view. To use Agent Platform Feature Store, you must create [an online store instance](https://docs.cloud.google.com/vertex-ai/docs/featurestore/latest/create-onlinestore) and define your feature views. BigQuery stores all the feature data, including historical feature data to allow you to work offline.

### Use Vertex AI TensorBoard and Experiments on Gemini Enterprise Agent Platform for analyzing experiments

When developing models, use [Vertex AI TensorBoard](https://docs.cloud.google.com/vertex-ai/docs/experiments/tensorboard-introduction) to visualize and compare specific experiments—for example, based on hyperparameters. Vertex AI TensorBoard is an enterprise-ready managed service with a cost-effective, secure solution that lets data scientists and ML researchers collaborate by making it seamless to track, compare, and share their experiments. Vertex AI TensorBoard enables tracking experiment metrics like loss and accuracy over time, visualizing the model graph, projecting embeddings to a lower dimensional space, and much more.

Use Experiments on Agent Platform to integrate with Vertex ML Metadata and to log and build linkage across parameters, metrics, and dataset and model artifacts.

### Train a model within a Agent Platform Workbench instance for small datasets

Training a model within the [Agent Platform Workbench instance](https://docs.cloud.google.com/vertex-ai/docs/workbench/instances/introduction) may be sufficient for small datasets, or subsets of a larger dataset. It may be helpful to use the training service for larger datasets or for distributed training. Using the [Gemini Enterprise Agent Platform Managed Training service](https://docs.cloud.google.com/vertex-ai/docs/training/create-model-custom-training) is also recommended to productionize training even on small datasets if the training is carried out on a schedule or in response to the arrival of additional data.

### Maximize your model's predictive accuracy with hyperparameter tuning

To maximize your model's predictive accuracy use hyperparameter tuning, the automated model enhancer provided by the [Gemini Enterprise Agent Platform Managed Training service](https://docs.cloud.google.com/vertex-ai/docs/training/create-model-custom-training) which takes advantage of the processing infrastructure of Google Cloud and [Vertex AI Vizier](https://docs.cloud.google.com/vertex-ai/docs/vizier/overview) to test different hyperparameter configurations when training your model. Hyperparameter tuning removes the need to manually adjust hyperparameters over the course of numerous training runs to arrive at the optimal values.

To learn more about hyperparameter tuning, see [Overview of hyperparameter tuning](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/hyperparameter-tuning-overview) and [Create a hyperparameter tuning job](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/using-hyperparameter-tuning).

### Use a Agent Platform Workbench instance to understand your models

Use a [Agent Platform Workbench instance](https://docs.cloud.google.com/vertex-ai/docs/workbench/instances/introduction) to evaluate and understand your models. In addition to built-in common libraries like scikit-learn, Agent Platform Workbench instances include the [What-if Tool (WIT)](https://www.youtube.com/watch?v=qTUUwfG1vSs) and [Language Interpretability Tool (LIT)](https://pair-code.github.io/lit/). WIT lets you interactively analyze your models for bias using multiple techniques, while LIT helps you understand natural language processing model behavior through a visual, interactive, and extensible tool.

### Use feature attributions to gain insights into model predictions

[Vertex Explainable AI](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/overview) is an integral part of the ML implementation process, offering feature attributions to provide insights into why models generate predictions. By detailing the importance of each feature that a model uses as input to make a prediction, Vertex Explainable AI helps you better understand your model's behavior and build trust in your models.

Vertex Explainable AI supports custom-trained models based on tabular and image data.

For more information about Vertex Explainable AI, see:

  * [Introduction to Vertex Explainable AI](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/overview)
  * [Improving explanations](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improving-explanations)
  * [Vertex Explainable AI code examples](https://github.com/GoogleCloudPlatform/vertex-ai-samples/tree/master/notebooks/official/explainable_ai)



## Data preparation

We recommend the following best practices for data preparation:

**Best practices** : 

Use BigQuery to process tabular data.  
Use Dataflow to process data.  
Use Managed Service for Apache Spark for serverless Spark data processing.  
Use managed datasets with Vertex ML Metadata. 

The recommended approach for processing your data depends on the framework and data types you're using. This section provides high-level recommendations for common scenarios.

### Use BigQuery to process structured and semi-structured data

Use BigQuery for storing unprocessed structured or semi-structured data. If you're building your model using [BigQuery ML](https://docs.cloud.google.com/bigquery/docs/managing-models-vertex), use the transformations built into BigQuery for preprocessing data. If you're using [AutoML](https://docs.cloud.google.com/vertex-ai/docs/start/automl-users), use the transformations built into AutoML for preprocessing data. If you're building a custom model, using the BigQuery transformations may be the most cost-effective method.

For large datasets, consider using partitioning in BigQuery. This practice can improve query performance and cost efficiency.

### Use Dataflow to process data

With large volumes of data, consider using [Dataflow](https://docs.cloud.google.com/dataflow/docs), which uses the [Apache Beam](https://beam.apache.org/) programming model. You can use Dataflow to convert the unstructured data into binary data formats like TFRecord, which can improve performance of data ingestion during the training process.

### Use Managed Service for Apache Spark for serverless Spark data processing

Alternatively, if your organization has an investment in an [Apache Spark](https://spark.apache.org/) codebase and skills, consider using [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs). Use one-off Python scripts for smaller datasets that fit into memory.

If you need to perform transformations that are not expressible in Cloud SQL or are for streaming, you can use a combination of Dataflow and the [pandas](https://pandas.pydata.org/) library.

### Use managed datasets with ML metadata

After your data is pre-processed for ML, you may want to consider using a managed dataset in Agent Platform. Managed datasets enable you to create a clear link between your data and custom-trained models, and provide descriptive statistics and automatic or manual splitting into train, test, and validation sets.

Managed datasets are not required; you may choose not to use them if you want more control over splitting your data in your training code, or if lineage between your data and model isn't critical to your application.

For more information, see [Datasets](https://docs.cloud.google.com/vertex-ai/docs/datasets/datasets) and [Using a managed dataset in a custom training application](https://docs.cloud.google.com/vertex-ai/docs/training/using-managed-datasets).

## ML training

We recommend the following best practices for ML training:

**Best practices** : 

Run your code in a managed service.  
Operationalize job execution with training pipelines.  
Use training checkpoints to save the current state of your experiment.  
Prepare model artifacts for serving in Cloud Storage.  
Regularly compute new feature values. 

In ML training, _operationalized training_ refers to the process of making model training repeatable by tracking repetitions, and managing performance. Although Agent Platform Workbench instances are convenient for iterative development on small datasets, we recommend that you operationalize your code to make it reproducible and able to scale to large datasets. In this section, we discuss tooling and best practices for operationalizing your training routines.

### Run your code in a managed service

We recommend that you run your code in either [Gemini Enterprise Agent Platform Managed Training service](https://docs.cloud.google.com/vertex-ai/docs/training/create-model-custom-training) or orchestrate with [Agent Platform Pipelines](https://docs.cloud.google.com/vertex-ai/docs/pipelines). Optionally, you can run your code directly in [Deep Learning VM Images](https://docs.cloud.google.com/deep-learning-vm/docs), [Deep Learning Containers](https://docs.cloud.google.com/deep-learning-containers/docs), or [Compute Engine](https://docs.cloud.google.com/compute). However, we advise against this approach if you are using features of Agent Platform such as automatic scaling and burst capability.

### Operationalize job execution with training pipelines

To operationalize training job execution on Agent Platform, you can create training pipelines. A training pipeline, which is different from a general ML pipeline, encapsulates training jobs. To learn more about training pipelines, see [Creating training pipelines](https://docs.cloud.google.com/vertex-ai/docs/training/create-training-pipeline) and [REST Resource: `projects.locations.trainingPipelines`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.trainingPipelines).

### Use training checkpoints to save the current state of your experiment

The ML workflow in this document assumes that you're not training interactively. If your model fails and isn't checkpointed, the training job or pipeline will finish and the data will be lost because the model isn't in memory. To prevent this scenario, make it a practice to always use training checkpoints to ensure you don't lose state.

We recommend that you save training checkpoints in Cloud Storage. Create a different folder for each experiment or training run.

To learn more about checkpoints, see [Training checkpoints](https://www.tensorflow.org/guide/checkpoint) for TensorFlow Core, [Saving and loading a General Checkpoint in PyTorch](https://pytorch.org/tutorials/recipes/recipes/saving_and_loading_a_general_checkpoint.html), and [ML Design Patterns](https://www.oreilly.com/library/view/machine-learning-design/9781098115777/).

### Prepare model artifacts for serving in Cloud Storage

For custom-trained models or custom containers, store your model artifacts in a Cloud Storage bucket, where the bucket's [region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) matches the regional endpoint you're using for production. See [Bucket regions](https://docs.cloud.google.com/storage/docs/locations) for more information.

Cloud Storage supports object versioning. To provide a mitigation against accidental data loss or corruption, enable object versioning in Cloud Storage.

Store your Cloud Storage bucket in the same Google Cloud project. If your Cloud Storage bucket is in a different Google Cloud project, you need to [grant Gemini Enterprise Agent Platform access](https://docs.cloud.google.com/vertex-ai/docs/general/access-control#foreign-project) to read your model artifacts.

If you're using a Gemini Enterprise Agent Platform prebuilt container, ensure that your model artifacts have filenames that exactly match these examples:

  * TensorFlow SavedModel: `saved_model.pb`
  * Scikit-learn: `model.joblib`
  * XGBoost: `model.bst`
  * PyTorch: `model.pth`



To learn how to save your model in the form of one or more model artifacts, see [Exporting model artifacts for prediction](https://docs.cloud.google.com/vertex-ai/docs/training/exporting-model-artifacts).

### Regularly compute new feature values

Often, a model will use a subset of features sourced from [Agent Platform Feature Store](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore). The features in Agent Platform Feature Store will already be ready for online serving. For any new features created by data scientist by sourcing data from the data lake, we recommend scheduling the corresponding data processing and feature engineering jobs (or ideally Dataflow) to regularly compute the new feature values at the required cadence, depending upon feature freshness needs, and ingesting them into Agent Platform Feature Store for online or batch serving.

## Model deployment and serving

We recommend the following best practices for model deployment and serving:

**Best practices** : 

Specify the number and types of machines you need.  
Plan inputs to the model.  
Turn on automatic scaling.  
[Monitor models by using BigQuery ML](https://docs.cloud.google.com/bigquery/docs/model-monitoring-overview). 

_Model deployment and serving_ refers to putting a model into production. The output of the training job is one or more model artifacts stored on Cloud Storage, which you can upload to Model Registry so the file can be used for prediction serving. There are two types of prediction serving: batch prediction is used to score batches of data at a regular cadence, and online prediction is used for near real-time scoring of data for live applications. Both approaches let you obtain predictions from trained models by passing input data to a cloud-hosted ML model and getting inferences for each data instance.To learn more, see [Getting batch predictions](https://docs.cloud.google.com/vertex-ai/docs/predictions/batch-predictions) and [Get online predictions from custom-trained models](https://docs.cloud.google.com/vertex-ai/docs/predictions/get-predictions#get_online_predictions).

To lower latency for peer-to-peer requests between the client and the model server, use [Agent Platform private endpoints](https://docs.cloud.google.com/vertex-ai/docs/predictions/using-private-endpoints). Private endpoints are particularly useful if your application that makes the prediction requests and the serving binary are within the same local network. You can avoid the overhead of internet routing and make a peer-to-peer connection using [Virtual Private Cloud](https://docs.cloud.google.com/vpc/docs/overview).

### Specify the number and types of machines you need

To deploy your model for prediction, choose hardware that is appropriate for your model, like different central processing unit (CPU) virtual machine (VM) types or graphics processing unit (GPU) types. For more information, see [Specifying machine types or scale tiers](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/configure-compute).

### Plan inputs to the model

In addition to deploying the model, you'll need to determine how you're going to pass inputs to the model. If you're using batch prediction you can fetch data from the data lake, or from the [Feature Store batch serving API](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1beta1/projects.locations.featurestores/batchReadFeatureValues). If you are using online prediction, you can send input instances to the service and it returns your predictions in the response. For more information, see [Response body details](https://docs.cloud.google.com/vertex-ai/docs/predictions/get-predictions#response-body-details).

If you are deploying your model for online prediction, you need a low latency, scalable way to serve the inputs or features that need to be passed to the model's endpoint. You can either do this by using one of the many [Database services on Google Cloud](https://cloud.google.com/products/databases), or you can use [Feature Store's online serving API](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1beta1/projects.locations.featurestores.entityTypes/readFeatureValues). The clients calling the online prediction endpoint can first call the feature serving solution to fetch the feature inputs, and then call the prediction endpoint with those inputs. You can serve multiple models to the same endpoint, for example, to gradually replace the model. Alternatively, you can deploy models to multiple endpoints,for example, in testing and production, by [sharing resources across deployments](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/model-co-hosting).

Streaming ingestion lets you make real-time updates to feature values. This method is useful when having the latest available data for online serving is a priority. For example, you can ingest streaming event data and, within a few seconds, [Feature Store streaming ingestion](https://docs.cloud.google.com/vertex-ai/docs/featurestore/ingesting-stream) makes that data available for online serving scenarios.

You can additionally customize the input (request) and output (response) handling and format to and from your model server by using [custom prediction routines](https://docs.cloud.google.com/vertex-ai/docs/predictions/custom-prediction-routines).

### Turn on automatic scaling

If you use the online prediction service, in most cases we recommend that you turn on automatic scaling by setting minimum and maximum nodes. For more information, see [Get predictions for a custom trained model](https://docs.cloud.google.com/vertex-ai/docs/predictions/get-predictions#deploy_a_model_to_an_endpoint). To ensure a high availability service level agreement (SLA), set automatic scaling with a minimum of two nodes.

To learn more about scaling options, see [Scaling ML predictions](https://cloud.google.com/blog/products/ai-machine-learning/scaling-machine-learning-predictions).

## ML workflow orchestration

We recommend the following best practices for ML workflow orchestration depending on your infrastructure and integration needs:

**Best practices** : 

Use Managed Service for Apache Airflow to orchestrate end-to-end enterprise MLOps and heterogeneous data workflows.  
Use Agent Platform to orchestrate serverless, container-native ML workflows.  
Use Kubeflow Pipelines for flexible ML pipeline construction within Agent Platform..  
Use Ray on Gemini Enterprise Agent Platform for distributed ML workflows. 

Google Cloud provides a comprehensive suite for ML workflow orchestration. For complex, end-to-end processes that span data engineering tasks such as [extract, load, and transform (ELT)](https://cloud.google.com/discover/what-is-elt), ML training, and external business systems, we recommend Managed Airflow as an enterprise orchestrator. For self-contained workflows that remain strictly within the Agent Platform ecosystem, Agent Platform Pipelines provides a serverless, fully managed service that lets you retrain your models as often as necessary. While retraining enables your models to adapt to changes and maintain performance over time, consider how much your data will change when choosing the optimal model retraining cadence.

ML orchestration workflows work best for customers who have already designed and built their model, put it into production, and want to automate their ML lifecycle. The code you use for experimentation will likely be useful for the rest of the ML workflow with some modification. To work with container-native ML workflows in Agent Platform Pipelines, you need to be fluent in Python, understand basic infrastructure like containers, and have ML knowledge. For broader orchestration without the need to manage custom containers for non-ML tasks, Managed Airflow offers over 1,000 prebuilt operators and an accessible, YAML-based configuration framework for Data Scientists.

### Use Managed Airflow for end-to-end Enterprise MLOps workflows

Although you can manually start each data process, training, evaluation, and deployment, we recommend that you use [Managed Airflow](https://docs.cloud.google.com/composer/docs/latest/composer-overview) to orchestrate the entire flow when your architecture spans heterogeneous systems. Managed Airflow is built on [Apache Airflow](https://airflow.apache.org/). Managed Airflow acts as a unified control plane, which lets you seamlessly integrate Google Cloud services (like BigQuery and Dataflow) with Agent Platform and third-party enterprise tools.

As an alternative to writing complex Airflow Python DAGs, you can use [Orchestration Pipelines](https://docs.cloud.google.com/orchestration-pipelines) to define your business logic and dependencies in concise YAML. This declarative approach drastically lowers the barrier to entry, which enables data scientists to seamlessly build and deploy multi-step pipelines without requiring deep Apache Airflow expertise. To learn more about MLOps on Orchestration Pipelines, see [From weeks to minutes: The new agentic era of data pipelines](https://cloud.google.com/blog/products/data-analytics/build-data-pipelines-in-less-time-with-data-agent-kit).

### Use Gemini Enterprise Agent Platform Pipelines for serverless workflows built into Agent Platform

If your workflows are entirely container-based and if they execute strictly within the Agent Platform ecosystem, we recommend that you use [Agent Platform Pipelines](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/introduction) to orchestrate the flow. For detailed information, see [MLOps level 1: ML pipeline automation](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning#mlops_level_1_ml_pipeline_automation). Agent Platform Pipelines provides serverless execution for DAGs that are generated by Kubeflow and TensorFlow Extended (TFX).

### Use Kubeflow Pipelines for flexible pipeline construction

We recommend the Kubeflow Pipelines SDK for most users who want to author managed pipelines for Agent Platform Pipelines. Kubeflow Pipelines is flexible, letting you use code to construct containerized pipelines. It also provides Google Cloud pipeline components, which lets you include Agent Platform functionality like AutoML in your pipeline. To learn more about Kubeflow Pipelines, see [Kubeflow Pipelines](https://www.kubeflow.org/docs/components/pipelines/) and [Agent Platform Pipelines](https://docs.cloud.google.com/vertex-ai/docs/pipelines).

### Use Ray on Gemini Enterprise Agent Platform for distributed ML workflows

Ray provides a general and unified distributed framework to scale machine learning workflows through a Python open-source, scalable, and distributed computing framework. This framework can help to solve the challenges that come from having a variety of distributed frameworks in your ML ecosystem, such as having to deal with multiple modes of task parallelism, scheduling, and resource management. You can use [Ray on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/open-source/ray) to develop applications on Agent Platform.

## Artifact organization

We recommend that you use the following best practices to organize your artifacts:

**Best practices** : 

Organize your ML model artifacts.  
Use a source control repository for pipeline definitions and training code. 

_Artifacts_ are outputs resulting from each step in the ML workflow. It's a best practice to organize them in a standardized way.

### Organize your ML model artifacts

Store your artifacts in these locations:

**Storage location** | **Artifacts**  
---|---  
Source control repository  | 

  * Gemini Enterprise Agent Platform Workbench instances
  * Pipeline source code
  * Preprocessing Functions
  * Model source code
  * Model training packages
  * Serving functions

  
Experiments and ML metadata  | 

  * Experiments
  * Parameters
  * Hyperparameters
  * Metaparameters
  * Metrics
  * Dataset artifacts
  * Model artifacts
  * Pipeline metadata

  
Model Registry  | 

  * Trained models

  
Artifact Registry  | 

  * Pipeline containers
  * Custom training environments
  * Custom prediction environments

  
Gemini Enterprise Agent Platform Inference  | 

  * Deployed models

  
  
### Use a source control repository for pipeline definitions and training code

You can use source control to version control your ML pipelines and the custom components you build for those pipelines. Use [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/docker/quickstart) to store, manage, and secure your Docker container images without making them publicly visible.

## Model monitoring

**Best practices** : 

Use skew and drift detection.  
Fine tune alert thresholds.  
Use feature attributions to detect data drift or skew.  
[Use BigQuery to support model monitoring](https://docs.cloud.google.com/bigquery/docs/model-monitoring-overview). 

Once you deploy your model into production, you need to monitor performance to ensure that the model is performing as expected. Gemini Enterprise Agent Platform provides two ways to monitor your ML models:

  * Skew detection: This approach looks for the degree of distortion between your model training and production data
  * Drift detection: In this type of monitoring, you're looking for drift in your production data. Drift occurs when the statistical properties of the inputs and the target, which the model is trying to predict, change over time in unforeseen ways. This causes problems because the predictions could become less accurate as time passes.



Model monitoring works for structured data, like numerical and categorical features, but not for unstructured data, like images. For more information, see [Monitoring models for feature skew or drift](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/overview).

### Use skew and drift detection

As much as possible, use skew detection because knowing that your production data has deviated from your training data is a strong indicator that your model isn't performing as expected in production. For skew detection, set up the model monitoring job by providing a pointer to the training data that you used to train your model.

If you don't have access to the training data, turn on drift detection so that you'll know when the inputs change over time.

Use drift detection to monitor whether your production data is deviating over time. For drift detection, enable the features you want to monitor and the corresponding thresholds to trigger an alert.

### Fine tune alert thresholds

Tune the thresholds used for alerting so you know when skew or drift occurs in your data. Alert thresholds are determined by the use case, the user's domain expertise, and by initial model monitoring metrics. To learn how to use monitoring to create dashboards or configure alerts based on the metrics, see [Cloud monitoring metrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/monitoring-metrics).

### Use feature attributions to detect data drift or skew

You can use feature attributions in [Vertex Explainable AI](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/overview) to detect data drift or skew as an early indicator that model performance may be degrading. For example, if your model originally relied on five features to make predictions in your training and test data, but the model began to rely on entirely different features when it went into production, feature attributions would help you detect this degradation in model performance.

**Note:** You can use feature attributions to detect model degradation regardless of the type of feature your model takes as input.

This is particularly useful for complex feature types, like embeddings and time series, which are difficult to compare using traditional skew and drift methods. With Vertex Explainable AI, feature attributions can indicate when model performance is degrading.

### Use BigQuery to support model monitoring

[BigQuery ML model monitoring](https://docs.cloud.google.com/bigquery/docs/model-monitoring-overview) is a set of tools and functionalities that helps you track and evaluate the performance of your ML models over time. Model monitoring is essential for maintaining model accuracy and reliability in real-world applications. We recommend that you monitor for the following issues:

  * **Data skew** : This issue happens when feature value distributions differ between training and serving data. Training statistics, which are saved during model training, enable skew detection without needing the original data.
  * **Data drift** : Real-world data often changes over time. Model monitoring helps you identify when the input data that your model sees in production (serving data) starts to differ significantly from the data that it was trained on (training data). This drift can lead to degraded performance.
  * **Advanced data skew or drift** : When you want fine-grained skew or drift statistics, monitor for advanced data skew or drift.



## What's next

  * [Agent Platform documentation](https://docs.cloud.google.com/vertex-ai/docs)
  * [Practitioners guide to Machine Learning Operations (MLOps): A framework for continuous delivery and automation of ML](https://cloud.google.com/resources/mlops-whitepaper)
  * For an overview of architectural principles and recommendations that are specific to AI and ML workloads in Google Cloud, see the [AI and ML perspective](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml) in the Well-Architected Framework. 
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-09-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-09-09 UTC."],[],[]] 
