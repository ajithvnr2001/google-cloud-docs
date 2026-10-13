---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-CapacityCommitment/
title: BigQuery Reservation V1 API - Class Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment (v1.14.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:42:19.103769+00:00
---

# BigQuery Reservation V1 API - Class Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment (v1.14.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-CapacityCommitment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Reservation V1 API - Class Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment (v1.14.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.14.0 (latest)  1.13.1  1.12.1  1.11.0  1.10.0  1.9.2  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.12.0  0.11.2  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.2 

Reference documentation and code samples for the BigQuery Reservation V1 API class Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment.

Capacity commitment is a way to purchase compute capacity for BigQuery jobs (in the form of slots) with some committed period of usage. Annual commitments renew by default. Commitments can be removed after their commitment end time passes.

In order to remove annual commitment, its plan needs to be changed to monthly or flex first.

A capacity commitment resource exists as a child resource of the admin project.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #commitment_end_time
    
    
    def commitment_end_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Protobuf-Timestamp)) — Output only. The end of the current commitment period. It is applicable only for ACTIVE capacity commitments. Note after renewal, commitment_end_time is the time the renewed commitment expires. So itwould be at a time after commitment_start_time + committed period, because we don't change commitment_start_time , 



### #commitment_start_time
    
    
    def commitment_start_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Protobuf-Timestamp)) — Output only. The start of the current commitment period. It is applicable only for ACTIVE capacity commitments. Note after the commitment is renewed, commitment_start_time won't be changed. It refers to the start time of the original commitment. 



### #edition
    
    
    def edition() -> ::Google::Cloud::Bigquery::Reservation::V1::Edition

**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::Edition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Edition)) — Optional. Edition of the capacity commitment. 



### #edition=
    
    
    def edition=(value) -> ::Google::Cloud::Bigquery::Reservation::V1::Edition

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::Reservation::V1::Edition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Edition)) — Optional. Edition of the capacity commitment. 



**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::Edition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Edition)) — Optional. Edition of the capacity commitment. 



### #failure_status
    
    
    def failure_status() -> ::Google::Rpc::Status

**Returns**

  * ([::Google::Rpc::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Rpc-Status)) — Output only. For FAILED commitment plan, provides the reason of failure. 



### #is_flat_rate
    
    
    def is_flat_rate() -> ::Boolean

**Returns**

  * (::Boolean) — Output only. If true, the commitment is a flat-rate commitment, otherwise, it's an edition commitment. 



### #multi_region_auxiliary
    
    
    def multi_region_auxiliary() -> ::Boolean

**Returns**

  * (::Boolean) — Applicable only for commitments located within one of the BigQuery multi-regions (US or EU).

If set to true, this commitment is placed in the organization's secondary region which is designated for disaster recovery purposes. If false, this commitment is placed in the organization's default region.

NOTE: this is a preview feature. Project must be allow-listed in order to set this field. 




### #multi_region_auxiliary=
    
    
    def multi_region_auxiliary=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Applicable only for commitments located within one of the BigQuery multi-regions (US or EU).

If set to true, this commitment is placed in the organization's secondary region which is designated for disaster recovery purposes. If false, this commitment is placed in the organization's default region.

NOTE: this is a preview feature. Project must be allow-listed in order to set this field. 




**Returns**

  * (::Boolean) — Applicable only for commitments located within one of the BigQuery multi-regions (US or EU).

If set to true, this commitment is placed in the organization's secondary region which is designated for disaster recovery purposes. If false, this commitment is placed in the organization's default region.

NOTE: this is a preview feature. Project must be allow-listed in order to set this field. 




### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. The resource name of the capacity commitment, e.g., `projects/myproject/locations/US/capacityCommitments/123` The commitment_id must only contain lower case alphanumeric characters or dashes. It must start with a letter and must not end with a dash. Its maximum length is 64 characters. 



### #plan
    
    
    def plan() -> ::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment::CommitmentPlan

**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment::CommitmentPlan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-CapacityCommitment-CommitmentPlan)) — Optional. Capacity commitment commitment plan. 



### #plan=
    
    
    def plan=(value) -> ::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment::CommitmentPlan

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment::CommitmentPlan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-CapacityCommitment-CommitmentPlan)) — Optional. Capacity commitment commitment plan. 



**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment::CommitmentPlan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-CapacityCommitment-CommitmentPlan)) — Optional. Capacity commitment commitment plan. 



### #renewal_plan
    
    
    def renewal_plan() -> ::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment::CommitmentPlan

**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment::CommitmentPlan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-CapacityCommitment-CommitmentPlan)) — Optional. The plan this capacity commitment is converted to after commitment_end_time passes. Once the plan is changed, committed period is extended according to commitment plan. Only applicable for ANNUAL and TRIAL commitments. 



### #renewal_plan=
    
    
    def renewal_plan=(value) -> ::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment::CommitmentPlan

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment::CommitmentPlan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-CapacityCommitment-CommitmentPlan)) — Optional. The plan this capacity commitment is converted to after commitment_end_time passes. Once the plan is changed, committed period is extended according to commitment plan. Only applicable for ANNUAL and TRIAL commitments. 



**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment::CommitmentPlan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-CapacityCommitment-CommitmentPlan)) — Optional. The plan this capacity commitment is converted to after commitment_end_time passes. Once the plan is changed, committed period is extended according to commitment plan. Only applicable for ANNUAL and TRIAL commitments. 



### #slot_count
    
    
    def slot_count() -> ::Integer

**Returns**

  * (::Integer) — Optional. Number of slots in this commitment. 



### #slot_count=
    
    
    def slot_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Number of slots in this commitment. 



**Returns**

  * (::Integer) — Optional. Number of slots in this commitment. 



### #state
    
    
    def state() -> ::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment::State

**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-CapacityCommitment-State)) — Output only. State of the commitment. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
