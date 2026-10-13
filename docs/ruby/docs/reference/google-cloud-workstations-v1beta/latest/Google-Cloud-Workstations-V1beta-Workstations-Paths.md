---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1beta/latest/Google-Cloud-Workstations-V1beta-Workstations-Paths/
title: Cloud Workstations V1BETA API - Module Google::Cloud::Workstations::V1beta::Workstations::Paths (v0.10.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:23:55.829684+00:00
---

# Cloud Workstations V1BETA API - Module Google::Cloud::Workstations::V1beta::Workstations::Paths (v0.10.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1beta/latest/Google-Cloud-Workstations-V1beta-Workstations-Paths/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Workstations V1BETA API - Module Google::Cloud::Workstations::V1beta::Workstations::Paths (v0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.10.0  0.9.0  0.8.1  0.7.1  0.6.0  0.5.1  0.4.1  0.3.0  0.2.0  0.1.3 

Reference documentation and code samples for the Cloud Workstations V1BETA API module Google::Cloud::Workstations::V1beta::Workstations::Paths.

Path helper methods for the Workstations API.

## Extended By

  * [Google::Cloud::Workstations::V1beta::Workstations::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1beta/latest/Google-Cloud-Workstations-V1beta-Workstations-Paths)



## Included In

  * [Google::Cloud::Workstations::V1beta::Workstations::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1beta/latest/Google-Cloud-Workstations-V1beta-Workstations-Client)
  * [Google::Cloud::Workstations::V1beta::Workstations::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1beta/latest/Google-Cloud-Workstations-V1beta-Workstations-Paths)
  * [Google::Cloud::Workstations::V1beta::Workstations::Rest::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workstations-v1beta/latest/Google-Cloud-Workstations-V1beta-Workstations-Rest-Client)



## Methods 

### #location_path
    
    
    def location_path(project:, location:) -> ::String

Create a fully-qualified Location resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}`

**Parameters**

  * **project** (String) 
  * **location** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #workstation_cluster_path
    
    
    def workstation_cluster_path(project:, location:, workstation_cluster:) -> ::String

Create a fully-qualified WorkstationCluster resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/workstationClusters/{workstation_cluster}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **workstation_cluster** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #workstation_config_path
    
    
    def workstation_config_path(project:, location:, workstation_cluster:, workstation_config:) -> ::String

Create a fully-qualified WorkstationConfig resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/workstationClusters/{workstation_cluster}/workstationConfigs/{workstation_config}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **workstation_cluster** (String) 
  * **workstation_config** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #workstation_path
    
    
    def workstation_path(project:, location:, workstation_cluster:, workstation_config:, workstation:) -> ::String

Create a fully-qualified Workstation resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/workstationClusters/{workstation_cluster}/workstationConfigs/{workstation_config}/workstations/{workstation}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **workstation_cluster** (String) 
  * **workstation_config** (String) 
  * **workstation** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
