---
url: https://docs.cloud.google.com/vertex-ai/docs/tabular-data/tabular-workflows/tabnet-train/
title: Train a model with TabNet \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:31:22.342657+00:00
---

# Train a model with TabNet  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/tabular-data/tabular-workflows/tabnet-train/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)



Send feedback 

#  Train a model with TabNet Stay organized with collections  Save and categorize content based on your preferences. 

To see an example of how to train a model with TabNet, run the "Tabular Workflows: TabNet Pipeline" notebook in one of the following environments: 

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/tabular_workflows/tabnet_on_vertex_pipelines.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/vertex-ai/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fofficial%2Ftabular_workflows%2Ftabnet_on_vertex_pipelines.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Vertex AI Workbench](https://console.cloud.google.com/vertex-ai/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fofficial%2Ftabular_workflows%2Ftabnet_on_vertex_pipelines.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/tabular_workflows/tabnet_on_vertex_pipelines.ipynb)

This page shows you how to train a classification or regression model from a tabular dataset with the Tabular Workflow for TabNet.

Two versions of the Tabular Workflow for TabNet are available:

  * HyperparameterTuningJob searches for the best set of hyperparameter values to use for model training.
  * CustomJob lets you specify the hyperparameter values to use for model training. If you know exactly which hyperparameter values you need, specify them instead of searching for them and save on training resources.



To learn about the service accounts this workflow uses, see [Service accounts for Tabular Workflows](https://docs.cloud.google.com/vertex-ai/docs/tabular-data/tabular-workflows/service-accounts#fte-workflow).

## Workflow APIs

This workflow uses the following APIs:

  * Vertex AI
  * Dataflow
  * Compute Engine
  * Cloud Storage



## Train a model with HyperparameterTuningJob

The following sample code demonstrates how to run a HyperparameterTuningJob pipeline:
    
    
    pipeline_job = aiplatform.PipelineJob(
        ...
        template_path=template_path,
        parameter_values=parameter_values,
        ...
    )
    pipeline_job.run(service_account=SERVICE_ACCOUNT)
    

The optional `service_account` parameter in `pipeline_job.run()` lets you set the Vertex AI Pipelines service account to an account of your choice.

The pipeline and the parameter values are defined by the following function. The training data can be either a CSV file in Cloud Storage or a table in BigQuery.
    
    
    template_path, parameter_values =  automl_tabular_utils.get_tabnet_hyperparameter_tuning_job_pipeline_and_parameters(...)
    

The following is a subset of `get_tabnet_hyperparameter_tuning_job_pipeline_and_parameters` parameters:

Parameter name | Type | Definition  
---|---|---  
`data_source_csv_filenames` | String | A URI for a CSV stored in Cloud Storage.  
`data_source_bigquery_table_path` | String | A URI for a BigQuery table.  
`dataflow_service_account` | String | (Optional) Custom service account to run Dataflow jobs. The Dataflow job can be configured to use private IPs and a specific VPC subnet. This parameter acts as an override for the default Dataflow worker service account.  
`study_spec_parameters_override` | List[Dict[String, Any]] | (Optional) An override for tuning hyperparameters. This parameter can be empty or contain one or more of the possible hyperparameters. If a hyperparameter value is not set, Vertex AI uses the default tuning range for the hyperparameter.  
  
To configure the hyperparameters using the `study_spec_parameters_override` parameter, use Vertex AI's helper function `get_tabnet_study_spec_parameters_override`. The function has the following inputs:

  * `dataset_size_bucket`: A bucket for the dataset size 
    * 'small': < 1M rows
    * 'medium': 1M - 100M rows
    * 'large': > 100M rows
  * `training_budget_bucket`: A bucket for the training budget 
    * 'small': < $600
    * 'medium': $600 - $2400
    * 'large': > $2400
  * `prediction_type`: The desired inference type



The `get_tabnet_study_spec_parameters_override` function returns a list of hyperparameters and ranges.

The following is an example of how to use the `get_tabnet_study_spec_parameters_override` function:
    
    
    study_spec_parameters_override = automl_tabular_utils.get_tabnet_study_spec_parameters_override(
        dataset_size_bucket="small",
        prediction_type="classification",
        training_budget_bucket="small",
    )
    

## Train a model with CustomJob

The following sample code demonstrates how to run a CustomJob pipeline:
    
    
    pipeline_job = aiplatform.PipelineJob(
        ...
        template_path=template_path,
        parameter_values=parameter_values,
        ...
    )
    pipeline_job.run(service_account=SERVICE_ACCOUNT)
    

The optional `service_account` parameter in `pipeline_job.run()` lets you set the Vertex AI Pipelines service account to an account of your choice.

The pipeline and the parameter values are defined by the following function. The training data can be either a CSV file in Cloud Storage or a table in BigQuery.
    
    
    template_path, parameter_values = automl_tabular_utils.get_tabnet_trainer_pipeline_and_parameters(...)
    

The following is a subset of `get_tabnet_trainer_pipeline_and_parameters` parameters:

Parameter name | Type | Definition  
---|---|---  
`data_source_csv_filenames` | String | A URI for a CSV stored in Cloud Storage.  
`data_source_bigquery_table_path` | String | A URI for a BigQuery table.  
`dataflow_service_account` | String | (Optional) Custom service account to run Dataflow jobs. The Dataflow job can be configured to use private IPs and a specific VPC subnet. This parameter acts as an override for the default Dataflow worker service account.  
  
## What's next

Once you're ready to make inferences with your classification or regression model, you have two options:

  * [Make online (real-time) inferences using your model](https://docs.cloud.google.com/vertex-ai/docs/tabular-data/tabular-workflows/tabnet-online-predictions)
  * [Get batch inferences directly from your model](https://docs.cloud.google.com/vertex-ai/docs/tabular-data/tabular-workflows/tabnet-batch-predictions).
  * Learn about [pricing for model training](https://docs.cloud.google.com/vertex-ai/docs/tabular-data/tabular-workflows/pricing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
