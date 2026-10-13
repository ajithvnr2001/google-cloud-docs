---
url: https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.notes
title: REST Resource: projects.notes \u00a0|\u00a0 Artifact Analysis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:06:16.961205+00:00
---

# REST Resource: projects.notes  |  Artifact Analysis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.notes

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)
  * [ Reference ](https://docs.cloud.google.com/artifact-analysis/docs/apis)



Send feedback 

#  REST Resource: projects.notes Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Note
    * JSON representation
  * Methods



## Resource: Note

A type of analysis that can be done for a resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "shortDescription": string,
      "longDescription": string,
      "kind": enum ([NoteKind](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/NoteKind)),
      "relatedUrl": [
        {
          object ([RelatedUrl](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/RelatedUrl))
        }
      ],
      "expirationTime": string,
      "createTime": string,
      "updateTime": string,
      "relatedNoteNames": [
        string
      ],
    
      // Union field type can be only one of the following:
      "vulnerability": {
        object ([Vulnerability](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.notes#Note.Vulnerability))
      },
      "build": {
        object ([Build](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.notes#Note.Build))
      },
      "baseImage": {
        object ([Basis](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.notes#Note.Basis))
      },
      "package": {
        object ([Package](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.notes#Note.Package))
      },
      "deployable": {
        object ([Deployable](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.notes#Note.Deployable))
      },
      "discovery": {
        object ([Discovery](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.notes#Note.Discovery))
      },
      "attestationAuthority": {
        object ([Authority](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.notes#Note.Authority))
      },
      "intoto": {
        object ([InToto](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.notes#Note.InToto))
      },
      "sbom": {
        object ([DocumentNote](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.notes#Note.DocumentNote))
      },
      "spdxPackage": {
        object ([PackageInfoNote](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.notes#Note.PackageInfoNote))
      },
      "spdxFile": {
        object ([FileNote](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.notes#Note.FileNote))
      },
      "spdxRelationship": {
        object ([RelationshipNote](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.notes#Note.RelationshipNote))
      },
      "vulnerabilityAssessment": {
        object ([VulnerabilityAssessmentNote](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.notes#Note.VulnerabilityAssessmentNote))
      },
      "sbomReference": {
        object ([SBOMReferenceNote](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.notes#Note.SBOMReferenceNote))
      },
      "secret": {
        object ([SecretNote](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.notes#Note.SecretNote))
      }
      // End of list of possible types for union field type.
    }  
  
Fields  
---  
`name` |  `string` Output only. The name of the note in the form of `projects/[PROVIDER_ID]/notes/[NOTE_ID]`.  
`shortDescription` |  `string` A one sentence description of this note.  
`longDescription` |  `string` A detailed description of this note.  
`kind` |  `enum (`[NoteKind](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/NoteKind)`)` Output only. The type of analysis. This field can be used as a filter in list requests.  
`relatedUrl[]` |  `object (`[RelatedUrl](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/RelatedUrl)`)` URLs associated with this note.  
`expirationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time of expiration for this note. Empty if note does not expire.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time this note was created. This field can be used as a filter in list requests.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time this note was last updated. This field can be used as a filter in list requests.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`relatedNoteNames[]` |  `string` Other notes related to this note.  
Union field `type`. Required. Immutable. The type of analysis this note represents. `type` can be only one of the following:  
`vulnerability` |  `object (`[Vulnerability](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.notes#Note.Vulnerability)`)` A note describing a package vulnerability.  
`build` |  `object (`[Build](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.notes#Note.Build)`)` A note describing build provenance for a verifiable build.  
`baseImage` |  `object (`[Basis](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.notes#Note.Basis)`)` A note describing a base image.  
`package` |  `object (`[Package](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.notes#Note.Package)`)` A note describing a package hosted by various package managers.  
`deployable` |  `object (`[Deployable](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.notes#Note.Deployable)`)` A note describing something that can be deployed.  
`discovery` |  `object (`[Discovery](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.notes#Note.Discovery)`)` A note describing the initial analysis of a resource.  
`attestationAuthority` |  `object (`[Authority](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.notes#Note.Authority)`)` A note describing an attestation role.  
`intoto` |  `object (`[InToto](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.notes#Note.InToto)`)` A note describing an in-toto link.  
`sbom` |  `object (`[DocumentNote](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.notes#Note.DocumentNote)`)` A note describing a software bill of materials.  
`spdxPackage` |  `object (`[PackageInfoNote](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.notes#Note.PackageInfoNote)`)` A note describing an SPDX Package.  
`spdxFile` |  `object (`[FileNote](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.notes#Note.FileNote)`)` A note describing an SPDX File.  
`spdxRelationship` |  `object (`[RelationshipNote](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.notes#Note.RelationshipNote)`)` A note describing an SPDX File.  
`vulnerabilityAssessment` |  `object (`[VulnerabilityAssessmentNote](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.notes#Note.VulnerabilityAssessmentNote)`)` A note describing a vulnerability assessment.  
`sbomReference` |  `object (`[SBOMReferenceNote](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.notes#Note.SBOMReferenceNote)`)` A note describing an SBOM reference.  
`secret` |  `object (`[SecretNote](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.notes#Note.SecretNote)`)` A note describing a secret.  
  
## Methods  
  
---  
  
### `[batchCreate](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.notes/batchCreate)`

|  Creates new notes in batch.  
  
### `[create](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.notes/create)`

|  Creates a new note.  
  
### `[delete](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.notes/delete)`

|  Deletes the specified note.  
  
### `[get](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.notes/get)`

|  Gets the specified note.  
  
### `[getIamPolicy](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.notes/getIamPolicy)`

|  Gets the access control policy for a note or an occurrence resource.  
  
### `[list](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.notes/list)`

|  Lists notes for the specified project.  
  
### `[patch](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.notes/patch)`

|  Updates the specified note.  
  
### `[setIamPolicy](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.notes/setIamPolicy)`

|  Sets the access control policy on the specified note or occurrence.  
  
### `[testIamPermissions](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.notes/testIamPermissions)`

|  Returns the permissions that a caller has on the specified note or occurrence.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-09 UTC."],[],[]] 
