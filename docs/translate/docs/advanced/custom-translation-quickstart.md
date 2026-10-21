---
url: https://docs.cloud.google.com/translate/docs/advanced/custom-translation-quickstart/
title: Create a custom translation model \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:14.179564+00:00
---

# Create a custom translation model  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/advanced/custom-translation-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Guides ](https://docs.cloud.google.com/translate/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a custom translation model

**Note:** Translation LLM can be customized with your training data using [Vertex AI supervised fine-tuning - Public Preview](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/translation-supervised-tuning).

Train and use a custom translation model by using the Google Cloud console. The following example uses AutoML Translation to train an English-to-Spanish translation model by using a dataset that contains technology-oriented segment pairs from software localization.

**Note:** The following tutorial assumes that, for your project, the Google Cloud console is using the Cloud Translation API instead of the AutoML API to create datasets. This condition is true if you have at least one native Cloud Translation resource or no legacy AutoML resources in your project. If you have only legacy AutoML resources, see [Upgrade AutoML resources](https://docs.cloud.google.com/translate/docs/advanced/automl-upgrade) for more information.

## Before you begin

Before you can start using AutoML Translation, your project must have the Cloud Translation API enabled, and you must have the permissions that are granted by the following roles:

  * **Viewer** role to view existing resources in your project
  * **Cloud Translation API Editor** role to create and manage datasets and models
  * **Storage Admin** role to upload training data to a Cloud Storage bucket



## Create a translation dataset and import segment pairs

  1. [Download](https://docs.cloud.google.com/static/translate/docs/advanced/sample/automl-translation-data.zip) the archive file that contains the sample data for training the model, and extract the files.

For this tutorial, you'll use the English to Spanish TSV file.

  2. Go to the AutoML Translation console.

[Go to the Translation page](https://console.cloud.google.com/translation)

  3. From the navigation pane, click **Datasets** to go to the **Datasets** page.

  4. Click **Create dataset**.

  5. In the **Create dataset** dialog, specify details about the dataset:

     1. Enter `tutorial_dataset` as the name for the dataset.
     2. Select **English (EN)** as your source language from the drop-down list.
     3. Select **Spanish (ES)** as your target language.
     4. Click **Create**.
  6. After the dataset is created, click the dataset name to view its details.

  7. Go to the **Import** tab and upload the `en-es.tsv` dataset to Cloud Storage:

     1. Select **Upload files from your computer**.
     2. Click **Select files** , and choose the `en-es.tsv` file that you previously downloaded and extracted.
     3. Click **Browse** to select or create a new Cloud Storage bucket where your TSV is stored. The bucket region must be `us-central1`.
  8. Click **Continue**.

AutoML Translation automatically splits your data into training, validation, and testing sets. You can view these splits and the imported sentence pairs in the **Sentences** tab of your dataset.




## Train a model

  1. Go to the AutoML Translation console.

[Go to the Translation page](https://console.cloud.google.com/translation)

  2. From the navigation pane, go to the **Datasets** page.

  3. Click the **tutorial_dataset** dataset.

  4. Go to the **Train** tab.

  5. Click **Start training** , which opens the **Train new model** pane.

  6. Enter `tutorial_model` for the model name.

  7. Click **Start training**.




Training a model can take several hours to complete.

## Evaluate the model

Check to see how the model compares to the default Google NMT model that is based on segment pairs from your test set.

  1. Go to the AutoML Translation console.

[Go to the Translation page](https://console.cloud.google.com/translation)

  2. From the navigation pane, go to the **Models** page.

  3. Click the **tutorial_model** model.

  4. Click the **Evaluate** tab.




In the **Previous evaluations** section, Cloud Translation shows your model's BLEU score compared to the Google NMT model. The [BLEU (Bilingual Evaluation Understudy)](https://docs.cloud.google.com/translate/docs/advanced/automl-evaluate#bleu) score indicates how similar the candidate text is to the reference texts; values closer to 100 represent more similar texts.

## Use the translation model

From the Google Cloud console, you can use your custom model to translate some text.

  1. Go to the AutoML Translation console.

[Go to the Translation page](https://console.cloud.google.com/translation)

  2. From the navigation pane, go to the **Models** page.

  3. Click the **tutorial_model** model.

  4. Click the **Predict** tab.

  5. In the **English** text box, enter text to translate and then click **Translate**.

You can compare the results from your custom model to the Google NMT model.




## Clean up

To avoid unnecessary Google Cloud charges, delete your [model](https://docs.cloud.google.com/translate/docs/advanced/automl-models#delete-model), [dataset](https://docs.cloud.google.com/translate/docs/advanced/automl-datasets#delete-dataset), and `en-es.tsv` file. You can also use the [Google Cloud console](https://console.cloud.google.com/) to delete your project if you don't need it.

## What's next

  * To learn about custom models, see the [Beginner's guide](https://docs.cloud.google.com/translate/docs/advanced/automl-beginner).
  * To create your own dataset and custom model, see [Prepare training data](https://docs.cloud.google.com/translate/docs/advanced/automl-prepare) for instructions on how to prepare your data.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
