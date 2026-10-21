---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-overview/
title: Vertex AI overview \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:22:12.041245+00:00
---

# Vertex AI overview  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Vertex AI overview Stay organized with collections  Save and categorize content based on your preferences. 

Vertex AI on Google Distributed Cloud (GDC) air-gapped appliance brings the power of a machine learning (ML) and artificial intelligence (AI) platform to your secure portable device. GDC air-gapped appliance provides access to a select set of pre-trained Vertex AI APIs, enabling AI capabilities in your private cloud solution.

## Key features

Vertex AI on GDC air-gapped appliance offers you the following features:

  * **Air-gapped deployment** : Run Vertex AI services entirely within your portable device, ensuring data sovereignty and compliance.
  * **Familiar Vertex AI experience** : Take advantage of the same tools and APIs from Google Cloud, simplifying development and management.
  * **Pre-built models and algorithms** : Access a range of pre-trained models for common machine learning tasks, accelerating your time to value.



## Available services

Vertex AI on GDC air-gapped appliance offers the following pre-trained services:

  * [**Optical Character Recognition (OCR)**](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-ocr): Extract text from images and files.
  * [**Speech-to-Text**](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-stt): Convert spoken language into written text.
  * [**Vertex AI Translation**](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-translation): Translate text between multiple languages.

**Caution:** GDC air-gapped appliance includes a single NVIDIA A100 80 GB GPU. This limits the device to running only _one_ GPU-dependent Vertex AI pre-trained API at a time. For more information, see Capacity planning and computing requirements.

## Capacity planning and computing requirements

Each Vertex AI service requires different computing resources. The following table provides the requirements for each pre-trained model:

Pre-trained API | Computing resources | GPU count requirements | GPU memory requirements  
---|---|---|---  
Optical Character Recognition (OCR) | GPU | A single A100 80 GB GPU | 40 GB  
Speech-to-Text | CPU | _Not applicable (only CPU)_ | _Not applicable (only CPU)_  
Vertex AI Translation | GPU | A single A100 80 GB GPU | 50 GB  
  
GDC air-gapped appliance includes a single NVIDIA A100 80 GB GPU. This limits the device to running only _one_ GPU-dependent Vertex AI pre-trained API at a time. If you attempt to enable both Vertex AI Translation and OCR, the second API will fail to enable with an error message indicating insufficient GPU resources. You can, however, run Speech-to-Text alongside either Vertex AI Translation or OCR, as Speech-to-Text only requires CPU resources.

To help you determine the number of appliance units needed for your AI/ML workloads, review the following capacity limits for each Vertex AI pre-trained API:

Pre-trained API | Capacity per appliance unit  
---|---  
Optical Character Recognition (OCR) | Up to 30 images per minute (one image every two seconds).  
Speech-to-Text | Up to seven minutes of audio transcribed per minute (seven seconds of audio transcribed per second).  
Vertex AI Translation | Up to 61,000 characters per minute (1,024 characters per second).  
  
When you plan your deployment, consider the following guidance:

  * The capacity limits are approximate and not guaranteed. Actual capacity might vary depending on factors such as the following:

    * Complexity of the input data (for example, language for translation, image quality for OCR, and audio clarity for Speech-to-Text).
    * Specific configuration of the appliance.
    * Concurrent usage of other services on the appliance.
  * Only one GPU-intensive API (Vertex AI Translation or OCR) can be active at a time because GDC air-gapped appliance is limited to a single A100 80 GB GPU.

  * Estimate your peak usage and potential future growth.

  * For demanding workloads requiring higher throughput, consider deploying multiple appliance units.




The following table outlines the storage requirements for each Vertex AI service on GDC air-gapped appliance:

Component | Storage requirements  
---|---  
OCR frontend | 0.1 GB  
OCR backend | 5 GB  
OCR extractor | 0.1 GB  
Speech-to-Text frontend | 0.1 GB  
Speech-to-Text backend | 1.5 GB  
Vertex AI Translation frontend | 0.7 GB  
Vertex AI Translation backend | 61.4 GB  
  
Ensure that your appliance has sufficient storage capacity to accommodate the Vertex AI services you intend to use.

## Benefits

Vertex AI on GDC air-gapped appliance offers the following benefits:

  * **Seamless development experience** : Use the same tools, APIs, and workflows of Vertex AI on Google Cloud, making development and management intuitive and efficient.
  * **Enhanced security and privacy** : Maintain complete control over your data and comply with regulatory requirements.
  * **Accelerated time to value** : Use pre-trained models for common machine learning tasks.
  * **Streamlined MLOps** : Benefit from robust machine learning operation capabilities for seamless AI integrations within your air-gapped environment.



## Getting started

To get started with Vertex AI on GDC air-gapped appliance, do the following:

  * [Learn about essential roles and permissions for available services](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-ao-permissions).
  * [Set up a project for your AI and machine learning workloads](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-set-up-project).
  * [Provision GPUs and enable the Vertex AI services](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-enable-pre-trained-apis).
  * [Install the Vertex AI client libraries](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-install-libraries).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
