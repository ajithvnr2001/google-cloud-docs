---
url: https://docs.cloud.google.com/translate/docs/supported-formats/
title: Supported formats quick reference \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:57.343212+00:00
---

# Supported formats quick reference  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/supported-formats/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Guides ](https://docs.cloud.google.com/translate/docs/overview)



Send feedback 

#  Supported formats quick reference Stay organized with collections  Save and categorize content based on your preferences. 

Request | Description | Mime types | Supported input file extensions | Supported output file extensions | Supported API  
---|---|---|---|---|---  
Text translation (NMT and AutoML Translation) | Synchronous requests in text string | text/plain, text/html |  inline | inline | Basic (v2) and Advanced (v3)  
Text translation (LLM) | Synchronous requests in text string | text/plain |  inline | inline | Advanced (v3) only  
Batch text translation - Cloud Storage (NMT and AutoML Translation) | Asynchronous requests with accepted input and output file formats | text/plain, text/html | .txt, .html, .tsv | .txt, .html, .tsv | Advanced (v3) only  
Batch document translation (NMT and AutoML Translation) | Asynchronous requests with accepted input and output file formats | application/msword, application/vnd.openxmlformats-officedocument.wordprocessingml.document, application/pdf, application/vnd.ms-powerpoint, application/vnd.openxmlformats-officedocument.presentationml.presentation, application/vnd.ms-excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet | .doc, .docx, .pdf, .ppt, .pptx, .xls, .xlsx | .doc, .docx, .pdf, .ppt, .pptx, .xls, .xlsx | Advanced (v3) only  
Document translation (NMT and AutoML Translation) | Synchronous requests with accepted input and output file formats | application/msword, application/vnd.openxmlformats-officedocument.wordprocessingml.document, application/pdf, application/vnd.ms-powerpoint, application/vnd.openxmlformats-officedocument.presentationml.presentation, application/vnd.ms-excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet | inline, .doc, .docx, .pdf, .ppt, .pptx, .xls, .xlsx | inline, .doc, .docx, .pdf, .ppt, .pptx, .xls, .xlsx | Advanced (v3) only  
Glossary creation | Glossary files uploaded to Google Cloud project | text/plain | .tmx, .csv, .tsv | n/a | Advanced (v3) only  
AutoML Translation dataset creation | Accepted formats for training data import. | text/plain | .tsv | n/a | Advanced (v3) only  
AutoML Translation dataset export | Exported segment pairs from existing datasets to Cloud Storage. | text/plain | n/a | .tsv | Advanced (v3) only  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
