---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.AttestorPublicKey
title: Binary Authorization v1beta1 API - Class AttestorPublicKey (2.0.0-beta10) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:28:47.921296+00:00
---

# Binary Authorization v1beta1 API - Class AttestorPublicKey (2.0.0-beta10)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.AttestorPublicKey

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Binary Authorization v1beta1 API - Class AttestorPublicKey (2.0.0-beta10) Stay organized with collections  Save and categorize content based on your preferences. 

2.0.0-beta10 (latest)  2.0.0-beta09  1.0.0-beta05 
    
    
    public sealed class AttestorPublicKey : IMessage<AttestorPublicKey>, IEquatable<AttestorPublicKey>, IDeepCloneable<AttestorPublicKey>, IBufferMessage, IMessage

Reference documentation and code samples for the Binary Authorization v1beta1 API class AttestorPublicKey.

An [attestor public key][google.cloud.binaryauthorization.v1beta1.AttestorPublicKey] that will be used to verify attestations signed by this attestor.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AttestorPublicKey

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AttestorPublicKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.AttestorPublicKey), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AttestorPublicKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.AttestorPublicKey), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AttestorPublicKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.AttestorPublicKey), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.BinaryAuthorization.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1)

## Assembly

Google.Cloud.BinaryAuthorization.V1Beta1.dll

## Constructors 

### AttestorPublicKey()
    
    
    public AttestorPublicKey()

### AttestorPublicKey(AttestorPublicKey)
    
    
    public AttestorPublicKey(AttestorPublicKey other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AttestorPublicKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.AttestorPublicKey)`  
  
  
## Properties 

### AsciiArmoredPgpPublicKey
    
    
    public string AsciiArmoredPgpPublicKey { get; set; }

ASCII-armored representation of a PGP public key, as the entire output by the command `gpg --export --armor foo@example.com` (either LF or CRLF line endings). When using this field, `id` should be left blank. The BinAuthz API handlers will calculate the ID and fill it in automatically. BinAuthz computes this ID as the OpenPGP RFC4880 V4 fingerprint, represented as upper-case hex. If `id` is provided by the caller, it will be overwritten by the API-calculated ID.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Comment
    
    
    public string Comment { get; set; }

Optional. A descriptive comment. This field may be updated.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HasAsciiArmoredPgpPublicKey
    
    
    public bool HasAsciiArmoredPgpPublicKey { get; }

Gets whether the "ascii_armored_pgp_public_key" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Id
    
    
    public string Id { get; set; }

The ID of this public key. Signatures verified by BinAuthz must include the ID of the public key that can be used to verify them, and that ID must match the contents of this field exactly. Additional restrictions on this field can be imposed based on which public key type is encapsulated. See the documentation on `public_key` cases below for details.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PkixPublicKey
    
    
    public PkixPublicKey PkixPublicKey { get; set; }

A raw PKIX SubjectPublicKeyInfo format public key.

NOTE: `id` may be explicitly provided by the caller when using this type of public key, but it MUST be a valid RFC3986 URI. If `id` is left blank, a default one will be computed based on the digest of the DER encoding of the public key.

**Property Value**  
---  
**Type** | **Description**  
`[PkixPublicKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.PkixPublicKey)` |   
  
### PublicKeyCase
    
    
    public AttestorPublicKey.PublicKeyOneofCase PublicKeyCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[AttestorPublicKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.AttestorPublicKey)[PublicKeyOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.AttestorPublicKey.PublicKeyOneofCase)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
