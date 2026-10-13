---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-LineageOutput-ProgressReport-WorkSummary-State/
title: BigQuery Migration V2 API - Module Google::Cloud::Bigquery::Migration::V2::LineageOutput::ProgressReport::WorkSummary::State (v0.23.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:28:03.954905+00:00
---

# BigQuery Migration V2 API - Module Google::Cloud::Bigquery::Migration::V2::LineageOutput::ProgressReport::WorkSummary::State (v0.23.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-LineageOutput-ProgressReport-WorkSummary-State/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Migration V2 API - Module Google::Cloud::Bigquery::Migration::V2::LineageOutput::ProgressReport::WorkSummary::State (v0.23.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.23.0 (latest)  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.1  0.14.1  0.13.0  0.12.0  0.11.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the BigQuery Migration V2 API module Google::Cloud::Bigquery::Migration::V2::LineageOutput::ProgressReport::WorkSummary::State.

States of work. Each piece of work is in exactly one state. [SUCCEEDED], [FAILED] and [SKIPPED] are terminal states; work in the [IN_PROGRESS] will eventually transition to one of the terminal states.

## Constants 

### STATE_UNSPECIFIED

**value:** 0  
The state is not specified.

### SUCCEEDED

**value:** 1  
Work that was processed successfully.

### FAILED

**value:** 2  
Work that failed processing.

### IN_PROGRESS

**value:** 3  
Work that is currently being processed or queued for processing.

### SKIPPED

**value:** 4  
Work that was recognised as necessary to fully process inputs but was skipped due to system limitations.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
