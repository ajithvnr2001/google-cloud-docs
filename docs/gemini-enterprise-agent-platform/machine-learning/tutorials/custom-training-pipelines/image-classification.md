---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/custom-training-pipelines/image-classification/
title: Fine-tune an image classification model with custom data on Gemini Enterprise Agent Platform Pipelines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:40:59.023830+00:00
---

# Fine-tune an image classification model with custom data on Gemini Enterprise Agent Platform Pipelines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/custom-training-pipelines/image-classification/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Fine-tune an image classification model with custom data on Gemini Enterprise Agent Platform Pipelines Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to use Gemini Enterprise Agent Platform Pipelines to run an end-to-end ML workflow, including the following tasks:

  * Import and transform data.
  * Fine-tune an [image classification model from TFHub](https://tfhub.dev/s?module-type=image-classification) using the transformed data.
  * Import the trained model to Gemini Enterprise Agent Platform Model Registry.
  * **Optional** : Deploy the model for online serving with Vertex AI Inference.



## Before you begin

  1. Ensure that you've completed steps 1-3 in [Set up a project](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/cloud-environment#set_up_a_project).

  2. Create an isolated Python environment and install the [Agent Platform SDK for Python](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/install-sdk).

  3. Install the Kubeflow Pipelines SDK:
         
         python3 -m pip install "kfp<2.0.0" "google-cloud-aiplatform>=1.16.0" --upgrade --quiet
         




## Run the ML model training pipeline

The sample code does the following:

  * Loads components from a [component repository](https://github.com/GoogleCloudPlatform/vertex-ai-samples/tree/main/community-content/pipeline_components) to be used as pipeline building blocks.
  * Composes a pipeline by creating component tasks and passing data between them using arguments.
  * Submits the pipeline for execution on Gemini Enterprise Agent Platform Pipelines. See [Gemini Enterprise Agent Platform Pipelines pricing](https://cloud.google.com/products/gemini-enterprise-agent-platform/pricing#pipelines).



Copy the following sample code into your development environment and run it.

### Image classification
    
    
    # python3 -m pip install "kfp<2.0.0" "google-cloud-aiplatform>=1.16.0" --upgrade --quiet
    from kfp import components
    from kfp.v2 import dsl
    
    # %% Loading components
    upload_Tensorflow_model_to_Google_Cloud_Vertex_AI_op = components.load_component_from_url('https://raw.githubusercontent.com/GoogleCloudPlatform/vertex-ai-samples/399405402d95f4a011e2d2e967c96f8508ba5688/community-content/pipeline_components/google-cloud/Vertex_AI/Models/Upload_Tensorflow_model/component.yaml')
    deploy_model_to_endpoint_op = components.load_component_from_url('https://raw.githubusercontent.com/GoogleCloudPlatform/vertex-ai-samples/399405402d95f4a011e2d2e967c96f8508ba5688/community-content/pipeline_components/google-cloud/Vertex_AI/Models/Deploy_to_endpoint/component.yaml')
    transcode_imagedataset_tfrecord_from_csv_op = components.load_component_from_url('https://raw.githubusercontent.com/GoogleCloudPlatform/vertex-ai-samples/main/community-content/pipeline_components/image_ml_model_training/transcode_tfrecord_image_dataset_from_csv/component.yaml')
    load_image_classification_model_from_tfhub_op = components.load_component_from_url('https://raw.githubusercontent.com/GoogleCloudPlatform/vertex-ai-samples/b5b65198a6c2ffe8c0fa2aa70127e3325752df68/community-content/pipeline_components/image_ml_model_training/load_image_classification_model/component.yaml')
    preprocess_image_data_op = components.load_component_from_url('https://raw.githubusercontent.com/GoogleCloudPlatform/vertex-ai-samples/main/community-content/pipeline_components/image_ml_model_training/preprocess_image_data/component.yaml')
    train_tensorflow_image_classification_model_op = components.load_component_from_url('https://raw.githubusercontent.com/GoogleCloudPlatform/vertex-ai-samples/main/community-content/pipeline_components/image_ml_model_training/train_image_classification_model/component.yaml')
    
    
    # %% Pipeline definition
    def image_classification_pipeline():
        class_names = ['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips']
        csv_image_data_path = 'gs://cloud-samples-data/ai-platform/flowers/flowers.csv'
        deploy_model = False
    
        image_data = dsl.importer(
            artifact_uri=csv_image_data_path, artifact_class=dsl.[Dataset](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.types.Dataset.html)).output
    
        image_tfrecord_data = transcode_imagedataset_tfrecord_from_csv_op(
            csv_image_data_path=image_data,
            class_names=class_names
        ).outputs['tfrecord_image_data_path']
    
        loaded_model_outputs = load_image_classification_model_from_tfhub_op(
            class_names=class_names,
        ).outputs
    
        preprocessed_data = preprocess_image_data_op(
            image_tfrecord_data,
            height_width_path=loaded_model_outputs['image_size_path'],
        ).outputs
    
        trained_model = (train_tensorflow_image_classification_model_op(
            preprocessed_training_data_path = preprocessed_data['preprocessed_training_data_path'],
            preprocessed_validation_data_path = preprocessed_data['preprocessed_validation_data_path'],
            model_path=loaded_model_outputs['loaded_model_path']).
                       set_cpu_limit('96').
                       set_memory_limit('128G').
                       add_node_selector_constraint('cloud.google.com/gke-accelerator', 'NVIDIA_TESLA_A100').
                       set_gpu_limit('8').
                       outputs['trained_model_path'])
    
        vertex_model_name = upload_Tensorflow_model_to_Google_Cloud_Vertex_AI_op(
            model=trained_model,
        ).outputs['model_name']
    
        # Deploying the model might incur additional costs over time
        if deploy_model:
            vertex_endpoint_name = deploy_model_to_endpoint_op(
                model_name=vertex_model_name,
            ).outputs['endpoint_name']
    
    pipeline_func = image_classification_pipeline
    
    # %% Pipeline submission
    if __name__ == '__main__':
        from google.cloud import aiplatform
        aiplatform.[PipelineJob](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.types.PipelineJob.html).from_pipeline_func(pipeline_func=pipeline_func).submit()
    

Note the following about the sample code provided:

  * A Kubeflow pipeline is defined as a Python function.
  * The pipeline's workflow steps are created using Kubeflow pipeline components. By using the outputs of a component as an input of another component, you define the pipeline's workflow as a graph. For example, the `preprocess_image_data_op` component task depends on the `tfrecord_image_data_path` output from the `transcode_imagedataset_tfrecord_from_csv_op` component task.
  * You create a pipeline run on Gemini Enterprise Agent Platform Pipelines using the Agent Platform SDK for Python.



## Monitor the pipeline

In the Google Cloud console, in the Agent Platform section, go to the **Pipelines** page and open the **Runs** tab.

[Go to Pipeline runs](https://console.cloud.google.com/agent-platform/pipelines/runs)

## What's next

  * To learn more about Gemini Enterprise Agent Platform Pipelines, see [Introduction to Gemini Enterprise Agent Platform Pipelines](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/introduction).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
