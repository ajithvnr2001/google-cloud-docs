---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-hypercompute_cluster-v1beta/latest/Google-Cloud-HypercomputeCluster-V1beta-HypercomputeCluster-Paths/
title: Cluster Director V1BETA API - Module Google::Cloud::HypercomputeCluster::V1beta::HypercomputeCluster::Paths (v1.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:13:47.638433+00:00
---

# Cluster Director V1BETA API - Module Google::Cloud::HypercomputeCluster::V1beta::HypercomputeCluster::Paths (v1.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-hypercompute_cluster-v1beta/latest/Google-Cloud-HypercomputeCluster-V1beta-HypercomputeCluster-Paths/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cluster Director V1BETA API - Module Google::Cloud::HypercomputeCluster::V1beta::HypercomputeCluster::Paths (v1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Cluster Director V1BETA API module Google::Cloud::HypercomputeCluster::V1beta::HypercomputeCluster::Paths.

Path helper methods for the HypercomputeCluster API.

## Extended By

  * [Google::Cloud::HypercomputeCluster::V1beta::HypercomputeCluster::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-hypercompute_cluster-v1beta/latest/Google-Cloud-HypercomputeCluster-V1beta-HypercomputeCluster-Paths)



## Included In

  * [Google::Cloud::HypercomputeCluster::V1beta::HypercomputeCluster::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-hypercompute_cluster-v1beta/latest/Google-Cloud-HypercomputeCluster-V1beta-HypercomputeCluster-Client)
  * [Google::Cloud::HypercomputeCluster::V1beta::HypercomputeCluster::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-hypercompute_cluster-v1beta/latest/Google-Cloud-HypercomputeCluster-V1beta-HypercomputeCluster-Paths)
  * [Google::Cloud::HypercomputeCluster::V1beta::HypercomputeCluster::Rest::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-hypercompute_cluster-v1beta/latest/Google-Cloud-HypercomputeCluster-V1beta-HypercomputeCluster-Rest-Client)



## Methods 

### #bucket_path
    
    
    def bucket_path(project:, bucket:) -> ::String

Create a fully-qualified Bucket resource string.

The resource will be in the following format:

`projects/{project}/buckets/{bucket}`

**Parameters**

  * **project** (String) 
  * **bucket** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #cluster_path
    
    
    def cluster_path(project:, location:, cluster:) -> ::String

Create a fully-qualified Cluster resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/clusters/{cluster}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **cluster** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #compute_instance_path
    
    
    def compute_instance_path(project:, zone:, instance:) -> ::String

Create a fully-qualified ComputeInstance resource string.

The resource will be in the following format:

`projects/{project}/zones/{zone}/instances/{instance}`

**Parameters**

  * **project** (String) 
  * **zone** (String) 
  * **instance** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #disk_type_path
    
    
    def disk_type_path(project:, zone:, disk_type:) -> ::String

Create a fully-qualified DiskType resource string.

The resource will be in the following format:

`projects/{project}/zones/{zone}/diskTypes/{disk_type}`

**Parameters**

  * **project** (String) 
  * **zone** (String) 
  * **disk_type** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #file_instance_path
    
    
    def file_instance_path(project:, location:, instance:) -> ::String

Create a fully-qualified FileInstance resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/instances/{instance}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **instance** (String) 



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



### #lustre_instance_path
    
    
    def lustre_instance_path(project:, location:, instance:) -> ::String

Create a fully-qualified LustreInstance resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/instances/{instance}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **instance** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #network_path
    
    
    def network_path(project:, network:) -> ::String

Create a fully-qualified Network resource string.

The resource will be in the following format:

`projects/{project}/global/networks/{network}`

**Parameters**

  * **project** (String) 
  * **network** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #reservation_path
    
    
    def reservation_path(project:, zone:, reservation:) -> ::String

Create a fully-qualified Reservation resource string.

The resource will be in the following format:

`projects/{project}/zones/{zone}/reservations/{reservation}`

**Parameters**

  * **project** (String) 
  * **zone** (String) 
  * **reservation** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #subnetwork_path
    
    
    def subnetwork_path(project:, region:, subnetwork:) -> ::String

Create a fully-qualified Subnetwork resource string.

The resource will be in the following format:

`projects/{project}/regions/{region}/subnetworks/{subnetwork}`

**Parameters**

  * **project** (String) 
  * **region** (String) 
  * **subnetwork** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
