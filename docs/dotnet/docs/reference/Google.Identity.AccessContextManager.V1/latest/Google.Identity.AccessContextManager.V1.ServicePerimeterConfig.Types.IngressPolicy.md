---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.ServicePerimeterConfig.Types.IngressPolicy
title: Identity Access Context Manager v1 API - Class ServicePerimeterConfig.Types.IngressPolicy (2.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:42:18.553502+00:00
---

# Identity Access Context Manager v1 API - Class ServicePerimeterConfig.Types.IngressPolicy (2.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.ServicePerimeterConfig.Types.IngressPolicy

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Identity Access Context Manager v1 API - Class ServicePerimeterConfig.Types.IngressPolicy (2.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.ServicePerimeterConfig.Types.IngressPolicy)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/2.5.0/Google.Identity.AccessContextManager.V1.ServicePerimeterConfig.Types.IngressPolicy)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/2.4.0/Google.Identity.AccessContextManager.V1.ServicePerimeterConfig.Types.IngressPolicy)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/2.3.0/Google.Identity.AccessContextManager.V1.ServicePerimeterConfig.Types.IngressPolicy)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/2.2.0/Google.Identity.AccessContextManager.V1.ServicePerimeterConfig.Types.IngressPolicy)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/2.1.0/Google.Identity.AccessContextManager.V1.ServicePerimeterConfig.Types.IngressPolicy)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/2.0.0/Google.Identity.AccessContextManager.V1.ServicePerimeterConfig.Types.IngressPolicy)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/1.5.0/Google.Identity.AccessContextManager.V1.ServicePerimeterConfig.Types.IngressPolicy)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/1.4.0/Google.Identity.AccessContextManager.V1.ServicePerimeterConfig.Types.IngressPolicy)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/1.3.0/Google.Identity.AccessContextManager.V1.ServicePerimeterConfig.Types.IngressPolicy)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/1.2.0/Google.Identity.AccessContextManager.V1.ServicePerimeterConfig.Types.IngressPolicy)


    
    
    public sealed class ServicePerimeterConfig.Types.IngressPolicy : IMessage<ServicePerimeterConfig.Types.IngressPolicy>, IEquatable<ServicePerimeterConfig.Types.IngressPolicy>, IDeepCloneable<ServicePerimeterConfig.Types.IngressPolicy>, IBufferMessage, IMessage

Reference documentation and code samples for the Identity Access Context Manager v1 API class ServicePerimeterConfig.Types.IngressPolicy.

Policy for ingress into [ServicePerimeter] [google.identity.accesscontextmanager.v1.ServicePerimeter].

[IngressPolicies] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy] match requests based on `ingress_from` and `ingress_to` stanzas. For an ingress policy to match, both the `ingress_from` and `ingress_to` stanzas must be matched. If an [IngressPolicy] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy] matches a request, the request is allowed through the perimeter boundary from outside the perimeter.

For example, access from the internet can be allowed either based on an [AccessLevel] [google.identity.accesscontextmanager.v1.AccessLevel] or, for traffic hosted on Google Cloud, the project of the source network. For access from private networks, using the project of the hosting network is required.

Individual ingress policies can be limited by restricting which services and/or actions they match using the `ingress_to` field.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ServicePerimeterConfig.Types.IngressPolicy

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ServicePerimeterConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.ServicePerimeterConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.ServicePerimeterConfig.Types)[IngressPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.ServicePerimeterConfig.Types.IngressPolicy), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ServicePerimeterConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.ServicePerimeterConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.ServicePerimeterConfig.Types)[IngressPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.ServicePerimeterConfig.Types.IngressPolicy), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ServicePerimeterConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.ServicePerimeterConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.ServicePerimeterConfig.Types)[IngressPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.ServicePerimeterConfig.Types.IngressPolicy), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Identity.AccessContextManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1)

## Assembly

Google.Identity.AccessContextManager.V1.dll

## Constructors 

### IngressPolicy()
    
    
    public IngressPolicy()

### IngressPolicy(IngressPolicy)
    
    
    public IngressPolicy(ServicePerimeterConfig.Types.IngressPolicy other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ServicePerimeterConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.ServicePerimeterConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.ServicePerimeterConfig.Types)[IngressPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.ServicePerimeterConfig.Types.IngressPolicy)`  
  
  
## Properties 

### IngressFrom
    
    
    public ServicePerimeterConfig.Types.IngressFrom IngressFrom { get; set; }

Defines the conditions on the source of a request causing this [IngressPolicy] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy] to apply.

**Property Value**  
---  
**Type** | **Description**  
`[ServicePerimeterConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.ServicePerimeterConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.ServicePerimeterConfig.Types)[IngressFrom](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.ServicePerimeterConfig.Types.IngressFrom)` |   
  
### IngressTo
    
    
    public ServicePerimeterConfig.Types.IngressTo IngressTo { get; set; }

Defines the conditions on the [ApiOperation] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.ApiOperation] and request destination that cause this [IngressPolicy] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.IngressPolicy] to apply.

**Property Value**  
---  
**Type** | **Description**  
`[ServicePerimeterConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.ServicePerimeterConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.ServicePerimeterConfig.Types)[IngressTo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.ServicePerimeterConfig.Types.IngressTo)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
