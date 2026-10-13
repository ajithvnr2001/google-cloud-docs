---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.spi.v2.LoggingRpc
title: Interface LoggingRpc (3.40.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:21:07.878509+00:00
---

# Interface LoggingRpc (3.40.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.spi.v2.LoggingRpc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface LoggingRpc (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.36.0  3.35.0  3.34.0  3.32.0  3.29.0  3.28.0  3.26.0  3.24.0  3.23.10  3.22.6  3.21.4  3.20.7  3.19.0  3.18.0  3.17.2  3.16.2  3.15.17  3.14.9  3.13.7  3.12.1  3.11.10  3.10.7  3.9.0  3.8.0  3.7.6  3.6.4  3.5.3 
    
    
    public interface LoggingRpc extends AutoCloseable, ServiceRpc

## Implements

[AutoCloseable](https://docs.oracle.com/javase/8/docs/api/java/lang/AutoCloseable.html), com.google.cloud.ServiceRpc

## Methods 

### create(CreateExclusionRequest request)
    
    
    public abstract ApiFuture<LogExclusion> create(CreateExclusionRequest request)

Sends a request to create a new exclusion in a specified parent resource. This method returns an `ApiFuture` object to consume the result. ApiFuture#get() returns the created exclusion.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateExclusionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CreateExclusionRequest)`  
the request object containing all of the parameters for the API call  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[LogExclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogExclusion)>` |   
  
### create(CreateLogMetricRequest request)
    
    
    public abstract ApiFuture<LogMetric> create(CreateLogMetricRequest request)

Sends a request to create a log metric. This method returns a `ApiFuture` object to consume the result. ApiFuture#get() returns the created metric.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateLogMetricRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CreateLogMetricRequest)`  
the request object containing all of the parameters for the API call  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[LogMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogMetric)>` |   
  
### create(CreateSinkRequest request)
    
    
    public abstract ApiFuture<LogSink> create(CreateSinkRequest request)

Sends a request to create a sink. This method returns a `ApiFuture` object to consume the result. ApiFuture#get() returns the created sink.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateSinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CreateSinkRequest)`  
the request object containing all of the parameters for the API call  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[LogSink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSink)>` |   
  
### delete(DeleteExclusionRequest request)
    
    
    public abstract ApiFuture<Empty> delete(DeleteExclusionRequest request)

Sends a request to delete an exclusion. This method returns an `ApiFuture` object to consume the result. ApiFuture#get() returns [Empty#getDefaultInstance()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html#com_google_protobuf_Empty_getDefaultInstance_) or `null` if the log exclusion was not found.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteExclusionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.DeleteExclusionRequest)`  
the request object containing all of the parameters for the API call  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### delete(DeleteLogMetricRequest request)
    
    
    public abstract ApiFuture<Empty> delete(DeleteLogMetricRequest request)

Sends a request to delete a log metric. This method returns a `ApiFuture` object to consume the result. ApiFuture#get() returns [Empty#getDefaultInstance()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html#com_google_protobuf_Empty_getDefaultInstance_) or `null` if the log was not found.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteLogMetricRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.DeleteLogMetricRequest)`  
the request object containing all of the parameters for the API call  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### delete(DeleteLogRequest request)
    
    
    public abstract ApiFuture<Empty> delete(DeleteLogRequest request)

Sends a request to deletes a log. This method returns a `ApiFuture` object to consume the result. ApiFuture#get() returns [Empty#getDefaultInstance()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html#com_google_protobuf_Empty_getDefaultInstance_) or `null` if the log was not found. The deleted log will reappear if it receives new log entries.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteLogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.DeleteLogRequest)`  
the request object containing all of the parameters for the API call  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### delete(DeleteSinkRequest request)
    
    
    public abstract ApiFuture<Empty> delete(DeleteSinkRequest request)

Sends a request to delete a sink. This method returns a `ApiFuture` object to consume the result. ApiFuture#get() returns [Empty#getDefaultInstance()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html#com_google_protobuf_Empty_getDefaultInstance_) or `null` if the sink was not found.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteSinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.DeleteSinkRequest)`  
the request object containing all of the parameters for the API call  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### get(GetExclusionRequest request)
    
    
    public abstract ApiFuture<LogExclusion> get(GetExclusionRequest request)

Sends a request to get the description of an exclusion. This method returns an ` ApiFuture` object to consume the result. ApiFuture#get() returns the requested exclusion or `null` if not found.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetExclusionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.GetExclusionRequest)`  
the request object containing all of the parameters for the API call  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[LogExclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogExclusion)>` |   
  
### get(GetLogMetricRequest request)
    
    
    public abstract ApiFuture<LogMetric> get(GetLogMetricRequest request)

Sends a request to get a log metric. This method returns a `ApiFuture` object to consume the result. ApiFuture#get() returns the requested log metric or `null` if not found.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetLogMetricRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.GetLogMetricRequest)`  
the request object containing all of the parameters for the API call  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[LogMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogMetric)>` |   
  
### get(GetSinkRequest request)
    
    
    public abstract ApiFuture<LogSink> get(GetSinkRequest request)

Sends a request to get a sink. This method returns a `ApiFuture` object to consume the result. ApiFuture#get() returns the requested sink or `null` if not found.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.GetSinkRequest)`  
the request object containing all of the parameters for the API call  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[LogSink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSink)>` |   
  
### getTailLogEntriesStream()
    
    
    public default BidiStream<TailLogEntriesRequest,TailLogEntriesResponse> getTailLogEntriesStream()

This method returns a {code BidiStream} object to consume the stream of log entries.

**Returns**  
---  
**Type** | **Description**  
`[BidiStream](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BidiStream.html)<[TailLogEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.TailLogEntriesRequest),[TailLogEntriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.TailLogEntriesResponse)>` |   
  
### list(ListExclusionsRequest request)
    
    
    public abstract ApiFuture<ListExclusionsResponse> list(ListExclusionsRequest request)

Sends a request to list all the exclusions in parent resource. Use this method to retrieve exclusions from Cloud Logging. This method returns an `ApiFuture` object to consume the result. ApiFuture#get() returns a response object containing the listing result.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListExclusionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListExclusionsRequest)`  
the request object containing all of the parameters for the API call  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[ListExclusionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListExclusionsResponse)>` |   
  
### list(ListLogEntriesRequest request)
    
    
    public abstract ApiFuture<ListLogEntriesResponse> list(ListLogEntriesRequest request)

Sends a request to list log entries. Use this method to retrieve log entries from Cloud Logging. This method returns a `ApiFuture` object to consume the result. ApiFuture#get() returns a response object containing the listing result.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListLogEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListLogEntriesRequest)`  
the request object containing all of the parameters for the API call  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[ListLogEntriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListLogEntriesResponse)>` |   
  
### list(ListLogMetricsRequest request)
    
    
    public abstract ApiFuture<ListLogMetricsResponse> list(ListLogMetricsRequest request)

Sends a request to list the log metrics in a project. This method returns a `ApiFuture` object to consume the result. ApiFuture#get() returns a response object containing the listing result.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListLogMetricsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListLogMetricsRequest)`  
the request object containing all of the parameters for the API call  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[ListLogMetricsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListLogMetricsResponse)>` |   
  
### list(ListMonitoredResourceDescriptorsRequest request)
    
    
    public abstract ApiFuture<ListMonitoredResourceDescriptorsResponse> list(ListMonitoredResourceDescriptorsRequest request)

Sends a request to list monitored resource descriptors. This method returns a `ApiFuture` object to consume the result. ApiFuture#get() returns a response object containing the listing result.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMonitoredResourceDescriptorsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListMonitoredResourceDescriptorsRequest)`  
the request object containing all of the parameters for the API call  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[ListMonitoredResourceDescriptorsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListMonitoredResourceDescriptorsResponse)>` |   
  
### list(ListSinksRequest request)
    
    
    public abstract ApiFuture<ListSinksResponse> list(ListSinksRequest request)

Sends a request to list the sinks in a project. This method returns a `ApiFuture` object to consume the result. ApiFuture#get() returns a response object containing the listing result.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSinksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListSinksRequest)`  
the request object containing all of the parameters for the API call  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[ListSinksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListSinksResponse)>` |   
  
### listLogs(ListLogsRequest request)
    
    
    public default ApiFuture<ListLogsResponse> listLogs(ListLogsRequest request)

Sends a request to list the log names in a project. This method returns a `ApiFuture` object to consume the result. ApiFuture#get() returns a response object containing the listing result.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListLogsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListLogsRequest)`  
the request object containing all of the parameters for the API call  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[ListLogsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListLogsResponse)>` |   
  
### update(UpdateExclusionRequest request)
    
    
    public abstract ApiFuture<LogExclusion> update(UpdateExclusionRequest request)

Sends a request to change one or more properties of an existing exclusion. This method returns an `ApiFuture` object to consume the result. ApiFuture#get() returns the updated exclusion.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateExclusionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.UpdateExclusionRequest)`  
the request object containing all of the parameters for the API call  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[LogExclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogExclusion)>` |   
  
### update(UpdateLogMetricRequest request)
    
    
    public abstract ApiFuture<LogMetric> update(UpdateLogMetricRequest request)

Sends a request to update a log metric. If the log metric does not exist, it is created. This method returns a `ApiFuture` object to consume the result. ApiFuture#get() returns the updated or created log metric.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateLogMetricRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.UpdateLogMetricRequest)`  
the request object containing all of the parameters for the API call  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[LogMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogMetric)>` |   
  
### update(UpdateSinkRequest request)
    
    
    public abstract ApiFuture<LogSink> update(UpdateSinkRequest request)

Sends a request to update a sink. If the sink does not exist, it is created. This method returns a `ApiFuture` object to consume the result. ApiFuture#get() returns the updated or created sink.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.UpdateSinkRequest)`  
the request object containing all of the parameters for the API call  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[LogSink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSink)>` |   
  
### write(WriteLogEntriesRequest request)
    
    
    public abstract ApiFuture<WriteLogEntriesResponse> write(WriteLogEntriesRequest request)

Sends a request to write log entries to Cloud Logging. This method returns a `ApiFuture` object to consume the result. ApiFuture#get() returns a response object for the write operation.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[WriteLogEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.WriteLogEntriesRequest)`  
the request object containing all of the parameters for the API call  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[WriteLogEntriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.WriteLogEntriesResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
