---
url: https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.Occurrence
title: Grafeas v1 API - Class Occurrence (3.16.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:05:49.151083+00:00
---

# Grafeas v1 API - Class Occurrence (3.16.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.Occurrence

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Grafeas v1 API - Class Occurrence (3.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.16.0 (latest)  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class Occurrence : IMessage<Occurrence>, IEquatable<Occurrence>, IDeepCloneable<Occurrence>, IBufferMessage, IMessage

Reference documentation and code samples for the Grafeas v1 API class Occurrence.

An instance of an analysis type that has been found on a resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Occurrence

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Occurrence](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.Occurrence), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Occurrence](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.Occurrence), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Occurrence](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.Occurrence), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Grafeas.V1](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1)

## Assembly

Grafeas.V1.dll

## Constructors 

### Occurrence()
    
    
    public Occurrence()

### Occurrence(Occurrence)
    
    
    public Occurrence(Occurrence other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Occurrence](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.Occurrence)`  
  
  
## Properties 

### Attestation
    
    
    public AttestationOccurrence Attestation { get; set; }

Describes an attestation of an artifact.

**Property Value**  
---  
**Type** | **Description**  
`[AttestationOccurrence](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.AttestationOccurrence)` |   
  
### Build
    
    
    public BuildOccurrence Build { get; set; }

Describes a verifiable build.

**Property Value**  
---  
**Type** | **Description**  
`[BuildOccurrence](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.BuildOccurrence)` |   
  
### Compliance
    
    
    public ComplianceOccurrence Compliance { get; set; }

Describes a compliance violation on a linked resource.

**Property Value**  
---  
**Type** | **Description**  
`[ComplianceOccurrence](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ComplianceOccurrence)` |   
  
### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. The time this occurrence was created.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Deployment
    
    
    public DeploymentOccurrence Deployment { get; set; }

Describes the deployment of an artifact on a runtime.

**Property Value**  
---  
**Type** | **Description**  
`[DeploymentOccurrence](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.DeploymentOccurrence)` |   
  
### DetailsCase
    
    
    public Occurrence.DetailsOneofCase DetailsCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[Occurrence](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.Occurrence)[DetailsOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.Occurrence.DetailsOneofCase)` |   
  
### Discovery
    
    
    public DiscoveryOccurrence Discovery { get; set; }

Describes when a resource was discovered.

**Property Value**  
---  
**Type** | **Description**  
`[DiscoveryOccurrence](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.DiscoveryOccurrence)` |   
  
### DsseAttestation
    
    
    public DSSEAttestationOccurrence DsseAttestation { get; set; }

Describes an attestation of an artifact using dsse.

**Property Value**  
---  
**Type** | **Description**  
`[DSSEAttestationOccurrence](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.DSSEAttestationOccurrence)` |   
  
### Envelope
    
    
    public Envelope Envelope { get; set; }

<https://github.com/secure-systems-lab/dsse>

**Property Value**  
---  
**Type** | **Description**  
`[Envelope](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.Envelope)` |   
  
### Image
    
    
    public ImageOccurrence Image { get; set; }

Describes how this resource derives from the basis in the associated note.

**Property Value**  
---  
**Type** | **Description**  
`[ImageOccurrence](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ImageOccurrence)` |   
  
### Kind
    
    
    public NoteKind Kind { get; set; }

Output only. This explicitly denotes which of the occurrence details are specified. This field can be used as a filter in list requests.

**Property Value**  
---  
**Type** | **Description**  
`[NoteKind](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.NoteKind)` |   
  
### Name
    
    
    public string Name { get; set; }

Output only. The name of the occurrence in the form of `projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### NoteName
    
    
    public string NoteName { get; set; }

Required. Immutable. The analysis note associated with this occurrence, in the form of `projects/[PROVIDER_ID]/notes/[NOTE_ID]`. This field can be used as a filter in list requests.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OccurrenceName
    
    
    public OccurrenceName OccurrenceName { get; set; }

[OccurrenceName](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.OccurrenceName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.Occurrence#Grafeas_V1_Occurrence_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[OccurrenceName](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.OccurrenceName)` |   
  
### Package
    
    
    public PackageOccurrence Package { get; set; }

Describes the installation of a package on the linked resource.

**Property Value**  
---  
**Type** | **Description**  
`[PackageOccurrence](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.PackageOccurrence)` |   
  
### Remediation
    
    
    public string Remediation { get; set; }

A description of actions that can be taken to remedy the note.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ResourceUri
    
    
    public string ResourceUri { get; set; }

Required. Immutable. A URI that represents the resource for which the occurrence applies. For example, `https://gcr.io/project/image@sha256:123abc` for a Docker image.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SbomReference
    
    
    public SBOMReferenceOccurrence SbomReference { get; set; }

Describes a specific SBOM reference occurrences.

**Property Value**  
---  
**Type** | **Description**  
`[SBOMReferenceOccurrence](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.SBOMReferenceOccurrence)` |   
  
### Secret
    
    
    public SecretOccurrence Secret { get; set; }

Describes a secret.

**Property Value**  
---  
**Type** | **Description**  
`[SecretOccurrence](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.SecretOccurrence)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. The time this occurrence was last updated.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Upgrade
    
    
    public UpgradeOccurrence Upgrade { get; set; }

Describes an available package upgrade on the linked resource.

**Property Value**  
---  
**Type** | **Description**  
`[UpgradeOccurrence](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.UpgradeOccurrence)` |   
  
### Vulnerability
    
    
    public VulnerabilityOccurrence Vulnerability { get; set; }

Describes a security vulnerability.

**Property Value**  
---  
**Type** | **Description**  
`[VulnerabilityOccurrence](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.VulnerabilityOccurrence)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
