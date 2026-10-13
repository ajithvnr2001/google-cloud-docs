---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-Backup-QuantityBasedExpiry/
title: AlloyDB V1ALPHA API - Class Google::Cloud::AlloyDB::V1alpha::Backup::QuantityBasedExpiry (v0.24.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:57:29.492157+00:00
---

# AlloyDB V1ALPHA API - Class Google::Cloud::AlloyDB::V1alpha::Backup::QuantityBasedExpiry (v0.24.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-Backup-QuantityBasedExpiry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  AlloyDB V1ALPHA API - Class Google::Cloud::AlloyDB::V1alpha::Backup::QuantityBasedExpiry (v0.24.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.24.0 (latest)  0.23.1  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.0  0.14.1  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.0  0.7.2  0.6.0  0.5.2  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the AlloyDB V1ALPHA API class Google::Cloud::AlloyDB::V1alpha::Backup::QuantityBasedExpiry.

A backup's position in a quantity-based retention queue, of backups with the same source cluster and type, with length, retention, specified by the backup's retention policy. Once the position is greater than the retention, the backup is eligible to be garbage collected.

Example: 5 backups from the same source cluster and type with a quantity-based retention of 3 and denoted by backup_id (position, retention).

Safe: backup_5 (1, 3), backup_4, (2, 3), backup_3 (3, 3). Awaiting garbage collection: backup_2 (4, 3), backup_1 (5, 3)

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #retention_count
    
    
    def retention_count() -> ::Integer

**Returns**

  * (::Integer) — Output only. The backup's position among its backups with the same source cluster and type, by descending chronological order create time(i.e. newest first). 



### #total_retention_count
    
    
    def total_retention_count() -> ::Integer

**Returns**

  * (::Integer) — Output only. The length of the quantity-based queue, specified by the backup's retention policy. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
