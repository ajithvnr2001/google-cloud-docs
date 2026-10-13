---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.DeleteAppVersionRequest
title: Gemini Enterprise for Customer Experience v1 API - Class DeleteAppVersionRequest (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:26:53.112775+00:00
---

# Gemini Enterprise for Customer Experience v1 API - Class DeleteAppVersionRequest (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.DeleteAppVersionRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience v1 API - Class DeleteAppVersionRequest (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta04 
    
    
    public sealed class DeleteAppVersionRequest : IMessage<DeleteAppVersionRequest>, IEquatable<DeleteAppVersionRequest>, IDeepCloneable<DeleteAppVersionRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Gemini Enterprise for Customer Experience v1 API class DeleteAppVersionRequest.

Request message for [AgentService.DeleteAppVersion][google.cloud.ces.v1.AgentService.DeleteAppVersion].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DeleteAppVersionRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DeleteAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.DeleteAppVersionRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DeleteAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.DeleteAppVersionRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DeleteAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.DeleteAppVersionRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Ces.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1)

## Assembly

Google.Cloud.Ces.V1.dll

## Constructors 

### DeleteAppVersionRequest()
    
    
    public DeleteAppVersionRequest()

### DeleteAppVersionRequest(DeleteAppVersionRequest)
    
    
    public DeleteAppVersionRequest(DeleteAppVersionRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DeleteAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.DeleteAppVersionRequest)`  
  
  
## Properties 

### AppVersionName
    
    
    public AppVersionName AppVersionName { get; set; }

[AppVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.AppVersionName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.DeleteAppVersionRequest#Google_Cloud_Ces_V1_DeleteAppVersionRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AppVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.AppVersionName)` |   
  
### Etag
    
    
    public string Etag { get; set; }

Optional. The current etag of the app version. If an etag is not provided, the deletion will overwrite any concurrent changes. If an etag is provided and does not match the current etag of the app version, deletion will be blocked and an ABORTED error will be returned.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. The resource name of the app version to delete.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
