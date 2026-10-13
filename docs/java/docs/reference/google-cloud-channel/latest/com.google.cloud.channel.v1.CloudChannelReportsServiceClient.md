---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelReportsServiceClient
title: Class CloudChannelReportsServiceClient (3.103.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:26:51.513201+00:00
---

# Class CloudChannelReportsServiceClient (3.103.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelReportsServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CloudChannelReportsServiceClient (3.103.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.103.0 (latest)  3.99.0  3.98.0  3.97.0  3.95.0  3.92.0  3.91.0  3.89.0  3.87.0  3.86.0  3.85.0  3.84.0  3.82.0  3.80.0  3.79.0  3.78.0  3.77.0  3.76.0  3.74.0  3.72.0  3.71.0  3.68.0  3.67.0  3.66.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.6  3.6.1  3.5.1  3.3.1 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-channel/google-cloud-channel/src/main/java/com/google/cloud/channel/v1/CloudChannelReportsServiceClient.java)| [Product Reference](https://cloud.google.com/channel/docs)| [REST Documentation](https://cloud.google.com/channel/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/channel/docs/reference/rpc)  
---|---|---|---  
  
**Deprecated.** _This class is deprecated and will be removed in the next major version update._

Service Description: CloudChannelReportsService lets Google Cloud resellers and distributors retrieve and combine a variety of data in Cloud Channel for multiple products (Google Cloud, Google Voice, and Google Workspace.)

Deprecated: This service is being deprecated. Please use [Export Channel Services data to BigQuery](https://cloud.google.com/channel/docs/rebilling/export-data-to-bigquery) instead.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelReportsServiceClient cloudChannelReportsServiceClient =
         CloudChannelReportsServiceClient.create()) {
       RunReportJobRequest request =
           RunReportJobRequest.newBuilder()
               .setName(ReportName.of("[ACCOUNT]", "[REPORT]").toString())
               .setDateRange(DateRange.newBuilder().build())
               .setFilter("filter-1274492040")
               .setLanguageCode("languageCode-2092349083")
               .build();
       RunReportJobResponse response =
           cloudChannelReportsServiceClient.runReportJobAsync(request).get();
     }
     

Note: close() needs to be called on the CloudChannelReportsServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
RunReportJob |  Begins generation of data for a given report. The report identifier is a UID (for example, `613bf59q`).  Possible error codes: 

  * PERMISSION_DENIED: The user doesn't have access to this report. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: The report identifier was not found. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 

Return value: The ID of a long-running operation.  To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata contains an instance of OperationMetadata.  To get the results of report generation, call CloudChannelReportsService.FetchReportResults with the RunReportJobResponse.report_job.  Deprecated: Please use [Export Channel Services data to BigQuery](https://cloud.google.com/channel/docs/rebilling/export-data-to-bigquery) instead. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * runReportJobAsync(RunReportJobRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * runReportJobOperationCallable() 
  * runReportJobCallable() 

  
FetchReportResults |  Retrieves data generated by CloudChannelReportsService.RunReportJob.  Deprecated: Please use [Export Channel Services data to BigQuery](https://cloud.google.com/channel/docs/rebilling/export-data-to-bigquery) instead. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * fetchReportResults(FetchReportResultsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * fetchReportResults(ReportJobName reportJob) 
  * fetchReportResults(String reportJob) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * fetchReportResultsPagedCallable() 
  * fetchReportResultsCallable() 

  
ListReports |  Lists the reports that RunReportJob can run. These reports include an ID, a description, and the list of columns that will be in the result.  Deprecated: Please use [Export Channel Services data to BigQuery](https://cloud.google.com/channel/docs/rebilling/export-data-to-bigquery) instead. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listReports(ListReportsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listReports(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listReportsPagedCallable() 
  * listReportsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of CloudChannelReportsServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CloudChannelReportsServiceSettings cloudChannelReportsServiceSettings =
         CloudChannelReportsServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     CloudChannelReportsServiceClient cloudChannelReportsServiceClient =
         CloudChannelReportsServiceClient.create(cloudChannelReportsServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CloudChannelReportsServiceSettings cloudChannelReportsServiceSettings =
         CloudChannelReportsServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     CloudChannelReportsServiceClient cloudChannelReportsServiceClient =
         CloudChannelReportsServiceClient.create(cloudChannelReportsServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CloudChannelReportsServiceSettings cloudChannelReportsServiceSettings =
         CloudChannelReportsServiceSettings.newHttpJsonBuilder().build();
     CloudChannelReportsServiceClient cloudChannelReportsServiceClient =
         CloudChannelReportsServiceClient.create(cloudChannelReportsServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CloudChannelReportsServiceClient

## Static Methods 

### create() (deprecated)
    
    
    public static final CloudChannelReportsServiceClient create()

Constructs an instance of CloudChannelReportsServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[CloudChannelReportsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelReportsServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CloudChannelReportsServiceSettings settings) (deprecated)
    
    
    public static final CloudChannelReportsServiceClient create(CloudChannelReportsServiceSettings settings)

Constructs an instance of CloudChannelReportsServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CloudChannelReportsServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelReportsServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelReportsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelReportsServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CloudChannelReportsServiceStub stub) (deprecated)
    
    
    public static final CloudChannelReportsServiceClient create(CloudChannelReportsServiceStub stub)

Constructs an instance of CloudChannelReportsServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(CloudChannelReportsServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CloudChannelReportsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.stub.CloudChannelReportsServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelReportsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelReportsServiceClient)` |   
  
## Constructors 

### CloudChannelReportsServiceClient(CloudChannelReportsServiceSettings settings) (deprecated)
    
    
    protected CloudChannelReportsServiceClient(CloudChannelReportsServiceSettings settings)

Constructs an instance of CloudChannelReportsServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CloudChannelReportsServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelReportsServiceSettings)`  
  
  
### CloudChannelReportsServiceClient(CloudChannelReportsServiceStub stub) (deprecated)
    
    
    protected CloudChannelReportsServiceClient(CloudChannelReportsServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CloudChannelReportsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.stub.CloudChannelReportsServiceStub)`  
  
  
## Methods 

### awaitTermination(long duration, TimeUnit unit) (deprecated)
    
    
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
  
### close() (deprecated)
    
    
    public final void close()

### fetchReportResults(@Nullable ReportJobName reportJob) (deprecated)
    
    
    public final CloudChannelReportsServiceClient.FetchReportResultsPagedResponse fetchReportResults(@Nullable ReportJobName reportJob)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Retrieves data generated by CloudChannelReportsService.RunReportJob.

Deprecated: Please use [Export Channel Services data to BigQuery](https://cloud.google.com/channel/docs/rebilling/export-data-to-bigquery) instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelReportsServiceClient cloudChannelReportsServiceClient =
         CloudChannelReportsServiceClient.create()) {
       ReportJobName reportJob = ReportJobName.of("[ACCOUNT]", "[REPORT_JOB]");
       for (Row element :
           cloudChannelReportsServiceClient.fetchReportResults(reportJob).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`reportJob` | `@org.jspecify.annotations.Nullable com.google.cloud.channel.v1.ReportJobName`  
Required. The report job created by CloudChannelReportsService.RunReportJob. Report_job uses the format: accounts/{account_id}/reportJobs/{report_job_id}  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelReportsServiceClient.FetchReportResultsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelReportsServiceClient.FetchReportResultsPagedResponse)` |   
  
### fetchReportResults(FetchReportResultsRequest request) (deprecated)
    
    
    public final CloudChannelReportsServiceClient.FetchReportResultsPagedResponse fetchReportResults(FetchReportResultsRequest request)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Retrieves data generated by CloudChannelReportsService.RunReportJob.

Deprecated: Please use [Export Channel Services data to BigQuery](https://cloud.google.com/channel/docs/rebilling/export-data-to-bigquery) instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelReportsServiceClient cloudChannelReportsServiceClient =
         CloudChannelReportsServiceClient.create()) {
       FetchReportResultsRequest request =
           FetchReportResultsRequest.newBuilder()
               .setReportJob(ReportJobName.of("[ACCOUNT]", "[REPORT_JOB]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .addAllPartitionKeys(new ArrayList<String>())
               .build();
       for (Row element :
           cloudChannelReportsServiceClient.fetchReportResults(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchReportResultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.FetchReportResultsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelReportsServiceClient.FetchReportResultsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelReportsServiceClient.FetchReportResultsPagedResponse)` |   
  
### fetchReportResults(String reportJob) (deprecated)
    
    
    public final CloudChannelReportsServiceClient.FetchReportResultsPagedResponse fetchReportResults(String reportJob)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Retrieves data generated by CloudChannelReportsService.RunReportJob.

Deprecated: Please use [Export Channel Services data to BigQuery](https://cloud.google.com/channel/docs/rebilling/export-data-to-bigquery) instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelReportsServiceClient cloudChannelReportsServiceClient =
         CloudChannelReportsServiceClient.create()) {
       String reportJob = ReportJobName.of("[ACCOUNT]", "[REPORT_JOB]").toString();
       for (Row element :
           cloudChannelReportsServiceClient.fetchReportResults(reportJob).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`reportJob` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The report job created by CloudChannelReportsService.RunReportJob. Report_job uses the format: accounts/{account_id}/reportJobs/{report_job_id}  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelReportsServiceClient.FetchReportResultsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelReportsServiceClient.FetchReportResultsPagedResponse)` |   
  
### fetchReportResultsCallable() (deprecated)
    
    
    public final UnaryCallable<FetchReportResultsRequest,FetchReportResultsResponse> fetchReportResultsCallable()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Retrieves data generated by CloudChannelReportsService.RunReportJob.

Deprecated: Please use [Export Channel Services data to BigQuery](https://cloud.google.com/channel/docs/rebilling/export-data-to-bigquery) instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelReportsServiceClient cloudChannelReportsServiceClient =
         CloudChannelReportsServiceClient.create()) {
       FetchReportResultsRequest request =
           FetchReportResultsRequest.newBuilder()
               .setReportJob(ReportJobName.of("[ACCOUNT]", "[REPORT_JOB]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .addAllPartitionKeys(new ArrayList<String>())
               .build();
       while (true) {
         FetchReportResultsResponse response =
             cloudChannelReportsServiceClient.fetchReportResultsCallable().call(request);
         for (Row element : response.getRowsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchReportResultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.FetchReportResultsRequest),[FetchReportResultsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.FetchReportResultsResponse)>` |   
  
### fetchReportResultsPagedCallable() (deprecated)
    
    
    public final UnaryCallable<FetchReportResultsRequest,CloudChannelReportsServiceClient.FetchReportResultsPagedResponse> fetchReportResultsPagedCallable()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Retrieves data generated by CloudChannelReportsService.RunReportJob.

Deprecated: Please use [Export Channel Services data to BigQuery](https://cloud.google.com/channel/docs/rebilling/export-data-to-bigquery) instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelReportsServiceClient cloudChannelReportsServiceClient =
         CloudChannelReportsServiceClient.create()) {
       FetchReportResultsRequest request =
           FetchReportResultsRequest.newBuilder()
               .setReportJob(ReportJobName.of("[ACCOUNT]", "[REPORT_JOB]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .addAllPartitionKeys(new ArrayList<String>())
               .build();
       ApiFuture<Row> future =
           cloudChannelReportsServiceClient.fetchReportResultsPagedCallable().futureCall(request);
       // Do something.
       for (Row element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchReportResultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.FetchReportResultsRequest),[FetchReportResultsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelReportsServiceClient.FetchReportResultsPagedResponse)>` |   
  
### getHttpJsonOperationsClient() (deprecated)
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getOperationsClient() (deprecated)
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings() (deprecated)
    
    
    public final @Nullable CloudChannelReportsServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.channel.v1.CloudChannelReportsServiceSettings` |   
  
### getStub() (deprecated)
    
    
    public CloudChannelReportsServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[CloudChannelReportsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.stub.CloudChannelReportsServiceStub)` |   
  
### isShutdown() (deprecated)
    
    
    public boolean isShutdown()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isTerminated() (deprecated)
    
    
    public boolean isTerminated()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### listReports(ListReportsRequest request) (deprecated)
    
    
    public final CloudChannelReportsServiceClient.ListReportsPagedResponse listReports(ListReportsRequest request)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Lists the reports that RunReportJob can run. These reports include an ID, a description, and the list of columns that will be in the result.

Deprecated: Please use [Export Channel Services data to BigQuery](https://cloud.google.com/channel/docs/rebilling/export-data-to-bigquery) instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelReportsServiceClient cloudChannelReportsServiceClient =
         CloudChannelReportsServiceClient.create()) {
       ListReportsRequest request =
           ListReportsRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setLanguageCode("languageCode-2092349083")
               .build();
       for (Report element : cloudChannelReportsServiceClient.listReports(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListReportsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListReportsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelReportsServiceClient.ListReportsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelReportsServiceClient.ListReportsPagedResponse)` |   
  
### listReports(String parent) (deprecated)
    
    
    public final CloudChannelReportsServiceClient.ListReportsPagedResponse listReports(String parent)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Lists the reports that RunReportJob can run. These reports include an ID, a description, and the list of columns that will be in the result.

Deprecated: Please use [Export Channel Services data to BigQuery](https://cloud.google.com/channel/docs/rebilling/export-data-to-bigquery) instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelReportsServiceClient cloudChannelReportsServiceClient =
         CloudChannelReportsServiceClient.create()) {
       String parent = "parent-995424086";
       for (Report element : cloudChannelReportsServiceClient.listReports(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the partner account to list available reports for. Parent uses the format: accounts/{account_id}  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelReportsServiceClient.ListReportsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelReportsServiceClient.ListReportsPagedResponse)` |   
  
### listReportsCallable() (deprecated)
    
    
    public final UnaryCallable<ListReportsRequest,ListReportsResponse> listReportsCallable()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Lists the reports that RunReportJob can run. These reports include an ID, a description, and the list of columns that will be in the result.

Deprecated: Please use [Export Channel Services data to BigQuery](https://cloud.google.com/channel/docs/rebilling/export-data-to-bigquery) instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelReportsServiceClient cloudChannelReportsServiceClient =
         CloudChannelReportsServiceClient.create()) {
       ListReportsRequest request =
           ListReportsRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setLanguageCode("languageCode-2092349083")
               .build();
       while (true) {
         ListReportsResponse response =
             cloudChannelReportsServiceClient.listReportsCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListReportsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListReportsRequest),[ListReportsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListReportsResponse)>` |   
  
### listReportsPagedCallable() (deprecated)
    
    
    public final UnaryCallable<ListReportsRequest,CloudChannelReportsServiceClient.ListReportsPagedResponse> listReportsPagedCallable()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Lists the reports that RunReportJob can run. These reports include an ID, a description, and the list of columns that will be in the result.

Deprecated: Please use [Export Channel Services data to BigQuery](https://cloud.google.com/channel/docs/rebilling/export-data-to-bigquery) instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelReportsServiceClient cloudChannelReportsServiceClient =
         CloudChannelReportsServiceClient.create()) {
       ListReportsRequest request =
           ListReportsRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setLanguageCode("languageCode-2092349083")
               .build();
       ApiFuture<Report> future =
           cloudChannelReportsServiceClient.listReportsPagedCallable().futureCall(request);
       // Do something.
       for (Report element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListReportsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListReportsRequest),[ListReportsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelReportsServiceClient.ListReportsPagedResponse)>` |   
  
### runReportJobAsync(RunReportJobRequest request) (deprecated)
    
    
    public final OperationFuture<RunReportJobResponse,OperationMetadata> runReportJobAsync(RunReportJobRequest request)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Begins generation of data for a given report. The report identifier is a UID (for example, `613bf59q`).

Possible error codes:

  * PERMISSION_DENIED: The user doesn't have access to this report. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: The report identifier was not found. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata contains an instance of OperationMetadata.

To get the results of report generation, call CloudChannelReportsService.FetchReportResults with the RunReportJobResponse.report_job.

Deprecated: Please use [Export Channel Services data to BigQuery](https://cloud.google.com/channel/docs/rebilling/export-data-to-bigquery) instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelReportsServiceClient cloudChannelReportsServiceClient =
         CloudChannelReportsServiceClient.create()) {
       RunReportJobRequest request =
           RunReportJobRequest.newBuilder()
               .setName(ReportName.of("[ACCOUNT]", "[REPORT]").toString())
               .setDateRange(DateRange.newBuilder().build())
               .setFilter("filter-1274492040")
               .setLanguageCode("languageCode-2092349083")
               .build();
       RunReportJobResponse response =
           cloudChannelReportsServiceClient.runReportJobAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RunReportJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.RunReportJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RunReportJobResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.RunReportJobResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.OperationMetadata)>` |   
  
### runReportJobCallable() (deprecated)
    
    
    public final UnaryCallable<RunReportJobRequest,Operation> runReportJobCallable()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Begins generation of data for a given report. The report identifier is a UID (for example, `613bf59q`).

Possible error codes:

  * PERMISSION_DENIED: The user doesn't have access to this report. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: The report identifier was not found. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata contains an instance of OperationMetadata.

To get the results of report generation, call CloudChannelReportsService.FetchReportResults with the RunReportJobResponse.report_job.

Deprecated: Please use [Export Channel Services data to BigQuery](https://cloud.google.com/channel/docs/rebilling/export-data-to-bigquery) instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelReportsServiceClient cloudChannelReportsServiceClient =
         CloudChannelReportsServiceClient.create()) {
       RunReportJobRequest request =
           RunReportJobRequest.newBuilder()
               .setName(ReportName.of("[ACCOUNT]", "[REPORT]").toString())
               .setDateRange(DateRange.newBuilder().build())
               .setFilter("filter-1274492040")
               .setLanguageCode("languageCode-2092349083")
               .build();
       ApiFuture<Operation> future =
           cloudChannelReportsServiceClient.runReportJobCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RunReportJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.RunReportJobRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### runReportJobOperationCallable() (deprecated)
    
    
    public final OperationCallable<RunReportJobRequest,RunReportJobResponse,OperationMetadata> runReportJobOperationCallable()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Begins generation of data for a given report. The report identifier is a UID (for example, `613bf59q`).

Possible error codes:

  * PERMISSION_DENIED: The user doesn't have access to this report. 
  * INVALID_ARGUMENT: Required request parameters are missing or invalid. 
  * NOT_FOUND: The report identifier was not found. 
  * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 
  * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. 



Return value: The ID of a long-running operation.

To get the results of the operation, call the GetOperation method of CloudChannelOperationsService. The Operation metadata contains an instance of OperationMetadata.

To get the results of report generation, call CloudChannelReportsService.FetchReportResults with the RunReportJobResponse.report_job.

Deprecated: Please use [Export Channel Services data to BigQuery](https://cloud.google.com/channel/docs/rebilling/export-data-to-bigquery) instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudChannelReportsServiceClient cloudChannelReportsServiceClient =
         CloudChannelReportsServiceClient.create()) {
       RunReportJobRequest request =
           RunReportJobRequest.newBuilder()
               .setName(ReportName.of("[ACCOUNT]", "[REPORT]").toString())
               .setDateRange(DateRange.newBuilder().build())
               .setFilter("filter-1274492040")
               .setLanguageCode("languageCode-2092349083")
               .build();
       OperationFuture<RunReportJobResponse, OperationMetadata> future =
           cloudChannelReportsServiceClient.runReportJobOperationCallable().futureCall(request);
       // Do something.
       RunReportJobResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RunReportJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.RunReportJobRequest),[RunReportJobResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.RunReportJobResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.OperationMetadata)>` |   
  
### shutdown() (deprecated)
    
    
    public void shutdown()

### shutdownNow() (deprecated)
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
