---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-BatchUpdate/
title: Cloud Spanner API - Class Google::Cloud::Spanner::BatchUpdate (v2.36.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:23:09.117522+00:00
---

# Cloud Spanner API - Class Google::Cloud::Spanner::BatchUpdate (v2.36.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-BatchUpdate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Spanner API - Class Google::Cloud::Spanner::BatchUpdate (v2.36.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.36.0 (latest)  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.1  2.18.1  2.17.0  2.16.1  2.15.0  2.14.0  2.13.0  2.12.1  2.11.0 

Reference documentation and code samples for the Cloud Spanner API class Google::Cloud::Spanner::BatchUpdate.

## BatchUpdate

Accepts DML statements and optional parameters and types of the parameters for a batch update.

See [Transaction#batch_update](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Transaction#Google__Cloud__Spanner__Transaction_batch_update_instance_ "Google::Cloud::Spanner::Transaction#batch_update \(method\)").

## Inherits

  * Object 



## Methods 

### #batch_update
    
    
    def batch_update(sql, params: nil, types: nil)

Adds a DML statement to a batch update. See [Transaction#batch_update](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Transaction#Google__Cloud__Spanner__Transaction_batch_update_instance_ "Google::Cloud::Spanner::Transaction#batch_update \(method\)").

**Parameters**

  * **sql** (String) — The DML statement string. See [Query syntax](https://cloud.google.com/spanner/docs/query-syntax).

The DML statement string can contain parameter placeholders. A parameter placeholder consists of "@" followed by the parameter name. Parameter names consist of any combination of letters, numbers, and underscores. 

  * **params** (Hash) _(defaults to: nil)_ — Parameters for the DML statement string. The parameter placeholders, minus the "@", are the the hash keys, and the literal values are the hash values. If the query string contains something like "WHERE id > @msg_id", then the params must contain something like `:msg_id => 1`.

Ruby types are mapped to Spanner types as follows:

| Spanner | Ruby | Notes | |-------------|----------------|---| | `BOOL` | `true`/`false` | | | `INT64` | `Integer` | | | `FLOAT64` | `Float` | | | `FLOAT32` | `Float` | | | `STRING` | `String` | | | `DATE` | `Date` | | | `TIMESTAMP` | `Time`, `DateTime` | | | `BYTES` | `File`, `IO`, `StringIO`, or similar | | | `ARRAY` | `Array` | Nested arrays are not supported. | | `STRUCT` | `Hash`, [Data](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Data "Google::Cloud::Spanner::Data \(class\)") | |

See [Data types](https://cloud.google.com/spanner/docs/data-definition-language#data_types).

See [Data Types - Constructing a STRUCT](https://cloud.google.com/spanner/docs/data-types#constructing-a-struct). 

  * **types** (Hash) _(defaults to: nil)_ — 

Types of the SQL parameters in `params`. It is not always possible for Cloud Spanner to infer the right SQL type from a value in `params`. In these cases, the `types` hash can be used to specify the exact SQL type for some or all of the SQL query parameters.

The keys of the hash should be query string parameter placeholders, minus the "@". The values of the hash should be Cloud Spanner type codes from the following list:

    * `:BOOL`
    * `:BYTES`
    * `:DATE`
    * `:FLOAT64`
    * `:FLOAT32`
    * `:INT64`
    * `:STRING`
    * `:TIMESTAMP`
    * `Array` \- Lists are specified by providing the type code in an array. For example, an array of integers are specified as `[:INT64]`.
    * [Fields](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Fields "Google::Cloud::Spanner::Fields \(class\)") \- Nested Structs are specified by providing a Fields object.



**Examples**
    
    
    require "google/cloud/spanner"
    
    spanner = Google::Cloud::Spanner.new
    db = spanner.client "my-instance", "my-database"
    
    db.transaction do |tx|
      begin
        row_counts = tx.batch_update do |b|
          statement_count = b.batch_update(
            "UPDATE users SET name = 'Charlie' WHERE id = 1"
          )
        end
        puts row_counts.inspect
      rescue Google::Cloud::Spanner::BatchUpdateError => err
        puts err.cause.message
        puts err.row_counts.inspect
      end
    end

Update using SQL parameters:
    
    
    require "google/cloud/spanner"
    
    spanner = Google::Cloud::Spanner.new
    db = spanner.client "my-instance", "my-database"
    
    db.transaction do |tx|
      begin
        row_counts = tx.batch_update do |b|
          statement_count = b.batch_update(
            "UPDATE users SET name = 'Charlie' WHERE id = 1",
            params: { id: 1, name: "Charlie" }
          )
        end
        puts row_counts.inspect
      rescue Google::Cloud::Spanner::BatchUpdateError => err
        puts err.cause.message
        puts err.row_counts.inspect
      end
    end

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-09 UTC."],[],[]] 
