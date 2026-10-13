---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateBreakTemplatesRequestOrBuilder
title: Interface BatchCreateBreakTemplatesRequestOrBuilder (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:33:13.214700+00:00
---

# Interface BatchCreateBreakTemplatesRequestOrBuilder (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateBreakTemplatesRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface BatchCreateBreakTemplatesRequestOrBuilder (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface BatchCreateBreakTemplatesRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getParent()
    
    
    public abstract String getParent()

Required. The parent resource where `BreakTemplates` will be created. Format: `networks/{network_code}` The parent field in the `CreateBreakTemplateRequest` must match this field.

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parent.  
  
### getParentBytes()
    
    
    public abstract ByteString getParentBytes()

Required. The parent resource where `BreakTemplates` will be created. Format: `networks/{network_code}` The parent field in the `CreateBreakTemplateRequest` must match this field.

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parent.  
  
### getRequests(int index)
    
    
    public abstract CreateBreakTemplateRequest getRequests(int index)

Required. The `BreakTemplate` objects to create. A maximum of 100 objects can be created in a batch.

` repeated .google.ads.admanager.v1.CreateBreakTemplateRequest requests = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CreateBreakTemplateRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateBreakTemplateRequest)` |   
  
### getRequestsCount()
    
    
    public abstract int getRequestsCount()

Required. The `BreakTemplate` objects to create. A maximum of 100 objects can be created in a batch.

` repeated .google.ads.admanager.v1.CreateBreakTemplateRequest requests = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getRequestsList()
    
    
    public abstract List<CreateBreakTemplateRequest> getRequestsList()

Required. The `BreakTemplate` objects to create. A maximum of 100 objects can be created in a batch.

` repeated .google.ads.admanager.v1.CreateBreakTemplateRequest requests = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateBreakTemplateRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateBreakTemplateRequest)>` |   
  
### getRequestsOrBuilder(int index)
    
    
    public abstract CreateBreakTemplateRequestOrBuilder getRequestsOrBuilder(int index)

Required. The `BreakTemplate` objects to create. A maximum of 100 objects can be created in a batch.

` repeated .google.ads.admanager.v1.CreateBreakTemplateRequest requests = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CreateBreakTemplateRequestOrBuilder](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateBreakTemplateRequestOrBuilder)` |   
  
### getRequestsOrBuilderList()
    
    
    public abstract List<? extends CreateBreakTemplateRequestOrBuilder> getRequestsOrBuilderList()

Required. The `BreakTemplate` objects to create. A maximum of 100 objects can be created in a batch.

` repeated .google.ads.admanager.v1.CreateBreakTemplateRequest requests = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.ads.admanager.v1.CreateBreakTemplateRequestOrBuilder>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
