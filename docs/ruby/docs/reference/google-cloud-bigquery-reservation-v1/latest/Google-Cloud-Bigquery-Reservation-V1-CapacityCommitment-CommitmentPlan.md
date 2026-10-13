---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-CapacityCommitment-CommitmentPlan/
title: BigQuery Reservation V1 API - Module Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment::CommitmentPlan (v1.14.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:42:18.919687+00:00
---

# BigQuery Reservation V1 API - Module Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment::CommitmentPlan (v1.14.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-CapacityCommitment-CommitmentPlan/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Reservation V1 API - Module Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment::CommitmentPlan (v1.14.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.14.0 (latest)  1.13.1  1.12.1  1.11.0  1.10.0  1.9.2  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.12.0  0.11.2  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.2 

Reference documentation and code samples for the BigQuery Reservation V1 API module Google::Cloud::Bigquery::Reservation::V1::CapacityCommitment::CommitmentPlan.

Commitment plan defines the current committed period. Capacity commitment cannot be deleted during it's committed period.

## Constants 

### COMMITMENT_PLAN_UNSPECIFIED

**value:** 0  
Invalid plan value. Requests with this value will be rejected with error code `google.rpc.Code.INVALID_ARGUMENT`.

### FLEX

**value:** 3  
Deprecated: Flex commitments are deprecated. Please use Edition-based capacity commitments. Flex commitments have committed period of 1 minute after becoming ACTIVE. After that, they are not in a committed period anymore and can be removed any time.

### FLEX_FLAT_RATE

**value:** 7  
Same as FLEX, should only be used if flat-rate commitments are still available.

### TRIAL

**value:** 5  
Trial commitments have a committed period of 182 days after becoming ACTIVE. After that, they are converted to a new commitment based on the `renewal_plan`. Default `renewal_plan` for Trial commitment is Flex so that it can be deleted right after committed period ends.

### MONTHLY

**value:** 2  
Monthly commitments have a committed period of 30 days after becoming ACTIVE. After that, they are not in a committed period anymore and can be removed any time.

### MONTHLY_FLAT_RATE

**value:** 8  
Same as MONTHLY, should only be used if flat-rate commitments are still available.

### ANNUAL

**value:** 4  
Annual commitments have a committed period of 365 days after becoming ACTIVE. After that they are converted to a new commitment based on the renewal_plan.

### ANNUAL_FLAT_RATE

**value:** 9  
Same as ANNUAL, should only be used if flat-rate commitments are still available.

### THREE_YEAR

**value:** 10  
3-year commitments have a committed period of 1095(3 * 365) days after becoming ACTIVE. After that they are converted to a new commitment based on the renewal_plan.

### NONE

**value:** 6  
Should only be used for `renewal_plan` and is only meaningful if edition is specified to values other than EDITION_UNSPECIFIED. Otherwise CreateCapacityCommitmentRequest or UpdateCapacityCommitmentRequest will be rejected with error code `google.rpc.Code.INVALID_ARGUMENT`. If the renewal_plan is NONE, capacity commitment will be removed at the end of its commitment period.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
