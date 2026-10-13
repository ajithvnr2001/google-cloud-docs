---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.LoggingClient
title: Class LoggingClient (3.40.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:21:09.105883+00:00
---

# Class LoggingClient (3.40.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.LoggingClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class LoggingClient (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.36.0  3.35.0  3.34.0  3.32.0  3.29.0  3.28.0  3.26.0  3.24.0  3.23.10  3.22.6  3.21.4  3.20.7  3.19.0  3.18.0  3.17.2  3.16.2  3.15.17  3.14.9  3.13.7  3.12.1  3.11.10  3.10.7  3.9.0  3.8.0  3.7.6  3.6.4  3.5.3 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-logging/google-cloud-logging/src/main/java/com/google/cloud/logging/v2/LoggingClient.java)| [Product Reference](https://cloud.google.com/logging/docs)  
---|---  
  
Service Description: Service for ingesting and querying logs.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LoggingClient loggingClient = LoggingClient.create()) {
       LogName logName = LogName.ofProjectLogName("[PROJECT]", "[LOG]");
       loggingClient.deleteLog(logName);
     }
     

Note: close() needs to be called on the LoggingClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
DeleteLog |  Deletes all the log entries in a log for the _Default Log Bucket. The log reappears if it receives new entries. Log entries written shortly before the delete operation might not be deleted. Entries received after the delete operation with a timestamp before the operation will be deleted. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteLog(DeleteLogRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteLog(LogName logName) 
  * deleteLog(String logName) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteLogCallable() 

  
WriteLogEntries |  Writes log entries to Logging. This API method is the only way to send log entries to Logging. This method is used, directly or indirectly, by the Logging agent (fluentd) and all logging libraries configured to use Logging. A single request may contain log entries for a maximum of 1000 different resources (projects, organizations, billing accounts or folders) |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * writeLogEntries(WriteLogEntriesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * writeLogEntries(LogName logName, MonitoredResource resource, Map<String, String> labels, List<LogEntry> entries) 
  * writeLogEntries(String logName, MonitoredResource resource, Map<String, String> labels, List<LogEntry> entries) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * writeLogEntriesCallable() 

  
ListLogEntries |  Lists log entries. Use this method to retrieve log entries that originated from a project/folder/organization/billing account. For ways to export log entries, see [Exporting Logs](https://cloud.google.com/logging/docs/export). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLogEntries(ListLogEntriesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listLogEntries(List<String> resourceNames, String filter, String orderBy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLogEntriesPagedCallable() 
  * listLogEntriesCallable() 

  
ListMonitoredResourceDescriptors |  Lists the descriptors for monitored resource types used by Logging. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listMonitoredResourceDescriptors(ListMonitoredResourceDescriptorsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listMonitoredResourceDescriptorsPagedCallable() 
  * listMonitoredResourceDescriptorsCallable() 

  
ListLogs |  Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLogs(ListLogsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listLogs(BillingAccountName parent) 
  * listLogs(FolderName parent) 
  * listLogs(OrganizationName parent) 
  * listLogs(ProjectName parent) 
  * listLogs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLogsPagedCallable() 
  * listLogsCallable() 

  
TailLogEntries |  Streaming read of log entries as they are ingested. Until the stream is terminated, it will continue reading logs. |  Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * tailLogEntriesCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of LoggingSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     LoggingSettings loggingSettings =
         LoggingSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     LoggingClient loggingClient = LoggingClient.create(loggingSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     LoggingSettings loggingSettings = LoggingSettings.newBuilder().setEndpoint(myEndpoint).build();
     LoggingClient loggingClient = LoggingClient.create(loggingSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > LoggingClient

## Static Methods 

### create()
    
    
    public static final LoggingClient create()

Constructs an instance of LoggingClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[LoggingClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.LoggingClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(LoggingSettings settings)
    
    
    public static final LoggingClient create(LoggingSettings settings)

Constructs an instance of LoggingClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[LoggingSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.LoggingSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LoggingClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.LoggingClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(LoggingServiceV2Stub stub)
    
    
    public static final LoggingClient create(LoggingServiceV2Stub stub)

Constructs an instance of LoggingClient, using the given stub for making calls. This is for advanced usage - prefer using create(LoggingSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[LoggingServiceV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.stub.LoggingServiceV2Stub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LoggingClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.LoggingClient)` |   
  
## Constructors 

### LoggingClient(LoggingSettings settings)
    
    
    protected LoggingClient(LoggingSettings settings)

Constructs an instance of LoggingClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[LoggingSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.LoggingSettings)`  
  
  
### LoggingClient(LoggingServiceV2Stub stub)
    
    
    protected LoggingClient(LoggingServiceV2Stub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[LoggingServiceV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.stub.LoggingServiceV2Stub)`  
  
  
## Methods 

### awaitTermination(long duration, TimeUnit unit)
    
    
    public boolean awaitTermination(long duration, TimeUnit unit)

**Parameters**  
---  
**Name** | **Description**  
`duration` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`unit` | `[TimeUnit](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/TimeUnit.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InterruptedException](https://docs.oracle.com/javase/8/docs/api/java/lang/InterruptedException.html)` |   
  
### close()
    
    
    public final void close()

### deleteLog(@Nullable LogName logName)
    
    
    public final void deleteLog(@Nullable LogName logName)

Deletes all the log entries in a log for the _Default Log Bucket. The log reappears if it receives new entries. Log entries written shortly before the delete operation might not be deleted. Entries received after the delete operation with a timestamp before the operation will be deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LoggingClient loggingClient = LoggingClient.create()) {
       LogName logName = LogName.ofProjectLogName("[PROJECT]", "[LOG]");
       loggingClient.deleteLog(logName);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`logName` | `@org.jspecify.annotations.Nullable com.google.logging.v2.LogName`  
Required. The resource name of the log to delete: 

  * `projects/[PROJECT_ID]/logs/[LOG_ID]`
  * `organizations/[ORGANIZATION_ID]/logs/[LOG_ID]`
  * `billingAccounts/[BILLING_ACCOUNT_ID]/logs/[LOG_ID]`
  * `folders/[FOLDER_ID]/logs/[LOG_ID]`

`[LOG_ID]` must be URL-encoded. For example, `"projects/my-project-id/logs/syslog"`, `"organizations/123/logs/cloudaudit.googleapis.com%2Factivity"`. For more information about log names, see LogEntry.  
  
### deleteLog(DeleteLogRequest request)
    
    
    public final void deleteLog(DeleteLogRequest request)

Deletes all the log entries in a log for the _Default Log Bucket. The log reappears if it receives new entries. Log entries written shortly before the delete operation might not be deleted. Entries received after the delete operation with a timestamp before the operation will be deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LoggingClient loggingClient = LoggingClient.create()) {
       DeleteLogRequest request =
           DeleteLogRequest.newBuilder()
               .setLogName(LogName.ofProjectLogName("[PROJECT]", "[LOG]").toString())
               .build();
       loggingClient.deleteLog(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteLogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.DeleteLogRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteLog(String logName)
    
    
    public final void deleteLog(String logName)

Deletes all the log entries in a log for the _Default Log Bucket. The log reappears if it receives new entries. Log entries written shortly before the delete operation might not be deleted. Entries received after the delete operation with a timestamp before the operation will be deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LoggingClient loggingClient = LoggingClient.create()) {
       String logName = LogName.ofProjectLogName("[PROJECT]", "[LOG]").toString();
       loggingClient.deleteLog(logName);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`logName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the log to delete: 

  * `projects/[PROJECT_ID]/logs/[LOG_ID]`
  * `organizations/[ORGANIZATION_ID]/logs/[LOG_ID]`
  * `billingAccounts/[BILLING_ACCOUNT_ID]/logs/[LOG_ID]`
  * `folders/[FOLDER_ID]/logs/[LOG_ID]`

`[LOG_ID]` must be URL-encoded. For example, `"projects/my-project-id/logs/syslog"`, `"organizations/123/logs/cloudaudit.googleapis.com%2Factivity"`. For more information about log names, see LogEntry.  
  
### deleteLogCallable()
    
    
    public final UnaryCallable<DeleteLogRequest,Empty> deleteLogCallable()

Deletes all the log entries in a log for the _Default Log Bucket. The log reappears if it receives new entries. Log entries written shortly before the delete operation might not be deleted. Entries received after the delete operation with a timestamp before the operation will be deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LoggingClient loggingClient = LoggingClient.create()) {
       DeleteLogRequest request =
           DeleteLogRequest.newBuilder()
               .setLogName(LogName.ofProjectLogName("[PROJECT]", "[LOG]").toString())
               .build();
       ApiFuture<Empty> future = loggingClient.deleteLogCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteLogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.DeleteLogRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getSettings()
    
    
    public final @Nullable LoggingSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.logging.v2.LoggingSettings` |   
  
### getStub()
    
    
    public LoggingServiceV2Stub getStub()

**Returns**  
---  
**Type** | **Description**  
`[LoggingServiceV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.stub.LoggingServiceV2Stub)` |   
  
### isShutdown()
    
    
    public boolean isShutdown()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isTerminated()
    
    
    public boolean isTerminated()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### listLogEntries(ListLogEntriesRequest request)
    
    
    public final LoggingClient.ListLogEntriesPagedResponse listLogEntries(ListLogEntriesRequest request)

Lists log entries. Use this method to retrieve log entries that originated from a project/folder/organization/billing account. For ways to export log entries, see [Exporting Logs](https://cloud.google.com/logging/docs/export).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LoggingClient loggingClient = LoggingClient.create()) {
       ListLogEntriesRequest request =
           ListLogEntriesRequest.newBuilder()
               .addAllResourceNames(new ArrayList<String>())
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (LogEntry element : loggingClient.listLogEntries(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListLogEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListLogEntriesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LoggingClient.ListLogEntriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.LoggingClient.ListLogEntriesPagedResponse)` |   
  
### listLogEntries(List<String> resourceNames, String filter, String orderBy)
    
    
    public final LoggingClient.ListLogEntriesPagedResponse listLogEntries(List<String> resourceNames, String filter, String orderBy)

Lists log entries. Use this method to retrieve log entries that originated from a project/folder/organization/billing account. For ways to export log entries, see [Exporting Logs](https://cloud.google.com/logging/docs/export).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LoggingClient loggingClient = LoggingClient.create()) {
       List<String> resourceNames = new ArrayList<>();
       String filter = "filter-1274492040";
       String orderBy = "orderBy-1207110587";
       for (LogEntry element :
           loggingClient.listLogEntries(resourceNames, filter, orderBy).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`resourceNames` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Names of one or more parent resources from which to retrieve log entries: 

  * `projects/[PROJECT_ID]`
  * `organizations/[ORGANIZATION_ID]`
  * `billingAccounts/[BILLING_ACCOUNT_ID]`
  * `folders/[FOLDER_ID]`

May alternatively be one or more views: * `projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]` * `organizations/[ORGANIZATION_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]` * `billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]` * `folders/[FOLDER_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]` Projects listed in the `project_ids` field are added to this list. A maximum of 100 resources may be specified in a single request.  
`filter` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. Only log entries that match the filter are returned. An empty filter matches all log entries in the resources listed in `resource_names`. Referencing a parent resource that is not listed in `resource_names` will cause the filter to return no results. The maximum length of a filter is 20,000 characters.  
`orderBy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. How the results should be sorted. Presently, the only permitted values are `"timestamp asc"` (default) and `"timestamp desc"`. The first option returns entries in order of increasing values of `LogEntry.timestamp` (oldest first), and the second option returns entries in order of decreasing timestamps (newest first). Entries with equal timestamps are returned in order of their `insert_id` values.  
**Returns**  
---  
**Type** | **Description**  
`[LoggingClient.ListLogEntriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.LoggingClient.ListLogEntriesPagedResponse)` |   
  
### listLogEntriesCallable()
    
    
    public final UnaryCallable<ListLogEntriesRequest,ListLogEntriesResponse> listLogEntriesCallable()

Lists log entries. Use this method to retrieve log entries that originated from a project/folder/organization/billing account. For ways to export log entries, see [Exporting Logs](https://cloud.google.com/logging/docs/export).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LoggingClient loggingClient = LoggingClient.create()) {
       ListLogEntriesRequest request =
           ListLogEntriesRequest.newBuilder()
               .addAllResourceNames(new ArrayList<String>())
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLogEntriesResponse response = loggingClient.listLogEntriesCallable().call(request);
         for (LogEntry element : response.getEntriesList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLogEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListLogEntriesRequest),[ListLogEntriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListLogEntriesResponse)>` |   
  
### listLogEntriesPagedCallable()
    
    
    public final UnaryCallable<ListLogEntriesRequest,LoggingClient.ListLogEntriesPagedResponse> listLogEntriesPagedCallable()

Lists log entries. Use this method to retrieve log entries that originated from a project/folder/organization/billing account. For ways to export log entries, see [Exporting Logs](https://cloud.google.com/logging/docs/export).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LoggingClient loggingClient = LoggingClient.create()) {
       ListLogEntriesRequest request =
           ListLogEntriesRequest.newBuilder()
               .addAllResourceNames(new ArrayList<String>())
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<LogEntry> future = loggingClient.listLogEntriesPagedCallable().futureCall(request);
       // Do something.
       for (LogEntry element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLogEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListLogEntriesRequest),[ListLogEntriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.LoggingClient.ListLogEntriesPagedResponse)>` |   
  
### listLogs(@Nullable BillingAccountName parent)
    
    
    public final LoggingClient.ListLogsPagedResponse listLogs(@Nullable BillingAccountName parent)

Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LoggingClient loggingClient = LoggingClient.create()) {
       BillingAccountName parent = BillingAccountName.of("[BILLING_ACCOUNT]");
       for (String element : loggingClient.listLogs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.logging.v2.BillingAccountName`  
Required. The resource name to list logs for: 

  * `projects/[PROJECT_ID]`
  * `organizations/[ORGANIZATION_ID]`
  * `billingAccounts/[BILLING_ACCOUNT_ID]`
  * `folders/[FOLDER_ID]`

  
**Returns**  
---  
**Type** | **Description**  
`[LoggingClient.ListLogsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.LoggingClient.ListLogsPagedResponse)` |   
  
### listLogs(@Nullable FolderName parent)
    
    
    public final LoggingClient.ListLogsPagedResponse listLogs(@Nullable FolderName parent)

Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LoggingClient loggingClient = LoggingClient.create()) {
       FolderName parent = FolderName.of("[FOLDER]");
       for (String element : loggingClient.listLogs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.logging.v2.FolderName`  
Required. The resource name to list logs for: 

  * `projects/[PROJECT_ID]`
  * `organizations/[ORGANIZATION_ID]`
  * `billingAccounts/[BILLING_ACCOUNT_ID]`
  * `folders/[FOLDER_ID]`

  
**Returns**  
---  
**Type** | **Description**  
`[LoggingClient.ListLogsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.LoggingClient.ListLogsPagedResponse)` |   
  
### listLogs(@Nullable OrganizationName parent)
    
    
    public final LoggingClient.ListLogsPagedResponse listLogs(@Nullable OrganizationName parent)

Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LoggingClient loggingClient = LoggingClient.create()) {
       OrganizationName parent = OrganizationName.of("[ORGANIZATION]");
       for (String element : loggingClient.listLogs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.logging.v2.OrganizationName`  
Required. The resource name to list logs for: 

  * `projects/[PROJECT_ID]`
  * `organizations/[ORGANIZATION_ID]`
  * `billingAccounts/[BILLING_ACCOUNT_ID]`
  * `folders/[FOLDER_ID]`

  
**Returns**  
---  
**Type** | **Description**  
`[LoggingClient.ListLogsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.LoggingClient.ListLogsPagedResponse)` |   
  
### listLogs(@Nullable ProjectName parent)
    
    
    public final LoggingClient.ListLogsPagedResponse listLogs(@Nullable ProjectName parent)

Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LoggingClient loggingClient = LoggingClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       for (String element : loggingClient.listLogs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.logging.v2.ProjectName`  
Required. The resource name to list logs for: 

  * `projects/[PROJECT_ID]`
  * `organizations/[ORGANIZATION_ID]`
  * `billingAccounts/[BILLING_ACCOUNT_ID]`
  * `folders/[FOLDER_ID]`

  
**Returns**  
---  
**Type** | **Description**  
`[LoggingClient.ListLogsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.LoggingClient.ListLogsPagedResponse)` |   
  
### listLogs(ListLogsRequest request)
    
    
    public final LoggingClient.ListLogsPagedResponse listLogs(ListLogsRequest request)

Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LoggingClient loggingClient = LoggingClient.create()) {
       ListLogsRequest request =
           ListLogsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .addAllResourceNames(new ArrayList<String>())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (String element : loggingClient.listLogs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListLogsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListLogsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LoggingClient.ListLogsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.LoggingClient.ListLogsPagedResponse)` |   
  
### listLogs(String parent)
    
    
    public final LoggingClient.ListLogsPagedResponse listLogs(String parent)

Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LoggingClient loggingClient = LoggingClient.create()) {
       String parent = ProjectName.of("[PROJECT]").toString();
       for (String element : loggingClient.listLogs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name to list logs for: 

  * `projects/[PROJECT_ID]`
  * `organizations/[ORGANIZATION_ID]`
  * `billingAccounts/[BILLING_ACCOUNT_ID]`
  * `folders/[FOLDER_ID]`

  
**Returns**  
---  
**Type** | **Description**  
`[LoggingClient.ListLogsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.LoggingClient.ListLogsPagedResponse)` |   
  
### listLogsCallable()
    
    
    public final UnaryCallable<ListLogsRequest,ListLogsResponse> listLogsCallable()

Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LoggingClient loggingClient = LoggingClient.create()) {
       ListLogsRequest request =
           ListLogsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .addAllResourceNames(new ArrayList<String>())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLogsResponse response = loggingClient.listLogsCallable().call(request);
         for (String element : response.getLogNamesList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLogsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListLogsRequest),[ListLogsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListLogsResponse)>` |   
  
### listLogsPagedCallable()
    
    
    public final UnaryCallable<ListLogsRequest,LoggingClient.ListLogsPagedResponse> listLogsPagedCallable()

Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LoggingClient loggingClient = LoggingClient.create()) {
       ListLogsRequest request =
           ListLogsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .addAllResourceNames(new ArrayList<String>())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<String> future = loggingClient.listLogsPagedCallable().futureCall(request);
       // Do something.
       for (String element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLogsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListLogsRequest),[ListLogsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.LoggingClient.ListLogsPagedResponse)>` |   
  
### listMonitoredResourceDescriptors(ListMonitoredResourceDescriptorsRequest request)
    
    
    public final LoggingClient.ListMonitoredResourceDescriptorsPagedResponse listMonitoredResourceDescriptors(ListMonitoredResourceDescriptorsRequest request)

Lists the descriptors for monitored resource types used by Logging.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LoggingClient loggingClient = LoggingClient.create()) {
       ListMonitoredResourceDescriptorsRequest request =
           ListMonitoredResourceDescriptorsRequest.newBuilder()
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (MonitoredResourceDescriptor element :
           loggingClient.listMonitoredResourceDescriptors(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMonitoredResourceDescriptorsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListMonitoredResourceDescriptorsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LoggingClient.ListMonitoredResourceDescriptorsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.LoggingClient.ListMonitoredResourceDescriptorsPagedResponse)` |   
  
### listMonitoredResourceDescriptorsCallable()
    
    
    public final UnaryCallable<ListMonitoredResourceDescriptorsRequest,ListMonitoredResourceDescriptorsResponse> listMonitoredResourceDescriptorsCallable()

Lists the descriptors for monitored resource types used by Logging.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LoggingClient loggingClient = LoggingClient.create()) {
       ListMonitoredResourceDescriptorsRequest request =
           ListMonitoredResourceDescriptorsRequest.newBuilder()
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListMonitoredResourceDescriptorsResponse response =
             loggingClient.listMonitoredResourceDescriptorsCallable().call(request);
         for (MonitoredResourceDescriptor element : response.getResourceDescriptorsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMonitoredResourceDescriptorsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListMonitoredResourceDescriptorsRequest),[ListMonitoredResourceDescriptorsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListMonitoredResourceDescriptorsResponse)>` |   
  
### listMonitoredResourceDescriptorsPagedCallable()
    
    
    public final UnaryCallable<ListMonitoredResourceDescriptorsRequest,LoggingClient.ListMonitoredResourceDescriptorsPagedResponse> listMonitoredResourceDescriptorsPagedCallable()

Lists the descriptors for monitored resource types used by Logging.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LoggingClient loggingClient = LoggingClient.create()) {
       ListMonitoredResourceDescriptorsRequest request =
           ListMonitoredResourceDescriptorsRequest.newBuilder()
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<MonitoredResourceDescriptor> future =
           loggingClient.listMonitoredResourceDescriptorsPagedCallable().futureCall(request);
       // Do something.
       for (MonitoredResourceDescriptor element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMonitoredResourceDescriptorsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListMonitoredResourceDescriptorsRequest),[ListMonitoredResourceDescriptorsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.LoggingClient.ListMonitoredResourceDescriptorsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### tailLogEntriesCallable()
    
    
    public final BidiStreamingCallable<TailLogEntriesRequest,TailLogEntriesResponse> tailLogEntriesCallable()

Streaming read of log entries as they are ingested. Until the stream is terminated, it will continue reading logs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LoggingClient loggingClient = LoggingClient.create()) {
       BidiStream<TailLogEntriesRequest, TailLogEntriesResponse> bidiStream =
           loggingClient.tailLogEntriesCallable().call();
       TailLogEntriesRequest request =
           TailLogEntriesRequest.newBuilder()
               .addAllResourceNames(new ArrayList<String>())
               .setFilter("filter-1274492040")
               .setBufferWindow(Duration.newBuilder().build())
               .build();
       bidiStream.send(request);
       for (TailLogEntriesResponse response : bidiStream) {
         // Do something when a response is received.
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[BidiStreamingCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BidiStreamingCallable.html)<[TailLogEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.TailLogEntriesRequest),[TailLogEntriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.TailLogEntriesResponse)>` |   
  
### writeLogEntries(@Nullable LogName logName, MonitoredResource resource, Map<String,String> labels, List<LogEntry> entries)
    
    
    public final WriteLogEntriesResponse writeLogEntries(@Nullable LogName logName, MonitoredResource resource, Map<String,String> labels, List<LogEntry> entries)

Writes log entries to Logging. This API method is the only way to send log entries to Logging. This method is used, directly or indirectly, by the Logging agent (fluentd) and all logging libraries configured to use Logging. A single request may contain log entries for a maximum of 1000 different resources (projects, organizations, billing accounts or folders)

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LoggingClient loggingClient = LoggingClient.create()) {
       LogName logName = LogName.ofProjectLogName("[PROJECT]", "[LOG]");
       MonitoredResource resource = MonitoredResource.newBuilder().build();
       Map<String, String> labels = new HashMap<>();
       List<LogEntry> entries = new ArrayList<>();
       WriteLogEntriesResponse response =
           loggingClient.writeLogEntries(logName, resource, labels, entries);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`logName` | `@org.jspecify.annotations.Nullable com.google.logging.v2.LogName`  
Optional. A default log resource name that is assigned to all log entries in `entries` that do not specify a value for `log_name`: 

  * `projects/[PROJECT_ID]/logs/[LOG_ID]`
  * `organizations/[ORGANIZATION_ID]/logs/[LOG_ID]`
  * `billingAccounts/[BILLING_ACCOUNT_ID]/logs/[LOG_ID]`
  * `folders/[FOLDER_ID]/logs/[LOG_ID]`

`[LOG_ID]` must be URL-encoded. For example: "projects/my-project-id/logs/syslog" "organizations/123/logs/cloudaudit.googleapis.com%2Factivity" The permission `logging.logEntries.create` is needed on each project, organization, billing account, or folder that is receiving new log entries, whether the resource is specified in `logName` or in an individual log entry.  
`resource` | `com.google.api.MonitoredResource`  
Optional. A default monitored resource object that is assigned to all log entries in `entries` that do not specify a value for `resource`. Example: { "type": "gce_instance", "labels": { "zone": "us-central1-a", "instance_id": "00000000000000000000" }} See LogEntry.  
`labels` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Optional. Default labels that are added to the `labels` field of all log entries in `entries`. If a log entry already has a label with the same key as a label in this parameter, then the log entry's label is not changed. See LogEntry.  
`entries` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogEntry)>`  
Required. The log entries to send to Logging. The order of log entries in this list does not matter. Values supplied in this method's `log_name`, `resource`, and `labels` fields are copied into those log entries in this list that do not include values for their corresponding fields. For more information, see the LogEntry type. If the `timestamp` or `insert_id` fields are missing in log entries, then this method supplies the current time or a unique identifier, respectively. The supplied values are chosen so that, among the log entries that did not supply their own values, the entries earlier in the list will sort before the entries later in the list. See the `entries.list` method. Log entries with timestamps that are more than the [logs retention period](https://cloud.google.com/logging/quotas) in the past or more than 24 hours in the future will not be available when calling `entries.list`. However, those log entries can still be [exported with LogSinks](https://cloud.google.com/logging/docs/api/tasks/exporting-logs). To improve throughput and to avoid exceeding the [quota limit](https://cloud.google.com/logging/quotas) for calls to `entries.write`, you should try to include several log entries in this list, rather than calling this method for each individual log entry.  
**Returns**  
---  
**Type** | **Description**  
`[WriteLogEntriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.WriteLogEntriesResponse)` |   
  
### writeLogEntries(WriteLogEntriesRequest request)
    
    
    public final WriteLogEntriesResponse writeLogEntries(WriteLogEntriesRequest request)

Writes log entries to Logging. This API method is the only way to send log entries to Logging. This method is used, directly or indirectly, by the Logging agent (fluentd) and all logging libraries configured to use Logging. A single request may contain log entries for a maximum of 1000 different resources (projects, organizations, billing accounts or folders)

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LoggingClient loggingClient = LoggingClient.create()) {
       WriteLogEntriesRequest request =
           WriteLogEntriesRequest.newBuilder()
               .setLogName(LogName.ofProjectLogName("[PROJECT]", "[LOG]").toString())
               .setResource(MonitoredResource.newBuilder().build())
               .putAllLabels(new HashMap<String, String>())
               .addAllEntries(new ArrayList<LogEntry>())
               .setPartialSuccess(true)
               .setDryRun(true)
               .build();
       WriteLogEntriesResponse response = loggingClient.writeLogEntries(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[WriteLogEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.WriteLogEntriesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[WriteLogEntriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.WriteLogEntriesResponse)` |   
  
### writeLogEntries(String logName, MonitoredResource resource, Map<String,String> labels, List<LogEntry> entries)
    
    
    public final WriteLogEntriesResponse writeLogEntries(String logName, MonitoredResource resource, Map<String,String> labels, List<LogEntry> entries)

Writes log entries to Logging. This API method is the only way to send log entries to Logging. This method is used, directly or indirectly, by the Logging agent (fluentd) and all logging libraries configured to use Logging. A single request may contain log entries for a maximum of 1000 different resources (projects, organizations, billing accounts or folders)

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LoggingClient loggingClient = LoggingClient.create()) {
       String logName = LogName.ofProjectLogName("[PROJECT]", "[LOG]").toString();
       MonitoredResource resource = MonitoredResource.newBuilder().build();
       Map<String, String> labels = new HashMap<>();
       List<LogEntry> entries = new ArrayList<>();
       WriteLogEntriesResponse response =
           loggingClient.writeLogEntries(logName, resource, labels, entries);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`logName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. A default log resource name that is assigned to all log entries in `entries` that do not specify a value for `log_name`: 

  * `projects/[PROJECT_ID]/logs/[LOG_ID]`
  * `organizations/[ORGANIZATION_ID]/logs/[LOG_ID]`
  * `billingAccounts/[BILLING_ACCOUNT_ID]/logs/[LOG_ID]`
  * `folders/[FOLDER_ID]/logs/[LOG_ID]`

`[LOG_ID]` must be URL-encoded. For example: "projects/my-project-id/logs/syslog" "organizations/123/logs/cloudaudit.googleapis.com%2Factivity" The permission `logging.logEntries.create` is needed on each project, organization, billing account, or folder that is receiving new log entries, whether the resource is specified in `logName` or in an individual log entry.  
`resource` | `com.google.api.MonitoredResource`  
Optional. A default monitored resource object that is assigned to all log entries in `entries` that do not specify a value for `resource`. Example: { "type": "gce_instance", "labels": { "zone": "us-central1-a", "instance_id": "00000000000000000000" }} See LogEntry.  
`labels` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Optional. Default labels that are added to the `labels` field of all log entries in `entries`. If a log entry already has a label with the same key as a label in this parameter, then the log entry's label is not changed. See LogEntry.  
`entries` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogEntry)>`  
Required. The log entries to send to Logging. The order of log entries in this list does not matter. Values supplied in this method's `log_name`, `resource`, and `labels` fields are copied into those log entries in this list that do not include values for their corresponding fields. For more information, see the LogEntry type. If the `timestamp` or `insert_id` fields are missing in log entries, then this method supplies the current time or a unique identifier, respectively. The supplied values are chosen so that, among the log entries that did not supply their own values, the entries earlier in the list will sort before the entries later in the list. See the `entries.list` method. Log entries with timestamps that are more than the [logs retention period](https://cloud.google.com/logging/quotas) in the past or more than 24 hours in the future will not be available when calling `entries.list`. However, those log entries can still be [exported with LogSinks](https://cloud.google.com/logging/docs/api/tasks/exporting-logs). To improve throughput and to avoid exceeding the [quota limit](https://cloud.google.com/logging/quotas) for calls to `entries.write`, you should try to include several log entries in this list, rather than calling this method for each individual log entry.  
**Returns**  
---  
**Type** | **Description**  
`[WriteLogEntriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.WriteLogEntriesResponse)` |   
  
### writeLogEntriesCallable()
    
    
    public final UnaryCallable<WriteLogEntriesRequest,WriteLogEntriesResponse> writeLogEntriesCallable()

Writes log entries to Logging. This API method is the only way to send log entries to Logging. This method is used, directly or indirectly, by the Logging agent (fluentd) and all logging libraries configured to use Logging. A single request may contain log entries for a maximum of 1000 different resources (projects, organizations, billing accounts or folders)

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LoggingClient loggingClient = LoggingClient.create()) {
       WriteLogEntriesRequest request =
           WriteLogEntriesRequest.newBuilder()
               .setLogName(LogName.ofProjectLogName("[PROJECT]", "[LOG]").toString())
               .setResource(MonitoredResource.newBuilder().build())
               .putAllLabels(new HashMap<String, String>())
               .addAllEntries(new ArrayList<LogEntry>())
               .setPartialSuccess(true)
               .setDryRun(true)
               .build();
       ApiFuture<WriteLogEntriesResponse> future =
           loggingClient.writeLogEntriesCallable().futureCall(request);
       // Do something.
       WriteLogEntriesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[WriteLogEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.WriteLogEntriesRequest),[WriteLogEntriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.WriteLogEntriesResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
