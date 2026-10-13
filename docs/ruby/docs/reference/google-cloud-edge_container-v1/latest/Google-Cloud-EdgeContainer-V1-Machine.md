---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_container-v1/latest/Google-Cloud-EdgeContainer-V1-Machine/
title: Distributed Cloud Edge Container V1 API - Class Google::Cloud::EdgeContainer::V1::Machine (v1.5.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:17:45.402951+00:00
---

# Distributed Cloud Edge Container V1 API - Class Google::Cloud::EdgeContainer::V1::Machine (v1.5.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_container-v1/latest/Google-Cloud-EdgeContainer-V1-Machine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Distributed Cloud Edge Container V1 API - Class Google::Cloud::EdgeContainer::V1::Machine (v1.5.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.2 (latest)  1.5.1  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.4.0  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the Distributed Cloud Edge Container V1 API class Google::Cloud::EdgeContainer::V1::Machine.

A Google Distributed Cloud Edge machine capable of acting as a Kubernetes node.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_container-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time when the node pool was created. 



### #disabled
    
    
    def disabled() -> ::Boolean

**Returns**

  * (::Boolean) — Output only. Whether the machine is disabled. If disabled, the machine is unable to enter service. 



### #hosted_node
    
    
    def hosted_node() -> ::String

**Returns**

  * (::String) — Canonical resource name of the node that this machine is responsible for hosting e.g. projects/{project}/locations/{location}/clusters/{cluster_id}/nodePools/{pool_id}/{node}, Or empty if the machine is not assigned to assume the role of a node.

For control plane nodes hosted on edge machines, this will return the following format: "projects/{project}/locations/{location}/clusters/{cluster_id}/controlPlaneNodes/{node}". 




### #hosted_node=
    
    
    def hosted_node=(value) -> ::String

**Parameter**

  * **value** (::String) — Canonical resource name of the node that this machine is responsible for hosting e.g. projects/{project}/locations/{location}/clusters/{cluster_id}/nodePools/{pool_id}/{node}, Or empty if the machine is not assigned to assume the role of a node.

For control plane nodes hosted on edge machines, this will return the following format: "projects/{project}/locations/{location}/clusters/{cluster_id}/controlPlaneNodes/{node}". 




**Returns**

  * (::String) — Canonical resource name of the node that this machine is responsible for hosting e.g. projects/{project}/locations/{location}/clusters/{cluster_id}/nodePools/{pool_id}/{node}, Or empty if the machine is not assigned to assume the role of a node.

For control plane nodes hosted on edge machines, this will return the following format: "projects/{project}/locations/{location}/clusters/{cluster_id}/controlPlaneNodes/{node}". 




### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Labels associated with this resource. 



### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Labels associated with this resource. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Labels associated with this resource. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. The resource name of the machine. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the machine. 



**Returns**

  * (::String) — Required. The resource name of the machine. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_container-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time when the node pool was last updated. 



### #version
    
    
    def version() -> ::String

**Returns**

  * (::String) — Output only. The software version of the machine. 



### #zone
    
    
    def zone() -> ::String

**Returns**

  * (::String) — The Google Distributed Cloud Edge zone of this machine. 



### #zone=
    
    
    def zone=(value) -> ::String

**Parameter**

  * **value** (::String) — The Google Distributed Cloud Edge zone of this machine. 



**Returns**

  * (::String) — The Google Distributed Cloud Edge zone of this machine. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
