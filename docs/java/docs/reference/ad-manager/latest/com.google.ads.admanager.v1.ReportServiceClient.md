---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ReportServiceClient
title: Class ReportServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:09:00.893240+00:00
---

# Class ReportServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ReportServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ReportServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/ReportServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for interacting with reports.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReportServiceClient reportServiceClient = ReportServiceClient.create()) {
       ReportName name = ReportName.of("[NETWORK_CODE]", "[REPORT]");
       Report response = reportServiceClient.getReport(name);
     }
     

Note: close() needs to be called on the ReportServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetReport |  Retrieves a `Report` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getReport(GetReportRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getReport(ReportName name) 
  * getReport(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getReportCallable() 

  
ListReports |  Lists `Report` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listReports(ListReportsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listReports(NetworkName parent) 
  * listReports(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listReportsPagedCallable() 
  * listReportsCallable() 

  
CreateReport |  Creates a `Report` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createReport(CreateReportRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createReport(NetworkName parent, Report report) 
  * createReport(String parent, Report report) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createReportCallable() 

  
UpdateReport |  Updates a `Report` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateReport(UpdateReportRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateReport(Report report, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateReportCallable() 

  
RunReport |  Initiates the execution of an existing report asynchronously. Users can get the report by polling this operation using `OperationsService.GetOperation`. Poll every 5 seconds initially, with an exponential backoff. Once a report is complete, the operation will contain a `RunReportResponse` in its response field containing a report_result that can be passed to the `FetchReportResultRows` method to retrieve the report data. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * runReportAsync(RunReportRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * runReportAsync(ReportName name) 
  * runReportAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * runReportOperationCallable() 
  * runReportCallable() 

  
FetchReportResultRows |  Returns the result rows from a completed report. The caller must have previously called `RunReport` and waited for that operation to complete. The rows will be returned according to the order specified by the `sorts` member of the report definition. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * fetchReportResultRows(FetchReportResultRowsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * fetchReportResultRows(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * fetchReportResultRowsPagedCallable() 
  * fetchReportResultRowsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of ReportServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ReportServiceSettings reportServiceSettings =
         ReportServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ReportServiceClient reportServiceClient = ReportServiceClient.create(reportServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ReportServiceSettings reportServiceSettings =
         ReportServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     ReportServiceClient reportServiceClient = ReportServiceClient.create(reportServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ReportServiceClient

## Static Methods 

### create()
    
    
    public static final ReportServiceClient create()

Constructs an instance of ReportServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ReportServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ReportServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ReportServiceSettings settings)
    
    
    public static final ReportServiceClient create(ReportServiceSettings settings)

Constructs an instance of ReportServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ReportServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ReportServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReportServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ReportServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ReportServiceStub stub)
    
    
    public static final ReportServiceClient create(ReportServiceStub stub)

Constructs an instance of ReportServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(ReportServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ReportServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ReportServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReportServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ReportServiceClient)` |   
  
## Constructors 

### ReportServiceClient(ReportServiceSettings settings)
    
    
    protected ReportServiceClient(ReportServiceSettings settings)

Constructs an instance of ReportServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ReportServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ReportServiceSettings)`  
  
  
### ReportServiceClient(ReportServiceStub stub)
    
    
    protected ReportServiceClient(ReportServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ReportServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ReportServiceStub)`  
  
  
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

### createReport(@Nullable NetworkName parent, Report report)
    
    
    public final Report createReport(@Nullable NetworkName parent, Report report)

Creates a `Report` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReportServiceClient reportServiceClient = ReportServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       Report report = Report.newBuilder().build();
       Report response = reportServiceClient.createReport(parent, report);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where this `Report` will be created. Format: `networks/{network_code}`  
`report` | `[Report](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Report)`  
Required. The `Report` to create.  
**Returns**  
---  
**Type** | **Description**  
`[Report](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Report)` |   
  
### createReport(CreateReportRequest request)
    
    
    public final Report createReport(CreateReportRequest request)

Creates a `Report` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReportServiceClient reportServiceClient = ReportServiceClient.create()) {
       CreateReportRequest request =
           CreateReportRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setReport(Report.newBuilder().build())
               .build();
       Report response = reportServiceClient.createReport(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateReportRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateReportRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Report](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Report)` |   
  
### createReport(String parent, Report report)
    
    
    public final Report createReport(String parent, Report report)

Creates a `Report` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReportServiceClient reportServiceClient = ReportServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       Report report = Report.newBuilder().build();
       Report response = reportServiceClient.createReport(parent, report);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this `Report` will be created. Format: `networks/{network_code}`  
`report` | `[Report](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Report)`  
Required. The `Report` to create.  
**Returns**  
---  
**Type** | **Description**  
`[Report](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Report)` |   
  
### createReportCallable()
    
    
    public final UnaryCallable<CreateReportRequest,Report> createReportCallable()

Creates a `Report` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReportServiceClient reportServiceClient = ReportServiceClient.create()) {
       CreateReportRequest request =
           CreateReportRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setReport(Report.newBuilder().build())
               .build();
       ApiFuture<Report> future = reportServiceClient.createReportCallable().futureCall(request);
       // Do something.
       Report response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateReportRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateReportRequest),[Report](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Report)>` |   
  
### fetchReportResultRows(FetchReportResultRowsRequest request)
    
    
    public final ReportServiceClient.FetchReportResultRowsPagedResponse fetchReportResultRows(FetchReportResultRowsRequest request)

Returns the result rows from a completed report. The caller must have previously called `RunReport` and waited for that operation to complete. The rows will be returned according to the order specified by the `sorts` member of the report definition.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReportServiceClient reportServiceClient = ReportServiceClient.create()) {
       FetchReportResultRowsRequest request =
           FetchReportResultRowsRequest.newBuilder()
               .setName("name3373707")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (ReportDataTable.Row element :
           reportServiceClient.fetchReportResultRows(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchReportResultRowsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.FetchReportResultRowsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ReportServiceClient.FetchReportResultRowsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ReportServiceClient.FetchReportResultRowsPagedResponse)` |   
  
### fetchReportResultRows(String name)
    
    
    public final ReportServiceClient.FetchReportResultRowsPagedResponse fetchReportResultRows(String name)

Returns the result rows from a completed report. The caller must have previously called `RunReport` and waited for that operation to complete. The rows will be returned according to the order specified by the `sorts` member of the report definition.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReportServiceClient reportServiceClient = ReportServiceClient.create()) {
       String name = "name3373707";
       for (ReportDataTable.Row element :
           reportServiceClient.fetchReportResultRows(name).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The report result being fetched. Format: `networks/{network_code}/reports/{report_id}/results/{report_result_id}`  
**Returns**  
---  
**Type** | **Description**  
`[ReportServiceClient.FetchReportResultRowsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ReportServiceClient.FetchReportResultRowsPagedResponse)` |   
  
### fetchReportResultRowsCallable()
    
    
    public final UnaryCallable<FetchReportResultRowsRequest,FetchReportResultRowsResponse> fetchReportResultRowsCallable()

Returns the result rows from a completed report. The caller must have previously called `RunReport` and waited for that operation to complete. The rows will be returned according to the order specified by the `sorts` member of the report definition.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReportServiceClient reportServiceClient = ReportServiceClient.create()) {
       FetchReportResultRowsRequest request =
           FetchReportResultRowsRequest.newBuilder()
               .setName("name3373707")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         FetchReportResultRowsResponse response =
             reportServiceClient.fetchReportResultRowsCallable().call(request);
         for (ReportDataTable.Row element : response.getRowsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchReportResultRowsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.FetchReportResultRowsRequest),[FetchReportResultRowsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.FetchReportResultRowsResponse)>` |   
  
### fetchReportResultRowsPagedCallable()
    
    
    public final UnaryCallable<FetchReportResultRowsRequest,ReportServiceClient.FetchReportResultRowsPagedResponse> fetchReportResultRowsPagedCallable()

Returns the result rows from a completed report. The caller must have previously called `RunReport` and waited for that operation to complete. The rows will be returned according to the order specified by the `sorts` member of the report definition.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReportServiceClient reportServiceClient = ReportServiceClient.create()) {
       FetchReportResultRowsRequest request =
           FetchReportResultRowsRequest.newBuilder()
               .setName("name3373707")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<ReportDataTable.Row> future =
           reportServiceClient.fetchReportResultRowsPagedCallable().futureCall(request);
       // Do something.
       for (ReportDataTable.Row element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchReportResultRowsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.FetchReportResultRowsRequest),[FetchReportResultRowsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ReportServiceClient.FetchReportResultRowsPagedResponse)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getReport(@Nullable ReportName name)
    
    
    public final Report getReport(@Nullable ReportName name)

Retrieves a `Report` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReportServiceClient reportServiceClient = ReportServiceClient.create()) {
       ReportName name = ReportName.of("[NETWORK_CODE]", "[REPORT]");
       Report response = reportServiceClient.getReport(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.ReportName`  
Required. The resource name of the report. Format: `networks/{network_code}/reports/{report_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Report](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Report)` |   
  
### getReport(GetReportRequest request)
    
    
    public final Report getReport(GetReportRequest request)

Retrieves a `Report` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReportServiceClient reportServiceClient = ReportServiceClient.create()) {
       GetReportRequest request =
           GetReportRequest.newBuilder()
               .setName(ReportName.of("[NETWORK_CODE]", "[REPORT]").toString())
               .build();
       Report response = reportServiceClient.getReport(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetReportRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetReportRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Report](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Report)` |   
  
### getReport(String name)
    
    
    public final Report getReport(String name)

Retrieves a `Report` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReportServiceClient reportServiceClient = ReportServiceClient.create()) {
       String name = ReportName.of("[NETWORK_CODE]", "[REPORT]").toString();
       Report response = reportServiceClient.getReport(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the report. Format: `networks/{network_code}/reports/{report_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Report](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Report)` |   
  
### getReportCallable()
    
    
    public final UnaryCallable<GetReportRequest,Report> getReportCallable()

Retrieves a `Report` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReportServiceClient reportServiceClient = ReportServiceClient.create()) {
       GetReportRequest request =
           GetReportRequest.newBuilder()
               .setName(ReportName.of("[NETWORK_CODE]", "[REPORT]").toString())
               .build();
       ApiFuture<Report> future = reportServiceClient.getReportCallable().futureCall(request);
       // Do something.
       Report response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetReportRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetReportRequest),[Report](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Report)>` |   
  
### getSettings()
    
    
    public final @Nullable ReportServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.ReportServiceSettings` |   
  
### getStub()
    
    
    public ReportServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ReportServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ReportServiceStub)` |   
  
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
  
### listReports(@Nullable NetworkName parent)
    
    
    public final ReportServiceClient.ListReportsPagedResponse listReports(@Nullable NetworkName parent)

Lists `Report` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReportServiceClient reportServiceClient = ReportServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (Report element : reportServiceClient.listReports(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of reports. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[ReportServiceClient.ListReportsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ReportServiceClient.ListReportsPagedResponse)` |   
  
### listReports(ListReportsRequest request)
    
    
    public final ReportServiceClient.ListReportsPagedResponse listReports(ListReportsRequest request)

Lists `Report` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReportServiceClient reportServiceClient = ReportServiceClient.create()) {
       ListReportsRequest request =
           ListReportsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (Report element : reportServiceClient.listReports(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListReportsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListReportsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ReportServiceClient.ListReportsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ReportServiceClient.ListReportsPagedResponse)` |   
  
### listReports(String parent)
    
    
    public final ReportServiceClient.ListReportsPagedResponse listReports(String parent)

Lists `Report` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReportServiceClient reportServiceClient = ReportServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (Report element : reportServiceClient.listReports(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of reports. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[ReportServiceClient.ListReportsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ReportServiceClient.ListReportsPagedResponse)` |   
  
### listReportsCallable()
    
    
    public final UnaryCallable<ListReportsRequest,ListReportsResponse> listReportsCallable()

Lists `Report` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReportServiceClient reportServiceClient = ReportServiceClient.create()) {
       ListReportsRequest request =
           ListReportsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListReportsResponse response = reportServiceClient.listReportsCallable().call(request);
         for (Report element : response.getReportsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListReportsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListReportsRequest),[ListReportsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListReportsResponse)>` |   
  
### listReportsPagedCallable()
    
    
    public final UnaryCallable<ListReportsRequest,ReportServiceClient.ListReportsPagedResponse> listReportsPagedCallable()

Lists `Report` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReportServiceClient reportServiceClient = ReportServiceClient.create()) {
       ListReportsRequest request =
           ListReportsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<Report> future = reportServiceClient.listReportsPagedCallable().futureCall(request);
       // Do something.
       for (Report element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListReportsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListReportsRequest),[ListReportsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ReportServiceClient.ListReportsPagedResponse)>` |   
  
### runReportAsync(@Nullable ReportName name)
    
    
    public final OperationFuture<RunReportResponse,RunReportMetadata> runReportAsync(@Nullable ReportName name)

Initiates the execution of an existing report asynchronously. Users can get the report by polling this operation using `OperationsService.GetOperation`. Poll every 5 seconds initially, with an exponential backoff. Once a report is complete, the operation will contain a `RunReportResponse` in its response field containing a report_result that can be passed to the `FetchReportResultRows` method to retrieve the report data.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReportServiceClient reportServiceClient = ReportServiceClient.create()) {
       ReportName name = ReportName.of("[NETWORK_CODE]", "[REPORT]");
       RunReportResponse response = reportServiceClient.runReportAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.ReportName`  
Required. The report to run. Format: `networks/{network_code}/reports/{report_id}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RunReportResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.RunReportResponse),[RunReportMetadata](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.RunReportMetadata)>` |   
  
### runReportAsync(RunReportRequest request)
    
    
    public final OperationFuture<RunReportResponse,RunReportMetadata> runReportAsync(RunReportRequest request)

Initiates the execution of an existing report asynchronously. Users can get the report by polling this operation using `OperationsService.GetOperation`. Poll every 5 seconds initially, with an exponential backoff. Once a report is complete, the operation will contain a `RunReportResponse` in its response field containing a report_result that can be passed to the `FetchReportResultRows` method to retrieve the report data.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReportServiceClient reportServiceClient = ReportServiceClient.create()) {
       RunReportRequest request =
           RunReportRequest.newBuilder()
               .setName(ReportName.of("[NETWORK_CODE]", "[REPORT]").toString())
               .build();
       RunReportResponse response = reportServiceClient.runReportAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RunReportRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.RunReportRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RunReportResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.RunReportResponse),[RunReportMetadata](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.RunReportMetadata)>` |   
  
### runReportAsync(String name)
    
    
    public final OperationFuture<RunReportResponse,RunReportMetadata> runReportAsync(String name)

Initiates the execution of an existing report asynchronously. Users can get the report by polling this operation using `OperationsService.GetOperation`. Poll every 5 seconds initially, with an exponential backoff. Once a report is complete, the operation will contain a `RunReportResponse` in its response field containing a report_result that can be passed to the `FetchReportResultRows` method to retrieve the report data.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReportServiceClient reportServiceClient = ReportServiceClient.create()) {
       String name = ReportName.of("[NETWORK_CODE]", "[REPORT]").toString();
       RunReportResponse response = reportServiceClient.runReportAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The report to run. Format: `networks/{network_code}/reports/{report_id}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RunReportResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.RunReportResponse),[RunReportMetadata](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.RunReportMetadata)>` |   
  
### runReportCallable()
    
    
    public final UnaryCallable<RunReportRequest,Operation> runReportCallable()

Initiates the execution of an existing report asynchronously. Users can get the report by polling this operation using `OperationsService.GetOperation`. Poll every 5 seconds initially, with an exponential backoff. Once a report is complete, the operation will contain a `RunReportResponse` in its response field containing a report_result that can be passed to the `FetchReportResultRows` method to retrieve the report data.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReportServiceClient reportServiceClient = ReportServiceClient.create()) {
       RunReportRequest request =
           RunReportRequest.newBuilder()
               .setName(ReportName.of("[NETWORK_CODE]", "[REPORT]").toString())
               .build();
       ApiFuture<Operation> future = reportServiceClient.runReportCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RunReportRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.RunReportRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### runReportOperationCallable()
    
    
    public final OperationCallable<RunReportRequest,RunReportResponse,RunReportMetadata> runReportOperationCallable()

Initiates the execution of an existing report asynchronously. Users can get the report by polling this operation using `OperationsService.GetOperation`. Poll every 5 seconds initially, with an exponential backoff. Once a report is complete, the operation will contain a `RunReportResponse` in its response field containing a report_result that can be passed to the `FetchReportResultRows` method to retrieve the report data.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReportServiceClient reportServiceClient = ReportServiceClient.create()) {
       RunReportRequest request =
           RunReportRequest.newBuilder()
               .setName(ReportName.of("[NETWORK_CODE]", "[REPORT]").toString())
               .build();
       OperationFuture<RunReportResponse, RunReportMetadata> future =
           reportServiceClient.runReportOperationCallable().futureCall(request);
       // Do something.
       RunReportResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RunReportRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.RunReportRequest),[RunReportResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.RunReportResponse),[RunReportMetadata](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.RunReportMetadata)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateReport(Report report, FieldMask updateMask)
    
    
    public final Report updateReport(Report report, FieldMask updateMask)

Updates a `Report` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReportServiceClient reportServiceClient = ReportServiceClient.create()) {
       Report report = Report.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Report response = reportServiceClient.updateReport(report, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`report` | `[Report](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Report)`  
Required. The `Report` to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[Report](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Report)` |   
  
### updateReport(UpdateReportRequest request)
    
    
    public final Report updateReport(UpdateReportRequest request)

Updates a `Report` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReportServiceClient reportServiceClient = ReportServiceClient.create()) {
       UpdateReportRequest request =
           UpdateReportRequest.newBuilder()
               .setReport(Report.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Report response = reportServiceClient.updateReport(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateReportRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateReportRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Report](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Report)` |   
  
### updateReportCallable()
    
    
    public final UnaryCallable<UpdateReportRequest,Report> updateReportCallable()

Updates a `Report` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReportServiceClient reportServiceClient = ReportServiceClient.create()) {
       UpdateReportRequest request =
           UpdateReportRequest.newBuilder()
               .setReport(Report.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Report> future = reportServiceClient.updateReportCallable().futureCall(request);
       // Do something.
       Report response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateReportRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateReportRequest),[Report](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Report)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
