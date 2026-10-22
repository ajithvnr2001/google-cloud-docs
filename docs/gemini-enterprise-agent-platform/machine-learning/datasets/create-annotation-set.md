---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/datasets/create-annotation-set/
title: Create an annotation set for AutoML image training \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:23:03.443577+00:00
---

# Create an annotation set for AutoML image training  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/datasets/create-annotation-set/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Create an annotation set for AutoML image training Stay organized with collections  Save and categorize content based on your preferences. 

An _annotation set_ is a set of labels that you apply to the data of an unstructured dataset for model training. Annotation sets are associated with a data type and model objective (for example, `image/classification`). You create an annotation set for image data types.

To learn how to apply the labels of your annotation set to your dataset's data, see [Label using the Google Cloud console](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/datasets/label-using-console).

## How to create an annotation set

When you create a dataset in Gemini Enterprise Agent Platform, if the imported CSV or [JSON Lines](https://jsonlines.org/) file contains labels, Gemini Enterprise Agent Platform automatically creates an annotation set and assigns it the objective that you selected for the dataset. For example, if you select _image_ as the data type and _Classification_ as the objective, the annotation set `DATASET_NAME\_icn` is created, where "icn" stands for "image classification."

If the dataset is already created and you want to add an annotation set or additional annotation sets, you can create them in the Google Cloud console as detailed in the following section.

## Create a new annotation set

You can create a new annotation set for an existing dataset in the Google Cloud console only.

  1. In the Google Cloud console, go to the Gemini Enterprise Agent Platform **Datasets** page.

[Go to Datasets](https://console.cloud.google.com/agent-platform/datasets)

  2. Click the dataset that you want to create an annotation set for.

The dataset appears.

![Agent Platform dashboard](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/machine-learning/datasets/images/dataset-appears-vcn.png)

  3. In the selector box next to the name of your dataset, select **Create annotation set**.

  4. In the **Create annotation set** pane, enter a name for the annotation set.

  5. Select the model objective.

  6. Click **Create**.

The dataset view appears with your new annotation set displayed. You are now ready to apply the labels of your new annotation set to your data.




## What's next

  * Edit, or add labels to your dataset [using the Google Cloud console](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/datasets/label-using-console).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
