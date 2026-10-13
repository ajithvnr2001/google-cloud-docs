---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Api-HttpBody/
title: Retail V2 API - Class Google::Api::HttpBody (v2.10.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:47:56.923454+00:00
---

# Retail V2 API - Class Google::Api::HttpBody (v2.10.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Api-HttpBody/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Retail V2 API - Class Google::Api::HttpBody (v2.10.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.10.0 (latest)  2.9.0  2.8.1  2.7.0  2.6.1  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.3.0  1.2.0  1.1.0  1.0.1  0.21.0  0.20.0  0.19.0  0.18.2  0.17.0  0.16.1  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.4 

Reference documentation and code samples for the Retail V2 API class Google::Api::HttpBody.

Message that represents an arbitrary HTTP body. It should only be used for payload formats that can't be represented as JSON, such as raw binary or an HTML page.

This message can be used both in streaming and non-streaming API methods in the request as well as the response.

It can be used as a top-level request field, which is convenient if one wants to extract parameters from either the URL or HTTP template into the request fields and also want access to the raw HTTP body.

Example:
    
    
    message GetResourceRequest {
      // A unique request id.
      string request_id = 1;
    
      // The raw HTTP body is bound to this field.
      google.api.HttpBody http_body = 2;
    
    }
    
    service ResourceService {
      rpc GetResource(GetResourceRequest)
        returns (google.api.HttpBody);
      rpc UpdateResource(google.api.HttpBody)
        returns (google.protobuf.Empty);
    
    }
    

Example with streaming methods:
    
    
    service CaldavService {
      rpc GetCalendar(stream google.api.HttpBody)
        returns (stream google.api.HttpBody);
      rpc UpdateCalendar(stream google.api.HttpBody)
        returns (stream google.api.HttpBody);
    
    }
    

Use of this type only changes how the request and response bodies are handled, all other features will continue to work unchanged.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #content_type
    
    
    def content_type() -> ::String

**Returns**

  * (::String) — The HTTP Content-Type header value specifying the content type of the body. 



### #content_type=
    
    
    def content_type=(value) -> ::String

**Parameter**

  * **value** (::String) — The HTTP Content-Type header value specifying the content type of the body. 



**Returns**

  * (::String) — The HTTP Content-Type header value specifying the content type of the body. 



### #data
    
    
    def data() -> ::String

**Returns**

  * (::String) — The HTTP request/response body as raw binary. 



### #data=
    
    
    def data=(value) -> ::String

**Parameter**

  * **value** (::String) — The HTTP request/response body as raw binary. 



**Returns**

  * (::String) — The HTTP request/response body as raw binary. 



### #extensions
    
    
    def extensions() -> ::Array<::Google::Protobuf::Any>

**Returns**

  * (::Array<[::Google::Protobuf::Any](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Protobuf-Any)>) — Application specific response metadata. Must be set in the first response for streaming APIs. 



### #extensions=
    
    
    def extensions=(value) -> ::Array<::Google::Protobuf::Any>

**Parameter**

  * **value** (::Array<[::Google::Protobuf::Any](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Protobuf-Any)>) — Application specific response metadata. Must be set in the first response for streaming APIs. 



**Returns**

  * (::Array<[::Google::Protobuf::Any](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Protobuf-Any)>) — Application specific response metadata. Must be set in the first response for streaming APIs. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
