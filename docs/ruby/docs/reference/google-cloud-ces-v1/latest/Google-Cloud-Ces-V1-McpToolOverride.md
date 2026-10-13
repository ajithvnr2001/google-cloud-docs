---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-McpToolOverride/
title: Gemini Enterprise for Customer Experience V1 API - Class Google::Cloud::Ces::V1::McpToolOverride (v1.0.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:23:04.647828+00:00
---

# Gemini Enterprise for Customer Experience V1 API - Class Google::Cloud::Ces::V1::McpToolOverride (v1.0.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-McpToolOverride/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience V1 API - Class Google::Cloud::Ces::V1::McpToolOverride (v1.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.1 (latest)  1.0.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Gemini Enterprise for Customer Experience V1 API class Google::Cloud::Ces::V1::McpToolOverride.

Overrides associated with a given tool in a Toolset. This enables "pinning" or "overriding" of tool definitions from the external dynamic server.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #description_override
    
    
    def description_override() -> ::String

**Returns**

  * (::String) — Optional. If present, this tool uses this description instead of the original description from the server. 



### #description_override=
    
    
    def description_override=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. If present, this tool uses this description instead of the original description from the server. 



**Returns**

  * (::String) — Optional. If present, this tool uses this description instead of the original description from the server. 



### #name_override
    
    
    def name_override() -> ::String

**Returns**

  * (::String) — Optional. If present, this tool uses this name in the Agent instead of the original name. This is primarily used as an alias if the MCP server offers poorly named tools. 



### #name_override=
    
    
    def name_override=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. If present, this tool uses this name in the Agent instead of the original name. This is primarily used as an alias if the MCP server offers poorly named tools. 



**Returns**

  * (::String) — Optional. If present, this tool uses this name in the Agent instead of the original name. This is primarily used as an alias if the MCP server offers poorly named tools. 



### #snapshot
    
    
    def snapshot() -> ::Google::Cloud::Ces::V1::McpToolDefinition

**Returns**

  * ([::Google::Cloud::Ces::V1::McpToolDefinition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-McpToolDefinition)) — Output only. If present, this tool is "Pinned" and uses the snapshot values as fallbacks if the server becomes temporarily unavailable or if no Override is present. 



### #tool
    
    
    def tool() -> ::String

**Returns**

  * (::String) — Required. The original name of the tool as it is emitted by the MCP server. 



### #tool=
    
    
    def tool=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The original name of the tool as it is emitted by the MCP server. 



**Returns**

  * (::String) — Required. The original name of the tool as it is emitted by the MCP server. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
