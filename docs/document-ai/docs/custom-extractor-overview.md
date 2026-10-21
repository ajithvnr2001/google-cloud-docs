---
url: https://docs.cloud.google.com/document-ai/docs/custom-extractor-overview/
title: Custom extractor overview \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:00:13.571295+00:00
---

# Custom extractor overview  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/custom-extractor-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/document-ai/docs/overview)



Send feedback 

#  Custom extractor overview Stay organized with collections  Save and categorize content based on your preferences. 

Custom extractor extracts entities from documents of a particular type. For example, it can extract the items in a menu or the name and contact information from a resume.

## Overview

The goal of the custom extractor is to enable Document AI users to build custom entity extraction solutions for new document types for which no pre-trained processors are available. Custom extractor includes a combination of layout-aware deep learning models (for generative AI and custom models) and template-based models.

## Which training method should I use?

Custom extractor supports a wide range of use cases with three different modes.

**Training method** | **Document examples** | **Document layout variation** | **Free form text or paragraphs** | **Number of training documents for production-ready quality, depending on variability**  
---|---|---|---|---  
Fine tune and foundation model (generative AI). | Contract, terms of service, invoice, bank statement, bill of lading, payslips. | High to Low (preferred). | High. | Medium: 0-50+ documents.  
Custom model. | Model. | Similar forms with layout variation across years or vendors (for example, W9). | Low to medium. | Low. | High: 10-100+ documents.  
Template. | Tax forms with a fixed layout (for example, Forms 941 and 709). | None. | Low. | Low (3 documents).  
  
Because foundation models typically require fewer training documents, they're recommended as the first option for all variable layouts.

For the steps required to create a custom extraction processor, see [create a processor](https://docs.cloud.google.com/document-ai/docs/ce-mechanisms#create_a_processor).

## Confidence score

The confidence score communicates how strongly your model associates each entity with the predicted value. The value is between zero and one, the closer it is to one, the higher the model's confidence that the value corresponds to the entity. This allows users to set triggers for manual review of individual entities when the value is low. For example, determining whether the text in an entity is "Hello, world!" or "HeIIo vvorld!"

The benefits of this approach allow for spotting individual entities with low confidence, setting thresholds for which predictions are used, selecting the optimal [confidence threshold](https://docs.cloud.google.com/document-ai/docs/evaluate#confidence_threshold), and development of new strategies for training models with higher accuracy and confidence scores.

For more information on evaluation concepts and metrics, see [Evaluate Performance](https://docs.cloud.google.com/document-ai/docs/evaluate#all-labels)

[ Previous arrow_back  Form Parser  ](https://docs.cloud.google.com/document-ai/docs/form-parser)

[ Next Custom extractor mechanisms  arrow_forward  ](https://docs.cloud.google.com/document-ai/docs/ce-mechanisms)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
