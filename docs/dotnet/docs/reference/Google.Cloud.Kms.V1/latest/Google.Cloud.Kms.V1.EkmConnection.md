---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EkmConnection
title: Google Cloud Key Management Service v1 API - Class EkmConnection (3.27.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:49:04.039150+00:00
---

# Google Cloud Key Management Service v1 API - Class EkmConnection (3.27.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EkmConnection

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Key Management Service v1 API - Class EkmConnection (3.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.27.0 (latest)  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class EkmConnection : IMessage<EkmConnection>, IEquatable<EkmConnection>, IDeepCloneable<EkmConnection>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Key Management Service v1 API class EkmConnection.

An [EkmConnection][google.cloud.kms.v1.EkmConnection] represents an individual EKM connection. It can be used for creating [CryptoKeys][google.cloud.kms.v1.CryptoKey] and [CryptoKeyVersions][google.cloud.kms.v1.CryptoKeyVersion] with a [ProtectionLevel][google.cloud.kms.v1.ProtectionLevel] of [EXTERNAL_VPC][google.cloud.kms.v1.ProtectionLevel.EXTERNAL_VPC], as well as performing cryptographic operations using keys created within the [EkmConnection][google.cloud.kms.v1.EkmConnection].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > EkmConnection

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[EkmConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EkmConnection), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[EkmConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EkmConnection), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[EkmConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EkmConnection), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1)

## Assembly

Google.Cloud.Kms.V1.dll

## Constructors 

### EkmConnection()
    
    
    public EkmConnection()

### EkmConnection(EkmConnection)
    
    
    public EkmConnection(EkmConnection other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[EkmConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EkmConnection)`  
  
  
## Properties 

### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. The time at which the [EkmConnection][google.cloud.kms.v1.EkmConnection] was created.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### CryptoSpacePath
    
    
    public string CryptoSpacePath { get; set; }

Optional. Identifies the EKM Crypto Space that this [EkmConnection][google.cloud.kms.v1.EkmConnection] maps to. Note: This field is required if [KeyManagementMode][google.cloud.kms.v1.EkmConnection.KeyManagementMode] is [CLOUD_KMS][google.cloud.kms.v1.EkmConnection.KeyManagementMode.CLOUD_KMS].

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### EkmConnectionName
    
    
    public EkmConnectionName EkmConnectionName { get; set; }

[EkmConnectionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EkmConnectionName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EkmConnection#Google_Cloud_Kms_V1_EkmConnection_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[EkmConnectionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EkmConnectionName)` |   
  
### Etag
    
    
    public string Etag { get; set; }

Optional. Etag of the currently stored [EkmConnection][google.cloud.kms.v1.EkmConnection].

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### KeyManagementMode
    
    
    public EkmConnection.Types.KeyManagementMode KeyManagementMode { get; set; }

Optional. Describes who can perform control plane operations on the EKM. If unset, this defaults to [MANUAL][google.cloud.kms.v1.EkmConnection.KeyManagementMode.MANUAL].

**Property Value**  
---  
**Type** | **Description**  
`[EkmConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EkmConnection)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EkmConnection.Types)[KeyManagementMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EkmConnection.Types.KeyManagementMode)` |   
  
### Name
    
    
    public string Name { get; set; }

Output only. The resource name for the [EkmConnection][google.cloud.kms.v1.EkmConnection] in the format `projects/*/locations/*/ekmConnections/*`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ServiceResolvers
    
    
    public RepeatedField<EkmConnection.Types.ServiceResolver> ServiceResolvers { get; }

Optional. A list of [ServiceResolvers][google.cloud.kms.v1.EkmConnection.ServiceResolver] where the EKM can be reached. There should be one ServiceResolver per EKM replica. Currently, only a single [ServiceResolver][google.cloud.kms.v1.EkmConnection.ServiceResolver] is supported.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[EkmConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EkmConnection)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EkmConnection.Types)[ServiceResolver](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EkmConnection.Types.ServiceResolver)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
