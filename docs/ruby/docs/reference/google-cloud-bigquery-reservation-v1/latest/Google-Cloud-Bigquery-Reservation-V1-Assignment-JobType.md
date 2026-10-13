---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Assignment-JobType/
title: BigQuery Reservation V1 API - Module Google::Cloud::Bigquery::Reservation::V1::Assignment::JobType (v1.14.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:42:18.216543+00:00
---

# BigQuery Reservation V1 API - Module Google::Cloud::Bigquery::Reservation::V1::Assignment::JobType (v1.14.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Assignment-JobType/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Reservation V1 API - Module Google::Cloud::Bigquery::Reservation::V1::Assignment::JobType (v1.14.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.14.0 (latest)  1.13.1  1.12.1  1.11.0  1.10.0  1.9.2  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.12.0  0.11.2  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.2 

Reference documentation and code samples for the BigQuery Reservation V1 API module Google::Cloud::Bigquery::Reservation::V1::Assignment::JobType.

Types of job, which could be specified when using the reservation.

## Constants 

### JOB_TYPE_UNSPECIFIED

**value:** 0  
Invalid type. Requests with this value will be rejected with error code `google.rpc.Code.INVALID_ARGUMENT`.

### PIPELINE

**value:** 1  
Pipeline (load/export) jobs from the project will use the reservation.

### QUERY

**value:** 2  
Query jobs from the project will use the reservation.

### ML_EXTERNAL

**value:** 3  
BigQuery ML jobs that use services external to BigQuery for model training. These jobs will not utilize idle slots from other reservations.

### BACKGROUND

**value:** 4  
Background jobs that BigQuery runs for the customers in the background.

### CONTINUOUS

**value:** 6  
Continuous SQL jobs will use this reservation. Reservations with continuous assignments cannot be mixed with non-continuous assignments.

### BACKGROUND_CHANGE_DATA_CAPTURE

**value:** 7  
Finer granularity background jobs for capturing changes in a source database and streaming them into BigQuery. Reservations with this job type take priority over a default BACKGROUND reservation assignment (if it exists).

### BACKGROUND_COLUMN_METADATA_INDEX

**value:** 8  
Finer granularity background jobs for refreshing cached metadata for BigQuery tables. Reservations with this job type take priority over a default BACKGROUND reservation assignment (if it exists).

### BACKGROUND_SEARCH_INDEX_REFRESH

**value:** 9  
Finer granularity background jobs for refreshing search indexes upon BigQuery table columns. Reservations with this job type take priority over a default BACKGROUND reservation assignment (if it exists).

### AUTOMATIC_MATERIALIZED_VIEW_REFRESH

**value:** 10  
Automated materialized view refresh jobs will use the reservation. Reservations with this job type will take priority over a default QUERY reservation assignment (if it exists).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
