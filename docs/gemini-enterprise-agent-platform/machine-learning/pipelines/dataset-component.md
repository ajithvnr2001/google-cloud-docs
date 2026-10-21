---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/dataset-component/
title: Dataset components \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:16:34.239788+00:00
---

# Dataset components  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/dataset-component/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Dataset components Stay organized with collections  Save and categorize content based on your preferences. 

The dataset operators prepare the data for training an AutoML model in Gemini Enterprise Agent Platform. For more details about specific data type dataset information, see [Train and use your own models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training-overview). For information about AutoML training in Agent Platform, see the [AutoML training documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training-overview#automl). For information about Google Cloud Pipeline Components related to AutoML models and workflows, see [Gemini Enterprise Agent Platform AutoML components](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/vertex-automl-component).

The Google Cloud SDK includes the following operators related to AutoML `dataset` resource management:

  * [ `GetVertexDatasetOp` ](https://google-cloud-pipeline-components.readthedocs.io/en/google-cloud-pipeline-components-2.22.0/api/v1/dataset.html#v1.dataset.GetVertexDatasetOp)
  * [ `ImageDatasetCreateOp` ](https://google-cloud-pipeline-components.readthedocs.io/en/google-cloud-pipeline-components-2.22.0/api/v1/dataset.html#v1.dataset.ImageDatasetCreateOp)
  * [ `ImageDatasetExportDataOp` ](https://google-cloud-pipeline-components.readthedocs.io/en/google-cloud-pipeline-components-2.22.0/api/v1/dataset.html#v1.dataset.ImageDatasetExportDataOp)
  * [ `ImageDatasetImportDataOp` ](https://google-cloud-pipeline-components.readthedocs.io/en/google-cloud-pipeline-components-2.22.0/api/v1/dataset.html#v1.dataset.ImageDatasetImportDataOp)
  * [ `TabularDatasetCreateOp` ](https://google-cloud-pipeline-components.readthedocs.io/en/google-cloud-pipeline-components-2.22.0/api/v1/dataset.html#v1.dataset.TabularDatasetCreateOp)
  * [ `TabularDatasetExportDataOp` ](https://google-cloud-pipeline-components.readthedocs.io/en/google-cloud-pipeline-components-2.22.0/api/v1/dataset.html#v1.dataset.TabularDatasetExportDataOp)
  * [ `TextDatasetCreateOp` ](https://google-cloud-pipeline-components.readthedocs.io/en/google-cloud-pipeline-components-2.22.0/api/v1/dataset.html#v1.dataset.TextDatasetCreateOp)
  * [ `TextDatasetExportDataOp` ](https://google-cloud-pipeline-components.readthedocs.io/en/google-cloud-pipeline-components-2.22.0/api/v1/dataset.html#v1.dataset.TextDatasetExportDataOp)
  * [ `TextDatasetImportDataOp` ](https://google-cloud-pipeline-components.readthedocs.io/en/google-cloud-pipeline-components-2.22.0/api/v1/dataset.html#v1.dataset.TextDatasetImportDataOp)
  * [ `TimeSeriesDatasetCreateOp` ](https://google-cloud-pipeline-components.readthedocs.io/en/google-cloud-pipeline-components-2.22.0/api/v1/dataset.html#v1.dataset.TimeSeriesDatasetCreateOp)
  * [ `TimeSeriesDatasetExportDataOp` ](https://google-cloud-pipeline-components.readthedocs.io/en/google-cloud-pipeline-components-2.22.0/api/v1/dataset.html#v1.dataset.TimeSeriesDatasetExportDataOp)



## API reference

  * For dataset component reference, see the [Google Cloud SDK reference for Dataset components](https://google-cloud-pipeline-components.readthedocs.io/en/google-cloud-pipeline-components-2.22.0/api/v1/dataset.html).

  * For Agent Platform API reference, see the following API reference pages:

    * [`Dataset` resource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.datasets)

    * [`TrainingPipeline` resource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.trainingPipelines)




## Tutorials

  * [Learn how to use the Google Cloud pipeline components to train an image classification model using Gemini Enterprise Agent Platform AutoML.](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/pipelines/google_cloud_pipeline_components_automl_images.ipynb)
  * [Learn how to use the Google Cloud pipeline components to train a classification model using tabular data and Gemini Enterprise Agent Platform AutoML.](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/pipelines/automl_tabular_classification_beans.ipynb)
  * [Learn how to use the Google Cloud pipeline components to train a linear regression model using tabular data and Gemini Enterprise Agent Platform AutoML.](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/pipelines/google_cloud_pipeline_components_automl_tabular.ipynb)
  * [Learn how to use the Google Cloud pipeline components to train a text classification model using Gemini Enterprise Agent Platform AutoML.](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/pipelines/google_cloud_pipeline_components_automl_text.ipynb)
  * [Learn how to use the Google Cloud pipeline components to upload and deploy a model.](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/pipelines/google_cloud_pipeline_components_model_train_upload_deploy.ipynb)



## Version history and release notes

To learn more about the version history and changes to the Google Cloud Pipeline Components SDK, see the [Google Cloud Pipeline Components SDK Release Notes](https://google-cloud-pipeline-components.readthedocs.io/en/google-cloud-pipeline-components-2.22.0/release.html).

### Technical support contacts

If you have any questions, reach out to [kubeflow-pipelines-components@google.com](mailto:%20kubeflow-pipelines-components@google.com).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
