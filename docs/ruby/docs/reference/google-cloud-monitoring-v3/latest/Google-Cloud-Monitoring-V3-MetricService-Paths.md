---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-MetricService-Paths/
title: Cloud Monitoring V3 API - Module Google::Cloud::Monitoring::V3::MetricService::Paths (v1.10.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:30:57.121781+00:00
---

# Cloud Monitoring V3 API - Module Google::Cloud::Monitoring::V3::MetricService::Paths (v1.10.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-MetricService-Paths/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Monitoring V3 API - Module Google::Cloud::Monitoring::V3::MetricService::Paths (v1.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.10.1 (latest)  1.10.0  1.9.0  1.8.0  1.7.1  1.6.1  1.5.1  1.4.0  1.3.0  1.2.0  1.1.0  1.0.1  0.18.0  0.17.0  0.16.0  0.15.2  0.14.0  0.13.0  0.12.1  0.11.0  0.10.0  0.9.0  0.8.0  0.7.1 

Reference documentation and code samples for the Cloud Monitoring V3 API module Google::Cloud::Monitoring::V3::MetricService::Paths.

Path helper methods for the MetricService API.

## Extended By

  * [Google::Cloud::Monitoring::V3::MetricService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-MetricService-Paths)



## Included In

  * [Google::Cloud::Monitoring::V3::MetricService::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-MetricService-Client)
  * [Google::Cloud::Monitoring::V3::MetricService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-MetricService-Paths)



## Methods 

### #folder_path
    
    
    def folder_path(folder:) -> ::String

Create a fully-qualified Folder resource string.

The resource will be in the following format:

`folders/{folder}`

**Parameter**

  * **folder** (String) 



**Returns**

  * (::String) 



### #metric_descriptor_path
    
    
    def metric_descriptor_path(project:, metric_descriptor:) -> ::String
    def metric_descriptor_path(organization:, metric_descriptor:) -> ::String
    def metric_descriptor_path(folder:, metric_descriptor:) -> ::String

Create a fully-qualified MetricDescriptor resource string.

**Overloads**
    
    
    def metric_descriptor_path(project:, metric_descriptor:) -> ::String

The resource will be in the following format:

`projects/{project}/metricDescriptors/{metric_descriptor=**}`

**Parameters**

  * **project** (String) 
  * **metric_descriptor** (String) 


    
    
    def metric_descriptor_path(organization:, metric_descriptor:) -> ::String

The resource will be in the following format:

`organizations/{organization}/metricDescriptors/{metric_descriptor=**}`

**Parameters**

  * **organization** (String) 
  * **metric_descriptor** (String) 


    
    
    def metric_descriptor_path(folder:, metric_descriptor:) -> ::String

The resource will be in the following format:

`folders/{folder}/metricDescriptors/{metric_descriptor=**}`

**Parameters**

  * **folder** (String) 
  * **metric_descriptor** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #monitored_resource_descriptor_path
    
    
    def monitored_resource_descriptor_path(project:, monitored_resource_descriptor:) -> ::String
    def monitored_resource_descriptor_path(organization:, monitored_resource_descriptor:) -> ::String
    def monitored_resource_descriptor_path(folder:, monitored_resource_descriptor:) -> ::String

Create a fully-qualified MonitoredResourceDescriptor resource string.

**Overloads**
    
    
    def monitored_resource_descriptor_path(project:, monitored_resource_descriptor:) -> ::String

The resource will be in the following format:

`projects/{project}/monitoredResourceDescriptors/{monitored_resource_descriptor}`

**Parameters**

  * **project** (String) 
  * **monitored_resource_descriptor** (String) 


    
    
    def monitored_resource_descriptor_path(organization:, monitored_resource_descriptor:) -> ::String

The resource will be in the following format:

`organizations/{organization}/monitoredResourceDescriptors/{monitored_resource_descriptor}`

**Parameters**

  * **organization** (String) 
  * **monitored_resource_descriptor** (String) 


    
    
    def monitored_resource_descriptor_path(folder:, monitored_resource_descriptor:) -> ::String

The resource will be in the following format:

`folders/{folder}/monitoredResourceDescriptors/{monitored_resource_descriptor}`

**Parameters**

  * **folder** (String) 
  * **monitored_resource_descriptor** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #organization_path
    
    
    def organization_path(organization:) -> ::String

Create a fully-qualified Organization resource string.

The resource will be in the following format:

`organizations/{organization}`

**Parameter**

  * **organization** (String) 



**Returns**

  * (::String) 



### #project_path
    
    
    def project_path(project:) -> ::String

Create a fully-qualified Project resource string.

The resource will be in the following format:

`projects/{project}`

**Parameter**

  * **project** (String) 



**Returns**

  * (::String) 



### #workspace_path
    
    
    def workspace_path(project:) -> ::String
    def workspace_path(workspace:) -> ::String

Create a fully-qualified Workspace resource string.

**Overloads**
    
    
    def workspace_path(project:) -> ::String

The resource will be in the following format:

`projects/{project}`

**Parameter**

  * **project** (String) 


    
    
    def workspace_path(workspace:) -> ::String

The resource will be in the following format:

`workspaces/{workspace}`

**Parameter**

  * **workspace** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
