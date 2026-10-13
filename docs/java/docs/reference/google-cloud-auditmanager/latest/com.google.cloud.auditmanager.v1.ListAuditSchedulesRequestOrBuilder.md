---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-auditmanager/latest/com.google.cloud.auditmanager.v1.ListAuditSchedulesRequestOrBuilder
title: Interface ListAuditSchedulesRequestOrBuilder (0.17.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:23:14.491667+00:00
---

# Interface ListAuditSchedulesRequestOrBuilder (0.17.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-auditmanager/latest/com.google.cloud.auditmanager.v1.ListAuditSchedulesRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ListAuditSchedulesRequestOrBuilder (0.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.0 (latest)  0.13.0  0.12.0  0.11.0  0.9.0  0.6.0  0.5.0  0.3.0  0.1.0 
    
    
    public interface ListAuditSchedulesRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getPageSize()
    
    
    public abstract int getPageSize()

Optional. Maximum number of items to return in a single page. The service might return fewer items than this value. If unspecified, the service picks an appropriate default. The maximum value is 100; values above 100 are reduced to 100.

`int32 page_size = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The pageSize.  
  
### getPageToken()
    
    
    public abstract String getPageToken()

Optional. A page token, received from a previous call, to retrieve the next page of results.

`string page_token = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The pageToken.  
  
### getPageTokenBytes()
    
    
    public abstract ByteString getPageTokenBytes()

Optional. A page token, received from a previous call, to retrieve the next page of results.

`string page_token = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for pageToken.  
  
### getParent()
    
    
    public abstract String getParent()

Required. Parent for the audit schedule, in one of the following formats:

  * `projects/{project}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `organizations/{organization}/locations/{location}`



` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parent.  
  
### getParentBytes()
    
    
    public abstract ByteString getParentBytes()

Required. Parent for the audit schedule, in one of the following formats:

  * `projects/{project}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `organizations/{organization}/locations/{location}`



` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parent.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
