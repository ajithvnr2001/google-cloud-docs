---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.ValidateAttestationOccurrenceRequest
title: Binary Authorization v1 API - Class ValidateAttestationOccurrenceRequest (2.7.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:17:51.909931+00:00
---

# Binary Authorization v1 API - Class ValidateAttestationOccurrenceRequest (2.7.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.ValidateAttestationOccurrenceRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Binary Authorization v1 API - Class ValidateAttestationOccurrenceRequest (2.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.7.0 (latest)  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.0.0 
    
    
    public sealed class ValidateAttestationOccurrenceRequest : IMessage<ValidateAttestationOccurrenceRequest>, IEquatable<ValidateAttestationOccurrenceRequest>, IDeepCloneable<ValidateAttestationOccurrenceRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Binary Authorization v1 API class ValidateAttestationOccurrenceRequest.

Request message for [ValidationHelperV1.ValidateAttestationOccurrence][google.cloud.binaryauthorization.v1.ValidationHelperV1.ValidateAttestationOccurrence].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ValidateAttestationOccurrenceRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ValidateAttestationOccurrenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.ValidateAttestationOccurrenceRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ValidateAttestationOccurrenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.ValidateAttestationOccurrenceRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ValidateAttestationOccurrenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.ValidateAttestationOccurrenceRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.BinaryAuthorization.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1)

## Assembly

Google.Cloud.BinaryAuthorization.V1.dll

## Constructors 

### ValidateAttestationOccurrenceRequest()
    
    
    public ValidateAttestationOccurrenceRequest()

### ValidateAttestationOccurrenceRequest(ValidateAttestationOccurrenceRequest)
    
    
    public ValidateAttestationOccurrenceRequest(ValidateAttestationOccurrenceRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ValidateAttestationOccurrenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.ValidateAttestationOccurrenceRequest)`  
  
  
## Properties 

### Attestation
    
    
    public AttestationOccurrence Attestation { get; set; }

Required. An [AttestationOccurrence][grafeas.v1.AttestationOccurrence] to be checked that it can be verified by the `Attestor`. It does not have to be an existing entity in Container Analysis. It must otherwise be a valid `AttestationOccurrence`.

**Property Value**  
---  
**Type** | **Description**  
`[AttestationOccurrence](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.AttestationOccurrence.html)` |   
  
### Attestor
    
    
    public string Attestor { get; set; }

Required. The resource name of the [Attestor][google.cloud.binaryauthorization.v1.Attestor] of the [occurrence][grafeas.v1.Occurrence], in the format `projects/*/attestors/*`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OccurrenceNote
    
    
    public string OccurrenceNote { get; set; }

Required. The resource name of the [Note][grafeas.v1.Note] to which the containing [Occurrence][grafeas.v1.Occurrence] is associated.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OccurrenceResourceUri
    
    
    public string OccurrenceResourceUri { get; set; }

Required. The URI of the artifact (e.g. container image) that is the subject of the containing [Occurrence][grafeas.v1.Occurrence].

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
