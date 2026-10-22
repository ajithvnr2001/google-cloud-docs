---
url: https://docs.cloud.google.com/document-ai/docs/custom-based-extraction/
title: Custom-based extraction \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:48.861558+00:00
---

# Custom-based extraction  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/custom-based-extraction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/document-ai/docs/overview)



Send feedback 

#  Custom-based extraction Stay organized with collections  Save and categorize content based on your preferences. 

Custom model training and extraction lets you to build your own model designed specifically for your documents without the use of generative AI. It's ideal if you don't want to use generative AI and want to control all aspects of the trained model.

##  Dataset configuration 

A document dataset is required to train, up-train, or evaluate a processor version. Document AI processors learn from examples, just like humans. Dataset fuels processor stability in terms of performance.  


###  Train dataset 

To improve the model and its accuracy, train a dataset on your documents. The model is made up of documents with ground-truth. You need a minimum of three documents to train a new model. Ground-truth is the correctly labeled data, as determined by humans.

###  Test dataset 

The test dataset is what the model uses to generate an F1 score (accuracy). It is made up of documents with ground-truth. To see how often the model is right, the ground truth is used to compare the model's predictions (extracted fields from the model) with the correct answers. The test dataset should have at least three documents. 

## Before getting started

If not done so already, [enable billing](https://docs.cloud.google.com/document-ai/docs/setup#billing) and the [Document AI API](https://docs.cloud.google.com/document-ai/docs/setup).

## Build and evaluate a custom model

Begin by building and then evaluating a custom processor.

  1. [Create a processor](https://docs.cloud.google.com/document-ai/docs/workbench/build-custom-processor#create_a_processor) and [define fields](https://docs.cloud.google.com/document-ai/docs/workbench/build-custom-processor#define_processor_fields) you want to extract, which is important because it impacts extraction quality.

**Note:** The default processor is a foundation model.
  2. Set dataset location: Select the default option folder **Google-managed**. This might be done automatically shortly after creating the processor.

  3. Navigate to the **Build** tab and select **Import Documents** with auto-labeling enabled (see Auto-labeling with the foundation model). You need a minimum of 10 documents in the training set and 10 in the testing set to train a custom model.

  4. Train model:

     1. Select **Train new version** and name the processor version.
     2. Go to **Show advanced options** and select the **Model based** option.

![custom-based-extraction-1](https://docs.cloud.google.com/static/document-ai/docs/images/create/custom-based-extraction-1.png)

**Note:** It takes some time for the training to complete.
  5. Evaluation:

     * Go to **Evaluate & test**, select the version you just trained, then select **View full evaluation**.

![custom-based-extraction-2](https://docs.cloud.google.com/static/document-ai/docs/images/create/custom-based-extraction-2.png)

     * You now see metrics such as [f1, precision, and recall](https://docs.cloud.google.com/document-ai/docs/workbench/evaluate#all-labels) for the entire document and each field.
     * Decide if performance meets your production goals. If it does not, then reevaluate training and testing sets, typically adding documents to the training test set that don't parse well.
  6. Set a new version as the default.

     1. Navigate to **Manage versions**.
     2. Navigate to the more_vert menu and then select **Set as default**.

![custom-based-extraction-3](https://docs.cloud.google.com/static/document-ai/docs/images/create/custom-based-extraction-3.png)




Your model is now deployed and documents sent to this processor are now using your custom version. You want to [evaluate the model's performance](https://docs.cloud.google.com/document-ai/docs/workbench/evaluate) to check if it requires further training.

## Evaluation reference

The evaluation engine can do both exact match or [fuzzy matching](https://docs.cloud.google.com/document-ai/docs/workbench/evaluate#fuzzy_matching). For an exact match, the extracted value must exactly match the ground truth or is counted as a miss.

Fuzzy matching extractions that had slight differences such as capitalization differences still count as a match. This can be changed at the **Evaluation** screen.

![custom-based-extraction-4](https://docs.cloud.google.com/static/document-ai/docs/images/create/custom-based-extraction-4.png)

## Auto-labeling with the foundation model

The foundation model can accurately extract fields for a variety of document types, but you can also provide additional training data to improve the accuracy of the model for specific document structures.

Document AI uses the label names you define and previous annotations to label documents at scale with auto-labeling.

  1. When you've created a custom processor, go to the **Get Started** tab.
  2. Select **Create new field**. 
  3. Provide a descriptive name and fill out the description field. Property description lets you provide additional context, insights, and prior knowledge for each entity to improve extraction accuracy and performance.

**Note:** Good examples of property descriptions include location information and text patterns of the property values, which help disambiguate potential sources of confusion in the document, guiding the model with rules that ensure more reliable and consistent extractions, regardless of the specific document structure or content variations.

![custom-based-extraction-5](https://docs.cloud.google.com/static/document-ai/docs/images/create/custom-based-extraction-5.png)

  1. Navigate to the **Build** tab, then select **Import documents**.

![custom-based-extraction-6](https://docs.cloud.google.com/static/document-ai/docs/images/create/custom-based-extraction-6.png)

  2. Select the path of the documents and which set the documents should be imported into. Check the auto-labeling box, and select the foundation model.

  3. In the **Build** tab, select **Manage Dataset**. You should see your imported documents. Select one of your documents.

![custom-based-extraction-7](https://docs.cloud.google.com/static/document-ai/docs/images/create/custom-based-extraction-7.png)




You now see the predictions from the model highlighted in purple.

  1. Review each label predicted by the model and ensure is correct. If there are missing fields, add those as well.

**Note:** It's important that all fields are as accurate as possible or model performance might affect the results. [More details on labeling](https://docs.cloud.google.com/document-ai/docs/workbench/label-documents).

![custom-based-extraction-8](https://docs.cloud.google.com/static/document-ai/docs/images/create/custom-based-extraction-8.png)

  1. After the document has been reviewed, select **Mark as labeled**. The document is now ready to be used by the model. Make sure the document is in either the **Testing** or **Training** set.



[ Previous arrow_back  Automated schema extraction  ](https://docs.cloud.google.com/document-ai/docs/ce-schema-extraction)

[ Next Template-based extraction  arrow_forward  ](https://docs.cloud.google.com/document-ai/docs/ce-template-based)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
