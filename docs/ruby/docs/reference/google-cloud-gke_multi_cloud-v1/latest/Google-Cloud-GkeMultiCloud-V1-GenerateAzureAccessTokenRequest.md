---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_multi_cloud-v1/latest/Google-Cloud-GkeMultiCloud-V1-GenerateAzureAccessTokenRequest/
title: Anthos Multi-Cloud V1 API - Class Google::Cloud::GkeMultiCloud::V1::GenerateAzureAccessTokenRequest (v0.21.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:27:01.736206+00:00
---

# Anthos Multi-Cloud V1 API - Class Google::Cloud::GkeMultiCloud::V1::GenerateAzureAccessTokenRequest (v0.21.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_multi_cloud-v1/latest/Google-Cloud-GkeMultiCloud-V1-GenerateAzureAccessTokenRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Anthos Multi-Cloud V1 API - Class Google::Cloud::GkeMultiCloud::V1::GenerateAzureAccessTokenRequest (v0.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.21.0 (latest)  0.20.1  0.19.0  0.18.0  0.17.1  0.16.0  0.15.0  0.14.1  0.13.0  0.12.0  0.11.0  0.10.1  0.9.0  0.8.2  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Anthos Multi-Cloud V1 API class Google::Cloud::GkeMultiCloud::V1::GenerateAzureAccessTokenRequest.

Request message for `AzureClusters.GenerateAzureAccessToken` method.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #azure_cluster
    
    
    def azure_cluster() -> ::String

**Returns**

  * (::String) — Required. The name of the [AzureCluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_multi_cloud-v1/latest/Google-Cloud-GkeMultiCloud-V1-AzureCluster "Google::Cloud::GkeMultiCloud::V1::AzureCluster \(class\)") resource to authenticate to.

`AzureCluster` names are formatted as `projects/<project-id>/locations/<region>/azureClusters/<cluster-id>`.

See [Resource Names](https://cloud.google.com/apis/design/resource_names) for more details on Google Cloud resource names. 




### #azure_cluster=
    
    
    def azure_cluster=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The name of the [AzureCluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_multi_cloud-v1/latest/Google-Cloud-GkeMultiCloud-V1-AzureCluster "Google::Cloud::GkeMultiCloud::V1::AzureCluster \(class\)") resource to authenticate to.

`AzureCluster` names are formatted as `projects/<project-id>/locations/<region>/azureClusters/<cluster-id>`.

See [Resource Names](https://cloud.google.com/apis/design/resource_names) for more details on Google Cloud resource names. 




**Returns**

  * (::String) — Required. The name of the [AzureCluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_multi_cloud-v1/latest/Google-Cloud-GkeMultiCloud-V1-AzureCluster "Google::Cloud::GkeMultiCloud::V1::AzureCluster \(class\)") resource to authenticate to.

`AzureCluster` names are formatted as `projects/<project-id>/locations/<region>/azureClusters/<cluster-id>`.

See [Resource Names](https://cloud.google.com/apis/design/resource_names) for more details on Google Cloud resource names. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
