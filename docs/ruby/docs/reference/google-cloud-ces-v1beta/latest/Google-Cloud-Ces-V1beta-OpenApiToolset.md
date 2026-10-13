---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-OpenApiToolset/
title: Gemini Enterprise for Customer Experience V1BETA API - Class Google::Cloud::Ces::V1beta::OpenApiToolset (v1.0.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:22:28.920918+00:00
---

# Gemini Enterprise for Customer Experience V1BETA API - Class Google::Cloud::Ces::V1beta::OpenApiToolset (v1.0.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-OpenApiToolset/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience V1BETA API - Class Google::Cloud::Ces::V1beta::OpenApiToolset (v1.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.1 (latest)  1.0.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Gemini Enterprise for Customer Experience V1BETA API class Google::Cloud::Ces::V1beta::OpenApiToolset.

A toolset that contains a list of tools that are defined by an OpenAPI schema.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #api_authentication
    
    
    def api_authentication() -> ::Google::Cloud::Ces::V1beta::ApiAuthentication

**Returns**

  * ([::Google::Cloud::Ces::V1beta::ApiAuthentication](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ApiAuthentication)) — Optional. Authentication information required by the API. 



### #api_authentication=
    
    
    def api_authentication=(value) -> ::Google::Cloud::Ces::V1beta::ApiAuthentication

**Parameter**

  * **value** ([::Google::Cloud::Ces::V1beta::ApiAuthentication](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ApiAuthentication)) — Optional. Authentication information required by the API. 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::ApiAuthentication](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ApiAuthentication)) — Optional. Authentication information required by the API. 



### #ignore_unknown_fields
    
    
    def ignore_unknown_fields() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. If true, the agent will ignore unknown fields in the API response for all operations defined in the OpenAPI schema. 



### #ignore_unknown_fields=
    
    
    def ignore_unknown_fields=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. If true, the agent will ignore unknown fields in the API response for all operations defined in the OpenAPI schema. 



**Returns**

  * (::Boolean) — Optional. If true, the agent will ignore unknown fields in the API response for all operations defined in the OpenAPI schema. 



### #open_api_schema
    
    
    def open_api_schema() -> ::String

**Returns**

  * (::String) — Required. The OpenAPI schema of the toolset. 



### #open_api_schema=
    
    
    def open_api_schema=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The OpenAPI schema of the toolset. 



**Returns**

  * (::String) — Required. The OpenAPI schema of the toolset. 



### #service_directory_config
    
    
    def service_directory_config() -> ::Google::Cloud::Ces::V1beta::ServiceDirectoryConfig

**Returns**

  * ([::Google::Cloud::Ces::V1beta::ServiceDirectoryConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ServiceDirectoryConfig)) — Optional. Service Directory configuration. 



### #service_directory_config=
    
    
    def service_directory_config=(value) -> ::Google::Cloud::Ces::V1beta::ServiceDirectoryConfig

**Parameter**

  * **value** ([::Google::Cloud::Ces::V1beta::ServiceDirectoryConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ServiceDirectoryConfig)) — Optional. Service Directory configuration. 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::ServiceDirectoryConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ServiceDirectoryConfig)) — Optional. Service Directory configuration. 



### #tls_config
    
    
    def tls_config() -> ::Google::Cloud::Ces::V1beta::TlsConfig

**Returns**

  * ([::Google::Cloud::Ces::V1beta::TlsConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-TlsConfig)) — Optional. The TLS configuration. Includes the custom server certificates 



### #tls_config=
    
    
    def tls_config=(value) -> ::Google::Cloud::Ces::V1beta::TlsConfig

**Parameter**

  * **value** ([::Google::Cloud::Ces::V1beta::TlsConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-TlsConfig)) — Optional. The TLS configuration. Includes the custom server certificates 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::TlsConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-TlsConfig)) — Optional. The TLS configuration. Includes the custom server certificates 



### #url
    
    
    def url() -> ::String

**Returns**

  * (::String) — Optional. The server URL of the Open API schema. This field is only set in toolsets in the environment dependencies during the export process if the schema contains a server url. During the import process, if this url is present in the environment dependencies and the schema has the $env_var placeholder, it will replace the placeholder in the schema. 



### #url=
    
    
    def url=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The server URL of the Open API schema. This field is only set in toolsets in the environment dependencies during the export process if the schema contains a server url. During the import process, if this url is present in the environment dependencies and the schema has the $env_var placeholder, it will replace the placeholder in the schema. 



**Returns**

  * (::String) — Optional. The server URL of the Open API schema. This field is only set in toolsets in the environment dependencies during the export process if the schema contains a server url. During the import process, if this url is present in the environment dependencies and the schema has the $env_var placeholder, it will replace the placeholder in the schema. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
