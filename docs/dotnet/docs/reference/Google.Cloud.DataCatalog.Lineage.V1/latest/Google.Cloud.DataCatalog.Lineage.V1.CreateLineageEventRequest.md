---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.CreateLineageEventRequest
title: Data Lineage v1 API - Class CreateLineageEventRequest (1.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:32.370219+00:00
---

# Data Lineage v1 API - Class CreateLineageEventRequest (1.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.CreateLineageEventRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Data Lineage v1 API - Class CreateLineageEventRequest (1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.0 (latest)  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class CreateLineageEventRequest : IMessage<CreateLineageEventRequest>, IEquatable<CreateLineageEventRequest>, IDeepCloneable<CreateLineageEventRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Data Lineage v1 API class CreateLineageEventRequest.

Request message for [CreateLineageEvent][google.cloud.datacatalog.lineage.v1.Lineage.CreateLineageEvent].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CreateLineageEventRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CreateLineageEventRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.CreateLineageEventRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CreateLineageEventRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.CreateLineageEventRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CreateLineageEventRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.CreateLineageEventRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DataCatalog.Lineage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1)

## Assembly

Google.Cloud.DataCatalog.Lineage.V1.dll

## Constructors 

### CreateLineageEventRequest()
    
    
    public CreateLineageEventRequest()

### CreateLineageEventRequest(CreateLineageEventRequest)
    
    
    public CreateLineageEventRequest(CreateLineageEventRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CreateLineageEventRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.CreateLineageEventRequest)`  
  
  
## Properties 

### LineageEvent
    
    
    public LineageEvent LineageEvent { get; set; }

Required. The lineage event to create.

**Property Value**  
---  
**Type** | **Description**  
`[LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The name of the run that should own the lineage event.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsRunName
    
    
    public RunName ParentAsRunName { get; set; }

[RunName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.RunName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.CreateLineageEventRequest#Google_Cloud_DataCatalog_Lineage_V1_CreateLineageEventRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[RunName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.RunName)` |   
  
### RequestId
    
    
    public string RequestId { get; set; }

Optional. A unique identifier for this request. Restricted to 36 ASCII characters. A random UUID is recommended. This request is idempotent only if a `request_id` is provided.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-11 UTC."],[],[]] 
