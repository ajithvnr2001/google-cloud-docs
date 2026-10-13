---
url: https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.BetaAnalyticsDataClient
title: Class BetaAnalyticsDataClient (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:10:37.174172+00:00
---

# Class BetaAnalyticsDataClient (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.BetaAnalyticsDataClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class BetaAnalyticsDataClient (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-analytics-data/google-analytics-data/src/main/java/com/google/analytics/data/v1beta/BetaAnalyticsDataClient.java)| [Product Reference](https://developers.google.com/analytics/trusted-testing/analytics-data)  
---|---  
  
Service Description: Google Analytics reporting data service.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BetaAnalyticsDataClient betaAnalyticsDataClient = BetaAnalyticsDataClient.create()) {
       RunReportRequest request =
           RunReportRequest.newBuilder()
               .setProperty("property-993141291")
               .addAllDimensions(new ArrayList<Dimension>())
               .addAllMetrics(new ArrayList<Metric>())
               .addAllDateRanges(new ArrayList<DateRange>())
               .setDimensionFilter(FilterExpression.newBuilder().build())
               .setMetricFilter(FilterExpression.newBuilder().build())
               .setOffset(-1019779949)
               .setLimit(102976443)
               .addAllMetricAggregations(new ArrayList<MetricAggregation>())
               .addAllOrderBys(new ArrayList<OrderBy>())
               .setCurrencyCode("currencyCode1004773790")
               .setCohortSpec(CohortSpec.newBuilder().build())
               .setKeepEmptyRows(true)
               .setReturnPropertyQuota(true)
               .addAllComparisons(new ArrayList<Comparison>())
               .build();
       RunReportResponse response = betaAnalyticsDataClient.runReport(request);
     }
     

Note: close() needs to be called on the BetaAnalyticsDataClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
RunReport |  Returns a customized report of your Google Analytics event data. Reports contain statistics derived from data collected by the Google Analytics tracking code. The data returned from the API is as a table with columns for the requested dimensions and metrics. Metrics are individual measurements of user activity on your property, such as active users or event count. Dimensions break down metrics across some common criteria, such as country or event name.  For a guide to constructing requests & understanding responses, see [Creating a Report](https://developers.google.com/analytics/devguides/reporting/data/v1/basics). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * runReport(RunReportRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * runReportCallable() 

  
RunPivotReport |  Returns a customized pivot report of your Google Analytics event data. Pivot reports are more advanced and expressive formats than regular reports. In a pivot report, dimensions are only visible if they are included in a pivot. Multiple pivots can be specified to further dissect your data. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * runPivotReport(RunPivotReportRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * runPivotReportCallable() 

  
BatchRunReports |  Returns multiple reports in a batch. All reports must be for the same Google Analytics property. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchRunReports(BatchRunReportsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchRunReportsCallable() 

  
BatchRunPivotReports |  Returns multiple pivot reports in a batch. All reports must be for the same Google Analytics property. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchRunPivotReports(BatchRunPivotReportsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchRunPivotReportsCallable() 

  
GetMetadata |  Returns metadata for dimensions and metrics available in reporting methods. Used to explore the dimensions and metrics. In this method, a Google Analytics property identifier is specified in the request, and the metadata response includes Custom dimensions and metrics as well as Universal metadata.  For example if a custom metric with parameter name `levels_unlocked` is registered to a property, the Metadata response will contain `customEvent:levels_unlocked`. Universal metadata are dimensions and metrics applicable to any property such as `country` and `totalUsers`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getMetadata(GetMetadataRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getMetadata(MetadataName name) 
  * getMetadata(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getMetadataCallable() 

  
RunRealtimeReport |  Returns a customized report of realtime event data for your property. Events appear in realtime reports seconds after they have been sent to the Google Analytics. Realtime reports show events and usage data for the periods of time ranging from the present moment to 30 minutes ago (up to 60 minutes for Google Analytics 360 properties).  For a guide to constructing realtime requests & understanding responses, see [Creating a Realtime Report](https://developers.google.com/analytics/devguides/reporting/data/v1/realtime-basics). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * runRealtimeReport(RunRealtimeReportRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * runRealtimeReportCallable() 

  
CheckCompatibility |  This compatibility method lists dimensions and metrics that can be added to a report request and maintain compatibility. This method fails if the request's dimensions and metrics are incompatible.  In Google Analytics, reports fail if they request incompatible dimensions and/or metrics; in that case, you will need to remove dimensions and/or metrics from the incompatible report until the report is compatible.  The Realtime and Core reports have different compatibility rules. This method checks compatibility for Core reports. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * checkCompatibility(CheckCompatibilityRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * checkCompatibilityCallable() 

  
CreateAudienceExport |  Creates an audience export for later retrieval. This method quickly returns the audience export's resource name and initiates a long running asynchronous request to form an audience export. To export the users in an audience export, first create the audience export through this method and then send the audience resource name to the `QueryAudienceExport` method.  See [Creating an Audience Export](https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics) for an introduction to Audience Exports with examples.  An audience export is a snapshot of the users currently in the audience at the time of audience export creation. Creating audience exports for one audience on different days will return different results as users enter and exit the audience.  Audiences in Google Analytics 4 allow you to segment your users in the ways that are important to your business. To learn more, see <https://support.google.com/analytics/answer/9267572>. Audience exports contain the users in each audience.  Audience Export APIs have some methods at alpha and other methods at beta stability. The intention is to advance methods to beta stability after some feedback and adoption. To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](https://forms.gle/EeA5u5LW6PEggtCEA) form. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createAudienceExportAsync(CreateAudienceExportRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createAudienceExportAsync(PropertyName parent, AudienceExport audienceExport) 
  * createAudienceExportAsync(String parent, AudienceExport audienceExport) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createAudienceExportOperationCallable() 
  * createAudienceExportCallable() 

  
QueryAudienceExport |  Retrieves an audience export of users. After creating an audience, the users are not immediately available for exporting. First, a request to `CreateAudienceExport` is necessary to create an audience export of users, and then second, this method is used to retrieve the users in the audience export.  See [Creating an Audience Export](https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics) for an introduction to Audience Exports with examples.  Audiences in Google Analytics 4 allow you to segment your users in the ways that are important to your business. To learn more, see <https://support.google.com/analytics/answer/9267572>.  Audience Export APIs have some methods at alpha and other methods at beta stability. The intention is to advance methods to beta stability after some feedback and adoption. To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](https://forms.gle/EeA5u5LW6PEggtCEA) form. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * queryAudienceExport(QueryAudienceExportRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * queryAudienceExport(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * queryAudienceExportCallable() 

  
GetAudienceExport |  Gets configuration metadata about a specific audience export. This method can be used to understand an audience export after it has been created.  See [Creating an Audience Export](https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics) for an introduction to Audience Exports with examples.  Audience Export APIs have some methods at alpha and other methods at beta stability. The intention is to advance methods to beta stability after some feedback and adoption. To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](https://forms.gle/EeA5u5LW6PEggtCEA) form. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAudienceExport(GetAudienceExportRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAudienceExport(AudienceExportName name) 
  * getAudienceExport(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAudienceExportCallable() 

  
ListAudienceExports |  Lists all audience exports for a property. This method can be used for you to find and reuse existing audience exports rather than creating unnecessary new audience exports. The same audience can have multiple audience exports that represent the export of users that were in an audience on different days.  See [Creating an Audience Export](https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics) for an introduction to Audience Exports with examples.  Audience Export APIs have some methods at alpha and other methods at beta stability. The intention is to advance methods to beta stability after some feedback and adoption. To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](https://forms.gle/EeA5u5LW6PEggtCEA) form. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listAudienceExports(ListAudienceExportsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listAudienceExports(PropertyName parent) 
  * listAudienceExports(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listAudienceExportsPagedCallable() 
  * listAudienceExportsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of BetaAnalyticsDataSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     BetaAnalyticsDataSettings betaAnalyticsDataSettings =
         BetaAnalyticsDataSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     BetaAnalyticsDataClient betaAnalyticsDataClient =
         BetaAnalyticsDataClient.create(betaAnalyticsDataSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     BetaAnalyticsDataSettings betaAnalyticsDataSettings =
         BetaAnalyticsDataSettings.newBuilder().setEndpoint(myEndpoint).build();
     BetaAnalyticsDataClient betaAnalyticsDataClient =
         BetaAnalyticsDataClient.create(betaAnalyticsDataSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     BetaAnalyticsDataSettings betaAnalyticsDataSettings =
         BetaAnalyticsDataSettings.newHttpJsonBuilder().build();
     BetaAnalyticsDataClient betaAnalyticsDataClient =
         BetaAnalyticsDataClient.create(betaAnalyticsDataSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > BetaAnalyticsDataClient

## Static Methods 

### create()
    
    
    public static final BetaAnalyticsDataClient create()

Constructs an instance of BetaAnalyticsDataClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[BetaAnalyticsDataClient](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.BetaAnalyticsDataClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(BetaAnalyticsDataSettings settings)
    
    
    public static final BetaAnalyticsDataClient create(BetaAnalyticsDataSettings settings)

Constructs an instance of BetaAnalyticsDataClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[BetaAnalyticsDataSettings](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.BetaAnalyticsDataSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BetaAnalyticsDataClient](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.BetaAnalyticsDataClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(BetaAnalyticsDataStub stub)
    
    
    public static final BetaAnalyticsDataClient create(BetaAnalyticsDataStub stub)

Constructs an instance of BetaAnalyticsDataClient, using the given stub for making calls. This is for advanced usage - prefer using create(BetaAnalyticsDataSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[BetaAnalyticsDataStub](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.stub.BetaAnalyticsDataStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BetaAnalyticsDataClient](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.BetaAnalyticsDataClient)` |   
  
## Constructors 

### BetaAnalyticsDataClient(BetaAnalyticsDataSettings settings)
    
    
    protected BetaAnalyticsDataClient(BetaAnalyticsDataSettings settings)

Constructs an instance of BetaAnalyticsDataClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[BetaAnalyticsDataSettings](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.BetaAnalyticsDataSettings)`  
  
  
### BetaAnalyticsDataClient(BetaAnalyticsDataStub stub)
    
    
    protected BetaAnalyticsDataClient(BetaAnalyticsDataStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[BetaAnalyticsDataStub](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.stub.BetaAnalyticsDataStub)`  
  
  
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
  
### batchRunPivotReports(BatchRunPivotReportsRequest request)
    
    
    public final BatchRunPivotReportsResponse batchRunPivotReports(BatchRunPivotReportsRequest request)

Returns multiple pivot reports in a batch. All reports must be for the same Google Analytics property.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BetaAnalyticsDataClient betaAnalyticsDataClient = BetaAnalyticsDataClient.create()) {
       BatchRunPivotReportsRequest request =
           BatchRunPivotReportsRequest.newBuilder()
               .setProperty("property-993141291")
               .addAllRequests(new ArrayList<RunPivotReportRequest>())
               .build();
       BatchRunPivotReportsResponse response = betaAnalyticsDataClient.batchRunPivotReports(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchRunPivotReportsRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.BatchRunPivotReportsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchRunPivotReportsResponse](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.BatchRunPivotReportsResponse)` |   
  
### batchRunPivotReportsCallable()
    
    
    public final UnaryCallable<BatchRunPivotReportsRequest,BatchRunPivotReportsResponse> batchRunPivotReportsCallable()

Returns multiple pivot reports in a batch. All reports must be for the same Google Analytics property.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BetaAnalyticsDataClient betaAnalyticsDataClient = BetaAnalyticsDataClient.create()) {
       BatchRunPivotReportsRequest request =
           BatchRunPivotReportsRequest.newBuilder()
               .setProperty("property-993141291")
               .addAllRequests(new ArrayList<RunPivotReportRequest>())
               .build();
       ApiFuture<BatchRunPivotReportsResponse> future =
           betaAnalyticsDataClient.batchRunPivotReportsCallable().futureCall(request);
       // Do something.
       BatchRunPivotReportsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchRunPivotReportsRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.BatchRunPivotReportsRequest),[BatchRunPivotReportsResponse](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.BatchRunPivotReportsResponse)>` |   
  
### batchRunReports(BatchRunReportsRequest request)
    
    
    public final BatchRunReportsResponse batchRunReports(BatchRunReportsRequest request)

Returns multiple reports in a batch. All reports must be for the same Google Analytics property.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BetaAnalyticsDataClient betaAnalyticsDataClient = BetaAnalyticsDataClient.create()) {
       BatchRunReportsRequest request =
           BatchRunReportsRequest.newBuilder()
               .setProperty("property-993141291")
               .addAllRequests(new ArrayList<RunReportRequest>())
               .build();
       BatchRunReportsResponse response = betaAnalyticsDataClient.batchRunReports(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchRunReportsRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.BatchRunReportsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchRunReportsResponse](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.BatchRunReportsResponse)` |   
  
### batchRunReportsCallable()
    
    
    public final UnaryCallable<BatchRunReportsRequest,BatchRunReportsResponse> batchRunReportsCallable()

Returns multiple reports in a batch. All reports must be for the same Google Analytics property.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BetaAnalyticsDataClient betaAnalyticsDataClient = BetaAnalyticsDataClient.create()) {
       BatchRunReportsRequest request =
           BatchRunReportsRequest.newBuilder()
               .setProperty("property-993141291")
               .addAllRequests(new ArrayList<RunReportRequest>())
               .build();
       ApiFuture<BatchRunReportsResponse> future =
           betaAnalyticsDataClient.batchRunReportsCallable().futureCall(request);
       // Do something.
       BatchRunReportsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchRunReportsRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.BatchRunReportsRequest),[BatchRunReportsResponse](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.BatchRunReportsResponse)>` |   
  
### checkCompatibility(CheckCompatibilityRequest request)
    
    
    public final CheckCompatibilityResponse checkCompatibility(CheckCompatibilityRequest request)

This compatibility method lists dimensions and metrics that can be added to a report request and maintain compatibility. This method fails if the request's dimensions and metrics are incompatible.

In Google Analytics, reports fail if they request incompatible dimensions and/or metrics; in that case, you will need to remove dimensions and/or metrics from the incompatible report until the report is compatible.

The Realtime and Core reports have different compatibility rules. This method checks compatibility for Core reports.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BetaAnalyticsDataClient betaAnalyticsDataClient = BetaAnalyticsDataClient.create()) {
       CheckCompatibilityRequest request =
           CheckCompatibilityRequest.newBuilder()
               .setProperty("property-993141291")
               .addAllDimensions(new ArrayList<Dimension>())
               .addAllMetrics(new ArrayList<Metric>())
               .setDimensionFilter(FilterExpression.newBuilder().build())
               .setMetricFilter(FilterExpression.newBuilder().build())
               .setCompatibilityFilter(Compatibility.forNumber(0))
               .build();
       CheckCompatibilityResponse response = betaAnalyticsDataClient.checkCompatibility(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CheckCompatibilityRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CheckCompatibilityResponse](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityResponse)` |   
  
### checkCompatibilityCallable()
    
    
    public final UnaryCallable<CheckCompatibilityRequest,CheckCompatibilityResponse> checkCompatibilityCallable()

This compatibility method lists dimensions and metrics that can be added to a report request and maintain compatibility. This method fails if the request's dimensions and metrics are incompatible.

In Google Analytics, reports fail if they request incompatible dimensions and/or metrics; in that case, you will need to remove dimensions and/or metrics from the incompatible report until the report is compatible.

The Realtime and Core reports have different compatibility rules. This method checks compatibility for Core reports.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BetaAnalyticsDataClient betaAnalyticsDataClient = BetaAnalyticsDataClient.create()) {
       CheckCompatibilityRequest request =
           CheckCompatibilityRequest.newBuilder()
               .setProperty("property-993141291")
               .addAllDimensions(new ArrayList<Dimension>())
               .addAllMetrics(new ArrayList<Metric>())
               .setDimensionFilter(FilterExpression.newBuilder().build())
               .setMetricFilter(FilterExpression.newBuilder().build())
               .setCompatibilityFilter(Compatibility.forNumber(0))
               .build();
       ApiFuture<CheckCompatibilityResponse> future =
           betaAnalyticsDataClient.checkCompatibilityCallable().futureCall(request);
       // Do something.
       CheckCompatibilityResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CheckCompatibilityRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest),[CheckCompatibilityResponse](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityResponse)>` |   
  
### close()
    
    
    public final void close()

### createAudienceExportAsync(@Nullable PropertyName parent, AudienceExport audienceExport)
    
    
    public final OperationFuture<AudienceExport,AudienceExportMetadata> createAudienceExportAsync(@Nullable PropertyName parent, AudienceExport audienceExport)

Creates an audience export for later retrieval. This method quickly returns the audience export's resource name and initiates a long running asynchronous request to form an audience export. To export the users in an audience export, first create the audience export through this method and then send the audience resource name to the `QueryAudienceExport` method.

See [Creating an Audience Export](https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics) for an introduction to Audience Exports with examples.

An audience export is a snapshot of the users currently in the audience at the time of audience export creation. Creating audience exports for one audience on different days will return different results as users enter and exit the audience.

Audiences in Google Analytics 4 allow you to segment your users in the ways that are important to your business. To learn more, see <https://support.google.com/analytics/answer/9267572>. Audience exports contain the users in each audience.

Audience Export APIs have some methods at alpha and other methods at beta stability. The intention is to advance methods to beta stability after some feedback and adoption. To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](https://forms.gle/EeA5u5LW6PEggtCEA) form.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BetaAnalyticsDataClient betaAnalyticsDataClient = BetaAnalyticsDataClient.create()) {
       PropertyName parent = PropertyName.of("[PROPERTY]");
       AudienceExport audienceExport = AudienceExport.newBuilder().build();
       AudienceExport response =
           betaAnalyticsDataClient.createAudienceExportAsync(parent, audienceExport).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.analytics.data.v1beta.PropertyName`  
Required. The parent resource where this audience export will be created. Format: `properties/{property}`  
`audienceExport` | `[AudienceExport](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.AudienceExport)`  
Required. The audience export to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AudienceExport](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.AudienceExport),[AudienceExportMetadata](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.AudienceExportMetadata)>` |   
  
### createAudienceExportAsync(CreateAudienceExportRequest request)
    
    
    public final OperationFuture<AudienceExport,AudienceExportMetadata> createAudienceExportAsync(CreateAudienceExportRequest request)

Creates an audience export for later retrieval. This method quickly returns the audience export's resource name and initiates a long running asynchronous request to form an audience export. To export the users in an audience export, first create the audience export through this method and then send the audience resource name to the `QueryAudienceExport` method.

See [Creating an Audience Export](https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics) for an introduction to Audience Exports with examples.

An audience export is a snapshot of the users currently in the audience at the time of audience export creation. Creating audience exports for one audience on different days will return different results as users enter and exit the audience.

Audiences in Google Analytics 4 allow you to segment your users in the ways that are important to your business. To learn more, see <https://support.google.com/analytics/answer/9267572>. Audience exports contain the users in each audience.

Audience Export APIs have some methods at alpha and other methods at beta stability. The intention is to advance methods to beta stability after some feedback and adoption. To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](https://forms.gle/EeA5u5LW6PEggtCEA) form.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BetaAnalyticsDataClient betaAnalyticsDataClient = BetaAnalyticsDataClient.create()) {
       CreateAudienceExportRequest request =
           CreateAudienceExportRequest.newBuilder()
               .setParent(PropertyName.of("[PROPERTY]").toString())
               .setAudienceExport(AudienceExport.newBuilder().build())
               .build();
       AudienceExport response = betaAnalyticsDataClient.createAudienceExportAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAudienceExportRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CreateAudienceExportRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AudienceExport](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.AudienceExport),[AudienceExportMetadata](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.AudienceExportMetadata)>` |   
  
### createAudienceExportAsync(String parent, AudienceExport audienceExport)
    
    
    public final OperationFuture<AudienceExport,AudienceExportMetadata> createAudienceExportAsync(String parent, AudienceExport audienceExport)

Creates an audience export for later retrieval. This method quickly returns the audience export's resource name and initiates a long running asynchronous request to form an audience export. To export the users in an audience export, first create the audience export through this method and then send the audience resource name to the `QueryAudienceExport` method.

See [Creating an Audience Export](https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics) for an introduction to Audience Exports with examples.

An audience export is a snapshot of the users currently in the audience at the time of audience export creation. Creating audience exports for one audience on different days will return different results as users enter and exit the audience.

Audiences in Google Analytics 4 allow you to segment your users in the ways that are important to your business. To learn more, see <https://support.google.com/analytics/answer/9267572>. Audience exports contain the users in each audience.

Audience Export APIs have some methods at alpha and other methods at beta stability. The intention is to advance methods to beta stability after some feedback and adoption. To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](https://forms.gle/EeA5u5LW6PEggtCEA) form.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BetaAnalyticsDataClient betaAnalyticsDataClient = BetaAnalyticsDataClient.create()) {
       String parent = PropertyName.of("[PROPERTY]").toString();
       AudienceExport audienceExport = AudienceExport.newBuilder().build();
       AudienceExport response =
           betaAnalyticsDataClient.createAudienceExportAsync(parent, audienceExport).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this audience export will be created. Format: `properties/{property}`  
`audienceExport` | `[AudienceExport](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.AudienceExport)`  
Required. The audience export to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AudienceExport](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.AudienceExport),[AudienceExportMetadata](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.AudienceExportMetadata)>` |   
  
### createAudienceExportCallable()
    
    
    public final UnaryCallable<CreateAudienceExportRequest,Operation> createAudienceExportCallable()

Creates an audience export for later retrieval. This method quickly returns the audience export's resource name and initiates a long running asynchronous request to form an audience export. To export the users in an audience export, first create the audience export through this method and then send the audience resource name to the `QueryAudienceExport` method.

See [Creating an Audience Export](https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics) for an introduction to Audience Exports with examples.

An audience export is a snapshot of the users currently in the audience at the time of audience export creation. Creating audience exports for one audience on different days will return different results as users enter and exit the audience.

Audiences in Google Analytics 4 allow you to segment your users in the ways that are important to your business. To learn more, see <https://support.google.com/analytics/answer/9267572>. Audience exports contain the users in each audience.

Audience Export APIs have some methods at alpha and other methods at beta stability. The intention is to advance methods to beta stability after some feedback and adoption. To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](https://forms.gle/EeA5u5LW6PEggtCEA) form.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BetaAnalyticsDataClient betaAnalyticsDataClient = BetaAnalyticsDataClient.create()) {
       CreateAudienceExportRequest request =
           CreateAudienceExportRequest.newBuilder()
               .setParent(PropertyName.of("[PROPERTY]").toString())
               .setAudienceExport(AudienceExport.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           betaAnalyticsDataClient.createAudienceExportCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateAudienceExportRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CreateAudienceExportRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createAudienceExportOperationCallable()
    
    
    public final OperationCallable<CreateAudienceExportRequest,AudienceExport,AudienceExportMetadata> createAudienceExportOperationCallable()

Creates an audience export for later retrieval. This method quickly returns the audience export's resource name and initiates a long running asynchronous request to form an audience export. To export the users in an audience export, first create the audience export through this method and then send the audience resource name to the `QueryAudienceExport` method.

See [Creating an Audience Export](https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics) for an introduction to Audience Exports with examples.

An audience export is a snapshot of the users currently in the audience at the time of audience export creation. Creating audience exports for one audience on different days will return different results as users enter and exit the audience.

Audiences in Google Analytics 4 allow you to segment your users in the ways that are important to your business. To learn more, see <https://support.google.com/analytics/answer/9267572>. Audience exports contain the users in each audience.

Audience Export APIs have some methods at alpha and other methods at beta stability. The intention is to advance methods to beta stability after some feedback and adoption. To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](https://forms.gle/EeA5u5LW6PEggtCEA) form.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BetaAnalyticsDataClient betaAnalyticsDataClient = BetaAnalyticsDataClient.create()) {
       CreateAudienceExportRequest request =
           CreateAudienceExportRequest.newBuilder()
               .setParent(PropertyName.of("[PROPERTY]").toString())
               .setAudienceExport(AudienceExport.newBuilder().build())
               .build();
       OperationFuture<AudienceExport, AudienceExportMetadata> future =
           betaAnalyticsDataClient.createAudienceExportOperationCallable().futureCall(request);
       // Do something.
       AudienceExport response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateAudienceExportRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CreateAudienceExportRequest),[AudienceExport](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.AudienceExport),[AudienceExportMetadata](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.AudienceExportMetadata)>` |   
  
### getAudienceExport(@Nullable AudienceExportName name)
    
    
    public final AudienceExport getAudienceExport(@Nullable AudienceExportName name)

Gets configuration metadata about a specific audience export. This method can be used to understand an audience export after it has been created.

See [Creating an Audience Export](https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics) for an introduction to Audience Exports with examples.

Audience Export APIs have some methods at alpha and other methods at beta stability. The intention is to advance methods to beta stability after some feedback and adoption. To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](https://forms.gle/EeA5u5LW6PEggtCEA) form.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BetaAnalyticsDataClient betaAnalyticsDataClient = BetaAnalyticsDataClient.create()) {
       AudienceExportName name = AudienceExportName.of("[PROPERTY]", "[AUDIENCE_EXPORT]");
       AudienceExport response = betaAnalyticsDataClient.getAudienceExport(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.analytics.data.v1beta.AudienceExportName`  
Required. The audience export resource name. Format: `properties/{property}/audienceExports/{audience_export}`  
**Returns**  
---  
**Type** | **Description**  
`[AudienceExport](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.AudienceExport)` |   
  
### getAudienceExport(GetAudienceExportRequest request)
    
    
    public final AudienceExport getAudienceExport(GetAudienceExportRequest request)

Gets configuration metadata about a specific audience export. This method can be used to understand an audience export after it has been created.

See [Creating an Audience Export](https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics) for an introduction to Audience Exports with examples.

Audience Export APIs have some methods at alpha and other methods at beta stability. The intention is to advance methods to beta stability after some feedback and adoption. To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](https://forms.gle/EeA5u5LW6PEggtCEA) form.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BetaAnalyticsDataClient betaAnalyticsDataClient = BetaAnalyticsDataClient.create()) {
       GetAudienceExportRequest request =
           GetAudienceExportRequest.newBuilder()
               .setName(AudienceExportName.of("[PROPERTY]", "[AUDIENCE_EXPORT]").toString())
               .build();
       AudienceExport response = betaAnalyticsDataClient.getAudienceExport(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAudienceExportRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.GetAudienceExportRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AudienceExport](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.AudienceExport)` |   
  
### getAudienceExport(String name)
    
    
    public final AudienceExport getAudienceExport(String name)

Gets configuration metadata about a specific audience export. This method can be used to understand an audience export after it has been created.

See [Creating an Audience Export](https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics) for an introduction to Audience Exports with examples.

Audience Export APIs have some methods at alpha and other methods at beta stability. The intention is to advance methods to beta stability after some feedback and adoption. To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](https://forms.gle/EeA5u5LW6PEggtCEA) form.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BetaAnalyticsDataClient betaAnalyticsDataClient = BetaAnalyticsDataClient.create()) {
       String name = AudienceExportName.of("[PROPERTY]", "[AUDIENCE_EXPORT]").toString();
       AudienceExport response = betaAnalyticsDataClient.getAudienceExport(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The audience export resource name. Format: `properties/{property}/audienceExports/{audience_export}`  
**Returns**  
---  
**Type** | **Description**  
`[AudienceExport](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.AudienceExport)` |   
  
### getAudienceExportCallable()
    
    
    public final UnaryCallable<GetAudienceExportRequest,AudienceExport> getAudienceExportCallable()

Gets configuration metadata about a specific audience export. This method can be used to understand an audience export after it has been created.

See [Creating an Audience Export](https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics) for an introduction to Audience Exports with examples.

Audience Export APIs have some methods at alpha and other methods at beta stability. The intention is to advance methods to beta stability after some feedback and adoption. To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](https://forms.gle/EeA5u5LW6PEggtCEA) form.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BetaAnalyticsDataClient betaAnalyticsDataClient = BetaAnalyticsDataClient.create()) {
       GetAudienceExportRequest request =
           GetAudienceExportRequest.newBuilder()
               .setName(AudienceExportName.of("[PROPERTY]", "[AUDIENCE_EXPORT]").toString())
               .build();
       ApiFuture<AudienceExport> future =
           betaAnalyticsDataClient.getAudienceExportCallable().futureCall(request);
       // Do something.
       AudienceExport response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAudienceExportRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.GetAudienceExportRequest),[AudienceExport](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.AudienceExport)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getMetadata(@Nullable MetadataName name)
    
    
    public final Metadata getMetadata(@Nullable MetadataName name)

Returns metadata for dimensions and metrics available in reporting methods. Used to explore the dimensions and metrics. In this method, a Google Analytics property identifier is specified in the request, and the metadata response includes Custom dimensions and metrics as well as Universal metadata.

For example if a custom metric with parameter name `levels_unlocked` is registered to a property, the Metadata response will contain `customEvent:levels_unlocked`. Universal metadata are dimensions and metrics applicable to any property such as `country` and `totalUsers`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BetaAnalyticsDataClient betaAnalyticsDataClient = BetaAnalyticsDataClient.create()) {
       MetadataName name = MetadataName.of("[PROPERTY]");
       Metadata response = betaAnalyticsDataClient.getMetadata(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.analytics.data.v1beta.MetadataName`  
Required. The resource name of the metadata to retrieve. This name field is specified in the URL path and not URL parameters. Property is a numeric Google Analytics property identifier. To learn more, see [where to find your Property ID](https://developers.google.com/analytics/devguides/reporting/data/v1/property-id). Example: properties/1234/metadata Set the Property ID to 0 for dimensions and metrics common to all properties. In this special mode, this method will not return custom dimensions and metrics.  
**Returns**  
---  
**Type** | **Description**  
`[Metadata](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Metadata)` |   
  
### getMetadata(GetMetadataRequest request)
    
    
    public final Metadata getMetadata(GetMetadataRequest request)

Returns metadata for dimensions and metrics available in reporting methods. Used to explore the dimensions and metrics. In this method, a Google Analytics property identifier is specified in the request, and the metadata response includes Custom dimensions and metrics as well as Universal metadata.

For example if a custom metric with parameter name `levels_unlocked` is registered to a property, the Metadata response will contain `customEvent:levels_unlocked`. Universal metadata are dimensions and metrics applicable to any property such as `country` and `totalUsers`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BetaAnalyticsDataClient betaAnalyticsDataClient = BetaAnalyticsDataClient.create()) {
       GetMetadataRequest request =
           GetMetadataRequest.newBuilder().setName(MetadataName.of("[PROPERTY]").toString()).build();
       Metadata response = betaAnalyticsDataClient.getMetadata(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMetadataRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.GetMetadataRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Metadata](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Metadata)` |   
  
### getMetadata(String name)
    
    
    public final Metadata getMetadata(String name)

Returns metadata for dimensions and metrics available in reporting methods. Used to explore the dimensions and metrics. In this method, a Google Analytics property identifier is specified in the request, and the metadata response includes Custom dimensions and metrics as well as Universal metadata.

For example if a custom metric with parameter name `levels_unlocked` is registered to a property, the Metadata response will contain `customEvent:levels_unlocked`. Universal metadata are dimensions and metrics applicable to any property such as `country` and `totalUsers`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BetaAnalyticsDataClient betaAnalyticsDataClient = BetaAnalyticsDataClient.create()) {
       String name = MetadataName.of("[PROPERTY]").toString();
       Metadata response = betaAnalyticsDataClient.getMetadata(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the metadata to retrieve. This name field is specified in the URL path and not URL parameters. Property is a numeric Google Analytics property identifier. To learn more, see [where to find your Property ID](https://developers.google.com/analytics/devguides/reporting/data/v1/property-id). Example: properties/1234/metadata Set the Property ID to 0 for dimensions and metrics common to all properties. In this special mode, this method will not return custom dimensions and metrics.  
**Returns**  
---  
**Type** | **Description**  
`[Metadata](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Metadata)` |   
  
### getMetadataCallable()
    
    
    public final UnaryCallable<GetMetadataRequest,Metadata> getMetadataCallable()

Returns metadata for dimensions and metrics available in reporting methods. Used to explore the dimensions and metrics. In this method, a Google Analytics property identifier is specified in the request, and the metadata response includes Custom dimensions and metrics as well as Universal metadata.

For example if a custom metric with parameter name `levels_unlocked` is registered to a property, the Metadata response will contain `customEvent:levels_unlocked`. Universal metadata are dimensions and metrics applicable to any property such as `country` and `totalUsers`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BetaAnalyticsDataClient betaAnalyticsDataClient = BetaAnalyticsDataClient.create()) {
       GetMetadataRequest request =
           GetMetadataRequest.newBuilder().setName(MetadataName.of("[PROPERTY]").toString()).build();
       ApiFuture<Metadata> future =
           betaAnalyticsDataClient.getMetadataCallable().futureCall(request);
       // Do something.
       Metadata response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetMetadataRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.GetMetadataRequest),[Metadata](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Metadata)>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings()
    
    
    public final @Nullable BetaAnalyticsDataSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.analytics.data.v1beta.BetaAnalyticsDataSettings` |   
  
### getStub()
    
    
    public BetaAnalyticsDataStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[BetaAnalyticsDataStub](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.stub.BetaAnalyticsDataStub)` |   
  
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
  
### listAudienceExports(@Nullable PropertyName parent)
    
    
    public final BetaAnalyticsDataClient.ListAudienceExportsPagedResponse listAudienceExports(@Nullable PropertyName parent)

Lists all audience exports for a property. This method can be used for you to find and reuse existing audience exports rather than creating unnecessary new audience exports. The same audience can have multiple audience exports that represent the export of users that were in an audience on different days.

See [Creating an Audience Export](https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics) for an introduction to Audience Exports with examples.

Audience Export APIs have some methods at alpha and other methods at beta stability. The intention is to advance methods to beta stability after some feedback and adoption. To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](https://forms.gle/EeA5u5LW6PEggtCEA) form.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BetaAnalyticsDataClient betaAnalyticsDataClient = BetaAnalyticsDataClient.create()) {
       PropertyName parent = PropertyName.of("[PROPERTY]");
       for (AudienceExport element :
           betaAnalyticsDataClient.listAudienceExports(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.analytics.data.v1beta.PropertyName`  
Required. All audience exports for this property will be listed in the response. Format: `properties/{property}`  
**Returns**  
---  
**Type** | **Description**  
`[BetaAnalyticsDataClient.ListAudienceExportsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.BetaAnalyticsDataClient.ListAudienceExportsPagedResponse)` |   
  
### listAudienceExports(ListAudienceExportsRequest request)
    
    
    public final BetaAnalyticsDataClient.ListAudienceExportsPagedResponse listAudienceExports(ListAudienceExportsRequest request)

Lists all audience exports for a property. This method can be used for you to find and reuse existing audience exports rather than creating unnecessary new audience exports. The same audience can have multiple audience exports that represent the export of users that were in an audience on different days.

See [Creating an Audience Export](https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics) for an introduction to Audience Exports with examples.

Audience Export APIs have some methods at alpha and other methods at beta stability. The intention is to advance methods to beta stability after some feedback and adoption. To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](https://forms.gle/EeA5u5LW6PEggtCEA) form.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BetaAnalyticsDataClient betaAnalyticsDataClient = BetaAnalyticsDataClient.create()) {
       ListAudienceExportsRequest request =
           ListAudienceExportsRequest.newBuilder()
               .setParent(PropertyName.of("[PROPERTY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (AudienceExport element :
           betaAnalyticsDataClient.listAudienceExports(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAudienceExportsRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.ListAudienceExportsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BetaAnalyticsDataClient.ListAudienceExportsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.BetaAnalyticsDataClient.ListAudienceExportsPagedResponse)` |   
  
### listAudienceExports(String parent)
    
    
    public final BetaAnalyticsDataClient.ListAudienceExportsPagedResponse listAudienceExports(String parent)

Lists all audience exports for a property. This method can be used for you to find and reuse existing audience exports rather than creating unnecessary new audience exports. The same audience can have multiple audience exports that represent the export of users that were in an audience on different days.

See [Creating an Audience Export](https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics) for an introduction to Audience Exports with examples.

Audience Export APIs have some methods at alpha and other methods at beta stability. The intention is to advance methods to beta stability after some feedback and adoption. To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](https://forms.gle/EeA5u5LW6PEggtCEA) form.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BetaAnalyticsDataClient betaAnalyticsDataClient = BetaAnalyticsDataClient.create()) {
       String parent = PropertyName.of("[PROPERTY]").toString();
       for (AudienceExport element :
           betaAnalyticsDataClient.listAudienceExports(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. All audience exports for this property will be listed in the response. Format: `properties/{property}`  
**Returns**  
---  
**Type** | **Description**  
`[BetaAnalyticsDataClient.ListAudienceExportsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.BetaAnalyticsDataClient.ListAudienceExportsPagedResponse)` |   
  
### listAudienceExportsCallable()
    
    
    public final UnaryCallable<ListAudienceExportsRequest,ListAudienceExportsResponse> listAudienceExportsCallable()

Lists all audience exports for a property. This method can be used for you to find and reuse existing audience exports rather than creating unnecessary new audience exports. The same audience can have multiple audience exports that represent the export of users that were in an audience on different days.

See [Creating an Audience Export](https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics) for an introduction to Audience Exports with examples.

Audience Export APIs have some methods at alpha and other methods at beta stability. The intention is to advance methods to beta stability after some feedback and adoption. To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](https://forms.gle/EeA5u5LW6PEggtCEA) form.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BetaAnalyticsDataClient betaAnalyticsDataClient = BetaAnalyticsDataClient.create()) {
       ListAudienceExportsRequest request =
           ListAudienceExportsRequest.newBuilder()
               .setParent(PropertyName.of("[PROPERTY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListAudienceExportsResponse response =
             betaAnalyticsDataClient.listAudienceExportsCallable().call(request);
         for (AudienceExport element : response.getAudienceExportsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAudienceExportsRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.ListAudienceExportsRequest),[ListAudienceExportsResponse](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.ListAudienceExportsResponse)>` |   
  
### listAudienceExportsPagedCallable()
    
    
    public final UnaryCallable<ListAudienceExportsRequest,BetaAnalyticsDataClient.ListAudienceExportsPagedResponse> listAudienceExportsPagedCallable()

Lists all audience exports for a property. This method can be used for you to find and reuse existing audience exports rather than creating unnecessary new audience exports. The same audience can have multiple audience exports that represent the export of users that were in an audience on different days.

See [Creating an Audience Export](https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics) for an introduction to Audience Exports with examples.

Audience Export APIs have some methods at alpha and other methods at beta stability. The intention is to advance methods to beta stability after some feedback and adoption. To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](https://forms.gle/EeA5u5LW6PEggtCEA) form.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BetaAnalyticsDataClient betaAnalyticsDataClient = BetaAnalyticsDataClient.create()) {
       ListAudienceExportsRequest request =
           ListAudienceExportsRequest.newBuilder()
               .setParent(PropertyName.of("[PROPERTY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<AudienceExport> future =
           betaAnalyticsDataClient.listAudienceExportsPagedCallable().futureCall(request);
       // Do something.
       for (AudienceExport element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAudienceExportsRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.ListAudienceExportsRequest),[ListAudienceExportsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.BetaAnalyticsDataClient.ListAudienceExportsPagedResponse)>` |   
  
### queryAudienceExport(QueryAudienceExportRequest request)
    
    
    public final QueryAudienceExportResponse queryAudienceExport(QueryAudienceExportRequest request)

Retrieves an audience export of users. After creating an audience, the users are not immediately available for exporting. First, a request to `CreateAudienceExport` is necessary to create an audience export of users, and then second, this method is used to retrieve the users in the audience export.

See [Creating an Audience Export](https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics) for an introduction to Audience Exports with examples.

Audiences in Google Analytics 4 allow you to segment your users in the ways that are important to your business. To learn more, see <https://support.google.com/analytics/answer/9267572>.

Audience Export APIs have some methods at alpha and other methods at beta stability. The intention is to advance methods to beta stability after some feedback and adoption. To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](https://forms.gle/EeA5u5LW6PEggtCEA) form.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BetaAnalyticsDataClient betaAnalyticsDataClient = BetaAnalyticsDataClient.create()) {
       QueryAudienceExportRequest request =
           QueryAudienceExportRequest.newBuilder()
               .setName("name3373707")
               .setOffset(-1019779949)
               .setLimit(102976443)
               .build();
       QueryAudienceExportResponse response = betaAnalyticsDataClient.queryAudienceExport(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[QueryAudienceExportRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QueryAudienceExportRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[QueryAudienceExportResponse](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QueryAudienceExportResponse)` |   
  
### queryAudienceExport(String name)
    
    
    public final QueryAudienceExportResponse queryAudienceExport(String name)

Retrieves an audience export of users. After creating an audience, the users are not immediately available for exporting. First, a request to `CreateAudienceExport` is necessary to create an audience export of users, and then second, this method is used to retrieve the users in the audience export.

See [Creating an Audience Export](https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics) for an introduction to Audience Exports with examples.

Audiences in Google Analytics 4 allow you to segment your users in the ways that are important to your business. To learn more, see <https://support.google.com/analytics/answer/9267572>.

Audience Export APIs have some methods at alpha and other methods at beta stability. The intention is to advance methods to beta stability after some feedback and adoption. To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](https://forms.gle/EeA5u5LW6PEggtCEA) form.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BetaAnalyticsDataClient betaAnalyticsDataClient = BetaAnalyticsDataClient.create()) {
       String name = "name3373707";
       QueryAudienceExportResponse response = betaAnalyticsDataClient.queryAudienceExport(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the audience export to retrieve users from. Format: `properties/{property}/audienceExports/{audience_export}`  
**Returns**  
---  
**Type** | **Description**  
`[QueryAudienceExportResponse](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QueryAudienceExportResponse)` |   
  
### queryAudienceExportCallable()
    
    
    public final UnaryCallable<QueryAudienceExportRequest,QueryAudienceExportResponse> queryAudienceExportCallable()

Retrieves an audience export of users. After creating an audience, the users are not immediately available for exporting. First, a request to `CreateAudienceExport` is necessary to create an audience export of users, and then second, this method is used to retrieve the users in the audience export.

See [Creating an Audience Export](https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics) for an introduction to Audience Exports with examples.

Audiences in Google Analytics 4 allow you to segment your users in the ways that are important to your business. To learn more, see <https://support.google.com/analytics/answer/9267572>.

Audience Export APIs have some methods at alpha and other methods at beta stability. The intention is to advance methods to beta stability after some feedback and adoption. To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](https://forms.gle/EeA5u5LW6PEggtCEA) form.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BetaAnalyticsDataClient betaAnalyticsDataClient = BetaAnalyticsDataClient.create()) {
       QueryAudienceExportRequest request =
           QueryAudienceExportRequest.newBuilder()
               .setName("name3373707")
               .setOffset(-1019779949)
               .setLimit(102976443)
               .build();
       ApiFuture<QueryAudienceExportResponse> future =
           betaAnalyticsDataClient.queryAudienceExportCallable().futureCall(request);
       // Do something.
       QueryAudienceExportResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[QueryAudienceExportRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QueryAudienceExportRequest),[QueryAudienceExportResponse](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QueryAudienceExportResponse)>` |   
  
### runPivotReport(RunPivotReportRequest request)
    
    
    public final RunPivotReportResponse runPivotReport(RunPivotReportRequest request)

Returns a customized pivot report of your Google Analytics event data. Pivot reports are more advanced and expressive formats than regular reports. In a pivot report, dimensions are only visible if they are included in a pivot. Multiple pivots can be specified to further dissect your data.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BetaAnalyticsDataClient betaAnalyticsDataClient = BetaAnalyticsDataClient.create()) {
       RunPivotReportRequest request =
           RunPivotReportRequest.newBuilder()
               .setProperty("property-993141291")
               .addAllDimensions(new ArrayList<Dimension>())
               .addAllMetrics(new ArrayList<Metric>())
               .addAllDateRanges(new ArrayList<DateRange>())
               .addAllPivots(new ArrayList<Pivot>())
               .setDimensionFilter(FilterExpression.newBuilder().build())
               .setMetricFilter(FilterExpression.newBuilder().build())
               .setCurrencyCode("currencyCode1004773790")
               .setCohortSpec(CohortSpec.newBuilder().build())
               .setKeepEmptyRows(true)
               .setReturnPropertyQuota(true)
               .addAllComparisons(new ArrayList<Comparison>())
               .build();
       RunPivotReportResponse response = betaAnalyticsDataClient.runPivotReport(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RunPivotReportRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.RunPivotReportRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RunPivotReportResponse](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.RunPivotReportResponse)` |   
  
### runPivotReportCallable()
    
    
    public final UnaryCallable<RunPivotReportRequest,RunPivotReportResponse> runPivotReportCallable()

Returns a customized pivot report of your Google Analytics event data. Pivot reports are more advanced and expressive formats than regular reports. In a pivot report, dimensions are only visible if they are included in a pivot. Multiple pivots can be specified to further dissect your data.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BetaAnalyticsDataClient betaAnalyticsDataClient = BetaAnalyticsDataClient.create()) {
       RunPivotReportRequest request =
           RunPivotReportRequest.newBuilder()
               .setProperty("property-993141291")
               .addAllDimensions(new ArrayList<Dimension>())
               .addAllMetrics(new ArrayList<Metric>())
               .addAllDateRanges(new ArrayList<DateRange>())
               .addAllPivots(new ArrayList<Pivot>())
               .setDimensionFilter(FilterExpression.newBuilder().build())
               .setMetricFilter(FilterExpression.newBuilder().build())
               .setCurrencyCode("currencyCode1004773790")
               .setCohortSpec(CohortSpec.newBuilder().build())
               .setKeepEmptyRows(true)
               .setReturnPropertyQuota(true)
               .addAllComparisons(new ArrayList<Comparison>())
               .build();
       ApiFuture<RunPivotReportResponse> future =
           betaAnalyticsDataClient.runPivotReportCallable().futureCall(request);
       // Do something.
       RunPivotReportResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RunPivotReportRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.RunPivotReportRequest),[RunPivotReportResponse](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.RunPivotReportResponse)>` |   
  
### runRealtimeReport(RunRealtimeReportRequest request)
    
    
    public final RunRealtimeReportResponse runRealtimeReport(RunRealtimeReportRequest request)

Returns a customized report of realtime event data for your property. Events appear in realtime reports seconds after they have been sent to the Google Analytics. Realtime reports show events and usage data for the periods of time ranging from the present moment to 30 minutes ago (up to 60 minutes for Google Analytics 360 properties).

For a guide to constructing realtime requests & understanding responses, see [Creating a Realtime Report](https://developers.google.com/analytics/devguides/reporting/data/v1/realtime-basics).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BetaAnalyticsDataClient betaAnalyticsDataClient = BetaAnalyticsDataClient.create()) {
       RunRealtimeReportRequest request =
           RunRealtimeReportRequest.newBuilder()
               .setProperty("property-993141291")
               .addAllDimensions(new ArrayList<Dimension>())
               .addAllMetrics(new ArrayList<Metric>())
               .setDimensionFilter(FilterExpression.newBuilder().build())
               .setMetricFilter(FilterExpression.newBuilder().build())
               .setLimit(102976443)
               .addAllMetricAggregations(new ArrayList<MetricAggregation>())
               .addAllOrderBys(new ArrayList<OrderBy>())
               .setReturnPropertyQuota(true)
               .addAllMinuteRanges(new ArrayList<MinuteRange>())
               .build();
       RunRealtimeReportResponse response = betaAnalyticsDataClient.runRealtimeReport(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RunRealtimeReportRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.RunRealtimeReportRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RunRealtimeReportResponse](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.RunRealtimeReportResponse)` |   
  
### runRealtimeReportCallable()
    
    
    public final UnaryCallable<RunRealtimeReportRequest,RunRealtimeReportResponse> runRealtimeReportCallable()

Returns a customized report of realtime event data for your property. Events appear in realtime reports seconds after they have been sent to the Google Analytics. Realtime reports show events and usage data for the periods of time ranging from the present moment to 30 minutes ago (up to 60 minutes for Google Analytics 360 properties).

For a guide to constructing realtime requests & understanding responses, see [Creating a Realtime Report](https://developers.google.com/analytics/devguides/reporting/data/v1/realtime-basics).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BetaAnalyticsDataClient betaAnalyticsDataClient = BetaAnalyticsDataClient.create()) {
       RunRealtimeReportRequest request =
           RunRealtimeReportRequest.newBuilder()
               .setProperty("property-993141291")
               .addAllDimensions(new ArrayList<Dimension>())
               .addAllMetrics(new ArrayList<Metric>())
               .setDimensionFilter(FilterExpression.newBuilder().build())
               .setMetricFilter(FilterExpression.newBuilder().build())
               .setLimit(102976443)
               .addAllMetricAggregations(new ArrayList<MetricAggregation>())
               .addAllOrderBys(new ArrayList<OrderBy>())
               .setReturnPropertyQuota(true)
               .addAllMinuteRanges(new ArrayList<MinuteRange>())
               .build();
       ApiFuture<RunRealtimeReportResponse> future =
           betaAnalyticsDataClient.runRealtimeReportCallable().futureCall(request);
       // Do something.
       RunRealtimeReportResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RunRealtimeReportRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.RunRealtimeReportRequest),[RunRealtimeReportResponse](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.RunRealtimeReportResponse)>` |   
  
### runReport(RunReportRequest request)
    
    
    public final RunReportResponse runReport(RunReportRequest request)

Returns a customized report of your Google Analytics event data. Reports contain statistics derived from data collected by the Google Analytics tracking code. The data returned from the API is as a table with columns for the requested dimensions and metrics. Metrics are individual measurements of user activity on your property, such as active users or event count. Dimensions break down metrics across some common criteria, such as country or event name.

For a guide to constructing requests & understanding responses, see [Creating a Report](https://developers.google.com/analytics/devguides/reporting/data/v1/basics).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BetaAnalyticsDataClient betaAnalyticsDataClient = BetaAnalyticsDataClient.create()) {
       RunReportRequest request =
           RunReportRequest.newBuilder()
               .setProperty("property-993141291")
               .addAllDimensions(new ArrayList<Dimension>())
               .addAllMetrics(new ArrayList<Metric>())
               .addAllDateRanges(new ArrayList<DateRange>())
               .setDimensionFilter(FilterExpression.newBuilder().build())
               .setMetricFilter(FilterExpression.newBuilder().build())
               .setOffset(-1019779949)
               .setLimit(102976443)
               .addAllMetricAggregations(new ArrayList<MetricAggregation>())
               .addAllOrderBys(new ArrayList<OrderBy>())
               .setCurrencyCode("currencyCode1004773790")
               .setCohortSpec(CohortSpec.newBuilder().build())
               .setKeepEmptyRows(true)
               .setReturnPropertyQuota(true)
               .addAllComparisons(new ArrayList<Comparison>())
               .build();
       RunReportResponse response = betaAnalyticsDataClient.runReport(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RunReportRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.RunReportRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RunReportResponse](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.RunReportResponse)` |   
  
### runReportCallable()
    
    
    public final UnaryCallable<RunReportRequest,RunReportResponse> runReportCallable()

Returns a customized report of your Google Analytics event data. Reports contain statistics derived from data collected by the Google Analytics tracking code. The data returned from the API is as a table with columns for the requested dimensions and metrics. Metrics are individual measurements of user activity on your property, such as active users or event count. Dimensions break down metrics across some common criteria, such as country or event name.

For a guide to constructing requests & understanding responses, see [Creating a Report](https://developers.google.com/analytics/devguides/reporting/data/v1/basics).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BetaAnalyticsDataClient betaAnalyticsDataClient = BetaAnalyticsDataClient.create()) {
       RunReportRequest request =
           RunReportRequest.newBuilder()
               .setProperty("property-993141291")
               .addAllDimensions(new ArrayList<Dimension>())
               .addAllMetrics(new ArrayList<Metric>())
               .addAllDateRanges(new ArrayList<DateRange>())
               .setDimensionFilter(FilterExpression.newBuilder().build())
               .setMetricFilter(FilterExpression.newBuilder().build())
               .setOffset(-1019779949)
               .setLimit(102976443)
               .addAllMetricAggregations(new ArrayList<MetricAggregation>())
               .addAllOrderBys(new ArrayList<OrderBy>())
               .setCurrencyCode("currencyCode1004773790")
               .setCohortSpec(CohortSpec.newBuilder().build())
               .setKeepEmptyRows(true)
               .setReturnPropertyQuota(true)
               .addAllComparisons(new ArrayList<Comparison>())
               .build();
       ApiFuture<RunReportResponse> future =
           betaAnalyticsDataClient.runReportCallable().futureCall(request);
       // Do something.
       RunReportResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RunReportRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.RunReportRequest),[RunReportResponse](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.RunReportResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
