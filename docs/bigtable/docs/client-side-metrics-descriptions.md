---
url: https://docs.cloud.google.com/bigtable/docs/client-side-metrics-descriptions/
title: Client-side metrics descriptions \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:42.045896+00:00
---

# Client-side metrics descriptions  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/client-side-metrics-descriptions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Client-side metrics descriptions

Client-side metrics are available for multiple Bigtable client libraries. This page provides a detailed description of each client-side metric.

For Go, C++, and Node.js, these metrics are enabled by default in the supported versions. For the Java client libraries, the metrics are available as an opt-in feature or by default, depending on the client library version. For information about the specific versions, see the "Client library support" section of each metric.

To learn how to set up and configure client-side metrics, see [Set up client-side metrics](https://docs.cloud.google.com/bigtable/docs/client-side-metrics-setup). For an overview, see the [Client-side metrics overview](https://docs.cloud.google.com/bigtable/docs/client-side-metrics).

Metrics are published to the region of the Bigtable cluster that they are for. If Bigtable can't resolve the cluster for a metric, like when an operation fails, then the metric is published to the global region and the `cluster` tag has the value `unspecified`.

Use client-side metrics in conjunction with server-side metrics for performance debugging. For a comprehensive list of Bigtable server-side and client-side metrics, see [Metrics](https://docs.cloud.google.com/bigtable/docs/metrics).

## Operation latencies

The following table shows the attributes and details of the operation latencies metric.

**Attribute** | **Description**  
---|---  
**Full metric** | `bigtable.googleapis.com/client/operation_latencies`  
**Definition** | The total end-to-end latency across all RPC attempts associated with a Bigtable operation. This metric measures an operation's round trip from the client to Bigtable and back to the client and includes all retries.  
  
For `ReadRows` requests, the operation latencies include the application processing time for each returned message.  
  
**Supported Bigtable operations** | 

  * `ReadRow`
  * `ReadRows`
  * `MutateRow`
  * `MutateRows`
  * `SampleRowKeys`
  * `CheckAndMutateRow`
  * `BulkReadRows`
  * `BulkMutateRows`

  
**Type** | Distribution  
**Available dimensions** | 

  * project ID
  * instance ID
  * table
  * cluster
  * zone
  * app profile ID
  * method name
  * final operation status
  * streaming operation
  * client name

  
  
### Client library support

The following table shows the minimum client library versions required to use the operation latencies metric.

Language | Client | Version (Opt-in) | Version (Enabled by default)  
---|---|---|---  
Java | `java-bigtable` | 2.16.0 | 2.38.0  
`java-bigtable-hbase` | 2.6.4 | 2.14.1  
Go |  | 1.27.0  
Node.js |  | 6.2.0 (`ReadRows` and `ReadRow` operations), 6.3.0 (other operations)  
C++ |  | 2.40.0  
  
## Attempt latencies

The following table shows the attributes and details of the attempt latencies metric.

**Attribute** | **Description**  
---|---  
**Full metric** | `bigtable.googleapis.com/client/attempt_latencies`  
**Definition** | The latencies of a client RPC attempt.  
  
Under normal circumstances, this value is identical to `operation_latencies`. If the client receives transient errors, however, then `operation_latencies` is the sum of all `attempt_latencies` and the exponential delays.  
  
**Supported Bigtable operations** | 

  * `ReadRow`
  * `ReadRows`
  * `MutateRow`
  * `MutateRows`
  * `SampleRowKeys`
  * `CheckAndMutateRow`
  * `BulkReadRows`
  * `BulkMutateRows`

  
**Type** | Distribution  
**Available dimensions** | 

  * project ID
  * instance ID
  * table
  * cluster
  * zone
  * app profile ID
  * method name
  * attempt status
  * streaming operation
  * client name

  
  
### Client library support

The following table shows the minimum client library versions required to use the attempt latencies metric.

Language | Client | Version (Opt-in) | Version (Enabled by default)  
---|---|---|---  
Java | `java-bigtable` | 2.16.0 | 2.38.0  
`java-bigtable-hbase` | 2.6.4 | 2.14.1  
Go |  | 1.27.0  
Node.js |  | 6.2.0 (`ReadRows` and `ReadRow` operations), 6.3.0 (other operations)  
C++ |  | 2.40.0  
  
## Retry count

The following table shows the attributes and details of the retry count metric.

**Attribute** | **Description**  
---|---  
**Full metric** | `bigtable.googleapis.com/client/retry_count`  
**Definition** | A counter that records the number of attempts that an operation required to complete. Under normal circumstances, this value is empty.  
**Supported Bigtable operations** | 

  * `ReadRow`
  * `ReadRows`
  * `MutateRow`
  * `MutateRows`
  * `SampleRowKeys`
  * `CheckAndMutateRow`
  * `BulkReadRows`
  * `BulkMutateRows`

  
**Type** | INT64  
**Available dimensions** | 

  * project ID
  * instance ID
  * table
  * cluster
  * zone
  * app profile ID
  * method name
  * final operation status
  * client name

  
  
### Client library support

The following table shows the minimum client library versions required to use the retry count metric.

Language | Client | Version (Opt-in) | Version (Enabled by default)  
---|---|---|---  
Java | `java-bigtable` | 2.16.0 | 2.38.0  
`java-bigtable-hbase` | 2.6.4 | 2.14.1  
Go |  | 1.27.0  
Node.js |  | 6.2.0 (`ReadRows` and `ReadRow` operations), 6.3.0 (other operations)  
C++ |  | 2.40.0  
  
## Application blocking latencies

The following table shows the attributes and details of the application blocking latencies metric.

**Attribute** | **Description**  
---|---  
**Full metric** | `bigtable.googleapis.com/client/application_blocking_latencies`  
**Definition** | The time from when the client receives the response to a request until the application reads the response. This metric is most relevant for `ReadRows` requests. The start and stop times for this metric depend on the way that you send the read request; see Application blocking latencies timer examples for details.   
**Supported Bigtable operations** | 

  * `ReadRow`
  * `ReadRows`
  * `MutateRow`
  * `MutateRows`
  * `SampleRowKeys`
  * `CheckAndMutateRow`
  * `BulkReadRows`
  * `BulkMutateRows`

  
**Type** | Distribution  
**Available dimensions** | 

  * project ID
  * instance ID
  * table
  * cluster
  * zone
  * app profile ID
  * method name
  * client name

  
  
### Client library support

The following table shows the minimum client library versions required to use the application blocking latencies metric.

Language | Client | Version (Opt-in) | Version (Enabled by default)  
---|---|---|---  
Java | `java-bigtable` | 2.16.0 | 2.38.0  
`java-bigtable-hbase` | 2.6.4 | 2.14.1  
Go |  | 1.38.0  
Node.js |  | 6.3.0 (`ReadRows` operation)  
C++ |  | 2.41.0  
  
### Application blocking latencies timer examples

`ReadRows` requests are typically sent in one of three ways: iteratively, asynchronously, or as a future call. The following examples demonstrate the start and stop times for the application blocking latencies for each type of `ReadRows` operation.

#### Iterative
    
    
    long totaLatency=0;
    ServerStream<Row> stream = bigtableDataClient.readRows(query);
    
    for (Row row : stream) {
       timer.start();
       // Do something with row
       timer.stop();
       totalLatency += timer.elapsed();
    }
    

#### Asynchronous
    
    
    client.readRowsAsync(query, new ResponseObserver<Row>() {
        @Override
        public void onStart(StreamController streamController) {
    
        }
    
        @Override
        public void onResponse(Row row) {
            timer.start();
            // Do something with the row
            timer.stop();
            totalLatency += timer.elapsed();
        }
    
        @Override
        public void onError(Throwable throwable) {
            // Do something with the error
        }
    
        @Override
        public void onComplete() {
        }
    });
    

#### Future call

The application blocking latencies should be approximately 0 (no timer) for this type of `ReadRows` request.
    
    
    List<Row> rows = bigtableDataClient.readRowsCallable().all().call(query);
    

## First-response latencies

The following table shows the attributes and details of the first-response latencies metric.

**Attribute** | **Description**  
---|---  
**Full metric** | `bigtable.googleapis.com/client/first_response_latencies`  
**Definition** | Latencies from when a client sends a request and receives the first row of the response.   
**Supported Bigtable operation** | `ReadRows`  
**Type** | Distribution  
**Available dimensions** | 

  * project ID
  * instance ID
  * table
  * cluster
  * zone
  * app profile ID
  * method name
  * final operation status
  * client name

  
  
### Client library support

The following table shows the minimum client library versions required to use the first-response latencies metric.

Language | Client | Version (Opt-in) | Version (Enabled by default)  
---|---|---|---  
Java | `java-bigtable` | 2.16.0 | 2.38.0  
`java-bigtable-hbase` | 2.6.4 | 2.14.1  
Go |  | 1.27.0  
Node.js |  | 6.2.0 (`ReadRows` and `ReadRow` operations), 6.3.0 (other operations)  
C++ |  | 2.40.0  
  
## Server latencies

The following table shows the attributes and details of the server latencies metric.

**Attribute** | **Description**  
---|---  
**Full metric** | `bigtable.googleapis.com/client/server_latencies`  
**Definition** | Latencies between the time when the Google frontend receives an RPC and when it sends the first byte of the response. When you use [direct connectivity](https://docs.cloud.google.com/bigtable/docs/performance#direct-connectivity), this metric is 0.   
**Supported Bigtable operations** | 

  * `ReadRow`
  * `ReadRows`
  * `MutateRow`
  * `MutateRows`
  * `SampleRowKeys`
  * `CheckAndMutateRow`
  * `BulkReadRows`
  * `BulkMutateRows`

  
**Type** |  Distribution   
**Available dimensions** | 

  * project ID
  * instance ID
  * table
  * cluster
  * zone
  * app profile ID
  * method name
  * attempt status
  * streaming operation
  * client name

  
  
### Client library support

The following table shows the minimum client library versions required to use the server latencies metric.

Language | Client | Version (Opt-in) | Version (Enabled by default)  
---|---|---|---  
Java | `java-bigtable` | 2.16.0 | 2.38.0  
`java-bigtable-hbase` | 2.6.4 | 2.14.1  
Go |  | 1.27.0  
Node.js |  | 6.2.0 (`ReadRows` and `ReadRow` operations), 6.3.0 (other operations)  
C++ |  | 2.41.0  
  
## Connectivity error count

The following table shows the attributes and details of the connectivity error count metric.

**Attribute** | **Description**  
---|---  
**Full metric** | `bigtable.googleapis.com/client/connectivity_error_count`  
**Definition** | The number of requests that failed to reach Google's network. In normal cases, this number is 0. When the number is not 0, it can indicate connectivity issues between the application and the Google network.   
**Supported Bigtable operations** | 

  * `ReadRow`
  * `ReadRows`
  * `MutateRow`
  * `MutateRows`
  * `SampleRowKeys`
  * `CheckAndMutateRow`
  * `BulkReadRows`
  * `BulkMutateRows`

  
**Type** |  Distribution   
**Available dimensions** | 

  * project ID
  * instance ID
  * table
  * cluster
  * zone
  * app profile ID
  * method name
  * attempt status
  * client name

  
  
### Client library support

The following table shows the minimum client library versions required to use the connectivity error count metric.

Language | Client | Version (Opt-in) | Version (Enabled by default)  
---|---|---|---  
Java | `java-bigtable` | 2.16.0 | 2.38.0  
`java-bigtable-hbase` | 2.6.4 | 2.14.1  
Go |  | 1.38.0  
Node.js |  | 6.2.0 (`ReadRows` and `ReadRow` operations), 6.3.0 (other operations)  
C++ |  | 2.41.0  
  
## Client blocking latencies

The following table shows the attributes and details of the client blocking latencies metric.

**Attribute** | **Description**  
---|---  
**Full metric** | `bigtable.googleapis.com/client/client_blocking_latencies`  
**Definition** | Latencies introduced when the client blocks the sending of more requests to the server because of too many pending requests in a bulk operation. For versions 2.21.0 and later, this metric also includes the latencies of requests queued on gRPC channels when the client creates a channel.   
**Supported Bigtable operations** | 

  * `ReadRow`
  * `ReadRows`
  * `MutateRow`
  * `MutateRows`
  * `SampleRowKeys`
  * `CheckAndMutateRow`
  * `BulkReadRows`
  * `BulkMutateRows`

  
**Type** |  Distribution   
**Available dimensions** | 

  * project ID
  * instance ID
  * table
  * cluster
  * zone
  * app profile ID
  * method name
  * client name

  
  
### Client library support

The following table shows the minimum Java client library versions required to use the client blocking latencies metric.

Language | Client | Version (Opt-in) | Version (Enabled by default)  
---|---|---|---  
Java | `java-bigtable` | 2.16.0 | 2.38.0  
`java-bigtable-hbase` | 2.6.4 | 2.14.1  
  
## What's next

  * [See all Google Cloud metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp).
  * [Install and configure client-side metrics.](https://docs.cloud.google.com/bigtable/docs/client-side-metrics-setup)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
