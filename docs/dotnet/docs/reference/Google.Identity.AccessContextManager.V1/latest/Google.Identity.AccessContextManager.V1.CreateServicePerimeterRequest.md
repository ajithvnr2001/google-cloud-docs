---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.CreateServicePerimeterRequest
title: Identity Access Context Manager v1 API - Class CreateServicePerimeterRequest (2.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:30:34.364131+00:00
---

# Identity Access Context Manager v1 API - Class CreateServicePerimeterRequest (2.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.CreateServicePerimeterRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Identity Access Context Manager v1 API - Class CreateServicePerimeterRequest (2.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.CreateServicePerimeterRequest)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/2.5.0/Google.Identity.AccessContextManager.V1.CreateServicePerimeterRequest)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/2.4.0/Google.Identity.AccessContextManager.V1.CreateServicePerimeterRequest)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/2.3.0/Google.Identity.AccessContextManager.V1.CreateServicePerimeterRequest)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/2.2.0/Google.Identity.AccessContextManager.V1.CreateServicePerimeterRequest)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/2.1.0/Google.Identity.AccessContextManager.V1.CreateServicePerimeterRequest)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/2.0.0/Google.Identity.AccessContextManager.V1.CreateServicePerimeterRequest)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/1.5.0/Google.Identity.AccessContextManager.V1.CreateServicePerimeterRequest)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/1.4.0/Google.Identity.AccessContextManager.V1.CreateServicePerimeterRequest)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/1.3.0/Google.Identity.AccessContextManager.V1.CreateServicePerimeterRequest)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/1.2.0/Google.Identity.AccessContextManager.V1.CreateServicePerimeterRequest)


    
    
    public sealed class CreateServicePerimeterRequest : IMessage<CreateServicePerimeterRequest>, IEquatable<CreateServicePerimeterRequest>, IDeepCloneable<CreateServicePerimeterRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Identity Access Context Manager v1 API class CreateServicePerimeterRequest.

A request to create a `ServicePerimeter`.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CreateServicePerimeterRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CreateServicePerimeterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.CreateServicePerimeterRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CreateServicePerimeterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.CreateServicePerimeterRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CreateServicePerimeterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.CreateServicePerimeterRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Identity.AccessContextManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1)

## Assembly

Google.Identity.AccessContextManager.V1.dll

## Constructors 

### CreateServicePerimeterRequest()
    
    
    public CreateServicePerimeterRequest()

### CreateServicePerimeterRequest(CreateServicePerimeterRequest)
    
    
    public CreateServicePerimeterRequest(CreateServicePerimeterRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CreateServicePerimeterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.CreateServicePerimeterRequest)`  
  
  
## Properties 

### Parent
    
    
    public string Parent { get; set; }

Required. Resource name for the access policy which owns this [Service Perimeter] [google.identity.accesscontextmanager.v1.ServicePerimeter].

Format: `accessPolicies/{policy_id}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsAccessPolicyName
    
    
    public AccessPolicyName ParentAsAccessPolicyName { get; set; }

[AccessPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.AccessPolicyName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.CreateServicePerimeterRequest#Google_Identity_AccessContextManager_V1_CreateServicePerimeterRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AccessPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.AccessPolicyName)` |   
  
### ServicePerimeter
    
    
    public ServicePerimeter ServicePerimeter { get; set; }

Required. The [Service Perimeter] [google.identity.accesscontextmanager.v1.ServicePerimeter] to create. Syntactic correctness of the [Service Perimeter] [google.identity.accesscontextmanager.v1.ServicePerimeter] is a precondition for creation.

**Property Value**  
---  
**Type** | **Description**  
`[ServicePerimeter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.ServicePerimeter)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
