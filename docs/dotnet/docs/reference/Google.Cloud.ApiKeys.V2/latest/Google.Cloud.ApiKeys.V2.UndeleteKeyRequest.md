---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiKeys.V2/latest/Google.Cloud.ApiKeys.V2.UndeleteKeyRequest
title: API Keys v2 API - Class UndeleteKeyRequest (1.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:21:25.879595+00:00
---

# API Keys v2 API - Class UndeleteKeyRequest (1.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiKeys.V2/latest/Google.Cloud.ApiKeys.V2.UndeleteKeyRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  API Keys v2 API - Class UndeleteKeyRequest (1.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiKeys.V2/latest/Google.Cloud.ApiKeys.V2.UndeleteKeyRequest)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiKeys.V2/1.4.0/Google.Cloud.ApiKeys.V2.UndeleteKeyRequest)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiKeys.V2/1.3.0/Google.Cloud.ApiKeys.V2.UndeleteKeyRequest)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiKeys.V2/1.2.0/Google.Cloud.ApiKeys.V2.UndeleteKeyRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiKeys.V2/1.1.0/Google.Cloud.ApiKeys.V2.UndeleteKeyRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiKeys.V2/1.0.0/Google.Cloud.ApiKeys.V2.UndeleteKeyRequest)


    
    
    public sealed class UndeleteKeyRequest : IMessage<UndeleteKeyRequest>, IEquatable<UndeleteKeyRequest>, IDeepCloneable<UndeleteKeyRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the API Keys v2 API class UndeleteKeyRequest.

Request message for `UndeleteKey` method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UndeleteKeyRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[UndeleteKeyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiKeys.V2/latest/Google.Cloud.ApiKeys.V2.UndeleteKeyRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[UndeleteKeyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiKeys.V2/latest/Google.Cloud.ApiKeys.V2.UndeleteKeyRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[UndeleteKeyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiKeys.V2/latest/Google.Cloud.ApiKeys.V2.UndeleteKeyRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ApiKeys.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiKeys.V2/latest/Google.Cloud.ApiKeys.V2)

## Assembly

Google.Cloud.ApiKeys.V2.dll

## Constructors 

### UndeleteKeyRequest()
    
    
    public UndeleteKeyRequest()

### UndeleteKeyRequest(UndeleteKeyRequest)
    
    
    public UndeleteKeyRequest(UndeleteKeyRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[UndeleteKeyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiKeys.V2/latest/Google.Cloud.ApiKeys.V2.UndeleteKeyRequest)`  
  
  
## Properties 

### KeyName
    
    
    public KeyName KeyName { get; set; }

[KeyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiKeys.V2/latest/Google.Cloud.ApiKeys.V2.KeyName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiKeys.V2/latest/Google.Cloud.ApiKeys.V2.UndeleteKeyRequest#Google_Cloud_ApiKeys_V2_UndeleteKeyRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[KeyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiKeys.V2/latest/Google.Cloud.ApiKeys.V2.KeyName)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. The resource name of the API key to be undeleted.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
