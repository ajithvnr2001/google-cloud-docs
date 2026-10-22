---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/error-analysis/
title: Hello image data: Evaluating and analyzing model performance \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:22:18.713527+00:00
---

# Hello image data: Evaluating and analyzing model performance  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/error-analysis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Hello image data: Evaluating and analyzing model performance Stay organized with collections  Save and categorize content based on your preferences. 

Use the Google Cloud console to check your model performance. Analyze test errors to iteratively improve model quality by fixing data issues.

This tutorial has several pages:

  1. [Set up your project and environment.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl)

  2. [Create an image classification dataset, and import images.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/dataset)

  3. [Train an AutoML image classification model.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/training)

  4. Evaluate and analyze model performance. 

  5. [Deploy a model to an endpoint, and send a prediction.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/deploy-predict)

  6. [Clean up your project.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/cleanup)




Each page assumes that you have already performed the instructions from the previous pages of the tutorial.

## 1\. Understand AutoML model evaluation results

After training is completed, your model is automatically evaluated against the test data split. The corresponding evaluation results are presented by clicking the model's name from either the **Model Registry** page or the **Dataset** page.

From there, you can find the metrics to measure the model's performance.

![Evaluation page](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/images/eval-page.png)

You can find a more detailed introduction to different evaluation metrics in the [Evaluate, test, and deploy your model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/beginner/beginners-guide#evaluate_model) section.

## 2\. Analyze test results

If you want to continue improving the model performance, the first step is often to examine the error cases and investigate the potential causes. The evaluation page of each class presents detailed test images of the given class categorized as false negatives, false positives, and true positives. The definition of each category can be found in the [Evaluate, test, and deploy your model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/beginner/beginners-guide#evaluate_model) section.

For each image under every category, you can further check the prediction details by clicking the image and access the detailed analysis results. You will see the **Review similar images** panel on the right side of the page, where the closest samples from the training set are presented with distances measured in the feature space.

![Error_analysis page](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/images/error-analysis.png)

There are two types of data issues that you might want to pay attention:

  1. Label inconsistency. If a visually similar sample from the training set has different labels from the test sample, it's possible that one of them is incorrect, or that the subtle difference requires more data for the model to learn from, or that the current class labels are simply not accurate enough to describe the given sample. Reviewing similar images can help you get the label information accurate by either correcting the error cases or excluding the problematic sample from the test set. You can conveniently change the label of either the test image or training images on the **Review similar images** panel on the same page.

  2. Outliers. If a test sample is marked as an outlier, it's possible that there are no visually similar samples in the training set to help train the model. Reviewing similar images from the training set can help you identify these samples and add similar images into the training set to further improve the model performance on these cases.




## What's next

If you're happy with the model performance, follow the [next page of this tutorial](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/deploy-predict) to deploy your trained AutoML model to an endpoint and send an image to the model for prediction. Otherwise, if you make any corrections on the data, train a new model using the [Training an AutoML image classification model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/training) tutorial.

[ Previous arrow_back  Train an AutoML image classification model  ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/training)

[ Next Deploy a model to an endpoint and make an inference  arrow_forward  ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-automl/deploy-predict)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
