---
url: https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/getting-explanations/
title: Get explanations \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:54:10.639933+00:00
---

# Get explanations  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/getting-explanations/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)



Send feedback 

#  Get explanations Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Vertex Explainable AI is deprecated as of March 16, 2026. Access to Vertex Explainable AI will no longer be available on or after March 16, 2027. For more information, see the [deprecations](https://docs.cloud.google.com/vertex-ai/docs/deprecations) page. 

This guide describes how to get explanations from a `Model` resource on Vertex AI. You can get explanations in two ways:

  * **Online explanations:** Synchronous requests to the Vertex AI API, similar to [online inferences](https://docs.cloud.google.com/vertex-ai/docs/predictions/overview) that return inferences with feature attributions.

  * **Batch explanations:** Asynchronous requests to the Vertex AI API that return inferences with feature attributions. Batch explanations are an optional part of [batch inference requests](https://docs.cloud.google.com/vertex-ai/docs/predictions/overview).




## Before you begin

Before getting explanations, you must do the following:

  1. This step differs depending on what type of machine learning model you use:

     * **If you want to get explanations from a custom-trained model,** then follow either [Configuring example-based explanations](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/configuring-explanations-example-based) or [Configuring feature-based explanations](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/configuring-explanations-feature-based) to create a `Model` that supports Vertex Explainable AI.

     * **If you want to get explanations from an AutoML tabular classification or regression model,** then [train an AutoML model on a tabular dataset](https://docs.cloud.google.com/vertex-ai/docs/training/automl-console). There is no specific configuration required to use Vertex Explainable AI. Explanations for forecasting models aren't supported.

     * **If you want to get explanations from an AutoML image classification model,** then [train an AutoML model on an image dataset](https://docs.cloud.google.com/vertex-ai/docs/training/automl-console) and [enable explanations when you deploy the model](https://docs.cloud.google.com/vertex-ai/docs/predictions/deploy-model-console). There is no specific configuration required to use Vertex Explainable AI. Explanations for object detection models aren't supported.

  2. If you want to get online explanations, [deploy the `Model` that you created in the preceding step to an `Endpoint` resource](https://docs.cloud.google.com/vertex-ai/docs/predictions/deploy-model-console).




## Get online explanations

To get online explanations, follow most of the same steps that you would to get online inferences. However, instead of sending a [`projects.locations.endpoints.predict` request](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.endpoints/predict) to the Vertex AI API, send a [`projects.locations.endpoints.explain` request](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.endpoints/explain).

The following guides provide detailed instructions for preparing and sending online explanation requests:

  * **For AutoML image classification models,** read [Getting online inferences from AutoML models](https://docs.cloud.google.com/vertex-ai/docs/predictions/overview#get_predictions_from_models).

  * **For AutoML tabular classification and regression models,** read [Get inferences from AutoML models](https://docs.cloud.google.com/vertex-ai/docs/predictions/overview#get_predictions_from_models).

  * **For custom-trained models,** read [Getting online inferences from custom-trained models](https://docs.cloud.google.com/vertex-ai/docs/predictions/get-online-predictions).




## Get batch explanations

Only feature-based batch explanations are supported; you cannot get example-based batch explanations.

To get batch explanations, set the [`generateExplanation` field](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.batchPredictionJobs#BatchPredictionJob.FIELDS.generate_explanation) to `true` when you create a batch inference job.

For detailed instructions about preparing and creating batch prediction jobs, read [Getting batch inferences](https://docs.cloud.google.com/vertex-ai/docs/predictions/batch-predictions-automl).

## Get Concurrent Explanations

Explainable AI supports concurrent explanations. Concurrent explanations allow you to request both feature-based and example-based explanations from the same deployed model endpoint without having to deploy your model separately for each explanation method.

To get concurrent explanations, upload your model and configure either [example-based](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/configuring-explanations-example-based) or [feature-based](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/configuring-explanations-feature-based) explanations. Then, deploy your model as usual.

After the model is deployed, you can request the configured explanations as usual. Additionally, you can request concurrent explanations by specifying [`concurrent_explanation_spec_override`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.endpoints/explain#body.request_body.FIELDS.concurrent_explanation_spec_override).

Note the following when using concurrent explanations:

  * Concurrent explanations are available using only the `v1beta1` API version. If you're using the Vertex python SDK, you'll need to use the `preview` model to use concurrent explanations.
  * Example-based explanations cannot be requested after deploying with feature-based explanations. If you want both Example-based explanation and Feature-based explanations, deploy your model using Example-based explanations and request Feature-based using the concurrent explanation field.
  * Batch Explanations are not supported for Concurrent explanations. Online Explanations are the only way to use this feature.



## Troubleshooting

This section describes troubleshooting steps that you might find helpful if you run into problems with while getting explanations.

### Error: list index out of range

If you get the following error message when requesting explanations:
    
    
    "error": "Explainability failed with exception: listindex out of range"
    

Make sure that you are not passing an empty array into a field that expects an array of objects. For example, if `field1` accepts an array of objects, the following request body might result in an error:
    
    
    {
      "instances": [
        {
          "field1": [],
        }
      ]
    }
    

Instead, make sure the array is not empty, for example:
    
    
    {
      "instances": [
        {
          "field1": [
            {}
          ],
        }
      ]
    }
    

## What's next

  * Based on the explanations you receive, learn how to [adjust your `Model` to improve explanations](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improving-explanations).
  * [Try a sample notebook demonstrating Vertex Explainable AI on tabular data or image data](https://github.com/GoogleCloudPlatform/vertex-ai-samples/tree/main/notebooks/official/explainable_ai).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
