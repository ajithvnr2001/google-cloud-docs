---
url: https://docs.cloud.google.com/vision/docs/supported-files/
title: Supported image formats and dimensions \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:24:47.405310+00:00
---

# Supported image formats and dimensions  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/supported-files/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Reference ](https://docs.cloud.google.com/vision/docs/apis)



Send feedback 

#  Supported image formats and dimensions Stay organized with collections  Save and categorize content based on your preferences. 

There are specific image formats, image dimensions, and file sizes you can send to Cloud Vision. Use this guidance to ensure effective feature detection when using the Vision API.

## File formats

The Vision API supports the following image types:

  * JPEG
  * PNG8
  * PNG24
  * GIF
  * Animated GIF (first frame only)
  * BMP
  * WEBP
  * RAW
  * ICO
  * PDF
  * TIFF



Some of these image formats are [_lossy_](https://en.wikipedia.org/wiki/Lossy_compression) (for example, JPEG). Reducing file sizes for such lossy formats might degrade image quality and Vision API accuracy.

## Image dimension recommendations

For accurate image detection within the Vision API, use images that are a minimum of 640x480 pixels (about 300,000 pixels).

In practice, a standard size of 640x480 pixels works well in most cases. Image sizes larger than 640x480 pixels may not gain much in accuracy, while greatly diminishing throughput. When possible, pre-process your images to reduce their size to these minimum standards.

The following recommended sizes vary by the feature detected. For example, `FACE_DETECTION` requests generally require larger image sizes because the detected features (faces) are smaller than the image. `LABEL_DETECTION` requests, on the other hand, generally evaluate an entire image.

The following table lists types of Vision API feature requests and their recommended image sizes:

Vision API feature | Recommended size | Notes  
---|---|---  
`FACE_DETECTION` | 1600x1200 | Distance between eyes is the most important.  
`LANDMARK_DETECTION` | 640x480 | -  
`LOGO_DETECTION` | 640x480 | -  
`LABEL_DETECTION` | 640x480 | -  
`TEXT_DETECTION` and `DOCUMENT_TEXT_DETECTION` | 1024x768 | OCR requires more resolution to detect characters.  
`SAFE_SEARCH_DETECTION` | 640x480 | -  
  
Vision API requires images large enough to distinguish important features. Sizes smaller or larger than these recommended sizes can work. However, smaller sizes can result in lower accuracy, and larger sizes can increase processing time and bandwidth usage without a proportional accuracy gain. For OCR analysis, image size must not exceed 75,000,000 pixels (length x width). If an image exceeds this limit, the Vision API resizes it; otherwise, the Vision API uses the original image.

## Image and file size

Image files sent to the Vision API shouldn't exceed 20 MB. Files exceeding 20 MB generate an error. The Vision API doesn't resize files of this size.

To improve query latency, reduce your file size. However, avoid reducing image quality during this process.

The Vision API imposes a 10 MB JSON request size limit. Host larger files on Cloud Storage or on the web, rather than passing them as base64-encoded content in the JSON itself.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
