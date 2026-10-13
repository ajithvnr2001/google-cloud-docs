---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V1/latest/Google.Cloud.Functions.V1.HttpsTrigger
title: Cloud Functions v1 API - Class HttpsTrigger (2.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:51:02.142858+00:00
---

# Cloud Functions v1 API - Class HttpsTrigger (2.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V1/latest/Google.Cloud.Functions.V1.HttpsTrigger

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Functions v1 API - Class HttpsTrigger (2.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.8.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V1/latest/Google.Cloud.Functions.V1.HttpsTrigger)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V1/2.7.0/Google.Cloud.Functions.V1.HttpsTrigger)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V1/2.6.0/Google.Cloud.Functions.V1.HttpsTrigger)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V1/2.5.0/Google.Cloud.Functions.V1.HttpsTrigger)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V1/2.4.0/Google.Cloud.Functions.V1.HttpsTrigger)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V1/2.3.0/Google.Cloud.Functions.V1.HttpsTrigger)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V1/2.2.0/Google.Cloud.Functions.V1.HttpsTrigger)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V1/2.1.0/Google.Cloud.Functions.V1.HttpsTrigger)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V1/2.0.0/Google.Cloud.Functions.V1.HttpsTrigger)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V1/1.3.0/Google.Cloud.Functions.V1.HttpsTrigger)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V1/1.2.0/Google.Cloud.Functions.V1.HttpsTrigger)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V1/1.1.0/Google.Cloud.Functions.V1.HttpsTrigger)


    
    
    public sealed class HttpsTrigger : IMessage<HttpsTrigger>, IEquatable<HttpsTrigger>, IDeepCloneable<HttpsTrigger>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Functions v1 API class HttpsTrigger.

Describes HttpsTrigger, could be used to connect web hooks to function.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > HttpsTrigger

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[HttpsTrigger](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V1/latest/Google.Cloud.Functions.V1.HttpsTrigger), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[HttpsTrigger](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V1/latest/Google.Cloud.Functions.V1.HttpsTrigger), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[HttpsTrigger](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V1/latest/Google.Cloud.Functions.V1.HttpsTrigger), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Functions.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V1/latest/Google.Cloud.Functions.V1)

## Assembly

Google.Cloud.Functions.V1.dll

## Constructors 

### HttpsTrigger()
    
    
    public HttpsTrigger()

### HttpsTrigger(HttpsTrigger)
    
    
    public HttpsTrigger(HttpsTrigger other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[HttpsTrigger](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V1/latest/Google.Cloud.Functions.V1.HttpsTrigger)`  
  
  
## Properties 

### SecurityLevel
    
    
    public HttpsTrigger.Types.SecurityLevel SecurityLevel { get; set; }

The security level for the function.

**Property Value**  
---  
**Type** | **Description**  
`[HttpsTrigger](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V1/latest/Google.Cloud.Functions.V1.HttpsTrigger)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V1/latest/Google.Cloud.Functions.V1.HttpsTrigger.Types)[SecurityLevel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V1/latest/Google.Cloud.Functions.V1.HttpsTrigger.Types.SecurityLevel)` |   
  
### Url
    
    
    public string Url { get; set; }

Output only. The deployed url for the function.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
