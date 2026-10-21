---
url: https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improving-explanations/
title: Improve feature-based explanations \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:59:40.732710+00:00
---

# Improve feature-based explanations  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improving-explanations/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)



Send feedback 

#  Improve feature-based explanations Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Vertex Explainable AI is deprecated as of March 16, 2026. Access to Vertex Explainable AI will no longer be available on or after March 16, 2027. For more information, see the [deprecations](https://docs.cloud.google.com/vertex-ai/docs/deprecations) page. 

When you are working with custom-trained models, you can configure specific parameters to improve your explanations. This guide describes how to inspect the explanations that you get from Vertex Explainable AI for error, and it describes how to adjust your Vertex Explainable AI configuration to mitigate error.

If you want to use Vertex Explainable AI with an AutoML tabular model, then you don't need to perform any configuration; Vertex AI automatically configures the model for Vertex Explainable AI. Skip this document and read [Getting explanations](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/getting-explanations).

The [Vertex Explainable AI feature attribution methods](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/overview#compare-methods) are all based on variants of Shapley values. Because Shapley values are computationally very expensive, Vertex Explainable AI provides approximations instead of the exact values.

You can reduce the approximation error and get closer to the exact values by changing the following inputs:

  * Increasing the number of integral steps or number of paths.
  * Changing the input baseline(s) you select.
  * Adding more input baselines. With the integrated gradients and XRAI methods, using additional baselines increases latency. Using additional baselines with the sampled Shapley method does not increase latency.



## Inspect explanations for error

After you have [requested and received explanations from Vertex Explainable AI](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/getting-explanations), you can check the explanations for approximation error. If the explanations have high approximation error, then the explanations might not be reliable. This section describes several ways to check for error.

### Check the `approximationError` field

For each [`Attribution`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.models.evaluations#attribution), Vertex Explainable AI returns approximation error in the `approximationError` field. If your approximation error exceeds 0.05, consider adjusting your Vertex Explainable AI configuration.

For the integrated gradients technique, we calculate the approximation error by comparing the sum of the feature attributions to the difference between the predicted values for the input score and the baseline score. For the integrated gradients technique, the feature attribution is an approximation of the integral of gradient values between the baseline and the input. We use the [Gaussian quadrature](https://en.wikipedia.org/wiki/Gaussian_quadrature) rule to approximate the integral because it is more accurate than Riemann Sum methods.

### Check the difference between inferences and baseline output

For each [`Attribution`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.models.evaluations#attribution), Vertex Explainable AI returns an `instanceOutputValue`, which represents the part of the inference output that feature attributions are for, and a `baselineOutputValue`, which represents what this part of the inference output would be if the inference was performed on an input baseline rather than the actual input instance.

If the difference between `instanceOutputValue` and `baselineOutputValue` is less than 0.05 for any attributions, then you might need to change your input baselines.

## Adjust your configuration

The following sections describe ways to adjust your Vertex Explainable AI configuration to reduce error. To make any of the following changes, you must [configure a new `Model` resource with an updated `ExplanationSpec`](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/configuring-explanations) or [override the `ExplanationSpec` of your existing `Model`](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/configuring-explanations#override) by redeploying it to an `Endpoint` resource or by getting new batch inferences.

### Increase steps or paths

To reduce approximation error, you can increase:

  * the number of paths for sampled Shapley ([`SampledShapleyAttribution.pathCount`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec#sampledshapleyattribution))
  * the number of integral steps for integrated gradients ([`IntegratedGradientsAttribution.stepCount`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec#integratedgradientsattribution)) or XRAI ([`XraiAttribution.stepCount`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec#xraiattribution))



### Adjust baselines

Input baselines represent a feature that provides no additional information. Baselines for tabular models can be median, minimum, maximum, or random values in relation to your training data. Similarly, for image models, your baselines can be a black image, a white image, a gray image, or an image with random pixel values.

When you configure Vertex Explainable AI, you can optionally specify the [`input_baselines` field](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec#inputmetadata). Otherwise, Vertex AI chooses input baselines for you. If you are encountering the problems described in previous sections of this guide, then you might want to adjust the `input_baselines` for each input of your `Model`.

In general:

  * Start with one baseline representing median values.
  * Change this baseline to one representing random values.
  * Try two baselines, representing the minimum and maximum values.
  * Add another baseline representing random values.



#### Example for tabular data

The following Python code creates a [`ExplanationMetadata` message](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec#explanationmetadata) for a hypothetical TensorFlow model trained on tabular data.

Notice that `input_baselines` is a list where you can specify multiple baselines. This example sets just one baseline. The baseline is a list of median values for the training data (`train_data` in this example).
    
    
    explanation_metadata = {
        "inputs": {
            "FEATURE_NAME": {
                "input_tensor_name": "INPUT_TENSOR_NAME",
                "input_baselines": [train_data.median().values.tolist()],
                "encoding": "bag_of_features",
                "index_feature_mapping": train_data.columns.tolist()
            }
        },
        "outputs": {
            "OUTPUT_NAME": {
                "output_tensor_name": "OUTPUT_TENSOR_NAME"
            }
        }
    }
    

See [Configuring explanations for custom-trained models](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/configuring-explanations) for more context on how to use this `ExplanationMetadata`

To set two baselines representing minimum and maximum values, set `input_baselines` as follows: `[train_data.min().values.tolist(), train_data.max().values.tolist()]`

#### Example for image data

The following Python code creates a [`ExplanationMetadata` message](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec#explanationmetadata) for a hypothetical TensorFlow model trained on image data.

Notice that `input_baselines` is a list where you can specify multiple baselines. This example sets just one baseline. The baseline is a list of random values. Using random values for an image baseline is a good approach if the images in your training dataset contain a lot of black and white.

Otherwise, set `input_baselines` to `[0, 1]` to represent black and white images.
    
    
    random_baseline = np.random.rand(192,192,3)
    
    explanation_metadata = {
        "inputs": {
            "FEATURE_NAME": {
                "input_tensor_name": "INPUT_TENSOR_NAME",
                "modality": "image",
                "input_baselines": [random_baseline.tolist()]
            }
        },
        "outputs": {
            "OUTPUT_NAME": {
                "output_tensor_name": "OUTPUT_TENSOR_NAME"
            }
        }
    }
    

## What's next

  * Follow the guide to [configuring explanations](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/configuring-explanations) to implement any configuration changes described on this page.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
