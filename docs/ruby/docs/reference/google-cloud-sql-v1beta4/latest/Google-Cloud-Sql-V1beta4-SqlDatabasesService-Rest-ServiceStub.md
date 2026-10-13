---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-SqlDatabasesService-Rest-ServiceStub/
title: Cloud SQL Admin V1BETA4 API - Class Google::Cloud::Sql::V1beta4::SqlDatabasesService::Rest::ServiceStub (v0.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:06:50.336794+00:00
---

# Cloud SQL Admin V1BETA4 API - Class Google::Cloud::Sql::V1beta4::SqlDatabasesService::Rest::ServiceStub (v0.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-SqlDatabasesService-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud SQL Admin V1BETA4 API - Class Google::Cloud::Sql::V1beta4::SqlDatabasesService::Rest::ServiceStub (v0.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.2.0 (latest)  0.1.1 

Reference documentation and code samples for the Cloud SQL Admin V1BETA4 API class Google::Cloud::Sql::V1beta4::SqlDatabasesService::Rest::ServiceStub.

REST service stub for the SqlDatabasesService service. Service stub contains baseline method implementations including transcoding, making the REST call, and deserialing the response.

## Inherits

  * Object 



## Methods 

### #delete
    
    
    def delete(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Sql::V1beta4::Operation

Baseline implementation for the delete REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Sql::V1beta4::SqlDatabasesDeleteRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-SqlDatabasesDeleteRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Sql::V1beta4::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Sql::V1beta4::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #endpoint
    
    
    def endpoint() -> String

The effective endpoint

**Returns**

  * (String) 



### #get
    
    
    def get(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Sql::V1beta4::Database

Baseline implementation for the get REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Sql::V1beta4::SqlDatabasesGetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-SqlDatabasesGetRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Sql::V1beta4::Database](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-Database)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Sql::V1beta4::Database](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-Database)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #insert
    
    
    def insert(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Sql::V1beta4::Operation

Baseline implementation for the insert REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Sql::V1beta4::SqlDatabasesInsertRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-SqlDatabasesInsertRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Sql::V1beta4::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Sql::V1beta4::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list
    
    
    def list(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Sql::V1beta4::DatabasesListResponse

Baseline implementation for the list REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Sql::V1beta4::SqlDatabasesListRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-SqlDatabasesListRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Sql::V1beta4::DatabasesListResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-DatabasesListResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Sql::V1beta4::DatabasesListResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-DatabasesListResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #logger
    
    
    def logger(stub: false) -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #patch
    
    
    def patch(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Sql::V1beta4::Operation

Baseline implementation for the patch REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Sql::V1beta4::SqlDatabasesUpdateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-SqlDatabasesUpdateRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Sql::V1beta4::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Sql::V1beta4::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update
    
    
    def update(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Sql::V1beta4::Operation

Baseline implementation for the update REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Sql::V1beta4::SqlDatabasesUpdateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-SqlDatabasesUpdateRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Sql::V1beta4::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Sql::V1beta4::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
