---
url: https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/configuring-explanations-feature-based/
title: Configure feature-based explanations \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:23:00.703754+00:00
---

# Configure feature-based explanations  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/configuring-explanations-feature-based/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)



Send feedback 

#  Configure feature-based explanations Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Vertex Explainable AI is deprecated as of March 16, 2026. Access to Vertex Explainable AI will no longer be available on or after March 16, 2027. For more information, see the [deprecations](https://docs.cloud.google.com/vertex-ai/docs/deprecations) page. 

To use Vertex Explainable AI with a custom-trained model, you must configure certain options when you create the `Model` resource that you plan to request explanations from, when you deploy the model, or when you submit a batch explanation job. This page describes configuring these options.

If you want to use Vertex Explainable AI with an AutoML tabular model, then you don't need to perform any configuration; Vertex AI automatically configures the model for Vertex Explainable AI. Skip this document and read [Getting explanations](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/getting-explanations).

## When and where to configure explanations

You configure explanations when you create or import a model. You can also configure explanations on a model that you have already created, even if you didn't configuring explanations previously.

### Configure explanations when creating or importing models

When you create or import a `Model`, you can set a default configuration for all its explanations using the `Model`'s [`explanationSpec` field](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.models#Model.FIELDS.explanation_spec).

You can create a custom-trained `Model` in Vertex AI in the following ways:

  * [Import or register a `Model` to the Vertex AI Model Registry](https://docs.cloud.google.com/vertex-ai/docs/model-registry/import-model)
  * [Create a custom `TrainingPipeline` resource that imports a `Model`.](https://docs.cloud.google.com/vertex-ai/docs/training/create-training-pipeline)
  * [Create a BigQuery ML model](https://docs.cloud.google.com/bigquery-ml/docs/create_vertex) and specify the optional `model_registry` setting in the `CREATE MODEL` syntax. This setting automatically registers the model to Vertex AI Model Registry and configures its `explanationSpec`.



In either case, you can configure the `Model` to support Vertex Explainable AI. The examples in this document assume that you are importing a `Model`. To configure Vertex Explainable AI when you create a custom-trained `Model` using a `TrainingPipeline`, use the configuration settings described in this document in the `TrainingPipeline`'s [`modelToUpload` field](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.trainingPipelines#TrainingPipeline.FIELDS.model_to_upload).

### Configure explanations when deploying models or getting batch inferences

When you [deploy a `Model` to an `Endpoint` resource](https://docs.cloud.google.com/vertex-ai/docs/predictions/deploy-model-api), you can either:

  * **Configure explanations** , whether or not the model was previously configured for explanations. This is useful if you didn't originally plan to get explanations (and omitted the `explanationSpec` field when you created the model), but decide later that you want explanations for the Model, or if you want to override some of the explanation settings.
  * **Disable explanations**. This is useful if your model is configured for explanations, but you don't plan to get explanations from the endpoint. To disable explanations when deploying the model to an endpoint, either clear the Explainability options in the Cloud Console or set [`DeployedModel.disableExplanations`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.endpoints#DeployedModel) to `true`.



Similarly, when you [get batch inferences from a `Model`](https://docs.cloud.google.com/vertex-ai/docs/predictions/batch-predictions#custom-trained), you can either configure explanations by populating the [`BatchPredictionJob.explanationSpec` field](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.batchPredictionJobs#BatchPredictionJob.FIELDS.explanation_spec) or disable explanations by setting `BatchPredictionJob.generateExplanation` to `false`.

### Override the configuration when getting online explanations

Regardless of whether you created or imported the `Model` with explanation settings, and regardless of whether you configured explanation settings during deployment, you can override the `Model`'s initial explanation settings when you [get online explanations](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/getting-explanations#getting_online_explanations).

When you send an `explain` request to Vertex AI, you can override some of the explanation configuration that you previously set for the `Model` or the `DeployedModel`.

In the `explain` request, you can override the following fields:

  * [Input baselines](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improving-explanations#baselines) for any custom-trained model
  * Visualization configuration for image models
  * [`ExplanationParameters`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec#ExplanationParameters) _except_ for the `method`



Override these settings in the explanation request's [explanationSpecOverride field](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.endpoints/explain#explanationspecoverride).

## Import a model with an `explanationSpec` field

Depending on whether you serve inferences using a [prebuilt container](https://docs.cloud.google.com/vertex-ai/docs/predictions/pre-built-containers) or a [custom container](https://docs.cloud.google.com/vertex-ai/docs/predictions/use-custom-container), specify slightly different details for the `ExplanationSpec`. Select the tab that matches the container that you are using:

### TensorFlow prebuilt container

You can use any of the following attribution methods for Vertex Explainable AI. Read the [comparison of feature attribution methods](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/overview#compare-methods) to select the appropriate one for your `Model`:

The following examples assume that your model accepts a single input feature; this is often the case for sequential Keras models and many other TensorFlow models. Since the feature is a tensor of any shape, it can in fact encode many pieces of information. When you [request explanations](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/getting-explanations), Vertex Explainable AI provides attributions for each element of the tensor.

If your model accepts multiple named input tensors, then add corresponding entries to the `inputs` metadata field.

For TensorFlow 2 models, [`ExplanationMetadata`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec#ExplanationMetadata) is optional. If omitted, Vertex AI automatically infers the values from the model and uses the tensor names as the feature names. This [notebook](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/explainable_ai/xai_image_classification_feature_attributions.ipynb) demonstrates how to import a model without `ExplanationMetadata`.

### Sampled Shapley

Depending on which tool you want to use to create or import the `Model`, select one of the following tabs:

### Console

Follow the guide to [importing a model using the Google Cloud console](https://docs.cloud.google.com/vertex-ai/docs/model-registry/import-model#import_a_model_using). When you get to the **Explainability** step, do the following:

  1. For your feature attribution method, select **Sampled Shapely (for tabular models)**.

  2. Set the path count to the [number of feature permutations](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec#sampledshapleyattribution) to use for the Sampled Shapley attribution method. This must be an integer in the range `[1, 50]`.

A higher value might [reduce approximation error](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improving-explanations) but is more computationally intensive. If you don't know what value to use, try `25`.

  3. Configure each input feature in your model:

**Note:** For Tensorflow 2 models, input feature name is optional. 

     1. Fill in your input feature name.

     2. Optionally, you can add one or more [input baselines](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improving-explanations#baselines). Otherwise, Vertex Explainable AI chooses a default input baseline of all-zero values, which is a black image for image data.

     3. If you're importing a TensorFlow model, there are additional input fields:

        1. Fill out the **Input tensor name**.

        2. If applicable, fill in the **Indices tensor name** and/or the **Dense shape tensor name**.

        3. The **Modality** cannot be updated here. It is set automatically to `NUMERIC` for tabular models, or `IMAGE` for image models.

        4. If applicable, set the **Encoding** field. This defaults to `IDENTITY` if not set.

        5. If applicable, set the **Group name** field.

  4. If you're importing a TensorFlow model, specify output fields:

     1. Set the **Output name** of your feature.
     2. Set the **Output tensor name** of your feature.
     3. If applicable, set the **Index display name mapping**.
     4. If applicable, set the **Display name mapping key**.
  5. Click the **Import** button when you have finished configuring the explainability settings. 




### gcloud

  1. For TensorFlow 2, `ExplanationMetadata` is optional. 

Write the following [`ExplanationMetadata`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec#explanationmetadata) to a JSON file in your local environment. The filename does not matter, but for this example call the file `explanation-metadata.json`:

#### `explanation-metadata.json`
         
         {
           "inputs": {
             "FEATURE_NAME": {
               "inputTensorName": "INPUT_TENSOR_NAME",
             }
           },
           "outputs": {
             "OUTPUT_NAME": {
               "outputTensorName": "OUTPUT_TENSOR_NAME"
             }
           }
         }
         

Replace the following:

     * FEATURE_NAME: Any memorable name for your input feature. 
     * INPUT_TENSOR_NAME: The name of the input tensor in TensorFlow. To find the correct value for this field, read [Using TensorFlow with Vertex Explainable AI](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/tensorflow). 
     * OUTPUT_NAME: Any memorable name for the output of your model. 
     * OUTPUT_TENSOR_NAME: The name of the output tensor in TensorFlow. To find the correct value for this field, read [Using TensorFlow with Vertex Explainable AI](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/tensorflow). 

You can optionally add [input baselines](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improving-explanations#baselines) to the `ExplanationMetadata`. Otherwise, Vertex AI chooses input baselines for the `Model`.

  2. Run the following command to create a `Model` resource that supports Vertex Explainable AI. The flags most pertinent to Vertex Explainable AI are highlighted. 
         
         gcloud ai models upload \
           --region=LOCATION \
           --display-name=MODEL_NAME \
           **--container-image-uri =IMAGE_URI** \
           --artifact-uri=PATH_TO_MODEL_ARTIFACT_DIRECTORY \
           **--explanation-method =sampled-shapley \
           --explanation-path-count=PATH_COUNT \
           --explanation-metadata-file=explanation-metadata.json**
         

Replace the following:

     * IMAGE_URI: The URI of a [TensorFlow pre-built container for serving predictions](https://docs.cloud.google.com/vertex-ai/docs/predictions/pre-built-containers#tensorflow). 
     * PATH_COUNT: The [number of feature permutations](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec#sampledshapleyattribution) to use for the Sampled Shapley attribution method. Must be an integer in the range `[1, 50]`.

A higher value might [reduce approximation error](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improving-explanations) but is more computationally intensive. If you don't know what value to use, try `25`.

To learn about appropriate values for the other placeholders, see [`upload`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.models/upload) and [Importing models](https://docs.cloud.google.com/vertex-ai/docs/general/import-model).




### REST

Before using any of the request data, make the following replacements: 

  * IMAGE_URI: The URI of a [TensorFlow pre-built container for serving predictions](https://docs.cloud.google.com/vertex-ai/docs/predictions/pre-built-containers#tensorflow). 
  * PATH_COUNT: The [number of feature permutations](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec#sampledshapleyattribution) to use for the Sampled Shapley attribution method. Must be an integer in the range `[1, 50]`.

A higher value might [reduce approximation error](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improving-explanations) but is more computationally intensive. If you don't know what value to use, try `25`.

  * FEATURE_NAME: Any memorable name for your input feature. 
  * INPUT_TENSOR_NAME: The name of the input tensor in TensorFlow. To find the correct value for this field, read [Using TensorFlow with Vertex Explainable AI](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/tensorflow). 
  * OUTPUT_NAME: Any memorable name for the output of your model. 
  * OUTPUT_TENSOR_NAME: The name of the output tensor in TensorFlow. To find the correct value for this field, read [Using TensorFlow with Vertex Explainable AI](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/tensorflow). 



To learn about appropriate values for the other placeholders, see [`upload`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.models/upload) and [Importing models](https://docs.cloud.google.com/vertex-ai/docs/general/import-model).

You can optionally add [input baselines](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improving-explanations#baselines) to the `ExplanationMetadata`. Otherwise, Vertex AI chooses input baselines for the `Model`.

For TensorFlow 2 models, the `metadata` field is optional. If omitted, Vertex AI automatically infers the `inputs` and `outputs` from the model.

HTTP method and URL: 
    
    
    POST https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/models:upload

Request JSON body: 
    
    
    {
      "model": {
        "displayName": "MODEL_NAME",
        "containerSpec": {
          **"imageUri": " IMAGE_URI"**
        },
        "artifactUri": "PATH_TO_MODEL_ARTIFACT_DIRECTORY",
        **"explanationSpec": {
          "parameters": {
            "sampledShapleyAttribution": {
              "pathCount": PATH_COUNT
            }
          },
          "metadata": {
            "inputs": {
              "FEATURE_NAME": {
                "inputTensorName": "INPUT_TENSOR_NAME",
              }
            },
            "outputs": {
              "OUTPUT_NAME": {
                "outputTensorName": "OUTPUT_TENSOR_NAME"
              }
            }
          }
        }**
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/models:upload"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/models:upload" | Select-Object -Expand Content

### Integrated Gradients

Depending on which tool you want to use to create or import the `Model`, select one of the following tabs:

### Console

Follow the guide to [importing a model using the Google Cloud console](https://docs.cloud.google.com/vertex-ai/docs/model-registry/import-model#import_a_model_using). When you get to the **Explainability** step, do the following:

  1. For your feature attribution method, select **Integrated gradients (for tabular models)** or **Integrated gradients (for image classification models)** , depending on which is more appropriate for your model.

  2. If you are importing an image classification model, do the following:

     1. Set the **Visualization type** and **Color map**.

     2. You can leave the **Clip below** , **Clip above** , **Overlay type** , and **Number of integral steps** at their default settings.

Learn more about [visualization settings](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/visualization-settings).

  3. Set the number of steps to use for approximating the path integral during feature attribution. This must be an integer in the range `[1, 100]`.

A higher value might [reduce approximation error](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improving-explanations) but is more computationally intensive. If you don't know what value to use, try `50`.

  4. Configure each input feature in your model:

**Note:** For Tensorflow 2 models, input feature name is optional. 

     1. Fill in your input feature name.

     2. Optionally, you can add one or more [input baselines](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improving-explanations#baselines). Otherwise, Vertex Explainable AI chooses a default input baseline of all-zero values, which is a black image for image data.

     3. If you're importing a TensorFlow model, there are additional input fields:

        1. Fill out the **Input tensor name**.

        2. If applicable, fill in the **Indices tensor name** and/or the **Dense shape tensor name**.

        3. The **Modality** cannot be updated here. It is set automatically to `NUMERIC` for tabular models, or `IMAGE` for image models.

        4. If applicable, set the **Encoding** field. This defaults to `IDENTITY` if not set.

        5. If applicable, set the **Group name** field.

  5. If you're importing a TensorFlow model, specify output fields:

     1. Set the **Output name** of your feature.
     2. Set the **Output tensor name** of your feature.
     3. If applicable, set the **Index display name mapping**.
     4. If applicable, set the **Display name mapping key**.
  6. Click the **Import** button when you have finished configuring the explainability settings. 




### gcloud

  1. For TensorFlow 2, `ExplanationMetadata` is optional. 

Write the following [`ExplanationMetadata`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec#explanationmetadata) to a JSON file in your local environment. The filename does not matter, but for this example call the file `explanation-metadata.json`:

#### `explanation-metadata.json`
         
         {
           "inputs": {
             "FEATURE_NAME": {
               "inputTensorName": "INPUT_TENSOR_NAME",
               "modality": "MODALITY",
               "visualization": VISUALIZATION_SETTINGS
             }
           },
           "outputs": {
             "OUTPUT_NAME": {
               "outputTensorName": "OUTPUT_TENSOR_NAME"
             }
           }
         }
         

Replace the following:

     * FEATURE_NAME: Any memorable name for your input feature. 
     * INPUT_TENSOR_NAME: The name of the input tensor in TensorFlow. To find the correct value for this field, read [Using TensorFlow with Vertex Explainable AI](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/tensorflow). 
     * MODALITY: `image` if the `Model` accepts images as input or `numeric` if the `Model` accepts tabular data as input. Defaults to `numeric`. 
     * VIZUALIZATION_OPTIONS: Options for visualizing explanations. To learn how to populate this field, read [Configuring visualization settings for image data](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/visualization-settings). 

If you omit the `modality` field or set the `modality` field to `numeric`, then omit the `visualization` field entirely.

     * OUTPUT_NAME: Any memorable name for the output of your model. 
     * OUTPUT_TENSOR_NAME: The name of the output tensor in TensorFlow. To find the correct value for this field, read [Using TensorFlow with Vertex Explainable AI](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/tensorflow). 

You can optionally add [input baselines](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improving-explanations#baselines) to the `ExplanationMetadata`. Otherwise, Vertex AI chooses input baselines for the `Model`.

  2. Run the following command to create a `Model` resource that supports Vertex Explainable AI. The flags most pertinent to Vertex Explainable AI are highlighted. 
         
         gcloud ai models upload \
           --region=LOCATION \
           --display-name=MODEL_NAME \
           **--container-image-uri =IMAGE_URI** \
           --artifact-uri=PATH_TO_MODEL_ARTIFACT_DIRECTORY \
           **--explanation-method =integrated-gradients \
           --explanation-step-count=STEP_COUNT \
           --explanation-metadata-file=explanation-metadata.json**
         

Replace the following:

     * IMAGE_URI: The URI of a [TensorFlow pre-built container for serving predictions](https://docs.cloud.google.com/vertex-ai/docs/predictions/pre-built-containers#tensorflow). 
     * STEP_COUNT: The number of steps to use for approximating the path integral during feature attribution. Must be an integer in the range `[1, 100]`. 

A higher value might [reduce approximation error](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improving-explanations) but is more computationally intensive. If you don't know what value to use, try `50`. 

To learn about appropriate values for the other placeholders, see [`upload`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.models/upload) and [Importing models](https://docs.cloud.google.com/vertex-ai/docs/general/import-model).

You can optionally add [flags to configure the SmoothGrad approximation of gradients](https://docs.cloud.google.com/sdk/gcloud/reference/ai/models/upload#--smooth-grad-noise-sigma).




### REST

Before using any of the request data, make the following replacements: 

  * IMAGE_URI: The URI of a [TensorFlow pre-built container for serving predictions](https://docs.cloud.google.com/vertex-ai/docs/predictions/pre-built-containers#tensorflow). 
  * STEP_COUNT: The number of steps to use for approximating the path integral during feature attribution. Must be an integer in the range `[1, 100]`. 

A higher value might [reduce approximation error](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improving-explanations) but is more computationally intensive. If you don't know what value to use, try `50`. 

  * FEATURE_NAME: Any memorable name for your input feature. 
  * INPUT_TENSOR_NAME: The name of the input tensor in TensorFlow. To find the correct value for this field, read [Using TensorFlow with Vertex Explainable AI](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/tensorflow). 
  * MODALITY: `image` if the `Model` accepts images as input or `numeric` if the `Model` accepts tabular data as input. Defaults to `numeric`. 
  * VIZUALIZATION_OPTIONS: Options for visualizing explanations. To learn how to populate this field, read [Configuring visualization settings for image data](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/visualization-settings). 

If you omit the `modality` field or set the `modality` field to `numeric`, then omit the `visualization` field entirely.

  * OUTPUT_NAME: Any memorable name for the output of your model. 
  * OUTPUT_TENSOR_NAME: The name of the output tensor in TensorFlow. To find the correct value for this field, read [Using TensorFlow with Vertex Explainable AI](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/tensorflow). 



To learn about appropriate values for the other placeholders, see [`upload`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.models/upload) and [Importing models](https://docs.cloud.google.com/vertex-ai/docs/general/import-model).

You can optionally add [input baselines](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improving-explanations#baselines) to the `ExplanationMetadata`. Otherwise, Vertex AI chooses input baselines for the `Model`.

You can optionally add [fields to configure the SmoothGrad approximation of gradients](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec#smoothgradconfig) to the `ExplanationParameters`.

For TensorFlow 2 models, the `metadata` field is optional. If omitted, Vertex AI automatically infers the `inputs` and `outputs` from the model.

HTTP method and URL: 
    
    
    POST https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/models:upload

Request JSON body: 
    
    
    {
      "model": {
        "displayName": "MODEL_NAME",
        "containerSpec": {
          **"imageUri": " IMAGE_URI"**
        },
        "artifactUri": "PATH_TO_MODEL_ARTIFACT_DIRECTORY",
        **"explanationSpec": {
          "parameters": {
            "integratedGradientsAttribution": {
              "stepCount": STEP_COUNT
            }
          },
          "metadata": {
            "inputs": {
              "FEATURE_NAME": {
                "inputTensorName": "INPUT_TENSOR_NAME",
                "modality": "MODALITY",
                "visualization": VISUALIZATION_SETTINGS
              }
            },
            "outputs": {
              "OUTPUT_NAME": {
                "outputTensorName": "OUTPUT_TENSOR_NAME"
              }
            }
          }
        }**
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/models:upload"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/models:upload" | Select-Object -Expand Content

### XRAI

Depending on which tool you want to use to create or import the `Model`, select one of the following tabs:

### Console

Follow the guide to [importing a model using the Google Cloud console](https://docs.cloud.google.com/vertex-ai/docs/model-registry/import-model#import_a_model_using). When you get to the **Explainability** step, do the following:

  1. For your feature attribution method, select **XRAI (for image classification models)**.

  2. Set the following visualization options:

     1. Set the **Color map**.

     2. You can leave the **Clip below** , **Clip above** , **Overlay type** , and **Number of integral steps** at their default settings.

Learn more about [visualization settings](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/visualization-settings).

  3. Set the number of steps to use for approximating the path integral during feature attribution. This must be an integer in the range `[1, 100]`.

A higher value might [reduce approximation error](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improving-explanations) but is more computationally intensive. If you don't know what value to use, try `50`.

  4. Configure each input feature in your model:

**Note:** For Tensorflow 2 models, input feature name is optional. 

     1. Fill in your input feature name.

     2. Optionally, you can add one or more [input baselines](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improving-explanations#baselines). Otherwise, Vertex Explainable AI chooses a default input baseline of all-zero values, which is a black image for image data.

     3. If you're importing a TensorFlow model, there are additional input fields:

        1. Fill out the **Input tensor name**.

        2. If applicable, fill in the **Indices tensor name** and/or the **Dense shape tensor name**.

        3. The **Modality** cannot be updated here. It is set automatically to `NUMERIC` for tabular models, or `IMAGE` for image models.

        4. If applicable, set the **Encoding** field. This defaults to `IDENTITY` if not set.

        5. If applicable, set the **Group name** field.

  5. If you're importing a TensorFlow model, specify output fields:

     1. Set the **Output name** of your feature.
     2. Set the **Output tensor name** of your feature.
     3. If applicable, set the **Index display name mapping**.
     4. If applicable, set the **Display name mapping key**.
  6. Click the **Import** button when you have finished configuring the explainability settings. 




### gcloud

  1. For TensorFlow 2, `ExplanationMetadata` is optional. 

Write the following [`ExplanationMetadata`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec#explanationmetadata) to a JSON file in your local environment. The filename does not matter, but for this example call the file `explanation-metadata.json`:

#### `explanation-metadata.json`
         
         {
           "inputs": {
             "FEATURE_NAME": {
               "inputTensorName": "INPUT_TENSOR_NAME",
               "modality": "image",
               "visualization": VISUALIZATION_SETTINGS
             }
           },
           "outputs": {
             "OUTPUT_NAME": {
               "outputTensorName": "OUTPUT_TENSOR_NAME"
             }
           }
         }
         

Replace the following:

     * FEATURE_NAME: Any memorable name for your input feature. 
     * INPUT_TENSOR_NAME: The name of the input tensor in TensorFlow. To find the correct value for this field, read [Using TensorFlow with Vertex Explainable AI](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/tensorflow). 
     * VIZUALIZATION_OPTIONS: Options for visualizing explanations. To learn how to populate this field, read [Configuring visualization settings for image data](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/visualization-settings). 
     * OUTPUT_NAME: Any memorable name for the output of your model. 
     * OUTPUT_TENSOR_NAME: The name of the output tensor in TensorFlow. To find the correct value for this field, read [Using TensorFlow with Vertex Explainable AI](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/tensorflow). 

You can optionally add [input baselines](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improving-explanations#baselines) to the `ExplanationMetadata`. Otherwise, Vertex AI chooses input baselines for the `Model`.

  2. Run the following command to create a `Model` resource that supports Vertex Explainable AI. The flags most pertinent to Vertex Explainable AI are highlighted. 
         
         gcloud ai models upload \
           --region=LOCATION \
           --display-name=MODEL_NAME \
           **--container-image-uri =IMAGE_URI** \
           --artifact-uri=PATH_TO_MODEL_ARTIFACT_DIRECTORY \
           **--explanation-method =xrai \
           --explanation-step-count=STEP_COUNT \
           --explanation-metadata-file=explanation-metadata.json**
         

Replace the following:

     * IMAGE_URI: The URI of a [TensorFlow pre-built container for serving predictions](https://docs.cloud.google.com/vertex-ai/docs/predictions/pre-built-containers#tensorflow). 
     * STEP_COUNT: The number of steps to use for approximating the path integral during feature attribution. Must be an integer in the range `[1, 100]`. 

A higher value might [reduce approximation error](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improving-explanations) but is more computationally intensive. If you don't know what value to use, try `50`. 

To learn about appropriate values for the other placeholders, see [`upload`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.models/upload) and [Importing models](https://docs.cloud.google.com/vertex-ai/docs/general/import-model).

You can optionally add [flags to configure the SmoothGrad approximation of gradients](https://docs.cloud.google.com/sdk/gcloud/reference/ai/models/upload#--smooth-grad-noise-sigma).




### REST

Before using any of the request data, make the following replacements: 

  * IMAGE_URI: The URI of a [TensorFlow pre-built container for serving predictions](https://docs.cloud.google.com/vertex-ai/docs/predictions/pre-built-containers#tensorflow). 
  * STEP_COUNT: The number of steps to use for approximating the path integral during feature attribution. Must be an integer in the range `[1, 100]`. 

A higher value might [reduce approximation error](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improving-explanations) but is more computationally intensive. If you don't know what value to use, try `50`. 

  * FEATURE_NAME: Any memorable name for your input feature. 
  * INPUT_TENSOR_NAME: The name of the input tensor in TensorFlow. To find the correct value for this field, read [Using TensorFlow with Vertex Explainable AI](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/tensorflow). 
  * VIZUALIZATION_OPTIONS: Options for visualizing explanations. To learn how to populate this field, read [Configuring visualization settings for image data](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/visualization-settings). 
  * OUTPUT_NAME: Any memorable name for the output of your model. 
  * OUTPUT_TENSOR_NAME: The name of the output tensor in TensorFlow. To find the correct value for this field, read [Using TensorFlow with Vertex Explainable AI](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/tensorflow). 



To learn about appropriate values for the other placeholders, see [`upload`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.models/upload) and [Importing models](https://docs.cloud.google.com/vertex-ai/docs/general/import-model).

You can optionally add [input baselines](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improving-explanations#baselines) to the `ExplanationMetadata`. Otherwise, Vertex AI chooses input baselines for the `Model`.

You can optionally add [fields to configure the SmoothGrad approximation of gradients](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec#smoothgradconfig) to the `ExplanationParameters`.

For TensorFlow 2 models, the `metadata` field is optional. If omitted, Vertex AI automatically infers the `inputs` and `outputs` from the model.

HTTP method and URL: 
    
    
    POST https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/models:upload

Request JSON body: 
    
    
    {
      "model": {
        "displayName": "MODEL_NAME",
        "containerSpec": {
          **"imageUri": " IMAGE_URI"**
        },
        "artifactUri": "PATH_TO_MODEL_ARTIFACT_DIRECTORY",
        **"explanationSpec": {
          "parameters": {
            "xraiAttribution": {
              "stepCount": STEP_COUNT
            }
          },
          "metadata": {
            "inputs": {
              "FEATURE_NAME": {
                "inputTensorName": "INPUT_TENSOR_NAME",
                "modality": "image",
                "visualization": VISUALIZATION_SETTINGS
              }
            },
            "outputs": {
              "OUTPUT_NAME": {
                "outputTensorName": "OUTPUT_TENSOR_NAME"
              }
            }
          }
        }**
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/models:upload"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/models:upload" | Select-Object -Expand Content

### scikit-learn and XGBoost prebuilt containers

If your `Model` accepts tabular data as input and serves predictions using a [pre-built scikit-learn or XGBoost container for prediction](https://docs.cloud.google.com/vertex-ai/docs/predictions/pre-built-containers), then you can configure it to use the [Sampled Shapley attribution method](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/overview#sampled-shapley) for explanations.

The following examples assume that your model accepts a single 2-D matrix as input; this is often the case for scikit-learn and XGBoost models. When you [request explanations](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/getting-explanations), Vertex Explainable AI provides attributions for each element of the input matrix.

Depending on which tool you want to use to create or import the `Model`, select one of the following tabs:

### Console

Follow the guide to [importing a model using the Google Cloud console](https://docs.cloud.google.com/vertex-ai/docs/model-registry/import-model#import_a_model_using). When you get to the **Explainability** step, do the following:

  1. For your feature attribution method, select **Sampled Shapely (for tabular models)**.

  2. Set the path count to the [number of feature permutations](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec#sampledshapleyattribution) to use for the Sampled Shapley attribution method. This must be an integer in the range `[1, 50]`.

A higher value might [reduce approximation error](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improving-explanations) but is more computationally intensive. If you don't know what value to use, try `25`.

  3. Configure each input feature in your model:

     1. Fill in your input feature name.

If your model artifacts do not include feature names, then Vertex AI is unable to map the specified input feature names to the model. In that case, you should provide only one input feature with any arbitrary, user-friendly name, such as `input_features`. In the explanation response, you will get an N dimensional list of attributions, where N is the number of features in the model and the elements in the list appear in the same order as the training dataset.

     2. Optionally, you can add one or more [input baselines](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improving-explanations#baselines). Otherwise, Vertex Explainable AI chooses a default input baseline of all-zero values, which is a black image for image data.

  4. Set the **Output name** of your feature.

  5. Click the **Import** button when you have finished configuring the explainability settings. 




### gcloud

  1. Write the following [`ExplanationMetadata`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec#explanationmetadata) to a JSON file in your local environment. The filename does not matter, but for this example call the file `explanation-metadata.json`:

#### `explanation-metadata.json`
         
         {
           "inputs": {
             "FEATURE_NAME": {
             }
           },
           "outputs": {
             "OUTPUT_NAME": {
             }
           }
         }
         

Replace the following:

     * FEATURE_NAME: Any memorable name for your input feature. 
     * OUTPUT_NAME: Any memorable name for the output of your model. 

If you specify [input baselines](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improving-explanations#baselines), make sure they match your model's input, usually a list of 2-D matrices. Otherwise, the default value for the input baseline is a 0-value 2-D matrix of the input shape.

  2. Run the following command to create a `Model` resource that supports Vertex Explainable AI. The flags most pertinent to Vertex Explainable AI are highlighted. 
         
         gcloud ai models upload \
           --region=LOCATION \
           --display-name=MODEL_NAME \
           **--container-image-uri =IMAGE_URI** \
           --artifact-uri=PATH_TO_MODEL_ARTIFACT_DIRECTORY \
           **--explanation-method =sampled-shapley \
           --explanation-path-count=PATH_COUNT \
           --explanation-metadata-file=explanation-metadata.json**
         

Replace the following:

     * IMAGE_URI: The URI of a [pre-built container for serving predictions](https://docs.cloud.google.com/vertex-ai/docs/predictions/pre-built-containers). 
     * PATH_COUNT: The [number of feature permutations](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec#sampledshapleyattribution) to use for the Sampled Shapley attribution method. Must be an integer in the range `[1, 50]`.

A higher value might [reduce approximation error](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improving-explanations) but is more computationally intensive. If you don't know what value to use, try `25`.

To learn about appropriate values for the other placeholders, see [`upload`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.models/upload) and [Importing models](https://docs.cloud.google.com/vertex-ai/docs/general/import-model).




### REST

Before using any of the request data, make the following replacements: 

  * IMAGE_URI: The URI of a [pre-built container for serving predictions](https://docs.cloud.google.com/vertex-ai/docs/predictions/pre-built-containers). 
  * PATH_COUNT: The [number of feature permutations](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec#sampledshapleyattribution) to use for the Sampled Shapley attribution method. Must be an integer in the range `[1, 50]`.

A higher value might [reduce approximation error](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improving-explanations) but is more computationally intensive. If you don't know what value to use, try `25`.

  * FEATURE_NAME: Any memorable name for your input feature. 
  * OUTPUT_NAME: Any memorable name for the output of your model. 



To learn about appropriate values for the other placeholders, see [`upload`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.models/upload) and [Importing models](https://docs.cloud.google.com/vertex-ai/docs/general/import-model).

If you specify [input baselines](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improving-explanations#baselines), make sure they match your model's input, usually a list of 2-D matrices. Otherwise, the default value for the input baseline is a 0-value 2-D matrix of the input shape.

HTTP method and URL: 
    
    
    POST https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/models:upload

Request JSON body: 
    
    
    {
      "model": {
        "displayName": "MODEL_NAME",
        "containerSpec": {
          **"imageUri": " IMAGE_URI"**
        },
      "artifactUri": "PATH_TO_MODEL_ARTIFACT_DIRECTORY",
      **"explanationSpec": {
        "parameters": {
          "sampledShapleyAttribution": {
            "pathCount": PATH_COUNT
          }
        },
        "metadata": {
           "inputs": {
             "FEATURE_NAME": {
             }
           },
           "outputs": {
             "OUTPUT_NAME": {
             }
           }
        }
      }**
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/models:upload"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/models:upload" | Select-Object -Expand Content

### Custom container

If your `Model` accepts tabular data as input and serves predictions using a [custom container](https://docs.cloud.google.com/vertex-ai/docs/predictions/use-custom-container), then you can configure it to use the [Sampled Shapley attribution method](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/overview#sampled-shapley) for explanations.

**Note:** The following instructions do not work if you are using any of Vertex AI's [pre-built containers for serving predictions](https://docs.cloud.google.com/vertex-ai/docs/predictions/pre-built-containers). You must use a custom container image that is not managed by Vertex AI and that meets the [custom container requirements](https://docs.cloud.google.com/vertex-ai/docs/predictions/custom-container-requirements).

Custom prediction servers must accept and return batch inference.

### Determining feature and output names

In the following steps, you must provide Vertex AI with the names of the features that your `Model` expects as input. You must also specify the key used for outputs in the `Model`'s predictions.

#### Determining feature names

If your `Model` expects each [input instance](https://docs.cloud.google.com/vertex-ai/docs/predictions/custom-container-requirements#request_requirements) to have certain top-level keys, then those keys are your feature names.

For example, consider a `Model` that expects each input instance to have the following format:
    
    
    {
      "length": <value>,
      "width": <value>
    }
    

In this case, the feature names are `length` and `width`. Even if the values of these fields contain nested lists or objects, `length` and `width` are the only keys you need for the following steps. When you [request explanations](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/getting-explanations), Vertex Explainable AI provides attributions for each nested element of your features.

If your `Model` expects unkeyed input, then Vertex Explainable AI considers the `Model` to have a single feature. You can use any memorable string for the feature name.

For example, consider a `Model` that expects each input instance to have the following format:
    
    
    [
      <value>,
      <value>
    ]
    

In this case, provide Vertex Explainable AI with a single feature name of your choosing, like `dimensions`.

**Note:** The following examples assume that your model has a single input feature. If your model has multiple features, as described in this section, then add corresponding entries to the `inputs` field.

#### Determining the output name

If your `Model` returns each [online prediction instance](https://docs.cloud.google.com/vertex-ai/docs/predictions/custom-container-requirements#response_requirements) with keyed output, then that key is your output name.

For example, consider a `Model` that returns each prediction in the following format:
    
    
    {
      "scores": <value>
    }
    

In this case, the output name is `scores`. If the value of the `scores` field is an array, then when you get explanations, Vertex Explainable AI returns feature attributions for the element with the highest value in each prediction. To configure Vertex Explainable AI to provide feature attributions for additional elements of the output field, you can specify the `topK` or `outputIndices` fields of [`ExplanationParameters`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec#explanationparameters). However, the examples in this document do not demonstrate these options.

If your `Model` returns unkeyed predictions, then you can use any memorable string for the output name. For example, this applies if your `Model` returns an array or a scalar for each prediction.

### Creating the `Model`

Depending on which tool you want to use to create or import the `Model`, select one of the following tabs:

### Console

Follow the guide to [importing a model using the Google Cloud console](https://docs.cloud.google.com/vertex-ai/docs/model-registry/import-model#import_a_model_using). When you get to the **Explainability** step, do the following:

  1. For your feature attribution method, select **Sampled Shapely (for tabular models)**.

  2. Set the path count to the [number of feature permutations](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec#sampledshapleyattribution) to use for the Sampled Shapley attribution method. This must be an integer in the range `[1, 50]`.

A higher value might [reduce approximation error](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improving-explanations) but is more computationally intensive. If you don't know what value to use, try `25`.

  3. Configure each input feature in your model:

     1. Fill in your input feature name.

If your model artifacts do not include feature names, then Vertex AI is unable to map the specified input feature names to the model. In that case, you should provide only one input feature with any arbitrary, user-friendly name, such as `input_features`. In the explanation response, you will get an N dimensional list of attributions, where N is the number of features in the model and the elements in the list appear in the same order as the training dataset.

     2. Optionally, you can add one or more [input baselines](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improving-explanations#baselines). Otherwise, Vertex Explainable AI chooses a default input baseline of all-zero values, which is a black image for image data.

  4. Set the **Output name** of your feature.

  5. Click the **Import** button when you have finished configuring the explainability settings. 




### gcloud

  1. Write the following [`ExplanationMetadata`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec#explanationmetadata) to a JSON file in your local environment. The filename does not matter, but for this example call the file `explanation-metadata.json`:

#### `explanation-metadata.json`
         
         {
           "inputs": {
             "FEATURE_NAME": {}
           },
           "outputs": {
             "OUTPUT_NAME": {}
           }
         }
         

Replace the following:

     * FEATURE_NAME: The name of the feature, as described in the "Determining feature names" section of this document. 
     * OUTPUT_NAME: The name of the output, as described in the "Determining the output name" section of this document. 

You can optionally add [input baselines](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improving-explanations#baselines) to the `ExplanationMetadata`. Otherwise, Vertex AI chooses input baselines for the `Model`.

If you specify [input baselines](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improving-explanations#baselines), make sure they match your model's input, usually a list of 2-D matrices. Otherwise, the default value for the input baseline is a 0-value 2-D matrix of the input shape.

  2. Run the following command to create a `Model` resource that supports Vertex Explainable AI. The flags most pertinent to Vertex Explainable AI are highlighted. 
         
         gcloud ai models upload \
           --region=LOCATION \
           --display-name=MODEL_NAME \
           --container-image-uri=IMAGE_URI \
           --artifact-uri=PATH_TO_MODEL_ARTIFACT_DIRECTORY \
           **--explanation-method =sampled-shapley \
           --explanation-path-count=PATH_COUNT \
           --explanation-metadata-file=explanation-metadata.json**
         

Replace the following:

     * PATH_COUNT: The [number of feature permutations](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec#sampledshapleyattribution) to use for the Sampled Shapley attribution method. Must be an integer in the range `[1, 50]`.

A higher value might [reduce approximation error](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improving-explanations) but is more computationally intensive. If you don't know what value to use, try `25`.

To learn about appropriate values for the other placeholders, see [`upload`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.models/upload) and [Importing models](https://docs.cloud.google.com/vertex-ai/docs/general/import-model).




### REST

Before using any of the request data, make the following replacements: 

  * PATH_COUNT: The [number of feature permutations](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec#sampledshapleyattribution) to use for the Sampled Shapley attribution method. Must be an integer in the range `[1, 50]`.

A higher value might [reduce approximation error](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improving-explanations) but is more computationally intensive. If you don't know what value to use, try `25`.

  * FEATURE_NAME: The name of the feature, as described in the "Determining feature names" section of this document. 
  * OUTPUT_NAME: The name of the output, as described in the "Determining the output name" section of this document. 



To learn about appropriate values for the other placeholders, see [`upload`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.models/upload) and [Importing models](https://docs.cloud.google.com/vertex-ai/docs/general/import-model).

You can optionally add [input baselines](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improving-explanations#baselines) to the `ExplanationMetadata`. Otherwise, Vertex AI chooses input baselines for the `Model`.

HTTP method and URL: 
    
    
    POST https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/models:upload

Request JSON body: 
    
    
    {
      "model": {
        "displayName": "MODEL_NAME",
        "containerSpec": {
          "imageUri": "IMAGE_URI"
        },
      "artifactUri": "PATH_TO_MODEL_ARTIFACT_DIRECTORY",
      **"explanationSpec": {
        "parameters": {
          "sampledShapleyAttribution": {
            "pathCount": PATH_COUNT
          }
        },
        "metadata": {
           "inputs": {
             "FEATURE_NAME": {}
           },
           "outputs": {
             "OUTPUT_NAME": {}
           }
        }
      }**
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/models:upload"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/models:upload" | Select-Object -Expand Content

## What's next

  * [Deploy your `Model` to an `Endpoint`](https://docs.cloud.google.com/vertex-ai/docs/predictions/overview#model_deployment) and [get explanations](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/getting-explanations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
