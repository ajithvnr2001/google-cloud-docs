---
url: https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-Note/
title: Grafeas V1 API - Class Grafeas::V1::Note (v1.10.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:33:33.603263+00:00
---

# Grafeas V1 API - Class Grafeas::V1::Note (v1.10.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-Note/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Grafeas V1 API - Class Grafeas::V1::Note (v1.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.10.1 (latest)  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.0  1.1.1  1.0.0  0.16.1  0.15.0  0.14.2  0.13.0  0.12.1  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.1  0.5.0  0.4.0  0.3.1 

Reference documentation and code samples for the Grafeas V1 API class Grafeas::V1::Note.

A type of analysis that can be done for a resource.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #attestation
    
    
    def attestation() -> ::Grafeas::V1::AttestationNote

**Returns**

  * ([::Grafeas::V1::AttestationNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-AttestationNote)) — A note describing an attestation role.

Note: The following fields are mutually exclusive: `attestation`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `upgrade`, `compliance`, `dsse_attestation`, `vulnerability_assessment`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #attestation=
    
    
    def attestation=(value) -> ::Grafeas::V1::AttestationNote

**Parameter**

  * **value** ([::Grafeas::V1::AttestationNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-AttestationNote)) — A note describing an attestation role.

Note: The following fields are mutually exclusive: `attestation`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `upgrade`, `compliance`, `dsse_attestation`, `vulnerability_assessment`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Grafeas::V1::AttestationNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-AttestationNote)) — A note describing an attestation role.

Note: The following fields are mutually exclusive: `attestation`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `upgrade`, `compliance`, `dsse_attestation`, `vulnerability_assessment`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #build
    
    
    def build() -> ::Grafeas::V1::BuildNote

**Returns**

  * ([::Grafeas::V1::BuildNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-BuildNote)) — A note describing build provenance for a verifiable build.

Note: The following fields are mutually exclusive: `build`, `vulnerability`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `vulnerability_assessment`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #build=
    
    
    def build=(value) -> ::Grafeas::V1::BuildNote

**Parameter**

  * **value** ([::Grafeas::V1::BuildNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-BuildNote)) — A note describing build provenance for a verifiable build.

Note: The following fields are mutually exclusive: `build`, `vulnerability`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `vulnerability_assessment`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Grafeas::V1::BuildNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-BuildNote)) — A note describing build provenance for a verifiable build.

Note: The following fields are mutually exclusive: `build`, `vulnerability`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `vulnerability_assessment`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #compliance
    
    
    def compliance() -> ::Grafeas::V1::ComplianceNote

**Returns**

  * ([::Grafeas::V1::ComplianceNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-ComplianceNote)) — A note describing a compliance check.

Note: The following fields are mutually exclusive: `compliance`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `dsse_attestation`, `vulnerability_assessment`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #compliance=
    
    
    def compliance=(value) -> ::Grafeas::V1::ComplianceNote

**Parameter**

  * **value** ([::Grafeas::V1::ComplianceNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-ComplianceNote)) — A note describing a compliance check.

Note: The following fields are mutually exclusive: `compliance`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `dsse_attestation`, `vulnerability_assessment`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Grafeas::V1::ComplianceNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-ComplianceNote)) — A note describing a compliance check.

Note: The following fields are mutually exclusive: `compliance`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `dsse_attestation`, `vulnerability_assessment`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time this note was created. This field can be used as a filter in list requests. 



### #create_time=
    
    
    def create_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time this note was created. This field can be used as a filter in list requests. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time this note was created. This field can be used as a filter in list requests. 



### #deployment
    
    
    def deployment() -> ::Grafeas::V1::DeploymentNote

**Returns**

  * ([::Grafeas::V1::DeploymentNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-DeploymentNote)) — A note describing something that can be deployed.

Note: The following fields are mutually exclusive: `deployment`, `vulnerability`, `build`, `image`, `package`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `vulnerability_assessment`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #deployment=
    
    
    def deployment=(value) -> ::Grafeas::V1::DeploymentNote

**Parameter**

  * **value** ([::Grafeas::V1::DeploymentNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-DeploymentNote)) — A note describing something that can be deployed.

Note: The following fields are mutually exclusive: `deployment`, `vulnerability`, `build`, `image`, `package`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `vulnerability_assessment`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Grafeas::V1::DeploymentNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-DeploymentNote)) — A note describing something that can be deployed.

Note: The following fields are mutually exclusive: `deployment`, `vulnerability`, `build`, `image`, `package`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `vulnerability_assessment`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #discovery
    
    
    def discovery() -> ::Grafeas::V1::DiscoveryNote

**Returns**

  * ([::Grafeas::V1::DiscoveryNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-DiscoveryNote)) — A note describing the initial analysis of a resource.

Note: The following fields are mutually exclusive: `discovery`, `vulnerability`, `build`, `image`, `package`, `deployment`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `vulnerability_assessment`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #discovery=
    
    
    def discovery=(value) -> ::Grafeas::V1::DiscoveryNote

**Parameter**

  * **value** ([::Grafeas::V1::DiscoveryNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-DiscoveryNote)) — A note describing the initial analysis of a resource.

Note: The following fields are mutually exclusive: `discovery`, `vulnerability`, `build`, `image`, `package`, `deployment`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `vulnerability_assessment`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Grafeas::V1::DiscoveryNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-DiscoveryNote)) — A note describing the initial analysis of a resource.

Note: The following fields are mutually exclusive: `discovery`, `vulnerability`, `build`, `image`, `package`, `deployment`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `vulnerability_assessment`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #dsse_attestation
    
    
    def dsse_attestation() -> ::Grafeas::V1::DSSEAttestationNote

**Returns**

  * ([::Grafeas::V1::DSSEAttestationNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-DSSEAttestationNote)) — A note describing a dsse attestation note.

Note: The following fields are mutually exclusive: `dsse_attestation`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `vulnerability_assessment`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #dsse_attestation=
    
    
    def dsse_attestation=(value) -> ::Grafeas::V1::DSSEAttestationNote

**Parameter**

  * **value** ([::Grafeas::V1::DSSEAttestationNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-DSSEAttestationNote)) — A note describing a dsse attestation note.

Note: The following fields are mutually exclusive: `dsse_attestation`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `vulnerability_assessment`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Grafeas::V1::DSSEAttestationNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-DSSEAttestationNote)) — A note describing a dsse attestation note.

Note: The following fields are mutually exclusive: `dsse_attestation`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `vulnerability_assessment`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #expiration_time
    
    
    def expiration_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Google-Protobuf-Timestamp)) — Time of expiration for this note. Empty if note does not expire. 



### #expiration_time=
    
    
    def expiration_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Google-Protobuf-Timestamp)) — Time of expiration for this note. Empty if note does not expire. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Google-Protobuf-Timestamp)) — Time of expiration for this note. Empty if note does not expire. 



### #image
    
    
    def image() -> ::Grafeas::V1::ImageNote

**Returns**

  * ([::Grafeas::V1::ImageNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-ImageNote)) — A note describing a base image.

Note: The following fields are mutually exclusive: `image`, `vulnerability`, `build`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `vulnerability_assessment`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #image=
    
    
    def image=(value) -> ::Grafeas::V1::ImageNote

**Parameter**

  * **value** ([::Grafeas::V1::ImageNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-ImageNote)) — A note describing a base image.

Note: The following fields are mutually exclusive: `image`, `vulnerability`, `build`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `vulnerability_assessment`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Grafeas::V1::ImageNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-ImageNote)) — A note describing a base image.

Note: The following fields are mutually exclusive: `image`, `vulnerability`, `build`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `vulnerability_assessment`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #kind
    
    
    def kind() -> ::Grafeas::V1::NoteKind

**Returns**

  * ([::Grafeas::V1::NoteKind](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-NoteKind)) — Output only. The type of analysis. This field can be used as a filter in list requests. 



### #kind=
    
    
    def kind=(value) -> ::Grafeas::V1::NoteKind

**Parameter**

  * **value** ([::Grafeas::V1::NoteKind](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-NoteKind)) — Output only. The type of analysis. This field can be used as a filter in list requests. 



**Returns**

  * ([::Grafeas::V1::NoteKind](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-NoteKind)) — Output only. The type of analysis. This field can be used as a filter in list requests. 



### #long_description
    
    
    def long_description() -> ::String

**Returns**

  * (::String) — A detailed description of this note. 



### #long_description=
    
    
    def long_description=(value) -> ::String

**Parameter**

  * **value** (::String) — A detailed description of this note. 



**Returns**

  * (::String) — A detailed description of this note. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. The name of the note in the form of `projects/[PROVIDER_ID]/notes/[NOTE_ID]`. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. The name of the note in the form of `projects/[PROVIDER_ID]/notes/[NOTE_ID]`. 



**Returns**

  * (::String) — Output only. The name of the note in the form of `projects/[PROVIDER_ID]/notes/[NOTE_ID]`. 



### #package
    
    
    def package() -> ::Grafeas::V1::PackageNote

**Returns**

  * ([::Grafeas::V1::PackageNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-PackageNote)) — A note describing a package hosted by various package managers.

Note: The following fields are mutually exclusive: `package`, `vulnerability`, `build`, `image`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `vulnerability_assessment`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #package=
    
    
    def package=(value) -> ::Grafeas::V1::PackageNote

**Parameter**

  * **value** ([::Grafeas::V1::PackageNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-PackageNote)) — A note describing a package hosted by various package managers.

Note: The following fields are mutually exclusive: `package`, `vulnerability`, `build`, `image`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `vulnerability_assessment`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Grafeas::V1::PackageNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-PackageNote)) — A note describing a package hosted by various package managers.

Note: The following fields are mutually exclusive: `package`, `vulnerability`, `build`, `image`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `vulnerability_assessment`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #related_note_names
    
    
    def related_note_names() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Other notes related to this note. 



### #related_note_names=
    
    
    def related_note_names=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Other notes related to this note. 



**Returns**

  * (::Array<::String>) — Other notes related to this note. 



### #related_url
    
    
    def related_url() -> ::Array<::Grafeas::V1::RelatedUrl>

**Returns**

  * (::Array<[::Grafeas::V1::RelatedUrl](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-RelatedUrl)>) — URLs associated with this note. 



### #related_url=
    
    
    def related_url=(value) -> ::Array<::Grafeas::V1::RelatedUrl>

**Parameter**

  * **value** (::Array<[::Grafeas::V1::RelatedUrl](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-RelatedUrl)>) — URLs associated with this note. 



**Returns**

  * (::Array<[::Grafeas::V1::RelatedUrl](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-RelatedUrl)>) — URLs associated with this note. 



### #sbom_reference
    
    
    def sbom_reference() -> ::Grafeas::V1::SBOMReferenceNote

**Returns**

  * ([::Grafeas::V1::SBOMReferenceNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-SBOMReferenceNote)) — A note describing an SBOM reference.

Note: The following fields are mutually exclusive: `sbom_reference`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `vulnerability_assessment`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #sbom_reference=
    
    
    def sbom_reference=(value) -> ::Grafeas::V1::SBOMReferenceNote

**Parameter**

  * **value** ([::Grafeas::V1::SBOMReferenceNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-SBOMReferenceNote)) — A note describing an SBOM reference.

Note: The following fields are mutually exclusive: `sbom_reference`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `vulnerability_assessment`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Grafeas::V1::SBOMReferenceNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-SBOMReferenceNote)) — A note describing an SBOM reference.

Note: The following fields are mutually exclusive: `sbom_reference`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `vulnerability_assessment`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #secret
    
    
    def secret() -> ::Grafeas::V1::SecretNote

**Returns**

  * ([::Grafeas::V1::SecretNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-SecretNote)) — A note describing a secret.

Note: The following fields are mutually exclusive: `secret`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `vulnerability_assessment`, `sbom_reference`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #secret=
    
    
    def secret=(value) -> ::Grafeas::V1::SecretNote

**Parameter**

  * **value** ([::Grafeas::V1::SecretNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-SecretNote)) — A note describing a secret.

Note: The following fields are mutually exclusive: `secret`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `vulnerability_assessment`, `sbom_reference`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Grafeas::V1::SecretNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-SecretNote)) — A note describing a secret.

Note: The following fields are mutually exclusive: `secret`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `vulnerability_assessment`, `sbom_reference`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #short_description
    
    
    def short_description() -> ::String

**Returns**

  * (::String) — A one sentence description of this note. 



### #short_description=
    
    
    def short_description=(value) -> ::String

**Parameter**

  * **value** (::String) — A one sentence description of this note. 



**Returns**

  * (::String) — A one sentence description of this note. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time this note was last updated. This field can be used as a filter in list requests. 



### #update_time=
    
    
    def update_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time this note was last updated. This field can be used as a filter in list requests. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time this note was last updated. This field can be used as a filter in list requests. 



### #upgrade
    
    
    def upgrade() -> ::Grafeas::V1::UpgradeNote

**Returns**

  * ([::Grafeas::V1::UpgradeNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-UpgradeNote)) — A note describing available package upgrades.

Note: The following fields are mutually exclusive: `upgrade`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `compliance`, `dsse_attestation`, `vulnerability_assessment`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #upgrade=
    
    
    def upgrade=(value) -> ::Grafeas::V1::UpgradeNote

**Parameter**

  * **value** ([::Grafeas::V1::UpgradeNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-UpgradeNote)) — A note describing available package upgrades.

Note: The following fields are mutually exclusive: `upgrade`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `compliance`, `dsse_attestation`, `vulnerability_assessment`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Grafeas::V1::UpgradeNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-UpgradeNote)) — A note describing available package upgrades.

Note: The following fields are mutually exclusive: `upgrade`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `compliance`, `dsse_attestation`, `vulnerability_assessment`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #vulnerability
    
    
    def vulnerability() -> ::Grafeas::V1::VulnerabilityNote

**Returns**

  * ([::Grafeas::V1::VulnerabilityNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-VulnerabilityNote)) — A note describing a package vulnerability.

Note: The following fields are mutually exclusive: `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `vulnerability_assessment`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #vulnerability=
    
    
    def vulnerability=(value) -> ::Grafeas::V1::VulnerabilityNote

**Parameter**

  * **value** ([::Grafeas::V1::VulnerabilityNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-VulnerabilityNote)) — A note describing a package vulnerability.

Note: The following fields are mutually exclusive: `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `vulnerability_assessment`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Grafeas::V1::VulnerabilityNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-VulnerabilityNote)) — A note describing a package vulnerability.

Note: The following fields are mutually exclusive: `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `vulnerability_assessment`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #vulnerability_assessment
    
    
    def vulnerability_assessment() -> ::Grafeas::V1::VulnerabilityAssessmentNote

**Returns**

  * ([::Grafeas::V1::VulnerabilityAssessmentNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-VulnerabilityAssessmentNote)) — A note describing a vulnerability assessment.

Note: The following fields are mutually exclusive: `vulnerability_assessment`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #vulnerability_assessment=
    
    
    def vulnerability_assessment=(value) -> ::Grafeas::V1::VulnerabilityAssessmentNote

**Parameter**

  * **value** ([::Grafeas::V1::VulnerabilityAssessmentNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-VulnerabilityAssessmentNote)) — A note describing a vulnerability assessment.

Note: The following fields are mutually exclusive: `vulnerability_assessment`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Grafeas::V1::VulnerabilityAssessmentNote](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-VulnerabilityAssessmentNote)) — A note describing a vulnerability assessment.

Note: The following fields are mutually exclusive: `vulnerability_assessment`, `vulnerability`, `build`, `image`, `package`, `deployment`, `discovery`, `attestation`, `upgrade`, `compliance`, `dsse_attestation`, `sbom_reference`, `secret`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
