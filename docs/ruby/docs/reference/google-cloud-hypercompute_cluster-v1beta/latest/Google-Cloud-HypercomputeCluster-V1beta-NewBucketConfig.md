---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-hypercompute_cluster-v1beta/latest/Google-Cloud-HypercomputeCluster-V1beta-NewBucketConfig/
title: Cluster Director V1BETA API - Class Google::Cloud::HypercomputeCluster::V1beta::NewBucketConfig (v1.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:28:10.079586+00:00
---

# Cluster Director V1BETA API - Class Google::Cloud::HypercomputeCluster::V1beta::NewBucketConfig (v1.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-hypercompute_cluster-v1beta/latest/Google-Cloud-HypercomputeCluster-V1beta-NewBucketConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cluster Director V1BETA API - Class Google::Cloud::HypercomputeCluster::V1beta::NewBucketConfig (v1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Cluster Director V1BETA API class Google::Cloud::HypercomputeCluster::V1beta::NewBucketConfig.

When set in a [StorageResourceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-hypercompute_cluster-v1beta/latest/Google-Cloud-HypercomputeCluster-V1beta-StorageResourceConfig "Google::Cloud::HypercomputeCluster::V1beta::StorageResourceConfig \(class\)"), indicates that a new [Google Cloud Storage](https://cloud.google.com/storage) bucket should be created.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #autoclass
    
    
    def autoclass() -> ::Google::Cloud::HypercomputeCluster::V1beta::GcsAutoclassConfig

**Returns**

  * ([::Google::Cloud::HypercomputeCluster::V1beta::GcsAutoclassConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-hypercompute_cluster-v1beta/latest/Google-Cloud-HypercomputeCluster-V1beta-GcsAutoclassConfig)) — Optional. Immutable. If set, indicates that the bucket should use [Autoclass](https://cloud.google.com/storage/docs/autoclass).

Note: The following fields are mutually exclusive: `autoclass`, `storage_class`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #autoclass=
    
    
    def autoclass=(value) -> ::Google::Cloud::HypercomputeCluster::V1beta::GcsAutoclassConfig

**Parameter**

  * **value** ([::Google::Cloud::HypercomputeCluster::V1beta::GcsAutoclassConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-hypercompute_cluster-v1beta/latest/Google-Cloud-HypercomputeCluster-V1beta-GcsAutoclassConfig)) — Optional. Immutable. If set, indicates that the bucket should use [Autoclass](https://cloud.google.com/storage/docs/autoclass).

Note: The following fields are mutually exclusive: `autoclass`, `storage_class`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::HypercomputeCluster::V1beta::GcsAutoclassConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-hypercompute_cluster-v1beta/latest/Google-Cloud-HypercomputeCluster-V1beta-GcsAutoclassConfig)) — Optional. Immutable. If set, indicates that the bucket should use [Autoclass](https://cloud.google.com/storage/docs/autoclass).

Note: The following fields are mutually exclusive: `autoclass`, `storage_class`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #bucket
    
    
    def bucket() -> ::String

**Returns**

  * (::String) — Required. Immutable. Name of the Cloud Storage bucket to create. 



### #bucket=
    
    
    def bucket=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Immutable. Name of the Cloud Storage bucket to create. 



**Returns**

  * (::String) — Required. Immutable. Name of the Cloud Storage bucket to create. 



### #hierarchical_namespace
    
    
    def hierarchical_namespace() -> ::Google::Cloud::HypercomputeCluster::V1beta::GcsHierarchicalNamespaceConfig

**Returns**

  * ([::Google::Cloud::HypercomputeCluster::V1beta::GcsHierarchicalNamespaceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-hypercompute_cluster-v1beta/latest/Google-Cloud-HypercomputeCluster-V1beta-GcsHierarchicalNamespaceConfig)) — Optional. Immutable. If set, indicates that the bucket should use [hierarchical namespaces](https://cloud.google.com/storage/docs/hns-overview). 



### #hierarchical_namespace=
    
    
    def hierarchical_namespace=(value) -> ::Google::Cloud::HypercomputeCluster::V1beta::GcsHierarchicalNamespaceConfig

**Parameter**

  * **value** ([::Google::Cloud::HypercomputeCluster::V1beta::GcsHierarchicalNamespaceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-hypercompute_cluster-v1beta/latest/Google-Cloud-HypercomputeCluster-V1beta-GcsHierarchicalNamespaceConfig)) — Optional. Immutable. If set, indicates that the bucket should use [hierarchical namespaces](https://cloud.google.com/storage/docs/hns-overview). 



**Returns**

  * ([::Google::Cloud::HypercomputeCluster::V1beta::GcsHierarchicalNamespaceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-hypercompute_cluster-v1beta/latest/Google-Cloud-HypercomputeCluster-V1beta-GcsHierarchicalNamespaceConfig)) — Optional. Immutable. If set, indicates that the bucket should use [hierarchical namespaces](https://cloud.google.com/storage/docs/hns-overview). 



### #storage_class
    
    
    def storage_class() -> ::Google::Cloud::HypercomputeCluster::V1beta::NewBucketConfig::StorageClass

**Returns**

  * ([::Google::Cloud::HypercomputeCluster::V1beta::NewBucketConfig::StorageClass](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-hypercompute_cluster-v1beta/latest/Google-Cloud-HypercomputeCluster-V1beta-NewBucketConfig-StorageClass)) — Optional. Immutable. If set, uses the provided storage class as the bucket's default storage class.

Note: The following fields are mutually exclusive: `storage_class`, `autoclass`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #storage_class=
    
    
    def storage_class=(value) -> ::Google::Cloud::HypercomputeCluster::V1beta::NewBucketConfig::StorageClass

**Parameter**

  * **value** ([::Google::Cloud::HypercomputeCluster::V1beta::NewBucketConfig::StorageClass](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-hypercompute_cluster-v1beta/latest/Google-Cloud-HypercomputeCluster-V1beta-NewBucketConfig-StorageClass)) — Optional. Immutable. If set, uses the provided storage class as the bucket's default storage class.

Note: The following fields are mutually exclusive: `storage_class`, `autoclass`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::HypercomputeCluster::V1beta::NewBucketConfig::StorageClass](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-hypercompute_cluster-v1beta/latest/Google-Cloud-HypercomputeCluster-V1beta-NewBucketConfig-StorageClass)) — Optional. Immutable. If set, uses the provided storage class as the bucket's default storage class.

Note: The following fields are mutually exclusive: `storage_class`, `autoclass`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
