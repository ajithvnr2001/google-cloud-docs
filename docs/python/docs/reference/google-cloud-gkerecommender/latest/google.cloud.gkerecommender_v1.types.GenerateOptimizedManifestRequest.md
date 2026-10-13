---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-gkerecommender/latest/google.cloud.gkerecommender_v1.types.GenerateOptimizedManifestRequest
title: Class GenerateOptimizedManifestRequest (0.3.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:48:05.244744+00:00
---

# Class GenerateOptimizedManifestRequest (0.3.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-gkerecommender/latest/google.cloud.gkerecommender_v1.types.GenerateOptimizedManifestRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class GenerateOptimizedManifestRequest (0.3.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.3.2 (latest)  0.3.1  0.2.0  0.1.0 
    
    
    GenerateOptimizedManifestRequest(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

Request message for GkeInferenceQuickstart.GenerateOptimizedManifest.

## Attributes  
  
---  
**Name** | **Description**  
`model_server_info` |  `[google.cloud.gkerecommender_v1.types.ModelServerInfo](https://docs.cloud.google.com/python/docs/reference/google-cloud-gkerecommender/latest/google.cloud.gkerecommender_v1.types.ModelServerInfo)`   
Required. The model server configuration to generate the manifest for. Use GkeInferenceQuickstart.FetchProfiles to find valid configurations.   
`accelerator_type` |  `str`   
Required. The accelerator type. Use GkeInferenceQuickstart.FetchProfiles to find valid accelerators for a given `model_server_info`.   
`kubernetes_namespace` |  `str`   
Optional. The kubernetes namespace to deploy the manifests in.   
`performance_requirements` |  `[google.cloud.gkerecommender_v1.types.PerformanceRequirements](https://docs.cloud.google.com/python/docs/reference/google-cloud-gkerecommender/latest/google.cloud.gkerecommender_v1.types.PerformanceRequirements)`   
Optional. The performance requirements to use for generating Horizontal Pod Autoscaler (HPA) resources. If provided, the manifest includes HPA resources to adjust the model server replica count to maintain the specified targets (e.g., NTPOT, TTFT) at a P50 latency. Cost targets are not currently supported for HPA generation. If the specified targets are not achievable, the HPA manifest will not be generated.   
`storage_config` |  `[google.cloud.gkerecommender_v1.types.StorageConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-gkerecommender/latest/google.cloud.gkerecommender_v1.types.StorageConfig)`   
Optional. The storage configuration for the model. If not provided, the model is loaded from Huggingface.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
