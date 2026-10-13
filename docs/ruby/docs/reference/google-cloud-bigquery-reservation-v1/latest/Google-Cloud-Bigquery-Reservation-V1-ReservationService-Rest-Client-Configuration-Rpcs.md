---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-ReservationService-Rest-Client-Configuration-Rpcs/
title: BigQuery Reservation V1 API - Class Google::Cloud::Bigquery::Reservation::V1::ReservationService::Rest::Client::Configuration::Rpcs (v1.14.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:42:26.728208+00:00
---

# BigQuery Reservation V1 API - Class Google::Cloud::Bigquery::Reservation::V1::ReservationService::Rest::Client::Configuration::Rpcs (v1.14.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-ReservationService-Rest-Client-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Reservation V1 API - Class Google::Cloud::Bigquery::Reservation::V1::ReservationService::Rest::Client::Configuration::Rpcs (v1.14.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.14.0 (latest)  1.13.1  1.12.1  1.11.0  1.10.0  1.9.2  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.12.0  0.11.2  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.2 

Reference documentation and code samples for the BigQuery Reservation V1 API class Google::Cloud::Bigquery::Reservation::V1::ReservationService::Rest::Client::Configuration::Rpcs.

Configuration RPC class for the ReservationService API.

Includes fields providing the configuration for each RPC in this service. Each configuration object is of type `Gapic::Config::Method` and includes the following configuration fields:

  * `timeout` (_type:_ `Numeric`) - The call timeout in seconds
  * `metadata` (_type:_ `Hash{Symbol=>String}`) - Additional headers
  * `retry_policy (_type:_`Hash`) - The retry policy. The policy fields include the following keys: 
    * `:initial_delay` (_type:_ `Numeric`) - The initial delay in seconds.
    * `:max_delay` (_type:_ `Numeric`) - The max delay in seconds.
    * `:multiplier` (_type:_ `Numeric`) - The incremental backoff multiplier.
    * `:jitter` (_type:_ `Numeric`) - The jitter in seconds. Default: 1.0.
    * `:retry_codes` (_type:_ `Array<String>`) - The error codes that should trigger a retry.



## Inherits

  * Object 



## Methods 

### #create_assignment
    
    
    def create_assignment() -> ::Gapic::Config::Method

RPC-specific configuration for `create_assignment`

**Returns**

  * (::Gapic::Config::Method) 



### #create_capacity_commitment
    
    
    def create_capacity_commitment() -> ::Gapic::Config::Method

RPC-specific configuration for `create_capacity_commitment`

**Returns**

  * (::Gapic::Config::Method) 



### #create_reservation
    
    
    def create_reservation() -> ::Gapic::Config::Method

RPC-specific configuration for `create_reservation`

**Returns**

  * (::Gapic::Config::Method) 



### #create_reservation_group
    
    
    def create_reservation_group() -> ::Gapic::Config::Method

RPC-specific configuration for `create_reservation_group`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_assignment
    
    
    def delete_assignment() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_assignment`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_capacity_commitment
    
    
    def delete_capacity_commitment() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_capacity_commitment`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_reservation
    
    
    def delete_reservation() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_reservation`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_reservation_group
    
    
    def delete_reservation_group() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_reservation_group`

**Returns**

  * (::Gapic::Config::Method) 



### #failover_reservation
    
    
    def failover_reservation() -> ::Gapic::Config::Method

RPC-specific configuration for `failover_reservation`

**Returns**

  * (::Gapic::Config::Method) 



### #get_bi_reservation
    
    
    def get_bi_reservation() -> ::Gapic::Config::Method

RPC-specific configuration for `get_bi_reservation`

**Returns**

  * (::Gapic::Config::Method) 



### #get_capacity_commitment
    
    
    def get_capacity_commitment() -> ::Gapic::Config::Method

RPC-specific configuration for `get_capacity_commitment`

**Returns**

  * (::Gapic::Config::Method) 



### #get_iam_policy
    
    
    def get_iam_policy() -> ::Gapic::Config::Method

RPC-specific configuration for `get_iam_policy`

**Returns**

  * (::Gapic::Config::Method) 



### #get_reservation
    
    
    def get_reservation() -> ::Gapic::Config::Method

RPC-specific configuration for `get_reservation`

**Returns**

  * (::Gapic::Config::Method) 



### #get_reservation_group
    
    
    def get_reservation_group() -> ::Gapic::Config::Method

RPC-specific configuration for `get_reservation_group`

**Returns**

  * (::Gapic::Config::Method) 



### #list_assignments
    
    
    def list_assignments() -> ::Gapic::Config::Method

RPC-specific configuration for `list_assignments`

**Returns**

  * (::Gapic::Config::Method) 



### #list_capacity_commitments
    
    
    def list_capacity_commitments() -> ::Gapic::Config::Method

RPC-specific configuration for `list_capacity_commitments`

**Returns**

  * (::Gapic::Config::Method) 



### #list_reservation_groups
    
    
    def list_reservation_groups() -> ::Gapic::Config::Method

RPC-specific configuration for `list_reservation_groups`

**Returns**

  * (::Gapic::Config::Method) 



### #list_reservations
    
    
    def list_reservations() -> ::Gapic::Config::Method

RPC-specific configuration for `list_reservations`

**Returns**

  * (::Gapic::Config::Method) 



### #merge_capacity_commitments
    
    
    def merge_capacity_commitments() -> ::Gapic::Config::Method

RPC-specific configuration for `merge_capacity_commitments`

**Returns**

  * (::Gapic::Config::Method) 



### #move_assignment
    
    
    def move_assignment() -> ::Gapic::Config::Method

RPC-specific configuration for `move_assignment`

**Returns**

  * (::Gapic::Config::Method) 



### #search_all_assignments
    
    
    def search_all_assignments() -> ::Gapic::Config::Method

RPC-specific configuration for `search_all_assignments`

**Returns**

  * (::Gapic::Config::Method) 



### #search_assignments
    
    
    def search_assignments() -> ::Gapic::Config::Method

RPC-specific configuration for `search_assignments`

**Returns**

  * (::Gapic::Config::Method) 



### #set_iam_policy
    
    
    def set_iam_policy() -> ::Gapic::Config::Method

RPC-specific configuration for `set_iam_policy`

**Returns**

  * (::Gapic::Config::Method) 



### #split_capacity_commitment
    
    
    def split_capacity_commitment() -> ::Gapic::Config::Method

RPC-specific configuration for `split_capacity_commitment`

**Returns**

  * (::Gapic::Config::Method) 



### #test_iam_permissions
    
    
    def test_iam_permissions() -> ::Gapic::Config::Method

RPC-specific configuration for `test_iam_permissions`

**Returns**

  * (::Gapic::Config::Method) 



### #update_assignment
    
    
    def update_assignment() -> ::Gapic::Config::Method

RPC-specific configuration for `update_assignment`

**Returns**

  * (::Gapic::Config::Method) 



### #update_bi_reservation
    
    
    def update_bi_reservation() -> ::Gapic::Config::Method

RPC-specific configuration for `update_bi_reservation`

**Returns**

  * (::Gapic::Config::Method) 



### #update_capacity_commitment
    
    
    def update_capacity_commitment() -> ::Gapic::Config::Method

RPC-specific configuration for `update_capacity_commitment`

**Returns**

  * (::Gapic::Config::Method) 



### #update_reservation
    
    
    def update_reservation() -> ::Gapic::Config::Method

RPC-specific configuration for `update_reservation`

**Returns**

  * (::Gapic::Config::Method) 



### #update_reservation_group
    
    
    def update_reservation_group() -> ::Gapic::Config::Method

RPC-specific configuration for `update_reservation_group`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
