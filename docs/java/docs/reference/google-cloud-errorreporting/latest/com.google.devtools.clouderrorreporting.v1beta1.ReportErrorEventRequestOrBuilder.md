---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-errorreporting/latest/com.google.devtools.clouderrorreporting.v1beta1.ReportErrorEventRequestOrBuilder
title: Interface ReportErrorEventRequestOrBuilder (0.220.0-beta) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:14:11.035503+00:00
---

# Interface ReportErrorEventRequestOrBuilder (0.220.0-beta)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-errorreporting/latest/com.google.devtools.clouderrorreporting.v1beta1.ReportErrorEventRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ReportErrorEventRequestOrBuilder (0.220.0-beta) Stay organized with collections  Save and categorize content based on your preferences. 

0.220.0-beta (latest)  0.216.0-beta  0.215.0-beta  0.214.0-beta  0.212.0-beta  0.209.0-beta  0.208.0-beta  0.206.0-beta  0.204.0-beta  0.203.0-beta  0.202.0-beta  0.201.0-beta  0.199.0-beta  0.197.0-beta  0.196.0-beta  0.195.0-beta  0.194.0-beta  0.193.0-beta  0.191.0-beta  0.189.0-beta  0.188.0-beta  0.185.0-beta  0.184.0-beta  0.183.0-beta  0.181.0-beta  0.180.0-beta  0.179.0-beta  0.178.0-beta  0.177.0-beta  0.176.0-beta  0.175.0-beta  0.174.0-beta  0.173.0-beta  0.172.0-beta  0.170.0-beta  0.169.0-beta  0.168.0-beta  0.167.0-beta  0.166.0-beta  0.165.0-beta  0.164.0-beta  0.163.0-beta  0.162.0-beta  0.161.0-beta  0.160.0-beta  0.158.0-beta  0.157.0-beta  0.156.0-beta  0.155.0-beta  0.154.0-beta  0.153.0-beta  0.152.0-beta  0.151.0-beta  0.150.0-beta  0.149.0-beta  0.148.0-beta  0.145.0-beta  0.144.0-beta  0.143.0-beta  0.142.0-beta  0.141.0-beta  0.140.0-beta  0.139.0-beta  0.138.0-beta  0.137.0-beta  0.136.0-beta  0.135.0-beta  0.134.0-beta  0.133.0-beta  0.132.0-beta  0.130.0-beta  0.129.0-beta  0.128.0-beta  0.127.0-beta  0.126.0-beta  0.125.0-beta  0.124.15-beta  0.123.4-beta  0.122.23-beta 
    
    
    public interface ReportErrorEventRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getEvent()
    
    
    public abstract ReportedErrorEvent getEvent()

Required. The error event to be reported.

` .google.devtools.clouderrorreporting.v1beta1.ReportedErrorEvent event = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[ReportedErrorEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-errorreporting/latest/com.google.devtools.clouderrorreporting.v1beta1.ReportedErrorEvent)` | The event.  
  
### getEventOrBuilder()
    
    
    public abstract ReportedErrorEventOrBuilder getEventOrBuilder()

Required. The error event to be reported.

` .google.devtools.clouderrorreporting.v1beta1.ReportedErrorEvent event = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[ReportedErrorEventOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-errorreporting/latest/com.google.devtools.clouderrorreporting.v1beta1.ReportedErrorEventOrBuilder)` |   
  
### getProjectName()
    
    
    public abstract String getProjectName()

Required. The resource name of the Google Cloud Platform project. Written as `projects/{projectId}`, where `{projectId}` is the [Google Cloud Platform project ID](https://support.google.com/cloud/answer/6158840).

Example: // `projects/my-project-123`.

` string project_name = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The projectName.  
  
### getProjectNameBytes()
    
    
    public abstract ByteString getProjectNameBytes()

Required. The resource name of the Google Cloud Platform project. Written as `projects/{projectId}`, where `{projectId}` is the [Google Cloud Platform project ID](https://support.google.com/cloud/answer/6158840).

Example: // `projects/my-project-123`.

` string project_name = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for projectName.  
  
### hasEvent()
    
    
    public abstract boolean hasEvent()

Required. The error event to be reported.

` .google.devtools.clouderrorreporting.v1beta1.ReportedErrorEvent event = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the event field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
