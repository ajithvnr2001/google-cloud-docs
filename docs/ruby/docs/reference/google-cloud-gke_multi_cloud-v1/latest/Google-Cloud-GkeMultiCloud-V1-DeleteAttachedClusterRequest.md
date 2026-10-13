---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_multi_cloud-v1/latest/Google-Cloud-GkeMultiCloud-V1-DeleteAttachedClusterRequest/
title: Anthos Multi-Cloud V1 API - Class Google::Cloud::GkeMultiCloud::V1::DeleteAttachedClusterRequest (v0.21.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:58:35.714910+00:00
---

# Anthos Multi-Cloud V1 API - Class Google::Cloud::GkeMultiCloud::V1::DeleteAttachedClusterRequest (v0.21.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_multi_cloud-v1/latest/Google-Cloud-GkeMultiCloud-V1-DeleteAttachedClusterRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Anthos Multi-Cloud V1 API - Class Google::Cloud::GkeMultiCloud::V1::DeleteAttachedClusterRequest (v0.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.21.0 (latest)  0.20.1  0.19.0  0.18.0  0.17.1  0.16.0  0.15.0  0.14.1  0.13.0  0.12.0  0.11.0  0.10.1  0.9.0  0.8.2  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Anthos Multi-Cloud V1 API class Google::Cloud::GkeMultiCloud::V1::DeleteAttachedClusterRequest.

Request message for `AttachedClusters.DeleteAttachedCluster` method.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #allow_missing
    
    
    def allow_missing() -> ::Boolean

**Returns**

  * (::Boolean) — If set to true, and the [AttachedCluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_multi_cloud-v1/latest/Google-Cloud-GkeMultiCloud-V1-AttachedCluster "Google::Cloud::GkeMultiCloud::V1::AttachedCluster \(class\)") resource is not found, the request will succeed but no action will be taken on the server and a completed [Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_multi_cloud-v1/latest/Google-Longrunning-Operation "Google::Longrunning::Operation \(class\)") will be returned.

Useful for idempotent deletion. 




### #allow_missing=
    
    
    def allow_missing=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — If set to true, and the [AttachedCluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_multi_cloud-v1/latest/Google-Cloud-GkeMultiCloud-V1-AttachedCluster "Google::Cloud::GkeMultiCloud::V1::AttachedCluster \(class\)") resource is not found, the request will succeed but no action will be taken on the server and a completed [Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_multi_cloud-v1/latest/Google-Longrunning-Operation "Google::Longrunning::Operation \(class\)") will be returned.

Useful for idempotent deletion. 




**Returns**

  * (::Boolean) — If set to true, and the [AttachedCluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_multi_cloud-v1/latest/Google-Cloud-GkeMultiCloud-V1-AttachedCluster "Google::Cloud::GkeMultiCloud::V1::AttachedCluster \(class\)") resource is not found, the request will succeed but no action will be taken on the server and a completed [Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_multi_cloud-v1/latest/Google-Longrunning-Operation "Google::Longrunning::Operation \(class\)") will be returned.

Useful for idempotent deletion. 




### #etag
    
    
    def etag() -> ::String

**Returns**

  * (::String) — The current etag of the [AttachedCluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_multi_cloud-v1/latest/Google-Cloud-GkeMultiCloud-V1-AttachedCluster "Google::Cloud::GkeMultiCloud::V1::AttachedCluster \(class\)").

Allows clients to perform deletions through optimistic concurrency control.

If the provided etag does not match the current etag of the cluster, the request will fail and an ABORTED error will be returned. 




### #etag=
    
    
    def etag=(value) -> ::String

**Parameter**

  * **value** (::String) — The current etag of the [AttachedCluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_multi_cloud-v1/latest/Google-Cloud-GkeMultiCloud-V1-AttachedCluster "Google::Cloud::GkeMultiCloud::V1::AttachedCluster \(class\)").

Allows clients to perform deletions through optimistic concurrency control.

If the provided etag does not match the current etag of the cluster, the request will fail and an ABORTED error will be returned. 




**Returns**

  * (::String) — The current etag of the [AttachedCluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_multi_cloud-v1/latest/Google-Cloud-GkeMultiCloud-V1-AttachedCluster "Google::Cloud::GkeMultiCloud::V1::AttachedCluster \(class\)").

Allows clients to perform deletions through optimistic concurrency control.

If the provided etag does not match the current etag of the cluster, the request will fail and an ABORTED error will be returned. 




### #ignore_errors
    
    
    def ignore_errors() -> ::Boolean

**Returns**

  * (::Boolean) — If set to true, the deletion of [AttachedCluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_multi_cloud-v1/latest/Google-Cloud-GkeMultiCloud-V1-AttachedCluster "Google::Cloud::GkeMultiCloud::V1::AttachedCluster \(class\)") resource will succeed even if errors occur during deleting in cluster resources. Using this parameter may result in orphaned resources in the cluster. 



### #ignore_errors=
    
    
    def ignore_errors=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — If set to true, the deletion of [AttachedCluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_multi_cloud-v1/latest/Google-Cloud-GkeMultiCloud-V1-AttachedCluster "Google::Cloud::GkeMultiCloud::V1::AttachedCluster \(class\)") resource will succeed even if errors occur during deleting in cluster resources. Using this parameter may result in orphaned resources in the cluster. 



**Returns**

  * (::Boolean) — If set to true, the deletion of [AttachedCluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_multi_cloud-v1/latest/Google-Cloud-GkeMultiCloud-V1-AttachedCluster "Google::Cloud::GkeMultiCloud::V1::AttachedCluster \(class\)") resource will succeed even if errors occur during deleting in cluster resources. Using this parameter may result in orphaned resources in the cluster. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. The resource name the [AttachedCluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_multi_cloud-v1/latest/Google-Cloud-GkeMultiCloud-V1-AttachedCluster "Google::Cloud::GkeMultiCloud::V1::AttachedCluster \(class\)") to delete.

`AttachedCluster` names are formatted as `projects/<project-id>/locations/<region>/attachedClusters/<cluster-id>`.

See [Resource Names](https://cloud.google.com/apis/design/resource_names) for more details on Google Cloud Platform resource names. 




### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name the [AttachedCluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_multi_cloud-v1/latest/Google-Cloud-GkeMultiCloud-V1-AttachedCluster "Google::Cloud::GkeMultiCloud::V1::AttachedCluster \(class\)") to delete.

`AttachedCluster` names are formatted as `projects/<project-id>/locations/<region>/attachedClusters/<cluster-id>`.

See [Resource Names](https://cloud.google.com/apis/design/resource_names) for more details on Google Cloud Platform resource names. 




**Returns**

  * (::String) — Required. The resource name the [AttachedCluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_multi_cloud-v1/latest/Google-Cloud-GkeMultiCloud-V1-AttachedCluster "Google::Cloud::GkeMultiCloud::V1::AttachedCluster \(class\)") to delete.

`AttachedCluster` names are formatted as `projects/<project-id>/locations/<region>/attachedClusters/<cluster-id>`.

See [Resource Names](https://cloud.google.com/apis/design/resource_names) for more details on Google Cloud Platform resource names. 




### #validate_only
    
    
    def validate_only() -> ::Boolean

**Returns**

  * (::Boolean) — If set, only validate the request, but do not actually delete the resource. 



### #validate_only=
    
    
    def validate_only=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — If set, only validate the request, but do not actually delete the resource. 



**Returns**

  * (::Boolean) — If set, only validate the request, but do not actually delete the resource. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
