---
url: https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences
title: REST Resource: projects.locations.occurrences \u00a0|\u00a0 Artifact Analysis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:40:49.636518+00:00
---

# REST Resource: projects.locations.occurrences  |  Artifact Analysis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)
  * [ Reference ](https://docs.cloud.google.com/artifact-analysis/docs/apis)



Send feedback 

#  REST Resource: projects.locations.occurrences Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Occurrence
    * JSON representation
    * Resource
      * JSON representation
    * Hash
      * JSON representation
    * HashType
    * Details
      * JSON representation
    * PackageIssue
      * JSON representation
    * VexAssessment
      * JSON representation
    * Details
      * JSON representation
    * BuildProvenance
      * JSON representation
    * Command
      * JSON representation
    * Artifact
      * JSON representation
    * Source
      * JSON representation
    * FileHashes
      * JSON representation
    * SourceContext
      * JSON representation
    * CloudRepoSourceContext
      * JSON representation
    * RepoId
      * JSON representation
    * ProjectRepoId
      * JSON representation
    * AliasContext
      * JSON representation
    * Kind
    * GerritSourceContext
      * JSON representation
    * GitSourceContext
      * JSON representation
    * InTotoSlsaProvenanceV1
      * JSON representation
    * Subject
      * JSON representation
    * SlsaProvenanceV1
      * JSON representation
    * BuildDefinition
      * JSON representation
    * ResourceDescriptor
      * JSON representation
    * RunDetails
      * JSON representation
    * ProvenanceBuilder
      * JSON representation
    * BuildMetadata
      * JSON representation
    * Details
      * JSON representation
    * Derived
      * JSON representation
    * Layer
      * JSON representation
    * Directive
    * Details
      * JSON representation
    * Installation
      * JSON representation
    * Location
      * JSON representation
    * Details
      * JSON representation
    * Deployment
      * JSON representation
    * Platform
    * Details
      * JSON representation
    * Discovered
      * JSON representation
    * ContinuousAnalysis
    * AnalysisStatus
    * AnalysisCompleted
      * JSON representation
    * SBOMStatus
      * JSON representation
    * SBOMState
    * File
      * JSON representation
    * Details
      * JSON representation
    * Attestation
      * JSON representation
    * PgpSignedAttestation
      * JSON representation
    * ContentType
    * GenericSignedAttestation
      * JSON representation
    * ContentType
    * Signature
      * JSON representation
    * Details
      * JSON representation
    * Signature
      * JSON representation
    * Link
      * JSON representation
    * Artifact
      * JSON representation
    * ArtifactHashes
      * JSON representation
    * ByProducts
      * JSON representation
    * Environment
      * JSON representation
    * DocumentOccurrence
      * JSON representation
    * PackageInfoOccurrence
      * JSON representation
    * FileOccurrence
      * JSON representation
    * RelationshipOccurrence
      * JSON representation
    * SBOMReferenceOccurrence
      * JSON representation
    * SbomReferenceIntotoPayload
      * JSON representation
    * SbomReferenceIntotoPredicate
      * JSON representation
    * EnvelopeSignature
      * JSON representation
    * SecretOccurrence
      * JSON representation
    * SecretKind
    * SecretLocation
      * JSON representation
    * FileLocation
      * JSON representation
    * SecretStatus
      * JSON representation
    * Status
    * Envelope
      * JSON representation
  * Methods



## Resource: Occurrence

An instance of an analysis type that has been found on a resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "resource": {
        object ([Resource](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Resource))
      },
      "noteName": string,
      "kind": enum ([NoteKind](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/NoteKind)),
      "remediation": string,
      "createTime": string,
      "updateTime": string,
      "envelope": {
        object ([Envelope](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Envelope))
      },
    
      // Union field details can be only one of the following:
      "vulnerability": {
        object ([Details](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Details))
      },
      "build": {
        object ([Details](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Details_1))
      },
      "derivedImage": {
        object ([Details](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Details_2))
      },
      "installation": {
        object ([Details](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Details_3))
      },
      "deployment": {
        object ([Details](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Details_4))
      },
      "discovered": {
        object ([Details](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Details_5))
      },
      "attestation": {
        object ([Details](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Details_6))
      },
      "intoto": {
        object ([Details](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Details_7))
      },
      "sbom": {
        object ([DocumentOccurrence](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.DocumentOccurrence))
      },
      "spdxPackage": {
        object ([PackageInfoOccurrence](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.PackageInfoOccurrence))
      },
      "spdxFile": {
        object ([FileOccurrence](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.FileOccurrence))
      },
      "spdxRelationship": {
        object ([RelationshipOccurrence](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.RelationshipOccurrence))
      },
      "sbomReference": {
        object ([SBOMReferenceOccurrence](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.SBOMReferenceOccurrence))
      },
      "secret": {
        object ([SecretOccurrence](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.SecretOccurrence))
      }
      // End of list of possible types for union field details.
    }  
  
Fields  
---  
`name` |  `string` Output only. The name of the occurrence in the form of `projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]`.  
`resource` |  `object (`[Resource](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Resource)`)` Required. Immutable. The resource for which the occurrence applies.  
`noteName` |  `string` Required. Immutable. The analysis note associated with this occurrence, in the form of `projects/[PROVIDER_ID]/notes/[NOTE_ID]`. This field can be used as a filter in list requests.  
`kind` |  `enum (`[NoteKind](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/NoteKind)`)` Output only. This explicitly denotes which of the occurrence details are specified. This field can be used as a filter in list requests.  
`remediation` |  `string` A description of actions that can be taken to remedy the note.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time this occurrence was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time this occurrence was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`envelope` |  `object (`[Envelope](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Envelope)`)` <https://github.com/secure-systems-lab/dsse>  
Union field `details`. Required. Immutable. Describes the details of the note kind found on this resource. `details` can be only one of the following:  
`vulnerability` |  `object (`[Details](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Details)`)` Describes a security vulnerability.  
`build` |  `object (`[Details](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Details_1)`)` Describes a verifiable build.  
`derivedImage` |  `object (`[Details](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Details_2)`)` Describes how this resource derives from the basis in the associated note.  
`installation` |  `object (`[Details](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Details_3)`)` Describes the installation of a package on the linked resource.  
`deployment` |  `object (`[Details](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Details_4)`)` Describes the deployment of an artifact on a runtime.  
`discovered` |  `object (`[Details](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Details_5)`)` Describes when a resource was discovered.  
`attestation` |  `object (`[Details](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Details_6)`)` Describes an attestation of an artifact.  
`intoto` |  `object (`[Details](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Details_7)`)` Describes a specific in-toto link.  
`sbom` |  `object (`[DocumentOccurrence](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.DocumentOccurrence)`)` Describes a specific software bill of materials document.  
`spdxPackage` |  `object (`[PackageInfoOccurrence](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.PackageInfoOccurrence)`)` Describes a specific SPDX Package.  
`spdxFile` |  `object (`[FileOccurrence](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.FileOccurrence)`)` Describes a specific SPDX File.  
`spdxRelationship` |  `object (`[RelationshipOccurrence](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.RelationshipOccurrence)`)` Describes a specific SPDX Relationship.  
`sbomReference` |  `object (`[SBOMReferenceOccurrence](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.SBOMReferenceOccurrence)`)` Describes a specific SBOM reference occurrences.  
`secret` |  `object (`[SecretOccurrence](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.SecretOccurrence)`)` Describes a secret.  
  
### Resource

An entity that can have metadata. For example, a Docker image.

JSON representation  
---  
      
    
    {
      "name": string,
      "uri": string,
      "contentHash": {
        object ([Hash](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Hash))
      }
    }  
  
Fields  
---  
`name  
**(deprecated)**` |  `string` This item is deprecated!Deprecated, do not use. Use uri instead.The name of the resource. For example, the name of a Docker image - "Debian".  
`uri` |  `string` Required. The unique URI of the resource. For example, `https://gcr.io/project/image@sha256:foo` for a Docker image.  
`contentHash  
**(deprecated)**` |  `object (`[Hash](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Hash)`)` This item is deprecated!Deprecated, do not use. Use uri instead.The hash of the resource content. For example, the Docker digest.  
  
### Hash

Container message for hash values.

JSON representation  
---  
      
    
    {
      "type": enum ([HashType](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.HashType)),
      "value": string
    }  
  
Fields  
---  
`type` |  `enum (`[HashType](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.HashType)`)` Required. The type of hash that was performed.  
`value` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. The hash value.A base64-encoded string.  
  
### HashType

Specifies the hash algorithm.

Enums  
---  
`HASH_TYPE_UNSPECIFIED` | Unknown.  
`SHA256` | A SHA-256 hash.  
`GO_MODULE_H1` | Dirhash of a Go module's source code which is then hex-encoded. See b/244466565 and <https://github.com/in-toto/attestation/pull/108>.  
`SHA512` | A SHA-512 hash.  
`DIRSUM_SHA256` | A Dirsum SHA-256 hash.  
  
### Details

Details of a vulnerability Occurrence.

JSON representation  
---  
      
    
    {
      "type": string,
      "severity": enum ([Severity](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/Severity)),
      "cvssScore": number,
      "packageIssue": [
        {
          object ([PackageIssue](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.PackageIssue))
        }
      ],
      "shortDescription": string,
      "longDescription": string,
      "relatedUrls": [
        {
          object ([RelatedUrl](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/RelatedUrl))
        }
      ],
      "effectiveSeverity": enum ([Severity](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/Severity)),
      "cvssVersion": enum ([CVSSVersion](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/CVSSVersion)),
      "vexAssessment": {
        object ([VexAssessment](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.VexAssessment))
      },
      "cvssV2": {
        object ([CVSS](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/CVSS))
      },
      "cvssV3": {
        object ([CVSS](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/CVSS))
      },
      "extraDetails": string
    }  
  
Fields  
---  
`type` |  `string` The type of package; whether native or non native(ruby gems, node.js packages etc)  
`severity` |  `enum (`[Severity](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/Severity)`)` Output only. The note provider assigned Severity of the vulnerability.  
`cvssScore` |  `number` Output only. The CVSS score of this vulnerability. CVSS score is on a scale of 0-10 where 0 indicates low severity and 10 indicates high severity.  
`packageIssue[]` |  `object (`[PackageIssue](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.PackageIssue)`)` Required. The set of affected locations and their fixes (if available) within the associated resource.  
`shortDescription` |  `string` Output only. A one sentence description of this vulnerability.  
`longDescription` |  `string` Output only. A detailed description of this vulnerability.  
`relatedUrls[]` |  `object (`[RelatedUrl](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/RelatedUrl)`)` Output only. URLs related to this vulnerability.  
`effectiveSeverity` |  `enum (`[Severity](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/Severity)`)` The distro assigned severity for this vulnerability when it is available, and note provider assigned severity when distro has not yet assigned a severity for this vulnerability.When there are multiple PackageIssues for this vulnerability, they can have different effective severities because some might be provided by the distro while others are provided by the language ecosystem for a language pack. For this reason, it is advised to use the effective severity on the PackageIssue level. In the case where multiple PackageIssues have differing effective severities, this field should be the highest severity for any of the PackageIssues.  
`cvssVersion` |  `enum (`[CVSSVersion](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/CVSSVersion)`)` Output only. CVSS version used to populate cvssScore and severity.  
`vexAssessment` |  `object (`[VexAssessment](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.VexAssessment)`)`  
`cvssV2` |  `object (`[CVSS](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/CVSS)`)` The cvss v2 score for the vulnerability.  
`cvssV3` |  `object (`[CVSS](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/CVSS)`)` The cvss v3 score for the vulnerability.  
`extraDetails` |  `string` Occurrence-specific extra details about the vulnerability.  
  
### PackageIssue

This message wraps a location affected by a vulnerability and its associated fix (if one is available).

JSON representation  
---  
      
    
    {
      "affectedLocation": {
        object ([VulnerabilityLocation](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/VulnerabilityLocation))
      },
      "fixedLocation": {
        object ([VulnerabilityLocation](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/VulnerabilityLocation))
      },
      "severityName": string,
      "packageType": string,
      "effectiveSeverity": enum ([Severity](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/Severity))
    }  
  
Fields  
---  
`affectedLocation` |  `object (`[VulnerabilityLocation](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/VulnerabilityLocation)`)` Required. The location of the vulnerability.  
`fixedLocation` |  `object (`[VulnerabilityLocation](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/VulnerabilityLocation)`)` The location of the available fix for vulnerability.  
`severityName` |  `string` Deprecated, use Details.effective_severity instead The severity (e.g., distro assigned severity) for this vulnerability.  
`packageType` |  `string` The type of package (e.g. OS, MAVEN, GO).  
`effectiveSeverity` |  `enum (`[Severity](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/Severity)`)` Output only. The distro or language system assigned severity for this vulnerability when that is available and note provider assigned severity when it is not available.  
  
### VexAssessment

VexAssessment provides all publisher provided Vex information that is related to this vulnerability.

JSON representation  
---  
      
    
    {
      "cve": string,
      "vulnerabilityId": string,
      "relatedUris": [
        {
          object ([RelatedUrl](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/RelatedUrl))
        }
      ],
      "noteName": string,
      "state": enum ([State](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/State)),
      "impacts": [
        string
      ],
      "remediations": [
        {
          object ([Remediation](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/Remediation))
        }
      ],
      "justification": {
        object ([Justification](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/Justification))
      }
    }  
  
Fields  
---  
`cve  
**(deprecated)**` |  `string` This item is deprecated!Holds the MITRE standard Common Vulnerabilities and Exposures (CVE) tracking number for the vulnerability. Deprecated: Use vulnerabilityId instead to denote CVEs.  
`vulnerabilityId` |  `string` The vulnerability identifier for this Assessment. Will hold one of common identifiers e.g. CVE, GHSA etc.  
`relatedUris[]` |  `object (`[RelatedUrl](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/RelatedUrl)`)` Holds a list of references associated with this vulnerability item and assessment.  
`noteName` |  `string` The VulnerabilityAssessment note from which this VexAssessment was generated. This will be of the form: `projects/[PROJECT_ID]/notes/[NOTE_ID]`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/State)`)` Provides the state of this Vulnerability assessment.  
`impacts[]` |  `string` Contains information about the impact of this vulnerability, this will change with time.  
`remediations[]` |  `object (`[Remediation](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/Remediation)`)` Specifies details on how to handle (and presumably, fix) a vulnerability.  
`justification` |  `object (`[Justification](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/Justification)`)` Justification provides the justification when the state of the assessment if NOT_AFFECTED.  
  
### Details

Details of a build occurrence.

JSON representation  
---  
      
    
    {
      "provenance": {
        object ([BuildProvenance](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.BuildProvenance))
      },
      "provenanceBytes": string,
      "inTotoSlsaProvenanceV1": {
        object ([InTotoSlsaProvenanceV1](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.InTotoSlsaProvenanceV1))
      }
    }  
  
Fields  
---  
`provenance` |  `object (`[BuildProvenance](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.BuildProvenance)`)` Required. The actual provenance for the build.  
`provenanceBytes` |  `string` Serialized JSON representation of the provenance, used in generating the build signature in the corresponding build note. After verifying the signature, `provenanceBytes` can be unmarshalled and compared to the provenance to confirm that it is unchanged. A base64-encoded string representation of the provenance bytes is used for the signature in order to interoperate with openssl which expects this format for signature verification.The serialized form is captured both to avoid ambiguity in how the provenance is marshalled to json as well to prevent incompatibilities with future changes.  
`inTotoSlsaProvenanceV1` |  `object (`[InTotoSlsaProvenanceV1](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.InTotoSlsaProvenanceV1)`)`  
  
### BuildProvenance

Provenance of a build. Contains all information needed to verify the full details about the build from source to completion.

JSON representation  
---  
      
    
    {
      "id": string,
      "projectId": string,
      "commands": [
        {
          object ([Command](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Command))
        }
      ],
      "builtArtifacts": [
        {
          object ([Artifact](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Artifact))
        }
      ],
      "createTime": string,
      "startTime": string,
      "endTime": string,
      "creator": string,
      "logsUri": string,
      "sourceProvenance": {
        object ([Source](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Source))
      },
      "triggerId": string,
      "buildOptions": {
        string: string,
        ...
      },
      "builderVersion": string
    }  
  
Fields  
---  
`id` |  `string` Required. Unique identifier of the build.  
`projectId` |  `string` ID of the project.  
`commands[]` |  `object (`[Command](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Command)`)` Commands requested by the build.  
`builtArtifacts[]` |  `object (`[Artifact](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Artifact)`)` Output of the build.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time at which the build was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time at which execution of the build was started.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time at which execution of the build was finished.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`creator` |  `string` E-mail address of the user who initiated this build. Note that this was the user's e-mail address at the time the build was initiated; this address may not represent the same end-user for all time.  
`logsUri` |  `string` URI where any logs for this provenance were written.  
`sourceProvenance` |  `object (`[Source](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Source)`)` Details of the Source input to the build.  
`triggerId` |  `string` Trigger identifier if the build was triggered automatically; empty if not.  
`buildOptions` |  `map (key: string, value: string)` Special options applied to this build. This is a catch-all field where build providers can enter any desired additional details.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`builderVersion` |  `string` Version string of the builder at the time this build was executed.  
  
### Command

Command describes a step performed as part of the build pipeline.

JSON representation  
---  
      
    
    {
      "name": string,
      "env": [
        string
      ],
      "args": [
        string
      ],
      "dir": string,
      "id": string,
      "waitFor": [
        string
      ]
    }  
  
Fields  
---  
`name` |  `string` Required. Name of the command, as presented on the command line, or if the command is packaged as a Docker container, as presented to `docker pull`.  
`env[]` |  `string` Environment variables set before running this command.  
`args[]` |  `string` Command-line arguments used when executing this command.  
`dir` |  `string` Working directory (relative to project source root) used when running this command.  
`id` |  `string` Optional unique identifier for this command, used in waitFor to reference this command as a dependency.  
`waitFor[]` |  `string` The ID(s) of the command(s) that this command depends on.  
  
### Artifact

Artifact describes a build product.

JSON representation  
---  
      
    
    {
      "checksum": string,
      "id": string,
      "names": [
        string
      ]
    }  
  
Fields  
---  
`checksum` |  `string` Hash or checksum value of a binary, or Docker Registry 2.0 digest of a container.  
`id` |  `string` Artifact ID, if any; for container images, this will be a URL by digest like `gcr.io/projectID/imagename@sha256:123456`.  
`names[]` |  `string` Related artifact names. This may be the path to a binary or jar file, or in the case of a container build, the name used to push the container image to Google Container Registry, as presented to `docker push`. Note that a single Artifact ID can have multiple names, for example if two tags are applied to one image.  
  
### Source

Source describes the location of the source used for the build.

JSON representation  
---  
      
    
    {
      "artifactStorageSourceUri": string,
      "fileHashes": {
        string: {
          object ([FileHashes](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.FileHashes))
        },
        ...
      },
      "context": {
        object ([SourceContext](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.SourceContext))
      },
      "additionalContexts": [
        {
          object ([SourceContext](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.SourceContext))
        }
      ]
    }  
  
Fields  
---  
`artifactStorageSourceUri` |  `string` If provided, the input binary artifacts for the build came from this location.  
`fileHashes` |  `map (key: string, value: object (`[FileHashes](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.FileHashes)`))` Hash(es) of the build source, which can be used to verify that the original source integrity was maintained in the build.The keys to this map are file paths used as build source and the values contain the hash values for those files.If the build source came in a single package such as a gzipped tarfile (.tar.gz), the FileHash will be for the single path to that file.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`context` |  `object (`[SourceContext](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.SourceContext)`)` If provided, the source code used for the build came from this location.  
`additionalContexts[]` |  `object (`[SourceContext](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.SourceContext)`)` If provided, some of the source code used for the build may be found in these locations, in the case where the source repository had multiple remotes or submodules. This list will not include the context specified in the context field.  
  
### FileHashes

Container message for hashes of byte content of files, used in source messages to verify integrity of source input to the build.

JSON representation  
---  
      
    
    {
      "fileHash": [
        {
          object ([Hash](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Hash))
        }
      ]
    }  
  
Fields  
---  
`fileHash[]` |  `object (`[Hash](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Hash)`)` Required. Collection of file hashes.  
  
### SourceContext

A SourceContext is a reference to a tree of files. A SourceContext together with a path point to a unique revision of a single file or directory.

JSON representation  
---  
      
    
    {
      "labels": {
        string: string,
        ...
      },
    
      // Union field context can be only one of the following:
      "cloudRepo": {
        object ([CloudRepoSourceContext](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.CloudRepoSourceContext))
      },
      "gerrit": {
        object ([GerritSourceContext](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.GerritSourceContext))
      },
      "git": {
        object ([GitSourceContext](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.GitSourceContext))
      }
      // End of list of possible types for union field context.
    }  
  
Fields  
---  
`labels` |  `map (key: string, value: string)` Labels with user defined metadata.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
Union field `context`. A SourceContext can refer any one of the following types of repositories. `context` can be only one of the following:  
`cloudRepo` |  `object (`[CloudRepoSourceContext](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.CloudRepoSourceContext)`)` A SourceContext referring to a revision in a Google Cloud Source Repo.  
`gerrit` |  `object (`[GerritSourceContext](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.GerritSourceContext)`)` A SourceContext referring to a Gerrit project.  
`git` |  `object (`[GitSourceContext](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.GitSourceContext)`)` A SourceContext referring to any third party Git repo (e.g., GitHub).  
  
### CloudRepoSourceContext

A CloudRepoSourceContext denotes a particular revision in a Google Cloud Source Repo.

JSON representation  
---  
      
    
    {
      "repoId": {
        object ([RepoId](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.RepoId))
      },
    
      // Union field revision can be only one of the following:
      "revisionId": string,
      "aliasContext": {
        object ([AliasContext](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.AliasContext))
      }
      // End of list of possible types for union field revision.
    }  
  
Fields  
---  
`repoId` |  `object (`[RepoId](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.RepoId)`)` The ID of the repo.  
Union field `revision`. A revision in a Cloud Repo can be identified by either its revision ID or its alias. `revision` can be only one of the following:  
`revisionId` |  `string` A revision ID.  
`aliasContext` |  `object (`[AliasContext](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.AliasContext)`)` An alias, which may be a branch or tag.  
  
### RepoId

A unique identifier for a Cloud Repo.

JSON representation  
---  
      
    
    {
    
      // Union field id can be only one of the following:
      "projectRepoId": {
        object ([ProjectRepoId](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.ProjectRepoId))
      },
      "uid": string
      // End of list of possible types for union field id.
    }  
  
Fields  
---  
Union field `id`. A cloud repo can be identified by either its project ID and repository name combination, or its globally unique identifier. `id` can be only one of the following:  
`projectRepoId` |  `object (`[ProjectRepoId](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.ProjectRepoId)`)` A combination of a project ID and a repo name.  
`uid` |  `string` A server-assigned, globally unique identifier.  
  
### ProjectRepoId

Selects a repo using a Google Cloud Platform project ID (e.g., winged-cargo-31) and a repo name within that project.

JSON representation  
---  
      
    
    {
      "projectId": string,
      "repoName": string
    }  
  
Fields  
---  
`projectId` |  `string` The ID of the project.  
`repoName` |  `string` The name of the repo. Leave empty for the default repo.  
  
### AliasContext

An alias to a repo revision.

JSON representation  
---  
      
    
    {
      "kind": enum ([Kind](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Kind)),
      "name": string
    }  
  
Fields  
---  
`kind` |  `enum (`[Kind](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Kind)`)` The alias kind.  
`name` |  `string` The alias name.  
  
### Kind

The type of an alias.

Enums  
---  
`KIND_UNSPECIFIED` | Unknown.  
`FIXED` | Git tag.  
`MOVABLE` | Git branch.  
`OTHER` | Used to specify non-standard aliases. For example, if a Git repo has a ref named "refs/foo/bar".  
  
### GerritSourceContext

A SourceContext referring to a Gerrit project.

JSON representation  
---  
      
    
    {
      "hostUri": string,
      "gerritProject": string,
    
      // Union field revision can be only one of the following:
      "revisionId": string,
      "aliasContext": {
        object ([AliasContext](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.AliasContext))
      }
      // End of list of possible types for union field revision.
    }  
  
Fields  
---  
`hostUri` |  `string` The URI of a running Gerrit instance.  
`gerritProject` |  `string` The full project name within the host. Projects may be nested, so "project/subproject" is a valid project name. The "repo name" is the hostURI/project.  
Union field `revision`. A revision in a Gerrit project can be identified by either its revision ID or its alias. `revision` can be only one of the following:  
`revisionId` |  `string` A revision (commit) ID.  
`aliasContext` |  `object (`[AliasContext](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.AliasContext)`)` An alias, which may be a branch or tag.  
  
### GitSourceContext

A GitSourceContext denotes a particular revision in a third party Git repository (e.g., GitHub).

JSON representation  
---  
      
    
    {
      "url": string,
      "revisionId": string
    }  
  
Fields  
---  
`url` |  `string` Git repository URL.  
`revisionId` |  `string` Git commit hash.  
  
### InTotoSlsaProvenanceV1

JSON representation  
---  
      
    
    {
      "_type": string,
      "subject": [
        {
          object ([Subject](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Subject))
        }
      ],
      "predicateType": string,
      "predicate": {
        object ([SlsaProvenanceV1](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.SlsaProvenanceV1))
      }
    }  
  
Fields  
---  
`_type` |  `string` InToto spec defined at <https://github.com/in-toto/attestation/tree/main/spec#statement>  
`subject[]` |  `object (`[Subject](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Subject)`)`  
`predicateType` |  `string`  
`predicate` |  `object (`[SlsaProvenanceV1](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.SlsaProvenanceV1)`)`  
  
### Subject

Set of software artifacts that the attestation applies to. Each element represents a single software artifact.

JSON representation  
---  
      
    
    {
      "name": string,
      "digest": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier to distinguish this artifact from others within the subject.  
`digest` |  `map (key: string, value: string)` `"<ALGORITHM>": "<HEX_VALUE>"` Algorithms can be e.g. sha256, sha512 See <https://github.com/in-toto/attestation/blob/main/spec/field_types.md#DigestSet>An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### SlsaProvenanceV1

Keep in sync with schema at <https://github.com/slsa-framework/slsa/blob/main/docs/provenance/schema/v1/provenance.proto> Builder renamed to ProvenanceBuilder because of Java conflicts.

JSON representation  
---  
      
    
    {
      "buildDefinition": {
        object ([BuildDefinition](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.BuildDefinition))
      },
      "runDetails": {
        object ([RunDetails](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.RunDetails))
      }
    }  
  
Fields  
---  
`buildDefinition` |  `object (`[BuildDefinition](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.BuildDefinition)`)`  
`runDetails` |  `object (`[RunDetails](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.RunDetails)`)`  
  
### BuildDefinition

JSON representation  
---  
      
    
    {
      "buildType": string,
      "externalParameters": {
        object
      },
      "internalParameters": {
        object
      },
      "resolvedDependencies": [
        {
          object ([ResourceDescriptor](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.ResourceDescriptor))
        }
      ]
    }  
  
Fields  
---  
`buildType` |  `string`  
`externalParameters` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)`  
`internalParameters` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)`  
`resolvedDependencies[]` |  `object (`[ResourceDescriptor](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.ResourceDescriptor)`)`  
  
### ResourceDescriptor

JSON representation  
---  
      
    
    {
      "name": string,
      "uri": string,
      "digest": {
        string: string,
        ...
      },
      "content": string,
      "downloadLocation": string,
      "mediaType": string,
      "annotations": {
        string: value,
        ...
      }
    }  
  
Fields  
---  
`name` |  `string`  
`uri` |  `string`  
`digest` |  `map (key: string, value: string)` An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`content` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` A base64-encoded string.  
`downloadLocation` |  `string`  
`mediaType` |  `string`  
`annotations` |  `map (key: string, value: value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format))` An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### RunDetails

JSON representation  
---  
      
    
    {
      "builder": {
        object ([ProvenanceBuilder](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.ProvenanceBuilder))
      },
      "metadata": {
        object ([BuildMetadata](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.BuildMetadata))
      },
      "byproducts": [
        {
          object ([ResourceDescriptor](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.ResourceDescriptor))
        }
      ]
    }  
  
Fields  
---  
`builder` |  `object (`[ProvenanceBuilder](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.ProvenanceBuilder)`)`  
`metadata` |  `object (`[BuildMetadata](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.BuildMetadata)`)`  
`byproducts[]` |  `object (`[ResourceDescriptor](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.ResourceDescriptor)`)`  
  
### ProvenanceBuilder

JSON representation  
---  
      
    
    {
      "id": string,
      "version": {
        string: string,
        ...
      },
      "builderDependencies": [
        {
          object ([ResourceDescriptor](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.ResourceDescriptor))
        }
      ]
    }  
  
Fields  
---  
`id` |  `string`  
`version` |  `map (key: string, value: string)` An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`builderDependencies[]` |  `object (`[ResourceDescriptor](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.ResourceDescriptor)`)`  
  
### BuildMetadata

JSON representation  
---  
      
    
    {
      "invocationId": string,
      "startedOn": string,
      "finishedOn": string
    }  
  
Fields  
---  
`invocationId` |  `string`  
`startedOn` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`finishedOn` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### Details

Details of an image occurrence.

JSON representation  
---  
      
    
    {
      "derivedImage": {
        object ([Derived](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Derived))
      }
    }  
  
Fields  
---  
`derivedImage` |  `object (`[Derived](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Derived)`)` Required. Immutable. The child image derived from the base image.  
  
### Derived

Derived describes the derived image portion (Occurrence) of the DockerImage relationship. This image would be produced from a Dockerfile with FROM <DockerImage.Basis in attached Note>.

JSON representation  
---  
      
    
    {
      "fingerprint": {
        object ([Fingerprint](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/Fingerprint))
      },
      "distance": integer,
      "layerInfo": [
        {
          object ([Layer](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Layer))
        }
      ],
      "baseResourceUrl": string
    }  
  
Fields  
---  
`fingerprint` |  `object (`[Fingerprint](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/Fingerprint)`)` Required. The fingerprint of the derived image.  
`distance` |  `integer` Output only. The number of layers by which this image differs from the associated image basis.  
`layerInfo[]` |  `object (`[Layer](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Layer)`)` This contains layer-specific metadata, if populated it has length "distance" and is ordered with [distance] being the layer immediately following the base image and [1] being the final layer.  
`baseResourceUrl` |  `string` Output only. This contains the base image URL for the derived image occurrence.  
  
### Layer

Layer holds metadata specific to a layer of a Docker image.

JSON representation  
---  
      
    
    {
      "directive": enum ([Directive](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Directive)),
      "arguments": string
    }  
  
Fields  
---  
`directive` |  `enum (`[Directive](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Directive)`)` Required. The recovered Dockerfile directive used to construct this layer.  
`arguments` |  `string` The recovered arguments to the Dockerfile directive.  
  
### Directive

Instructions from Dockerfile.

Enums  
---  
`DIRECTIVE_UNSPECIFIED` | Default value for unsupported/missing directive.  
`MAINTAINER` | <https://docs.docker.com/engine/reference/builder/>  
`RUN` | <https://docs.docker.com/engine/reference/builder/>  
`CMD` | <https://docs.docker.com/engine/reference/builder/>  
`LABEL` | <https://docs.docker.com/engine/reference/builder/>  
`EXPOSE` | <https://docs.docker.com/engine/reference/builder/>  
`ENV` | <https://docs.docker.com/engine/reference/builder/>  
`ADD` | <https://docs.docker.com/engine/reference/builder/>  
`COPY` | <https://docs.docker.com/engine/reference/builder/>  
`ENTRYPOINT` | <https://docs.docker.com/engine/reference/builder/>  
`VOLUME` | <https://docs.docker.com/engine/reference/builder/>  
`USER` | <https://docs.docker.com/engine/reference/builder/>  
`WORKDIR` | <https://docs.docker.com/engine/reference/builder/>  
`ARG` | <https://docs.docker.com/engine/reference/builder/>  
`ONBUILD` | <https://docs.docker.com/engine/reference/builder/>  
`STOPSIGNAL` | <https://docs.docker.com/engine/reference/builder/>  
`HEALTHCHECK` | <https://docs.docker.com/engine/reference/builder/>  
`SHELL` | <https://docs.docker.com/engine/reference/builder/>  
  
### Details

Details of a package occurrence.

JSON representation  
---  
      
    
    {
      "installation": {
        object ([Installation](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Installation))
      }
    }  
  
Fields  
---  
`installation` |  `object (`[Installation](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Installation)`)` Required. Where the package was installed.  
  
### Installation

This represents how a particular software package may be installed on a system.

JSON representation  
---  
      
    
    {
      "name": string,
      "location": [
        {
          object ([Location](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Location))
        }
      ],
      "packageType": string,
      "cpeUri": string,
      "architecture": enum ([Architecture](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/Architecture)),
      "license": {
        object ([License](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/License))
      },
      "version": {
        object ([Version](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/Version))
      }
    }  
  
Fields  
---  
`name` |  `string` Required. Output only. The name of the installed package.  
`location[]` |  `object (`[Location](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Location)`)` All of the places within the filesystem versions of this package have been found.  
`packageType` |  `string` Output only. The type of package; whether native or non native (e.g., ruby gems, node.js packages, etc.).  
`cpeUri` |  `string` Output only. The cpeUri in [CPE format](https://cpe.mitre.org/specification/) denoting the package manager version distributing a package. The cpeUri will be blank for language packages.  
`architecture` |  `enum (`[Architecture](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/Architecture)`)` Output only. The CPU architecture for which packages in this distribution channel were built. Architecture will be blank for language packages.  
`license` |  `object (`[License](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/License)`)` Licenses that have been declared by the authors of the package.  
`version` |  `object (`[Version](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/Version)`)` Output only. The version of the package.  
  
### Location

An occurrence of a particular package installation found within a system's filesystem. E.g., glibc was found in `/var/lib/dpkg/status`.

JSON representation  
---  
      
    
    {
      "cpeUri": string,
      "version": {
        object ([Version](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/Version))
      },
      "path": string
    }  
  
Fields  
---  
`cpeUri` |  `string` Deprecated. The CPE URI in [CPE format](https://cpe.mitre.org/specification/) denoting the package manager version distributing a package.  
`version` |  `object (`[Version](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/Version)`)` Deprecated. The version installed at this location.  
`path` |  `string` The path from which we gathered that this package/version is installed.  
  
### Details

Details of a deployment occurrence.

JSON representation  
---  
      
    
    {
      "deployment": {
        object ([Deployment](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Deployment))
      }
    }  
  
Fields  
---  
`deployment` |  `object (`[Deployment](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Deployment)`)` Required. Deployment history for the resource.  
  
### Deployment

The period during which some deployable was active in a runtime.

JSON representation  
---  
      
    
    {
      "userEmail": string,
      "deployTime": string,
      "undeployTime": string,
      "config": string,
      "address": string,
      "resourceUri": [
        string
      ],
      "platform": enum ([Platform](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Platform))
    }  
  
Fields  
---  
`userEmail` |  `string` Identity of the user that triggered this deployment.  
`deployTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Required. Beginning of the lifetime of this deployment.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`undeployTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` End of the lifetime of this deployment.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`config` |  `string` Configuration used to create this deployment.  
`address` |  `string` Address of the runtime element hosting this deployment.  
`resourceUri[]` |  `string` Output only. Resource URI for the artifact being deployed taken from the deployable field with the same name.  
`platform` |  `enum (`[Platform](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Platform)`)` Platform hosting this deployment.  
  
### Platform

Types of platforms.

Enums  
---  
`PLATFORM_UNSPECIFIED` | Unknown.  
`GKE` | Google Container Engine.  
`FLEX` | Google App Engine: Flexible Environment.  
`CUSTOM` | Custom user-defined platform.  
  
### Details

Details of a discovery occurrence.

JSON representation  
---  
      
    
    {
      "discovered": {
        object ([Discovered](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Discovered))
      }
    }  
  
Fields  
---  
`discovered` |  `object (`[Discovered](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Discovered)`)` Required. Analysis status for the discovered resource.  
  
### Discovered

Provides information about the analysis status of a discovered resource.

JSON representation  
---  
      
    
    {
      "continuousAnalysis": enum ([ContinuousAnalysis](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.ContinuousAnalysis)),
      "lastAnalysisTime": string,
      "analysisStatus": enum ([AnalysisStatus](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.AnalysisStatus)),
      "analysisCompleted": {
        object ([AnalysisCompleted](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.AnalysisCompleted))
      },
      "analysisError": [
        {
          object ([Status](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/Shared.Types/Status))
        }
      ],
      "analysisStatusError": {
        object ([Status](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/Shared.Types/Status))
      },
      "sbomStatus": {
        object ([SBOMStatus](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.SBOMStatus))
      },
      "lastScanTime": string,
      "files": [
        {
          object ([File](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.File))
        }
      ]
    }  
  
Fields  
---  
`continuousAnalysis` |  `enum (`[ContinuousAnalysis](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.ContinuousAnalysis)`)` Whether the resource is continuously analyzed.  
`lastAnalysisTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The last time continuous analysis was done for this resource. Deprecated, do not use.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`analysisStatus` |  `enum (`[AnalysisStatus](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.AnalysisStatus)`)` The status of discovery for the resource.  
`analysisCompleted` |  `object (`[AnalysisCompleted](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.AnalysisCompleted)`)`  
`analysisError[]` |  `object (`[Status](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/Shared.Types/Status)`)` Indicates any errors encountered during analysis of a resource. There could be 0 or more of these errors.  
`analysisStatusError` |  `object (`[Status](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/Shared.Types/Status)`)` When an error is encountered this will contain a LocalizedMessage under details to show to the user. The LocalizedMessage is output only and populated by the API.  
`sbomStatus` |  `object (`[SBOMStatus](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.SBOMStatus)`)` The status of an SBOM generation.  
`lastScanTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The last time this resource was scanned.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`files[]` |  `object (`[File](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.File)`)` Files that make up the resource described by the occurrence.  
  
### ContinuousAnalysis

Whether the resource is continuously analyzed.

Enums  
---  
`CONTINUOUS_ANALYSIS_UNSPECIFIED` | Unknown.  
`ACTIVE` | The resource is continuously analyzed.  
`INACTIVE` | The resource is ignored for continuous analysis.  
  
### AnalysisStatus

Analysis status for a resource. Currently for initial analysis only (not updated in continuous analysis).

Enums  
---  
`ANALYSIS_STATUS_UNSPECIFIED` | Unknown.  
`PENDING` | Resource is known but no action has been taken yet.  
`SCANNING` | Resource is being analyzed.  
`FINISHED_SUCCESS` | Analysis has finished successfully.  
`COMPLETE` | Analysis has completed.  
`FINISHED_FAILED` | Analysis has finished unsuccessfully, the analysis itself is in a bad state.  
`FINISHED_UNSUPPORTED` | The resource is known not to be supported  
  
### AnalysisCompleted

Indicates which analysis completed successfully. Multiple types of analysis can be performed on a single resource.

JSON representation  
---  
      
    
    {
      "analysisType": [
        string
      ]
    }  
  
Fields  
---  
`analysisType[]` |  `string`  
  
### SBOMStatus

The status of an SBOM generation.

JSON representation  
---  
      
    
    {
      "sbomState": enum ([SBOMState](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.SBOMState)),
      "error": string
    }  
  
Fields  
---  
`sbomState` |  `enum (`[SBOMState](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.SBOMState)`)` The progress of the SBOM generation.  
`error` |  `string` If there was an error generating an SBOM, this will indicate what that error was.  
  
### SBOMState

An enum indicating the progress of the SBOM generation.

Enums  
---  
`SBOM_STATE_UNSPECIFIED` | Default unknown state.  
`PENDING` | SBOM scanning is pending.  
`COMPLETE` | SBOM scanning has completed.  
  
### File

JSON representation  
---  
      
    
    {
      "name": string,
      "digest": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`name` |  `string`  
`digest` |  `map (key: string, value: string)` An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### Details

Details of an attestation occurrence.

JSON representation  
---  
      
    
    {
      "attestation": {
        object ([Attestation](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Attestation))
      }
    }  
  
Fields  
---  
`attestation` |  `object (`[Attestation](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Attestation)`)` Required. Attestation for the resource.  
  
### Attestation

Occurrence that represents a single "attestation". The authenticity of an attestation can be verified using the attached signature. If the verifier trusts the public key of the signer, then verifying the signature is sufficient to establish trust. In this circumstance, the authority to which this attestation is attached is primarily useful for look-up (how to find this attestation if you already know the authority and artifact to be verified) and intent (which authority was this attestation intended to sign for).

JSON representation  
---  
      
    
    {
    
      // Union field signature can be only one of the following:
      "pgpSignedAttestation": {
        object ([PgpSignedAttestation](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.PgpSignedAttestation))
      },
      "genericSignedAttestation": {
        object ([GenericSignedAttestation](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.GenericSignedAttestation))
      }
      // End of list of possible types for union field signature.
    }  
  
Fields  
---  
Union field `signature`. Required. The signature, generally over the `resource_url`, that verifies this attestation. The semantics of the signature veracity are ultimately determined by the verification engine. `signature` can be only one of the following:  
`pgpSignedAttestation` |  `object (`[PgpSignedAttestation](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.PgpSignedAttestation)`)` A PGP signed attestation.  
`genericSignedAttestation` |  `object (`[GenericSignedAttestation](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.GenericSignedAttestation)`)`  
  
### PgpSignedAttestation

An attestation wrapper with a PGP-compatible signature. This message only supports `ATTACHED` signatures, where the payload that is signed is included alongside the signature itself in the same file.

JSON representation  
---  
      
    
    {
      "signature": string,
      "contentType": enum ([ContentType](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.ContentType)),
    
      // Union field key_id can be only one of the following:
      "pgpKeyId": string
      // End of list of possible types for union field key_id.
    }  
  
Fields  
---  
`signature` |  `string` Required. The raw content of the signature, as output by GNU Privacy Guard (GPG) or equivalent. Since this message only supports attached signatures, the payload that was signed must be attached. While the signature format supported is dependent on the verification implementation, currently only ASCII-armored (`--armor` to gpg), non-clearsigned (`--sign` rather than `--clearsign` to gpg) are supported. Concretely, `gpg --sign --armor --output=signature.gpg payload.json` will create the signature content expected in this field in `signature.gpg` for the `payload.json` attestation payload.  
`contentType` |  `enum (`[ContentType](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.ContentType)`)` Type (for example schema) of the attestation payload that was signed. The verifier must ensure that the provided type is one that the verifier supports, and that the attestation payload is a valid instantiation of that type (for example by validating a JSON schema).  
Union field `key_id`. This field is used by verifiers to select the public key used to validate the signature. Note that the policy of the verifier ultimately determines which public keys verify a signature based on the context of the verification. There is no guarantee validation will succeed if the verifier has no key matching this ID, even if it has a key under a different ID that would verify the signature. Note that this ID should also be present in the signature content above, but that is not expected to be used by the verifier. `key_id` can be only one of the following:  
`pgpKeyId` |  `string` The cryptographic fingerprint of the key used to generate the signature, as output by, e.g. `gpg --list-keys`. This should be the version 4, full 160-bit fingerprint, expressed as a 40 character hexadecimal string. See <https://tools.ietf.org/html/rfc4880#section-12.2> for details. Implementations may choose to acknowledge "LONG", "SHORT", or other abbreviated key IDs, but only the full fingerprint is guaranteed to work. In gpg, the full fingerprint can be retrieved from the `fpr` field returned when calling --list-keys with --with-colons. For example:
    
    
    gpg --with-colons --with-fingerprint --force-v4-certs \
        --list-keys attester@example.com
    tru::1:1513631572:0:3:1:5
    pub:...<SNIP>...
    fpr:::::::::24FF6481B76AC91E66A00AC657A93A81EF3AE6FB:
    

Above, the fingerprint is `24FF6481B76AC91E66A00AC657A93A81EF3AE6FB`.  
  
### ContentType

Type (for example schema) of the attestation payload that was signed.

Enums  
---  
`CONTENT_TYPE_UNSPECIFIED` | `ContentType` is not set.  
`SIMPLE_SIGNING_JSON` | Atomic format attestation signature. See <https://github.com/containers/image/blob/8a5d2f82a6e3263290c8e0276c3e0f64e77723e7/docs/atomic-signature.md> The payload extracted from `signature` is a JSON blob conforming to the linked schema.  
  
### GenericSignedAttestation

An attestation wrapper that uses the Grafeas `Signature` message. This attestation must define the `serializedPayload` that the `signatures` verify and any metadata necessary to interpret that plaintext. The signatures should always be over the `serializedPayload` bytestring.

JSON representation  
---  
      
    
    {
      "contentType": enum ([ContentType](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.ContentType_1)),
      "serializedPayload": string,
      "signatures": [
        {
          object ([Signature](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Signature))
        }
      ]
    }  
  
Fields  
---  
`contentType` |  `enum (`[ContentType](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.ContentType_1)`)` Type (for example schema) of the attestation payload that was signed. The verifier must ensure that the provided type is one that the verifier supports, and that the attestation payload is a valid instantiation of that type (for example by validating a JSON schema).  
`serializedPayload` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The serialized payload that is verified by one or more `signatures`. The encoding and semantic meaning of this payload must match what is set in `contentType`.A base64-encoded string.  
`signatures[]` |  `object (`[Signature](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Signature)`)` One or more signatures over `serializedPayload`. Verifier implementations should consider this attestation message verified if at least one `signature` verifies `serializedPayload`. See `Signature` in common.proto for more details on signature structure and verification.  
  
### ContentType

Type of the attestation plaintext that was signed.

Enums  
---  
`CONTENT_TYPE_UNSPECIFIED` | `ContentType` is not set.  
`SIMPLE_SIGNING_JSON` | Atomic format attestation signature. See <https://github.com/containers/image/blob/8a5d2f82a6e3263290c8e0276c3e0f64e77723e7/docs/atomic-signature.md> The payload extracted in `plaintext` is a JSON blob conforming to the linked schema.  
  
### Signature

Verifiers (e.g. Kritis implementations) MUST verify signatures with respect to the trust anchors defined in policy (e.g. a Kritis policy). Typically this means that the verifier has been configured with a map from `publicKeyId` to public key material (and any required parameters, e.g. signing algorithm).

In particular, verification implementations MUST NOT treat the signature `publicKeyId` as anything more than a key lookup hint. The `publicKeyId` DOES NOT validate or authenticate a public key; it only provides a mechanism for quickly selecting a public key ALREADY CONFIGURED on the verifier through a trusted channel. Verification implementations MUST reject signatures in any of the following circumstances: * The `publicKeyId` is not recognized by the verifier. * The public key that `publicKeyId` refers to does not verify the signature with respect to the payload.

The `signature` contents SHOULD NOT be "attached" (where the payload is included with the serialized `signature` bytes). Verifiers MUST ignore any "attached" payload and only verify signatures with respect to explicitly provided payload (e.g. a `payload` field on the proto message that holds this Signature, or the canonical serialization of the proto message that holds this signature).

JSON representation  
---  
      
    
    {
      "signature": string,
      "publicKeyId": string
    }  
  
Fields  
---  
`signature` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The content of the signature, an opaque bytestring. The payload that this signature verifies MUST be unambiguously provided with the Signature during verification. A wrapper message might provide the payload explicitly. Alternatively, a message might have a canonical serialization that can always be unambiguously computed to derive the payload.A base64-encoded string.  
`publicKeyId` |  `string` The identifier for the public key that verifies this signature. * The `publicKeyId` is required. * The `publicKeyId` SHOULD be an RFC3986 conformant URI. * When possible, the `publicKeyId` SHOULD be an immutable reference, such as a cryptographic digest.Examples of valid `publicKeyId`s:OpenPGP V4 public key fingerprint: * "openpgp4fpr:74FAF3B861BDA0870C7B6DEF607E48D2A663AEEA" See <https://www.iana.org/assignments/uri-schemes/prov/openpgp4fpr> for more details on this scheme.RFC6920 digest-named SubjectPublicKeyInfo (digest of the DER serialization): * "ni:///sha-256;cD9o9Cq6LG3jD0iKXqEi_vdjJGecm_iXkbqVoScViaU" * "nih:///sha-256;703f68f42aba2c6de30f488a5ea122fef76324679c9bf89791ba95a1271589a5"  
  
### Details

This corresponds to a signed in-toto link - it is made up of one or more signatures and the in-toto link itself. This is used for occurrences of a Grafeas in-toto note.

JSON representation  
---  
      
    
    {
      "signatures": [
        {
          object ([Signature](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Signature_1))
        }
      ],
      "signed": {
        object ([Link](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Link))
      }
    }  
  
Fields  
---  
`signatures[]` |  `object (`[Signature](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Signature_1)`)`  
`signed` |  `object (`[Link](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Link)`)`  
  
### Signature

A signature object consists of the KeyID used and the signature itself.

JSON representation  
---  
      
    
    {
      "keyid": string,
      "sig": string
    }  
  
Fields  
---  
`keyid` |  `string`  
`sig` |  `string`  
  
### Link

This corresponds to an in-toto link.

JSON representation  
---  
      
    
    {
      "command": [
        string
      ],
      "materials": [
        {
          object ([Artifact](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Artifact_1))
        }
      ],
      "products": [
        {
          object ([Artifact](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Artifact_1))
        }
      ],
      "byproducts": {
        object ([ByProducts](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.ByProducts))
      },
      "environment": {
        object ([Environment](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Environment))
      }
    }  
  
Fields  
---  
`command[]` |  `string` This field contains the full command executed for the step. This can also be empty if links are generated for operations that aren't directly mapped to a specific command. Each term in the command is an independent string in the list. An example of a command in the in-toto metadata field is: "command": ["git", "clone", "https://github.com/in-toto/demo-project.git"]  
`materials[]` |  `object (`[Artifact](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Artifact_1)`)` Materials are the supply chain artifacts that go into the step and are used for the operation performed. The key of the map is the path of the artifact and the structure contains the recorded hash information. An example is: "materials": [ { "resourceUri": "foo/bar", "hashes": { "sha256": "ebebf...", :  } } ]  
`products[]` |  `object (`[Artifact](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Artifact_1)`)` Products are the supply chain artifacts generated as a result of the step. The structure is identical to that of materials.  
`byproducts` |  `object (`[ByProducts](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.ByProducts)`)` ByProducts are data generated as part of a software supply chain step, but are not the actual result of the step.  
`environment` |  `object (`[Environment](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Environment)`)` This is a field that can be used to capture information about the environment. It is suggested for this field to contain information that details environment variables, filesystem information, and the present working directory. The recommended structure of this field is: "environment": { "customValues": { "variables": "", "filesystem": "", "workdir": "", "": "..." } }  
  
### Artifact

JSON representation  
---  
      
    
    {
      "resourceUri": string,
      "hashes": {
        object ([ArtifactHashes](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.ArtifactHashes))
      }
    }  
  
Fields  
---  
`resourceUri` |  `string`  
`hashes` |  `object (`[ArtifactHashes](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.ArtifactHashes)`)`  
  
### ArtifactHashes

Defines a hash object for use in Materials and Products.

JSON representation  
---  
      
    
    {
      "sha256": string
    }  
  
Fields  
---  
`sha256` |  `string`  
  
### ByProducts

Defines an object for the byproducts field in in-toto links. The suggested fields are "stderr", "stdout", and "return-value".

JSON representation  
---  
      
    
    {
      "customValues": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`customValues` |  `map (key: string, value: string)` An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### Environment

Defines an object for the environment field in in-toto links. The suggested fields are "variables", "filesystem", and "workdir".

JSON representation  
---  
      
    
    {
      "customValues": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`customValues` |  `map (key: string, value: string)` An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### DocumentOccurrence

DocumentOccurrence represents an SPDX Document Creation Information section: <https://spdx.github.io/spdx-spec/2-document-creation-information/>

JSON representation  
---  
      
    
    {
      "id": string,
      "title": string,
      "namespace": string,
      "externalDocumentRefs": [
        string
      ],
      "licenseListVersion": string,
      "creators": [
        string
      ],
      "createTime": string,
      "creatorComment": string,
      "documentComment": string
    }  
  
Fields  
---  
`id` |  `string` Identify the current SPDX document which may be referenced in relationships by other files, packages internally and documents externally  
`title` |  `string` Identify name of this document as designated by creator  
`namespace` |  `string` Provide an SPDX document specific namespace as a unique absolute Uniform Resource Identifier (URI) as specified in RFC-3986, with the exception of the ‘#’ delimiter  
`externalDocumentRefs[]` |  `string` Identify any external SPDX documents referenced within this SPDX document  
`licenseListVersion` |  `string` A field for creators of the SPDX file to provide the version of the SPDX License List used when the SPDX file was created  
`creators[]` |  `string` Identify who (or what, in the case of a tool) created the SPDX file. If the SPDX file was created by an individual, indicate the person's name  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Identify when the SPDX file was originally created. The date is to be specified according to combined date and time in UTC format as specified in ISO 8601 standardUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`creatorComment` |  `string` A field for creators of the SPDX file to provide general comments about the creation of the SPDX file or any other relevant comment not included in the other fields  
`documentComment` |  `string` A field for creators of the SPDX file content to provide comments to the consumers of the SPDX document  
  
### PackageInfoOccurrence

PackageInfoOccurrence represents an SPDX Package Information section: <https://spdx.github.io/spdx-spec/3-package-information/>

JSON representation  
---  
      
    
    {
      "id": string,
      "filename": string,
      "sourceInfo": string,
      "licenseConcluded": {
        object ([License](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/License))
      },
      "comment": string,
      "packageType": string,
      "title": string,
      "version": string,
      "homePage": string,
      "summaryDescription": string
    }  
  
Fields  
---  
`id` |  `string` Uniquely identify any element in an SPDX document which may be referenced by other elements  
`filename` |  `string` Provide the actual file name of the package, or path of the directory being treated as a package  
`sourceInfo` |  `string` Provide a place for the SPDX file creator to record any relevant background information or additional comments about the origin of the package  
`licenseConcluded` |  `object (`[License](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/License)`)` package or alternative values, if the governing license cannot be determined  
`comment` |  `string` A place for the SPDX file creator to record any general comments about the package being described  
`packageType` |  `string` Output only. The type of package: OS, MAVEN, GO, GO_STDLIB, etc.  
`title` |  `string` Output only. Identify the full name of the package as given by the Package Originator  
`version` |  `string` Output only. Identify the version of the package  
`homePage` |  `string` Output only. Provide a place for the SPDX file creator to record a web site that serves as the package's home page  
`summaryDescription` |  `string` Output only. A short description of the package  
  
### FileOccurrence

FileOccurrence represents an SPDX File Information section: <https://spdx.github.io/spdx-spec/4-file-information/>

JSON representation  
---  
      
    
    {
      "id": string,
      "licenseConcluded": {
        object ([License](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/License))
      },
      "filesLicenseInfo": [
        string
      ],
      "copyright": string,
      "comment": string,
      "notice": string,
      "contributors": [
        string
      ],
      "attributions": [
        string
      ]
    }  
  
Fields  
---  
`id` |  `string` Uniquely identify any element in an SPDX document which may be referenced by other elements  
`licenseConcluded` |  `object (`[License](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/License)`)` This field contains the license the SPDX file creator has concluded as governing the file or alternative values if the governing license cannot be determined  
`filesLicenseInfo[]` |  `string` This field contains the license information actually found in the file, if any  
`copyright` |  `string` Identify the copyright holder of the file, as well as any dates present  
`comment` |  `string` This field provides a place for the SPDX file creator to record any general comments about the file  
`notice` |  `string` This field provides a place for the SPDX file creator to record license notices or other such related notices found in the file  
`contributors[]` |  `string` This field provides a place for the SPDX file creator to record file contributors  
`attributions[]` |  `string` This field provides a place for the SPDX data creator to record, at the file level, acknowledgements that may be needed to be communicated in some contexts  
  
### RelationshipOccurrence

RelationshipOccurrence represents an SPDX Relationship section: <https://spdx.github.io/spdx-spec/7-relationships-between-SPDX-elements/>

JSON representation  
---  
      
    
    {
      "source": string,
      "target": string,
      "type": enum ([RelationshipType](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/RelationshipType)),
      "comment": string
    }  
  
Fields  
---  
`source` |  `string` Also referred to as SPDXRef-A The source SPDX element (file, package, etc)  
`target` |  `string` Also referred to as SPDXRef-B The target SPDC element (file, package, etc) In cases where there are "known unknowns", the use of the keyword NOASSERTION can be used The keywords NONE can be used to indicate that an SPDX element (package/file/snippet) has no other elements connected by some relationship to it  
`type` |  `enum (`[RelationshipType](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/RelationshipType)`)` Output only. The type of relationship between the source and target SPDX elements  
`comment` |  `string` A place for the SPDX file creator to record any general comments about the relationship  
  
### SBOMReferenceOccurrence

The occurrence representing an SBOM reference as applied to a specific resource. The occurrence follows the DSSE specification. See <https://github.com/secure-systems-lab/dsse/blob/master/envelope.md> for more details.

JSON representation  
---  
      
    
    {
      "payload": {
        object ([SbomReferenceIntotoPayload](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.SbomReferenceIntotoPayload))
      },
      "payloadType": string,
      "signatures": [
        {
          object ([EnvelopeSignature](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.EnvelopeSignature))
        }
      ]
    }  
  
Fields  
---  
`payload` |  `object (`[SbomReferenceIntotoPayload](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.SbomReferenceIntotoPayload)`)` The actual payload that contains the SBOM reference data.  
`payloadType` |  `string` The kind of payload that SbomReferenceIntotoPayload takes. Since it's in the intoto format, this value is expected to be 'application/vnd.in-toto+json'.  
`signatures[]` |  `object (`[EnvelopeSignature](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.EnvelopeSignature)`)` The signatures over the payload.  
  
### SbomReferenceIntotoPayload

The actual payload that contains the SBOM Reference data. The payload follows the intoto statement specification. See <https://github.com/in-toto/attestation/blob/main/spec/v1.0/statement.md> for more details.

JSON representation  
---  
      
    
    {
      "_type": string,
      "predicateType": string,
      "subject": [
        {
          object ([Subject](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Subject))
        }
      ],
      "predicate": {
        object ([SbomReferenceIntotoPredicate](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.SbomReferenceIntotoPredicate))
      }
    }  
  
Fields  
---  
`_type` |  `string` Identifier for the schema of the Statement.  
`predicateType` |  `string` URI identifying the type of the Predicate.  
`subject[]` |  `object (`[Subject](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Subject)`)` Set of software artifacts that the attestation applies to. Each element represents a single software artifact.  
`predicate` |  `object (`[SbomReferenceIntotoPredicate](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.SbomReferenceIntotoPredicate)`)` Additional parameters of the Predicate. Includes the actual data about the SBOM.  
  
### SbomReferenceIntotoPredicate

A predicate which describes the SBOM being referenced.

JSON representation  
---  
      
    
    {
      "referrerId": string,
      "location": string,
      "mimeType": string,
      "digest": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`referrerId` |  `string` The person or system referring this predicate to the consumer.  
`location` |  `string` The location of the SBOM.  
`mimeType` |  `string` The mime type of the SBOM.  
`digest` |  `map (key: string, value: string)` A map of algorithm to digest of the contents of the SBOM.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### EnvelopeSignature

JSON representation  
---  
      
    
    {
      "sig": string,
      "keyid": string
    }  
  
Fields  
---  
`sig` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` A base64-encoded string.  
`keyid` |  `string`  
  
### SecretOccurrence

The occurrence provides details of a secret.

JSON representation  
---  
      
    
    {
      "kind": enum ([SecretKind](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.SecretKind)),
      "locations": [
        {
          object ([SecretLocation](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.SecretLocation))
        }
      ],
      "statuses": [
        {
          object ([SecretStatus](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.SecretStatus))
        }
      ]
    }  
  
Fields  
---  
`kind` |  `enum (`[SecretKind](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.SecretKind)`)` Required. Type of secret.  
`locations[]` |  `object (`[SecretLocation](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.SecretLocation)`)` Optional. Locations where the secret is detected.  
`statuses[]` |  `object (`[SecretStatus](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.SecretStatus)`)` Optional. Status of the secret.  
  
### SecretKind

Kind of secret.

Enums  
---  
`SECRET_KIND_UNSPECIFIED` | Unspecified  
`SECRET_KIND_UNKNOWN` | The secret kind is unknown.  
`SECRET_KIND_GCP_SERVICE_ACCOUNT_KEY` | A Google Cloud service account key per: <https://cloud.google.com/iam/docs/creating-managing-service-account-keys>  
`SECRET_KIND_GCP_API_KEY` | A Google Cloud API key per: <https://cloud.google.com/docs/authentication/api-keys>  
`SECRET_KIND_GCP_OAUTH2_CLIENT_CREDENTIALS` | A Google Cloud OAuth2 client credentials per: <https://developers.google.com/identity/protocols/oauth2>  
`SECRET_KIND_GCP_OAUTH2_ACCESS_TOKEN` | A Google Cloud OAuth2 access token per: <https://cloud.google.com/docs/authentication/token-types#access>  
`SECRET_KIND_ANTHROPIC_ADMIN_API_KEY` | An Anthropic Admin API key.  
`SECRET_KIND_ANTHROPIC_API_KEY` | An Anthropic API key.  
`SECRET_KIND_AZURE_ACCESS_TOKEN` | An Azure access token.  
`SECRET_KIND_AZURE_IDENTITY_TOKEN` | An Azure Identity Platform ID token.  
`SECRET_KIND_DOCKER_HUB_PERSONAL_ACCESS_TOKEN` | A Docker Hub personal access token.  
`SECRET_KIND_GITHUB_APP_REFRESH_TOKEN` | A GitHub App refresh token.  
`SECRET_KIND_GITHUB_APP_SERVER_TO_SERVER_TOKEN` | A GitHub App server-to-server token.  
`SECRET_KIND_GITHUB_APP_USER_TO_SERVER_TOKEN` | A GitHub App user-to-server token.  
`SECRET_KIND_GITHUB_CLASSIC_PERSONAL_ACCESS_TOKEN` | A GitHub personal access token (classic).  
`SECRET_KIND_GITHUB_FINE_GRAINED_PERSONAL_ACCESS_TOKEN` | A GitHub fine-grained personal access token.  
`SECRET_KIND_GITHUB_OAUTH_TOKEN` | A GitHub OAuth token.  
`SECRET_KIND_HUGGINGFACE_API_KEY` | A Hugging Face API key.  
`SECRET_KIND_OPENAI_API_KEY` | An OpenAI API key.  
`SECRET_KIND_PERPLEXITY_API_KEY` | A Perplexity API key.  
`SECRET_KIND_STRIPE_SECRET_KEY` | A Stripe secret key.  
`SECRET_KIND_STRIPE_RESTRICTED_KEY` | A Stripe restricted key.  
`SECRET_KIND_STRIPE_WEBHOOK_SECRET` | A Stripe webhook secret.  
  
### SecretLocation

The location of the secret.

JSON representation  
---  
      
    
    {
    
      // Union field location can be only one of the following:
      "fileLocation": {
        object ([FileLocation](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.FileLocation))
      }
      // End of list of possible types for union field location.
    }  
  
Fields  
---  
Union field `location`. The detailed location of the secret. `location` can be only one of the following:  
`fileLocation` |  `object (`[FileLocation](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.FileLocation)`)` The secret is found from a file.  
  
### FileLocation

Indicates the location at which a package was found.

JSON representation  
---  
      
    
    {
      "filePath": string
    }  
  
Fields  
---  
`filePath` |  `string` For jars that are contained inside .war files, this filepath can indicate the path to war file combined with the path to jar file.  
  
### SecretStatus

The status of the secret with a timestamp.

JSON representation  
---  
      
    
    {
      "status": enum ([Status](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Status)),
      "updateTime": string,
      "message": string
    }  
  
Fields  
---  
`status` |  `enum (`[Status](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.Status)`)` Optional. The status of the secret.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. The time the secret status was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`message` |  `string` Optional. Optional message about the status code.  
  
### Status

The status of the secret.

Enums  
---  
`STATUS_UNSPECIFIED` | Unspecified  
`UNKNOWN` | The status of the secret is unknown.  
`VALID` | The secret is valid.  
`INVALID` | The secret is invalid.  
  
### Envelope

MUST match <https://github.com/secure-systems-lab/dsse/blob/master/envelope.proto>. An authenticated message of arbitrary type.

JSON representation  
---  
      
    
    {
      "payload": string,
      "payloadType": string,
      "signatures": [
        {
          object ([EnvelopeSignature](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.EnvelopeSignature))
        }
      ]
    }  
  
Fields  
---  
`payload` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` A base64-encoded string.  
`payloadType` |  `string`  
`signatures[]` |  `object (`[EnvelopeSignature](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence.EnvelopeSignature)`)`  
  
## Methods  
  
---  
  
### `[batchCreate](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences/batchCreate)`

|  Creates new occurrences in batch.  
  
### `[create](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences/create)`

|  Creates a new occurrence.  
  
### `[delete](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences/delete)`

|  Deletes the specified occurrence.  
  
### `[get](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences/get)`

|  Gets the specified occurrence.  
  
### `[getIamPolicy](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences/getIamPolicy)`

|  Gets the access control policy for a note or an occurrence resource.  
  
### `[getNotes](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences/getNotes)`

|  Gets the note attached to the specified occurrence.  
  
### `[getVulnerabilitySummary](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences/getVulnerabilitySummary)`

|  Gets a summary of the number and severity of occurrences.  
  
### `[list](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences/list)`

|  Lists occurrences for the specified project.  
  
### `[patch](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences/patch)`

|  Updates the specified occurrence.  
  
### `[setIamPolicy](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences/setIamPolicy)`

|  Sets the access control policy on the specified note or occurrence.  
  
### `[testIamPermissions](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences/testIamPermissions)`

|  Returns the permissions that a caller has on the specified note or occurrence.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-09 UTC."],[],[]] 
