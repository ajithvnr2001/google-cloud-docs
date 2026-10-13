---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.ResetAuthorizationCodeRequest
title: Cloud Domains v1 API - Class ResetAuthorizationCodeRequest (2.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:16:07.499506+00:00
---

# Cloud Domains v1 API - Class ResetAuthorizationCodeRequest (2.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.ResetAuthorizationCodeRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Domains v1 API - Class ResetAuthorizationCodeRequest (2.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.ResetAuthorizationCodeRequest)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/2.4.0/Google.Cloud.Domains.V1.ResetAuthorizationCodeRequest)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/2.3.0/Google.Cloud.Domains.V1.ResetAuthorizationCodeRequest)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/2.2.0/Google.Cloud.Domains.V1.ResetAuthorizationCodeRequest)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/2.1.0/Google.Cloud.Domains.V1.ResetAuthorizationCodeRequest)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/2.0.0/Google.Cloud.Domains.V1.ResetAuthorizationCodeRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/1.0.0/Google.Cloud.Domains.V1.ResetAuthorizationCodeRequest)


    
    
    public sealed class ResetAuthorizationCodeRequest : IMessage<ResetAuthorizationCodeRequest>, IEquatable<ResetAuthorizationCodeRequest>, IDeepCloneable<ResetAuthorizationCodeRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Domains v1 API class ResetAuthorizationCodeRequest.

Request for the `ResetAuthorizationCode` method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ResetAuthorizationCodeRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ResetAuthorizationCodeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.ResetAuthorizationCodeRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ResetAuthorizationCodeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.ResetAuthorizationCodeRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ResetAuthorizationCodeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.ResetAuthorizationCodeRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Domains.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1)

## Assembly

Google.Cloud.Domains.V1.dll

## Constructors 

### ResetAuthorizationCodeRequest()
    
    
    public ResetAuthorizationCodeRequest()

### ResetAuthorizationCodeRequest(ResetAuthorizationCodeRequest)
    
    
    public ResetAuthorizationCodeRequest(ResetAuthorizationCodeRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ResetAuthorizationCodeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.ResetAuthorizationCodeRequest)`  
  
  
## Properties 

### Registration
    
    
    public string Registration { get; set; }

Required. The name of the `Registration` whose authorization code is being reset, in the format `projects/*/locations/*/registrations/*`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RegistrationAsRegistrationName
    
    
    public RegistrationName RegistrationAsRegistrationName { get; set; }

[RegistrationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.RegistrationName)-typed view over the [Registration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.ResetAuthorizationCodeRequest#Google_Cloud_Domains_V1_ResetAuthorizationCodeRequest_Registration) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[RegistrationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.RegistrationName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
