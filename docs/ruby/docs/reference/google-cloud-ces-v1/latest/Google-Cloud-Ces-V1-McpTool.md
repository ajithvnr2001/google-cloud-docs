---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-McpTool/
title: Gemini Enterprise for Customer Experience V1 API - Class Google::Cloud::Ces::V1::McpTool (v1.0.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:29:16.203479+00:00
---

# Gemini Enterprise for Customer Experience V1 API - Class Google::Cloud::Ces::V1::McpTool (v1.0.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-McpTool/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience V1 API - Class Google::Cloud::Ces::V1::McpTool (v1.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.1 (latest)  1.0.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Gemini Enterprise for Customer Experience V1 API class Google::Cloud::Ces::V1::McpTool.

An MCP tool. See <https://modelcontextprotocol.io/specification/2025-06-18/server/tools> for more details.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #api_authentication
    
    
    def api_authentication() -> ::Google::Cloud::Ces::V1::ApiAuthentication

**Returns**

  * ([::Google::Cloud::Ces::V1::ApiAuthentication](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-ApiAuthentication)) — Optional. Authentication information required to execute the tool against the MCP server. For bearer token authentication, the token applies only to tool execution, not to listing tools. This requires that tools can be listed without authentication. 



### #api_authentication=
    
    
    def api_authentication=(value) -> ::Google::Cloud::Ces::V1::ApiAuthentication

**Parameter**

  * **value** ([::Google::Cloud::Ces::V1::ApiAuthentication](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-ApiAuthentication)) — Optional. Authentication information required to execute the tool against the MCP server. For bearer token authentication, the token applies only to tool execution, not to listing tools. This requires that tools can be listed without authentication. 



**Returns**

  * ([::Google::Cloud::Ces::V1::ApiAuthentication](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-ApiAuthentication)) — Optional. Authentication information required to execute the tool against the MCP server. For bearer token authentication, the token applies only to tool execution, not to listing tools. This requires that tools can be listed without authentication. 



### #custom_headers
    
    
    def custom_headers() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. The custom headers to send in the request to the MCP server. The values must be in the format `$context.variables.<name_of_variable>` and can be set in the session variables. See https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/tool/open-api#openapi-injection for more details. 



### #custom_headers=
    
    
    def custom_headers=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Optional. The custom headers to send in the request to the MCP server. The values must be in the format `$context.variables.<name_of_variable>` and can be set in the session variables. See https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/tool/open-api#openapi-injection for more details. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. The custom headers to send in the request to the MCP server. The values must be in the format `$context.variables.<name_of_variable>` and can be set in the session variables. See https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/tool/open-api#openapi-injection for more details. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — Optional. The description of the MCP tool. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The description of the MCP tool. 



**Returns**

  * (::String) — Optional. The description of the MCP tool. 



### #input_schema
    
    
    def input_schema() -> ::Google::Cloud::Ces::V1::Schema

**Returns**

  * ([::Google::Cloud::Ces::V1::Schema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-Schema)) — Optional. The schema of the input arguments of the MCP tool. 



### #input_schema=
    
    
    def input_schema=(value) -> ::Google::Cloud::Ces::V1::Schema

**Parameter**

  * **value** ([::Google::Cloud::Ces::V1::Schema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-Schema)) — Optional. The schema of the input arguments of the MCP tool. 



**Returns**

  * ([::Google::Cloud::Ces::V1::Schema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-Schema)) — Optional. The schema of the input arguments of the MCP tool. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. The name of the MCP tool. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The name of the MCP tool. 



**Returns**

  * (::String) — Required. The name of the MCP tool. 



### #name_override
    
    
    def name_override() -> ::String

**Returns**

  * (::String) — Optional. The name override of the MCP tool. This is populated if the name was overridden by a Toolset override. 



### #name_override=
    
    
    def name_override=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The name override of the MCP tool. This is populated if the name was overridden by a Toolset override. 



**Returns**

  * (::String) — Optional. The name override of the MCP tool. This is populated if the name was overridden by a Toolset override. 



### #output_schema
    
    
    def output_schema() -> ::Google::Cloud::Ces::V1::Schema

**Returns**

  * ([::Google::Cloud::Ces::V1::Schema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-Schema)) — Optional. The schema of the output arguments of the MCP tool. 



### #output_schema=
    
    
    def output_schema=(value) -> ::Google::Cloud::Ces::V1::Schema

**Parameter**

  * **value** ([::Google::Cloud::Ces::V1::Schema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-Schema)) — Optional. The schema of the output arguments of the MCP tool. 



**Returns**

  * ([::Google::Cloud::Ces::V1::Schema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-Schema)) — Optional. The schema of the output arguments of the MCP tool. 



### #server_address
    
    
    def server_address() -> ::String

**Returns**

  * (::String) — Required. The server address of the MCP server, e.g., "https://example.com/mcp/". If the server is built with the MCP SDK, the url should be suffixed with "/mcp/". Only Streamable HTTP transport based servers are supported. This is the same as the server_address in the McpToolset. See https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http for more details. 



### #server_address=
    
    
    def server_address=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The server address of the MCP server, e.g., "https://example.com/mcp/". If the server is built with the MCP SDK, the url should be suffixed with "/mcp/". Only Streamable HTTP transport based servers are supported. This is the same as the server_address in the McpToolset. See https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http for more details. 



**Returns**

  * (::String) — Required. The server address of the MCP server, e.g., "https://example.com/mcp/". If the server is built with the MCP SDK, the url should be suffixed with "/mcp/". Only Streamable HTTP transport based servers are supported. This is the same as the server_address in the McpToolset. See https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http for more details. 



### #service_directory_config
    
    
    def service_directory_config() -> ::Google::Cloud::Ces::V1::ServiceDirectoryConfig

**Returns**

  * ([::Google::Cloud::Ces::V1::ServiceDirectoryConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-ServiceDirectoryConfig)) — Optional. Service Directory configuration for VPC-SC, used to resolve service names within a perimeter. 



### #service_directory_config=
    
    
    def service_directory_config=(value) -> ::Google::Cloud::Ces::V1::ServiceDirectoryConfig

**Parameter**

  * **value** ([::Google::Cloud::Ces::V1::ServiceDirectoryConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-ServiceDirectoryConfig)) — Optional. Service Directory configuration for VPC-SC, used to resolve service names within a perimeter. 



**Returns**

  * ([::Google::Cloud::Ces::V1::ServiceDirectoryConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-ServiceDirectoryConfig)) — Optional. Service Directory configuration for VPC-SC, used to resolve service names within a perimeter. 



### #state
    
    
    def state() -> ::Google::Cloud::Ces::V1::McpTool::State

**Returns**

  * ([::Google::Cloud::Ces::V1::McpTool::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-McpTool-State)) — Output only. The dynamic availability state of the tool on the external server. 



### #tls_config
    
    
    def tls_config() -> ::Google::Cloud::Ces::V1::TlsConfig

**Returns**

  * ([::Google::Cloud::Ces::V1::TlsConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-TlsConfig)) — Optional. The TLS configuration. Includes the custom server certificates that the client should trust. 



### #tls_config=
    
    
    def tls_config=(value) -> ::Google::Cloud::Ces::V1::TlsConfig

**Parameter**

  * **value** ([::Google::Cloud::Ces::V1::TlsConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-TlsConfig)) — Optional. The TLS configuration. Includes the custom server certificates that the client should trust. 



**Returns**

  * ([::Google::Cloud::Ces::V1::TlsConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-TlsConfig)) — Optional. The TLS configuration. Includes the custom server certificates that the client should trust. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
