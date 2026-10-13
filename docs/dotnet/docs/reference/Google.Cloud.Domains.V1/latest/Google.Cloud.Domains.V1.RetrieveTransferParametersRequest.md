---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.RetrieveTransferParametersRequest
title: Cloud Domains v1 API - Class RetrieveTransferParametersRequest (2.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:27:37.988178+00:00
---

# Cloud Domains v1 API - Class RetrieveTransferParametersRequest (2.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.RetrieveTransferParametersRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Domains v1 API - Class RetrieveTransferParametersRequest (2.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.RetrieveTransferParametersRequest)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/2.4.0/Google.Cloud.Domains.V1.RetrieveTransferParametersRequest)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/2.3.0/Google.Cloud.Domains.V1.RetrieveTransferParametersRequest)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/2.2.0/Google.Cloud.Domains.V1.RetrieveTransferParametersRequest)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/2.1.0/Google.Cloud.Domains.V1.RetrieveTransferParametersRequest)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/2.0.0/Google.Cloud.Domains.V1.RetrieveTransferParametersRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/1.0.0/Google.Cloud.Domains.V1.RetrieveTransferParametersRequest)


    
    
    public sealed class RetrieveTransferParametersRequest : IMessage<RetrieveTransferParametersRequest>, IEquatable<RetrieveTransferParametersRequest>, IDeepCloneable<RetrieveTransferParametersRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Domains v1 API class RetrieveTransferParametersRequest.

Request for the `RetrieveTransferParameters` method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > RetrieveTransferParametersRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[RetrieveTransferParametersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.RetrieveTransferParametersRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[RetrieveTransferParametersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.RetrieveTransferParametersRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[RetrieveTransferParametersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.RetrieveTransferParametersRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Domains.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1)

## Assembly

Google.Cloud.Domains.V1.dll

## Constructors 

### RetrieveTransferParametersRequest()
    
    
    public RetrieveTransferParametersRequest()

### RetrieveTransferParametersRequest(RetrieveTransferParametersRequest)
    
    
    public RetrieveTransferParametersRequest(RetrieveTransferParametersRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[RetrieveTransferParametersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.RetrieveTransferParametersRequest)`  
  
  
## Properties 

### DomainName
    
    
    public string DomainName { get; set; }

Required. The domain name. Unicode domain names must be expressed in Punycode format.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Location
    
    
    public string Location { get; set; }

Required. The location. Must be in the format `projects/*/locations/*`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### LocationAsLocationName
    
    
    public LocationName LocationAsLocationName { get; set; }

[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)-typed view over the [Location](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.RetrieveTransferParametersRequest#Google_Cloud_Domains_V1_RetrieveTransferParametersRequest_Location) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
