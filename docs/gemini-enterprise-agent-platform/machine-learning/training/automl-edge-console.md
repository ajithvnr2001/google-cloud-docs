---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/automl-edge-console/
title: Train an AutoML Edge model using the Google Cloud console \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:26:23.047878+00:00
---

# Train an AutoML Edge model using the Google Cloud console  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/automl-edge-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Train an AutoML Edge model using the Google Cloud console Stay organized with collections  Save and categorize content based on your preferences. 

You create an AutoML Edge (exportable) model directly in the UI for certain data types, or by starting a training pipeline job [programmatically](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/automl-edge-api). You create this model using a prepared dataset. Create this dataset in the Google Cloud console or using the [API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/automl-edge-api). Agent Platform API uses the items from the dataset to train the model, test it, and evaluate model performance. Review the evaluations results, adjust the training dataset as needed, and create a new training job using the improved dataset.

Training jobs can take several hours to complete. The Agent Platform page of the Google Cloud console shows the status of training.

**Note:** AutoML Edge object detection is in maintenance mode. Only severe failures will be addressed. We recommend migrating to alternative solutions such as open source (OSS) models.

## Training an AutoML Edge model

  1. In the Google Cloud console, in the Agent Platform section, go to the **Datasets** page.

[Go to the Datasets page](https://console.cloud.google.com/agent-platform/datasets)

  2. Click the name of the dataset you want to use to train your model to open its details page.

  3. If your data type uses annotation sets, select the annotation set you want to use for this model.

  4. Click **Train new model**.

  5. In the **Train new model** page, complete the following steps:

     1. Select radio_button_checked **AutoML Edge** for the training method and click **Continue**.

     2. Enter the display name for your new model.

     3. If you want manually set how your training data is split, expand _Advanced options_ * and select a data split option. For more information, see [About data splits for AutoML models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/ml-use).

     4. Click **Continue**.

     5. Select the optimization goal that best suits your need. You can optimize for accuracy, latency, or both.

     6. Click **Continue**.

     7. In the **Compute and pricing** window, enter the maximum number of hours you want your model to train for.

This setting helps you put a cap on the training costs. The actual time elapsed can be longer than this value, because there are other operations involved in creating a new model.

  6. If you want to stop training when the model is no longer improving, select **Enable early stopping**.

  7. Click **Start Training**.

Model training can take many hours, depending on your training budget (image only) and the size and complexity of your data. You can close this tab and return to it later. You will receive an email when your model has completed training.




## What's next

  * [Evaluate AutoML models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training-overview#automl).
  * [Export AutoML Edge models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/export/export-edge-model). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
