---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_usage-v1/latest/Google-Api-Endpoint/
title: Service Usage V1 API - Class Google::Api::Endpoint (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:07:15.298974+00:00
---

# Service Usage V1 API - Class Google::Api::Endpoint (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_usage-v1/latest/Google-Api-Endpoint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Service Usage V1 API - Class Google::Api::Endpoint (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.1  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.7.0  0.6.2  0.5.0  0.4.0  0.3.1  0.2.1  0.1.4 

Reference documentation and code samples for the Service Usage V1 API class Google::Api::Endpoint.

`Endpoint` describes a network address of a service that serves a set of APIs. It is commonly known as a service endpoint. A service may expose any number of service endpoints, and all service endpoints share the same service definition, such as quota limits and monitoring metrics.

Example:
    
    
    type: google.api.Service
    name: library-example.googleapis.com
    endpoints:
      # Declares network address `https://library-example.googleapis.com`
      # for service `library-example.googleapis.com`. The `https` scheme
      # is implicit for all service endpoints. Other schemes may be
      # supported in the future.
    - name: library-example.googleapis.com
      allow_cors: false
    - name: content-staging-library-example.googleapis.com
      # Allows HTTP OPTIONS calls to be passed to the API frontend, for it
      # to decide whether the subsequent cross-origin request is allowed
      # to proceed.
      allow_cors: true
    

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #aliases
    
    
    def aliases() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Aliases for this endpoint, these will be served by the same UrlMap as the parent endpoint, and will be provisioned in the GCP stack for the Regional Endpoints. 



### #aliases=
    
    
    def aliases=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Aliases for this endpoint, these will be served by the same UrlMap as the parent endpoint, and will be provisioned in the GCP stack for the Regional Endpoints. 



**Returns**

  * (::Array<::String>) — Aliases for this endpoint, these will be served by the same UrlMap as the parent endpoint, and will be provisioned in the GCP stack for the Regional Endpoints. 



### #allow_cors
    
    
    def allow_cors() -> ::Boolean

**Returns**

  * (::Boolean) — Allowing [CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing), aka cross-domain traffic, would allow the backends served from this endpoint to receive and respond to HTTP OPTIONS requests. The response will be used by the browser to determine whether the subsequent cross-origin request is allowed to proceed. 



### #allow_cors=
    
    
    def allow_cors=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Allowing [CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing), aka cross-domain traffic, would allow the backends served from this endpoint to receive and respond to HTTP OPTIONS requests. The response will be used by the browser to determine whether the subsequent cross-origin request is allowed to proceed. 



**Returns**

  * (::Boolean) — Allowing [CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing), aka cross-domain traffic, would allow the backends served from this endpoint to receive and respond to HTTP OPTIONS requests. The response will be used by the browser to determine whether the subsequent cross-origin request is allowed to proceed. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — The canonical name of this endpoint. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — The canonical name of this endpoint. 



**Returns**

  * (::String) — The canonical name of this endpoint. 



### #target
    
    
    def target() -> ::String

**Returns**

  * (::String) — The specification of an Internet routable address of API frontend that will handle requests to this [API Endpoint](https://cloud.google.com/apis/design/glossary). It should be either a valid IPv4 address or a fully-qualified domain name. For example, "8.8.8.8" or "myservice.appspot.com". 



### #target=
    
    
    def target=(value) -> ::String

**Parameter**

  * **value** (::String) — The specification of an Internet routable address of API frontend that will handle requests to this [API Endpoint](https://cloud.google.com/apis/design/glossary). It should be either a valid IPv4 address or a fully-qualified domain name. For example, "8.8.8.8" or "myservice.appspot.com". 



**Returns**

  * (::String) — The specification of an Internet routable address of API frontend that will handle requests to this [API Endpoint](https://cloud.google.com/apis/design/glossary). It should be either a valid IPv4 address or a fully-qualified domain name. For example, "8.8.8.8" or "myservice.appspot.com". 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
