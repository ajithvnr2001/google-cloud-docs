---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/datasets/label-using-console/
title: Label data using the Google Cloud console \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:16:30.914625+00:00
---

# Label data using the Google Cloud console  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/datasets/label-using-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Label data using the Google Cloud console Stay organized with collections  Save and categorize content based on your preferences. 

For image data, you can import labeled or unlabeled data and add labels using the Google Cloud console. You can also delete or add new labels to existing labeled datasets.

To learn how to import your data, see the _Prepare data_ page of the data type and objective that you're working with on the [AutoML training overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/automl-training-overview#data) page. Continue with the respective _Create dataset_ page for your data type and objective.

After creating the dataset and importing the unlabeled data, you will be in **Browse** mode.

![Browse mode view of the dataset in the Google Cloud console](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/machine-learning/datasets/images/browse-mode.png)

## How to add labels

Instructions for labeling objectives are provided here.

The images you have just imported in the dataset are unlabeled, as expected. 

### Classification

When in Browse mode, and the dataset with the unlabeled images is selected, you can see your uploaded images. 

  1. Click **Add new label** and enter your new label.
  2. Click **Done**.  
Repeat for each label you want to add.
  3. Select the image you want to label.  
The list of labels appears.
  4. Select the label you want to associate with the image.
  5. Click **Save**.



### Classification

When in **Browse** mode, and the dataset with the unlabeled images is selected, you can see your uploaded images. 

  1. Click **Add new label** and enter your new label.
  2. Click **Done**.  
Repeat for each label you want to add.
  3. Select the image you want to label.  
The list of labels appears.
  4. Select the label you want to associate with the image.
  5. Click **Save**.
  6. You can view the labels applied to each image in the **Browse** tab. ![multi-labeled images](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/machine-learning/datasets/images/multi-labeled-images.png)



### Object detection

When in **Browse** mode, and the dataset with the unlabeled images is selected, you can see your uploaded images. 

  1. Click **Add new label** and enter your new label.
  2. Click **Done**.  
Repeat for each label you want to add.
  3. Select the image you want to label.
  4. The list of labels objects appears, if there are any.
  5. In the add annotation window, select the Add bounding box button to add an object bounding box to the image.  
![add bounding box to image](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/machine-learning/datasets/images/add-bounding-box-image.png)
  6. After drawing a bounding box, a list of labels to apply to the object will appear. Choose the appropriate label.  
![add label bounding boxed image](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/machine-learning/datasets/images/image-bounding-box-label.png)
  7. After you have added all labels and bounding boxes, click **Save** to update the image's annotations.  
![save added labels for bounding boxed image](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/machine-learning/datasets/images/image-save-bounding-box-labels.png)



## What's next

  * [Train an AutoML model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/automl-training-overview).
  * [Train an AutoML Edge model using the Google Cloud console](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/automl-edge-console). (image only)
  * [Train an AutoML Edge model using the Agent Platform API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/automl-edge-api). (image only)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
