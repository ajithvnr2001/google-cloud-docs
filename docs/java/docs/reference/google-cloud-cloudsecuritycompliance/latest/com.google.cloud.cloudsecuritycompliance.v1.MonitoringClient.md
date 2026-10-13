---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.MonitoringClient
title: Class MonitoringClient (0.26.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:26:48.093929+00:00
---

# Class MonitoringClient (0.26.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.MonitoringClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class MonitoringClient (0.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.26.0 (latest)  0.22.0  0.21.0  0.20.0  0.18.0  0.15.0  0.14.0  0.12.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-cloudsecuritycompliance/google-cloud-cloudsecuritycompliance/src/main/java/com/google/cloud/cloudsecuritycompliance/v1/MonitoringClient.java)| [Product Reference](https://cloud.google.com/security-command-center/docs/compliance-manager-overview)  
---|---  
  
Service Description: Service describing handlers for resources

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MonitoringClient monitoringClient = MonitoringClient.create()) {
       FrameworkComplianceReportName name =
           FrameworkComplianceReportName.ofOrganizationLocationFrameworkComplianceReportName(
               "[ORGANIZATION]", "[LOCATION]", "[FRAMEWORK_COMPLIANCE_REPORT]");
       FrameworkComplianceReport response = monitoringClient.fetchFrameworkComplianceReport(name);
     }
     

Note: close() needs to be called on the MonitoringClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListFrameworkComplianceSummaries |  Lists the framework compliance summary for a given scope. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listFrameworkComplianceSummaries(ListFrameworkComplianceSummariesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listFrameworkComplianceSummaries(FolderLocationName parent) 
  * listFrameworkComplianceSummaries(LocationName parent) 
  * listFrameworkComplianceSummaries(OrganizationLocationName parent) 
  * listFrameworkComplianceSummaries(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listFrameworkComplianceSummariesPagedCallable() 
  * listFrameworkComplianceSummariesCallable() 

  
ListFindingSummaries |  Lists the finding summary by category for a given scope. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listFindingSummaries(ListFindingSummariesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listFindingSummaries(FolderLocationName parent) 
  * listFindingSummaries(LocationName parent) 
  * listFindingSummaries(OrganizationLocationName parent) 
  * listFindingSummaries(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listFindingSummariesPagedCallable() 
  * listFindingSummariesCallable() 

  
FetchFrameworkComplianceReport |  Fetches the framework compliance report for a given scope. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * fetchFrameworkComplianceReport(FetchFrameworkComplianceReportRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * fetchFrameworkComplianceReport(FrameworkComplianceReportName name) 
  * fetchFrameworkComplianceReport(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * fetchFrameworkComplianceReportCallable() 

  
ListControlComplianceSummaries |  Lists the control compliance summary for a given scope. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listControlComplianceSummaries(ListControlComplianceSummariesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listControlComplianceSummaries(FrameworkComplianceReportName parent) 
  * listControlComplianceSummaries(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listControlComplianceSummariesPagedCallable() 
  * listControlComplianceSummariesCallable() 

  
AggregateFrameworkComplianceReport |  Gets the aggregated compliance report over time for a given scope. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * aggregateFrameworkComplianceReport(AggregateFrameworkComplianceReportRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * aggregateFrameworkComplianceReport(FrameworkComplianceReportName name) 
  * aggregateFrameworkComplianceReport(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * aggregateFrameworkComplianceReportCallable() 

  
ListLocations |  Lists information about the supported locations for this service.  This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.  For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLocations(ListLocationsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLocationsPagedCallable() 
  * listLocationsCallable() 

  
GetLocation |  Gets information about a location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLocation(GetLocationRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLocationCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of MonitoringSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     MonitoringSettings monitoringSettings =
         MonitoringSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     MonitoringClient monitoringClient = MonitoringClient.create(monitoringSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     MonitoringSettings monitoringSettings =
         MonitoringSettings.newBuilder().setEndpoint(myEndpoint).build();
     MonitoringClient monitoringClient = MonitoringClient.create(monitoringSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     MonitoringSettings monitoringSettings = MonitoringSettings.newHttpJsonBuilder().build();
     MonitoringClient monitoringClient = MonitoringClient.create(monitoringSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > MonitoringClient

## Static Methods 

### create()
    
    
    public static final MonitoringClient create()

Constructs an instance of MonitoringClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[MonitoringClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.MonitoringClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(MonitoringSettings settings)
    
    
    public static final MonitoringClient create(MonitoringSettings settings)

Constructs an instance of MonitoringClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[MonitoringSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.MonitoringSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MonitoringClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.MonitoringClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(MonitoringStub stub)
    
    
    public static final MonitoringClient create(MonitoringStub stub)

Constructs an instance of MonitoringClient, using the given stub for making calls. This is for advanced usage - prefer using create(MonitoringSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[MonitoringStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.stub.MonitoringStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MonitoringClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.MonitoringClient)` |   
  
## Constructors 

### MonitoringClient(MonitoringSettings settings)
    
    
    protected MonitoringClient(MonitoringSettings settings)

Constructs an instance of MonitoringClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[MonitoringSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.MonitoringSettings)`  
  
  
### MonitoringClient(MonitoringStub stub)
    
    
    protected MonitoringClient(MonitoringStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[MonitoringStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.stub.MonitoringStub)`  
  
  
## Methods 

### aggregateFrameworkComplianceReport(@Nullable FrameworkComplianceReportName name)
    
    
    public final AggregateFrameworkComplianceReportResponse aggregateFrameworkComplianceReport(@Nullable FrameworkComplianceReportName name)

Gets the aggregated compliance report over time for a given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MonitoringClient monitoringClient = MonitoringClient.create()) {
       FrameworkComplianceReportName name =
           FrameworkComplianceReportName.ofOrganizationLocationFrameworkComplianceReportName(
               "[ORGANIZATION]", "[LOCATION]", "[FRAMEWORK_COMPLIANCE_REPORT]");
       AggregateFrameworkComplianceReportResponse response =
           monitoringClient.aggregateFrameworkComplianceReport(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.FrameworkComplianceReportName`  
Required. The name of the aggregated compliance report over time to retrieve. The supported format is: `organizations/{organization_id}/locations/{location}/frameworkComplianceReports/{framework_compliance_report}`  
**Returns**  
---  
**Type** | **Description**  
`[AggregateFrameworkComplianceReportResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.AggregateFrameworkComplianceReportResponse)` |   
  
### aggregateFrameworkComplianceReport(AggregateFrameworkComplianceReportRequest request)
    
    
    public final AggregateFrameworkComplianceReportResponse aggregateFrameworkComplianceReport(AggregateFrameworkComplianceReportRequest request)

Gets the aggregated compliance report over time for a given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MonitoringClient monitoringClient = MonitoringClient.create()) {
       AggregateFrameworkComplianceReportRequest request =
           AggregateFrameworkComplianceReportRequest.newBuilder()
               .setName(
                   FrameworkComplianceReportName.ofOrganizationLocationFrameworkComplianceReportName(
                           "[ORGANIZATION]", "[LOCATION]", "[FRAMEWORK_COMPLIANCE_REPORT]")
                       .toString())
               .setInterval(Interval.newBuilder().build())
               .setFilter("filter-1274492040")
               .build();
       AggregateFrameworkComplianceReportResponse response =
           monitoringClient.aggregateFrameworkComplianceReport(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AggregateFrameworkComplianceReportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.AggregateFrameworkComplianceReportRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AggregateFrameworkComplianceReportResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.AggregateFrameworkComplianceReportResponse)` |   
  
### aggregateFrameworkComplianceReport(String name)
    
    
    public final AggregateFrameworkComplianceReportResponse aggregateFrameworkComplianceReport(String name)

Gets the aggregated compliance report over time for a given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MonitoringClient monitoringClient = MonitoringClient.create()) {
       String name =
           FrameworkComplianceReportName.ofProjectLocationFrameworkComplianceReportName(
                   "[PROJECT]", "[LOCATION]", "[FRAMEWORK_COMPLIANCE_REPORT]")
               .toString();
       AggregateFrameworkComplianceReportResponse response =
           monitoringClient.aggregateFrameworkComplianceReport(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the aggregated compliance report over time to retrieve. The supported format is: `organizations/{organization_id}/locations/{location}/frameworkComplianceReports/{framework_compliance_report}`  
**Returns**  
---  
**Type** | **Description**  
`[AggregateFrameworkComplianceReportResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.AggregateFrameworkComplianceReportResponse)` |   
  
### aggregateFrameworkComplianceReportCallable()
    
    
    public final UnaryCallable<AggregateFrameworkComplianceReportRequest,AggregateFrameworkComplianceReportResponse> aggregateFrameworkComplianceReportCallable()

Gets the aggregated compliance report over time for a given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MonitoringClient monitoringClient = MonitoringClient.create()) {
       AggregateFrameworkComplianceReportRequest request =
           AggregateFrameworkComplianceReportRequest.newBuilder()
               .setName(
                   FrameworkComplianceReportName.ofOrganizationLocationFrameworkComplianceReportName(
                           "[ORGANIZATION]", "[LOCATION]", "[FRAMEWORK_COMPLIANCE_REPORT]")
                       .toString())
               .setInterval(Interval.newBuilder().build())
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<AggregateFrameworkComplianceReportResponse> future =
           monitoringClient.aggregateFrameworkComplianceReportCallable().futureCall(request);
       // Do something.
       AggregateFrameworkComplianceReportResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregateFrameworkComplianceReportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.AggregateFrameworkComplianceReportRequest),[AggregateFrameworkComplianceReportResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.AggregateFrameworkComplianceReportResponse)>` |   
  
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

### fetchFrameworkComplianceReport(@Nullable FrameworkComplianceReportName name)
    
    
    public final FrameworkComplianceReport fetchFrameworkComplianceReport(@Nullable FrameworkComplianceReportName name)

Fetches the framework compliance report for a given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MonitoringClient monitoringClient = MonitoringClient.create()) {
       FrameworkComplianceReportName name =
           FrameworkComplianceReportName.ofOrganizationLocationFrameworkComplianceReportName(
               "[ORGANIZATION]", "[LOCATION]", "[FRAMEWORK_COMPLIANCE_REPORT]");
       FrameworkComplianceReport response = monitoringClient.fetchFrameworkComplianceReport(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.FrameworkComplianceReportName`  
Required. The name of the framework compliance report to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[FrameworkComplianceReport](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.FrameworkComplianceReport)` |   
  
### fetchFrameworkComplianceReport(FetchFrameworkComplianceReportRequest request)
    
    
    public final FrameworkComplianceReport fetchFrameworkComplianceReport(FetchFrameworkComplianceReportRequest request)

Fetches the framework compliance report for a given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MonitoringClient monitoringClient = MonitoringClient.create()) {
       FetchFrameworkComplianceReportRequest request =
           FetchFrameworkComplianceReportRequest.newBuilder()
               .setName(
                   FrameworkComplianceReportName.ofOrganizationLocationFrameworkComplianceReportName(
                           "[ORGANIZATION]", "[LOCATION]", "[FRAMEWORK_COMPLIANCE_REPORT]")
                       .toString())
               .setEndTime(Timestamp.newBuilder().build())
               .setFilter("filter-1274492040")
               .build();
       FrameworkComplianceReport response = monitoringClient.fetchFrameworkComplianceReport(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchFrameworkComplianceReportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.FetchFrameworkComplianceReportRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FrameworkComplianceReport](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.FrameworkComplianceReport)` |   
  
### fetchFrameworkComplianceReport(String name)
    
    
    public final FrameworkComplianceReport fetchFrameworkComplianceReport(String name)

Fetches the framework compliance report for a given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MonitoringClient monitoringClient = MonitoringClient.create()) {
       String name =
           FrameworkComplianceReportName.ofProjectLocationFrameworkComplianceReportName(
                   "[PROJECT]", "[LOCATION]", "[FRAMEWORK_COMPLIANCE_REPORT]")
               .toString();
       FrameworkComplianceReport response = monitoringClient.fetchFrameworkComplianceReport(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the framework compliance report to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[FrameworkComplianceReport](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.FrameworkComplianceReport)` |   
  
### fetchFrameworkComplianceReportCallable()
    
    
    public final UnaryCallable<FetchFrameworkComplianceReportRequest,FrameworkComplianceReport> fetchFrameworkComplianceReportCallable()

Fetches the framework compliance report for a given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MonitoringClient monitoringClient = MonitoringClient.create()) {
       FetchFrameworkComplianceReportRequest request =
           FetchFrameworkComplianceReportRequest.newBuilder()
               .setName(
                   FrameworkComplianceReportName.ofOrganizationLocationFrameworkComplianceReportName(
                           "[ORGANIZATION]", "[LOCATION]", "[FRAMEWORK_COMPLIANCE_REPORT]")
                       .toString())
               .setEndTime(Timestamp.newBuilder().build())
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<FrameworkComplianceReport> future =
           monitoringClient.fetchFrameworkComplianceReportCallable().futureCall(request);
       // Do something.
       FrameworkComplianceReport response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchFrameworkComplianceReportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.FetchFrameworkComplianceReportRequest),[FrameworkComplianceReport](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.FrameworkComplianceReport)>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MonitoringClient monitoringClient = MonitoringClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = monitoringClient.getLocation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.cloud.location.GetLocationRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.location.Location` |   
  
### getLocationCallable()
    
    
    public final UnaryCallable<GetLocationRequest,Location> getLocationCallable()

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MonitoringClient monitoringClient = MonitoringClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = monitoringClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getSettings()
    
    
    public final @Nullable MonitoringSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.MonitoringSettings` |   
  
### getStub()
    
    
    public MonitoringStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[MonitoringStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.stub.MonitoringStub)` |   
  
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
  
### listControlComplianceSummaries(@Nullable FrameworkComplianceReportName parent)
    
    
    public final MonitoringClient.ListControlComplianceSummariesPagedResponse listControlComplianceSummaries(@Nullable FrameworkComplianceReportName parent)

Lists the control compliance summary for a given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MonitoringClient monitoringClient = MonitoringClient.create()) {
       FrameworkComplianceReportName parent =
           FrameworkComplianceReportName.ofOrganizationLocationFrameworkComplianceReportName(
               "[ORGANIZATION]", "[LOCATION]", "[FRAMEWORK_COMPLIANCE_REPORT]");
       for (ControlComplianceSummary element :
           monitoringClient.listControlComplianceSummaries(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.FrameworkComplianceReportName`  
Required. The parent scope for the framework overview page.  
**Returns**  
---  
**Type** | **Description**  
`[MonitoringClient.ListControlComplianceSummariesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.MonitoringClient.ListControlComplianceSummariesPagedResponse)` |   
  
### listControlComplianceSummaries(ListControlComplianceSummariesRequest request)
    
    
    public final MonitoringClient.ListControlComplianceSummariesPagedResponse listControlComplianceSummaries(ListControlComplianceSummariesRequest request)

Lists the control compliance summary for a given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MonitoringClient monitoringClient = MonitoringClient.create()) {
       ListControlComplianceSummariesRequest request =
           ListControlComplianceSummariesRequest.newBuilder()
               .setParent(
                   FrameworkComplianceReportName.ofOrganizationLocationFrameworkComplianceReportName(
                           "[ORGANIZATION]", "[LOCATION]", "[FRAMEWORK_COMPLIANCE_REPORT]")
                       .toString())
               .setEndTime(Timestamp.newBuilder().build())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (ControlComplianceSummary element :
           monitoringClient.listControlComplianceSummaries(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListControlComplianceSummariesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListControlComplianceSummariesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MonitoringClient.ListControlComplianceSummariesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.MonitoringClient.ListControlComplianceSummariesPagedResponse)` |   
  
### listControlComplianceSummaries(String parent)
    
    
    public final MonitoringClient.ListControlComplianceSummariesPagedResponse listControlComplianceSummaries(String parent)

Lists the control compliance summary for a given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MonitoringClient monitoringClient = MonitoringClient.create()) {
       String parent =
           FrameworkComplianceReportName.ofProjectLocationFrameworkComplianceReportName(
                   "[PROJECT]", "[LOCATION]", "[FRAMEWORK_COMPLIANCE_REPORT]")
               .toString();
       for (ControlComplianceSummary element :
           monitoringClient.listControlComplianceSummaries(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent scope for the framework overview page.  
**Returns**  
---  
**Type** | **Description**  
`[MonitoringClient.ListControlComplianceSummariesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.MonitoringClient.ListControlComplianceSummariesPagedResponse)` |   
  
### listControlComplianceSummariesCallable()
    
    
    public final UnaryCallable<ListControlComplianceSummariesRequest,ListControlComplianceSummariesResponse> listControlComplianceSummariesCallable()

Lists the control compliance summary for a given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MonitoringClient monitoringClient = MonitoringClient.create()) {
       ListControlComplianceSummariesRequest request =
           ListControlComplianceSummariesRequest.newBuilder()
               .setParent(
                   FrameworkComplianceReportName.ofOrganizationLocationFrameworkComplianceReportName(
                           "[ORGANIZATION]", "[LOCATION]", "[FRAMEWORK_COMPLIANCE_REPORT]")
                       .toString())
               .setEndTime(Timestamp.newBuilder().build())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListControlComplianceSummariesResponse response =
             monitoringClient.listControlComplianceSummariesCallable().call(request);
         for (ControlComplianceSummary element : response.getControlComplianceSummariesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListControlComplianceSummariesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListControlComplianceSummariesRequest),[ListControlComplianceSummariesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListControlComplianceSummariesResponse)>` |   
  
### listControlComplianceSummariesPagedCallable()
    
    
    public final UnaryCallable<ListControlComplianceSummariesRequest,MonitoringClient.ListControlComplianceSummariesPagedResponse> listControlComplianceSummariesPagedCallable()

Lists the control compliance summary for a given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MonitoringClient monitoringClient = MonitoringClient.create()) {
       ListControlComplianceSummariesRequest request =
           ListControlComplianceSummariesRequest.newBuilder()
               .setParent(
                   FrameworkComplianceReportName.ofOrganizationLocationFrameworkComplianceReportName(
                           "[ORGANIZATION]", "[LOCATION]", "[FRAMEWORK_COMPLIANCE_REPORT]")
                       .toString())
               .setEndTime(Timestamp.newBuilder().build())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<ControlComplianceSummary> future =
           monitoringClient.listControlComplianceSummariesPagedCallable().futureCall(request);
       // Do something.
       for (ControlComplianceSummary element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListControlComplianceSummariesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListControlComplianceSummariesRequest),[ListControlComplianceSummariesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.MonitoringClient.ListControlComplianceSummariesPagedResponse)>` |   
  
### listFindingSummaries(@Nullable FolderLocationName parent)
    
    
    public final MonitoringClient.ListFindingSummariesPagedResponse listFindingSummaries(@Nullable FolderLocationName parent)

Lists the finding summary by category for a given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MonitoringClient monitoringClient = MonitoringClient.create()) {
       FolderLocationName parent = FolderLocationName.of("[FOLDER]", "[LOCATION]");
       for (FindingSummary element : monitoringClient.listFindingSummaries(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.FolderLocationName`  
Required. The parent scope for the framework overview page.  
**Returns**  
---  
**Type** | **Description**  
`[MonitoringClient.ListFindingSummariesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.MonitoringClient.ListFindingSummariesPagedResponse)` |   
  
### listFindingSummaries(@Nullable LocationName parent)
    
    
    public final MonitoringClient.ListFindingSummariesPagedResponse listFindingSummaries(@Nullable LocationName parent)

Lists the finding summary by category for a given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MonitoringClient monitoringClient = MonitoringClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (FindingSummary element : monitoringClient.listFindingSummaries(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.LocationName`  
Required. The parent scope for the framework overview page.  
**Returns**  
---  
**Type** | **Description**  
`[MonitoringClient.ListFindingSummariesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.MonitoringClient.ListFindingSummariesPagedResponse)` |   
  
### listFindingSummaries(@Nullable OrganizationLocationName parent)
    
    
    public final MonitoringClient.ListFindingSummariesPagedResponse listFindingSummaries(@Nullable OrganizationLocationName parent)

Lists the finding summary by category for a given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MonitoringClient monitoringClient = MonitoringClient.create()) {
       OrganizationLocationName parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]");
       for (FindingSummary element : monitoringClient.listFindingSummaries(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.OrganizationLocationName`  
Required. The parent scope for the framework overview page.  
**Returns**  
---  
**Type** | **Description**  
`[MonitoringClient.ListFindingSummariesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.MonitoringClient.ListFindingSummariesPagedResponse)` |   
  
### listFindingSummaries(ListFindingSummariesRequest request)
    
    
    public final MonitoringClient.ListFindingSummariesPagedResponse listFindingSummaries(ListFindingSummariesRequest request)

Lists the finding summary by category for a given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MonitoringClient monitoringClient = MonitoringClient.create()) {
       ListFindingSummariesRequest request =
           ListFindingSummariesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setEndTime(Timestamp.newBuilder().build())
               .build();
       for (FindingSummary element : monitoringClient.listFindingSummaries(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListFindingSummariesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListFindingSummariesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MonitoringClient.ListFindingSummariesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.MonitoringClient.ListFindingSummariesPagedResponse)` |   
  
### listFindingSummaries(String parent)
    
    
    public final MonitoringClient.ListFindingSummariesPagedResponse listFindingSummaries(String parent)

Lists the finding summary by category for a given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MonitoringClient monitoringClient = MonitoringClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (FindingSummary element : monitoringClient.listFindingSummaries(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent scope for the framework overview page.  
**Returns**  
---  
**Type** | **Description**  
`[MonitoringClient.ListFindingSummariesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.MonitoringClient.ListFindingSummariesPagedResponse)` |   
  
### listFindingSummariesCallable()
    
    
    public final UnaryCallable<ListFindingSummariesRequest,ListFindingSummariesResponse> listFindingSummariesCallable()

Lists the finding summary by category for a given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MonitoringClient monitoringClient = MonitoringClient.create()) {
       ListFindingSummariesRequest request =
           ListFindingSummariesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setEndTime(Timestamp.newBuilder().build())
               .build();
       while (true) {
         ListFindingSummariesResponse response =
             monitoringClient.listFindingSummariesCallable().call(request);
         for (FindingSummary element : response.getFindingSummariesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFindingSummariesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListFindingSummariesRequest),[ListFindingSummariesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListFindingSummariesResponse)>` |   
  
### listFindingSummariesPagedCallable()
    
    
    public final UnaryCallable<ListFindingSummariesRequest,MonitoringClient.ListFindingSummariesPagedResponse> listFindingSummariesPagedCallable()

Lists the finding summary by category for a given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MonitoringClient monitoringClient = MonitoringClient.create()) {
       ListFindingSummariesRequest request =
           ListFindingSummariesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setEndTime(Timestamp.newBuilder().build())
               .build();
       ApiFuture<FindingSummary> future =
           monitoringClient.listFindingSummariesPagedCallable().futureCall(request);
       // Do something.
       for (FindingSummary element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFindingSummariesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListFindingSummariesRequest),[ListFindingSummariesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.MonitoringClient.ListFindingSummariesPagedResponse)>` |   
  
### listFrameworkComplianceSummaries(@Nullable FolderLocationName parent)
    
    
    public final MonitoringClient.ListFrameworkComplianceSummariesPagedResponse listFrameworkComplianceSummaries(@Nullable FolderLocationName parent)

Lists the framework compliance summary for a given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MonitoringClient monitoringClient = MonitoringClient.create()) {
       FolderLocationName parent = FolderLocationName.of("[FOLDER]", "[LOCATION]");
       for (FrameworkComplianceSummary element :
           monitoringClient.listFrameworkComplianceSummaries(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.FolderLocationName`  
Required. The parent scope for the framework compliance summary.  
**Returns**  
---  
**Type** | **Description**  
`[MonitoringClient.ListFrameworkComplianceSummariesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.MonitoringClient.ListFrameworkComplianceSummariesPagedResponse)` |   
  
### listFrameworkComplianceSummaries(@Nullable LocationName parent)
    
    
    public final MonitoringClient.ListFrameworkComplianceSummariesPagedResponse listFrameworkComplianceSummaries(@Nullable LocationName parent)

Lists the framework compliance summary for a given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MonitoringClient monitoringClient = MonitoringClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (FrameworkComplianceSummary element :
           monitoringClient.listFrameworkComplianceSummaries(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.LocationName`  
Required. The parent scope for the framework compliance summary.  
**Returns**  
---  
**Type** | **Description**  
`[MonitoringClient.ListFrameworkComplianceSummariesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.MonitoringClient.ListFrameworkComplianceSummariesPagedResponse)` |   
  
### listFrameworkComplianceSummaries(@Nullable OrganizationLocationName parent)
    
    
    public final MonitoringClient.ListFrameworkComplianceSummariesPagedResponse listFrameworkComplianceSummaries(@Nullable OrganizationLocationName parent)

Lists the framework compliance summary for a given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MonitoringClient monitoringClient = MonitoringClient.create()) {
       OrganizationLocationName parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]");
       for (FrameworkComplianceSummary element :
           monitoringClient.listFrameworkComplianceSummaries(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.OrganizationLocationName`  
Required. The parent scope for the framework compliance summary.  
**Returns**  
---  
**Type** | **Description**  
`[MonitoringClient.ListFrameworkComplianceSummariesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.MonitoringClient.ListFrameworkComplianceSummariesPagedResponse)` |   
  
### listFrameworkComplianceSummaries(ListFrameworkComplianceSummariesRequest request)
    
    
    public final MonitoringClient.ListFrameworkComplianceSummariesPagedResponse listFrameworkComplianceSummaries(ListFrameworkComplianceSummariesRequest request)

Lists the framework compliance summary for a given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MonitoringClient monitoringClient = MonitoringClient.create()) {
       ListFrameworkComplianceSummariesRequest request =
           ListFrameworkComplianceSummariesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setView(FrameworkComplianceSummaryView.forNumber(0))
               .build();
       for (FrameworkComplianceSummary element :
           monitoringClient.listFrameworkComplianceSummaries(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListFrameworkComplianceSummariesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListFrameworkComplianceSummariesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MonitoringClient.ListFrameworkComplianceSummariesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.MonitoringClient.ListFrameworkComplianceSummariesPagedResponse)` |   
  
### listFrameworkComplianceSummaries(String parent)
    
    
    public final MonitoringClient.ListFrameworkComplianceSummariesPagedResponse listFrameworkComplianceSummaries(String parent)

Lists the framework compliance summary for a given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MonitoringClient monitoringClient = MonitoringClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (FrameworkComplianceSummary element :
           monitoringClient.listFrameworkComplianceSummaries(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent scope for the framework compliance summary.  
**Returns**  
---  
**Type** | **Description**  
`[MonitoringClient.ListFrameworkComplianceSummariesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.MonitoringClient.ListFrameworkComplianceSummariesPagedResponse)` |   
  
### listFrameworkComplianceSummariesCallable()
    
    
    public final UnaryCallable<ListFrameworkComplianceSummariesRequest,ListFrameworkComplianceSummariesResponse> listFrameworkComplianceSummariesCallable()

Lists the framework compliance summary for a given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MonitoringClient monitoringClient = MonitoringClient.create()) {
       ListFrameworkComplianceSummariesRequest request =
           ListFrameworkComplianceSummariesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setView(FrameworkComplianceSummaryView.forNumber(0))
               .build();
       while (true) {
         ListFrameworkComplianceSummariesResponse response =
             monitoringClient.listFrameworkComplianceSummariesCallable().call(request);
         for (FrameworkComplianceSummary element : response.getFrameworkComplianceSummariesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFrameworkComplianceSummariesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListFrameworkComplianceSummariesRequest),[ListFrameworkComplianceSummariesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListFrameworkComplianceSummariesResponse)>` |   
  
### listFrameworkComplianceSummariesPagedCallable()
    
    
    public final UnaryCallable<ListFrameworkComplianceSummariesRequest,MonitoringClient.ListFrameworkComplianceSummariesPagedResponse> listFrameworkComplianceSummariesPagedCallable()

Lists the framework compliance summary for a given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MonitoringClient monitoringClient = MonitoringClient.create()) {
       ListFrameworkComplianceSummariesRequest request =
           ListFrameworkComplianceSummariesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setView(FrameworkComplianceSummaryView.forNumber(0))
               .build();
       ApiFuture<FrameworkComplianceSummary> future =
           monitoringClient.listFrameworkComplianceSummariesPagedCallable().futureCall(request);
       // Do something.
       for (FrameworkComplianceSummary element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFrameworkComplianceSummariesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListFrameworkComplianceSummariesRequest),[ListFrameworkComplianceSummariesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.MonitoringClient.ListFrameworkComplianceSummariesPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final MonitoringClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MonitoringClient monitoringClient = MonitoringClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : monitoringClient.listLocations(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.cloud.location.ListLocationsRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MonitoringClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.MonitoringClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MonitoringClient monitoringClient = MonitoringClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = monitoringClient.listLocationsCallable().call(request);
         for (Location element : response.getLocationsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse>` |   
  
### listLocationsPagedCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,MonitoringClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MonitoringClient monitoringClient = MonitoringClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           monitoringClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.MonitoringClient.ListLocationsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
