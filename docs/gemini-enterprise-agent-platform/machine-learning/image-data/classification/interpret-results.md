---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/image-data/classification/interpret-results/
title: Interpret prediction results from image classification models \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:45:54.166886+00:00
---

# Interpret prediction results from image classification models  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/image-data/classification/interpret-results/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Interpret prediction results from image classification models Stay organized with collections  Save and categorize content based on your preferences. 

After requesting a prediction, Gemini Enterprise Agent Platform returns results based on your model's objective. AutoML single-label image classification predictions return a single label category and its corresponding confidence score. Multi- label classification predictions return multiple label categories and their corresponding confidence scores. 

The confidence score communicates how strongly your model associates each class or label with a test item. The higher the number, the higher the model's confidence that the label should be applied to that item. You decide how high the confidence score must be for you to accept the model's results.

#### Score threshold slider

In the Google Cloud console, Gemini Enterprise Agent Platform provides a slider that's used to adjust the confidence threshold for all classes or labels, or an individual class or label. The slider is available on a model's detail page in the **Evaluate** tab. The confidence threshold is the confidence level that the model must have for it to assign a class or label to a test item. As you adjust the threshold, you can see how your model's precision and recall changes. Higher thresholds typically increase precision and lower recall.

#### Example batch prediction output

Batch AutoML image classification prediction output are stored as [JSON Lines](https://jsonlines.org/) files in Cloud Storage buckets. Each line of the JSON Lines file contains all annotation (label) categories and their corresponding confidence scores for a single image file. 

**Note** : The following JSON Lines example includes line breaks for readability. In your JSON Lines files, line breaks are included only after each each JSON object.
    
    
    {
      "instance": {"content": "gs://bucket/image.jpg", "mimeType": "image/jpeg"},
      "prediction": {
        "ids": [1, 2],
        "displayNames": ["cat", "dog"],
        "confidences": [0.7, 0.5]
      }
    }
    

[ Previous arrow_back  Get predictions  ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/image-data/classification/get-predictions)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
