---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_stub_util/StubServiceConverter/
title: google.appengine.datastore.datastore_stub_util.StubServiceConverter \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:02:43.057075+00:00
---

# google.appengine.datastore.datastore_stub_util.StubServiceConverter  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_stub_util/StubServiceConverter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.datastore.datastore_stub_util.StubServiceConverter Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L4046-L4853) Converter for v3/v4/v1 request/response protos suitable for use in stubs. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.datastore.datastore_stub_util.StubServiceConverter(
        entity_converter, query_converter
    )
    

## Methods

### `v1_commit_req_to_v3_txn`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L4157-L4168)
    
    
    v1_commit_req_to_v3_txn(
        v1_req
    )
    

Converts a v1 CommitRequest to a v3 Transaction. | Args  
---  
  
`v1_req` |  a googledatastore.CommitRequest   
  
Returns  
---  
a datastore_pb.Transaction()   
  
### `v1_rollback_req_to_v3_txn`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L4141-L4152)
    
    
    v1_rollback_req_to_v3_txn(
        v1_req
    )
    

Converts a v1 RollbackRequest to a v3 Transaction.

Args  
---  
  
`v1_req` |  a googledatastore.RollbackRequest   
  
Returns  
---  
a datastore_pb.Transaction()   
  
### `v1_run_query_req_to_v3_query`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L4173-L4219)
    
    
    v1_run_query_req_to_v3_query(
        v1_req, new_txn=None
    )
    

Converts a v1 RunQueryRequest to a v3 Query.

GQL is not supported.

Args  
---  
  
`v1_req` |  a googledatastore.RunQueryRequest   
`new_txn` |  a v1 transaction created ad-hoc for this query, or None.   
  
Returns  
---  
a datastore_pb.Query   
  
### `v1_run_query_resp_to_v3_query_result`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L4252-L4263)
    
    
    v1_run_query_resp_to_v3_query_result(
        v1_resp
    )
    

Converts a V4 RunQueryResponse to a v3 QueryResult.

Args  
---  
  
`v1_resp` |  a googledatastore.QueryResult   
  
Returns  
---  
a datastore_pb.QueryResult   
  
### `v1_to_v3_begin_transaction_req`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L4105-L4123)
    
    
    v1_to_v3_begin_transaction_req(
        app_id, v1_req
    )
    

Converts a v1 BeginTransactionRequest to a v3 BeginTransactionRequest.

Args  
---  
  
`app_id` |  app id   
`v1_req` |  a googledatastore.BeginTransactionRequest   
  
Returns  
---  
a datastore_pb.BeginTransactionRequest   
  
### `v1_to_v3_cursor`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L4054-L4065)
    
    
    v1_to_v3_cursor(
        v1_query_handle, v3_cursor
    )
    

Converts a v1 cursor string to a v3 Cursor.

Args  
---  
  
`v1_query_handle` |  a string representing a v1 query handle   
`v3_cursor` |  a datastore_pb.Cursor to populate   
  
### `v1_to_v3_get_req`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L4286-L4328)
    
    
    v1_to_v3_get_req(
        v1_req, new_txn=None
    )
    

Converts a v1 LookupRequest to a v3 GetRequest.

Args  
---  
  
`v1_req` |  a googledatastore.LookupRequest   
`new_txn` |  a v1 transaction created ad-hoc for this lookup, or None.   
  
Returns  
---  
a datastore_pb.GetRequest   
  
### `v1_to_v3_query_result`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L4360-L4404)
    
    
    v1_to_v3_query_result(
        v1_batch
    )
    

Converts a v1 QueryResultBatch to a v3 QueryResult.

Args  
---  
  
`v1_batch` |  a googledatastore.QueryResultBatch   
  
Returns  
---  
a datastore_pb.QueryResult   
  
### `v1_to_v3_txn`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L4078-L4089)
    
    
    v1_to_v3_txn(
        v1_txn, v3_txn
    )
    

Converts a v1 transaction string to a v3 Transaction.

Args  
---  
  
`v1_txn` |  a string representing a v1 transaction   
`v3_txn` |  a datastore_pb.Transaction() to populate   
  
### `v3_to_v1_begin_transaction_resp`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L4125-L4136)
    
    
    v3_to_v1_begin_transaction_resp(
        v3_resp
    )
    

Converts a v3 Transaction to a v1 BeginTransactionResponse.

Args  
---  
  
`v3_resp` |  a datastore_pb.Transaction()   
  
Returns  
---  
a googledatastore.BeginTransactionResponse   
  
### `v3_to_v1_lookup_resp`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L4330-L4358)
    
    
    v3_to_v1_lookup_resp(
        v3_resp, new_txn=None
    )
    

Converts a v3 GetResponse to a v1 LookupResponse.

Args  
---  
  
`v3_resp` |  a datastore_pb.GetResponse   
`new_txn` |  a v1 transaction created ad-hoc for this lookup, or None.   
  
Returns  
---  
a googledatastore.LookupResponse   
  
### `v3_to_v1_query_result_batch`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L4406-L4450)
    
    
    v3_to_v1_query_result_batch(
        v3_result, v1_batch
    )
    

Converts a v3 QueryResult to a v1 QueryResultBatch.

Args  
---  
  
`v3_result` |  a datastore_pb.QueryResult   
`v1_batch` |  a googledatastore.QueryResultBatch to populate   
  
### `v3_to_v1_run_query_req`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L4221-L4250)
    
    
    v3_to_v1_run_query_req(
        v3_req
    )
    

Converts a v3 Query to a v1 RunQueryRequest.

Args  
---  
  
`v3_req` |  a datastore_pb.Query   
  
Returns  
---  
a googledatastore.RunQueryRequest   
  
### `v3_to_v1_run_query_resp`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L4265-L4281)
    
    
    v3_to_v1_run_query_resp(
        v3_resp, new_txn=None
    )
    

Converts a v3 QueryResult to a V4 RunQueryResponse.

Args  
---  
  
`v3_resp` |  a datastore_pb.QueryResult   
`new_txn` |  optional, a transaction that was created when processing the RunQueryRequest.   
  
Returns  
---  
a googledatastore.RunQueryResponse   
  
### `v3_to_v4_begin_transaction_resp`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L4518-L4529)
    
    
    v3_to_v4_begin_transaction_resp(
        v3_resp
    )
    

Converts a v3 Transaction to a v4 BeginTransactionResponse.

Args  
---  
  
`v3_resp` |  a datastore_pb.Transaction()   
  
Returns  
---  
a datastore_v4_pb2.BeginTransactionResponse   
  
### `v3_to_v4_continue_query_resp`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L4694-L4705)
    
    
    v3_to_v4_continue_query_resp(
        v3_resp
    )
    

Converts a v3 QueryResult to a v4 ContinueQueryResponse.

Args  
---  
  
`v3_resp` |  a datastore_pb.QueryResult   
  
Returns  
---  
a datastore_v4_pb2.ContinueQueryResponse   
  
### `v3_to_v4_lookup_resp`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L4739-L4762)
    
    
    v3_to_v4_lookup_resp(
        v3_resp
    )
    

Converts a v3 GetResponse to a v4 LookupResponse.

Args  
---  
  
`v3_resp` |  a datastore_pb.GetResponse   
  
Returns  
---  
a datastore_v4_pb2.LookupResponse   
  
### `v3_to_v4_query_result_batch`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L4810-L4853)
    
    
    v3_to_v4_query_result_batch(
        v3_result, v4_batch
    )
    

Converts a v3 QueryResult to a v4 QueryResultBatch.

Args  
---  
  
`v3_result` |  a datastore_pb.QueryResult   
`v4_batch` |  a datastore_v4_pb2.QueryResultBatch to populate   
  
### `v3_to_v4_run_query_req`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L4604-L4640)
    
    
    v3_to_v4_run_query_req(
        v3_req
    )
    

Converts a v3 Query to a v4 RunQueryRequest.

Args  
---  
  
`v3_req` |  a datastore_pb.Query   
  
Returns  
---  
a datastore_v4_pb2.RunQueryRequest   
  
### `v3_to_v4_run_query_resp`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L4659-L4675)
    
    
    v3_to_v4_run_query_resp(
        v3_resp
    )
    

Converts a v3 QueryResult to a V4 RunQueryResponse.

Args  
---  
  
`v3_resp` |  a datastore_pb.QueryResult   
  
Returns  
---  
a datastore_v4_pb2.RunQueryResponse   
  
### `v4_commit_req_to_v3_txn`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L4550-L4561)
    
    
    v4_commit_req_to_v3_txn(
        v4_req
    )
    

Converts a v4 CommitRequest to a v3 Transaction.

Args  
---  
  
`v4_req` |  a datastore_v4_pb2.CommitRequest   
  
Returns  
---  
a datastore_pb.Transaction()   
  
### `v4_rollback_req_to_v3_txn`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L4534-L4545)
    
    
    v4_rollback_req_to_v3_txn(
        v4_req
    )
    

Converts a v4 RollbackRequest to a v3 Transaction.

Args  
---  
  
`v4_req` |  a datastore_v4_pb2.RollbackRequest   
  
Returns  
---  
a datastore_pb.Transaction()   
  
### `v4_run_query_req_to_v3_query`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L4566-L4602)
    
    
    v4_run_query_req_to_v3_query(
        v4_req
    )
    

Converts a v4 RunQueryRequest to a v3 Query.

GQL is not supported.

Args  
---  
  
`v4_req` |  a datastore_v4_pb2.RunQueryRequest   
  
Returns  
---  
a datastore_pb.Query   
  
### `v4_run_query_resp_to_v3_query_result`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L4642-L4657)
    
    
    v4_run_query_resp_to_v3_query_result(
        v4_resp
    )
    

Converts a V4 RunQueryResponse to a v3 QueryResult.

Args  
---  
  
`v4_resp` |  a datastore_v4_pb2.QueryResult   
  
Returns  
---  
a datastore_pb.QueryResult   
  
### `v4_to_v3_begin_transaction_req`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L4503-L4516)
    
    
    v4_to_v3_begin_transaction_req(
        app_id, v4_req
    )
    

Converts a v4 BeginTransactionRequest to a v3 BeginTransactionRequest.

Args  
---  
  
`app_id` |  app id   
`v4_req` |  a datastore_v4_pb2.BeginTransactionRequest   
  
Returns  
---  
a datastore_pb.BeginTransactionRequest   
  
### `v4_to_v3_cursor`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L4452-L4463)
    
    
    v4_to_v3_cursor(
        v4_query_handle, v3_cursor
    )
    

Converts a v4 cursor string to a v3 Cursor.

Args  
---  
  
`v4_query_handle` |  a string representing a v4 query handle   
`v3_cursor` |  a datastore_pb.Cursor to populate   
  
### `v4_to_v3_get_req`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L4710-L4737)
    
    
    v4_to_v3_get_req(
        v4_req
    )
    

Converts a v4 LookupRequest to a v3 GetRequest.

Args  
---  
  
`v4_req` |  a datastore_v4_pb2.LookupRequest   
  
Returns  
---  
a datastore_pb.GetRequest   
  
### `v4_to_v3_next_req`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L4680-L4692)
    
    
    v4_to_v3_next_req(
        v4_req
    )
    

Converts a v4 ContinueQueryRequest to a v3 NextRequest.

Args  
---  
  
`v4_req` |  a datastore_v4_pb2.ContinueQueryRequest   
  
Returns  
---  
a datastore_pb.NextRequest   
  
### `v4_to_v3_query_result`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L4764-L4808)
    
    
    v4_to_v3_query_result(
        v4_batch
    )
    

Converts a v4 QueryResultBatch to a v3 QueryResult.

Args  
---  
  
`v4_batch` |  a datastore_v4_pb2.QueryResultBatch   
  
Returns  
---  
a datastore_pb.QueryResult   
  
### `v4_to_v3_txn`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L4476-L4487)
    
    
    v4_to_v3_txn(
        v4_txn, v3_txn
    )
    

Converts a v4 transaction string to a v3 Transaction.

Args  
---  
  
`v4_txn` |  a string representing a v4 transaction   
`v3_txn` |  a datastore_pb.Transaction() to populate   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
