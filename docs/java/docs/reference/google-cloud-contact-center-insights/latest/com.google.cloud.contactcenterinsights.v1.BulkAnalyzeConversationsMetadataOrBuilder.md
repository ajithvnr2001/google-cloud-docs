---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.BulkAnalyzeConversationsMetadataOrBuilder
title: Interface BulkAnalyzeConversationsMetadataOrBuilder (2.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:56:06.942806+00:00
---

# Interface BulkAnalyzeConversationsMetadataOrBuilder (2.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.BulkAnalyzeConversationsMetadataOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface BulkAnalyzeConversationsMetadataOrBuilder (2.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.99.0 (latest)  2.95.0  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.81.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.10  2.2.7 
    
    
    public interface BulkAnalyzeConversationsMetadataOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCompletedAnalysesCount()
    
    
    public abstract int getCompletedAnalysesCount()

The number of requested analyses that have completed successfully so far.

`int32 completed_analyses_count = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The completedAnalysesCount.  
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

The time the operation was created.

`.google.protobuf.Timestamp create_time = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

The time the operation was created.

`.google.protobuf.Timestamp create_time = 1;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getEndTime()
    
    
    public abstract Timestamp getEndTime()

The time the operation finished running.

`.google.protobuf.Timestamp end_time = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The endTime.  
  
### getEndTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getEndTimeOrBuilder()

The time the operation finished running.

`.google.protobuf.Timestamp end_time = 2;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getFailedAnalysesCount()
    
    
    public abstract int getFailedAnalysesCount()

The number of requested analyses that have failed so far.

`int32 failed_analyses_count = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The failedAnalysesCount.  
  
### getPartialErrors(int index)
    
    
    public abstract Status getPartialErrors(int index)

Output only. Partial errors during bulk analyze operation that might cause the operation output to be incomplete.

` repeated .google.rpc.Status partial_errors = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.Status` |   
  
### getPartialErrorsCount()
    
    
    public abstract int getPartialErrorsCount()

Output only. Partial errors during bulk analyze operation that might cause the operation output to be incomplete.

` repeated .google.rpc.Status partial_errors = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getPartialErrorsList()
    
    
    public abstract List<Status> getPartialErrorsList()

Output only. Partial errors during bulk analyze operation that might cause the operation output to be incomplete.

` repeated .google.rpc.Status partial_errors = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<com.google.rpc.Status>` |   
  
### getPartialErrorsOrBuilder(int index)
    
    
    public abstract StatusOrBuilder getPartialErrorsOrBuilder(int index)

Output only. Partial errors during bulk analyze operation that might cause the operation output to be incomplete.

` repeated .google.rpc.Status partial_errors = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.StatusOrBuilder` |   
  
### getPartialErrorsOrBuilderList()
    
    
    public abstract List<? extends StatusOrBuilder> getPartialErrorsOrBuilderList()

Output only. Partial errors during bulk analyze operation that might cause the operation output to be incomplete.

` repeated .google.rpc.Status partial_errors = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.rpc.StatusOrBuilder>` |   
  
### getRequest()
    
    
    public abstract BulkAnalyzeConversationsRequest getRequest()

The original request for bulk analyze.

`.google.cloud.contactcenterinsights.v1.BulkAnalyzeConversationsRequest request = 3; `

**Returns**  
---  
**Type** | **Description**  
`[BulkAnalyzeConversationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.BulkAnalyzeConversationsRequest)` | The request.  
  
### getRequestOrBuilder()
    
    
    public abstract BulkAnalyzeConversationsRequestOrBuilder getRequestOrBuilder()

The original request for bulk analyze.

`.google.cloud.contactcenterinsights.v1.BulkAnalyzeConversationsRequest request = 3; `

**Returns**  
---  
**Type** | **Description**  
`[BulkAnalyzeConversationsRequestOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.BulkAnalyzeConversationsRequestOrBuilder)` |   
  
### getTotalRequestedAnalysesCount()
    
    
    public abstract int getTotalRequestedAnalysesCount()

Total number of analyses requested. Computed by the number of conversations returned by `filter` multiplied by `analysis_percentage` in the request.

`int32 total_requested_analyses_count = 6;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The totalRequestedAnalysesCount.  
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

The time the operation was created.

`.google.protobuf.Timestamp create_time = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasEndTime()
    
    
    public abstract boolean hasEndTime()

The time the operation finished running.

`.google.protobuf.Timestamp end_time = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the endTime field is set.  
  
### hasRequest()
    
    
    public abstract boolean hasRequest()

The original request for bulk analyze.

`.google.cloud.contactcenterinsights.v1.BulkAnalyzeConversationsRequest request = 3; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the request field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
