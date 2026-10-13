---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-TelcoAutomation-Paths/
title: Telco Automation V1 API - Module Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Paths (v2.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:28:34.450454+00:00
---

# Telco Automation V1 API - Module Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Paths (v2.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-TelcoAutomation-Paths/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Telco Automation V1 API - Module Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Paths (v2.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.5.1 (latest)  2.5.0  2.4.0  2.3.1  2.2.0  2.1.0  2.0.1  1.2.0  1.1.0  1.0.2  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Telco Automation V1 API module Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Paths.

Path helper methods for the TelcoAutomation API.

## Extended By

  * [Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-TelcoAutomation-Paths)



## Included In

  * [Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-TelcoAutomation-Client)
  * [Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-TelcoAutomation-Paths)
  * [Google::Cloud::TelcoAutomation::V1::TelcoAutomation::Rest::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-TelcoAutomation-Rest-Client)



## Methods 

### #blueprint_path
    
    
    def blueprint_path(project:, location:, orchestration_cluster:, blueprint:) -> ::String

Create a fully-qualified Blueprint resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/orchestrationClusters/{orchestration_cluster}/blueprints/{blueprint}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **orchestration_cluster** (String) 
  * **blueprint** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #deployment_path
    
    
    def deployment_path(project:, location:, orchestration_cluster:, deployment:) -> ::String

Create a fully-qualified Deployment resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/orchestrationClusters/{orchestration_cluster}/deployments/{deployment}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **orchestration_cluster** (String) 
  * **deployment** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #edge_slm_path
    
    
    def edge_slm_path(project:, location:, edge_slm:) -> ::String

Create a fully-qualified EdgeSlm resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/edgeSlms/{edge_slm}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **edge_slm** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #hydrated_deployment_path
    
    
    def hydrated_deployment_path(project:, location:, orchestration_cluster:, deployment:, hydrated_deployment:) -> ::String

Create a fully-qualified HydratedDeployment resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/orchestrationClusters/{orchestration_cluster}/deployments/{deployment}/hydratedDeployments/{hydrated_deployment}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **orchestration_cluster** (String) 
  * **deployment** (String) 
  * **hydrated_deployment** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



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



### #orchestration_cluster_path
    
    
    def orchestration_cluster_path(project:, location:, orchestration_cluster:) -> ::String

Create a fully-qualified OrchestrationCluster resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/orchestrationClusters/{orchestration_cluster}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **orchestration_cluster** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #public_blueprint_path
    
    
    def public_blueprint_path(project:, location:, public_lueprint:) -> ::String

Create a fully-qualified PublicBlueprint resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/publicBlueprints/{public_lueprint}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **public_lueprint** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
