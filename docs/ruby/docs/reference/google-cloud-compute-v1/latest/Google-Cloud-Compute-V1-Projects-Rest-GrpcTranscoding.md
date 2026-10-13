---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Projects-Rest-GrpcTranscoding/
title: Google Cloud Compute V1 API - Module Google::Cloud::Compute::V1::Projects::Rest::GrpcTranscoding (v4.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:28:17.763497+00:00
---

# Google Cloud Compute V1 API - Module Google::Cloud::Compute::V1::Projects::Rest::GrpcTranscoding (v4.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Projects-Rest-GrpcTranscoding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Compute V1 API - Module Google::Cloud::Compute::V1::Projects::Rest::GrpcTranscoding (v4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.12.0  3.10.0  3.9.1  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.22.0  2.21.1  2.20.0  2.19.1  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.5.0 

Reference documentation and code samples for the Google Cloud Compute V1 API module Google::Cloud::Compute::V1::Projects::Rest::GrpcTranscoding.

GRPC transcoding helper methods for the Projects REST API.

## Extended By

  * [Google::Cloud::Compute::V1::Projects::Rest::GrpcTranscoding](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Projects-Rest-GrpcTranscoding)



## Included In

  * [Google::Cloud::Compute::V1::Projects::Rest::GrpcTranscoding](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Projects-Rest-GrpcTranscoding)



## Methods 

### #transcode_disable_xpn_host
    
    
    def transcode_disable_xpn_host(request_pb) -> Array(String, [String, nil], Hash{String => String})

**Parameter**

  * **request_pb** ([::Google::Cloud::Compute::V1::DisableXpnHostProjectRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-DisableXpnHostProjectRequest)) — A request object representing the call parameters. Required. 



**Returns**

  * (Array(String, [String, nil], Hash{String => String})) — Uri, Body, Query string parameters 



### #transcode_disable_xpn_resource
    
    
    def transcode_disable_xpn_resource(request_pb) -> Array(String, [String, nil], Hash{String => String})

**Parameter**

  * **request_pb** ([::Google::Cloud::Compute::V1::DisableXpnResourceProjectRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-DisableXpnResourceProjectRequest)) — A request object representing the call parameters. Required. 



**Returns**

  * (Array(String, [String, nil], Hash{String => String})) — Uri, Body, Query string parameters 



### #transcode_enable_xpn_host
    
    
    def transcode_enable_xpn_host(request_pb) -> Array(String, [String, nil], Hash{String => String})

**Parameter**

  * **request_pb** ([::Google::Cloud::Compute::V1::EnableXpnHostProjectRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-EnableXpnHostProjectRequest)) — A request object representing the call parameters. Required. 



**Returns**

  * (Array(String, [String, nil], Hash{String => String})) — Uri, Body, Query string parameters 



### #transcode_enable_xpn_resource
    
    
    def transcode_enable_xpn_resource(request_pb) -> Array(String, [String, nil], Hash{String => String})

**Parameter**

  * **request_pb** ([::Google::Cloud::Compute::V1::EnableXpnResourceProjectRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-EnableXpnResourceProjectRequest)) — A request object representing the call parameters. Required. 



**Returns**

  * (Array(String, [String, nil], Hash{String => String})) — Uri, Body, Query string parameters 



### #transcode_get
    
    
    def transcode_get(request_pb) -> Array(String, [String, nil], Hash{String => String})

**Parameter**

  * **request_pb** ([::Google::Cloud::Compute::V1::GetProjectRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GetProjectRequest)) — A request object representing the call parameters. Required. 



**Returns**

  * (Array(String, [String, nil], Hash{String => String})) — Uri, Body, Query string parameters 



### #transcode_get_xpn_host
    
    
    def transcode_get_xpn_host(request_pb) -> Array(String, [String, nil], Hash{String => String})

**Parameter**

  * **request_pb** ([::Google::Cloud::Compute::V1::GetXpnHostProjectRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GetXpnHostProjectRequest)) — A request object representing the call parameters. Required. 



**Returns**

  * (Array(String, [String, nil], Hash{String => String})) — Uri, Body, Query string parameters 



### #transcode_get_xpn_resources
    
    
    def transcode_get_xpn_resources(request_pb) -> Array(String, [String, nil], Hash{String => String})

**Parameter**

  * **request_pb** ([::Google::Cloud::Compute::V1::GetXpnResourcesProjectsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GetXpnResourcesProjectsRequest)) — A request object representing the call parameters. Required. 



**Returns**

  * (Array(String, [String, nil], Hash{String => String})) — Uri, Body, Query string parameters 



### #transcode_list_xpn_hosts
    
    
    def transcode_list_xpn_hosts(request_pb) -> Array(String, [String, nil], Hash{String => String})

**Parameter**

  * **request_pb** ([::Google::Cloud::Compute::V1::ListXpnHostsProjectsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ListXpnHostsProjectsRequest)) — A request object representing the call parameters. Required. 



**Returns**

  * (Array(String, [String, nil], Hash{String => String})) — Uri, Body, Query string parameters 



### #transcode_move_disk
    
    
    def transcode_move_disk(request_pb) -> Array(String, [String, nil], Hash{String => String})

**Parameter**

  * **request_pb** ([::Google::Cloud::Compute::V1::MoveDiskProjectRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-MoveDiskProjectRequest)) — A request object representing the call parameters. Required. 



**Returns**

  * (Array(String, [String, nil], Hash{String => String})) — Uri, Body, Query string parameters 



### #transcode_move_instance
    
    
    def transcode_move_instance(request_pb) -> Array(String, [String, nil], Hash{String => String})

**Parameter**

  * **request_pb** ([::Google::Cloud::Compute::V1::MoveInstanceProjectRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-MoveInstanceProjectRequest)) — A request object representing the call parameters. Required. 



**Returns**

  * (Array(String, [String, nil], Hash{String => String})) — Uri, Body, Query string parameters 



### #transcode_set_common_instance_metadata
    
    
    def transcode_set_common_instance_metadata(request_pb) -> Array(String, [String, nil], Hash{String => String})

**Parameter**

  * **request_pb** ([::Google::Cloud::Compute::V1::SetCommonInstanceMetadataProjectRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-SetCommonInstanceMetadataProjectRequest)) — A request object representing the call parameters. Required. 



**Returns**

  * (Array(String, [String, nil], Hash{String => String})) — Uri, Body, Query string parameters 



### #transcode_set_default_network_tier
    
    
    def transcode_set_default_network_tier(request_pb) -> Array(String, [String, nil], Hash{String => String})

**Parameter**

  * **request_pb** ([::Google::Cloud::Compute::V1::SetDefaultNetworkTierProjectRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-SetDefaultNetworkTierProjectRequest)) — A request object representing the call parameters. Required. 



**Returns**

  * (Array(String, [String, nil], Hash{String => String})) — Uri, Body, Query string parameters 



### #transcode_set_usage_export_bucket
    
    
    def transcode_set_usage_export_bucket(request_pb) -> Array(String, [String, nil], Hash{String => String})

**Parameter**

  * **request_pb** ([::Google::Cloud::Compute::V1::SetUsageExportBucketProjectRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-SetUsageExportBucketProjectRequest)) — A request object representing the call parameters. Required. 



**Returns**

  * (Array(String, [String, nil], Hash{String => String})) — Uri, Body, Query string parameters 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
