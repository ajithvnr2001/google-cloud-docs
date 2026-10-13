---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ConsistentHashLoadBalancerSettings/
title: Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::ConsistentHashLoadBalancerSettings (v4.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:11:20.152348+00:00
---

# Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::ConsistentHashLoadBalancerSettings (v4.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ConsistentHashLoadBalancerSettings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::ConsistentHashLoadBalancerSettings (v4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.12.0  3.10.0  3.9.1  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.22.0  2.21.1  2.20.0  2.19.1  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.5.0 

Reference documentation and code samples for the Google Cloud Compute V1 API class Google::Cloud::Compute::V1::ConsistentHashLoadBalancerSettings.

This message defines settings for a consistent hash style load balancer.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #http_cookie
    
    
    def http_cookie() -> ::Google::Cloud::Compute::V1::ConsistentHashLoadBalancerSettingsHttpCookie

**Returns**

  * ([::Google::Cloud::Compute::V1::ConsistentHashLoadBalancerSettingsHttpCookie](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ConsistentHashLoadBalancerSettingsHttpCookie)) — Hash is based on HTTP Cookie. This field describes a HTTP cookie that will be used as the hash key for the consistent hash load balancer. If the cookie is not present, it will be generated. This field is applicable if the sessionAffinity is set to HTTP_COOKIE.

Not supported when the backend service is referenced by a URL map that is bound to target gRPC proxy that has validateForProxyless field set to true. 




### #http_cookie=
    
    
    def http_cookie=(value) -> ::Google::Cloud::Compute::V1::ConsistentHashLoadBalancerSettingsHttpCookie

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::ConsistentHashLoadBalancerSettingsHttpCookie](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ConsistentHashLoadBalancerSettingsHttpCookie)) — Hash is based on HTTP Cookie. This field describes a HTTP cookie that will be used as the hash key for the consistent hash load balancer. If the cookie is not present, it will be generated. This field is applicable if the sessionAffinity is set to HTTP_COOKIE.

Not supported when the backend service is referenced by a URL map that is bound to target gRPC proxy that has validateForProxyless field set to true. 




**Returns**

  * ([::Google::Cloud::Compute::V1::ConsistentHashLoadBalancerSettingsHttpCookie](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ConsistentHashLoadBalancerSettingsHttpCookie)) — Hash is based on HTTP Cookie. This field describes a HTTP cookie that will be used as the hash key for the consistent hash load balancer. If the cookie is not present, it will be generated. This field is applicable if the sessionAffinity is set to HTTP_COOKIE.

Not supported when the backend service is referenced by a URL map that is bound to target gRPC proxy that has validateForProxyless field set to true. 




### #http_header_name
    
    
    def http_header_name() -> ::String

**Returns**

  * (::String) — The hash based on the value of the specified header field. This field is applicable if the sessionAffinity is set toHEADER_FIELD. 



### #http_header_name=
    
    
    def http_header_name=(value) -> ::String

**Parameter**

  * **value** (::String) — The hash based on the value of the specified header field. This field is applicable if the sessionAffinity is set toHEADER_FIELD. 



**Returns**

  * (::String) — The hash based on the value of the specified header field. This field is applicable if the sessionAffinity is set toHEADER_FIELD. 



### #minimum_ring_size
    
    
    def minimum_ring_size() -> ::Integer

**Returns**

  * (::Integer) — 

The minimum number of virtual nodes to use for the hash ring. Defaults to

    1. Larger ring sizes result in more granular load distributions. If the number of hosts in the load balancing pool is larger than the ring size, each host will be assigned a single virtual node.



### #minimum_ring_size=
    
    
    def minimum_ring_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — 

The minimum number of virtual nodes to use for the hash ring. Defaults to

    1. Larger ring sizes result in more granular load distributions. If the number of hosts in the load balancing pool is larger than the ring size, each host will be assigned a single virtual node.



**Returns**

  * (::Integer) — 

The minimum number of virtual nodes to use for the hash ring. Defaults to

    1. Larger ring sizes result in more granular load distributions. If the number of hosts in the load balancing pool is larger than the ring size, each host will be assigned a single virtual node.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
