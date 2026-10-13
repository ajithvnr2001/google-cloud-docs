---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-EdgePattern/
title: App Topology V1 API - Class Google::Cloud::AppTopology::V1::EdgePattern (v0.1.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:02:51.685820+00:00
---

# App Topology V1 API - Class Google::Cloud::AppTopology::V1::EdgePattern (v0.1.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-EdgePattern/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  App Topology V1 API - Class Google::Cloud::AppTopology::V1::EdgePattern (v0.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

Reference documentation and code samples for the App Topology V1 API class Google::Cloud::AppTopology::V1::EdgePattern.

Edge pattern matcher to match the edge direction, labels and properties.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #alias
    
    
    def alias() -> ::String

**Returns**

  * (::String) — Optional. Represents an identifier to be referenced in `property_matcher_expr`. For example, an alias for `edge` can be referenced as `edge.description = "value_1"`. `alias` must be unique within the query, otherwise an error will be returned. 



### #alias=
    
    
    def alias=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Represents an identifier to be referenced in `property_matcher_expr`. For example, an alias for `edge` can be referenced as `edge.description = "value_1"`. `alias` must be unique within the query, otherwise an error will be returned. 



**Returns**

  * (::String) — Optional. Represents an identifier to be referenced in `property_matcher_expr`. For example, an alias for `edge` can be referenced as `edge.description = "value_1"`. `alias` must be unique within the query, otherwise an error will be returned. 



### #direction
    
    
    def direction() -> ::Google::Cloud::AppTopology::V1::EdgePattern::Direction

**Returns**

  * ([::Google::Cloud::AppTopology::V1::EdgePattern::Direction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-EdgePattern-Direction)) — Required. The direction of the edge to match. 



### #direction=
    
    
    def direction=(value) -> ::Google::Cloud::AppTopology::V1::EdgePattern::Direction

**Parameter**

  * **value** ([::Google::Cloud::AppTopology::V1::EdgePattern::Direction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-EdgePattern-Direction)) — Required. The direction of the edge to match. 



**Returns**

  * ([::Google::Cloud::AppTopology::V1::EdgePattern::Direction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-EdgePattern-Direction)) — Required. The direction of the edge to match. 



### #label_properties_pattern
    
    
    def label_properties_pattern() -> ::Google::Cloud::AppTopology::V1::LabelPropertiesPattern

**Returns**

  * ([::Google::Cloud::AppTopology::V1::LabelPropertiesPattern](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-LabelPropertiesPattern)) — Required. Matcher for labels/properties. 



### #label_properties_pattern=
    
    
    def label_properties_pattern=(value) -> ::Google::Cloud::AppTopology::V1::LabelPropertiesPattern

**Parameter**

  * **value** ([::Google::Cloud::AppTopology::V1::LabelPropertiesPattern](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-LabelPropertiesPattern)) — Required. Matcher for labels/properties. 



**Returns**

  * ([::Google::Cloud::AppTopology::V1::LabelPropertiesPattern](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-LabelPropertiesPattern)) — Required. Matcher for labels/properties. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
