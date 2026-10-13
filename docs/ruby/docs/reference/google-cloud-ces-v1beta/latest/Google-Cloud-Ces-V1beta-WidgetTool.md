---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-WidgetTool/
title: Gemini Enterprise for Customer Experience V1BETA API - Class Google::Cloud::Ces::V1beta::WidgetTool (v1.0.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:13:42.379823+00:00
---

# Gemini Enterprise for Customer Experience V1BETA API - Class Google::Cloud::Ces::V1beta::WidgetTool (v1.0.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-WidgetTool/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience V1BETA API - Class Google::Cloud::Ces::V1beta::WidgetTool (v1.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.1 (latest)  1.0.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Gemini Enterprise for Customer Experience V1BETA API class Google::Cloud::Ces::V1beta::WidgetTool.

Represents a widget tool that the agent can invoke. When the tool is chosen by the agent, agent will return the widget to the client. The client is responsible for processing the widget and generating the next user query to continue the interaction with the agent.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #data_mapping
    
    
    def data_mapping() -> ::Google::Cloud::Ces::V1beta::WidgetTool::DataMapping

**Returns**

  * ([::Google::Cloud::Ces::V1beta::WidgetTool::DataMapping](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-WidgetTool-DataMapping)) — Optional. The mapping that defines how data from a source tool is mapped to the widget's input parameters. 



### #data_mapping=
    
    
    def data_mapping=(value) -> ::Google::Cloud::Ces::V1beta::WidgetTool::DataMapping

**Parameter**

  * **value** ([::Google::Cloud::Ces::V1beta::WidgetTool::DataMapping](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-WidgetTool-DataMapping)) — Optional. The mapping that defines how data from a source tool is mapped to the widget's input parameters. 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::WidgetTool::DataMapping](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-WidgetTool-DataMapping)) — Optional. The mapping that defines how data from a source tool is mapped to the widget's input parameters. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — Optional. The description of the widget tool. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The description of the widget tool. 



**Returns**

  * (::String) — Optional. The description of the widget tool. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. The display name of the widget tool. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The display name of the widget tool. 



**Returns**

  * (::String) — Required. The display name of the widget tool. 



### #parameters
    
    
    def parameters() -> ::Google::Cloud::Ces::V1beta::Schema

**Returns**

  * ([::Google::Cloud::Ces::V1beta::Schema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Schema)) — Optional. The input parameters of the widget tool. 



### #parameters=
    
    
    def parameters=(value) -> ::Google::Cloud::Ces::V1beta::Schema

**Parameter**

  * **value** ([::Google::Cloud::Ces::V1beta::Schema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Schema)) — Optional. The input parameters of the widget tool. 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::Schema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-Schema)) — Optional. The input parameters of the widget tool. 



### #text_response_config
    
    
    def text_response_config() -> ::Google::Cloud::Ces::V1beta::WidgetTool::TextResponseConfig

**Returns**

  * ([::Google::Cloud::Ces::V1beta::WidgetTool::TextResponseConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-WidgetTool-TextResponseConfig)) — Optional. Configuration for always-included text responses. 



### #text_response_config=
    
    
    def text_response_config=(value) -> ::Google::Cloud::Ces::V1beta::WidgetTool::TextResponseConfig

**Parameter**

  * **value** ([::Google::Cloud::Ces::V1beta::WidgetTool::TextResponseConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-WidgetTool-TextResponseConfig)) — Optional. Configuration for always-included text responses. 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::WidgetTool::TextResponseConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-WidgetTool-TextResponseConfig)) — Optional. Configuration for always-included text responses. 



### #ui_config
    
    
    def ui_config() -> ::Google::Protobuf::Struct

**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Protobuf-Struct)) — Optional. Configuration for rendering the widget. 



### #ui_config=
    
    
    def ui_config=(value) -> ::Google::Protobuf::Struct

**Parameter**

  * **value** ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Protobuf-Struct)) — Optional. Configuration for rendering the widget. 



**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Protobuf-Struct)) — Optional. Configuration for rendering the widget. 



### #widget_type
    
    
    def widget_type() -> ::Google::Cloud::Ces::V1beta::WidgetTool::WidgetType

**Returns**

  * ([::Google::Cloud::Ces::V1beta::WidgetTool::WidgetType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-WidgetTool-WidgetType)) — Optional. The type of the widget tool. If not specified, the default type will be CUSTOMIZED. 



### #widget_type=
    
    
    def widget_type=(value) -> ::Google::Cloud::Ces::V1beta::WidgetTool::WidgetType

**Parameter**

  * **value** ([::Google::Cloud::Ces::V1beta::WidgetTool::WidgetType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-WidgetTool-WidgetType)) — Optional. The type of the widget tool. If not specified, the default type will be CUSTOMIZED. 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::WidgetTool::WidgetType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-WidgetTool-WidgetType)) — Optional. The type of the widget tool. If not specified, the default type will be CUSTOMIZED. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
