---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.RuntimeConfig
title: Class RuntimeConfig (0.6.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:28:43.215711+00:00
---

# Class RuntimeConfig (0.6.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.RuntimeConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class RuntimeConfig (0.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.1 (latest)  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.10 
    
    
    RuntimeConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

RuntimeConfig represents the runtimes where the application is deployed.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`gke_workload` |  `[google.cloud.developerconnect_v1.types.GKEWorkload](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GKEWorkload)`   
Output only. Google Kubernetes Engine runtime. This field is a member of `oneof`_ `runtime`.   
`google_cloud_run` |  `[google.cloud.developerconnect_v1.types.GoogleCloudRun](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GoogleCloudRun)`   
Output only. Cloud Run runtime. This field is a member of `oneof`_ `runtime`.   
`app_hub_workload` |  `[google.cloud.developerconnect_v1.types.AppHubWorkload](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.AppHubWorkload)`   
Output only. App Hub Workload. This field is a member of `oneof`_ `derived_from`.   
`app_hub_service` |  `[google.cloud.developerconnect_v1.types.AppHubService](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.AppHubService)`   
Output only. App Hub Service. This field is a member of `oneof`_ `derived_from`.   
`uri` |  `str`   
Required. Immutable. The URI of the runtime configuration. For GKE, this is the cluster name. For Cloud Run, this is the service name.   
`state` |  `[google.cloud.developerconnect_v1.types.RuntimeConfig.State](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.RuntimeConfig.State)`   
Output only. The state of the Runtime.   
  
## Classes 

### State
    
    
    State(value)

The state of the runtime in the InsightsConfig. Whether the runtime is linked to the InsightsConfig.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
