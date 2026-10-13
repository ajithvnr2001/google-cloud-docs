---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging
title: Interface Logging (3.40.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:45:07.787571+00:00
---

# Interface Logging (3.40.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface Logging (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.36.0  3.35.0  3.34.0  3.32.0  3.29.0  3.28.0  3.26.0  3.24.0  3.23.10  3.22.6  3.21.4  3.20.7  3.19.0  3.18.0  3.17.2  3.16.2  3.15.17  3.14.9  3.13.7  3.12.1  3.11.10  3.10.7  3.9.0  3.8.0  3.7.6  3.6.4  3.5.3 
    
    
    public interface Logging extends AutoCloseable, Service<LoggingOptions>

## Implements

[AutoCloseable](https://docs.oracle.com/javase/8/docs/api/java/lang/AutoCloseable.html), com.google.cloud.Service<com.google.cloud.logging.LoggingOptions>

## Methods 

### create(Exclusion exclusion)
    
    
    public abstract Exclusion create(Exclusion exclusion)

Creates a new exclusion in a specified parent resource. Only log entries belonging to that resource can be excluded. You can have up to 10 exclusions in a resource.

Example of creating the exclusion:

{ @code String exclusionName = "my_exclusion_name"; Exclusion exclusion = Exclusion.of(exclusionName, "resource.type=gcs_bucket severity<ERROR sample(insertId, 0.99)"); Exclusion exclusion = logging.create(exclusion); }

**Parameter**  
---  
**Name** | **Description**  
`exclusion` | `[Exclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Exclusion)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Exclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Exclusion)` | the created exclusion  
  
### create(MetricInfo metric)
    
    
    public abstract Metric create(MetricInfo metric)

Creates a new metric.

Example of creating a metric for logs with severity higher or equal to ERROR.

{ @code String metricName = "my_metric_name"; MetricInfo metricInfo = MetricInfo.of(metricName, "severity>=ERROR"); Metric metric = logging.create(metricInfo); }

**Parameter**  
---  
**Name** | **Description**  
`metric` | `[MetricInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.MetricInfo)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Metric](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Metric)` | the created metric  
  
### create(SinkInfo sink)
    
    
    public abstract Sink create(SinkInfo sink)

Creates a new sink.

Example of creating a sink to export logs to a BigQuery dataset (in the LoggingOptions#getProjectId() project).

{ @code String sinkName = "my_sink_name"; String datasetName = "my_dataset"; SinkInfo sinkInfo = SinkInfo.of(sinkName, DatasetDestination.of(datasetName)); Sink sink = logging.create(sinkInfo); }

**Parameter**  
---  
**Name** | **Description**  
`sink` | `[SinkInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Sink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Sink)` | the created sink  
  
### createAsync(Exclusion exclusion)
    
    
    public abstract ApiFuture<Exclusion> createAsync(Exclusion exclusion)

Sends a request to create the exclusion. This method returns an `ApiFuture` object to consume the result. ApiFuture#get() returns the created exclusion.

Example of asynchronously creating the exclusion:
    
    
     String exclusionName = "my_exclusion_name";
     Exclusion exclusion = Exclusion.of(exclusionName,
         "resource.type=gcs_bucket severity

**Parameter**  
---  
**Name** | **Description**  
`exclusion` | `[Exclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Exclusion)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Exclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Exclusion)>` |   
  
### createAsync(MetricInfo metric)
    
    
    public abstract ApiFuture<Metric> createAsync(MetricInfo metric)

Sends a request for creating a metric. This method returns a `ApiFuture` object to consume the result. ApiFuture#get() returns the created metric.

Example of asynchronously creating a metric for logs with severity higher or equal to ERROR.
    
    
     String metricName = "my_metric_name";
     MetricInfo metricInfo = MetricInfo.of(metricName, "severity>=ERROR");
     ApiFuture<Metric> future = logging.createAsync(metricInfo);
     // ...
     Metric metric = future.get();
     

**Parameter**  
---  
**Name** | **Description**  
`metric` | `[MetricInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.MetricInfo)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Metric](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Metric)>` |   
  
### createAsync(SinkInfo sink)
    
    
    public abstract ApiFuture<Sink> createAsync(SinkInfo sink)

Sends a request for creating a sink. This method returns a `ApiFuture` object to consume the result. ApiFuture#get() returns the created sink.

Example of asynchronously creating a sink to export logs to a BigQuery dataset (in the LoggingOptions#getProjectId() project).
    
    
     String sinkName = "my_sink_name";
     String datasetName = "my_dataset";
     SinkInfo sinkInfo = SinkInfo.of(sinkName, DatasetDestination.of(datasetName));
     ApiFuture<Sink> future = logging.createAsync(sinkInfo);
     // ...
     Sink sink = future.get();
     

**Parameter**  
---  
**Name** | **Description**  
`sink` | `[SinkInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Sink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Sink)>` |   
  
### deleteExclusion(String exclusion)
    
    
    public abstract boolean deleteExclusion(String exclusion)

Deletes the requested exclusion.

Example of deleting the exclusion:
    
    
     String exclusionName = "my_exclusion_name";
     boolean deleted = logging.deleteExclusion(exclusionName);
     if (deleted) {
       // the exclusion was deleted
     } else {
       // the exclusion was not found
     }
     

**Parameter**  
---  
**Name** | **Description**  
`exclusion` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | `true` if the exclusion was deleted, `false` if it was not found  
  
### deleteExclusionAsync(String exclusion)
    
    
    public abstract ApiFuture<Boolean> deleteExclusionAsync(String exclusion)

Sends a request to delete an exclusion. This method returns an `ApiFuture` object to consume the result. ApiFuture#get() returns `true` if the exclusion was deleted, `false` if it was not found.

Example of asynchronously deleting the exclusion:
    
    
     String exclusionName = "my_exclusion_name";
     ApiFuture<Boolean> future = logging.deleteExclusionAsync(metricName);
     // ...
     boolean deleted = future.get();
     if (deleted) {
       // the exclusion was deleted
     } else {
       // the exclusion was not found
     }
     

**Parameter**  
---  
**Name** | **Description**  
`exclusion` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Boolean](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html)>` |   
  
### deleteLog(String log)
    
    
    public abstract boolean deleteLog(String log)

Deletes a log and all its log entries. The log will reappear if new entries are written to it.

Example of deleting a log.
    
    
     String logName = "my_log_name";
     boolean deleted = logging.deleteLog(logName);
     if (deleted) {
       // the log was deleted
     } else {
       // the log was not found
     }
     

**Parameter**  
---  
**Name** | **Description**  
`log` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | `true` if the log was deleted, `false` if it was not found  
  
### deleteLog(String log, LogDestinationName destination)
    
    
    public default boolean deleteLog(String log, LogDestinationName destination)

Deletes a log and all its log entries for given log destination (see 'logName' parameter in <https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry>). The log will reappear if new entries are written to it.

Example of deleting a log by folder destination.
    
    
     String logName = "my_log_name";
     String folder = "my_folder";
     boolean deleted = logging.deleteLog(logName, LogDestinationName.folder(folder));
     if (deleted) {
       // the log was deleted
     } else {
       // the log was not found
     }
     

**Parameters**  
---  
**Name** | **Description**  
`log` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`destination` | `[LogDestinationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogDestinationName)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | `true` if the log was deleted, `false` if it was not found  
  
### deleteLogAsync(String log)
    
    
    public abstract ApiFuture<Boolean> deleteLogAsync(String log)

Sends a request for deleting a log and all its log entries. This method returns a ` ApiFuture` object to consume the result. ApiFuture#get() returns `true` if the log was deleted, `false` if it was not found.

Example of asynchronously deleting a log.
    
    
     String logName = "my_log_name";
     ApiFuture<Boolean> future = logging.deleteLogAsync(logName);
     // ...
     boolean deleted = future.get();
     if (deleted) {
       // the log was deleted
     } else {
       // the log was not found
     }
     

**Parameter**  
---  
**Name** | **Description**  
`log` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Boolean](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html)>` |   
  
### deleteLogAsync(String log, LogDestinationName destination)
    
    
    public default ApiFuture<Boolean> deleteLogAsync(String log, LogDestinationName destination)

Sends a request for deleting a log and all its log entries for given log destination (see 'logName' parameter in <https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry>). This method returns a `ApiFuture` object to consume the result. ApiFuture#get() returns `true` if the log was deleted, `false` if it was not found.

Example of asynchronously deleting a log by folder destination.
    
    
     String logName = "my_log_name";
     String folder = "my_folder";
     ApiFuture<Boolean> future = logging.deleteLogAsync(logName, LogDestinationName.folder(folder));
     // ...
     boolean deleted = future.get();
     if (deleted) {
       // the log was deleted
     } else {
       // the log was not found
     }
     

**Parameters**  
---  
**Name** | **Description**  
`log` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`destination` | `[LogDestinationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogDestinationName)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Boolean](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html)>` |   
  
### deleteMetric(String metric)
    
    
    public abstract boolean deleteMetric(String metric)

Deletes the requested metric.

Example of deleting a metric.
    
    
     String metricName = "my_metric_name";
     boolean deleted = logging.deleteMetric(metricName);
     if (deleted) {
       // the metric was deleted
     } else {
       // the metric was not found
     }
     

**Parameter**  
---  
**Name** | **Description**  
`metric` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | `true` if the metric was deleted, `false` if it was not found  
  
### deleteMetricAsync(String metric)
    
    
    public abstract ApiFuture<Boolean> deleteMetricAsync(String metric)

Sends a request for deleting a metric. This method returns a `ApiFuture` object to consume the result. ApiFuture#get() returns `true` if the metric was deleted, `false` if it was not found.

Example of asynchronously deleting a metric.
    
    
     String metricName = "my_metric_name";
     ApiFuture<Boolean> future = logging.deleteMetricAsync(metricName);
     // ...
     boolean deleted = future.get();
     if (deleted) {
       // the metric was deleted
     } else {
       // the metric was not found
     }
     

**Parameter**  
---  
**Name** | **Description**  
`metric` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Boolean](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html)>` |   
  
### deleteSink(String sink)
    
    
    public abstract boolean deleteSink(String sink)

Deletes the requested sink.

Example of deleting a sink.
    
    
     String sinkName = "my_sink_name";
     boolean deleted = logging.deleteSink(sinkName);
     if (deleted) {
       // the sink was deleted
     } else {
       // the sink was not found
     }
     

**Parameter**  
---  
**Name** | **Description**  
`sink` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | `true` if the sink was deleted, `false` if it was not found  
  
### deleteSinkAsync(String sink)
    
    
    public abstract ApiFuture<Boolean> deleteSinkAsync(String sink)

Sends a request for deleting a sink. This method returns a `ApiFuture` object to consume the result. ApiFuture#get() returns `true` if the sink was deleted, `false` if it was not found.

Example of asynchronously deleting a sink.
    
    
     String sinkName = "my_sink_name";
     ApiFuture<Boolean> future = logging.deleteSinkAsync(sinkName);
     // ...
     boolean deleted = future.get();
     if (deleted) {
       // the sink was deleted
     } else {
       // the sink was not found
     }
     

**Parameter**  
---  
**Name** | **Description**  
`sink` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Boolean](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html)>` |   
  
### flush()
    
    
    public abstract void flush()

Flushes any pending asynchronous logging writes. Logs are automatically flushed based on time and message count that be configured via [com.google.api.gax.batching.BatchingSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.batching.BatchingSettings.html), Logs are also flushed if enabled, at or above flush severity, see [#setFlushSeverity](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging#com_google_cloud_logging_Logging_setFlushSeverity_). Logging frameworks require support for an explicit flush. See usage in the java.util.logging handler[LoggingHandler](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingHandler).

### getExclusion(String exclusion)
    
    
    public abstract Exclusion getExclusion(String exclusion)

Gets the description of an exclusion or `null` if not found.

Example of getting the description of an exclusion:
    
    
     String exclusionName = "my_exclusion_name";
     Exclusion exclusion = logging.getExclusion(exclusionName);
     if (exclusion == null) {
       // exclusion was not found
     }
     

**Parameter**  
---  
**Name** | **Description**  
`exclusion` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Exclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Exclusion)` |   
  
### getExclusionAsync(String exclusion)
    
    
    public abstract ApiFuture<Exclusion> getExclusionAsync(String exclusion)

Sends a request to get the description of an exclusion . This method returns an ` ApiFuture` object to consume the result. ApiFuture#get() returns the requested exclusion or `null` if not found.

Example of asynchronously getting the exclusion:
    
    
     String exclusionName = "my_exclusion_name";
     ApiFuture<Exclusion> future = logging.getExclusionAsync(exclusionName);
     // ...
     Exclusion exclusion = future.get();
     if (exclusion == null) {
       // exclusion was not found
     }
     

**Parameter**  
---  
**Name** | **Description**  
`exclusion` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Exclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Exclusion)>` |   
  
### getFlushSeverity()
    
    
    public abstract Severity getFlushSeverity()

**Returns**  
---  
**Type** | **Description**  
`[Severity](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Severity)` |   
  
### getMetric(String metric)
    
    
    public abstract Metric getMetric(String metric)

Returns the requested metric or `null` if not found.

Example of getting a metric.
    
    
     String metricName = "my_metric_name";
     Metric metric = logging.getMetric(metricName);
     if (metric == null) {
       // metric was not found
     }
     

**Parameter**  
---  
**Name** | **Description**  
`metric` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Metric](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Metric)` |   
  
### getMetricAsync(String metric)
    
    
    public abstract ApiFuture<Metric> getMetricAsync(String metric)

Sends a request for getting a metric. This method returns a `ApiFuture` object to consume the result. ApiFuture#get() returns the requested metric or `null` if not found.

Example of asynchronously getting a metric.
    
    
     String metricName = "my_metric_name";
     ApiFuture<Metric> future = logging.getMetricAsync(metricName);
     // ...
     Metric metric = future.get();
     if (metric == null) {
       // metric was not found
     }
     

**Parameter**  
---  
**Name** | **Description**  
`metric` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Metric](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Metric)>` |   
  
### getSink(String sink)
    
    
    public abstract Sink getSink(String sink)

Returns the requested sink or `null` if not found.

Example of getting a sink.
    
    
     String sinkName = "my_sink_name";
     Sink sink = logging.getSink(sinkName);
     if (sink == null) {
       // sink was not found
     }
     

**Parameter**  
---  
**Name** | **Description**  
`sink` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Sink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Sink)` |   
  
### getSinkAsync(String sink)
    
    
    public abstract ApiFuture<Sink> getSinkAsync(String sink)

Sends a request for getting a sink. This method returns a `ApiFuture` object to consume the result. ApiFuture#get() returns the requested sink or `null` if not found.

Example of asynchronously getting a sink.
    
    
     String sinkName = "my_sink_name";
     ApiFuture<Sink> future = logging.getSinkAsync(sinkName);
     // ...
     Sink sink = future.get();
     if (sink == null) {
       // sink was not found
     }
     

**Parameter**  
---  
**Name** | **Description**  
`sink` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Sink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Sink)>` |   
  
### getWriteSynchronicity()
    
    
    public abstract Synchronicity getWriteSynchronicity()

Retrieves current set synchronicity [Synchronicity](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Synchronicity) of logging writes.

**Returns**  
---  
**Type** | **Description**  
`[Synchronicity](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Synchronicity)` |   
  
### listExclusions(Logging.ListOption[] options)
    
    
    public abstract Page<Exclusion> listExclusions(Logging.ListOption[] options)

Lists the exclusion. This method returns a [Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html) object that can be used to consume paginated results. Use [ListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.ListOption) to specify the page size or the page token from which to start listing exclusion.

Example of listing exclusions, specifying the page size:
    
    
     Page<Exclusion> exclusions = logging.listMetrics(ListOption.pageSize(100));
     Iterator<Exclusion> exclusionIterator = exclusions.iterateAll().iterator();
     while (exclusionIterator.hasNext()) {
       Exclusion exclusion = exclusionIterator.next();
       // do something with the exclusion
     }
     

**Parameter**  
---  
**Name** | **Description**  
`options` | `[ListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.ListOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html)<[Exclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Exclusion)>` |   
  
### listExclusionsAsync(Logging.ListOption[] options)
    
    
    public abstract ApiFuture<AsyncPage<Exclusion>> listExclusionsAsync(Logging.ListOption[] options)

Sends a request for listing exclusions. This method returns an `ApiFuture` object to consume the result. ApiFuture#get() returns an [AsyncPage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AsyncPage.html) object that can be used to asynchronously handle paginated results. Use [ListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.ListOption) to specify the page size or the page token from which to start listing exclusions.

Example of asynchronously listing exclusions, specifying the page size:
    
    
     ApiFuture<AsyncPage<Exclusion>> future = logging.listExclusionsAsync(ListOption.pageSize(100));
     // ...
     AsyncPage<Exclusion> exclusions = future.get();
     Iterator<Exclusion> exclusionIterator = exclusions.iterateAll().iterator();
     while (exclusionIterator.hasNext()) {
       Exclusion exclusion = exclusionIterator.next();
       // do something with the exclusion
     }
     

**Parameter**  
---  
**Name** | **Description**  
`options` | `[ListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.ListOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[AsyncPage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AsyncPage.html)<[Exclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Exclusion)>>` |   
  
### listLogEntries(Logging.EntryListOption[] options)
    
    
    public abstract Page<LogEntry> listLogEntries(Logging.EntryListOption[] options)

Lists log entries. This method returns a [Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html) object that can be used to consume paginated results. Use [EntryListOption#pageSize(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.EntryListOption#com_google_cloud_logging_Logging_EntryListOption_pageSize_) to specify the page size. Use [EntryListOption#pageToken(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.EntryListOption#com_google_cloud_logging_Logging_EntryListOption_pageToken_) to specify the page token from which to start listing entries. Use [EntryListOption#sortOrder(SortingField, SortingOrder)](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.EntryListOption#com_google_cloud_logging_Logging_EntryListOption_sortOrder_) to sort log entries according to your preferred order (default is most-recent last). Use [EntryListOption#filter(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.EntryListOption#com_google_cloud_logging_Logging_EntryListOption_filter_) to filter listed log entries. By default a 24 hour filter is applied.

Example of listing log entries for a specific log.
    
    
     String filter = "logName=projects/my_project_id/logs/my_log_name";
     Page<LogEntry> entries = logging.listLogEntries(EntryListOption.filter(filter));
     Iterator<LogEntry> entryIterator = entries.iterateAll().iterator();
     while (entryIterator.hasNext()) {
       LogEntry entry = entryIterator.next();
       // do something with the entry
     }
     

**Parameter**  
---  
**Name** | **Description**  
`options` | `[EntryListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.EntryListOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html)<[LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry)>` |   
  
### listLogEntriesAsync(Logging.EntryListOption[] options)
    
    
    public abstract ApiFuture<AsyncPage<LogEntry>> listLogEntriesAsync(Logging.EntryListOption[] options)

Sends a request for listing log entries. This method returns a `ApiFuture` object to consume the result. ApiFuture#get() returns an [AsyncPage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AsyncPage.html) object that can be used to asynchronously handle paginated results. Use [EntryListOption#pageSize(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.EntryListOption#com_google_cloud_logging_Logging_EntryListOption_pageSize_) to specify the page size. Use [EntryListOption#pageToken(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.EntryListOption#com_google_cloud_logging_Logging_EntryListOption_pageToken_) to specify the page token from which to start listing entries. Use EntryListOption#sortOrder(SortingField, SortingOrder) to sort log entries according to your preferred order (default is most-recent last). Use [EntryListOption#filter(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.EntryListOption#com_google_cloud_logging_Logging_EntryListOption_filter_) to filter listed log entries. By default a 24 hour filter is applied.

Example of asynchronously listing log entries for a specific log.
    
    
     String filter = "logName=projects/my_project_id/logs/my_log_name";
     ApiFuture<AsyncPage<LogEntry>> future = logging.listLogEntriesAsync(EntryListOption.filter(filter));
     // ...
     AsyncPage<LogEntry> entries = future.get();
     Iterator<LogEntry> entryIterator = entries.iterateAll().iterator();
     while (entryIterator.hasNext()) {
       LogEntry entry = entryIterator.next();
       // do something with the entry
     }
     

**Parameter**  
---  
**Name** | **Description**  
`options` | `[EntryListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.EntryListOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[AsyncPage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AsyncPage.html)<[LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry)>>` |   
  
### listLogs(Logging.ListOption[] options)
    
    
    public default Page<String> listLogs(Logging.ListOption[] options)

Lists the log names. This method returns a [Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html) object that can be used to consume paginated results. Use [ListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.ListOption) to specify the page size or the page token from which to start listing logs.

Example of listing log names, specifying the page size.
    
    
     Page<Log> logNames = logging.listLogs(ListOption.pageSize(100));
     Iterator<Log> logIterator = logNames.iterateAll().iterator();
     while (logIterator.hasNext()) {
       String logName = logIterator.next();
       // do something with the log name
     }
     

**Parameter**  
---  
**Name** | **Description**  
`options` | `[ListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.ListOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### listLogsAsync(Logging.ListOption[] options)
    
    
    public default ApiFuture<AsyncPage<String>> listLogsAsync(Logging.ListOption[] options)

Sends a request for listing log names. This method returns a `ApiFuture` object to consume the result. ApiFuture#get() returns an [AsyncPage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AsyncPage.html) object that can be used to asynchronously handle paginated results. Use [ListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.ListOption) to specify the page size or the page token from which to start listing log names.

Example of asynchronously listing log names, specifying the page size.
    
    
     ApiFuture<AsyncPage<Log>> future = logging.listLogsAsync(ListOption.pageSize(100));
     // ...
     AsyncPage<Sink> logNames = future.get();
     Iterator<Sink> logIterator = logNames.iterateAll().iterator();
     while (logIterator.hasNext()) {
       String logName = logIterator.next();
       // do something with the log name
     }
     

**Parameter**  
---  
**Name** | **Description**  
`options` | `[ListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.ListOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[AsyncPage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AsyncPage.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>>` |   
  
### listMetrics(Logging.ListOption[] options)
    
    
    public abstract Page<Metric> listMetrics(Logging.ListOption[] options)

Lists the metrics. This method returns a [Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html) object that can be used to consume paginated results. Use [ListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.ListOption) to specify the page size or the page token from which to start listing metrics.

Example of listing metrics, specifying the page size.
    
    
     Page<Metric> metrics = logging.listMetrics(ListOption.pageSize(100));
     Iterator<Metric> metricIterator = metrics.iterateAll().iterator();
     while (metricIterator.hasNext()) {
       Metric metric = metricIterator.next();
       // do something with the metric
     }
     

**Parameter**  
---  
**Name** | **Description**  
`options` | `[ListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.ListOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html)<[Metric](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Metric)>` |   
  
### listMetricsAsync(Logging.ListOption[] options)
    
    
    public abstract ApiFuture<AsyncPage<Metric>> listMetricsAsync(Logging.ListOption[] options)

Sends a request for listing metrics. This method returns a `ApiFuture` object to consume the result. ApiFuture#get() returns an [AsyncPage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AsyncPage.html) object that can be used to asynchronously handle paginated results. Use [ListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.ListOption) to specify the page size or the page token from which to start listing metrics.

Example of asynchronously listing metrics, specifying the page size.
    
    
     ApiFuture<AsyncPage<Metric>> future = logging.listMetricsAsync(ListOption.pageSize(100));
     // ...
     AsyncPage<Metric> metrics = future.get();
     Iterator<Metric> metricIterator = metrics.iterateAll().iterator();
     while (metricIterator.hasNext()) {
       Metric metric = metricIterator.next();
       // do something with the metric
     }
     

**Parameter**  
---  
**Name** | **Description**  
`options` | `[ListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.ListOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[AsyncPage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AsyncPage.html)<[Metric](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Metric)>>` |   
  
### listMonitoredResourceDescriptors(Logging.ListOption[] options)
    
    
    public abstract Page<MonitoredResourceDescriptor> listMonitoredResourceDescriptors(Logging.ListOption[] options)

Lists the monitored resource descriptors used by Cloud Logging. This method returns a [Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html) object that can be used to consume paginated results. Use [ListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.ListOption) to specify the page size or the page token from which to start listing resource descriptors.

Example of listing monitored resource descriptors, specifying the page size.
    
    
     Page<MonitoredResourceDescriptor> descriptors = logging
         .listMonitoredResourceDescriptors(ListOption.pageSize(100));
     Iterator<MonitoredResourceDescriptor> descriptorIterator = descriptors.iterateAll().iterator();
     while (descriptorIterator.hasNext()) {
       MonitoredResourceDescriptor descriptor = descriptorIterator.next();
       // do something with the descriptor
     }
     

**Parameter**  
---  
**Name** | **Description**  
`options` | `[ListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.ListOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html)<com.google.cloud.MonitoredResourceDescriptor>` |   
  
### listMonitoredResourceDescriptorsAsync(Logging.ListOption[] options)
    
    
    public abstract ApiFuture<AsyncPage<MonitoredResourceDescriptor>> listMonitoredResourceDescriptorsAsync(Logging.ListOption[] options)

Sends a request for listing monitored resource descriptors used by Cloud Logging. This method returns a `ApiFuture` object to consume the result. ApiFuture#get() returns an [AsyncPage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AsyncPage.html) object that can be used to asynchronously handle paginated results. Use [ListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.ListOption) to specify the page size or the page token from which to start listing resource descriptors.

Example of asynchronously listing monitored resource descriptors, specifying the page size.
    
    
     ApiFuture<AsyncPage<MonitoredResourceDescriptor>> future = logging
         .listMonitoredResourceDescriptorsAsync(ListOption.pageSize(100));
     // ...
     AsyncPage<MonitoredResourceDescriptor> descriptors = future.get();
     Iterator<MonitoredResourceDescriptor> descriptorIterator = descriptors.iterateAll().iterator();
     while (descriptorIterator.hasNext()) {
       MonitoredResourceDescriptor descriptor = descriptorIterator.next();
       // do something with the descriptor
     }
     

**Parameter**  
---  
**Name** | **Description**  
`options` | `[ListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.ListOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[AsyncPage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AsyncPage.html)<com.google.cloud.MonitoredResourceDescriptor>>` |   
  
### listSinks(Logging.ListOption[] options)
    
    
    public abstract Page<Sink> listSinks(Logging.ListOption[] options)

Lists the sinks. This method returns a [Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html) object that can be used to consume paginated results. Use [ListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.ListOption) to specify the page size or the page token from which to start listing sinks.

Example of listing sinks, specifying the page size.
    
    
     Page<Sink> sinks = logging.listSinks(ListOption.pageSize(100));
     Iterator<Sink> sinkIterator = sinks.iterateAll().iterator();
     while (sinkIterator.hasNext()) {
       Sink sink = sinkIterator.next();
       // do something with the sink
     }
     

**Parameter**  
---  
**Name** | **Description**  
`options` | `[ListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.ListOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html)<[Sink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Sink)>` |   
  
### listSinksAsync(Logging.ListOption[] options)
    
    
    public abstract ApiFuture<AsyncPage<Sink>> listSinksAsync(Logging.ListOption[] options)

Sends a request for listing sinks. This method returns a `ApiFuture` object to consume the result. ApiFuture#get() returns an [AsyncPage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AsyncPage.html) object that can be used to asynchronously handle paginated results. Use [ListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.ListOption) to specify the page size or the page token from which to start listing sinks.

Example of asynchronously listing sinks, specifying the page size.
    
    
     ApiFuture<AsyncPage<Sink>> future = logging.listSinksAsync(ListOption.pageSize(100));
     // ...
     AsyncPage<Sink> sinks = future.get();
     Iterator<Sink> sinkIterator = sinks.iterateAll().iterator();
     while (sinkIterator.hasNext()) {
       Sink sink = sinkIterator.next();
       // do something with the sink
     }
     

**Parameter**  
---  
**Name** | **Description**  
`options` | `[ListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.ListOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[AsyncPage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.AsyncPage.html)<[Sink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Sink)>>` |   
  
### populateMetadata(Iterable<LogEntry> logEntries, MonitoredResource customResource, String[] exclusionClassPaths)
    
    
    public default Iterable<LogEntry> populateMetadata(Iterable<LogEntry> logEntries, MonitoredResource customResource, String[] exclusionClassPaths)

Populates metadata fields of the immutable collection of [LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry) items. Only empty fields are populated. The [SourceLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SourceLocation) is populated only for items with the severity set to [Severity#DEBUG](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Severity#com_google_cloud_logging_Severity_DEBUG). The information about [HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest), trace and span Id is retrieved using [ContextHandler](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.ContextHandler).

**Parameters**  
---  
**Name** | **Description**  
`logEntries` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry)>`  
an immutable collection of [LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry) items.  
`customResource` | `com.google.cloud.MonitoredResource`  
a customized instance of the MonitoredResource. If this parameter is `null` then the new instance will be generated using [MonitoredResourceUtil#getResource(String, String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.MonitoredResourceUtil#com_google_cloud_logging_MonitoredResourceUtil_getResource_java_lang_String_java_lang_String_).  
`exclusionClassPaths` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)[]`  
a list of exclussion class path prefixes. If left empty then [SourceLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SourceLocation) instance is built based on the caller's stack trace information. Otherwise, the information from the first StackTraceElement along the call stack which class name does not start with any not `null` exclusion class paths is used.  
**Returns**  
---  
**Type** | **Description**  
`[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry)>` | A collection of [LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry) items composed from the `logEntries` parameter with populated metadata fields.  
  
### setFlushSeverity(Severity flushSeverity)
    
    
    public abstract void setFlushSeverity(Severity flushSeverity)

Sets flush severity for asynchronous logging writes. It is disabled by default, enabled when this method is called with any [Severity](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Severity) value other than [Severity#NONE](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Severity#com_google_cloud_logging_Severity_NONE). Logs will be immediately written out for entries at or higher than flush severity.

Enabling this can cause the leaking and hanging threads, see BUG(2796) BUG(3880). However you can explicitly call [#flush](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging#com_google_cloud_logging_Logging_flush_).

TODO: Enable this by default once functionality to trigger rpc is available in generated code.

**Parameter**  
---  
**Name** | **Description**  
`flushSeverity` | `[Severity](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Severity)`  
  
  
### setWriteSynchronicity(Synchronicity synchronicity)
    
    
    public abstract void setWriteSynchronicity(Synchronicity synchronicity)

Sets synchronicity [Synchronicity](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Synchronicity) of logging writes, defaults to asynchronous.

**Parameter**  
---  
**Name** | **Description**  
`synchronicity` | `[Synchronicity](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Synchronicity)`  
  
  
### tailLogEntries(Logging.TailOption[] options)
    
    
    public abstract LogEntryServerStream tailLogEntries(Logging.TailOption[] options)

**Beta**

_The surface for the tail streaming is not stable yet and may change in the future._

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Sends a request to stream fresh log entries. The method returns a `LogEntryServerStream` object to iterate through the returned stream of the log entries. Use EntryListOption#bufferWindow(String)} to specify amount of time to buffer log entries at the server before being returned. entries. Use [TailOption#filter(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.TailOption#com_google_cloud_logging_Logging_TailOption_filter_) to filter tailed log entries.

Example of streaming log entries for a specific project.
    
    
     LogEntryServerStream stream = logging.tailLogEntries(TailOption.project("my_project_id"));
     Iterator<LogEntry> it = stream.iterator();
     while (it.hasNext()) {
       // do something with entry
       // call stream.cancel(); to stop streaming
     }
     

**Parameter**  
---  
**Name** | **Description**  
`options` | `[TailOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.TailOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[LogEntryServerStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntryServerStream)` |   
  
### update(Exclusion exclusion)
    
    
    public abstract Exclusion update(Exclusion exclusion)

Updates one or more properties of an existing exclusion.

Example of updating the exclusion:
    
    
     String exclusionName = "my_exclusion_name";
     Exclusion exclusion = Exclusion
         .newBuilder(exclusionName, "resource.type=gcs_bucket severity

**Parameter**  
---  
**Name** | **Description**  
`exclusion` | `[Exclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Exclusion)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Exclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Exclusion)` | the updated exclusion  
  
### update(MetricInfo metric)
    
    
    public abstract Metric update(MetricInfo metric)

Updates a metric or creates one if it does not exist.

Example of updating a metric.
    
    
     String metricName = "my_metric_name";
     MetricInfo metricInfo = MetricInfo.newBuilder(metricName, "severity>=ERROR").setDescription("new description")
         .build();
     Metric metric = logging.update(metricInfo);
     

**Parameter**  
---  
**Name** | **Description**  
`metric` | `[MetricInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.MetricInfo)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Metric](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Metric)` | the created metric  
  
### update(SinkInfo sink)
    
    
    public abstract Sink update(SinkInfo sink)

Updates a sink or creates one if it does not exist.

Example of updating a sink.
    
    
     String sinkName = "my_sink_name";
     String datasetName = "my_dataset";
     SinkInfo sinkInfo = SinkInfo.newBuilder(sinkName, DatasetDestination.of(datasetName))
         .setVersionFormat(SinkInfo.VersionFormat.V2).setFilter("severity>=ERROR").build();
     Sink sink = logging.update(sinkInfo);
     

**Parameter**  
---  
**Name** | **Description**  
`sink` | `[SinkInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Sink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Sink)` | the created sink  
  
### updateAsync(Exclusion exclusion)
    
    
    public abstract ApiFuture<Exclusion> updateAsync(Exclusion exclusion)

Sends a request to change one or more properties of an existing exclusion. This method returns an `ApiFuture` object to consume the result. ApiFuture#get() returns the updated exclusion or `null` if not found.

Example of asynchronous exclusion update:
    
    
     String exclusionName = "my_exclusion_name";
     Exclusion exclusion = Exclusion
         .newBuilder(exclusionName, "resource.type=gcs_bucket severity

**Parameter**  
---  
**Name** | **Description**  
`exclusion` | `[Exclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Exclusion)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Exclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Exclusion)>` |   
  
### updateAsync(MetricInfo metric)
    
    
    public abstract ApiFuture<Metric> updateAsync(MetricInfo metric)

Sends a request for updating a metric (or creating it, if it does not exist). This method returns a `ApiFuture` object to consume the result. ApiFuture#get() returns the updated/created metric or `null` if not found.

Example of asynchronously updating a metric.
    
    
     String metricName = "my_metric_name";
     MetricInfo metricInfo = MetricInfo.newBuilder(metricName, "severity>=ERROR").setDescription("new description")
         .build();
     ApiFuture<Metric> future = logging.updateAsync(metricInfo);
     // ...
     Metric metric = future.get();
     

**Parameter**  
---  
**Name** | **Description**  
`metric` | `[MetricInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.MetricInfo)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Metric](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Metric)>` |   
  
### updateAsync(SinkInfo sink)
    
    
    public abstract ApiFuture<Sink> updateAsync(SinkInfo sink)

Sends a request for updating a sink (or creating it, if it does not exist). This method returns a `ApiFuture` object to consume the result. ApiFuture#get() returns the updated/created sink or `null` if not found.

Example of asynchronously updating a sink.
    
    
     String sinkName = "my_sink_name";
     String datasetName = "my_dataset";
     SinkInfo sinkInfo = SinkInfo.newBuilder(sinkName, DatasetDestination.of(datasetName))
         .setVersionFormat(SinkInfo.VersionFormat.V2).setFilter("severity>=ERROR").build();
     ApiFuture<Sink> future = logging.updateAsync(sinkInfo);
     // ...
     Sink sink = future.get();
     

**Parameter**  
---  
**Name** | **Description**  
`sink` | `[SinkInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Sink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Sink)>` |   
  
### write(Iterable<LogEntry> logEntries, Logging.WriteOption[] options)
    
    
    public abstract void write(Iterable<LogEntry> logEntries, Logging.WriteOption[] options)

Sends a request to log entries to Cloud Logging. Use [WriteOption#logName(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.WriteOption#com_google_cloud_logging_Logging_WriteOption_logName_) to provide a log name for those entries that do not specify one. Use [WriteOption#resource(MonitoredResource)](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.WriteOption#com_google_cloud_logging_Logging_WriteOption_resource_) to provide a monitored resource for those entries that do not specify one. Use [WriteOption#labels(Map)](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.WriteOption#com_google_cloud_logging_Logging_WriteOption_labels_) to provide some labels to be added to every entry in `logEntries`.

Example of writing log entries and providing a default log name and monitored resource.
    
    
     String logName = "my_log_name";
     List<LogEntry> entries = new ArrayList<>();
     entries.add(LogEntry.of(StringPayload.of("Entry payload")));
     Map<String, Object> jsonMap = new HashMap<>();
     jsonMap.put("key", "value");
     entries.add(LogEntry.of(JsonPayload.of(jsonMap)));
     logging.write(entries, WriteOption.logName(logName),
         WriteOption.resource(MonitoredResource.newBuilder("global").build()));
     

**Parameters**  
---  
**Name** | **Description**  
`logEntries` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry)>`  
  
`options` | `[WriteOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.WriteOption)[]`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
