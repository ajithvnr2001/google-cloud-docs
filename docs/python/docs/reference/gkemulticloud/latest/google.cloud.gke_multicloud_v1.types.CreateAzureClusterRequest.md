---
url: https://docs.cloud.google.com/python/docs/reference/gkemulticloud/latest/google.cloud.gke_multicloud_v1.types.CreateAzureClusterRequest
title: Class CreateAzureClusterRequest (0.9.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:08:50.723608+00:00
---

# Class CreateAzureClusterRequest (0.9.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/gkemulticloud/latest/google.cloud.gke_multicloud_v1.types.CreateAzureClusterRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CreateAzureClusterRequest (0.9.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.2 (latest)  0.9.1  0.8.0  0.7.0  0.6.22  0.5.1  0.4.0  0.3.0  0.2.2  0.1.1 
    
    
    CreateAzureClusterRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request message for `AzureClusters.CreateAzureCluster` method.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The parent location where this AzureCluster resource will be created. Location names are formatted as `projects/`. See `Resource Names   
`azure_cluster` |  `[google.cloud.gke_multicloud_v1.types.AzureCluster](https://docs.cloud.google.com/python/docs/reference/gkemulticloud/latest/google.cloud.gke_multicloud_v1.types.AzureCluster)`   
Required. The specification of the AzureCluster to create.   
`azure_cluster_id` |  `str`   
Required. A client provided ID the resource. Must be unique within the parent resource. The provided ID will be part of the AzureCluster resource name formatted as `projects/`. Valid characters are `/`a-z][0-9]`-/`. Cannot be longer than 63 characters.   
`validate_only` |  `bool`   
If set, only validate the request, but do not actually create the cluster.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
