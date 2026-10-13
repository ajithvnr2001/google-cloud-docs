---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.StorageInsightsGrpc.StorageInsightsBlockingStub
title: Class StorageInsightsGrpc.StorageInsightsBlockingStub (0.84.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:44:12.061693+00:00
---

# Class StorageInsightsGrpc.StorageInsightsBlockingStub (0.84.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.StorageInsightsGrpc.StorageInsightsBlockingStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class StorageInsightsGrpc.StorageInsightsBlockingStub (0.84.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.84.0 (latest)  0.80.0  0.79.0  0.78.0  0.76.0  0.73.0  0.72.0  0.70.0  0.68.0  0.67.0  0.65.0  0.63.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.55.0  0.53.0  0.52.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class StorageInsightsGrpc.StorageInsightsBlockingStub extends AbstractBlockingStub<StorageInsightsGrpc.StorageInsightsBlockingStub>

A stub to allow clients to do limited synchronous rpc calls to service StorageInsights.

Service describing handlers for resources

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > StorageInsightsGrpc.StorageInsightsBlockingStub

## Inherited Members

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

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
    
    
    protected StorageInsightsGrpc.StorageInsightsBlockingStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[StorageInsightsGrpc.StorageInsightsBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.StorageInsightsGrpc.StorageInsightsBlockingStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createDatasetConfig(CreateDatasetConfigRequest request)
    
    
    public Operation createDatasetConfig(CreateDatasetConfigRequest request)

Creates a dataset configuration in a given project for a given location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDatasetConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.CreateDatasetConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### createReportConfig(CreateReportConfigRequest request)
    
    
    public ReportConfig createReportConfig(CreateReportConfigRequest request)

Creates a new ReportConfig in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateReportConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.CreateReportConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReportConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ReportConfig)` |   
  
### deleteDatasetConfig(DeleteDatasetConfigRequest request)
    
    
    public Operation deleteDatasetConfig(DeleteDatasetConfigRequest request)

Deletes a dataset configuration in a given project for a given location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDatasetConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.DeleteDatasetConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteReportConfig(DeleteReportConfigRequest request)
    
    
    public Empty deleteReportConfig(DeleteReportConfigRequest request)

Deletes a single ReportConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteReportConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.DeleteReportConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)` |   
  
### getDatasetConfig(GetDatasetConfigRequest request)
    
    
    public DatasetConfig getDatasetConfig(GetDatasetConfigRequest request)

Gets the dataset configuration in a given project for a given location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDatasetConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.GetDatasetConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DatasetConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.DatasetConfig)` |   
  
### getReportConfig(GetReportConfigRequest request)
    
    
    public ReportConfig getReportConfig(GetReportConfigRequest request)

Gets details of a single ReportConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetReportConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.GetReportConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReportConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ReportConfig)` |   
  
### getReportDetail(GetReportDetailRequest request)
    
    
    public ReportDetail getReportDetail(GetReportDetailRequest request)

Gets details of a single ReportDetail.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetReportDetailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.GetReportDetailRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReportDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ReportDetail)` |   
  
### linkDataset(LinkDatasetRequest request)
    
    
    public Operation linkDataset(LinkDatasetRequest request)

Links a dataset to BigQuery in a given project for a given location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[LinkDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.LinkDatasetRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### listDatasetConfigs(ListDatasetConfigsRequest request)
    
    
    public ListDatasetConfigsResponse listDatasetConfigs(ListDatasetConfigsRequest request)

Lists the dataset configurations in a given project for a given location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDatasetConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ListDatasetConfigsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListDatasetConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ListDatasetConfigsResponse)` |   
  
### listReportConfigs(ListReportConfigsRequest request)
    
    
    public ListReportConfigsResponse listReportConfigs(ListReportConfigsRequest request)

Lists ReportConfigs in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListReportConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ListReportConfigsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListReportConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ListReportConfigsResponse)` |   
  
### listReportDetails(ListReportDetailsRequest request)
    
    
    public ListReportDetailsResponse listReportDetails(ListReportDetailsRequest request)

Lists ReportDetails in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListReportDetailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ListReportDetailsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListReportDetailsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ListReportDetailsResponse)` |   
  
### unlinkDataset(UnlinkDatasetRequest request)
    
    
    public Operation unlinkDataset(UnlinkDatasetRequest request)

Unlinks a dataset from BigQuery in a given project for a given location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UnlinkDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.UnlinkDatasetRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updateDatasetConfig(UpdateDatasetConfigRequest request)
    
    
    public Operation updateDatasetConfig(UpdateDatasetConfigRequest request)

Updates a dataset configuration in a given project for a given location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDatasetConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.UpdateDatasetConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updateReportConfig(UpdateReportConfigRequest request)
    
    
    public ReportConfig updateReportConfig(UpdateReportConfigRequest request)

Updates the parameters of a single ReportConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateReportConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.UpdateReportConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReportConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.ReportConfig)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
