---
url: https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills.revisions
title: REST Resource: projects.locations.skills.revisions \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:06:45.507317+00:00
---

# REST Resource: projects.locations.skills.revisions  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills.revisions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Reference ](https://docs.cloud.google.com/agent-registry/apis)



Send feedback 

#  REST Resource: projects.locations.skills.revisions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: SkillRevision
    * JSON representation
    * GcsSource
      * JSON representation
    * ArchiveUploadSource
      * JSON representation
    * State
  * Methods



## Resource: SkillRevision

Represents an immutable, versioned snapshot of a Skill package.

JSON representation  
---  
      
    
    {
      "name": string,
      "state": enum ([State](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills.revisions#SkillRevision.State)),
      "sha256Hash": string,
      "frontmatter": {
        object ([Frontmatter](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/Frontmatter))
      },
      "createTime": string,
      "sizeBytes": string,
      "uid": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "gcsSource": {
        object ([GcsSource](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills.revisions#SkillRevision.GcsSource))
      },
      "archiveUploadSource": {
        object ([ArchiveUploadSource](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills.revisions#SkillRevision.ArchiveUploadSource))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Identifier. Resource name of the SkillRevision. Format: `projects/{project}/locations/{location}/skills/{skill}/revisions/{revision}`  
`state` |  `enum (`[State](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills.revisions#SkillRevision.State)`)` Output only. The system-managed lifecycle state of this revision.  
`sha256Hash` |  `string` Output only. Cryptographic SHA-256 integrity and deduplication digest of the payload zip.  
`frontmatter` |  `object (`[Frontmatter](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/Frontmatter)`)` Output only. Extracted YAML frontmatter configuration snapshot.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Revision creation timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`sizeBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Size of the compiled zip payload in bytes (assists client download progress).  
`uid` |  `string` Output only. Universally unique identifier (UUID4) for the skill revision.  
Output only. The storage location pointer. In standard listing, the raw zip bytes are completely excluded. They are streamed separately via a dedicated GetSkillRevision request with `?alt=media`. The physical source pointing to the executable payload. Exactly one source must be provided during creation; otherwise, the server will return an `INVALID_ARGUMENT` error.Size constraints: - Maximum compressed ZIP size: 500 KB - Maximum total uncompressed size: 10 MB - Maximum individual uncompressed file size: 1 MB The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`gcsSource` |  `object (`[GcsSource](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills.revisions#SkillRevision.GcsSource)`)` Optional. Immutable. Cloud Storage object generation URI.  
`archiveUploadSource` |  `object (`[ArchiveUploadSource](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills.revisions#SkillRevision.ArchiveUploadSource)`)` Optional. Immutable. Direct write-only raw archive upload source.  
End of mutually exclusive fields.  
  
### GcsSource

Specifications for Cloud Storage objects.

JSON representation  
---  
      
    
    {
      "uri": string,
      "generation": string
    }  
  
Fields  
---  
`uri` |  `string` Required. Cloud Storage object URI. Format: `gs://{bucketName}/{objectName}`  
`generation` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Cloud Storage object generation ID. If not specified, the latest generation is used.  
  
### ArchiveUploadSource

Direct write-only raw archive payload upload.

JSON representation  
---  
      
    
    {
      "archiveContent": string
    }  
  
Fields  
---  
`archiveContent` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. Input only. Write-only raw ZIP/TAR archive payload bytes containing the skill package.A base64-encoded string.  
  
### State

System-managed computed state.

Enums  
---  
`STATE_UNSPECIFIED` | Default value. This value is unused.  
`CREATING` | The revision is being created.  
`ACTIVE` | The revision is active.  
`FAILED` | The revision failed to compile or ingest.  
`DELETING` | The revision is being deleted.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills.revisions/create)`

|  Creates a new immutable revision and triggers validation pipelines.  
  
### `[delete](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills.revisions/delete)`

|  Deletes a specific revision (restricted to admins to purge accidentally committed secrets).  
  
### `[get](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills.revisions/get)`

|  Gets details of a single immutable Revision.  
  
### `[list](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills.revisions/list)`

|  Lists all revisions belonging to a parent Skill.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
