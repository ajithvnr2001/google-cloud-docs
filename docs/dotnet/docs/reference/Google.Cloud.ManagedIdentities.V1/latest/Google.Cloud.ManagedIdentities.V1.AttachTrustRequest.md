---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.AttachTrustRequest
title: Managed Service for Microsoft Active Directory v1 API - Class AttachTrustRequest (3.4.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:20:38.232333+00:00
---

# Managed Service for Microsoft Active Directory v1 API - Class AttachTrustRequest (3.4.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.AttachTrustRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Managed Service for Microsoft Active Directory v1 API - Class AttachTrustRequest (3.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.4.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.AttachTrustRequest)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/3.3.0/Google.Cloud.ManagedIdentities.V1.AttachTrustRequest)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/3.2.0/Google.Cloud.ManagedIdentities.V1.AttachTrustRequest)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/3.1.0/Google.Cloud.ManagedIdentities.V1.AttachTrustRequest)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/3.0.0/Google.Cloud.ManagedIdentities.V1.AttachTrustRequest)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/2.3.0/Google.Cloud.ManagedIdentities.V1.AttachTrustRequest)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/2.2.0/Google.Cloud.ManagedIdentities.V1.AttachTrustRequest)


    
    
    public sealed class AttachTrustRequest : IMessage<AttachTrustRequest>, IEquatable<AttachTrustRequest>, IDeepCloneable<AttachTrustRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Managed Service for Microsoft Active Directory v1 API class AttachTrustRequest.

Request message for [AttachTrust][google.cloud.managedidentities.v1.AttachTrust]

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AttachTrustRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AttachTrustRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.AttachTrustRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AttachTrustRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.AttachTrustRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AttachTrustRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.AttachTrustRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ManagedIdentities.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1)

## Assembly

Google.Cloud.ManagedIdentities.V1.dll

## Constructors 

### AttachTrustRequest()
    
    
    public AttachTrustRequest()

### AttachTrustRequest(AttachTrustRequest)
    
    
    public AttachTrustRequest(AttachTrustRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AttachTrustRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.AttachTrustRequest)`  
  
  
## Properties 

### DomainName
    
    
    public DomainName DomainName { get; set; }

[DomainName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.DomainName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.AttachTrustRequest#Google_Cloud_ManagedIdentities_V1_AttachTrustRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[DomainName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.DomainName)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. The resource domain name, project name and location using the form: `projects/{project_id}/locations/global/domains/{domain_name}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Trust
    
    
    public Trust Trust { get; set; }

Required. The domain trust resource.

**Property Value**  
---  
**Type** | **Description**  
`[Trust](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedIdentities.V1/latest/Google.Cloud.ManagedIdentities.V1.Trust)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
