---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-hypercompute_cluster-v1beta/latest/Google-Cloud-HypercomputeCluster-V1beta-NewSpotInstancesConfig/
title: Cluster Director V1BETA API - Class Google::Cloud::HypercomputeCluster::V1beta::NewSpotInstancesConfig (v1.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:48:14.683636+00:00
---

# Cluster Director V1BETA API - Class Google::Cloud::HypercomputeCluster::V1beta::NewSpotInstancesConfig (v1.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-hypercompute_cluster-v1beta/latest/Google-Cloud-HypercomputeCluster-V1beta-NewSpotInstancesConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cluster Director V1BETA API - Class Google::Cloud::HypercomputeCluster::V1beta::NewSpotInstancesConfig (v1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Cluster Director V1BETA API class Google::Cloud::HypercomputeCluster::V1beta::NewSpotInstancesConfig.

When set in a [ComputeResourceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-hypercompute_cluster-v1beta/latest/Google-Cloud-HypercomputeCluster-V1beta-ComputeResourceConfig "Google::Cloud::HypercomputeCluster::V1beta::ComputeResourceConfig \(class\)"), indicates that [spot VM](https://cloud.google.com/compute/docs/instances/spot) instances should be created.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #machine_type
    
    
    def machine_type() -> ::String

**Returns**

  * (::String) — Required. Immutable. Name of the Compute Engine [machine type](https://cloud.google.com/compute/docs/machine-resource) to use, e.g. `n2-standard-2`. 



### #machine_type=
    
    
    def machine_type=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Immutable. Name of the Compute Engine [machine type](https://cloud.google.com/compute/docs/machine-resource) to use, e.g. `n2-standard-2`. 



**Returns**

  * (::String) — Required. Immutable. Name of the Compute Engine [machine type](https://cloud.google.com/compute/docs/machine-resource) to use, e.g. `n2-standard-2`. 



### #zone
    
    
    def zone() -> ::String

**Returns**

  * (::String) — Required. Immutable. Name of the zone in which VM instances should run, e.g., `us-central1-a`. Must be in the same region as the cluster, and must match the zone of any other resources specified in the cluster. 



### #zone=
    
    
    def zone=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Immutable. Name of the zone in which VM instances should run, e.g., `us-central1-a`. Must be in the same region as the cluster, and must match the zone of any other resources specified in the cluster. 



**Returns**

  * (::String) — Required. Immutable. Name of the zone in which VM instances should run, e.g., `us-central1-a`. Must be in the same region as the cluster, and must match the zone of any other resources specified in the cluster. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
