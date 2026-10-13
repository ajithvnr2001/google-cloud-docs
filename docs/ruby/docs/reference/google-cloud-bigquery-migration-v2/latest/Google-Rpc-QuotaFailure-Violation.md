---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Rpc-QuotaFailure-Violation/
title: BigQuery Migration V2 API - Class Google::Rpc::QuotaFailure::Violation (v0.23.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:28:18.291177+00:00
---

# BigQuery Migration V2 API - Class Google::Rpc::QuotaFailure::Violation (v0.23.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Rpc-QuotaFailure-Violation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Migration V2 API - Class Google::Rpc::QuotaFailure::Violation (v0.23.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.23.0 (latest)  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.1  0.14.1  0.13.0  0.12.0  0.11.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the BigQuery Migration V2 API class Google::Rpc::QuotaFailure::Violation.

A message type used to describe a single quota violation. For example, a daily quota or a custom quota that was exceeded.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #api_service
    
    
    def api_service() -> ::String

**Returns**

  * (::String) — The API Service from which the `QuotaFailure.Violation` orginates. In some cases, Quota issues originate from an API Service other than the one that was called. In other words, a dependency of the called API Service could be the cause of the `QuotaFailure`, and this field would have the dependency API service name.

For example, if the called API is Kubernetes Engine API (container.googleapis.com), and a quota violation occurs in the Kubernetes Engine API itself, this field would be "container.googleapis.com". On the other hand, if the quota violation occurs when the Kubernetes Engine API creates VMs in the Compute Engine API (compute.googleapis.com), this field would be "compute.googleapis.com". 




### #api_service=
    
    
    def api_service=(value) -> ::String

**Parameter**

  * **value** (::String) — The API Service from which the `QuotaFailure.Violation` orginates. In some cases, Quota issues originate from an API Service other than the one that was called. In other words, a dependency of the called API Service could be the cause of the `QuotaFailure`, and this field would have the dependency API service name.

For example, if the called API is Kubernetes Engine API (container.googleapis.com), and a quota violation occurs in the Kubernetes Engine API itself, this field would be "container.googleapis.com". On the other hand, if the quota violation occurs when the Kubernetes Engine API creates VMs in the Compute Engine API (compute.googleapis.com), this field would be "compute.googleapis.com". 




**Returns**

  * (::String) — The API Service from which the `QuotaFailure.Violation` orginates. In some cases, Quota issues originate from an API Service other than the one that was called. In other words, a dependency of the called API Service could be the cause of the `QuotaFailure`, and this field would have the dependency API service name.

For example, if the called API is Kubernetes Engine API (container.googleapis.com), and a quota violation occurs in the Kubernetes Engine API itself, this field would be "container.googleapis.com". On the other hand, if the quota violation occurs when the Kubernetes Engine API creates VMs in the Compute Engine API (compute.googleapis.com), this field would be "compute.googleapis.com". 




### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — A description of how the quota check failed. Clients can use this description to find more about the quota configuration in the service's public documentation, or find the relevant quota limit to adjust through developer console.

For example: "Service disabled" or "Daily Limit for read operations exceeded". 




### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — A description of how the quota check failed. Clients can use this description to find more about the quota configuration in the service's public documentation, or find the relevant quota limit to adjust through developer console.

For example: "Service disabled" or "Daily Limit for read operations exceeded". 




**Returns**

  * (::String) — A description of how the quota check failed. Clients can use this description to find more about the quota configuration in the service's public documentation, or find the relevant quota limit to adjust through developer console.

For example: "Service disabled" or "Daily Limit for read operations exceeded". 




### #future_quota_value
    
    
    def future_quota_value() -> ::Integer

**Returns**

  * (::Integer) — The new quota value being rolled out at the time of the violation. At the completion of the rollout, this value will be enforced in place of quota_value. If no rollout is in progress at the time of the violation, this field is not set.

For example, if at the time of the violation a rollout is in progress changing the number of CPUs quota from 10 to 20, 20 would be the value of this field. 




### #future_quota_value=
    
    
    def future_quota_value=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The new quota value being rolled out at the time of the violation. At the completion of the rollout, this value will be enforced in place of quota_value. If no rollout is in progress at the time of the violation, this field is not set.

For example, if at the time of the violation a rollout is in progress changing the number of CPUs quota from 10 to 20, 20 would be the value of this field. 




**Returns**

  * (::Integer) — The new quota value being rolled out at the time of the violation. At the completion of the rollout, this value will be enforced in place of quota_value. If no rollout is in progress at the time of the violation, this field is not set.

For example, if at the time of the violation a rollout is in progress changing the number of CPUs quota from 10 to 20, 20 would be the value of this field. 




### #quota_dimensions
    
    
    def quota_dimensions() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — The dimensions of the violated quota. Every non-global quota is enforced on a set of dimensions. While quota metric defines what to count, the dimensions specify for what aspects the counter should be increased.

For example, the quota "CPUs per region per VM family" enforces a limit on the metric "compute.googleapis.com/cpus_per_vm_family" on dimensions "region" and "vm_family". And if the violation occurred in region "us-central1" and for VM family "n1", the quota_dimensions would be,

{ "region": "us-central1", "vm_family": "n1", }

When a quota is enforced globally, the quota_dimensions would always be empty. 




### #quota_dimensions=
    
    
    def quota_dimensions=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — The dimensions of the violated quota. Every non-global quota is enforced on a set of dimensions. While quota metric defines what to count, the dimensions specify for what aspects the counter should be increased.

For example, the quota "CPUs per region per VM family" enforces a limit on the metric "compute.googleapis.com/cpus_per_vm_family" on dimensions "region" and "vm_family". And if the violation occurred in region "us-central1" and for VM family "n1", the quota_dimensions would be,

{ "region": "us-central1", "vm_family": "n1", }

When a quota is enforced globally, the quota_dimensions would always be empty. 




**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — The dimensions of the violated quota. Every non-global quota is enforced on a set of dimensions. While quota metric defines what to count, the dimensions specify for what aspects the counter should be increased.

For example, the quota "CPUs per region per VM family" enforces a limit on the metric "compute.googleapis.com/cpus_per_vm_family" on dimensions "region" and "vm_family". And if the violation occurred in region "us-central1" and for VM family "n1", the quota_dimensions would be,

{ "region": "us-central1", "vm_family": "n1", }

When a quota is enforced globally, the quota_dimensions would always be empty. 




### #quota_id
    
    
    def quota_id() -> ::String

**Returns**

  * (::String) — The id of the violated quota. Also know as "limit name", this is the unique identifier of a quota in the context of an API service.

For example, "CPUS-PER-VM-FAMILY-per-project-region". 




### #quota_id=
    
    
    def quota_id=(value) -> ::String

**Parameter**

  * **value** (::String) — The id of the violated quota. Also know as "limit name", this is the unique identifier of a quota in the context of an API service.

For example, "CPUS-PER-VM-FAMILY-per-project-region". 




**Returns**

  * (::String) — The id of the violated quota. Also know as "limit name", this is the unique identifier of a quota in the context of an API service.

For example, "CPUS-PER-VM-FAMILY-per-project-region". 




### #quota_metric
    
    
    def quota_metric() -> ::String

**Returns**

  * (::String) — The metric of the violated quota. A quota metric is a named counter to measure usage, such as API requests or CPUs. When an activity occurs in a service, such as Virtual Machine allocation, one or more quota metrics may be affected.

For example, "compute.googleapis.com/cpus_per_vm_family", "storage.googleapis.com/internet_egress_bandwidth". 




### #quota_metric=
    
    
    def quota_metric=(value) -> ::String

**Parameter**

  * **value** (::String) — The metric of the violated quota. A quota metric is a named counter to measure usage, such as API requests or CPUs. When an activity occurs in a service, such as Virtual Machine allocation, one or more quota metrics may be affected.

For example, "compute.googleapis.com/cpus_per_vm_family", "storage.googleapis.com/internet_egress_bandwidth". 




**Returns**

  * (::String) — The metric of the violated quota. A quota metric is a named counter to measure usage, such as API requests or CPUs. When an activity occurs in a service, such as Virtual Machine allocation, one or more quota metrics may be affected.

For example, "compute.googleapis.com/cpus_per_vm_family", "storage.googleapis.com/internet_egress_bandwidth". 




### #quota_value
    
    
    def quota_value() -> ::Integer

**Returns**

  * (::Integer) — The enforced quota value at the time of the `QuotaFailure`.

For example, if the enforced quota value at the time of the `QuotaFailure` on the number of CPUs is "10", then the value of this field would reflect this quantity. 




### #quota_value=
    
    
    def quota_value=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The enforced quota value at the time of the `QuotaFailure`.

For example, if the enforced quota value at the time of the `QuotaFailure` on the number of CPUs is "10", then the value of this field would reflect this quantity. 




**Returns**

  * (::Integer) — The enforced quota value at the time of the `QuotaFailure`.

For example, if the enforced quota value at the time of the `QuotaFailure` on the number of CPUs is "10", then the value of this field would reflect this quantity. 




### #subject
    
    
    def subject() -> ::String

**Returns**

  * (::String) — The subject on which the quota check failed. For example, "clientip:



### #subject=
    
    
    def subject=(value) -> ::String

**Parameter**

  * **value** (::String) — The subject on which the quota check failed. For example, "clientip:



**Returns**

  * (::String) — The subject on which the quota check failed. For example, "clientip:



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
