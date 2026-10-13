---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_usage-v1/latest/Google-Api-QuotaLimit/
title: Service Usage V1 API - Class Google::Api::QuotaLimit (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:30:21.652351+00:00
---

# Service Usage V1 API - Class Google::Api::QuotaLimit (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_usage-v1/latest/Google-Api-QuotaLimit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Service Usage V1 API - Class Google::Api::QuotaLimit (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.1  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.7.0  0.6.2  0.5.0  0.4.0  0.3.1  0.2.1  0.1.4 

Reference documentation and code samples for the Service Usage V1 API class Google::Api::QuotaLimit.

`QuotaLimit` defines a specific limit that applies over a specified duration for a limit type. There can be at most one limit for a duration and limit type combination defined within a `QuotaGroup`.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #default_limit
    
    
    def default_limit() -> ::Integer

**Returns**

  * (::Integer) — Default number of tokens that can be consumed during the specified duration. This is the number of tokens assigned when a client application developer activates the service for his/her project.

Specifying a value of 0 will block all requests. This can be used if you are provisioning quota to selected consumers and blocking others. Similarly, a value of -1 will indicate an unlimited quota. No other negative values are allowed.

Used by group-based quotas only. 




### #default_limit=
    
    
    def default_limit=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Default number of tokens that can be consumed during the specified duration. This is the number of tokens assigned when a client application developer activates the service for his/her project.

Specifying a value of 0 will block all requests. This can be used if you are provisioning quota to selected consumers and blocking others. Similarly, a value of -1 will indicate an unlimited quota. No other negative values are allowed.

Used by group-based quotas only. 




**Returns**

  * (::Integer) — Default number of tokens that can be consumed during the specified duration. This is the number of tokens assigned when a client application developer activates the service for his/her project.

Specifying a value of 0 will block all requests. This can be used if you are provisioning quota to selected consumers and blocking others. Similarly, a value of -1 will indicate an unlimited quota. No other negative values are allowed.

Used by group-based quotas only. 




### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — Optional. User-visible, extended description for this quota limit. Should be used only when more context is needed to understand this limit than provided by the limit's display name (see: `display_name`). 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. User-visible, extended description for this quota limit. Should be used only when more context is needed to understand this limit than provided by the limit's display name (see: `display_name`). 



**Returns**

  * (::String) — Optional. User-visible, extended description for this quota limit. Should be used only when more context is needed to understand this limit than provided by the limit's display name (see: `display_name`). 



### #display_name
    
    
    def display_name() -> ::String

**Returns**

  * (::String) — User-visible display name for this limit. Optional. If not set, the UI will provide a default display name based on the quota configuration. This field can be used to override the default display name generated from the configuration. 



### #display_name=
    
    
    def display_name=(value) -> ::String

**Parameter**

  * **value** (::String) — User-visible display name for this limit. Optional. If not set, the UI will provide a default display name based on the quota configuration. This field can be used to override the default display name generated from the configuration. 



**Returns**

  * (::String) — User-visible display name for this limit. Optional. If not set, the UI will provide a default display name based on the quota configuration. This field can be used to override the default display name generated from the configuration. 



### #duration
    
    
    def duration() -> ::String

**Returns**

  * (::String) — Duration of this limit in textual notation. Must be "100s" or "1d".

Used by group-based quotas only. 




### #duration=
    
    
    def duration=(value) -> ::String

**Parameter**

  * **value** (::String) — Duration of this limit in textual notation. Must be "100s" or "1d".

Used by group-based quotas only. 




**Returns**

  * (::String) — Duration of this limit in textual notation. Must be "100s" or "1d".

Used by group-based quotas only. 




### #free_tier
    
    
    def free_tier() -> ::Integer

**Returns**

  * (::Integer) — Free tier value displayed in the Developers Console for this limit. The free tier is the number of tokens that will be subtracted from the billed amount when billing is enabled. This field can only be set on a limit with duration "1d", in a billable group; it is invalid on any other limit. If this field is not set, it defaults to 0, indicating that there is no free tier for this service.

Used by group-based quotas only. 




### #free_tier=
    
    
    def free_tier=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Free tier value displayed in the Developers Console for this limit. The free tier is the number of tokens that will be subtracted from the billed amount when billing is enabled. This field can only be set on a limit with duration "1d", in a billable group; it is invalid on any other limit. If this field is not set, it defaults to 0, indicating that there is no free tier for this service.

Used by group-based quotas only. 




**Returns**

  * (::Integer) — Free tier value displayed in the Developers Console for this limit. The free tier is the number of tokens that will be subtracted from the billed amount when billing is enabled. This field can only be set on a limit with duration "1d", in a billable group; it is invalid on any other limit. If this field is not set, it defaults to 0, indicating that there is no free tier for this service.

Used by group-based quotas only. 




### #max_limit
    
    
    def max_limit() -> ::Integer

**Returns**

  * (::Integer) — Maximum number of tokens that can be consumed during the specified duration. Client application developers can override the default limit up to this maximum. If specified, this value cannot be set to a value less than the default limit. If not specified, it is set to the default limit.

To allow clients to apply overrides with no upper bound, set this to -1, indicating unlimited maximum quota.

Used by group-based quotas only. 




### #max_limit=
    
    
    def max_limit=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Maximum number of tokens that can be consumed during the specified duration. Client application developers can override the default limit up to this maximum. If specified, this value cannot be set to a value less than the default limit. If not specified, it is set to the default limit.

To allow clients to apply overrides with no upper bound, set this to -1, indicating unlimited maximum quota.

Used by group-based quotas only. 




**Returns**

  * (::Integer) — Maximum number of tokens that can be consumed during the specified duration. Client application developers can override the default limit up to this maximum. If specified, this value cannot be set to a value less than the default limit. If not specified, it is set to the default limit.

To allow clients to apply overrides with no upper bound, set this to -1, indicating unlimited maximum quota.

Used by group-based quotas only. 




### #metric
    
    
    def metric() -> ::String

**Returns**

  * (::String) — The name of the metric this quota limit applies to. The quota limits with the same metric will be checked together during runtime. The metric must be defined within the service config. 



### #metric=
    
    
    def metric=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of the metric this quota limit applies to. The quota limits with the same metric will be checked together during runtime. The metric must be defined within the service config. 



**Returns**

  * (::String) — The name of the metric this quota limit applies to. The quota limits with the same metric will be checked together during runtime. The metric must be defined within the service config. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Name of the quota limit.

The name must be provided, and it must be unique within the service. The name can only include alphanumeric characters as well as '-'.

The maximum length of the limit name is 64 characters. 




### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Name of the quota limit.

The name must be provided, and it must be unique within the service. The name can only include alphanumeric characters as well as '-'.

The maximum length of the limit name is 64 characters. 




**Returns**

  * (::String) — Name of the quota limit.

The name must be provided, and it must be unique within the service. The name can only include alphanumeric characters as well as '-'.

The maximum length of the limit name is 64 characters. 




### #unit
    
    
    def unit() -> ::String

**Returns**

  * (::String) — Specify the unit of the quota limit. It uses the same syntax as [MetricDescriptor.unit][google.api.MetricDescriptor.unit]. The supported unit kinds are determined by the quota backend system.

Here are some examples:

    * "1/min/{project}" for quota per minute per project.

Note: the order of unit components is insignificant. The "1" at the beginning is required to follow the metric unit syntax. 




### #unit=
    
    
    def unit=(value) -> ::String

**Parameter**

  * **value** (::String) — Specify the unit of the quota limit. It uses the same syntax as [MetricDescriptor.unit][google.api.MetricDescriptor.unit]. The supported unit kinds are determined by the quota backend system.

Here are some examples:

    * "1/min/{project}" for quota per minute per project.

Note: the order of unit components is insignificant. The "1" at the beginning is required to follow the metric unit syntax. 




**Returns**

  * (::String) — Specify the unit of the quota limit. It uses the same syntax as [MetricDescriptor.unit][google.api.MetricDescriptor.unit]. The supported unit kinds are determined by the quota backend system.

Here are some examples:

    * "1/min/{project}" for quota per minute per project.

Note: the order of unit components is insignificant. The "1" at the beginning is required to follow the metric unit syntax. 




### #values
    
    
    def values() -> ::Google::Protobuf::Map{::String => ::Integer}

**Returns**

  * (::Google::Protobuf::Map{::String => ::Integer}) — Tiered limit values. You must specify this as a key:value pair, with an integer value that is the maximum number of requests allowed for the specified unit. Currently only STANDARD is supported. 



### #values=
    
    
    def values=(value) -> ::Google::Protobuf::Map{::String => ::Integer}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::Integer}) — Tiered limit values. You must specify this as a key:value pair, with an integer value that is the maximum number of requests allowed for the specified unit. Currently only STANDARD is supported. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::Integer}) — Tiered limit values. You must specify this as a key:value pair, with an integer value that is the maximum number of requests allowed for the specified unit. Currently only STANDARD is supported. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
