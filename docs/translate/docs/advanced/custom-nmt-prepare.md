---
url: https://docs.cloud.google.com/translate/docs/advanced/custom-nmt-prepare/
title: Prepare training data \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:03.790772+00:00
---

# Prepare training data  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/advanced/custom-nmt-prepare/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Guides ](https://docs.cloud.google.com/translate/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Prepare training data

Cloud Translation trains custom models by using matching pairs of segments in the source and target languages. It treats each segment pair as an independent training item, without assuming any correlation between separate pairs.

The segment pairs that are used to train your custom model must be in the tab-separated values (`.tsv`) or Translation Memory eXchange (`.tmx`) format. For more information, see [Prepare example translations](https://docs.cloud.google.com/translate/docs/advanced/custom-translations#file-prep).

Segment pairs are always de-duplicated across all imported pairs. A segment pair is a duplicate of another when their source segment matches another source segment. Cloud Translation doesn't allow you to import files with the same content.

## Data split

Cloud Translation uses the segment pairs that you provide to for different purposes while creating your custom model:

  * **Train** \- Segment pairs to train the model. Allocate most of your data for this purpose.
  * **Validation** \- Segment pairs to validate the results that the model returns during training.
  * **Test** \- Segment pairs to generate the final evaluation metrics of your model. Indicates how the model might perform in production.



You can control which segment pairs Cloud Translation uses for each purpose by uploading separate files for the training, validation, and testing sets. If you don't explicitly specify which files to use for these three purposes, Cloud Translation automatically divides your segment pairs into three sets. Cloud Translation uses approximately 80% of your data for training, 10% for validation, and 10% for testing. Cloud Translation randomly assigns your segment pairs into the three sets. You can have a maximum of 10,000 segment pairs each for the validation and testing sets. After 10,000 pairs, segment pairs are pushed to the training set.

If you do multiple data imports into the same dataset, you can manually specify the data split for one import and use the automatic split for another. Data is always re-balanced with respect to your manual division after each import and file deletion.

**Note:** If you exceed 100,000 segment pairs, you might have an unbalanced data split because you can only include a maximum of 10,000 segment pairs for the validation and test sets. Cloud Translation warns you but still allows training to proceed.

## Data requirements

Your training data must conform to the following requirements:

  * If you let Cloud Translation automatically split your data, you must submit at least 1,000 segment pairs to train a custom model.
  * If you manually split your data, you must provide at least three segment pairs for the `TRAIN` set, and you must have at least 100 segment pairs each for the `VALIDATION` and `TEST` sets.
  * You must provide at least three segment pairs for the `TRAIN` set, and you must have at least 100 segment pairs each for the `VALIDATION` and `TEST` sets.
  * You cannot provide more than 10,000 segment pairs each for the `VALIDATION` and `TEST` sets.
  * Your dataset cannot exceed the maximum of 15 million segment pairs.

**Important:** Do not use this product with any personal identifiable information (PII) or any data or images that have been obtained from a website or online service (including mobile apps) directed to children or from children under the age of 13, as covered by the Children's Online Privacy Protection Act, regardless of any parental consent. Data should be sanitized before sending it to the API. For support with removing PII or sensitive data visit <https://cloud.google.com/dlp>

## Data recommendations

The following recommendations can help you increase the quality of your model:

  * Use at least 5,000 segment pairs for `TRAIN`, 500 segment pairs for `VALIDATION`, and 500 segment pairs for `TEST`. That said, use more data if possible. Having more data for the `TRAIN` set helps the model learn patterns, and having more data for the `VALIDATION` and `TEST` sets help verify that the model can be generalized to a wider variety of scenarios in your domain.
  * Keep segments to roughly 200 words or less. Cloud Translation might drop segment pairs larger than that. For more information, see [Import issues](https://docs.cloud.google.com/translate/docs/advanced/custom-nmt-datasets#issues).
  * Fix common source data issues, as described in the "Clean up messy data" part in the [data preparation](https://docs.cloud.google.com/translate/docs/advanced/nmt-customization#clean-up) section of the overview.



## What's next

  * [Create a dataset and import your data](https://docs.cloud.google.com/translate/docs/advanced/custom-translations#file-prep).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
