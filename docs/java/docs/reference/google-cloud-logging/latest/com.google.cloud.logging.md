---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging
title: Package com.google.cloud.logging (3.40.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:20:56.353226+00:00
---

# Package com.google.cloud.logging (3.40.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Package com.google.cloud.logging (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.36.0  3.35.0  3.34.0  3.32.0  3.29.0  3.28.0  3.26.0  3.24.0  3.23.10  3.22.6  3.21.4  3.20.7  3.19.0  3.18.0  3.17.2  3.16.2  3.15.17  3.14.9  3.13.7  3.12.1  3.11.10  3.10.7  3.9.0  3.8.0  3.7.6  3.6.4  3.5.3 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-logging/google-cloud-logging/src/main/java/com/google/cloud/logging)  
---  
  
## Classes

Class |  Description  
---|---  
[com.google.cloud.logging.Context](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Context) |  Class to hold context attributes including information about {@see HttpRequest} and tracing.  
[com.google.cloud.logging.Context.Builder](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Context.Builder) |  A builder for {@see Context} objects.  
[com.google.cloud.logging.ContextHandler](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.ContextHandler) |  Class provides a per-thread storage of the {@see Context} instances.  
[com.google.cloud.logging.Exclusion](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Exclusion) |  Specifies a set of log entries that are not to be stored in Logging. If your GCP resource receives a large volume of logs, you can use exclusions to reduce your chargeable logs. Exclusions are processed after log sinks, so you can export log entries before they are excluded. Note that organization-level and folder-level exclusions don't apply to child resources, and that  
[com.google.cloud.logging.Exclusion.Builder](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Exclusion.Builder) |  A builder for `Exclusion` objects.  
[com.google.cloud.logging.HttpRequest](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest) |  Objects of this class represent information about the (optional) HTTP request associated with a log entry. See Also: [ Http Request](https://cloud.google.com/logging/docs/api/ref_v2beta1/rest/v2beta1/LogEntry#httprequest)  
[com.google.cloud.logging.HttpRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest.Builder) |  A builder for `HttpRequest` objects.  
[com.google.cloud.logging.HttpRequest.RequestMethod](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest.RequestMethod) |  The HTTP request method.  
[com.google.cloud.logging.Instrumentation](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Instrumentation) |   
[com.google.cloud.logging.LogDestinationName](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogDestinationName) |  Class for specifying resource name of the log to which this log entry belongs (see 'logName' parameter in <https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry>)  
[com.google.cloud.logging.LogEntry](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry) |  A Cloud Logging log entry. All log entries are represented via objects of this class. Log entries can have different type of payloads: an UTF-8 string (see Payload.StringPayload), a JSON object (see Payload.JsonPayload, or a protobuf object (see Payload.ProtoPayload). Entries can also store additional information about the operation or the HTTP request that  
[com.google.cloud.logging.LogEntry.Builder](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry.Builder) |  A builder for `LogEntry` objects.  
[com.google.cloud.logging.LogEntryIterator](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntryIterator) |  The class implements {@see Iterator} interface over {@see LogEntry} by iterating through {@see TailLogEntriesResponse} streamed by `BidiStream`. This class is instantiated by {@see LogEntryServerStream} and is not intended to be used explicitly.  
[com.google.cloud.logging.LogEntryServerStream](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntryServerStream) |  The class implements Iterable interface over {@see LogEntry}. It wraps around BidiStream bi-directional gRPC stream to support iterating through ingested responses. The class uses {@see LogEntryIterator} to iterate through the processed responses. The stream should be explicitly canceled by calling {@see LogEntryServerStream#cancel()} method. The class does not provide recovery or resuming functionality over the stream.  
[com.google.cloud.logging.Logging.EntryListOption](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.EntryListOption) |  Class for specifying options for listing log entries.  
[com.google.cloud.logging.Logging.ListOption](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.ListOption) |  Class for specifying options for listing sinks, monitored resources and monitored resource descriptors.  
[com.google.cloud.logging.Logging.TailOption](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.TailOption) |  Class for specifying options for tailing log entries.  
[com.google.cloud.logging.Logging.WriteOption](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.WriteOption) |  Class for specifying options for writing log entries.  
[com.google.cloud.logging.LoggingHandler](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingHandler) |  A logging handler that outputs logs generated with [java.util.logging.Logger](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html) to Cloud Logging. Java logging levels (see [java.util.logging.Level](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Level.html)) are mapped to the following Google  
[com.google.cloud.logging.LoggingLevel](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingLevel) |  This class adds some additional Java logging levels for Cloud Logging. Added levels fill in the gap between Java logging levels and Cloud Logging severities. Added levels in descending order are (between parenthesis the relation with Java logging  
[com.google.cloud.logging.LoggingOptions](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions) |   
[com.google.cloud.logging.LoggingOptions.Builder](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions.Builder) |   
[com.google.cloud.logging.LoggingOptions.DefaultLoggingFactory](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions.DefaultLoggingFactory) |   
[com.google.cloud.logging.LoggingOptions.DefaultLoggingRpcFactory](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions.DefaultLoggingRpcFactory) |   
[com.google.cloud.logging.MetadataLoader](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.MetadataLoader) |   
[com.google.cloud.logging.Metric](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Metric) |  Cloud Logging metrics describe logs-based metric. The value of the metric is the number of log entries that match a logs filter (see #getFilter()). `Metric` adds a layer of service-related functionality over MetricInfo. Objects  
[com.google.cloud.logging.Metric.Builder](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Metric.Builder) |  A builder for `Metric` objects.  
[com.google.cloud.logging.MetricInfo](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.MetricInfo) |  Cloud Logging metrics describe logs-based metric. The value of the metric is the number of log entries that match a logs filter (see #getFilter()). See Also: [Logs-based Metrics ](https://cloud.google.com/logging/docs/view/logs_based_metrics)  
[com.google.cloud.logging.MetricInfo.Builder](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.MetricInfo.Builder) |  A builder for `MetricInfo` objects.  
[com.google.cloud.logging.MonitoredResourceUtil](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.MonitoredResourceUtil) |  Monitored resource construction utilities to detect resource type and add labels. Used by logging framework adapters to configure default resource. See usage in LoggingHandler.  
[com.google.cloud.logging.Operation](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Operation) |  Additional information about a potentially long-running operation with which a log entry is associated. See Also: [ Log Entry Operation](https://cloud.google.com/logging/docs/api/ref_v2beta1/rest/v2beta1/LogEntry#LogEntryOperation)  
[com.google.cloud.logging.Operation.Builder](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Operation.Builder) |  A builder for `Operation` objects.  
[com.google.cloud.logging.Payload](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Payload) |  A base class for log entry payloads. See Also: [Log Entries and Logs](https://cloud.google.com/logging/docs/view/logs_index)  
[com.google.cloud.logging.Payload.JsonPayload](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Payload.JsonPayload) |  A log entry's JSON payload.  
[com.google.cloud.logging.Payload.ProtoPayload](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Payload.ProtoPayload) |  A log entry payload as a protobuf object.  
[com.google.cloud.logging.Payload.StringPayload](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Payload.StringPayload) |  A log entry payload as an UTF-8 string.  
[com.google.cloud.logging.Sink](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Sink) |  Cloud Logging sinks can be used to control the export of your logs. Each sink specifies the export of a set of log entries to a certain destination. A sink consists of a name, unique to the project, a filter for choosing the log entries to export and a destination for the log entries.   
[com.google.cloud.logging.Sink.Builder](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Sink.Builder) |  A builder for `Sink` objects.  
[com.google.cloud.logging.SinkInfo](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo) |  Cloud Logging sinks can be used to control the export of your logs. Each sink specifies the export of a set of log entries to a certain destination. A sink consists of a name, unique to the project, a filter for choosing the log entries to export and a destination for the log entries.   
[com.google.cloud.logging.SinkInfo.Builder](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo.Builder) |  A builder for `SinkInfo` objects.  
[com.google.cloud.logging.SinkInfo.Destination](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo.Destination) |   
[com.google.cloud.logging.SinkInfo.Destination.BucketDestination](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo.Destination.BucketDestination) |  Class for specifying a Google Cloud Storage bucket as destination for the sink.  
[com.google.cloud.logging.SinkInfo.Destination.DatasetDestination](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo.Destination.DatasetDestination) |  Class for specifying a Google Cloud BigQuery dataset as destination for the sink.  
[com.google.cloud.logging.SinkInfo.Destination.LoggingBucketDestination](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo.Destination.LoggingBucketDestination) |   
[com.google.cloud.logging.SinkInfo.Destination.TopicDestination](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo.Destination.TopicDestination) |  Class for specifying a Google Cloud BigQuery dataset as destination for the sink.  
[com.google.cloud.logging.SourceLocation](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SourceLocation) |  Additional information about the source code location that produced the log entry.  
[com.google.cloud.logging.SourceLocation.Builder](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SourceLocation.Builder) |  A builder for `SourceLocation` objects.  
[com.google.cloud.logging.TimestampDefaultFilter](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.TimestampDefaultFilter) |   
[com.google.cloud.logging.TraceLoggingEnhancer](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.TraceLoggingEnhancer) |   
  
## Interfaces

Interface |  Description  
---|---  
[com.google.cloud.logging.ITimestampDefaultFilter](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.ITimestampDefaultFilter) |  Encapsulates implementation of default time filter. This is needed for testing since we can't mock static classes with EasyMock  
[com.google.cloud.logging.Logging](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging) |   
[com.google.cloud.logging.LoggingEnhancer](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingEnhancer) |  An enhancer for log entries. Used to add custom labels to the LogEntry.Builder  
[com.google.cloud.logging.LoggingFactory](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingFactory) |  An interface for Logging factories.  
[com.google.cloud.logging.ResourceTypeEnvironmentGetter](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.ResourceTypeEnvironmentGetter) |   
  
## Enums

Enum |  Description  
---|---  
[com.google.cloud.logging.ContextHandler.ContextPriority](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.ContextHandler.ContextPriority) |   
[com.google.cloud.logging.LogDestinationName.DestinationType](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogDestinationName.DestinationType) |   
[com.google.cloud.logging.Logging.SortingField](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.SortingField) |  Fields according to which log entries can be sorted.  
[com.google.cloud.logging.Logging.SortingOrder](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.SortingOrder) |  Sorting orders available when listing log entries.  
[com.google.cloud.logging.LoggingHandler.LogTarget](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingHandler.LogTarget) |  Where to send logs.  
[com.google.cloud.logging.MonitoredResourceUtil.Label](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.MonitoredResourceUtil.Label) |   
[com.google.cloud.logging.Payload.Type](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Payload.Type) |  Type for a log entry payload.  
[com.google.cloud.logging.Severity](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Severity) |  The severity of the event described in a log entry. These guideline severity levels are ordered, with numerically smaller levels treated as less severe than numerically larger levels. If the source of the log entries uses a different set of severity levels, the client should select the closest corresponding `Severity` value.  
[com.google.cloud.logging.SinkInfo.Destination.Type](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo.Destination.Type) |  Type of destination for Cloud Logging sink.  
[com.google.cloud.logging.SinkInfo.VersionFormat](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo.VersionFormat) |  Available log entry formats. Log entries can be written to Cloud Logging in either format and can be exported in either format. Version 2 is the preferred format.  
[com.google.cloud.logging.Synchronicity](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Synchronicity) |  Used to specify the behavior of write calls to the Cloud Logging service. Specifying SYNC will make synchronous calls; specifying ASYNC will make asynchronous calls. The default behavior is ASYNC.  
  
## Exceptions

Exception |  Description  
---|---  
[com.google.cloud.logging.LoggingException](https://cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingException) |  Logging service exception.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
