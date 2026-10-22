---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/ai-content-detection/
title: Detect AI-generated images \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:42:26.780487+00:00
---

# Detect AI-generated images  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/ai-content-detection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Detect AI-generated images Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To identify AI-generated or modified images from Google and third-party models, you can use the AI Content Detection API. This document explains how the API works, its limitations, and how to request access.

## How it works

To use the API, send an image payload to the Gemini Enterprise Agent Platform endpoint using a REST API call. Supported image formats include the following:

  * JPEG
  * PNG
  * WebP



### Processing

The API processes the payload using machine learning models that analyze pixel-level artifacts, noise patterns, and spectral anomalies. The response aggregates findings from the models.

**Note:** Support for C2PA metadata detection is not included.

### Data retention

The API does not store or retain processed images.

## Request access

The AI Content Detection API is in Private Preview. To request access to the endpoint, complete the [application form](https://docs.google.com/forms/d/e/1FAIpQLScj_8Im1G0A1DsJBfqT7mVN4ZaSKbP58D1PNrx3lnKr4Zt6jg/viewform).

## Disclaimers and limitations

The API provides a probabilistic estimate and doesn't guarantee definitive identification. Use of the service is subject to the following conditions:

  * **Statistical Errors:** The model may produce false positives (authentic images flagged as AI-generated) and false negatives (AI-generated images misclassified as authentic).
  * **Advisory Use:** The API output should serve as a supplementary signal. It must not be used as the sole basis for critical decisions, such as content takedowns or user sanctions.
  * **Liability:** The service is provided "as is". Google assumes no liability for damages or disputes arising from reliance on API outputs.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
