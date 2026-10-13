---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.ListJobMessagesResponseOrBuilder
title: Interface ListJobMessagesResponseOrBuilder (0.103.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:00:00.941325+00:00
---

# Interface ListJobMessagesResponseOrBuilder (0.103.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.ListJobMessagesResponseOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ListJobMessagesResponseOrBuilder (0.103.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.103.0 (latest)  0.99.0  0.98.0  0.97.0  0.95.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.82.0  0.80.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.68.0  0.67.0  0.66.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.5.0 
    
    
    public interface ListJobMessagesResponseOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAutoscalingEvents(int index)
    
    
    public abstract AutoscalingEvent getAutoscalingEvents(int index)

Autoscaling events in ascending timestamp order.

`repeated .google.dataflow.v1beta3.AutoscalingEvent autoscaling_events = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AutoscalingEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.AutoscalingEvent)` |   
  
### getAutoscalingEventsCount()
    
    
    public abstract int getAutoscalingEventsCount()

Autoscaling events in ascending timestamp order.

`repeated .google.dataflow.v1beta3.AutoscalingEvent autoscaling_events = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAutoscalingEventsList()
    
    
    public abstract List<AutoscalingEvent> getAutoscalingEventsList()

Autoscaling events in ascending timestamp order.

`repeated .google.dataflow.v1beta3.AutoscalingEvent autoscaling_events = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[AutoscalingEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.AutoscalingEvent)>` |   
  
### getAutoscalingEventsOrBuilder(int index)
    
    
    public abstract AutoscalingEventOrBuilder getAutoscalingEventsOrBuilder(int index)

Autoscaling events in ascending timestamp order.

`repeated .google.dataflow.v1beta3.AutoscalingEvent autoscaling_events = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AutoscalingEventOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.AutoscalingEventOrBuilder)` |   
  
### getAutoscalingEventsOrBuilderList()
    
    
    public abstract List<? extends AutoscalingEventOrBuilder> getAutoscalingEventsOrBuilderList()

Autoscaling events in ascending timestamp order.

`repeated .google.dataflow.v1beta3.AutoscalingEvent autoscaling_events = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.dataflow.v1beta3.AutoscalingEventOrBuilder>` |   
  
### getJobMessages(int index)
    
    
    public abstract JobMessage getJobMessages(int index)

Messages in ascending timestamp order.

`repeated .google.dataflow.v1beta3.JobMessage job_messages = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[JobMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.JobMessage)` |   
  
### getJobMessagesCount()
    
    
    public abstract int getJobMessagesCount()

Messages in ascending timestamp order.

`repeated .google.dataflow.v1beta3.JobMessage job_messages = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getJobMessagesList()
    
    
    public abstract List<JobMessage> getJobMessagesList()

Messages in ascending timestamp order.

`repeated .google.dataflow.v1beta3.JobMessage job_messages = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[JobMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.JobMessage)>` |   
  
### getJobMessagesOrBuilder(int index)
    
    
    public abstract JobMessageOrBuilder getJobMessagesOrBuilder(int index)

Messages in ascending timestamp order.

`repeated .google.dataflow.v1beta3.JobMessage job_messages = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[JobMessageOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.JobMessageOrBuilder)` |   
  
### getJobMessagesOrBuilderList()
    
    
    public abstract List<? extends JobMessageOrBuilder> getJobMessagesOrBuilderList()

Messages in ascending timestamp order.

`repeated .google.dataflow.v1beta3.JobMessage job_messages = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.dataflow.v1beta3.JobMessageOrBuilder>` |   
  
### getNextPageToken()
    
    
    public abstract String getNextPageToken()

The token to obtain the next page of results if there are more.

`string next_page_token = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The nextPageToken.  
  
### getNextPageTokenBytes()
    
    
    public abstract ByteString getNextPageTokenBytes()

The token to obtain the next page of results if there are more.

`string next_page_token = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for nextPageToken.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
