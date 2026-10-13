---
url: https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-Occurrence/
title: Grafeas V1 API - Class Grafeas::V1::Occurrence (v1.10.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:41:12.641982+00:00
---

# Grafeas V1 API - Class Grafeas::V1::Occurrence (v1.10.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-Occurrence/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Grafeas V1 API - Class Grafeas::V1::Occurrence (v1.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.10.1 (latest)  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.0  1.1.1  1.0.0  0.16.1  0.15.0  0.14.2  0.13.0  0.12.1  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.1  0.5.0  0.4.0  0.3.1 

Reference documentation and code samples for the Grafeas V1 API class Grafeas::V1::Occurrence.

An instance of an analysis type that has been found on a resource.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #attestation
    
    
    def attestation() -> ::Grafeas::V1::AttestationOccurrence

**Returns**

  * ([::Grafeas::V1::AttestationOccurrence](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-AttestationOccurrence)) — Describes an attestation of an artifact.

Note: The following fields are mutually exclusive: `attestation`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `upgrade`, `compliance`, `dsse_attestation`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #attestation=
    
    
    def attestation=(value) -> ::Grafeas::V1::AttestationOccurrence

**Parameter**

  * **value** ([::Grafeas::V1::AttestationOccurrence](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-AttestationOccurrence)) — Describes an attestation of an artifact.

Note: The following fields are mutually exclusive: `attestation`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `upgrade`, `compliance`, `dsse_attestation`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Grafeas::V1::AttestationOccurrence](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-AttestationOccurrence)) — Describes an attestation of an artifact.

Note: The following fields are mutually exclusive: `attestation`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `upgrade`, `compliance`, `dsse_attestation`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #build
    
    
    def build() -> ::Grafeas::V1::BuildOccurrence

**Returns**

  * ([::Grafeas::V1::BuildOccurrence](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-BuildOccurrence)) — Describes a verifiable build.

Note: The following fields are mutually exclusive: `build`, `vulnerability`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #build=
    
    
    def build=(value) -> ::Grafeas::V1::BuildOccurrence

**Parameter**

  * **value** ([::Grafeas::V1::BuildOccurrence](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-BuildOccurrence)) — Describes a verifiable build.

Note: The following fields are mutually exclusive: `build`, `vulnerability`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Grafeas::V1::BuildOccurrence](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-BuildOccurrence)) — Describes a verifiable build.

Note: The following fields are mutually exclusive: `build`, `vulnerability`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #compliance
    
    
    def compliance() -> ::Grafeas::V1::ComplianceOccurrence

**Returns**

  * ([::Grafeas::V1::ComplianceOccurrence](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-ComplianceOccurrence)) — Describes a compliance violation on a linked resource.

Note: The following fields are mutually exclusive: `compliance`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `dsse_attestation`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #compliance=
    
    
    def compliance=(value) -> ::Grafeas::V1::ComplianceOccurrence

**Parameter**

  * **value** ([::Grafeas::V1::ComplianceOccurrence](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-ComplianceOccurrence)) — Describes a compliance violation on a linked resource.

Note: The following fields are mutually exclusive: `compliance`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `dsse_attestation`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Grafeas::V1::ComplianceOccurrence](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-ComplianceOccurrence)) — Describes a compliance violation on a linked resource.

Note: The following fields are mutually exclusive: `compliance`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `dsse_attestation`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time this occurrence was created. 



### #create_time=
    
    
    def create_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time this occurrence was created. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time this occurrence was created. 



### #deployment
    
    
    def deployment() -> ::Grafeas::V1::DeploymentOccurrence

**Returns**

  * ([::Grafeas::V1::DeploymentOccurrence](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-DeploymentOccurrence)) — Describes the deployment of an artifact on a runtime.

Note: The following fields are mutually exclusive: `deployment`, `vulnerability`, `build`, `image`, `package`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #deployment=
    
    
    def deployment=(value) -> ::Grafeas::V1::DeploymentOccurrence

**Parameter**

  * **value** ([::Grafeas::V1::DeploymentOccurrence](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-DeploymentOccurrence)) — Describes the deployment of an artifact on a runtime.

Note: The following fields are mutually exclusive: `deployment`, `vulnerability`, `build`, `image`, `package`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Grafeas::V1::DeploymentOccurrence](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-DeploymentOccurrence)) — Describes the deployment of an artifact on a runtime.

Note: The following fields are mutually exclusive: `deployment`, `vulnerability`, `build`, `image`, `package`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #discovery
    
    
    def discovery() -> ::Grafeas::V1::DiscoveryOccurrence

**Returns**

  * ([::Grafeas::V1::DiscoveryOccurrence](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-DiscoveryOccurrence)) — Describes when a resource was discovered.

Note: The following fields are mutually exclusive: `discovery`, `vulnerability`, `build`, `image`, `package`, `deployment`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #discovery=
    
    
    def discovery=(value) -> ::Grafeas::V1::DiscoveryOccurrence

**Parameter**

  * **value** ([::Grafeas::V1::DiscoveryOccurrence](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-DiscoveryOccurrence)) — Describes when a resource was discovered.

Note: The following fields are mutually exclusive: `discovery`, `vulnerability`, `build`, `image`, `package`, `deployment`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Grafeas::V1::DiscoveryOccurrence](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-DiscoveryOccurrence)) — Describes when a resource was discovered.

Note: The following fields are mutually exclusive: `discovery`, `vulnerability`, `build`, `image`, `package`, `deployment`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #dsse_attestation
    
    
    def dsse_attestation() -> ::Grafeas::V1::DSSEAttestationOccurrence

**Returns**

  * ([::Grafeas::V1::DSSEAttestationOccurrence](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-DSSEAttestationOccurrence)) — Describes an attestation of an artifact using dsse.

Note: The following fields are mutually exclusive: `dsse_attestation`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #dsse_attestation=
    
    
    def dsse_attestation=(value) -> ::Grafeas::V1::DSSEAttestationOccurrence

**Parameter**

  * **value** ([::Grafeas::V1::DSSEAttestationOccurrence](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-DSSEAttestationOccurrence)) — Describes an attestation of an artifact using dsse.

Note: The following fields are mutually exclusive: `dsse_attestation`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Grafeas::V1::DSSEAttestationOccurrence](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-DSSEAttestationOccurrence)) — Describes an attestation of an artifact using dsse.

Note: The following fields are mutually exclusive: `dsse_attestation`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #envelope
    
    
    def envelope() -> ::Grafeas::V1::Envelope

**Returns**

  * ([::Grafeas::V1::Envelope](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-Envelope)) — https://github.com/secure-systems-lab/dsse 



### #envelope=
    
    
    def envelope=(value) -> ::Grafeas::V1::Envelope

**Parameter**

  * **value** ([::Grafeas::V1::Envelope](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-Envelope)) — https://github.com/secure-systems-lab/dsse 



**Returns**

  * ([::Grafeas::V1::Envelope](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-Envelope)) — https://github.com/secure-systems-lab/dsse 



### #image
    
    
    def image() -> ::Grafeas::V1::ImageOccurrence

**Returns**

  * ([::Grafeas::V1::ImageOccurrence](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-ImageOccurrence)) — Describes how this resource derives from the basis in the associated note.

Note: The following fields are mutually exclusive: `image`, `vulnerability`, `build`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #image=
    
    
    def image=(value) -> ::Grafeas::V1::ImageOccurrence

**Parameter**

  * **value** ([::Grafeas::V1::ImageOccurrence](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-ImageOccurrence)) — Describes how this resource derives from the basis in the associated note.

Note: The following fields are mutually exclusive: `image`, `vulnerability`, `build`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Grafeas::V1::ImageOccurrence](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-ImageOccurrence)) — Describes how this resource derives from the basis in the associated note.

Note: The following fields are mutually exclusive: `image`, `vulnerability`, `build`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #kind
    
    
    def kind() -> ::Grafeas::V1::NoteKind

**Returns**

  * ([::Grafeas::V1::NoteKind](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-NoteKind)) — Output only. This explicitly denotes which of the occurrence details are specified. This field can be used as a filter in list requests. 



### #kind=
    
    
    def kind=(value) -> ::Grafeas::V1::NoteKind

**Parameter**

  * **value** ([::Grafeas::V1::NoteKind](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-NoteKind)) — Output only. This explicitly denotes which of the occurrence details are specified. This field can be used as a filter in list requests. 



**Returns**

  * ([::Grafeas::V1::NoteKind](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-NoteKind)) — Output only. This explicitly denotes which of the occurrence details are specified. This field can be used as a filter in list requests. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. The name of the occurrence in the form of `projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]`. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. The name of the occurrence in the form of `projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]`. 



**Returns**

  * (::String) — Output only. The name of the occurrence in the form of `projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]`. 



### #note_name
    
    
    def note_name() -> ::String

**Returns**

  * (::String) — Required. Immutable. The analysis note associated with this occurrence, in the form of `projects/[PROVIDER_ID]/notes/[NOTE_ID]`. This field can be used as a filter in list requests. 



### #note_name=
    
    
    def note_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Immutable. The analysis note associated with this occurrence, in the form of `projects/[PROVIDER_ID]/notes/[NOTE_ID]`. This field can be used as a filter in list requests. 



**Returns**

  * (::String) — Required. Immutable. The analysis note associated with this occurrence, in the form of `projects/[PROVIDER_ID]/notes/[NOTE_ID]`. This field can be used as a filter in list requests. 



### #package
    
    
    def package() -> ::Grafeas::V1::PackageOccurrence

**Returns**

  * ([::Grafeas::V1::PackageOccurrence](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-PackageOccurrence)) — Describes the installation of a package on the linked resource.

Note: The following fields are mutually exclusive: `package`, `vulnerability`, `build`, `image`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #package=
    
    
    def package=(value) -> ::Grafeas::V1::PackageOccurrence

**Parameter**

  * **value** ([::Grafeas::V1::PackageOccurrence](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-PackageOccurrence)) — Describes the installation of a package on the linked resource.

Note: The following fields are mutually exclusive: `package`, `vulnerability`, `build`, `image`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Grafeas::V1::PackageOccurrence](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-PackageOccurrence)) — Describes the installation of a package on the linked resource.

Note: The following fields are mutually exclusive: `package`, `vulnerability`, `build`, `image`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #remediation
    
    
    def remediation() -> ::String

**Returns**

  * (::String) — A description of actions that can be taken to remedy the note. 



### #remediation=
    
    
    def remediation=(value) -> ::String

**Parameter**

  * **value** (::String) — A description of actions that can be taken to remedy the note. 



**Returns**

  * (::String) — A description of actions that can be taken to remedy the note. 



### #resource_uri
    
    
    def resource_uri() -> ::String

**Returns**

  * (::String) — Required. Immutable. A URI that represents the resource for which the occurrence applies. For example, `https://gcr.io/project/image@sha256:123abc` for a Docker image. 



### #resource_uri=
    
    
    def resource_uri=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Immutable. A URI that represents the resource for which the occurrence applies. For example, `https://gcr.io/project/image@sha256:123abc` for a Docker image. 



**Returns**

  * (::String) — Required. Immutable. A URI that represents the resource for which the occurrence applies. For example, `https://gcr.io/project/image@sha256:123abc` for a Docker image. 



### #sbom_reference
    
    
    def sbom_reference() -> ::Grafeas::V1::SBOMReferenceOccurrence

**Returns**

  * ([::Grafeas::V1::SBOMReferenceOccurrence](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-SBOMReferenceOccurrence)) — Describes a specific SBOM reference occurrences.

Note: The following fields are mutually exclusive: `sbom_reference`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #sbom_reference=
    
    
    def sbom_reference=(value) -> ::Grafeas::V1::SBOMReferenceOccurrence

**Parameter**

  * **value** ([::Grafeas::V1::SBOMReferenceOccurrence](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-SBOMReferenceOccurrence)) — Describes a specific SBOM reference occurrences.

Note: The following fields are mutually exclusive: `sbom_reference`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Grafeas::V1::SBOMReferenceOccurrence](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-SBOMReferenceOccurrence)) — Describes a specific SBOM reference occurrences.

Note: The following fields are mutually exclusive: `sbom_reference`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #secret
    
    
    def secret() -> ::Grafeas::V1::SecretOccurrence

**Returns**

  * ([::Grafeas::V1::SecretOccurrence](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-SecretOccurrence)) — Describes a secret.

Note: The following fields are mutually exclusive: `secret`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `sbom_reference`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #secret=
    
    
    def secret=(value) -> ::Grafeas::V1::SecretOccurrence

**Parameter**

  * **value** ([::Grafeas::V1::SecretOccurrence](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-SecretOccurrence)) — Describes a secret.

Note: The following fields are mutually exclusive: `secret`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `sbom_reference`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Grafeas::V1::SecretOccurrence](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-SecretOccurrence)) — Describes a secret.

Note: The following fields are mutually exclusive: `secret`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `sbom_reference`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time this occurrence was last updated. 



### #update_time=
    
    
    def update_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time this occurrence was last updated. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time this occurrence was last updated. 



### #upgrade
    
    
    def upgrade() -> ::Grafeas::V1::UpgradeOccurrence

**Returns**

  * ([::Grafeas::V1::UpgradeOccurrence](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-UpgradeOccurrence)) — Describes an available package upgrade on the linked resource.

Note: The following fields are mutually exclusive: `upgrade`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `compliance`, `dsse_attestation`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #upgrade=
    
    
    def upgrade=(value) -> ::Grafeas::V1::UpgradeOccurrence

**Parameter**

  * **value** ([::Grafeas::V1::UpgradeOccurrence](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-UpgradeOccurrence)) — Describes an available package upgrade on the linked resource.

Note: The following fields are mutually exclusive: `upgrade`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `compliance`, `dsse_attestation`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Grafeas::V1::UpgradeOccurrence](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-UpgradeOccurrence)) — Describes an available package upgrade on the linked resource.

Note: The following fields are mutually exclusive: `upgrade`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `compliance`, `dsse_attestation`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #vulnerability
    
    
    def vulnerability() -> ::Grafeas::V1::VulnerabilityOccurrence

**Returns**

  * ([::Grafeas::V1::VulnerabilityOccurrence](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-VulnerabilityOccurrence)) — Describes a security vulnerability.

Note: The following fields are mutually exclusive: `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #vulnerability=
    
    
    def vulnerability=(value) -> ::Grafeas::V1::VulnerabilityOccurrence

**Parameter**

  * **value** ([::Grafeas::V1::VulnerabilityOccurrence](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-VulnerabilityOccurrence)) — Describes a security vulnerability.

Note: The following fields are mutually exclusive: `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Grafeas::V1::VulnerabilityOccurrence](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-VulnerabilityOccurrence)) — Describes a security vulnerability.

Note: The following fields are mutually exclusive: `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
