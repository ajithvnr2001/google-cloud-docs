---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-online-predictions/
title: Learn about online predictions \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:59:21.944080+00:00
---

# Learn about online predictions  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-online-predictions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Learn about online predictions Stay organized with collections  Save and categorize content based on your preferences. 

**Preview:** Online Prediction is a Preview feature that is available as-is and is not recommended for production environments. Google provides no service-level agreements (SLA) or technical support commitments for Preview features. For more information, see GDC's [feature stages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/feature-stages).

Vertex AI offers online predictions on Google Distributed Cloud (GDC) air-gapped through the Online Prediction API. A prediction is the output of a trained machine-learning model. Specifically, online predictions are synchronous requests made to your model endpoint.

Online Prediction lets you upload, deploy, serve, and make requests using your own prediction models on a set of supported containers. Use Online Prediction when making requests in response to application input or in situations requiring timely inference.

You can use the Online Prediction API by applying Kubernetes custom resources to the dedicated [prediction cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/prediction-user-cluster) that your Infrastructure Operator (IO) creates for you.

Before getting online predictions, you must [export model artifacts](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-export-model-artifacts) and [deploy the model to an endpoint](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-deploy-model). This action associates compute resources with the model to serve online predictions with low latency.

Then, you can get online predictions from a custom-trained model by [formatting](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-format-online-prediction) and [sending](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/quickstart-op) a request.

## Available container images

The following table contains the list of supported containers for Online Prediction in Distributed Cloud:

ML framework | Version | Supported accelerators | Supported images  
---|---|---|---  
TensorFlow | 2.18 | CPU | tf2-cpu.2-18  
GPU | tf2-gpu.2-18  
PyTorch | 2.4 | CPU | pytorch-cpu.2-4  
GPU | pytorch-gpu.2-4  
2.1 (DEPRECATED) | CPU | pytorch-cpu.2-1  
GPU | pytorch-gpu.2-1  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
