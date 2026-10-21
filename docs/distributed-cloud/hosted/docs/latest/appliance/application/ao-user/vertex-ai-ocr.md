---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-ocr/
title: Learn about character recognition features \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:22:13.130084+00:00
---

# Learn about character recognition features  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-ocr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Learn about character recognition features Stay organized with collections  Save and categorize content based on your preferences. 

Optical Character Recognition (OCR) is one of the three Vertex AI pre-trained APIs on Google Distributed Cloud (GDC) air-gapped appliance. The OCR service detects text in various file types, such as images, document files, and handwritten text.

OCR offers the following methods available in GDC air-gapped appliance to recognize text:

Method | Description  
---|---  
[`BatchAnnotateImages`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/quickstart-ocr-images) | Detect text from a batch of JPEG or PNG images provided in an inline request.  
[`BatchAnnotateFiles`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/quickstart-ocr-files) | Detect text from a batch of PDF or TIFF files provided in an inline request.  
**Note:** The `BatchAnnotateImages` and `BatchAnnotateFiles` API methods only support a single request per batch call.

Learn more about the [supported languages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-ocr-supported-langs) detected by the text recognition feature.

## Optical character recognition features

The OCR API can detect and extract text from images. The following two annotation features support optical character recognition:

  * `TEXT_DETECTION` detects and extracts text from any image. For example, a photograph might contain a street or traffic sign. The OCR service returns a JSON file with the extracted string, individual words, and their bounding boxes.

![Road sign containing individual words and bounding boxes for text detection](https://docs.cloud.google.com/static/vision/docs/images/sign_text.png)

**Figure 1.** Road sign photograph where the OCR API detects words and their bounding boxes.

  * `DOCUMENT_TEXT_DETECTION` also extracts text from an image, but the service optimizes the response for dense text and documents. For example, a scanned image of typed text might contain several paragraphs and headings. The OCR service returns a JSON file with page, block, paragraph, word, and break information.

![Scanned image of typed text with a dense proportion of annotations](https://docs.cloud.google.com/static/vision/docs/images/document_text_highlighted.png)

**Figure 2.** Scanned image of typed text where the OCR API detects information such as words, pages, and paragraphs.




## Handwritten text

Figure 3 is an image of handwritten text. The OCR API detects and extracts text from these images. For a list of handwriting scripts that support handwriting recognition, see [Handwriting scripts](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-ocr-supported-langs#handwriting-scripts).

![Handwriting figure](https://docs.cloud.google.com/static/vision/docs/images/detect_handwriting_OCR-detect-handwriting_SMALL.png)

**Figure 3.** Handwriting image where the OCR API detects text.

## Optical character recognition limits

You can recognize up to 30 images per minute, equivalent to one image every two seconds per appliance unit.

The `BatchAnnotateImages` and `BatchAnnotateFiles` API methods only support a single request per batch call.

The following table lists the current limits of the OCR service in Distributed Cloud.

File limit for OCR | Value  
---|---  
Maximum number of pages | Five  
Maximum file size | 20 MB  
Maximum image size | 20 million pixels (length x width)  
  
Submitted files for the OCR API that exceed the maximum number of pages or the maximum file size return an error. Submitted files that exceed the maximum image size are downsized to 20 million pixels.

## Supported file types for OCR

The OCR pre-trained API detects and transcribes text from the following file types:

  * PDF
  * TIFF
  * JPG
  * PNG



You must store the files locally in your Distributed Cloud environment. You can't access files hosted in Cloud Storage or publicly available files for text detection.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-08 UTC."],[],[]] 
