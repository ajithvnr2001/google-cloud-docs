---
url: https://docs.cloud.google.com/bigtable/docs/hbase-metrics/
title: Legacy HBase client-side metrics \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:36:35.300329+00:00
---

# Legacy HBase client-side metrics  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/hbase-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Legacy HBase client-side metrics

This page describes a set of client-side metrics that has been replaced with built-in client-side metrics. This page is maintained as a reference for any developers who still use the legacy metrics.

**We recommend using the built-in client-side metrics described on the[Client-side metrics overview](https://docs.cloud.google.com/bigtable/docs/client-side-metrics) instead of the legacy metrics described on this page.**

## Enable metrics

This information is provided for customers who are using the legacy metrics. To enable the newer, built-in client-side metrics, see [Set up client-side metrics](https://docs.cloud.google.com/bigtable/docs/client-side-metrics-setup).

The Cloud Bigtable HBase client for Java used [Dropwizard Metrics](http://metrics.dropwizard.io/) to collect and report client-side metrics. Because collecting metrics can add a very small amount of latency (single-digit microseconds) to each request, metrics were not enabled by default. The following sections explain how to enable the legacy client-side metrics.

### Use the Log4j reporter

The simplest way to enable the legacy client-side metrics is to add the following line to your [Log4j](https://logging.apache.org/log4j/) configuration file:
    
    
    log4j.category.com.google.cloud.bigtable.metrics=DEBUG
    

This configuration setting turns on metrics collection and logs Bigtable metrics with an [SLF4J logger](http://metrics.dropwizard.io/3.1.0/manual/core/#man-core-reporters-slf4j).

### Use other reporters

You can use other types of reporters by updating your application's code. For example, here is a reporter that sends metrics to a [Graphite](https://graphiteapp.org/) server:
    
    
    Graphite pickledGraphite = new PickledGraphite(new InetSocketAddress("graphite.example.com", 2004));
    DropwizardMetricRegistry registry = new DropwizardMetricRegistry();
    GraphiteReporter reporter =
        GraphiteReporter.forRegistry(registry.getRegistry())
            .convertRatesTo(TimeUnit.SECONDS)
            .convertDurationsTo(TimeUnit.MILLISECONDS)
            .filter(MetricFilter.ALL)
            .build(pickledGraphite);
    reporter.start(1, TimeUnit.MINUTES);
    BigtableClientMetrics.setMetricRegistry(registry);
    

Dropwizard Metrics [provides reporters](http://metrics.dropwizard.io/3.1.0/manual/core/#reporters) for JMX, console logging, SLF4J, and CSV. There are also a variety of [third-party reporters](http://metrics.dropwizard.io/3.1.0/manual/third-party/) available.

## Available metrics

This section describes the metrics that are available when the legacy HBase client-side metrics are enabled. Each metric has one of the following types:

  * **Counter** : A cumulative count per Java virtual machine (JVM).
  * **Meter** : Count information plus throughput information (a count per the last minute, 5 minutes, or 15 minutes)
  * **Timer** : Meter information plus latency information (such as median, mean, and 95th percentile)



Only certain metrics are collected for each type of request. See "Example: Metrics for a `Put` request" for an example of the metrics that are collected during a `Put` request.

### Channel-level metrics

Type | Name | Description  
---|---|---  
Counter | `google-cloud-bigtable.sessions.active` | How many `BigtableSession`s are opened. Each HBase `Connection` has a single `BigtableSession`.  
Counter | `google-cloud-bigtable.grpc.channel.active` | How many lower-level gRPC/Netty channels are opened. Each `BigtableSession` has many gRPC channels.  
  
### General RPC metrics

Type | Name | Description  
---|---|---  
Counter | `google-cloud-bigtable.grpc.rpc.active` | The number of remote procedure calls (RPCs) that are currently active.  
Meter | `google-cloud-bigtable.grpc.rpc.performed` | RPC throughput.  
  
### Data method metrics

Data method metrics are collected for the following data methods:

  * `ReadRows`: Implements gets and scans.
  * `MutateRow`: Implements puts and deletes.
  * `MutateRows`: Implements bulk writes.
  * `CheckAndMutateRow`: Implements HBase's `checkAnd*` methods.
  * `ReadModifyWrite`: Implements HBase's `Append` and `Increment` methods.
  * `SampleRowKeys`: Retrieves region information that is used for MapReduce operations.

Type | Name | Description  
---|---|---  
Timer | `google-cloud-bigtable.grpc.method.[METHOD_TYPE].operation.latency` | The length of time that individual operations take. Operations include the total amount of latency of all RPCs that are performed. (Usually only one RPC is performed. Client-side retries can cause the same RPC to be performed more than once if there is a transient error.)  
Timer | `google-cloud-bigtable.grpc.method.ReadRows.firstResponse.latency` | The length of time that it takes to receive the first response to a scan request.  
Meter | `google-cloud-bigtable.grpc.method.[METHOD_TYPE].retries.performed` | The number of retries that were performed.  
Meter | `google-cloud-bigtable.grpc.method.[METHOD_TYPE].failures` | The number of non-retryable failures.  
Meter | `google-cloud-bigtable.grpc.method.[METHOD_TYPE].retries.exhausted` | The number of times that retrying was aborted because too many retries had failed.  
  
### Bulk metrics

Bulk metrics are provided for methods that return more than one response, such as a bulk write.

Type | Name | Description  
---|---|---  
Meter | `google-cloud-bigtable.scanner.results` | The throughput of individual rows returned by a scan.  
Meter | `google-cloud-bigtable.bulk-mutator.mutations.added` | The throughput of individual mutations added for each `MutateRows` request.  
Meter | `google-cloud-bigtable.bulk-mutator.mutations.retried` | The number of individual mutations retried over time.  
  
### Bigtable table metrics

Converting Bigtable objects to HBase objects can add to the latency of a request. The following timers can be correlated with the specified `*.operation.latency` timers to measure the cost of the conversion.

Type | Name | Description  
---|---|---  
Timer | `google-cloud-bigtable.table.put.latency` | The length of time that individual `Put` operations take. Correlates with `google-cloud-bigtable.grpc.method.MutateRow.operation.latency`.  
Timer | `google-cloud-bigtable.table.get.latency` | The length of time that individual `Get` operations take. Correlates with `google-cloud-bigtable.grpc.method.ReadRows.operation.latency`.  
  
## Example: Metrics for a `Put` request

When client-side metrics are enabled, the following metrics are collected for a successful `Put` request that is not retried:

  * **Counter** : `google-cloud-bigtable.grpc.rpc.active`
  * **Meter** : `google-cloud-bigtable.grpc.rpc.performed`
  * **Timer** : `google-cloud-bigtable.grpc.method.MutateRow.operation.latency`
  * **Timer** : `google-cloud-bigtable.table.put.latency`



Collecting these metrics adds approximately 1 microsecond (1/1000 of a millisecond) to the `Put` operation. The overall `Put` operation could be as fast as 2 to 3 milliseconds, assuming that the operation includes about 1 KB of data.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
