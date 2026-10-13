---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.CertificateAuthority
title: Google Cloud Memorystore for Redis (cluster management) v1 API - Class CertificateAuthority (1.9.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:17:06.729137+00:00
---

# Google Cloud Memorystore for Redis (cluster management) v1 API - Class CertificateAuthority (1.9.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.CertificateAuthority

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Memorystore for Redis (cluster management) v1 API - Class CertificateAuthority (1.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.0 (latest)  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class CertificateAuthority : IMessage<CertificateAuthority>, IEquatable<CertificateAuthority>, IDeepCloneable<CertificateAuthority>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Memorystore for Redis (cluster management) v1 API class CertificateAuthority.

Redis cluster certificate authority

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CertificateAuthority

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CertificateAuthority](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.CertificateAuthority), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CertificateAuthority](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.CertificateAuthority), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CertificateAuthority](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.CertificateAuthority), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Redis.Cluster.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1)

## Assembly

Google.Cloud.Redis.Cluster.V1.dll

## Constructors 

### CertificateAuthority()
    
    
    public CertificateAuthority()

### CertificateAuthority(CertificateAuthority)
    
    
    public CertificateAuthority(CertificateAuthority other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CertificateAuthority](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.CertificateAuthority)`  
  
  
## Properties 

### CertificateAuthorityName
    
    
    public CertificateAuthorityName CertificateAuthorityName { get; set; }

[CertificateAuthorityName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.CertificateAuthorityName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.CertificateAuthority#Google_Cloud_Redis_Cluster_V1_CertificateAuthority_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[CertificateAuthorityName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.CertificateAuthorityName)` |   
  
### ManagedServerCa
    
    
    public CertificateAuthority.Types.ManagedCertificateAuthority ManagedServerCa { get; set; }

**Property Value**  
---  
**Type** | **Description**  
`[CertificateAuthority](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.CertificateAuthority)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.CertificateAuthority.Types)[ManagedCertificateAuthority](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.CertificateAuthority.Types.ManagedCertificateAuthority)` |   
  
### Name
    
    
    public string Name { get; set; }

Identifier. Unique name of the resource in this scope including project, location and cluster using the form: `projects/{project}/locations/{location}/clusters/{cluster}/certificateAuthority`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ServerCaCase
    
    
    public CertificateAuthority.ServerCaOneofCase ServerCaCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[CertificateAuthority](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.CertificateAuthority)[ServerCaOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/Google.Cloud.Redis.Cluster.V1.CertificateAuthority.ServerCaOneofCase)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
