---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ProcessOpenLineageRunEventResponse
title: Data Lineage v1 API - Class ProcessOpenLineageRunEventResponse (1.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:38.577095+00:00
---

# Data Lineage v1 API - Class ProcessOpenLineageRunEventResponse (1.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ProcessOpenLineageRunEventResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Data Lineage v1 API - Class ProcessOpenLineageRunEventResponse (1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.0 (latest)  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class ProcessOpenLineageRunEventResponse : IMessage<ProcessOpenLineageRunEventResponse>, IEquatable<ProcessOpenLineageRunEventResponse>, IDeepCloneable<ProcessOpenLineageRunEventResponse>, IBufferMessage, IMessage

Reference documentation and code samples for the Data Lineage v1 API class ProcessOpenLineageRunEventResponse.

Response message for [ProcessOpenLineageRunEvent][google.cloud.datacatalog.lineage.v1.Lineage.ProcessOpenLineageRunEvent].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ProcessOpenLineageRunEventResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ProcessOpenLineageRunEventResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ProcessOpenLineageRunEventResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ProcessOpenLineageRunEventResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ProcessOpenLineageRunEventResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ProcessOpenLineageRunEventResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ProcessOpenLineageRunEventResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DataCatalog.Lineage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1)

## Assembly

Google.Cloud.DataCatalog.Lineage.V1.dll

## Constructors 

### ProcessOpenLineageRunEventResponse()
    
    
    public ProcessOpenLineageRunEventResponse()

### ProcessOpenLineageRunEventResponse(ProcessOpenLineageRunEventResponse)
    
    
    public ProcessOpenLineageRunEventResponse(ProcessOpenLineageRunEventResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ProcessOpenLineageRunEventResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ProcessOpenLineageRunEventResponse)`  
  
  
## Properties 

### LineageEvents
    
    
    public RepeatedField<string> LineageEvents { get; }

Created lineage event names. Format: `projects/{project}/locations/{location}/processes/{process}/runs/{run}/lineageEvents/{lineage_event}`.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### LineageEventsAsLineageEventNames
    
    
    public ResourceNameList<LineageEventName> LineageEventsAsLineageEventNames { get; }

[LineageEventName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEventName)-typed view over the [LineageEvents](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ProcessOpenLineageRunEventResponse#Google_Cloud_DataCatalog_Lineage_V1_ProcessOpenLineageRunEventResponse_LineageEvents) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ResourceNameList](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNameList-1.html)[LineageEventName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEventName)` |   
  
### Process
    
    
    public string Process { get; set; }

Created process name. Format: `projects/{project}/locations/{location}/processes/{process}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ProcessAsProcessName
    
    
    public ProcessName ProcessAsProcessName { get; set; }

[ProcessName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ProcessName)-typed view over the [Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ProcessOpenLineageRunEventResponse#Google_Cloud_DataCatalog_Lineage_V1_ProcessOpenLineageRunEventResponse_Process) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ProcessName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ProcessName)` |   
  
### Run
    
    
    public string Run { get; set; }

Created run name. Format: `projects/{project}/locations/{location}/processes/{process}/runs/{run}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RunAsRunName
    
    
    public RunName RunAsRunName { get; set; }

[RunName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.RunName)-typed view over the [Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ProcessOpenLineageRunEventResponse#Google_Cloud_DataCatalog_Lineage_V1_ProcessOpenLineageRunEventResponse_Run) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[RunName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.RunName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-11 UTC."],[],[]] 
