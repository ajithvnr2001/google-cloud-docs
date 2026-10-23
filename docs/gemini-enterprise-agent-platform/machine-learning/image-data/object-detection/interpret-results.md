---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/image-data/object-detection/interpret-results/
title: Interpret prediction results from image object detection models \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:43:11.287338+00:00
---

# Interpret prediction results from image object detection models  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/image-data/object-detection/interpret-results/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Interpret prediction results from image object detection models Stay organized with collections  Save and categorize content based on your preferences. 

After requesting a prediction, Gemini Enterprise Agent Platform returns results based on your model's objective. AutoML image object detection prediction responses return all objects found in an image. Each found object has an annotation (label and normalized bounding box) with a corresponding confidence score. The bounding box is written as: 

` "bboxes": [ [xMin, xMax, yMin, yMax], ...] `

Where `xMin, xMax` are the minimum and maximum x values and ` yMin, yMax` are the minimum and maximum y values respectively. 

#### Example batch prediction output

Batch AutoML image object detection prediction responses are stored as JSON Lines files in Cloud Storage buckets. Each line of the JSON Lines file contains all objects found in a single image file. Each found object has an annotation (label and normalized bounding box) with a corresponding confidence score. 

**Note: Zero coordinate values omitted.** When the API detects a coordinate ("x" or "y") value of 0, **_that coordinate is omitted in the JSON response_**. Thus, a response with a bounding poly around the entire image would be   
**[{},{"x": 1,"y": 1}]**. For more information, see [Method: projects.locations.models.predict](https://cloud.google.com/automl/docs/reference/rest/v1/projects.locations.models/predict#boundingpoly). 

**Note** : The following JSON Lines example includes line breaks for readability. In your JSON Lines files, line breaks are included only after each each JSON object.

**Important:** Bounding boxes are specified as: 

` "bboxes": [ [xMin, xMax, yMin, yMax], ...] `

Where `xMin` and `xMax` are the minimum and maximum x values and ` yMin` and `yMax` are the minimum and maximum y values respectively. 
    
    
    {
      "instance": {"content": "gs://bucket/image.jpg", "mimeType": "image/jpeg"},
      "prediction": {
        "ids": [1, 2],
        "displayNames": ["cat", "dog"],
        "bboxes":  [
          [0.1, 0.2, 0.3, 0.4],
          [0.2, 0.3, 0.4, 0.5]
        ],
        "confidences": [0.7, 0.5]
      }
    }
    

[ Previous arrow_back  Get predictions  ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/image-data/object-detection/get-predictions)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
