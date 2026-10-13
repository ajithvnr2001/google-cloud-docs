---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.GetCmekConfigRequest
title: Google Cloud Tasks v2beta3 API - Class GetCmekConfigRequest (3.0.0-beta09) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:44:45.989722+00:00
---

# Google Cloud Tasks v2beta3 API - Class GetCmekConfigRequest (3.0.0-beta09)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.GetCmekConfigRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Tasks v2beta3 API - Class GetCmekConfigRequest (3.0.0-beta09) Stay organized with collections  Save and categorize content based on your preferences. 

3.0.0-beta09 (latest)  3.0.0-beta08  2.0.0-beta08 
    
    
    public sealed class GetCmekConfigRequest : IMessage<GetCmekConfigRequest>, IEquatable<GetCmekConfigRequest>, IDeepCloneable<GetCmekConfigRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Tasks v2beta3 API class GetCmekConfigRequest.

Request message for [GetCmekConfig][google.cloud.tasks.v2beta3.CloudTasks.GetCmekConfig].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GetCmekConfigRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GetCmekConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.GetCmekConfigRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GetCmekConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.GetCmekConfigRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GetCmekConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.GetCmekConfigRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Tasks.V2Beta3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3)

## Assembly

Google.Cloud.Tasks.V2Beta3.dll

## Constructors 

### GetCmekConfigRequest()
    
    
    public GetCmekConfigRequest()

### GetCmekConfigRequest(GetCmekConfigRequest)
    
    
    public GetCmekConfigRequest(GetCmekConfigRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GetCmekConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.GetCmekConfigRequest)`  
  
  
## Properties 

### CmekConfigName
    
    
    public CmekConfigName CmekConfigName { get; set; }

[CmekConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.CmekConfigName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.GetCmekConfigRequest#Google_Cloud_Tasks_V2Beta3_GetCmekConfigRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[CmekConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.CmekConfigName)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. The config resource name. For example: projects/PROJECT_ID/locations/LOCATION_ID/cmekConfig`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
