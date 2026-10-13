---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.GetApplicationRequest
title: App Hub v1 API - Class GetApplicationRequest (1.3.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:48:58.224209+00:00
---

# App Hub v1 API - Class GetApplicationRequest (1.3.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.GetApplicationRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  App Hub v1 API - Class GetApplicationRequest (1.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.3.0 (latest)  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class GetApplicationRequest : IMessage<GetApplicationRequest>, IEquatable<GetApplicationRequest>, IDeepCloneable<GetApplicationRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the App Hub v1 API class GetApplicationRequest.

Request for GetApplication.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GetApplicationRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GetApplicationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.GetApplicationRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GetApplicationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.GetApplicationRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GetApplicationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.GetApplicationRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AppHub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1)

## Assembly

Google.Cloud.AppHub.V1.dll

## Constructors 

### GetApplicationRequest()
    
    
    public GetApplicationRequest()

### GetApplicationRequest(GetApplicationRequest)
    
    
    public GetApplicationRequest(GetApplicationRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GetApplicationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.GetApplicationRequest)`  
  
  
## Properties 

### ApplicationName
    
    
    public ApplicationName ApplicationName { get; set; }

[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ApplicationName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.GetApplicationRequest#Google_Cloud_AppHub_V1_GetApplicationRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ApplicationName)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. Fully qualified name of the Application to fetch. Expected format: `projects/{project}/locations/{location}/applications/{application}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
