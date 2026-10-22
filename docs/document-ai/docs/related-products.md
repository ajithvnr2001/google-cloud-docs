---
url: https://docs.cloud.google.com/document-ai/docs/related-products/
title: Related Google Cloud products \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:43.819194+00:00
---

# Related Google Cloud products  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/related-products/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/document-ai/docs/overview)



Send feedback 

#  Related Google Cloud products Stay organized with collections  Save and categorize content based on your preferences. 

The following products share capabilities with Document AI. However, these products perform a specific text and analysis function. Depending on your use case, these products might provide the specific capabilities you need.

## Convert images to text

You can convert content in images to text using either:

  * [Enterprise Document OCR](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_doc-ocr).
  * [Cloud Vision API](https://docs.cloud.google.com/vision) (using the `TEXT_DETECTION` or `DOCUMENT_TEXT_DETECTION` enums). See:

    * [Cloud Vision API Quickstarts](https://docs.cloud.google.com/vision/docs/quickstarts)

    * [Detect text (OCR)](https://docs.cloud.google.com/vision/docs/ocr)

    * [Detect handwriting (OCR)](https://docs.cloud.google.com/vision/docs/handwriting)

    * [PDF/TIFF Document text detection](https://docs.cloud.google.com/vision/docs/pdf)




## Detect visual artifacts

You can use [AutoML Vision object detection](https://docs.cloud.google.com/vertex-ai/docs/training-overview#object_detection_for_images) to convert sections of images into text documents. For details, see [Image data](https://docs.cloud.google.com/vertex-ai/docs/start/automl-model-types#image). 

## Classify documents

With document plain text and running OCR beforehand, you can categorize and label documents using the following products:

  * The pretrained Natural Language API helps you classify content using a generalized list of categories.
  * Use AutoML Natural Language classification to create a custom machine learning model, and classify content with your own category labels.
  * While there may be exceptions, AutoML Vision classification is not generally recommended for document classification because its tends to be less accurate than text-based methods. However, you can use it for classifying image content.

    * This is not generally a recommended method for classification of documents, as its accuracy tends to be less than text based methods, but there may be exceptions

**Natural Language API** | 

  * [Cloud Natural Language API Quickstarts](https://docs.cloud.google.com/natural-language/docs/quickstarts)
  * [Classifying content](https://docs.cloud.google.com/natural-language/docs/classifying-text)

  
---|---  
**AutoML Natural Language classification** | 

  * [Text model type](https://docs.cloud.google.com/vertex-ai/docs/start/automl-model-types#text)

  
**AutoML Vision classification** | 

  * [Image model type](https://docs.cloud.google.com/vertex-ai/docs/start/automl-model-types#image)

  
  
## Analyze and extract entities

You can identify known entities in documents (proper nouns such as public figures, company branding, and so on) and entities that follow common patterns such as phone numbers and addresses with using [Form Parser](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_form-parser) or any of the [pretrained processors](https://docs.cloud.google.com/document-ai/docs/processor-overview) for your use case.

  * You can also use the Natural Language API to identify common, public entities.
  * AutoML Natural Language products are for entity extraction. Use them to create a custom machine learning model to identify entities specific to your company or use case.

**Natural Language API** | 

  * [Natural language API quickstart](https://docs.cloud.google.com/natural-language/docs/quickstarts)
  * [Analyzing entities](https://docs.cloud.google.com/natural-language/docs/analyzing-entities)

  
---|---  
**AutoML Natural Language Entity Extraction** | 

  * [Text model type](https://docs.cloud.google.com/vertex-ai/docs/start/automl-model-types#text)

  
  
## Other products

Integrate these complimentary products with Document AI to create a complete document processing and analysis solution.

  * [Vertex AI](https://docs.cloud.google.com/vertex-ai): Brings AutoML and AI Platform together into a unified API, client library, and platform.
  * [Cloud Translation API](https://docs.cloud.google.com/translate/docs): Dynamically translates text between thousands of language pairs through pretrained models. Provides a document translation API for directly translating documents in formats such as PDF and DOCX. See [Translate documents](https://docs.cloud.google.com/translate/docs/advanced/translate-documents). 
  * [Workflows](https://docs.cloud.google.com/workflows): Combines Google Cloud services and APIs to build reliable applications, process automation, and data and machine learning pipelines.
  * [AppSheet Automation](https://docs.cloud.google.com/appsheet/automation): Creates custom automations and applications with an open cloud.
  * [Drive scanner by Google Drive](https://support.google.com/drive/answer/3145835?&co=GENIE.Platform%3DAndroid): The Google Drive Android app lets you scan and upload documents to Google Drive and offers intelligent title suggestions powered by Document AI.
  * [Google Translate](https://translate.google.com/): This service instantly translates words, phrases, and web pages between English and over 100 other languages.



## Find a partner

Take advantage of our growing partner ecosystem to help you create and manage your document analysis solution. For a list of partners and the services that they provide, see [Document AI partners](https://cloud.google.com/find-a-partner/).

## What's next?

  * Learn how to [set up](https://docs.cloud.google.com/document-ai/docs/setup) Document AI.
  * Find specific guides in [How-to](https://docs.cloud.google.com/document-ai/docs/how-to).



[ Previous arrow_back  Try Document AI  ](https://docs.cloud.google.com/document-ai/docs/try-docai)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
