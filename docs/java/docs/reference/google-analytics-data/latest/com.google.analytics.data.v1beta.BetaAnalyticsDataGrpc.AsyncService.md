---
url: https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.BetaAnalyticsDataGrpc.AsyncService
title: Interface BetaAnalyticsDataGrpc.AsyncService (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:11:27.349899+00:00
---

# Interface BetaAnalyticsDataGrpc.AsyncService (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.BetaAnalyticsDataGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface BetaAnalyticsDataGrpc.AsyncService (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0 
    
    
    public static interface BetaAnalyticsDataGrpc.AsyncService

Google Analytics reporting data service.

## Methods 

### batchRunPivotReports(BatchRunPivotReportsRequest request, StreamObserver<BatchRunPivotReportsResponse> responseObserver)
    
    
    public default void batchRunPivotReports(BatchRunPivotReportsRequest request, StreamObserver<BatchRunPivotReportsResponse> responseObserver)

Returns multiple pivot reports in a batch. All reports must be for the same Google Analytics property.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchRunPivotReportsRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.BatchRunPivotReportsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[BatchRunPivotReportsResponse](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.BatchRunPivotReportsResponse)>`  
  
  
### batchRunReports(BatchRunReportsRequest request, StreamObserver<BatchRunReportsResponse> responseObserver)
    
    
    public default void batchRunReports(BatchRunReportsRequest request, StreamObserver<BatchRunReportsResponse> responseObserver)

Returns multiple reports in a batch. All reports must be for the same Google Analytics property.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchRunReportsRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.BatchRunReportsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[BatchRunReportsResponse](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.BatchRunReportsResponse)>`  
  
  
### checkCompatibility(CheckCompatibilityRequest request, StreamObserver<CheckCompatibilityResponse> responseObserver)
    
    
    public default void checkCompatibility(CheckCompatibilityRequest request, StreamObserver<CheckCompatibilityResponse> responseObserver)

This compatibility method lists dimensions and metrics that can be added to a report request and maintain compatibility. This method fails if the request's dimensions and metrics are incompatible. In Google Analytics, reports fail if they request incompatible dimensions and/or metrics; in that case, you will need to remove dimensions and/or metrics from the incompatible report until the report is compatible. The Realtime and Core reports have different compatibility rules. This method checks compatibility for Core reports.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CheckCompatibilityRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[CheckCompatibilityResponse](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CheckCompatibilityResponse)>`  
  
  
### createAudienceExport(CreateAudienceExportRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createAudienceExport(CreateAudienceExportRequest request, StreamObserver<Operation> responseObserver)

Creates an audience export for later retrieval. This method quickly returns the audience export's resource name and initiates a long running asynchronous request to form an audience export. To export the users in an audience export, first create the audience export through this method and then send the audience resource name to the `QueryAudienceExport` method. See [Creating an Audience Export](https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics) for an introduction to Audience Exports with examples. An audience export is a snapshot of the users currently in the audience at the time of audience export creation. Creating audience exports for one audience on different days will return different results as users enter and exit the audience. Audiences in Google Analytics 4 allow you to segment your users in the ways that are important to your business. To learn more, see <https://support.google.com/analytics/answer/9267572>. Audience exports contain the users in each audience. Audience Export APIs have some methods at alpha and other methods at beta stability. The intention is to advance methods to beta stability after some feedback and adoption. To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](https://forms.gle/EeA5u5LW6PEggtCEA) form.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAudienceExportRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.CreateAudienceExportRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### getAudienceExport(GetAudienceExportRequest request, StreamObserver<AudienceExport> responseObserver)
    
    
    public default void getAudienceExport(GetAudienceExportRequest request, StreamObserver<AudienceExport> responseObserver)

Gets configuration metadata about a specific audience export. This method can be used to understand an audience export after it has been created. See [Creating an Audience Export](https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics) for an introduction to Audience Exports with examples. Audience Export APIs have some methods at alpha and other methods at beta stability. The intention is to advance methods to beta stability after some feedback and adoption. To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](https://forms.gle/EeA5u5LW6PEggtCEA) form.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAudienceExportRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.GetAudienceExportRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AudienceExport](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.AudienceExport)>`  
  
  
### getMetadata(GetMetadataRequest request, StreamObserver<Metadata> responseObserver)
    
    
    public default void getMetadata(GetMetadataRequest request, StreamObserver<Metadata> responseObserver)

Returns metadata for dimensions and metrics available in reporting methods. Used to explore the dimensions and metrics. In this method, a Google Analytics property identifier is specified in the request, and the metadata response includes Custom dimensions and metrics as well as Universal metadata. For example if a custom metric with parameter name `levels_unlocked` is registered to a property, the Metadata response will contain `customEvent:levels_unlocked`. Universal metadata are dimensions and metrics applicable to any property such as `country` and `totalUsers`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMetadataRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.GetMetadataRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Metadata](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Metadata)>`  
  
  
### listAudienceExports(ListAudienceExportsRequest request, StreamObserver<ListAudienceExportsResponse> responseObserver)
    
    
    public default void listAudienceExports(ListAudienceExportsRequest request, StreamObserver<ListAudienceExportsResponse> responseObserver)

Lists all audience exports for a property. This method can be used for you to find and reuse existing audience exports rather than creating unnecessary new audience exports. The same audience can have multiple audience exports that represent the export of users that were in an audience on different days. See [Creating an Audience Export](https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics) for an introduction to Audience Exports with examples. Audience Export APIs have some methods at alpha and other methods at beta stability. The intention is to advance methods to beta stability after some feedback and adoption. To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](https://forms.gle/EeA5u5LW6PEggtCEA) form.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAudienceExportsRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.ListAudienceExportsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListAudienceExportsResponse](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.ListAudienceExportsResponse)>`  
  
  
### queryAudienceExport(QueryAudienceExportRequest request, StreamObserver<QueryAudienceExportResponse> responseObserver)
    
    
    public default void queryAudienceExport(QueryAudienceExportRequest request, StreamObserver<QueryAudienceExportResponse> responseObserver)

Retrieves an audience export of users. After creating an audience, the users are not immediately available for exporting. First, a request to `CreateAudienceExport` is necessary to create an audience export of users, and then second, this method is used to retrieve the users in the audience export. See [Creating an Audience Export](https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics) for an introduction to Audience Exports with examples. Audiences in Google Analytics 4 allow you to segment your users in the ways that are important to your business. To learn more, see <https://support.google.com/analytics/answer/9267572>. Audience Export APIs have some methods at alpha and other methods at beta stability. The intention is to advance methods to beta stability after some feedback and adoption. To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](https://forms.gle/EeA5u5LW6PEggtCEA) form.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryAudienceExportRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QueryAudienceExportRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[QueryAudienceExportResponse](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QueryAudienceExportResponse)>`  
  
  
### runPivotReport(RunPivotReportRequest request, StreamObserver<RunPivotReportResponse> responseObserver)
    
    
    public default void runPivotReport(RunPivotReportRequest request, StreamObserver<RunPivotReportResponse> responseObserver)

Returns a customized pivot report of your Google Analytics event data. Pivot reports are more advanced and expressive formats than regular reports. In a pivot report, dimensions are only visible if they are included in a pivot. Multiple pivots can be specified to further dissect your data.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RunPivotReportRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.RunPivotReportRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[RunPivotReportResponse](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.RunPivotReportResponse)>`  
  
  
### runRealtimeReport(RunRealtimeReportRequest request, StreamObserver<RunRealtimeReportResponse> responseObserver)
    
    
    public default void runRealtimeReport(RunRealtimeReportRequest request, StreamObserver<RunRealtimeReportResponse> responseObserver)

Returns a customized report of realtime event data for your property. Events appear in realtime reports seconds after they have been sent to the Google Analytics. Realtime reports show events and usage data for the periods of time ranging from the present moment to 30 minutes ago (up to 60 minutes for Google Analytics 360 properties). For a guide to constructing realtime requests & understanding responses, see [Creating a Realtime Report](https://developers.google.com/analytics/devguides/reporting/data/v1/realtime-basics).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RunRealtimeReportRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.RunRealtimeReportRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[RunRealtimeReportResponse](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.RunRealtimeReportResponse)>`  
  
  
### runReport(RunReportRequest request, StreamObserver<RunReportResponse> responseObserver)
    
    
    public default void runReport(RunReportRequest request, StreamObserver<RunReportResponse> responseObserver)

Returns a customized report of your Google Analytics event data. Reports contain statistics derived from data collected by the Google Analytics tracking code. The data returned from the API is as a table with columns for the requested dimensions and metrics. Metrics are individual measurements of user activity on your property, such as active users or event count. Dimensions break down metrics across some common criteria, such as country or event name. For a guide to constructing requests & understanding responses, see [Creating a Report](https://developers.google.com/analytics/devguides/reporting/data/v1/basics).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RunReportRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.RunReportRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[RunReportResponse](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.RunReportResponse)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
