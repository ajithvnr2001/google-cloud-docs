---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-PlanNode/
title: Cloud Spanner V1 API - Class Google::Cloud::Spanner::V1::PlanNode (v1.19.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:53:06.001814+00:00
---

# Cloud Spanner V1 API - Class Google::Cloud::Spanner::V1::PlanNode (v1.19.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-PlanNode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Spanner V1 API - Class Google::Cloud::Spanner::V1::PlanNode (v1.19.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.19.2 (latest)  1.19.1  1.18.0  1.17.1  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.1  1.10.1  1.9.1  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.2  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.2  0.21.0  0.20.1  0.19.0  0.18.0  0.17.0  0.16.0  0.15.1  0.14.1  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.1  0.7.4 

Reference documentation and code samples for the Cloud Spanner V1 API class Google::Cloud::Spanner::V1::PlanNode.

Node information for nodes appearing in a [QueryPlan.plan_nodes](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-QueryPlan#Google__Cloud__Spanner__V1__QueryPlan_plan_nodes_instance_ "Google::Cloud::Spanner::V1::QueryPlan#plan_nodes \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #child_links
    
    
    def child_links() -> ::Array<::Google::Cloud::Spanner::V1::PlanNode::ChildLink>

**Returns**

  * (::Array<[::Google::Cloud::Spanner::V1::PlanNode::ChildLink](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-PlanNode-ChildLink)>) — List of child node `index`es and their relationship to this parent. 



### #child_links=
    
    
    def child_links=(value) -> ::Array<::Google::Cloud::Spanner::V1::PlanNode::ChildLink>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Spanner::V1::PlanNode::ChildLink](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-PlanNode-ChildLink)>) — List of child node `index`es and their relationship to this parent. 



**Returns**

  * (::Array<[::Google::Cloud::Spanner::V1::PlanNode::ChildLink](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-PlanNode-ChildLink)>) — List of child node `index`es and their relationship to this parent. 



### #display_name
    
    
    def display_name() -> ::String

**Returns**

  * (::String) — The display name for the node. 



### #display_name=
    
    
    def display_name=(value) -> ::String

**Parameter**

  * **value** (::String) — The display name for the node. 



**Returns**

  * (::String) — The display name for the node. 



### #execution_stats
    
    
    def execution_stats() -> ::Google::Protobuf::Struct

**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Protobuf-Struct)) — The execution statistics associated with the node, contained in a group of key-value pairs. Only present if the plan was returned as a result of a profile query. For example, number of executions, number of rows/time per execution etc. 



### #execution_stats=
    
    
    def execution_stats=(value) -> ::Google::Protobuf::Struct

**Parameter**

  * **value** ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Protobuf-Struct)) — The execution statistics associated with the node, contained in a group of key-value pairs. Only present if the plan was returned as a result of a profile query. For example, number of executions, number of rows/time per execution etc. 



**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Protobuf-Struct)) — The execution statistics associated with the node, contained in a group of key-value pairs. Only present if the plan was returned as a result of a profile query. For example, number of executions, number of rows/time per execution etc. 



### #index
    
    
    def index() -> ::Integer

**Returns**

  * (::Integer) — The `PlanNode`'s index in [node list][google.spanner.v1.QueryPlan.plan_nodes]. 



### #index=
    
    
    def index=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The `PlanNode`'s index in [node list][google.spanner.v1.QueryPlan.plan_nodes]. 



**Returns**

  * (::Integer) — The `PlanNode`'s index in [node list][google.spanner.v1.QueryPlan.plan_nodes]. 



### #kind
    
    
    def kind() -> ::Google::Cloud::Spanner::V1::PlanNode::Kind

**Returns**

  * ([::Google::Cloud::Spanner::V1::PlanNode::Kind](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-PlanNode-Kind)) — Used to determine the type of node. May be needed for visualizing different kinds of nodes differently. For example, If the node is a [SCALAR](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-PlanNode-Kind#Google__Cloud__Spanner__V1__PlanNode__Kind__SCALAR "Google::Cloud::Spanner::V1::PlanNode::Kind::SCALAR \(constant\)") node, it will have a condensed representation which can be used to directly embed a description of the node in its parent. 



### #kind=
    
    
    def kind=(value) -> ::Google::Cloud::Spanner::V1::PlanNode::Kind

**Parameter**

  * **value** ([::Google::Cloud::Spanner::V1::PlanNode::Kind](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-PlanNode-Kind)) — Used to determine the type of node. May be needed for visualizing different kinds of nodes differently. For example, If the node is a [SCALAR](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-PlanNode-Kind#Google__Cloud__Spanner__V1__PlanNode__Kind__SCALAR "Google::Cloud::Spanner::V1::PlanNode::Kind::SCALAR \(constant\)") node, it will have a condensed representation which can be used to directly embed a description of the node in its parent. 



**Returns**

  * ([::Google::Cloud::Spanner::V1::PlanNode::Kind](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-PlanNode-Kind)) — Used to determine the type of node. May be needed for visualizing different kinds of nodes differently. For example, If the node is a [SCALAR](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-PlanNode-Kind#Google__Cloud__Spanner__V1__PlanNode__Kind__SCALAR "Google::Cloud::Spanner::V1::PlanNode::Kind::SCALAR \(constant\)") node, it will have a condensed representation which can be used to directly embed a description of the node in its parent. 



### #metadata
    
    
    def metadata() -> ::Google::Protobuf::Struct

**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Protobuf-Struct)) — 

Attributes relevant to the node contained in a group of key-value pairs. For example, a Parameter Reference node could have the following information in its metadata:
        
        {
          "parameter_reference": "param1",
          "parameter_type": "array"
        }
        




### #metadata=
    
    
    def metadata=(value) -> ::Google::Protobuf::Struct

**Parameter**

  * **value** ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Protobuf-Struct)) — 

Attributes relevant to the node contained in a group of key-value pairs. For example, a Parameter Reference node could have the following information in its metadata:
        
        {
          "parameter_reference": "param1",
          "parameter_type": "array"
        }
        




**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Protobuf-Struct)) — 

Attributes relevant to the node contained in a group of key-value pairs. For example, a Parameter Reference node could have the following information in its metadata:
        
        {
          "parameter_reference": "param1",
          "parameter_type": "array"
        }
        




### #short_representation
    
    
    def short_representation() -> ::Google::Cloud::Spanner::V1::PlanNode::ShortRepresentation

**Returns**

  * ([::Google::Cloud::Spanner::V1::PlanNode::ShortRepresentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-PlanNode-ShortRepresentation)) — Condensed representation for [SCALAR](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-PlanNode-Kind#Google__Cloud__Spanner__V1__PlanNode__Kind__SCALAR "Google::Cloud::Spanner::V1::PlanNode::Kind::SCALAR \(constant\)") nodes. 



### #short_representation=
    
    
    def short_representation=(value) -> ::Google::Cloud::Spanner::V1::PlanNode::ShortRepresentation

**Parameter**

  * **value** ([::Google::Cloud::Spanner::V1::PlanNode::ShortRepresentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-PlanNode-ShortRepresentation)) — Condensed representation for [SCALAR](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-PlanNode-Kind#Google__Cloud__Spanner__V1__PlanNode__Kind__SCALAR "Google::Cloud::Spanner::V1::PlanNode::Kind::SCALAR \(constant\)") nodes. 



**Returns**

  * ([::Google::Cloud::Spanner::V1::PlanNode::ShortRepresentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-PlanNode-ShortRepresentation)) — Condensed representation for [SCALAR](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-PlanNode-Kind#Google__Cloud__Spanner__V1__PlanNode__Kind__SCALAR "Google::Cloud::Spanner::V1::PlanNode::Kind::SCALAR \(constant\)") nodes. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
