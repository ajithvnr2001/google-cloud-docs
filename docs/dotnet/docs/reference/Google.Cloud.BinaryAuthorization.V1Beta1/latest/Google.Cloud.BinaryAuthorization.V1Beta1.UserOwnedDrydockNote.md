---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.UserOwnedDrydockNote
title: Binary Authorization v1beta1 API - Class UserOwnedDrydockNote (2.0.0-beta10) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:28:56.238080+00:00
---

# Binary Authorization v1beta1 API - Class UserOwnedDrydockNote (2.0.0-beta10)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.UserOwnedDrydockNote

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Binary Authorization v1beta1 API - Class UserOwnedDrydockNote (2.0.0-beta10) Stay organized with collections  Save and categorize content based on your preferences. 

2.0.0-beta10 (latest)  2.0.0-beta09  1.0.0-beta05 
    
    
    public sealed class UserOwnedDrydockNote : IMessage<UserOwnedDrydockNote>, IEquatable<UserOwnedDrydockNote>, IDeepCloneable<UserOwnedDrydockNote>, IBufferMessage, IMessage

Reference documentation and code samples for the Binary Authorization v1beta1 API class UserOwnedDrydockNote.

An [user owned drydock note][google.cloud.binaryauthorization.v1beta1.UserOwnedDrydockNote] references a Drydock ATTESTATION_AUTHORITY Note created by the user.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UserOwnedDrydockNote

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[UserOwnedDrydockNote](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.UserOwnedDrydockNote), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[UserOwnedDrydockNote](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.UserOwnedDrydockNote), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[UserOwnedDrydockNote](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.UserOwnedDrydockNote), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.BinaryAuthorization.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1)

## Assembly

Google.Cloud.BinaryAuthorization.V1Beta1.dll

## Constructors 

### UserOwnedDrydockNote()
    
    
    public UserOwnedDrydockNote()

### UserOwnedDrydockNote(UserOwnedDrydockNote)
    
    
    public UserOwnedDrydockNote(UserOwnedDrydockNote other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[UserOwnedDrydockNote](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.UserOwnedDrydockNote)`  
  
  
## Properties 

### DelegationServiceAccountEmail
    
    
    public string DelegationServiceAccountEmail { get; set; }

Output only. This field will contain the service account email address that this Attestor will use as the principal when querying Container Analysis. Attestor administrators must grant this service account the IAM role needed to read attestations from the [note_reference][Note] in Container Analysis (`containeranalysis.notes.occurrences.viewer`).

This email address is fixed for the lifetime of the Attestor, but callers should not make any other assumptions about the service account email; future versions may use an email based on a different naming pattern.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### NoteReference
    
    
    public string NoteReference { get; set; }

Required. The Drydock resource name of a ATTESTATION_AUTHORITY Note, created by the user, in the format: `projects/*/notes/*` (or the legacy `providers/*/notes/*`). This field may not be updated.

An attestation by this attestor is stored as a Drydock ATTESTATION_AUTHORITY Occurrence that names a container image and that links to this Note. Drydock is an external dependency.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PublicKeys
    
    
    public RepeatedField<AttestorPublicKey> PublicKeys { get; }

Optional. Public keys that verify attestations signed by this attestor. This field may be updated.

If this field is non-empty, one of the specified public keys must verify that an attestation was signed by this attestor for the image specified in the admission request.

If this field is empty, this attestor always returns that no valid attestations exist.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[AttestorPublicKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.AttestorPublicKey)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
