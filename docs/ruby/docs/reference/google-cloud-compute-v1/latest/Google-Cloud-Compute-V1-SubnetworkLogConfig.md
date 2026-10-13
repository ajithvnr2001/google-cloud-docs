---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-SubnetworkLogConfig/
title: Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::SubnetworkLogConfig (v4.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:44:35.256370+00:00
---

# Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::SubnetworkLogConfig (v4.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-SubnetworkLogConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::SubnetworkLogConfig (v4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.12.0  3.10.0  3.9.1  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.22.0  2.21.1  2.20.0  2.19.1  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.5.0 

Reference documentation and code samples for the Google Cloud Compute V1 API class Google::Cloud::Compute::V1::SubnetworkLogConfig.

The available logging options for this subnetwork.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #aggregation_interval
    
    
    def aggregation_interval() -> ::String

**Returns**

  * (::String) — Can only be specified if VPC flow logging for this subnetwork is enabled. Toggles the aggregation interval for collecting flow logs. Increasing the interval time will reduce the amount of generated flow logs for long lasting connections. Default is an interval of 5 seconds per connection. Check the AggregationInterval enum for the list of possible values. 



### #aggregation_interval=
    
    
    def aggregation_interval=(value) -> ::String

**Parameter**

  * **value** (::String) — Can only be specified if VPC flow logging for this subnetwork is enabled. Toggles the aggregation interval for collecting flow logs. Increasing the interval time will reduce the amount of generated flow logs for long lasting connections. Default is an interval of 5 seconds per connection. Check the AggregationInterval enum for the list of possible values. 



**Returns**

  * (::String) — Can only be specified if VPC flow logging for this subnetwork is enabled. Toggles the aggregation interval for collecting flow logs. Increasing the interval time will reduce the amount of generated flow logs for long lasting connections. Default is an interval of 5 seconds per connection. Check the AggregationInterval enum for the list of possible values. 



### #enable
    
    
    def enable() -> ::Boolean

**Returns**

  * (::Boolean) — Whether to enable flow logging for this subnetwork. If this field is not explicitly set, it will not appear in get listings. If not set the default behavior is determined by the org policy, if there is no org policy specified, then it will default to disabled. Flow logging isn't supported if the subnet purpose field is set to REGIONAL_MANAGED_PROXY. 



### #enable=
    
    
    def enable=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Whether to enable flow logging for this subnetwork. If this field is not explicitly set, it will not appear in get listings. If not set the default behavior is determined by the org policy, if there is no org policy specified, then it will default to disabled. Flow logging isn't supported if the subnet purpose field is set to REGIONAL_MANAGED_PROXY. 



**Returns**

  * (::Boolean) — Whether to enable flow logging for this subnetwork. If this field is not explicitly set, it will not appear in get listings. If not set the default behavior is determined by the org policy, if there is no org policy specified, then it will default to disabled. Flow logging isn't supported if the subnet purpose field is set to REGIONAL_MANAGED_PROXY. 



### #filter_expr
    
    
    def filter_expr() -> ::String

**Returns**

  * (::String) — Can only be specified if VPC flow logs for this subnetwork is enabled. The filter expression is used to define which VPC flow logs should be exported to Cloud Logging. 



### #filter_expr=
    
    
    def filter_expr=(value) -> ::String

**Parameter**

  * **value** (::String) — Can only be specified if VPC flow logs for this subnetwork is enabled. The filter expression is used to define which VPC flow logs should be exported to Cloud Logging. 



**Returns**

  * (::String) — Can only be specified if VPC flow logs for this subnetwork is enabled. The filter expression is used to define which VPC flow logs should be exported to Cloud Logging. 



### #flow_sampling
    
    
    def flow_sampling() -> ::Float

**Returns**

  * (::Float) — Can only be specified if VPC flow logging for this subnetwork is enabled. The value of the field must be in [0, 1]. Set the sampling rate of VPC flow logs within the subnetwork where 1.0 means all collected logs are reported and 0.0 means no logs are reported. Default is 0.5 unless otherwise specified by the org policy, which means half of all collected logs are reported. 



### #flow_sampling=
    
    
    def flow_sampling=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Can only be specified if VPC flow logging for this subnetwork is enabled. The value of the field must be in [0, 1]. Set the sampling rate of VPC flow logs within the subnetwork where 1.0 means all collected logs are reported and 0.0 means no logs are reported. Default is 0.5 unless otherwise specified by the org policy, which means half of all collected logs are reported. 



**Returns**

  * (::Float) — Can only be specified if VPC flow logging for this subnetwork is enabled. The value of the field must be in [0, 1]. Set the sampling rate of VPC flow logs within the subnetwork where 1.0 means all collected logs are reported and 0.0 means no logs are reported. Default is 0.5 unless otherwise specified by the org policy, which means half of all collected logs are reported. 



### #metadata
    
    
    def metadata() -> ::String

**Returns**

  * (::String) — Can only be specified if VPC flow logs for this subnetwork is enabled. Configures whether all, none or a subset of metadata fields should be added to the reported VPC flow logs. Default isEXCLUDE_ALL_METADATA. Check the Metadata enum for the list of possible values. 



### #metadata=
    
    
    def metadata=(value) -> ::String

**Parameter**

  * **value** (::String) — Can only be specified if VPC flow logs for this subnetwork is enabled. Configures whether all, none or a subset of metadata fields should be added to the reported VPC flow logs. Default isEXCLUDE_ALL_METADATA. Check the Metadata enum for the list of possible values. 



**Returns**

  * (::String) — Can only be specified if VPC flow logs for this subnetwork is enabled. Configures whether all, none or a subset of metadata fields should be added to the reported VPC flow logs. Default isEXCLUDE_ALL_METADATA. Check the Metadata enum for the list of possible values. 



### #metadata_fields
    
    
    def metadata_fields() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Can only be specified if VPC flow logs for this subnetwork is enabled and "metadata" was set to CUSTOM_METADATA. 



### #metadata_fields=
    
    
    def metadata_fields=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Can only be specified if VPC flow logs for this subnetwork is enabled and "metadata" was set to CUSTOM_METADATA. 



**Returns**

  * (::Array<::String>) — Can only be specified if VPC flow logs for this subnetwork is enabled and "metadata" was set to CUSTOM_METADATA. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
