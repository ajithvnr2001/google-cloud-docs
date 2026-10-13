---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.SharedRegionalCertificateAuthority
title: Memorystore v1beta API - Class SharedRegionalCertificateAuthority (1.0.0-beta07) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:21:12.967621+00:00
---

# Memorystore v1beta API - Class SharedRegionalCertificateAuthority (1.0.0-beta07)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.SharedRegionalCertificateAuthority

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Memorystore v1beta API - Class SharedRegionalCertificateAuthority (1.0.0-beta07) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta07 (latest)  1.0.0-beta06 
    
    
    public sealed class SharedRegionalCertificateAuthority : IMessage<SharedRegionalCertificateAuthority>, IEquatable<SharedRegionalCertificateAuthority>, IDeepCloneable<SharedRegionalCertificateAuthority>, IBufferMessage, IMessage

Reference documentation and code samples for the Memorystore v1beta API class SharedRegionalCertificateAuthority.

Shared regional certificate authority for an instance.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SharedRegionalCertificateAuthority

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[SharedRegionalCertificateAuthority](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.SharedRegionalCertificateAuthority), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SharedRegionalCertificateAuthority](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.SharedRegionalCertificateAuthority), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[SharedRegionalCertificateAuthority](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.SharedRegionalCertificateAuthority), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Memorystore.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta)

## Assembly

Google.Cloud.Memorystore.V1Beta.dll

## Constructors 

### SharedRegionalCertificateAuthority()
    
    
    public SharedRegionalCertificateAuthority()

### SharedRegionalCertificateAuthority(SharedRegionalCertificateAuthority)
    
    
    public SharedRegionalCertificateAuthority(SharedRegionalCertificateAuthority other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SharedRegionalCertificateAuthority](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.SharedRegionalCertificateAuthority)`  
  
  
## Properties 

### ManagedServerCa
    
    
    public SharedRegionalCertificateAuthority.Types.RegionalManagedCertificateAuthority ManagedServerCa { get; set; }

CA certificate chains for memorystore managed server authentication.

**Property Value**  
---  
**Type** | **Description**  
`[SharedRegionalCertificateAuthority](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.SharedRegionalCertificateAuthority)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.SharedRegionalCertificateAuthority.Types)[RegionalManagedCertificateAuthority](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.SharedRegionalCertificateAuthority.Types.RegionalManagedCertificateAuthority)` |   
  
### Name
    
    
    public string Name { get; set; }

Identifier. Unique name of the resource in this scope including project and location using the form: `projects/{project}/locations/{location}/sharedRegionalCertificateAuthority`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ServerCaCase
    
    
    public SharedRegionalCertificateAuthority.ServerCaOneofCase ServerCaCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[SharedRegionalCertificateAuthority](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.SharedRegionalCertificateAuthority)[ServerCaOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.SharedRegionalCertificateAuthority.ServerCaOneofCase)` |   
  
### SharedRegionalCertificateAuthorityName
    
    
    public SharedRegionalCertificateAuthorityName SharedRegionalCertificateAuthorityName { get; set; }

[SharedRegionalCertificateAuthorityName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.SharedRegionalCertificateAuthorityName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.SharedRegionalCertificateAuthority#Google_Cloud_Memorystore_V1Beta_SharedRegionalCertificateAuthority_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[SharedRegionalCertificateAuthorityName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.SharedRegionalCertificateAuthorityName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
