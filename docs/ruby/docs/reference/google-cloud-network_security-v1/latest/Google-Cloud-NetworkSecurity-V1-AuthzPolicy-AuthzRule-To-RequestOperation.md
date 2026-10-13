---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy-AuthzRule-To-RequestOperation/
title: Network Security V1 API - Class Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::To::RequestOperation (v0.1.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:12:03.139410+00:00
---

# Network Security V1 API - Class Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::To::RequestOperation (v0.1.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy-AuthzRule-To-RequestOperation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Network Security V1 API - Class Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::To::RequestOperation (v0.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

Reference documentation and code samples for the Network Security V1 API class Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::To::RequestOperation.

Describes properties of one or more targets of a request.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #header_set
    
    
    def header_set() -> ::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::To::RequestOperation::HeaderSet

**Returns**

  * ([::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::To::RequestOperation::HeaderSet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy-AuthzRule-To-RequestOperation-HeaderSet)) — Optional. A list of headers to match against in http header. 



### #header_set=
    
    
    def header_set=(value) -> ::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::To::RequestOperation::HeaderSet

**Parameter**

  * **value** ([::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::To::RequestOperation::HeaderSet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy-AuthzRule-To-RequestOperation-HeaderSet)) — Optional. A list of headers to match against in http header. 



**Returns**

  * ([::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::To::RequestOperation::HeaderSet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy-AuthzRule-To-RequestOperation-HeaderSet)) — Optional. A list of headers to match against in http header. 



### #hosts
    
    
    def hosts() -> ::Array<::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::StringMatch>

**Returns**

  * (::Array<[::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::StringMatch](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy-AuthzRule-StringMatch)>) — Optional. A list of HTTP Hosts to match against. The match can be one of exact, prefix, suffix, or contains (substring match). Matches are always case sensitive unless the ignoreCase is set. Limited to 10 hosts per Authorization Policy. 



### #hosts=
    
    
    def hosts=(value) -> ::Array<::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::StringMatch>

**Parameter**

  * **value** (::Array<[::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::StringMatch](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy-AuthzRule-StringMatch)>) — Optional. A list of HTTP Hosts to match against. The match can be one of exact, prefix, suffix, or contains (substring match). Matches are always case sensitive unless the ignoreCase is set. Limited to 10 hosts per Authorization Policy. 



**Returns**

  * (::Array<[::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::StringMatch](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy-AuthzRule-StringMatch)>) — Optional. A list of HTTP Hosts to match against. The match can be one of exact, prefix, suffix, or contains (substring match). Matches are always case sensitive unless the ignoreCase is set. Limited to 10 hosts per Authorization Policy. 



### #mcp
    
    
    def mcp() -> ::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::To::RequestOperation::MCP

**Returns**

  * ([::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::To::RequestOperation::MCP](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy-AuthzRule-To-RequestOperation-MCP)) — Optional. Defines the MCP protocol attributes to match on. If the MCP payload in the request body cannot be successfully parsed, the request will be denied. This field can be set only for AuthzPolicies targeting AgentGateway resources. 



### #mcp=
    
    
    def mcp=(value) -> ::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::To::RequestOperation::MCP

**Parameter**

  * **value** ([::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::To::RequestOperation::MCP](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy-AuthzRule-To-RequestOperation-MCP)) — Optional. Defines the MCP protocol attributes to match on. If the MCP payload in the request body cannot be successfully parsed, the request will be denied. This field can be set only for AuthzPolicies targeting AgentGateway resources. 



**Returns**

  * ([::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::To::RequestOperation::MCP](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy-AuthzRule-To-RequestOperation-MCP)) — Optional. Defines the MCP protocol attributes to match on. If the MCP payload in the request body cannot be successfully parsed, the request will be denied. This field can be set only for AuthzPolicies targeting AgentGateway resources. 



### #methods
    
    
    def methods() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. A list of HTTP methods to match against. Each entry must be a valid HTTP method name (GET, PUT, POST, HEAD, PATCH, DELETE, OPTIONS). It only allows exact match and is always case sensitive. Limited to 10 methods per Authorization Policy. 



### #methods=
    
    
    def methods=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. A list of HTTP methods to match against. Each entry must be a valid HTTP method name (GET, PUT, POST, HEAD, PATCH, DELETE, OPTIONS). It only allows exact match and is always case sensitive. Limited to 10 methods per Authorization Policy. 



**Returns**

  * (::Array<::String>) — Optional. A list of HTTP methods to match against. Each entry must be a valid HTTP method name (GET, PUT, POST, HEAD, PATCH, DELETE, OPTIONS). It only allows exact match and is always case sensitive. Limited to 10 methods per Authorization Policy. 



### #paths
    
    
    def paths() -> ::Array<::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::StringMatch>

**Returns**

  * (::Array<[::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::StringMatch](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy-AuthzRule-StringMatch)>) — Optional. A list of paths to match against. The match can be one of exact, prefix, suffix, or contains (substring match). Matches are always case sensitive unless the ignoreCase is set. Limited to 10 paths per Authorization Policy. Note that this path match includes the query parameters. For gRPC services, this should be a fully-qualified name of the form /package.service/method. 



### #paths=
    
    
    def paths=(value) -> ::Array<::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::StringMatch>

**Parameter**

  * **value** (::Array<[::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::StringMatch](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy-AuthzRule-StringMatch)>) — Optional. A list of paths to match against. The match can be one of exact, prefix, suffix, or contains (substring match). Matches are always case sensitive unless the ignoreCase is set. Limited to 10 paths per Authorization Policy. Note that this path match includes the query parameters. For gRPC services, this should be a fully-qualified name of the form /package.service/method. 



**Returns**

  * (::Array<[::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::StringMatch](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy-AuthzRule-StringMatch)>) — Optional. A list of paths to match against. The match can be one of exact, prefix, suffix, or contains (substring match). Matches are always case sensitive unless the ignoreCase is set. Limited to 10 paths per Authorization Policy. Note that this path match includes the query parameters. For gRPC services, this should be a fully-qualified name of the form /package.service/method. 



### #snis
    
    
    def snis() -> ::Array<::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::StringMatch>

**Returns**

  * (::Array<[::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::StringMatch](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy-AuthzRule-StringMatch)>) — Optional. A list of SNIs to match against. The match can be one of exact, prefix, suffix, or contains (substring match). If there is no SNI (i.e. plaintext HTTP traffic), the request will be denied. Matches are always case sensitive unless the ignoreCase is set. Limited to 10 SNIs per Authorization Policy. 



### #snis=
    
    
    def snis=(value) -> ::Array<::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::StringMatch>

**Parameter**

  * **value** (::Array<[::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::StringMatch](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy-AuthzRule-StringMatch)>) — Optional. A list of SNIs to match against. The match can be one of exact, prefix, suffix, or contains (substring match). If there is no SNI (i.e. plaintext HTTP traffic), the request will be denied. Matches are always case sensitive unless the ignoreCase is set. Limited to 10 SNIs per Authorization Policy. 



**Returns**

  * (::Array<[::Google::Cloud::NetworkSecurity::V1::AuthzPolicy::AuthzRule::StringMatch](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-AuthzPolicy-AuthzRule-StringMatch)>) — Optional. A list of SNIs to match against. The match can be one of exact, prefix, suffix, or contains (substring match). If there is no SNI (i.e. plaintext HTTP traffic), the request will be denied. Matches are always case sensitive unless the ignoreCase is set. Limited to 10 SNIs per Authorization Policy. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-07 UTC."],[],[]] 
