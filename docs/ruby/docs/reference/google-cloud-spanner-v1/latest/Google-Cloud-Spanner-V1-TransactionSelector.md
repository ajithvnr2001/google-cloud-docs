---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-TransactionSelector/
title: Cloud Spanner V1 API - Class Google::Cloud::Spanner::V1::TransactionSelector (v1.19.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:02:12.616992+00:00
---

# Cloud Spanner V1 API - Class Google::Cloud::Spanner::V1::TransactionSelector (v1.19.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-TransactionSelector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Spanner V1 API - Class Google::Cloud::Spanner::V1::TransactionSelector (v1.19.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.19.2 (latest)  1.19.1  1.18.0  1.17.1  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.1  1.10.1  1.9.1  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.2  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.2  0.21.0  0.20.1  0.19.0  0.18.0  0.17.0  0.16.0  0.15.1  0.14.1  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.1  0.7.4 

Reference documentation and code samples for the Cloud Spanner V1 API class Google::Cloud::Spanner::V1::TransactionSelector.

This message is used to select the transaction in which a [Read](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-Spanner-Client#Google__Cloud__Spanner__V1__Spanner__Client_read_instance_ "Google::Cloud::Spanner::V1::Spanner::Client#read \(method\)") or [ExecuteSql](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-Spanner-Client#Google__Cloud__Spanner__V1__Spanner__Client_execute_sql_instance_ "Google::Cloud::Spanner::V1::Spanner::Client#execute_sql \(method\)") call runs.

See [TransactionOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-TransactionOptions "Google::Cloud::Spanner::V1::TransactionOptions \(class\)") for more information about transactions.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #begin
    
    
    def begin() -> ::Google::Cloud::Spanner::V1::TransactionOptions

**Returns**

  * ([::Google::Cloud::Spanner::V1::TransactionOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-TransactionOptions)) — Begin a new transaction and execute this read or SQL query in it. The transaction ID of the new transaction is returned in [ResultSetMetadata.transaction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-ResultSetMetadata#Google__Cloud__Spanner__V1__ResultSetMetadata_transaction_instance_ "Google::Cloud::Spanner::V1::ResultSetMetadata#transaction \(method\)"), which is a [Transaction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-Transaction "Google::Cloud::Spanner::V1::Transaction \(class\)").

Note: The following fields are mutually exclusive: `begin`, `single_use`, `id`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #begin=
    
    
    def begin=(value) -> ::Google::Cloud::Spanner::V1::TransactionOptions

**Parameter**

  * **value** ([::Google::Cloud::Spanner::V1::TransactionOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-TransactionOptions)) — Begin a new transaction and execute this read or SQL query in it. The transaction ID of the new transaction is returned in [ResultSetMetadata.transaction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-ResultSetMetadata#Google__Cloud__Spanner__V1__ResultSetMetadata_transaction_instance_ "Google::Cloud::Spanner::V1::ResultSetMetadata#transaction \(method\)"), which is a [Transaction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-Transaction "Google::Cloud::Spanner::V1::Transaction \(class\)").

Note: The following fields are mutually exclusive: `begin`, `single_use`, `id`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Spanner::V1::TransactionOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-TransactionOptions)) — Begin a new transaction and execute this read or SQL query in it. The transaction ID of the new transaction is returned in [ResultSetMetadata.transaction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-ResultSetMetadata#Google__Cloud__Spanner__V1__ResultSetMetadata_transaction_instance_ "Google::Cloud::Spanner::V1::ResultSetMetadata#transaction \(method\)"), which is a [Transaction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-Transaction "Google::Cloud::Spanner::V1::Transaction \(class\)").

Note: The following fields are mutually exclusive: `begin`, `single_use`, `id`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #id
    
    
    def id() -> ::String

**Returns**

  * (::String) — Execute the read or SQL query in a previously-started transaction.

Note: The following fields are mutually exclusive: `id`, `single_use`, `begin`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #id=
    
    
    def id=(value) -> ::String

**Parameter**

  * **value** (::String) — Execute the read or SQL query in a previously-started transaction.

Note: The following fields are mutually exclusive: `id`, `single_use`, `begin`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — Execute the read or SQL query in a previously-started transaction.

Note: The following fields are mutually exclusive: `id`, `single_use`, `begin`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #single_use
    
    
    def single_use() -> ::Google::Cloud::Spanner::V1::TransactionOptions

**Returns**

  * ([::Google::Cloud::Spanner::V1::TransactionOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-TransactionOptions)) — Execute the read or SQL query in a temporary transaction. This is the most efficient way to execute a transaction that consists of a single SQL query.

Note: The following fields are mutually exclusive: `single_use`, `id`, `begin`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #single_use=
    
    
    def single_use=(value) -> ::Google::Cloud::Spanner::V1::TransactionOptions

**Parameter**

  * **value** ([::Google::Cloud::Spanner::V1::TransactionOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-TransactionOptions)) — Execute the read or SQL query in a temporary transaction. This is the most efficient way to execute a transaction that consists of a single SQL query.

Note: The following fields are mutually exclusive: `single_use`, `id`, `begin`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Spanner::V1::TransactionOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-TransactionOptions)) — Execute the read or SQL query in a temporary transaction. This is the most efficient way to execute a transaction that consists of a single SQL query.

Note: The following fields are mutually exclusive: `single_use`, `id`, `begin`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
