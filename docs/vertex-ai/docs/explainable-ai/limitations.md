---
url: https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/limitations/
title: Limitations of Vertex Explainable AI \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:03:53.043848+00:00
---

# Limitations of Vertex Explainable AI  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/limitations/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)



Send feedback 

#  Limitations of Vertex Explainable AI Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Vertex Explainable AI is deprecated as of March 16, 2026. Access to Vertex Explainable AI will no longer be available on or after March 16, 2027. For more information, see the [deprecations](https://docs.cloud.google.com/vertex-ai/docs/deprecations) page. 

As you consider the explanations returned from the service, you should keep in mind these high-level limitations.

## Meaning and scope of feature attributions

Consider the following when analyzing feature attributions provided by Vertex Explainable AI:

  * Each attribution only shows how much the feature affected the prediction for that particular example. A single attribution might not reflect the overall behavior of the model. To understand approximate model behavior on an entire dataset, aggregate attributions over the entire dataset.
  * The attributions depend entirely on the model and data used to train the model. They can only reveal the patterns the model found in the data, and can't detect any fundamental relationships in the data. The presence or absence of a strong attribution to a certain feature doesn't mean there is or is not a relationship between that feature and the target. The attribution merely shows that the model is or is not using the feature in its predictions.
  * Attributions alone can't tell if your model is fair, unbiased, or of sound quality. Carefully evaluate your training data and evaluation metrics in addition to the attributions.



## Improving feature attributions

When you are working with custom-trained models, you can configure specific parameters to improve your explanations. This section does not apply to AutoML models.

The following factors have the highest impact on feature attributions:

  * The attribution methods approximate the Shapley value. You can increase the precision of the approximation by:

    * Increasing the number of integral steps for the integrated gradients or XRAI methods.
    * Increasing the number of integral paths for the sampled Shapley method.

As a result, the attributions could change dramatically.

  * The attributions only express how much the feature affected the change in prediction value, relative to the baseline value. Be sure to choose a meaningful baseline, relevant to the question you're asking of the model. Attribution values and their interpretation might change significantly as you switch baselines.

  * For integrated gradients and XRAI, using two baselines can improve your results. For example, you can specify baselines that represent an entirely black image and an entirely white image.




Read more about [improving feature attributions](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improving-explanations).

## Limitations for image data

The two attribution methods that support image data are integrated gradients and XRAI.

Integrated gradients is a pixel-based attribution method that highlights important areas in the image regardless of contrast, making this method ideal for non-natural images such as X-rays. However, the granular output can make it difficult to assess the relative importance of areas. The default output highlights areas in the image that have high positive attributions by drawing outlines, but these outlines are not ranked and may span across objects.

XRAI works best on natural, higher-contrast images containing multiple objects. Because this method produces region-based attributions, it produces a smoother, more human-readable heatmap of regions that are most salient for a given image classification.

XRAI does _not_ work well on the following types of image input:

  * Low-contrast images that are all one shade, such as X-rays.
  * Very tall or very wide images, such as panoramas.
  * Very large images, which may slow down overall runtime.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
