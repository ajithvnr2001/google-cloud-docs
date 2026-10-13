---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-SessionClientConfiguration-ChannelPoolConfiguration/
title: Cloud Bigtable V2 API - Class Google::Cloud::Bigtable::V2::SessionClientConfiguration::ChannelPoolConfiguration (v1.18.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:14:46.662493+00:00
---

# Cloud Bigtable V2 API - Class Google::Cloud::Bigtable::V2::SessionClientConfiguration::ChannelPoolConfiguration (v1.18.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-SessionClientConfiguration-ChannelPoolConfiguration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Bigtable V2 API - Class Google::Cloud::Bigtable::V2::SessionClientConfiguration::ChannelPoolConfiguration (v1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.0  1.16.0  1.15.1  1.14.0  1.13.0  1.12.0  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.1  1.1.0  1.0.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.2  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.0  0.3.5 

Reference documentation and code samples for the Cloud Bigtable V2 API class Google::Cloud::Bigtable::V2::SessionClientConfiguration::ChannelPoolConfiguration.

Configuration for the channel pool.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #cloud_path_only
    
    
    def cloud_path_only() -> ::Google::Cloud::Bigtable::V2::SessionClientConfiguration::ChannelPoolConfiguration::CloudPathOnly

**Returns**

  * ([::Google::Cloud::Bigtable::V2::SessionClientConfiguration::ChannelPoolConfiguration::CloudPathOnly](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-SessionClientConfiguration-ChannelPoolConfiguration-CloudPathOnly)) — CloudPath only.

Note: The following fields are mutually exclusive: `cloud_path_only`, `direct_access_with_fallback`, `direct_access_only`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #cloud_path_only=
    
    
    def cloud_path_only=(value) -> ::Google::Cloud::Bigtable::V2::SessionClientConfiguration::ChannelPoolConfiguration::CloudPathOnly

**Parameter**

  * **value** ([::Google::Cloud::Bigtable::V2::SessionClientConfiguration::ChannelPoolConfiguration::CloudPathOnly](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-SessionClientConfiguration-ChannelPoolConfiguration-CloudPathOnly)) — CloudPath only.

Note: The following fields are mutually exclusive: `cloud_path_only`, `direct_access_with_fallback`, `direct_access_only`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Bigtable::V2::SessionClientConfiguration::ChannelPoolConfiguration::CloudPathOnly](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-SessionClientConfiguration-ChannelPoolConfiguration-CloudPathOnly)) — CloudPath only.

Note: The following fields are mutually exclusive: `cloud_path_only`, `direct_access_with_fallback`, `direct_access_only`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #direct_access_only
    
    
    def direct_access_only() -> ::Google::Cloud::Bigtable::V2::SessionClientConfiguration::ChannelPoolConfiguration::DirectAccessOnly

**Returns**

  * ([::Google::Cloud::Bigtable::V2::SessionClientConfiguration::ChannelPoolConfiguration::DirectAccessOnly](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-SessionClientConfiguration-ChannelPoolConfiguration-DirectAccessOnly)) — DirectAccess only.

Note: The following fields are mutually exclusive: `direct_access_only`, `direct_access_with_fallback`, `cloud_path_only`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #direct_access_only=
    
    
    def direct_access_only=(value) -> ::Google::Cloud::Bigtable::V2::SessionClientConfiguration::ChannelPoolConfiguration::DirectAccessOnly

**Parameter**

  * **value** ([::Google::Cloud::Bigtable::V2::SessionClientConfiguration::ChannelPoolConfiguration::DirectAccessOnly](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-SessionClientConfiguration-ChannelPoolConfiguration-DirectAccessOnly)) — DirectAccess only.

Note: The following fields are mutually exclusive: `direct_access_only`, `direct_access_with_fallback`, `cloud_path_only`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Bigtable::V2::SessionClientConfiguration::ChannelPoolConfiguration::DirectAccessOnly](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-SessionClientConfiguration-ChannelPoolConfiguration-DirectAccessOnly)) — DirectAccess only.

Note: The following fields are mutually exclusive: `direct_access_only`, `direct_access_with_fallback`, `cloud_path_only`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #direct_access_with_fallback
    
    
    def direct_access_with_fallback() -> ::Google::Cloud::Bigtable::V2::SessionClientConfiguration::ChannelPoolConfiguration::DirectAccessWithFallback

**Returns**

  * ([::Google::Cloud::Bigtable::V2::SessionClientConfiguration::ChannelPoolConfiguration::DirectAccessWithFallback](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-SessionClientConfiguration-ChannelPoolConfiguration-DirectAccessWithFallback)) — DirectAccess with a fallback to CloudPath.

Note: The following fields are mutually exclusive: `direct_access_with_fallback`, `direct_access_only`, `cloud_path_only`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #direct_access_with_fallback=
    
    
    def direct_access_with_fallback=(value) -> ::Google::Cloud::Bigtable::V2::SessionClientConfiguration::ChannelPoolConfiguration::DirectAccessWithFallback

**Parameter**

  * **value** ([::Google::Cloud::Bigtable::V2::SessionClientConfiguration::ChannelPoolConfiguration::DirectAccessWithFallback](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-SessionClientConfiguration-ChannelPoolConfiguration-DirectAccessWithFallback)) — DirectAccess with a fallback to CloudPath.

Note: The following fields are mutually exclusive: `direct_access_with_fallback`, `direct_access_only`, `cloud_path_only`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Bigtable::V2::SessionClientConfiguration::ChannelPoolConfiguration::DirectAccessWithFallback](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-SessionClientConfiguration-ChannelPoolConfiguration-DirectAccessWithFallback)) — DirectAccess with a fallback to CloudPath.

Note: The following fields are mutually exclusive: `direct_access_with_fallback`, `direct_access_only`, `cloud_path_only`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #max_server_count
    
    
    def max_server_count() -> ::Integer

**Returns**

  * (::Integer) — The maximum number of distinct servers to connect to in the channel pool. The client will ensure that the channel pool will have at most this many distinct servers. 



### #max_server_count=
    
    
    def max_server_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The maximum number of distinct servers to connect to in the channel pool. The client will ensure that the channel pool will have at most this many distinct servers. 



**Returns**

  * (::Integer) — The maximum number of distinct servers to connect to in the channel pool. The client will ensure that the channel pool will have at most this many distinct servers. 



### #min_server_count
    
    
    def min_server_count() -> ::Integer

**Returns**

  * (::Integer) — The minimum number of distcint servers to connect to in the channel pool. The client will ensure that the channel pool will have at least this many distinct servers, but may have multiple channels connected to the same server (e.g. the client may have M channels on N machines, where M > N). 



### #min_server_count=
    
    
    def min_server_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The minimum number of distcint servers to connect to in the channel pool. The client will ensure that the channel pool will have at least this many distinct servers, but may have multiple channels connected to the same server (e.g. the client may have M channels on N machines, where M > N). 



**Returns**

  * (::Integer) — The minimum number of distcint servers to connect to in the channel pool. The client will ensure that the channel pool will have at least this many distinct servers, but may have multiple channels connected to the same server (e.g. the client may have M channels on N machines, where M > N). 



### #per_server_session_count
    
    
    def per_server_session_count() -> ::Integer

**Returns**

  * (::Integer) — Soft maximum for how many sessions are allowed per server. Normally, the client will ensure that it does not host more than this count of sessions per server, unless there are other limits encountered (e.g. the connected servers is already at max_servers). 



### #per_server_session_count=
    
    
    def per_server_session_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Soft maximum for how many sessions are allowed per server. Normally, the client will ensure that it does not host more than this count of sessions per server, unless there are other limits encountered (e.g. the connected servers is already at max_servers). 



**Returns**

  * (::Integer) — Soft maximum for how many sessions are allowed per server. Normally, the client will ensure that it does not host more than this count of sessions per server, unless there are other limits encountered (e.g. the connected servers is already at max_servers). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
