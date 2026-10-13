---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Cluster/
title: Cloud Bigtable Admin V2 API - Class Google::Cloud::Bigtable::Admin::V2::Cluster (v1.22.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:11:08.729709+00:00
---

# Cloud Bigtable Admin V2 API - Class Google::Cloud::Bigtable::Admin::V2::Cluster (v1.22.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Bigtable Admin V2 API - Class Google::Cloud::Bigtable::Admin::V2::Cluster (v1.22.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.22.0 (latest)  1.19.0  1.18.1  1.17.0  1.16.0  1.15.1  1.14.0  1.13.0  1.12.0  1.11.1  1.10.0  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.1  1.1.0  1.0.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.3  0.20.0  0.19.0  0.18.0  0.17.0  0.16.3  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.1  0.8.1 

Reference documentation and code samples for the Cloud Bigtable Admin V2 API class Google::Cloud::Bigtable::Admin::V2::Cluster.

A resizable group of nodes in a particular cloud location, capable of serving all [Tables](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Table "Google::Cloud::Bigtable::Admin::V2::Table \(class\)") in the parent [Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Instance "Google::Cloud::Bigtable::Admin::V2::Instance \(class\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #cluster_config
    
    
    def cluster_config() -> ::Google::Cloud::Bigtable::Admin::V2::Cluster::ClusterConfig

**Returns**

  * ([::Google::Cloud::Bigtable::Admin::V2::Cluster::ClusterConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Cluster-ClusterConfig)) — Configuration for this cluster. 



### #cluster_config=
    
    
    def cluster_config=(value) -> ::Google::Cloud::Bigtable::Admin::V2::Cluster::ClusterConfig

**Parameter**

  * **value** ([::Google::Cloud::Bigtable::Admin::V2::Cluster::ClusterConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Cluster-ClusterConfig)) — Configuration for this cluster. 



**Returns**

  * ([::Google::Cloud::Bigtable::Admin::V2::Cluster::ClusterConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Cluster-ClusterConfig)) — Configuration for this cluster. 



### #default_storage_type
    
    
    def default_storage_type() -> ::Google::Cloud::Bigtable::Admin::V2::StorageType

**Returns**

  * ([::Google::Cloud::Bigtable::Admin::V2::StorageType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-StorageType)) — Immutable. The type of storage used by this cluster to serve its parent instance's tables, unless explicitly overridden. 



### #default_storage_type=
    
    
    def default_storage_type=(value) -> ::Google::Cloud::Bigtable::Admin::V2::StorageType

**Parameter**

  * **value** ([::Google::Cloud::Bigtable::Admin::V2::StorageType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-StorageType)) — Immutable. The type of storage used by this cluster to serve its parent instance's tables, unless explicitly overridden. 



**Returns**

  * ([::Google::Cloud::Bigtable::Admin::V2::StorageType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-StorageType)) — Immutable. The type of storage used by this cluster to serve its parent instance's tables, unless explicitly overridden. 



### #encryption_config
    
    
    def encryption_config() -> ::Google::Cloud::Bigtable::Admin::V2::Cluster::EncryptionConfig

**Returns**

  * ([::Google::Cloud::Bigtable::Admin::V2::Cluster::EncryptionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Cluster-EncryptionConfig)) — Immutable. The encryption configuration for CMEK-protected clusters. 



### #encryption_config=
    
    
    def encryption_config=(value) -> ::Google::Cloud::Bigtable::Admin::V2::Cluster::EncryptionConfig

**Parameter**

  * **value** ([::Google::Cloud::Bigtable::Admin::V2::Cluster::EncryptionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Cluster-EncryptionConfig)) — Immutable. The encryption configuration for CMEK-protected clusters. 



**Returns**

  * ([::Google::Cloud::Bigtable::Admin::V2::Cluster::EncryptionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Cluster-EncryptionConfig)) — Immutable. The encryption configuration for CMEK-protected clusters. 



### #location
    
    
    def location() -> ::String

**Returns**

  * ([::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Type-String)) — Immutable. The location where this cluster's nodes and storage reside. For best performance, clients should be located as close as possible to this cluster. Currently only zones are supported, so values should be of the form `projects/{project}/locations/{zone}`. 



### #location=
    
    
    def location=(value) -> ::String

**Parameter**

  * **value** ([::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Type-String)) — Immutable. The location where this cluster's nodes and storage reside. For best performance, clients should be located as close as possible to this cluster. Currently only zones are supported, so values should be of the form `projects/{project}/locations/{zone}`. 



**Returns**

  * ([::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Type-String)) — Immutable. The location where this cluster's nodes and storage reside. For best performance, clients should be located as close as possible to this cluster. Currently only zones are supported, so values should be of the form `projects/{project}/locations/{zone}`. 



### #name
    
    
    def name() -> ::String

**Returns**

  * ([::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Type-String)) — The unique name of the cluster. Values are of the form `projects/{project}/instances/{instance}/clusters/[a-z][-a-z0-9]*`. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** ([::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Type-String)) — The unique name of the cluster. Values are of the form `projects/{project}/instances/{instance}/clusters/[a-z][-a-z0-9]*`. 



**Returns**

  * ([::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Type-String)) — The unique name of the cluster. Values are of the form `projects/{project}/instances/{instance}/clusters/[a-z][-a-z0-9]*`. 



### #node_scaling_factor
    
    
    def node_scaling_factor() -> ::Google::Cloud::Bigtable::Admin::V2::Cluster::NodeScalingFactor

**Returns**

  * ([::Google::Cloud::Bigtable::Admin::V2::Cluster::NodeScalingFactor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Cluster-NodeScalingFactor)) — Immutable. The node scaling factor of this cluster. 



### #node_scaling_factor=
    
    
    def node_scaling_factor=(value) -> ::Google::Cloud::Bigtable::Admin::V2::Cluster::NodeScalingFactor

**Parameter**

  * **value** ([::Google::Cloud::Bigtable::Admin::V2::Cluster::NodeScalingFactor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Cluster-NodeScalingFactor)) — Immutable. The node scaling factor of this cluster. 



**Returns**

  * ([::Google::Cloud::Bigtable::Admin::V2::Cluster::NodeScalingFactor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Cluster-NodeScalingFactor)) — Immutable. The node scaling factor of this cluster. 



### #serve_nodes
    
    
    def serve_nodes() -> ::Integer

**Returns**

  * (::Integer) — The number of nodes in the cluster. If no value is set, Cloud Bigtable automatically allocates nodes based on your data footprint and optimized for 50% storage utilization. 



### #serve_nodes=
    
    
    def serve_nodes=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The number of nodes in the cluster. If no value is set, Cloud Bigtable automatically allocates nodes based on your data footprint and optimized for 50% storage utilization. 



**Returns**

  * (::Integer) — The number of nodes in the cluster. If no value is set, Cloud Bigtable automatically allocates nodes based on your data footprint and optimized for 50% storage utilization. 



### #state
    
    
    def state() -> ::Google::Cloud::Bigtable::Admin::V2::Cluster::State

**Returns**

  * ([::Google::Cloud::Bigtable::Admin::V2::Cluster::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-admin-v2/latest/Google-Cloud-Bigtable-Admin-V2-Cluster-State)) — Output only. The current state of the cluster. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
