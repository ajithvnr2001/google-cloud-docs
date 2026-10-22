---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rest/overview/
title: Vertex AI Optical Character Recognition API \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:02.101577+00:00
---

# Vertex AI Optical Character Recognition API  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rest/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  Vertex AI Optical Character Recognition API Stay organized with collections  Save and categorize content based on your preferences. 

This is the REST API reference for the Optical Character Recognition pre-trained API that is included with Vertex AI on Google Distributed Cloud (GDC) air-gapped appliance. Use this guide to programmatically detect text in files and images.

## Service: Optical Character Recognition (OCR)

### Service endpoint

A service endpoint is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and URIs that are relative to this service endpoint:

  * `https://OCR_ENDPOINT`



Replace `OCR_ENDPOINT` with the endpoint used to access Vertex AI OCR API. For more information, see [View Vertex AI service statuses and endpoints](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-api-status). 

## REST Resource: [v1.files](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rest/v1/files)

Methods  
---  
`[annotate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rest/v1/files/annotate)` |  `POST /v1/files:annotate`   
Service that performs image detection and annotation for a batch of files.  
  
## REST Resource: [v1.images](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rest/v1/images)

Methods  
---  
`[annotate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rest/v1/images/annotate)` |  `POST /v1/images:annotate`   
Run image detection and annotation for a batch of images.  
  
## REST Resource: [v1.projects.files](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rest/v1/projects.files)

Methods  
---  
`[annotate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rest/v1/projects.files/annotate)` |  `POST /v1/{parent}/files:annotate`   
Service that performs image detection and annotation for a batch of files.  
  
## REST Resource: [v1.projects.images](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rest/v1/projects.images)

Methods  
---  
`[annotate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rest/v1/projects.images/annotate)` |  `POST /v1/{parent}/images:annotate`   
Run image detection and annotation for a batch of images.  
  
## REST Resource: [v1.projects.locations.files](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rest/v1/projects.locations.files)

Methods  
---  
`[annotate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rest/v1/projects.locations.files/annotate)` |  `POST /v1/{parent}/files:annotate`   
Service that performs image detection and annotation for a batch of files.  
  
## REST Resource: [v1.projects.locations.images](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rest/v1/projects.locations.images)

Methods  
---  
`[annotate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rest/v1/projects.locations.images/annotate)` |  `POST /v1/{parent}/images:annotate`   
Run image detection and annotation for a batch of images.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
