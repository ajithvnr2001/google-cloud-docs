---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage/latest/Google-Cloud-Bigquery-Storage/
title: BigQuery Storage API - Module Google::Cloud::Bigquery::Storage (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:42:34.806318+00:00
---

# BigQuery Storage API - Module Google::Cloud::Bigquery::Storage (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage/latest/Google-Cloud-Bigquery-Storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Storage API - Module Google::Cloud::Bigquery::Storage (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.0  1.6.2  1.5.1  1.4.0  1.3.0  1.2.1 

Reference documentation and code samples for the BigQuery Storage API module Google::Cloud::Bigquery::Storage.

## Methods 

### .big_query_read
    
    
    def self.big_query_read(version: :v1, &block) -> ::Object

Create a new client object for BigQueryRead.

By default, this returns an instance of [Google::Cloud::Bigquery::Storage::V1::BigQueryRead::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-BigQueryRead-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the BigQueryRead service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the BigQueryRead service. You can determine whether the method will succeed by calling [Storage.big_query_read_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage/latest/Google-Cloud-Bigquery-Storage#Google__Cloud__Bigquery__Storage_big_query_read_available__class_ "Google::Cloud::Bigquery::Storage.big_query_read_available? \(method\)").

#### About BigQueryRead

BigQuery Read API.

The Read API can be used to read data from BigQuery.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .big_query_read_available?
    
    
    def self.big_query_read_available?(version: :v1) -> boolean

Determines whether the BigQueryRead service is supported by the current client. If true, you can retrieve a client object by calling [Storage.big_query_read](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage/latest/Google-Cloud-Bigquery-Storage#Google__Cloud__Bigquery__Storage_big_query_read_class_ "Google::Cloud::Bigquery::Storage.big_query_read \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the BigQueryRead service, or if the versioned client gem needs an update to support the BigQueryRead service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .big_query_write
    
    
    def self.big_query_write(version: :v1, &block) -> ::Object

Create a new client object for BigQueryWrite.

By default, this returns an instance of [Google::Cloud::Bigquery::Storage::V1::BigQueryWrite::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-BigQueryWrite-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the BigQueryWrite service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the BigQueryWrite service. You can determine whether the method will succeed by calling [Storage.big_query_write_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage/latest/Google-Cloud-Bigquery-Storage#Google__Cloud__Bigquery__Storage_big_query_write_available__class_ "Google::Cloud::Bigquery::Storage.big_query_write_available? \(method\)").

#### About BigQueryWrite

BigQuery Write API.

The Write API can be used to write data to BigQuery.

For supplementary information about the Write API, see: <https://cloud.google.com/bigquery/docs/write-api>

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .big_query_write_available?
    
    
    def self.big_query_write_available?(version: :v1) -> boolean

Determines whether the BigQueryWrite service is supported by the current client. If true, you can retrieve a client object by calling [Storage.big_query_write](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage/latest/Google-Cloud-Bigquery-Storage#Google__Cloud__Bigquery__Storage_big_query_write_class_ "Google::Cloud::Bigquery::Storage.big_query_write \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the BigQueryWrite service, or if the versioned client gem needs an update to support the BigQueryWrite service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .configure
    
    
    def self.configure() -> ::Google::Cloud::Config

Configure the google-cloud-bigquery-storage library.

The following configuration parameters are supported:

  * `credentials` (_type:_ `String, Hash, Google::Auth::Credentials`) - The path to the keyfile as a String, the contents of the keyfile as a Hash, or a Google::Auth::Credentials object.
  * `lib_name` (_type:_ `String`) - The library name as recorded in instrumentation and logging.
  * `lib_version` (_type:_ `String`) - The library version as recorded in instrumentation and logging.
  * `interceptors` (_type:_ `Array<GRPC::ClientInterceptor>`) - An array of interceptors that are run before calls are executed.
  * `timeout` (_type:_ `Numeric`) - Default timeout in seconds.
  * `metadata` (_type:_ `Hash{Symbol=>String}`) - Additional headers to be sent with the call.
  * `retry_policy` (_type:_ `Hash`) - The retry policy. The value is a hash with the following keys: 
    * `:initial_delay` (_type:_ `Numeric`) - The initial delay in seconds.
    * `:max_delay` (_type:_ `Numeric`) - The max delay in seconds.
    * `:multiplier` (_type:_ `Numeric`) - The incremental backoff multiplier.
    * `:jitter` (_type:_ `Numeric`) - The jitter in seconds. Default: 1.0.
    * `:retry_codes` (_type:_ `Array<String>`) - The error codes that should trigger a retry.



**Yields**

  * (::Google::Cloud.configure.bigquery_storage) 



**Returns**

  * (::Google::Cloud::Config) — The default configuration used by this library 



## Constants 

### VERSION

**value:** "1.8.1"

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
