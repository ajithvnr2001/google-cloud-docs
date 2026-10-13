---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsResponseOrBuilder
title: Interface AppendRowsResponseOrBuilder (3.35.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:59:58.732986+00:00
---

# Interface AppendRowsResponseOrBuilder (3.35.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsResponseOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AppendRowsResponseOrBuilder (3.35.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.35.0 (latest)  3.31.0  3.30.0  3.29.0  3.27.0  3.24.0  3.23.0  3.21.0  3.20.0  3.19.1  3.18.0  3.17.3  3.16.3  3.15.3  3.14.1  3.12.0  3.11.4  3.10.3  3.9.3  3.8.0  3.6.1  3.5.2  3.4.0  3.3.1  3.2.0  3.1.0  3.0.1  2.47.0  2.45.0  2.44.1  2.43.0 
    
    
    public interface AppendRowsResponseOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAppendResult()
    
    
    public abstract AppendRowsResponse.AppendResult getAppendResult()

Result if the append is successful.

`.google.cloud.bigquery.storage.v1.AppendRowsResponse.AppendResult append_result = 1; `

**Returns**  
---  
**Type** | **Description**  
`[AppendRowsResponse.AppendResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsResponse.AppendResult)` | The appendResult.  
  
### getAppendResultOrBuilder()
    
    
    public abstract AppendRowsResponse.AppendResultOrBuilder getAppendResultOrBuilder()

Result if the append is successful.

`.google.cloud.bigquery.storage.v1.AppendRowsResponse.AppendResult append_result = 1; `

**Returns**  
---  
**Type** | **Description**  
`[AppendRowsResponse.AppendResultOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsResponse.AppendResultOrBuilder)` |   
  
### getError()
    
    
    public abstract Status getError()

Error returned when problems were encountered. If present, it indicates rows were not accepted into the system. Users can retry or continue with other append requests within the same connection.

Additional information about error signalling:

ALREADY_EXISTS: Happens when an append specified an offset, and the backend already has received data at this offset. Typically encountered in retry scenarios, and can be ignored.

OUT_OF_RANGE: Returned when the specified offset in the stream is beyond the current end of the stream.

INVALID_ARGUMENT: Indicates a malformed request or data.

ABORTED: Request processing is aborted because of prior failures. The request can be retried if previous failure is addressed.

INTERNAL: Indicates server side error(s) that can be retried.

`.google.rpc.Status error = 2;`

**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.Status` | The error.  
  
### getErrorOrBuilder()
    
    
    public abstract StatusOrBuilder getErrorOrBuilder()

Error returned when problems were encountered. If present, it indicates rows were not accepted into the system. Users can retry or continue with other append requests within the same connection.

Additional information about error signalling:

ALREADY_EXISTS: Happens when an append specified an offset, and the backend already has received data at this offset. Typically encountered in retry scenarios, and can be ignored.

OUT_OF_RANGE: Returned when the specified offset in the stream is beyond the current end of the stream.

INVALID_ARGUMENT: Indicates a malformed request or data.

ABORTED: Request processing is aborted because of prior failures. The request can be retried if previous failure is addressed.

INTERNAL: Indicates server side error(s) that can be retried.

`.google.rpc.Status error = 2;`

**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.StatusOrBuilder` |   
  
### getResponseCase()
    
    
    public abstract AppendRowsResponse.ResponseCase getResponseCase()

**Returns**  
---  
**Type** | **Description**  
`[AppendRowsResponse.ResponseCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsResponse.ResponseCase)` |   
  
### getRowErrors(int index)
    
    
    public abstract RowError getRowErrors(int index)

If a request failed due to corrupted rows, no rows in the batch will be appended. The API will return row level error info, so that the caller can remove the bad rows and retry the request.

`repeated .google.cloud.bigquery.storage.v1.RowError row_errors = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RowError](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.RowError)` |   
  
### getRowErrorsCount()
    
    
    public abstract int getRowErrorsCount()

If a request failed due to corrupted rows, no rows in the batch will be appended. The API will return row level error info, so that the caller can remove the bad rows and retry the request.

`repeated .google.cloud.bigquery.storage.v1.RowError row_errors = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getRowErrorsList()
    
    
    public abstract List<RowError> getRowErrorsList()

If a request failed due to corrupted rows, no rows in the batch will be appended. The API will return row level error info, so that the caller can remove the bad rows and retry the request.

`repeated .google.cloud.bigquery.storage.v1.RowError row_errors = 4;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[RowError](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.RowError)>` |   
  
### getRowErrorsOrBuilder(int index)
    
    
    public abstract RowErrorOrBuilder getRowErrorsOrBuilder(int index)

If a request failed due to corrupted rows, no rows in the batch will be appended. The API will return row level error info, so that the caller can remove the bad rows and retry the request.

`repeated .google.cloud.bigquery.storage.v1.RowError row_errors = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RowErrorOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.RowErrorOrBuilder)` |   
  
### getRowErrorsOrBuilderList()
    
    
    public abstract List<? extends RowErrorOrBuilder> getRowErrorsOrBuilderList()

If a request failed due to corrupted rows, no rows in the batch will be appended. The API will return row level error info, so that the caller can remove the bad rows and retry the request.

`repeated .google.cloud.bigquery.storage.v1.RowError row_errors = 4;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.bigquery.storage.v1.RowErrorOrBuilder>` |   
  
### getUpdatedSchema()
    
    
    public abstract TableSchema getUpdatedSchema()

If backend detects a schema update, pass it to user so that user can use it to input new type of message. It will be empty when no schema updates have occurred.

`.google.cloud.bigquery.storage.v1.TableSchema updated_schema = 3;`

**Returns**  
---  
**Type** | **Description**  
`[TableSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableSchema)` | The updatedSchema.  
  
### getUpdatedSchemaOrBuilder()
    
    
    public abstract TableSchemaOrBuilder getUpdatedSchemaOrBuilder()

If backend detects a schema update, pass it to user so that user can use it to input new type of message. It will be empty when no schema updates have occurred.

`.google.cloud.bigquery.storage.v1.TableSchema updated_schema = 3;`

**Returns**  
---  
**Type** | **Description**  
`[TableSchemaOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.TableSchemaOrBuilder)` |   
  
### getWriteStream()
    
    
    public abstract String getWriteStream()

The target of the append operation. Matches the write_stream in the corresponding request.

`string write_stream = 5;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The writeStream.  
  
### getWriteStreamBytes()
    
    
    public abstract ByteString getWriteStreamBytes()

The target of the append operation. Matches the write_stream in the corresponding request.

`string write_stream = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for writeStream.  
  
### hasAppendResult()
    
    
    public abstract boolean hasAppendResult()

Result if the append is successful.

`.google.cloud.bigquery.storage.v1.AppendRowsResponse.AppendResult append_result = 1; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the appendResult field is set.  
  
### hasError()
    
    
    public abstract boolean hasError()

Error returned when problems were encountered. If present, it indicates rows were not accepted into the system. Users can retry or continue with other append requests within the same connection.

Additional information about error signalling:

ALREADY_EXISTS: Happens when an append specified an offset, and the backend already has received data at this offset. Typically encountered in retry scenarios, and can be ignored.

OUT_OF_RANGE: Returned when the specified offset in the stream is beyond the current end of the stream.

INVALID_ARGUMENT: Indicates a malformed request or data.

ABORTED: Request processing is aborted because of prior failures. The request can be retried if previous failure is addressed.

INTERNAL: Indicates server side error(s) that can be retried.

`.google.rpc.Status error = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the error field is set.  
  
### hasUpdatedSchema()
    
    
    public abstract boolean hasUpdatedSchema()

If backend detects a schema update, pass it to user so that user can use it to input new type of message. It will be empty when no schema updates have occurred.

`.google.cloud.bigquery.storage.v1.TableSchema updated_schema = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updatedSchema field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
