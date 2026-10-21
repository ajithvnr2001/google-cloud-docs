---
url: https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/visualization-settings-automl-icn/
title: Configure visualization settings for AutoML image classification \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:47:51.331971+00:00
---

# Configure visualization settings for AutoML image classification  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/visualization-settings-automl-icn/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)



Send feedback 

#  Configure visualization settings for AutoML image classification Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Vertex Explainable AI is deprecated as of March 16, 2026. Access to Vertex Explainable AI will no longer be available on or after March 16, 2027. For more information, see the [deprecations](https://docs.cloud.google.com/vertex-ai/docs/deprecations) page. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Vertex Explainable AI provides built-in visualization capabilities for your image data. You can configure visualizations for AutoML image classification models.

When you request an explanation on an image classification model, you get the predicted class along with an image overlay showing which pixels (integrated gradients) or regions (integrated gradients or XRAI) contributed to the prediction.

The following images show visualizations on a husky image. The left visualization uses the integrated gradients method and highlights areas of positive attribution. The right visualization uses an XRAI method with a color gradient indicating areas of lesser (blue) and greater (yellow) influence in making a positive prediction.

![A feature attribution visualization of a husky using integrated
       gradients](https://docs.cloud.google.com/static/vertex-ai/docs/explainable-ai/images/husky_ig.jpg)![A feature attribution visualization of a husky using XRAI](https://docs.cloud.google.com/static/vertex-ai/docs/explainable-ai/images/husky_xrai.jpg)

The type of data you're working with can influence whether you use an integrated gradients or XRAI approach to visualizing your explanations.

  * XRAI tends to be better with natural images and provides a better high-level summary of insights, like showing that positive attribution is related to the shape of a dog's face.
  * Integrated gradients (IG) tends to provide details at the pixel level and is useful for uncovering more granular attributions.



Learn more about the attribution methods in the Vertex Explainable AI [Overview page](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/overview).

## Getting started

Configure visualization when you [train an AutoML model that supports Vertex Explainable AI](https://docs.cloud.google.com/vertex-ai/docs/training/automl-console) and [enable explanations when you deploy the model](https://docs.cloud.google.com/vertex-ai/docs/predictions/deploy-model-console).

## Visualization options

The default and recommended settings depend on the attribution method (integrated gradients or XRAI). The following list describes configuration options and how you might use them. For a full list of options, see the [API reference for the `Visualization` message](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec#visualization).

  * `type`: The type of visualization used: `OUTLINES` or `PIXELS`. Only specify this field if you are using integrated gradients; you can't specify it if you are using XRAI.

For integrated gradients, the field defaults to `OUTLINES`, which shows regions of attribution. To show per-pixel attribution, set the field to `PIXELS`.

  * `polarity`: The directionality of the highlighted attributions. `positive` is set by default, which highlights areas with the highest positive attributions. This means highlighting pixels that were most influential to the model's positive prediction. Setting polarity to `negative` highlights areas that lead the model to not predicting the positive class. Using a negative polarity can be useful for debugging your model by identifying false negative regions. You can also set polarity to `both` which shows positive and negative attributions.

  * `clip_percent_upperbound`: Excludes attributions above the specified percentile from the highlighted areas. Using the clip parameters together can be useful for filtering out noise and making it easier to see areas of strong attribution.

  * `clip_percent_lowerbound`: Excludes attributions below the specified percentile from the highlighted areas.

  * `color_map`: The color scheme used for the highlighted areas. Default is `pink_green` for integrated gradients, which shows positive attributions in green and negative in pink. For XRAI visualizations, the color map is a gradient. The XRAI default is `viridis` which highlights the most influential regions in yellow and the least influential in blue.

For a full list of possible values, see the [API reference for the `Visualization` message](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec#visualization).

  * `overlay_type`: How the original image is displayed in the visualization. Adjusting the overlay can help increase visual clarity if the original image makes it difficult to view the visualization.

For a full list of possible values, see the [API reference for the `Visualization` message](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec#visualization).




## Example configurations

To get started, here are sample `Visualization` configurations that you can use as a starting point and images that show a range of settings applied.

### Integrated gradients

For integrated gradients, you may need to adjust the clip values if the attribution areas are too noisy.
    
    
    visualization: {
      "type": "OUTLINES",
      "polarity": "positive",
      "clip_percent_lowerbound": 70,
      "clip_percent_upperbound": 99.9,
      "color_map": "pink_green",
      "overlay_type": "grayscale"
    }
    

The following are two visualizations using both the `outlines` and `pixels` types. The columns labeled "Highly predictive only," "Moderately predictive," and "Almost all" are examples of clipping at different levels that can help focus your visualization.

![A feature attribution viz with outlines for IG attribution](https://docs.cloud.google.com/static/vertex-ai/docs/explainable-ai/images/viz-ig-outlines.png)

![A feature attribution viz with pixels for IG attribution](https://docs.cloud.google.com/static/vertex-ai/docs/explainable-ai/images/viz-ig-pixels.png)

### XRAI

For XRAI visualizations, we recommend starting with no clip values for XRAI because the overlay uses a gradient to show areas of high and low attribution.
    
    
    visualization: {
      "clip_percent_lowerbound": 0,
      "clip_percent_upperbound": 100,
      "color_map": "viridis",
      "overlay_type": "grayscale"
    }
    

The following image is an XRAI visualization using the default viridis color map and a range of overlay types. The areas in yellow indicate the most influential regions that contributed positively to the prediction.

![A feature attribution visualization for XRAI attribution](https://docs.cloud.google.com/static/vertex-ai/docs/explainable-ai/images/viz-xrai.png)

## What's next

  * Use [Getting explanations](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/getting-explanations) to get predictions with explanations from your model.
  * For details about improving Vertex Explainable AI results for AutoML image classification models, read [Improving explanations](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/improve-explanations-automl-icn).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
