---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-ExecuteSqlMetadata-Status/
title: AlloyDB V1ALPHA API - Module Google::Cloud::AlloyDB::V1alpha::ExecuteSqlMetadata::Status (v0.24.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:06:09.120622+00:00
---

# AlloyDB V1ALPHA API - Module Google::Cloud::AlloyDB::V1alpha::ExecuteSqlMetadata::Status (v0.24.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-ExecuteSqlMetadata-Status/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  AlloyDB V1ALPHA API - Module Google::Cloud::AlloyDB::V1alpha::ExecuteSqlMetadata::Status (v0.24.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.24.0 (latest)  0.23.1  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.0  0.14.1  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.0  0.7.2  0.6.0  0.5.2  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the AlloyDB V1ALPHA API module Google::Cloud::AlloyDB::V1alpha::ExecuteSqlMetadata::Status.

Status contains all valid Status a SQL execution can end up in.

## Constants 

### STATUS_UNSPECIFIED

**value:** 0  
The status is unknown.

### OK

**value:** 1  
No error during SQL execution i.e. All SQL statements ran to completion. The "message" will be empty.

### PARTIAL

**value:** 2  
Same as OK, except indicates that only partial results were returned. The "message" field will contain details on why results were truncated.

### ERROR

**value:** 3  
Error during SQL execution. Atleast 1 SQL statement execution resulted in a error. Side effects of other statements are rolled back. The "message" field will contain human readable error given by Postgres of the first bad SQL statement. SQL execution errors don't constitute API errors as defined in <https://google.aip.dev/193> but will be returned as part of this message.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
