---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Reservation/
title: BigQuery Reservation V1 API - Class Google::Cloud::Bigquery::Reservation::V1::Reservation (v1.14.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:42:23.248991+00:00
---

# BigQuery Reservation V1 API - Class Google::Cloud::Bigquery::Reservation::V1::Reservation (v1.14.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Reservation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Reservation V1 API - Class Google::Cloud::Bigquery::Reservation::V1::Reservation (v1.14.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.14.0 (latest)  1.13.1  1.12.1  1.11.0  1.10.0  1.9.2  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.12.0  0.11.2  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.2 

Reference documentation and code samples for the BigQuery Reservation V1 API class Google::Cloud::Bigquery::Reservation::V1::Reservation.

A reservation is a mechanism used to guarantee slots to users.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #autoscale
    
    
    def autoscale() -> ::Google::Cloud::Bigquery::Reservation::V1::Reservation::Autoscale

**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::Reservation::Autoscale](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Reservation-Autoscale)) — Optional. The configuration parameters for the auto scaling feature. 



### #autoscale=
    
    
    def autoscale=(value) -> ::Google::Cloud::Bigquery::Reservation::V1::Reservation::Autoscale

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::Reservation::V1::Reservation::Autoscale](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Reservation-Autoscale)) — Optional. The configuration parameters for the auto scaling feature. 



**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::Reservation::Autoscale](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Reservation-Autoscale)) — Optional. The configuration parameters for the auto scaling feature. 



### #concurrency
    
    
    def concurrency() -> ::Integer

**Returns**

  * (::Integer) — Optional. Job concurrency target which sets a soft upper bound on the number of jobs that can run concurrently in this reservation. This is a soft target due to asynchronous nature of the system and various optimizations for small queries. Default value is 0 which means that concurrency target will be automatically computed by the system. NOTE: this field is exposed as target job concurrency in the Information Schema, DDL and BigQuery CLI. 



### #concurrency=
    
    
    def concurrency=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Job concurrency target which sets a soft upper bound on the number of jobs that can run concurrently in this reservation. This is a soft target due to asynchronous nature of the system and various optimizations for small queries. Default value is 0 which means that concurrency target will be automatically computed by the system. NOTE: this field is exposed as target job concurrency in the Information Schema, DDL and BigQuery CLI. 



**Returns**

  * (::Integer) — Optional. Job concurrency target which sets a soft upper bound on the number of jobs that can run concurrently in this reservation. This is a soft target due to asynchronous nature of the system and various optimizations for small queries. Default value is 0 which means that concurrency target will be automatically computed by the system. NOTE: this field is exposed as target job concurrency in the Information Schema, DDL and BigQuery CLI. 



### #creation_time
    
    
    def creation_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Protobuf-Timestamp)) — Output only. Creation time of the reservation. 



### #edition
    
    
    def edition() -> ::Google::Cloud::Bigquery::Reservation::V1::Edition

**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::Edition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Edition)) — Optional. Edition of the reservation. 



### #edition=
    
    
    def edition=(value) -> ::Google::Cloud::Bigquery::Reservation::V1::Edition

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::Reservation::V1::Edition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Edition)) — Optional. Edition of the reservation. 



**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::Edition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Edition)) — Optional. Edition of the reservation. 



### #ignore_idle_slots
    
    
    def ignore_idle_slots() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. If false, any query or pipeline job using this reservation will use idle slots from other reservations within the same admin project. If true, a query or pipeline job using this reservation will execute with the slot capacity specified in the slot_capacity field at most. 



### #ignore_idle_slots=
    
    
    def ignore_idle_slots=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. If false, any query or pipeline job using this reservation will use idle slots from other reservations within the same admin project. If true, a query or pipeline job using this reservation will execute with the slot capacity specified in the slot_capacity field at most. 



**Returns**

  * (::Boolean) — Optional. If false, any query or pipeline job using this reservation will use idle slots from other reservations within the same admin project. If true, a query or pipeline job using this reservation will execute with the slot capacity specified in the slot_capacity field at most. 



### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. The labels associated with this reservation. You can use these to organize and group your reservations. You can set this property when you create or update a reservation. 



### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Optional. The labels associated with this reservation. You can use these to organize and group your reservations. You can set this property when you create or update a reservation. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. The labels associated with this reservation. You can use these to organize and group your reservations. You can set this property when you create or update a reservation. 



### #max_slots
    
    
    def max_slots() -> ::Integer

**Returns**

  * (::Integer) — Optional. The overall max slots for the reservation, covering slot_capacity (baseline), idle slots (if ignore_idle_slots is false) and scaled slots. If present, the reservation won't use more than the specified number of slots, even if there is demand and supply (from idle slots). NOTE: capping a reservation's idle slot usage is best effort and its usage may exceed the max_slots value. However, in terms of autoscale.current_slots (which accounts for the additional added slots), it will never exceed the max_slots - baseline.

This field must be set together with the scaling_mode enum value, otherwise the request will be rejected with error code `google.rpc.Code.INVALID_ARGUMENT`.

If the max_slots and scaling_mode are set, the autoscale or autoscale.max_slots field must be unset. Otherwise the request will be rejected with error code `google.rpc.Code.INVALID_ARGUMENT`. However, the autoscale field may still be in the output. The autopscale.max_slots will always show as 0 and the autoscaler.current_slots will represent the current slots from autoscaler excluding idle slots. For example, if the max_slots is 1000 and scaling_mode is AUTOSCALE_ONLY, then in the output, the autoscaler.max_slots will be 0 and the autoscaler.current_slots may be any value between 0 and 1000.

If the max_slots is 1000, scaling_mode is ALL_SLOTS, the baseline is 100 and idle slots usage is 200, then in the output, the autoscaler.max_slots will be 0 and the autoscaler.current_slots will not be higher than 700.

If the max_slots is 1000, scaling_mode is IDLE_SLOTS_ONLY, then in the output, the autoscaler field will be null.

If the max_slots and scaling_mode are set, then the ignore_idle_slots field must be aligned with the scaling_mode enum value.(See details in ScalingMode comments). Otherwise the request will be rejected with error code `google.rpc.Code.INVALID_ARGUMENT`.

Please note, the max_slots is for user to manage the part of slots greater than the baseline. Therefore, we don't allow users to set max_slots smaller or equal to the baseline as it will not be meaningful. If the field is present and slot_capacity>=max_slots, requests will be rejected with error code `google.rpc.Code.INVALID_ARGUMENT`.

Please note that if max_slots is set to 0, we will treat it as unset. Customers can set max_slots to 0 and set scaling_mode to SCALING_MODE_UNSPECIFIED to disable the max_slots feature. 




### #max_slots=
    
    
    def max_slots=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. The overall max slots for the reservation, covering slot_capacity (baseline), idle slots (if ignore_idle_slots is false) and scaled slots. If present, the reservation won't use more than the specified number of slots, even if there is demand and supply (from idle slots). NOTE: capping a reservation's idle slot usage is best effort and its usage may exceed the max_slots value. However, in terms of autoscale.current_slots (which accounts for the additional added slots), it will never exceed the max_slots - baseline.

This field must be set together with the scaling_mode enum value, otherwise the request will be rejected with error code `google.rpc.Code.INVALID_ARGUMENT`.

If the max_slots and scaling_mode are set, the autoscale or autoscale.max_slots field must be unset. Otherwise the request will be rejected with error code `google.rpc.Code.INVALID_ARGUMENT`. However, the autoscale field may still be in the output. The autopscale.max_slots will always show as 0 and the autoscaler.current_slots will represent the current slots from autoscaler excluding idle slots. For example, if the max_slots is 1000 and scaling_mode is AUTOSCALE_ONLY, then in the output, the autoscaler.max_slots will be 0 and the autoscaler.current_slots may be any value between 0 and 1000.

If the max_slots is 1000, scaling_mode is ALL_SLOTS, the baseline is 100 and idle slots usage is 200, then in the output, the autoscaler.max_slots will be 0 and the autoscaler.current_slots will not be higher than 700.

If the max_slots is 1000, scaling_mode is IDLE_SLOTS_ONLY, then in the output, the autoscaler field will be null.

If the max_slots and scaling_mode are set, then the ignore_idle_slots field must be aligned with the scaling_mode enum value.(See details in ScalingMode comments). Otherwise the request will be rejected with error code `google.rpc.Code.INVALID_ARGUMENT`.

Please note, the max_slots is for user to manage the part of slots greater than the baseline. Therefore, we don't allow users to set max_slots smaller or equal to the baseline as it will not be meaningful. If the field is present and slot_capacity>=max_slots, requests will be rejected with error code `google.rpc.Code.INVALID_ARGUMENT`.

Please note that if max_slots is set to 0, we will treat it as unset. Customers can set max_slots to 0 and set scaling_mode to SCALING_MODE_UNSPECIFIED to disable the max_slots feature. 




**Returns**

  * (::Integer) — Optional. The overall max slots for the reservation, covering slot_capacity (baseline), idle slots (if ignore_idle_slots is false) and scaled slots. If present, the reservation won't use more than the specified number of slots, even if there is demand and supply (from idle slots). NOTE: capping a reservation's idle slot usage is best effort and its usage may exceed the max_slots value. However, in terms of autoscale.current_slots (which accounts for the additional added slots), it will never exceed the max_slots - baseline.

This field must be set together with the scaling_mode enum value, otherwise the request will be rejected with error code `google.rpc.Code.INVALID_ARGUMENT`.

If the max_slots and scaling_mode are set, the autoscale or autoscale.max_slots field must be unset. Otherwise the request will be rejected with error code `google.rpc.Code.INVALID_ARGUMENT`. However, the autoscale field may still be in the output. The autopscale.max_slots will always show as 0 and the autoscaler.current_slots will represent the current slots from autoscaler excluding idle slots. For example, if the max_slots is 1000 and scaling_mode is AUTOSCALE_ONLY, then in the output, the autoscaler.max_slots will be 0 and the autoscaler.current_slots may be any value between 0 and 1000.

If the max_slots is 1000, scaling_mode is ALL_SLOTS, the baseline is 100 and idle slots usage is 200, then in the output, the autoscaler.max_slots will be 0 and the autoscaler.current_slots will not be higher than 700.

If the max_slots is 1000, scaling_mode is IDLE_SLOTS_ONLY, then in the output, the autoscaler field will be null.

If the max_slots and scaling_mode are set, then the ignore_idle_slots field must be aligned with the scaling_mode enum value.(See details in ScalingMode comments). Otherwise the request will be rejected with error code `google.rpc.Code.INVALID_ARGUMENT`.

Please note, the max_slots is for user to manage the part of slots greater than the baseline. Therefore, we don't allow users to set max_slots smaller or equal to the baseline as it will not be meaningful. If the field is present and slot_capacity>=max_slots, requests will be rejected with error code `google.rpc.Code.INVALID_ARGUMENT`.

Please note that if max_slots is set to 0, we will treat it as unset. Customers can set max_slots to 0 and set scaling_mode to SCALING_MODE_UNSPECIFIED to disable the max_slots feature. 




### #multi_region_auxiliary
    
    
    def multi_region_auxiliary() -> ::Boolean

**Returns**

  * (::Boolean) — Applicable only for reservations located within one of the BigQuery multi-regions (US or EU).

If set to true, this reservation is placed in the organization's secondary region which is designated for disaster recovery purposes. If false, this reservation is placed in the organization's default region.

NOTE: this is a preview feature. Project must be allow-listed in order to set this field. 




### #multi_region_auxiliary=
    
    
    def multi_region_auxiliary=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Applicable only for reservations located within one of the BigQuery multi-regions (US or EU).

If set to true, this reservation is placed in the organization's secondary region which is designated for disaster recovery purposes. If false, this reservation is placed in the organization's default region.

NOTE: this is a preview feature. Project must be allow-listed in order to set this field. 




**Returns**

  * (::Boolean) — Applicable only for reservations located within one of the BigQuery multi-regions (US or EU).

If set to true, this reservation is placed in the organization's secondary region which is designated for disaster recovery purposes. If false, this reservation is placed in the organization's default region.

NOTE: this is a preview feature. Project must be allow-listed in order to set this field. 




### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Identifier. The resource name of the reservation, e.g., `projects/*/locations/*/reservations/team1-prod`. The reservation_id must only contain lower case alphanumeric characters or dashes. It must start with a letter and must not end with a dash. Its maximum length is 64 characters. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Identifier. The resource name of the reservation, e.g., `projects/*/locations/*/reservations/team1-prod`. The reservation_id must only contain lower case alphanumeric characters or dashes. It must start with a letter and must not end with a dash. Its maximum length is 64 characters. 



**Returns**

  * (::String) — Identifier. The resource name of the reservation, e.g., `projects/*/locations/*/reservations/team1-prod`. The reservation_id must only contain lower case alphanumeric characters or dashes. It must start with a letter and must not end with a dash. Its maximum length is 64 characters. 



### #original_primary_location
    
    
    def original_primary_location() -> ::String

**Returns**

  * (::String) — Output only. The location where the reservation was originally created. This is set only during the failover reservation's creation. All billing charges for the failover reservation will be applied to this location. 



### #primary_location
    
    
    def primary_location() -> ::String

**Returns**

  * (::String) — Output only. The current location of the reservation's primary replica. This field is only set for reservations using the managed disaster recovery feature. 



### #replication_status
    
    
    def replication_status() -> ::Google::Cloud::Bigquery::Reservation::V1::Reservation::ReplicationStatus

**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::Reservation::ReplicationStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Reservation-ReplicationStatus)) — Output only. The Disaster Recovery(DR) replication status of the reservation. This is only available for the primary replicas of DR/failover reservations and provides information about the both the staleness of the secondary and the last error encountered while trying to replicate changes from the primary to the secondary. If this field is blank, it means that the reservation is either not a DR reservation or the reservation is a DR secondary or that any replication operations on the reservation have succeeded. 



### #reservation_group
    
    
    def reservation_group() -> ::String

**Returns**

  * (::String) — Optional. The reservation group that this reservation belongs to. You can set this property when you create or update a reservation. Reservations do not need to belong to a reservation group. Format: projects/{project}/locations/{location}/reservationGroups/{reservation_group} or just {reservation_group} 



### #reservation_group=
    
    
    def reservation_group=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The reservation group that this reservation belongs to. You can set this property when you create or update a reservation. Reservations do not need to belong to a reservation group. Format: projects/{project}/locations/{location}/reservationGroups/{reservation_group} or just {reservation_group} 



**Returns**

  * (::String) — Optional. The reservation group that this reservation belongs to. You can set this property when you create or update a reservation. Reservations do not need to belong to a reservation group. Format: projects/{project}/locations/{location}/reservationGroups/{reservation_group} or just {reservation_group} 



### #reservation_group_path
    
    
    def reservation_group_path() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Output only. The reservation group path of the reservation from root to leaf. The order of elements matters: the first element is the top level group and the last element is the direct parent reservation group. For example, if a reservation is under group-1 -> group-2 -> group-3, then the reservation group path is ["group-1", "group-2", "group-3"]. 



### #scaling_mode
    
    
    def scaling_mode() -> ::Google::Cloud::Bigquery::Reservation::V1::Reservation::ScalingMode

**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::Reservation::ScalingMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Reservation-ScalingMode)) — Optional. The scaling mode for the reservation. If the field is present but max_slots is not present, requests will be rejected with error code `google.rpc.Code.INVALID_ARGUMENT`. 



### #scaling_mode=
    
    
    def scaling_mode=(value) -> ::Google::Cloud::Bigquery::Reservation::V1::Reservation::ScalingMode

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::Reservation::V1::Reservation::ScalingMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Reservation-ScalingMode)) — Optional. The scaling mode for the reservation. If the field is present but max_slots is not present, requests will be rejected with error code `google.rpc.Code.INVALID_ARGUMENT`. 



**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::Reservation::ScalingMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Reservation-ScalingMode)) — Optional. The scaling mode for the reservation. If the field is present but max_slots is not present, requests will be rejected with error code `google.rpc.Code.INVALID_ARGUMENT`. 



### #scheduling_policy
    
    
    def scheduling_policy() -> ::Google::Cloud::Bigquery::Reservation::V1::SchedulingPolicy

**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::SchedulingPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-SchedulingPolicy)) — Optional. The scheduling policy to use for jobs and queries running under this reservation. The scheduling policy controls how the reservation's resources are distributed.

This feature is not yet generally available. 




### #scheduling_policy=
    
    
    def scheduling_policy=(value) -> ::Google::Cloud::Bigquery::Reservation::V1::SchedulingPolicy

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::Reservation::V1::SchedulingPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-SchedulingPolicy)) — Optional. The scheduling policy to use for jobs and queries running under this reservation. The scheduling policy controls how the reservation's resources are distributed.

This feature is not yet generally available. 




**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::SchedulingPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-SchedulingPolicy)) — Optional. The scheduling policy to use for jobs and queries running under this reservation. The scheduling policy controls how the reservation's resources are distributed.

This feature is not yet generally available. 




### #secondary_location
    
    
    def secondary_location() -> ::String

**Returns**

  * (::String) — Optional. The current location of the reservation's secondary replica. This field is only set for reservations using the managed disaster recovery feature. Users can set this in create reservation calls to create a failover reservation or in update reservation calls to convert a non-failover reservation to a failover reservation(or vice versa). 



### #secondary_location=
    
    
    def secondary_location=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The current location of the reservation's secondary replica. This field is only set for reservations using the managed disaster recovery feature. Users can set this in create reservation calls to create a failover reservation or in update reservation calls to convert a non-failover reservation to a failover reservation(or vice versa). 



**Returns**

  * (::String) — Optional. The current location of the reservation's secondary replica. This field is only set for reservations using the managed disaster recovery feature. Users can set this in create reservation calls to create a failover reservation or in update reservation calls to convert a non-failover reservation to a failover reservation(or vice versa). 



### #slot_capacity
    
    
    def slot_capacity() -> ::Integer

**Returns**

  * (::Integer) — Optional. Baseline slots available to this reservation. A slot is a unit of computational power in BigQuery, and serves as the unit of parallelism.

Queries using this reservation might use more slots during runtime if ignore_idle_slots is set to false, or autoscaling is enabled.

The total slot_capacity of the reservation and its siblings may exceed the total slot_count of capacity commitments. In that case, the exceeding slots will be charged with the autoscale SKU. You can increase the number of baseline slots in a reservation every few minutes. If you want to decrease your baseline slots, you are limited to once an hour if you have recently changed your baseline slot capacity and your baseline slots exceed your committed slots. Otherwise, you can decrease your baseline slots every few minutes. 




### #slot_capacity=
    
    
    def slot_capacity=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Baseline slots available to this reservation. A slot is a unit of computational power in BigQuery, and serves as the unit of parallelism.

Queries using this reservation might use more slots during runtime if ignore_idle_slots is set to false, or autoscaling is enabled.

The total slot_capacity of the reservation and its siblings may exceed the total slot_count of capacity commitments. In that case, the exceeding slots will be charged with the autoscale SKU. You can increase the number of baseline slots in a reservation every few minutes. If you want to decrease your baseline slots, you are limited to once an hour if you have recently changed your baseline slot capacity and your baseline slots exceed your committed slots. Otherwise, you can decrease your baseline slots every few minutes. 




**Returns**

  * (::Integer) — Optional. Baseline slots available to this reservation. A slot is a unit of computational power in BigQuery, and serves as the unit of parallelism.

Queries using this reservation might use more slots during runtime if ignore_idle_slots is set to false, or autoscaling is enabled.

The total slot_capacity of the reservation and its siblings may exceed the total slot_count of capacity commitments. In that case, the exceeding slots will be charged with the autoscale SKU. You can increase the number of baseline slots in a reservation every few minutes. If you want to decrease your baseline slots, you are limited to once an hour if you have recently changed your baseline slot capacity and your baseline slots exceed your committed slots. Otherwise, you can decrease your baseline slots every few minutes. 




### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Protobuf-Timestamp)) — Output only. Last update time of the reservation. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
