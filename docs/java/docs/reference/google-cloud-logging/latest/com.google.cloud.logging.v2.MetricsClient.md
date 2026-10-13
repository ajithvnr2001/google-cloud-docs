---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.MetricsClient
title: Class MetricsClient (3.40.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:21:09.375042+00:00
---

# Class MetricsClient (3.40.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.MetricsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class MetricsClient (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.36.0  3.35.0  3.34.0  3.32.0  3.29.0  3.28.0  3.26.0  3.24.0  3.23.10  3.22.6  3.21.4  3.20.7  3.19.0  3.18.0  3.17.2  3.16.2  3.15.17  3.14.9  3.13.7  3.12.1  3.11.10  3.10.7  3.9.0  3.8.0  3.7.6  3.6.4  3.5.3 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-logging/google-cloud-logging/src/main/java/com/google/cloud/logging/v2/MetricsClient.java)| [Product Reference](https://cloud.google.com/logging/docs)  
---|---  
  
Service Description: Service for configuring logs-based metrics.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetricsClient metricsClient = MetricsClient.create()) {
       LogMetricName metricName = LogMetricName.of("[PROJECT]", "[METRIC]");
       LogMetric response = metricsClient.getLogMetric(metricName);
     }
     

Note: close() needs to be called on the MetricsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListLogMetrics |  Lists logs-based metrics. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLogMetrics(ListLogMetricsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listLogMetrics(ProjectName parent) 
  * listLogMetrics(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLogMetricsPagedCallable() 
  * listLogMetricsCallable() 

  
GetLogMetric |  Gets a logs-based metric. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLogMetric(GetLogMetricRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getLogMetric(LogMetricName metricName) 
  * getLogMetric(String metricName) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLogMetricCallable() 

  
CreateLogMetric |  Creates a logs-based metric. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createLogMetric(CreateLogMetricRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createLogMetric(ProjectName parent, LogMetric metric) 
  * createLogMetric(String parent, LogMetric metric) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createLogMetricCallable() 

  
UpdateLogMetric |  Creates or updates a logs-based metric. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateLogMetric(UpdateLogMetricRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateLogMetric(LogMetricName metricName, LogMetric metric) 
  * updateLogMetric(String metricName, LogMetric metric) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateLogMetricCallable() 

  
DeleteLogMetric |  Deletes a logs-based metric. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteLogMetric(DeleteLogMetricRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteLogMetric(LogMetricName metricName) 
  * deleteLogMetric(String metricName) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteLogMetricCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of MetricsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     MetricsSettings metricsSettings =
         MetricsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     MetricsClient metricsClient = MetricsClient.create(metricsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     MetricsSettings metricsSettings = MetricsSettings.newBuilder().setEndpoint(myEndpoint).build();
     MetricsClient metricsClient = MetricsClient.create(metricsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > MetricsClient

## Static Methods 

### create()
    
    
    public static final MetricsClient create()

Constructs an instance of MetricsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[MetricsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.MetricsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(MetricsSettings settings)
    
    
    public static final MetricsClient create(MetricsSettings settings)

Constructs an instance of MetricsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[MetricsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.MetricsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MetricsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.MetricsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(MetricsServiceV2Stub stub)
    
    
    public static final MetricsClient create(MetricsServiceV2Stub stub)

Constructs an instance of MetricsClient, using the given stub for making calls. This is for advanced usage - prefer using create(MetricsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[MetricsServiceV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.stub.MetricsServiceV2Stub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MetricsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.MetricsClient)` |   
  
## Constructors 

### MetricsClient(MetricsSettings settings)
    
    
    protected MetricsClient(MetricsSettings settings)

Constructs an instance of MetricsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[MetricsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.MetricsSettings)`  
  
  
### MetricsClient(MetricsServiceV2Stub stub)
    
    
    protected MetricsClient(MetricsServiceV2Stub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[MetricsServiceV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.stub.MetricsServiceV2Stub)`  
  
  
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

### createLogMetric(@Nullable ProjectName parent, LogMetric metric)
    
    
    public final LogMetric createLogMetric(@Nullable ProjectName parent, LogMetric metric)

Creates a logs-based metric.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetricsClient metricsClient = MetricsClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       LogMetric metric = LogMetric.newBuilder().build();
       LogMetric response = metricsClient.createLogMetric(parent, metric);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.logging.v2.ProjectName`  
Required. The resource name of the project in which to create the metric: "projects/[PROJECT_ID]" The new metric must be provided in the request.  
`metric` | `[LogMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogMetric)`  
Required. The new logs-based metric, which must not have an identifier that already exists.  
**Returns**  
---  
**Type** | **Description**  
`[LogMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogMetric)` |   
  
### createLogMetric(CreateLogMetricRequest request)
    
    
    public final LogMetric createLogMetric(CreateLogMetricRequest request)

Creates a logs-based metric.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetricsClient metricsClient = MetricsClient.create()) {
       CreateLogMetricRequest request =
           CreateLogMetricRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setMetric(LogMetric.newBuilder().build())
               .build();
       LogMetric response = metricsClient.createLogMetric(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateLogMetricRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CreateLogMetricRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LogMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogMetric)` |   
  
### createLogMetric(String parent, LogMetric metric)
    
    
    public final LogMetric createLogMetric(String parent, LogMetric metric)

Creates a logs-based metric.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetricsClient metricsClient = MetricsClient.create()) {
       String parent = ProjectName.of("[PROJECT]").toString();
       LogMetric metric = LogMetric.newBuilder().build();
       LogMetric response = metricsClient.createLogMetric(parent, metric);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the project in which to create the metric: "projects/[PROJECT_ID]" The new metric must be provided in the request.  
`metric` | `[LogMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogMetric)`  
Required. The new logs-based metric, which must not have an identifier that already exists.  
**Returns**  
---  
**Type** | **Description**  
`[LogMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogMetric)` |   
  
### createLogMetricCallable()
    
    
    public final UnaryCallable<CreateLogMetricRequest,LogMetric> createLogMetricCallable()

Creates a logs-based metric.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetricsClient metricsClient = MetricsClient.create()) {
       CreateLogMetricRequest request =
           CreateLogMetricRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setMetric(LogMetric.newBuilder().build())
               .build();
       ApiFuture<LogMetric> future = metricsClient.createLogMetricCallable().futureCall(request);
       // Do something.
       LogMetric response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateLogMetricRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CreateLogMetricRequest),[LogMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogMetric)>` |   
  
### deleteLogMetric(@Nullable LogMetricName metricName)
    
    
    public final void deleteLogMetric(@Nullable LogMetricName metricName)

Deletes a logs-based metric.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetricsClient metricsClient = MetricsClient.create()) {
       LogMetricName metricName = LogMetricName.of("[PROJECT]", "[METRIC]");
       metricsClient.deleteLogMetric(metricName);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`metricName` | `@org.jspecify.annotations.Nullable com.google.logging.v2.LogMetricName`  
Required. The resource name of the metric to delete: "projects/[PROJECT_ID]/metrics/[METRIC_ID]"  
  
### deleteLogMetric(DeleteLogMetricRequest request)
    
    
    public final void deleteLogMetric(DeleteLogMetricRequest request)

Deletes a logs-based metric.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetricsClient metricsClient = MetricsClient.create()) {
       DeleteLogMetricRequest request =
           DeleteLogMetricRequest.newBuilder()
               .setMetricName(LogMetricName.of("[PROJECT]", "[METRIC]").toString())
               .build();
       metricsClient.deleteLogMetric(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteLogMetricRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.DeleteLogMetricRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteLogMetric(String metricName)
    
    
    public final void deleteLogMetric(String metricName)

Deletes a logs-based metric.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetricsClient metricsClient = MetricsClient.create()) {
       String metricName = LogMetricName.of("[PROJECT]", "[METRIC]").toString();
       metricsClient.deleteLogMetric(metricName);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`metricName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the metric to delete: "projects/[PROJECT_ID]/metrics/[METRIC_ID]"  
  
### deleteLogMetricCallable()
    
    
    public final UnaryCallable<DeleteLogMetricRequest,Empty> deleteLogMetricCallable()

Deletes a logs-based metric.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetricsClient metricsClient = MetricsClient.create()) {
       DeleteLogMetricRequest request =
           DeleteLogMetricRequest.newBuilder()
               .setMetricName(LogMetricName.of("[PROJECT]", "[METRIC]").toString())
               .build();
       ApiFuture<Empty> future = metricsClient.deleteLogMetricCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteLogMetricRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.DeleteLogMetricRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getLogMetric(@Nullable LogMetricName metricName)
    
    
    public final LogMetric getLogMetric(@Nullable LogMetricName metricName)

Gets a logs-based metric.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetricsClient metricsClient = MetricsClient.create()) {
       LogMetricName metricName = LogMetricName.of("[PROJECT]", "[METRIC]");
       LogMetric response = metricsClient.getLogMetric(metricName);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`metricName` | `@org.jspecify.annotations.Nullable com.google.logging.v2.LogMetricName`  
Required. The resource name of the desired metric: "projects/[PROJECT_ID]/metrics/[METRIC_ID]"  
**Returns**  
---  
**Type** | **Description**  
`[LogMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogMetric)` |   
  
### getLogMetric(GetLogMetricRequest request)
    
    
    public final LogMetric getLogMetric(GetLogMetricRequest request)

Gets a logs-based metric.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetricsClient metricsClient = MetricsClient.create()) {
       GetLogMetricRequest request =
           GetLogMetricRequest.newBuilder()
               .setMetricName(LogMetricName.of("[PROJECT]", "[METRIC]").toString())
               .build();
       LogMetric response = metricsClient.getLogMetric(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetLogMetricRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.GetLogMetricRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LogMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogMetric)` |   
  
### getLogMetric(String metricName)
    
    
    public final LogMetric getLogMetric(String metricName)

Gets a logs-based metric.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetricsClient metricsClient = MetricsClient.create()) {
       String metricName = LogMetricName.of("[PROJECT]", "[METRIC]").toString();
       LogMetric response = metricsClient.getLogMetric(metricName);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`metricName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the desired metric: "projects/[PROJECT_ID]/metrics/[METRIC_ID]"  
**Returns**  
---  
**Type** | **Description**  
`[LogMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogMetric)` |   
  
### getLogMetricCallable()
    
    
    public final UnaryCallable<GetLogMetricRequest,LogMetric> getLogMetricCallable()

Gets a logs-based metric.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetricsClient metricsClient = MetricsClient.create()) {
       GetLogMetricRequest request =
           GetLogMetricRequest.newBuilder()
               .setMetricName(LogMetricName.of("[PROJECT]", "[METRIC]").toString())
               .build();
       ApiFuture<LogMetric> future = metricsClient.getLogMetricCallable().futureCall(request);
       // Do something.
       LogMetric response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetLogMetricRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.GetLogMetricRequest),[LogMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogMetric)>` |   
  
### getSettings()
    
    
    public final @Nullable MetricsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.logging.v2.MetricsSettings` |   
  
### getStub()
    
    
    public MetricsServiceV2Stub getStub()

**Returns**  
---  
**Type** | **Description**  
`[MetricsServiceV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.stub.MetricsServiceV2Stub)` |   
  
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
  
### listLogMetrics(@Nullable ProjectName parent)
    
    
    public final MetricsClient.ListLogMetricsPagedResponse listLogMetrics(@Nullable ProjectName parent)

Lists logs-based metrics.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetricsClient metricsClient = MetricsClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       for (LogMetric element : metricsClient.listLogMetrics(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.logging.v2.ProjectName`  
Required. The name of the project containing the metrics: "projects/[PROJECT_ID]"  
**Returns**  
---  
**Type** | **Description**  
`[MetricsClient.ListLogMetricsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.MetricsClient.ListLogMetricsPagedResponse)` |   
  
### listLogMetrics(ListLogMetricsRequest request)
    
    
    public final MetricsClient.ListLogMetricsPagedResponse listLogMetrics(ListLogMetricsRequest request)

Lists logs-based metrics.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetricsClient metricsClient = MetricsClient.create()) {
       ListLogMetricsRequest request =
           ListLogMetricsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       for (LogMetric element : metricsClient.listLogMetrics(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListLogMetricsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListLogMetricsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MetricsClient.ListLogMetricsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.MetricsClient.ListLogMetricsPagedResponse)` |   
  
### listLogMetrics(String parent)
    
    
    public final MetricsClient.ListLogMetricsPagedResponse listLogMetrics(String parent)

Lists logs-based metrics.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetricsClient metricsClient = MetricsClient.create()) {
       String parent = ProjectName.of("[PROJECT]").toString();
       for (LogMetric element : metricsClient.listLogMetrics(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the project containing the metrics: "projects/[PROJECT_ID]"  
**Returns**  
---  
**Type** | **Description**  
`[MetricsClient.ListLogMetricsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.MetricsClient.ListLogMetricsPagedResponse)` |   
  
### listLogMetricsCallable()
    
    
    public final UnaryCallable<ListLogMetricsRequest,ListLogMetricsResponse> listLogMetricsCallable()

Lists logs-based metrics.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetricsClient metricsClient = MetricsClient.create()) {
       ListLogMetricsRequest request =
           ListLogMetricsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       while (true) {
         ListLogMetricsResponse response = metricsClient.listLogMetricsCallable().call(request);
         for (LogMetric element : response.getMetricsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLogMetricsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListLogMetricsRequest),[ListLogMetricsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListLogMetricsResponse)>` |   
  
### listLogMetricsPagedCallable()
    
    
    public final UnaryCallable<ListLogMetricsRequest,MetricsClient.ListLogMetricsPagedResponse> listLogMetricsPagedCallable()

Lists logs-based metrics.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetricsClient metricsClient = MetricsClient.create()) {
       ListLogMetricsRequest request =
           ListLogMetricsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       ApiFuture<LogMetric> future = metricsClient.listLogMetricsPagedCallable().futureCall(request);
       // Do something.
       for (LogMetric element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLogMetricsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListLogMetricsRequest),[ListLogMetricsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.MetricsClient.ListLogMetricsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateLogMetric(@Nullable LogMetricName metricName, LogMetric metric)
    
    
    public final LogMetric updateLogMetric(@Nullable LogMetricName metricName, LogMetric metric)

Creates or updates a logs-based metric.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetricsClient metricsClient = MetricsClient.create()) {
       LogMetricName metricName = LogMetricName.of("[PROJECT]", "[METRIC]");
       LogMetric metric = LogMetric.newBuilder().build();
       LogMetric response = metricsClient.updateLogMetric(metricName, metric);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`metricName` | `@org.jspecify.annotations.Nullable com.google.logging.v2.LogMetricName`  
Required. The resource name of the metric to update: "projects/[PROJECT_ID]/metrics/[METRIC_ID]" The updated metric must be provided in the request and it's `name` field must be the same as `[METRIC_ID]` If the metric does not exist in `[PROJECT_ID]`, then a new metric is created.  
`metric` | `[LogMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogMetric)`  
Required. The updated metric.  
**Returns**  
---  
**Type** | **Description**  
`[LogMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogMetric)` |   
  
### updateLogMetric(UpdateLogMetricRequest request)
    
    
    public final LogMetric updateLogMetric(UpdateLogMetricRequest request)

Creates or updates a logs-based metric.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetricsClient metricsClient = MetricsClient.create()) {
       UpdateLogMetricRequest request =
           UpdateLogMetricRequest.newBuilder()
               .setMetricName(LogMetricName.of("[PROJECT]", "[METRIC]").toString())
               .setMetric(LogMetric.newBuilder().build())
               .build();
       LogMetric response = metricsClient.updateLogMetric(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateLogMetricRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.UpdateLogMetricRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LogMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogMetric)` |   
  
### updateLogMetric(String metricName, LogMetric metric)
    
    
    public final LogMetric updateLogMetric(String metricName, LogMetric metric)

Creates or updates a logs-based metric.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetricsClient metricsClient = MetricsClient.create()) {
       String metricName = LogMetricName.of("[PROJECT]", "[METRIC]").toString();
       LogMetric metric = LogMetric.newBuilder().build();
       LogMetric response = metricsClient.updateLogMetric(metricName, metric);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`metricName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the metric to update: "projects/[PROJECT_ID]/metrics/[METRIC_ID]" The updated metric must be provided in the request and it's `name` field must be the same as `[METRIC_ID]` If the metric does not exist in `[PROJECT_ID]`, then a new metric is created.  
`metric` | `[LogMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogMetric)`  
Required. The updated metric.  
**Returns**  
---  
**Type** | **Description**  
`[LogMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogMetric)` |   
  
### updateLogMetricCallable()
    
    
    public final UnaryCallable<UpdateLogMetricRequest,LogMetric> updateLogMetricCallable()

Creates or updates a logs-based metric.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MetricsClient metricsClient = MetricsClient.create()) {
       UpdateLogMetricRequest request =
           UpdateLogMetricRequest.newBuilder()
               .setMetricName(LogMetricName.of("[PROJECT]", "[METRIC]").toString())
               .setMetric(LogMetric.newBuilder().build())
               .build();
       ApiFuture<LogMetric> future = metricsClient.updateLogMetricCallable().futureCall(request);
       // Do something.
       LogMetric response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateLogMetricRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.UpdateLogMetricRequest),[LogMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogMetric)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
