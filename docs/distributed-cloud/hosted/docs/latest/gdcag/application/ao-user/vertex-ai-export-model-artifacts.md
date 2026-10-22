---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-export-model-artifacts/
title: Export model artifacts for prediction \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:17.201019+00:00
---

# Export model artifacts for prediction  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-export-model-artifacts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Export model artifacts for prediction Stay organized with collections  Save and categorize content based on your preferences. 

**Preview:** Online Prediction is a Preview feature that is available as-is and is not recommended for production environments. Google provides no service-level agreements (SLA) or technical support commitments for Preview features. For more information, see GDC's [feature stages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/feature-stages).

Google Distributed Cloud (GDC) air-gapped offers [prebuilt containers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-online-predictions#available-container-images) to serve online predictions from models trained using the following machine learning (ML) frameworks:

  * TensorFlow
  * PyTorch



To use one of these prebuilt containers, you must save your model as one or more _model artifacts_ that comply with the requirements of the prebuilt container. These requirements apply whether or not your model artifacts are created on Distributed Cloud.

## Before you begin

Before exporting model artifacts, perform the following steps:

  1. Create and train a prediction model targeting one of the [supported containers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-online-predictions#available-container-images).
  2. If you don't have a project, [set up a project for Vertex AI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-set-up-project).
  3. Work with your Infrastructure Operator (IO) to [create the prediction cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/prediction-user-cluster).

The IO creates the cluster for you, associates it with your project, and assigns the appropriate node pools within the cluster, considering the resources you need for online predictions.

  4. [Create a storage bucket for your project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/create-storage-buckets).

  5. Create the Vertex AI Default Serving (`vai-default-serving-sa`) service account within your project. For information about service accounts, see [Set up service accounts](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-set-up-project#set-up-service).

  6. Grant the Project Bucket Object Viewer (`project-bucket-object-viewer`) role to the Vertex AI Default Serving (`vai-default-serving-sa`) service account for the storage bucket you created. For information about granting bucket access to service accounts, see [Grant bucket access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/grant-obtain-storage-access#grant_bucket_access).

  7. To get the permissions that you need to access Online Prediction, ask your IAM Project Admin to grant you the Vertex AI Prediction User (`vertex-ai-prediction-user`) role. For information about this role, see [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-ao-permissions).

  8. To get the permissions that you need to deploy Online Prediction models, ask your IAM Project Admin to grant you the Vertex AI Prediction Admin (`vertex-ai-prediction-Admin`) role. For information about this role, see [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-ao-permissions).




## Framework-specific requirements for exporting to prebuilt containers

Depending on [the ML framework you plan to use for prediction](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-online-predictions#available-container-images), you must export model artifacts in different formats. The following sections describe the acceptable model formats for each ML framework.

**Important:** To access the URLs listed on this page, you must connect to the internet. The URLs are provided to access outside of your air-gapped environment.

### TensorFlow

If you [use TensorFlow to train a model](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-online-predictions#tf), export your model as a [TensorFlow SavedModel directory](https://www.tensorflow.org/guide/saved_model).

There are several ways to export `SavedModels` from TensorFlow training code. The following list describes a few ways that work for various TensorFlow APIs:

  * If you use Keras for training, [use `tf.keras.Model.save` to export a SavedModel](https://www.tensorflow.org/guide/keras/save_and_serialize#whole-model_saving_loading).

  * If you use an Estimator for training, [use `tf.estimator.Estimator.export_saved_model` to export a SavedModel](https://www.tensorflow.org/guide/estimator#savedmodels_from_estimators).

  * Otherwise, [use `tf.saved_model.save`](https://www.tensorflow.org/guide/saved_model#saving_a_custom_model) or [use `tf.compat.v1.saved_model.SavedModelBuilder`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/builder).




If you are not using Keras or an Estimator, then make sure to [use the `serve` tag and `serving_default` signature when you export your SavedModel](https://www.tensorflow.org/tfx/serving/serving_basic#train_and_export_tensorflow_model) to ensure Vertex AI can use your model artifacts to serve predictions. Keras and Estimator handle this task automatically. Learn more about [specifying signatures during export](https://www.tensorflow.org/guide/saved_model#specifying_signatures_during_export).

To serve predictions using these artifacts, create a `Model` with the [prebuilt container for prediction](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-online-predictions#tf) matching the version of TensorFlow that you used for training.

### PyTorch

If you [use PyTorch to train a model](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-online-predictions#pt), you must package the model artifacts including either a [default](https://pytorch.org/serve/#default-handlers) or [custom](https://pytorch.org/serve/custom_service.html) handler by creating an archive file using [Torch model archiver](https://github.com/pytorch/serve/tree/master/model-archiver). The prebuilt PyTorch images expect the archive to be named `model.mar`, so make sure you set the model name to _model_.

For information about optimizing the memory usage, latency, or throughput of a PyTorch model served with TorchServe, see the [PyTorch performance guide](https://github.com/pytorch/serve/blob/master/docs/performance_guide.md).

## Upload your model

You must upload your model to the storage bucket you created. For more information about uploading objects to storage buckets, see [Upload and download storage objects in projects](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/upload-download-storage-objects).

The path to the storage bucket of your model must have the following structure:
    
    
    s3://BUCKET_NAME/MODEL_ID/MODEL_VERSION_ID
    

For export details, see the framework-specific requirements for exporting to prebuilt containers.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
