---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-Node-InputEdge/
title: Vision AI V1 API - Class Google::Cloud::VisionAI::V1::Node::InputEdge (v1.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:09:32.946649+00:00
---

# Vision AI V1 API - Class Google::Cloud::VisionAI::V1::Node::InputEdge (v1.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-Node-InputEdge/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Vision AI V1 API - Class Google::Cloud::VisionAI::V1::Node::InputEdge (v1.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.1 (latest)  1.5.0  1.4.1  1.3.1  1.2.0  1.1.1  1.0.1  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Vision AI V1 API class Google::Cloud::VisionAI::V1::Node::InputEdge.

Message describing one edge pointing into a node.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #connected_input_channel
    
    
    def connected_input_channel() -> ::String

**Returns**

  * (::String) — The connected input channel of the current node's processor. It can be omitted if target processor only has 1 input channel. 



### #connected_input_channel=
    
    
    def connected_input_channel=(value) -> ::String

**Parameter**

  * **value** (::String) — The connected input channel of the current node's processor. It can be omitted if target processor only has 1 input channel. 



**Returns**

  * (::String) — The connected input channel of the current node's processor. It can be omitted if target processor only has 1 input channel. 



### #parent_node
    
    
    def parent_node() -> ::String

**Returns**

  * (::String) — The name of the parent node. 



### #parent_node=
    
    
    def parent_node=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of the parent node. 



**Returns**

  * (::String) — The name of the parent node. 



### #parent_output_channel
    
    
    def parent_output_channel() -> ::String

**Returns**

  * (::String) — The connected output artifact of the parent node. It can be omitted if target processor only has 1 output artifact. 



### #parent_output_channel=
    
    
    def parent_output_channel=(value) -> ::String

**Parameter**

  * **value** (::String) — The connected output artifact of the parent node. It can be omitted if target processor only has 1 output artifact. 



**Returns**

  * (::String) — The connected output artifact of the parent node. It can be omitted if target processor only has 1 output artifact. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
