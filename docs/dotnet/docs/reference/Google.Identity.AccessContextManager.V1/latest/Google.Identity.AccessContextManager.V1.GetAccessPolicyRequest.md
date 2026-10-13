---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.GetAccessPolicyRequest
title: Identity Access Context Manager v1 API - Class GetAccessPolicyRequest (2.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:43:42.782203+00:00
---

# Identity Access Context Manager v1 API - Class GetAccessPolicyRequest (2.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.GetAccessPolicyRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Identity Access Context Manager v1 API - Class GetAccessPolicyRequest (2.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.GetAccessPolicyRequest)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/2.5.0/Google.Identity.AccessContextManager.V1.GetAccessPolicyRequest)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/2.4.0/Google.Identity.AccessContextManager.V1.GetAccessPolicyRequest)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/2.3.0/Google.Identity.AccessContextManager.V1.GetAccessPolicyRequest)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/2.2.0/Google.Identity.AccessContextManager.V1.GetAccessPolicyRequest)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/2.1.0/Google.Identity.AccessContextManager.V1.GetAccessPolicyRequest)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/2.0.0/Google.Identity.AccessContextManager.V1.GetAccessPolicyRequest)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/1.5.0/Google.Identity.AccessContextManager.V1.GetAccessPolicyRequest)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/1.4.0/Google.Identity.AccessContextManager.V1.GetAccessPolicyRequest)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/1.3.0/Google.Identity.AccessContextManager.V1.GetAccessPolicyRequest)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/1.2.0/Google.Identity.AccessContextManager.V1.GetAccessPolicyRequest)


    
    
    public sealed class GetAccessPolicyRequest : IMessage<GetAccessPolicyRequest>, IEquatable<GetAccessPolicyRequest>, IDeepCloneable<GetAccessPolicyRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Identity Access Context Manager v1 API class GetAccessPolicyRequest.

A request to get a particular `AccessPolicy`.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GetAccessPolicyRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GetAccessPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.GetAccessPolicyRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GetAccessPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.GetAccessPolicyRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GetAccessPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.GetAccessPolicyRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Identity.AccessContextManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1)

## Assembly

Google.Identity.AccessContextManager.V1.dll

## Constructors 

### GetAccessPolicyRequest()
    
    
    public GetAccessPolicyRequest()

### GetAccessPolicyRequest(GetAccessPolicyRequest)
    
    
    public GetAccessPolicyRequest(GetAccessPolicyRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GetAccessPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.GetAccessPolicyRequest)`  
  
  
## Properties 

### AccessPolicyName
    
    
    public AccessPolicyName AccessPolicyName { get; set; }

[AccessPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.AccessPolicyName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.GetAccessPolicyRequest#Google_Identity_AccessContextManager_V1_GetAccessPolicyRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AccessPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.AccessPolicyName)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. Resource name for the access policy to get.

Format `accessPolicies/{policy_id}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
