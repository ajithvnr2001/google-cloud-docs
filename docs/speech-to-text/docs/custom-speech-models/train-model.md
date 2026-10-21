---
url: https://docs.cloud.google.com/speech-to-text/docs/custom-speech-models/train-model/
title: Train and manage models \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:50:12.368612+00:00
---

# Train and manage models  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/custom-speech-models/train-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



Send feedback 

#  Train and manage models Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Using the API, without any code, you can create and train a Custom Speech-to-Text model to improve recognition accuracy from an existing Cloud Speech-to-Text model. This fully managed service automatically provisions compute resources, executes the training application code, and ensures deletion of compute resources after the training job. You get a fully fine-tuned transcription model useful for any downstream application.

Similar to machine-learning models, training a Custom Speech-to-Text model is typically iterative and involves selecting a base model as a starting point, fine-tuning it with your text and audio datasets, then testing the recognition quality of the model. If the results are not what you expected, you retrain a new model with a different mixture of data, test again, or use it directly for transcription in your domain.

## Before you begin

Ensure you have signed up for a Google Cloud account, created a Google Cloud project, and enabled the Cloud Speech-to-Text API: Go to **Speech** in the Google Cloud console, and navigate to the Cloud Speech-to-Text API. Operate in the **Custom Models** section of the navigation bar on the left.

## Create a custom model

Start by creating a custom Speech-to-Text model and defining its parameters, like base model and transcription language:

  1. Click **Create** to create a custom model.
  2. Enter a **Model name** , which will be used for the display and be referenced in your API requests and Google Cloud Speech console.
  3. Enter a **Description** for the model.
  4. Select a **Base model** that is suited best for your use case.
  5. Select the transcription **Language** of the model.
  6. Select the **Region** in which training should take place.
  7. Click **Continue**.

![Screenshot of the Custom Speech-to-Text model creation workflow, showing the fields required for the custom model](https://docs.cloud.google.com/static/speech-to-text/v2/docs/images/custom_models_create_model.png)

To complete the definition of the Custom Speech-to-Text model job and start the training, you will need to define the training and validation datasets.

  1. Select a **training dataset** , by providing a valid Cloud Storage directory URI. Ensure that only audio and text files are present and that the total duration of audio follows the [training dataset requirements](https://docs.cloud.google.com/speech-to-text/docs/custom-speech-models/prepare-data#training_dataset_guidelines). 
     1. Select a **validation dataset** , by providing a valid Cloud Storage directory URI. Ensure that only audio and text files are present and that the total duration of audio follows the [validation dataset requirements](https://docs.cloud.google.com/speech-to-text/docs/custom-speech-models/prepare-data#validation_dataset_guidelines). 
        1. Click **Create** to initiate the training process.



If not enough audio hours are indexed or the files don't follow the guidelines, the training job will fail.

![Screenshot of the Custom Speech-to-Text model creation workflow, showing the fields required for the training and validation datasets of the custom model](https://docs.cloud.google.com/static/speech-to-text/v2/docs/images/custom_models_create_dataset.png)

Training jobs can be queued behind other jobs in our system, and training a model can take anywhere from a couple of hours to a few days depending on the dataset size. After the model training, its state will be flagged as **Active**.

## Delete a custom model

Before you start, make sure that there is no traffic routed to your Custom Speech-to-Text model through any endpoint, because deleting it will stop it from serving any requests.

  1. Navigate to the **Models** tab of the **Custom Models** section.
  2. Click to expand options and then click **Delete**. In a few moments the Custom Speech-to-Text model will be deleted, along with all of its endpoints, and will no longer serve any traffic.



## List your custom models

By selecting the **Models** in the **Custom Models** section, you can also list all of your Custom Speech-to-Text models, including the ones that are training, active, and deleting.

![Screenshot of the Custom Speech-to-Text model list workflow, showing a table with all the already created custom models](https://docs.cloud.google.com/static/speech-to-text/v2/docs/images/custom_models_list.png)

## What's next

Follow the resources to take advantage of custom speech models in your application:

  * [Deploy and manage model endpoints ](https://docs.cloud.google.com/speech-to-text/docs/custom-speech-models/deploy-model).
  * [Use your custom models](https://docs.cloud.google.com/speech-to-text/docs/custom-speech-models/use-model)
  * [Evaluate your custom models](https://docs.cloud.google.com/speech-to-text/docs/custom-speech-models/evaluate-model)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
