---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.BatchCreateTasksRequestOrBuilder
title: Interface BatchCreateTasksRequestOrBuilder (2.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:46:28.753439+00:00
---

# Interface BatchCreateTasksRequestOrBuilder (2.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.BatchCreateTasksRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface BatchCreateTasksRequestOrBuilder (2.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.99.0 (latest)  2.95.0  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.12  2.2.0  2.1.11 
    
    
    public interface BatchCreateTasksRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getParent()
    
    
    public abstract String getParent()

Required. The queue name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID`

The queue must already exist.

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parent.  
  
### getParentBytes()
    
    
    public abstract ByteString getParentBytes()

Required. The queue name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID`

The queue must already exist.

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parent.  
  
### getRequestId()
    
    
    public abstract String getRequestId()

Optional. This field will be used to identify the long running operation, avoiding duplication when user retries. If not provided, then a UUID will be generated at server side.

` string request_id = 3 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_info) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The requestId.  
  
### getRequestIdBytes()
    
    
    public abstract ByteString getRequestIdBytes()

Optional. This field will be used to identify the long running operation, avoiding duplication when user retries. If not provided, then a UUID will be generated at server side.

` string request_id = 3 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_info) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for requestId.  
  
### getRequests(int index)
    
    
    public abstract CreateTaskRequest getRequests(int index)

Required. The list of requests to create tasks. The queue specified in parent field of each CreateTaskRequest will be the same. This validation happens on the client side as well as in the handler. BatchCreateTasksRequest.parent will also be the same value as the individual CreateTaskRequest.parent. The maximum number of requests is 100.

` repeated .google.cloud.tasks.v2.CreateTaskRequest requests = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CreateTaskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CreateTaskRequest)` |   
  
### getRequestsCount()
    
    
    public abstract int getRequestsCount()

Required. The list of requests to create tasks. The queue specified in parent field of each CreateTaskRequest will be the same. This validation happens on the client side as well as in the handler. BatchCreateTasksRequest.parent will also be the same value as the individual CreateTaskRequest.parent. The maximum number of requests is 100.

` repeated .google.cloud.tasks.v2.CreateTaskRequest requests = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getRequestsList()
    
    
    public abstract List<CreateTaskRequest> getRequestsList()

Required. The list of requests to create tasks. The queue specified in parent field of each CreateTaskRequest will be the same. This validation happens on the client side as well as in the handler. BatchCreateTasksRequest.parent will also be the same value as the individual CreateTaskRequest.parent. The maximum number of requests is 100.

` repeated .google.cloud.tasks.v2.CreateTaskRequest requests = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateTaskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CreateTaskRequest)>` |   
  
### getRequestsOrBuilder(int index)
    
    
    public abstract CreateTaskRequestOrBuilder getRequestsOrBuilder(int index)

Required. The list of requests to create tasks. The queue specified in parent field of each CreateTaskRequest will be the same. This validation happens on the client side as well as in the handler. BatchCreateTasksRequest.parent will also be the same value as the individual CreateTaskRequest.parent. The maximum number of requests is 100.

` repeated .google.cloud.tasks.v2.CreateTaskRequest requests = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CreateTaskRequestOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CreateTaskRequestOrBuilder)` |   
  
### getRequestsOrBuilderList()
    
    
    public abstract List<? extends CreateTaskRequestOrBuilder> getRequestsOrBuilderList()

Required. The list of requests to create tasks. The queue specified in parent field of each CreateTaskRequest will be the same. This validation happens on the client side as well as in the handler. BatchCreateTasksRequest.parent will also be the same value as the individual CreateTaskRequest.parent. The maximum number of requests is 100.

` repeated .google.cloud.tasks.v2.CreateTaskRequest requests = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.tasks.v2.CreateTaskRequestOrBuilder>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
