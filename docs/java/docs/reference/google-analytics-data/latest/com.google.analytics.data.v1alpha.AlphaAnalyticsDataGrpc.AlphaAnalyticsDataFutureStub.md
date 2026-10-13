---
url: https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.AlphaAnalyticsDataGrpc.AlphaAnalyticsDataFutureStub
title: Class AlphaAnalyticsDataGrpc.AlphaAnalyticsDataFutureStub (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:30:03.027174+00:00
---

# Class AlphaAnalyticsDataGrpc.AlphaAnalyticsDataFutureStub (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.AlphaAnalyticsDataGrpc.AlphaAnalyticsDataFutureStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AlphaAnalyticsDataGrpc.AlphaAnalyticsDataFutureStub (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0 
    
    
    public static final class AlphaAnalyticsDataGrpc.AlphaAnalyticsDataFutureStub extends AbstractFutureStub<AlphaAnalyticsDataGrpc.AlphaAnalyticsDataFutureStub>

A stub to allow clients to do ListenableFuture-style rpc calls to service AlphaAnalyticsData.

Google Analytics reporting data service.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractFutureStub > AlphaAnalyticsDataGrpc.AlphaAnalyticsDataFutureStub

## Inherited Members

io.grpc.stub.AbstractFutureStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractFutureStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.<T>withOption(io.grpc.CallOptions.Key<T>,T)

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.getCallOptions()

io.grpc.stub.AbstractStub.getChannel()

io.grpc.stub.AbstractStub.withCallCredentials(io.grpc.CallCredentials)

io.grpc.stub.AbstractStub.withChannel(io.grpc.Channel)

io.grpc.stub.AbstractStub.withCompression(java.lang.String)

io.grpc.stub.AbstractStub.withDeadline(io.grpc.Deadline)

io.grpc.stub.AbstractStub.withDeadlineAfter(java.time.Duration)

io.grpc.stub.AbstractStub.withDeadlineAfter(long,java.util.concurrent.TimeUnit)

io.grpc.stub.AbstractStub.withExecutor(java.util.concurrent.Executor)

io.grpc.stub.AbstractStub.withInterceptors(io.grpc.ClientInterceptor...)

io.grpc.stub.AbstractStub.withMaxInboundMessageSize(int)

io.grpc.stub.AbstractStub.withMaxOutboundMessageSize(int)

io.grpc.stub.AbstractStub.withOnReadyThreshold(int)

io.grpc.stub.AbstractStub.withWaitForReady()

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Methods 

### build(Channel channel, CallOptions callOptions)
    
    
    protected AlphaAnalyticsDataGrpc.AlphaAnalyticsDataFutureStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[AlphaAnalyticsDataGrpc.AlphaAnalyticsDataFutureStub](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.AlphaAnalyticsDataGrpc.AlphaAnalyticsDataFutureStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### chat(ChatRequest request)
    
    
    public ListenableFuture<ChatResponse> chat(ChatRequest request)

Provides a chat interface for interacting with Google Analytics data through the API. This product uses AI and may display inaccurate info. Your chat activity may be used to improve the product and your use is subject to Google's [Terms](https://policies.google.com/terms), [AI Use Policy](https://policies.google.com/terms/generative-ai/use-policy), and [Privacy Policy](https://policies.google.com/privacy). [Learn more about Chat AI Privacy](https://support.google.com/helpguide/answer/14185196).

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ChatRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.ChatRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ChatResponse](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.ChatResponse)>` |   
  
### createAudienceList(CreateAudienceListRequest request)
    
    
    public ListenableFuture<Operation> createAudienceList(CreateAudienceListRequest request)

Creates an audience list for later retrieval. This method quickly returns the audience list's resource name and initiates a long running asynchronous request to form an audience list. To list the users in an audience list, first create the audience list through this method and then send the audience resource name to the `QueryAudienceList` method. See [Creating an Audience List](https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics) for an introduction to Audience Lists with examples. An audience list is a snapshot of the users currently in the audience at the time of audience list creation. Creating audience lists for one audience on different days will return different results as users enter and exit the audience. Audiences in Google Analytics 4 allow you to segment your users in the ways that are important to your business. To learn more, see <https://support.google.com/analytics/answer/9267572>. Audience lists contain the users in each audience. This method is available at beta stability at [audienceExports.create](https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties.audienceExports/create). To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](https://forms.gle/EeA5u5LW6PEggtCEA) form.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAudienceListRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.CreateAudienceListRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createRecurringAudienceList(CreateRecurringAudienceListRequest request)
    
    
    public ListenableFuture<RecurringAudienceList> createRecurringAudienceList(CreateRecurringAudienceListRequest request)

Creates a recurring audience list. Recurring audience lists produces new audience lists each day. Audience lists are users in an audience at the time of the list's creation. A recurring audience list ensures that you have audience list based on the most recent data available for use each day. If you manually create audience list, you don't know when an audience list based on an additional day's data is available. This recurring audience list automates the creation of an audience list when an additional day's data is available. You will consume fewer quota tokens by using recurring audience list versus manually creating audience list at various times of day trying to guess when an additional day's data is ready. This method is introduced at alpha stability with the intention of gathering feedback on syntax and capabilities before entering beta. To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](https://forms.gle/EeA5u5LW6PEggtCEA) form.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateRecurringAudienceListRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.CreateRecurringAudienceListRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[RecurringAudienceList](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.RecurringAudienceList)>` |   
  
### createReportTask(CreateReportTaskRequest request)
    
    
    public ListenableFuture<Operation> createReportTask(CreateReportTaskRequest request)

Initiates the creation of a report task. This method quickly returns a report task and initiates a long running asynchronous request to form a customized report of your Google Analytics event data. A report task will be retained and available for querying for 72 hours after it has been created. A report task created by one user can be listed and queried by all users who have access to the property.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateReportTaskRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.CreateReportTaskRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getAudienceList(GetAudienceListRequest request)
    
    
    public ListenableFuture<AudienceList> getAudienceList(GetAudienceListRequest request)

Gets configuration metadata about a specific audience list. This method can be used to understand an audience list after it has been created. See [Creating an Audience List](https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics) for an introduction to Audience Lists with examples. This method is available at beta stability at [audienceExports.get](https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties.audienceExports/get). To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](https://forms.gle/EeA5u5LW6PEggtCEA) form.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAudienceListRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.GetAudienceListRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[AudienceList](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.AudienceList)>` |   
  
### getMetadata(GetMetadataRequest request)
    
    
    public ListenableFuture<Metadata> getMetadata(GetMetadataRequest request)

Returns metadata for dimensions and metrics available in reporting methods. Used to explore the dimensions and metrics. In this method, a Google Analytics property identifier is specified in the request, and the metadata response includes Custom dimensions and metrics as well as Universal metadata. For example if a custom metric with parameter name `levels_unlocked` is registered to a property, the Metadata response will contain `customEvent:levels_unlocked`. Universal metadata are dimensions and metrics applicable to any property such as `country` and `totalUsers`.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMetadataRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.GetMetadataRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Metadata](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.Metadata)>` |   
  
### getPropertyQuotasSnapshot(GetPropertyQuotasSnapshotRequest request)
    
    
    public ListenableFuture<PropertyQuotasSnapshot> getPropertyQuotasSnapshot(GetPropertyQuotasSnapshotRequest request)

Get all property quotas organized by quota category for a given property. This will charge 1 property quota from the category with the most quota.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPropertyQuotasSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.GetPropertyQuotasSnapshotRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[PropertyQuotasSnapshot](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.PropertyQuotasSnapshot)>` |   
  
### getRecurringAudienceList(GetRecurringAudienceListRequest request)
    
    
    public ListenableFuture<RecurringAudienceList> getRecurringAudienceList(GetRecurringAudienceListRequest request)

Gets configuration metadata about a specific recurring audience list. This method can be used to understand a recurring audience list's state after it has been created. For example, a recurring audience list resource will generate audience list instances for each day, and this method can be used to get the resource name of the most recent audience list instance. This method is introduced at alpha stability with the intention of gathering feedback on syntax and capabilities before entering beta. To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](https://forms.gle/EeA5u5LW6PEggtCEA) form.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRecurringAudienceListRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.GetRecurringAudienceListRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[RecurringAudienceList](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.RecurringAudienceList)>` |   
  
### getReportTask(GetReportTaskRequest request)
    
    
    public ListenableFuture<ReportTask> getReportTask(GetReportTaskRequest request)

Gets report metadata about a specific report task. After creating a report task, use this method to check its processing state or inspect its report definition.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetReportTaskRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.GetReportTaskRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ReportTask](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.ReportTask)>` |   
  
### listAudienceLists(ListAudienceListsRequest request)
    
    
    public ListenableFuture<ListAudienceListsResponse> listAudienceLists(ListAudienceListsRequest request)

Lists all audience lists for a property. This method can be used for you to find and reuse existing audience lists rather than creating unnecessary new audience lists. The same audience can have multiple audience lists that represent the list of users that were in an audience on different days. See [Creating an Audience List](https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics) for an introduction to Audience Lists with examples. This method is available at beta stability at [audienceExports.list](https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties.audienceExports/list). To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](https://forms.gle/EeA5u5LW6PEggtCEA) form.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAudienceListsRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.ListAudienceListsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListAudienceListsResponse](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.ListAudienceListsResponse)>` |   
  
### listRecurringAudienceLists(ListRecurringAudienceListsRequest request)
    
    
    public ListenableFuture<ListRecurringAudienceListsResponse> listRecurringAudienceLists(ListRecurringAudienceListsRequest request)

Lists all recurring audience lists for a property. This method can be used for you to find and reuse existing recurring audience lists rather than creating unnecessary new recurring audience lists. The same audience can have multiple recurring audience lists that represent different dimension combinations; for example, just the dimension `deviceId` or both the dimensions `deviceId` and `userId`. This method is introduced at alpha stability with the intention of gathering feedback on syntax and capabilities before entering beta. To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](https://forms.gle/EeA5u5LW6PEggtCEA) form.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRecurringAudienceListsRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.ListRecurringAudienceListsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListRecurringAudienceListsResponse](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.ListRecurringAudienceListsResponse)>` |   
  
### listReportTasks(ListReportTasksRequest request)
    
    
    public ListenableFuture<ListReportTasksResponse> listReportTasks(ListReportTasksRequest request)

Lists all report tasks for a property.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListReportTasksRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.ListReportTasksRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListReportTasksResponse](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.ListReportTasksResponse)>` |   
  
### queryAudienceList(QueryAudienceListRequest request)
    
    
    public ListenableFuture<QueryAudienceListResponse> queryAudienceList(QueryAudienceListRequest request)

Retrieves an audience list of users. After creating an audience, the users are not immediately available for listing. First, a request to `CreateAudienceList` is necessary to create an audience list of users, and then second, this method is used to retrieve the users in the audience list. See [Creating an Audience List](https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics) for an introduction to Audience Lists with examples. Audiences in Google Analytics 4 allow you to segment your users in the ways that are important to your business. To learn more, see <https://support.google.com/analytics/answer/9267572>. This method is available at beta stability at [audienceExports.query](https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties.audienceExports/query). To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](https://forms.gle/EeA5u5LW6PEggtCEA) form.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[QueryAudienceListRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.QueryAudienceListRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[QueryAudienceListResponse](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.QueryAudienceListResponse)>` |   
  
### queryReportTask(QueryReportTaskRequest request)
    
    
    public ListenableFuture<QueryReportTaskResponse> queryReportTask(QueryReportTaskRequest request)

Retrieves a report task's content. After requesting the `CreateReportTask`, you are able to retrieve the report content once the report is ACTIVE. This method will return an error if the report task's state is not `ACTIVE`. A query response will return the tabular row & column values of the report.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[QueryReportTaskRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.QueryReportTaskRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[QueryReportTaskResponse](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.QueryReportTaskResponse)>` |   
  
### runFunnelReport(RunFunnelReportRequest request)
    
    
    public ListenableFuture<RunFunnelReportResponse> runFunnelReport(RunFunnelReportRequest request)

Returns a customized funnel report of your Google Analytics event data. The data returned from the API is as a table with columns for the requested dimensions and metrics. Funnel exploration lets you visualize the steps your users take to complete a task and quickly see how well they are succeeding or failing at each step. For example, how do prospects become shoppers and then become buyers? How do one time buyers become repeat buyers? With this information, you can improve inefficient or abandoned customer journeys. To learn more, see [GA4 Funnel Explorations](https://support.google.com/analytics/answer/9327974). This method is introduced at alpha stability with the intention of gathering feedback on syntax and capabilities before entering beta. To give your feedback on this API, complete the [Google Analytics Data API Funnel Reporting Feedback](https://docs.google.com/forms/d/e/1FAIpQLSdwOlQDJAUoBiIgUZZ3S_Lwi8gr7Bb0k1jhvc-DEg7Rol3UjA/viewform).

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RunFunnelReportRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.RunFunnelReportRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[RunFunnelReportResponse](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.RunFunnelReportResponse)>` |   
  
### runReport(RunReportRequest request)
    
    
    public ListenableFuture<RunReportResponse> runReport(RunReportRequest request)

Returns a customized report of your Google Analytics event data. Reports contain statistics derived from data collected by the Google Analytics tracking code. The data returned from the API is as a table with columns for the requested dimensions and metrics. Metrics are individual measurements of user activity on your property, such as active users or event count. Dimensions break down metrics across some common criteria, such as country or event name.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RunReportRequest](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.RunReportRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[RunReportResponse](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.RunReportResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
