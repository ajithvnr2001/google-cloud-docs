---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Reservation-ScalingMode/
title: BigQuery Reservation V1 API - Module Google::Cloud::Bigquery::Reservation::V1::Reservation::ScalingMode (v1.14.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:42:23.343168+00:00
---

# BigQuery Reservation V1 API - Module Google::Cloud::Bigquery::Reservation::V1::Reservation::ScalingMode (v1.14.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Reservation-ScalingMode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Reservation V1 API - Module Google::Cloud::Bigquery::Reservation::V1::Reservation::ScalingMode (v1.14.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.14.0 (latest)  1.13.1  1.12.1  1.11.0  1.10.0  1.9.2  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.12.0  0.11.2  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.2 

Reference documentation and code samples for the BigQuery Reservation V1 API module Google::Cloud::Bigquery::Reservation::V1::Reservation::ScalingMode.

The scaling mode for the reservation. This enum determines how the reservation scales up and down.

## Constants 

### SCALING_MODE_UNSPECIFIED

**value:** 0  
Default value of ScalingMode.

### AUTOSCALE_ONLY

**value:** 1  
The reservation will scale up only using slots from autoscaling. It will not use any idle slots even if there may be some available. The upper limit that autoscaling can scale up to will be max_slots - baseline. For example, if max_slots is 1000, baseline is 200 and customer sets ScalingMode to AUTOSCALE_ONLY, then autoscalerg will scale up to 800 slots and no idle slots will be used.

Please note, in this mode, the ignore_idle_slots field must be set to true. Otherwise the request will be rejected with error code `google.rpc.Code.INVALID_ARGUMENT`.

### IDLE_SLOTS_ONLY

**value:** 2  
The reservation will scale up using only idle slots contributed by other reservations or from unassigned commitments. If no idle slots are available it will not scale up further. If the idle slots which it is using are reclaimed by the contributing reservation(s) it may be forced to scale down. The max idle slots the reservation can be max_slots - baseline capacity. For example, if max_slots is 1000, baseline is 200 and customer sets ScalingMode to IDLE_SLOTS_ONLY,

  1. if there are 1000 idle slots available in other reservations, the reservation will scale up to 1000 slots with 200 baseline and 800 idle slots.
  2. if there are 500 idle slots available in other reservations, the reservation will scale up to 700 slots with 200 baseline and 500 idle slots. Please note, in this mode, the reservation might not be able to scale up to max_slots.



Please note, in this mode, the ignore_idle_slots field must be set to false. Otherwise the request will be rejected with error code `google.rpc.Code.INVALID_ARGUMENT`.

### ALL_SLOTS

**value:** 3  
The reservation will scale up using all slots available to it. It will use idle slots contributed by other reservations or from unassigned commitments first. If no idle slots are available it will scale up using autoscaling. For example, if max_slots is 1000, baseline is 200 and customer sets ScalingMode to ALL_SLOTS,

  1. if there are 800 idle slots available in other reservations, the reservation will scale up to 1000 slots with 200 baseline and 800 idle slots.
  2. if there are 500 idle slots available in other reservations, the reservation will scale up to 1000 slots with 200 baseline, 500 idle slots and 300 autoscaling slots.
  3. if there are no idle slots available in other reservations, it will scale up to 1000 slots with 200 baseline and 800 autoscaling slots.



Please note, in this mode, the ignore_idle_slots field must be set to false. Otherwise the request will be rejected with error code `google.rpc.Code.INVALID_ARGUMENT`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
