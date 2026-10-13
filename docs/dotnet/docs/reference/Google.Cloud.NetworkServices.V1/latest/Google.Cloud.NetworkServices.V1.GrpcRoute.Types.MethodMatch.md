---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.GrpcRoute.Types.MethodMatch
title: Network Services v1 API - Class GrpcRoute.Types.MethodMatch (1.7.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:27:46.087606+00:00
---

# Network Services v1 API - Class GrpcRoute.Types.MethodMatch (1.7.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.GrpcRoute.Types.MethodMatch

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Network Services v1 API - Class GrpcRoute.Types.MethodMatch (1.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.0 (latest)  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class GrpcRoute.Types.MethodMatch : IMessage<GrpcRoute.Types.MethodMatch>, IEquatable<GrpcRoute.Types.MethodMatch>, IDeepCloneable<GrpcRoute.Types.MethodMatch>, IBufferMessage, IMessage

Reference documentation and code samples for the Network Services v1 API class GrpcRoute.Types.MethodMatch.

Specifies a match against a method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GrpcRoute.Types.MethodMatch

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GrpcRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.GrpcRoute)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.GrpcRoute.Types)[MethodMatch](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.GrpcRoute.Types.MethodMatch), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GrpcRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.GrpcRoute)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.GrpcRoute.Types)[MethodMatch](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.GrpcRoute.Types.MethodMatch), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GrpcRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.GrpcRoute)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.GrpcRoute.Types)[MethodMatch](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.GrpcRoute.Types.MethodMatch), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.NetworkServices.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1)

## Assembly

Google.Cloud.NetworkServices.V1.dll

## Constructors 

### MethodMatch()
    
    
    public MethodMatch()

### MethodMatch(MethodMatch)
    
    
    public MethodMatch(GrpcRoute.Types.MethodMatch other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GrpcRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.GrpcRoute)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.GrpcRoute.Types)[MethodMatch](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.GrpcRoute.Types.MethodMatch)`  
  
  
## Properties 

### CaseSensitive
    
    
    public bool CaseSensitive { get; set; }

Optional. Specifies that matches are case sensitive. The default value is true. case_sensitive must not be used with a type of REGULAR_EXPRESSION.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### GrpcMethod
    
    
    public string GrpcMethod { get; set; }

Required. Name of the method to match against. If unspecified, will match all methods.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### GrpcService
    
    
    public string GrpcService { get; set; }

Required. Name of the service to match against. If unspecified, will match all services.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HasCaseSensitive
    
    
    public bool HasCaseSensitive { get; }

Gets whether the "case_sensitive" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Type
    
    
    public GrpcRoute.Types.MethodMatch.Types.Type Type { get; set; }

Optional. Specifies how to match against the name. If not specified, a default value of "EXACT" is used.

**Property Value**  
---  
**Type** | **Description**  
`[GrpcRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.GrpcRoute)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.GrpcRoute.Types)[MethodMatch](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.GrpcRoute.Types.MethodMatch)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.GrpcRoute.Types.MethodMatch.Types)[Type](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.GrpcRoute.Types.MethodMatch.Types.Type)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
