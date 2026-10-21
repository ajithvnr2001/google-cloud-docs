---
url: https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flagReleases
title: REST Resource: projects.locations.flagReleases \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:39:53.721434+00:00
---

# REST Resource: projects.locations.flagReleases  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flagReleases

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Reference ](https://docs.cloud.google.com/app-lifecycle-manager/apis)



Send feedback 

#  REST Resource: projects.locations.flagReleases Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: FlagRelease
    * JSON representation
  * FlagRevisionList
    * JSON representation
  * FlagSetList
    * JSON representation
  * Methods



## Resource: FlagRelease

A collection of `[FlagRevision](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flagRevisions#FlagRevision)`s.

JSON representation  
---  
      
    
    {
      "name": string,
      "flagRevisions": [
        string
      ],
      "obsoleteFlags": [
        string
      ],
      "unitKind": string,
      "flagSets": [
        string
      ],
      "allFlags": boolean,
      "effectiveFlagRevisions": [
        string
      ],
      "labels": {
        string: string,
        ...
      },
      "annotations": {
        string: string,
        ...
      },
      "uid": string,
      "etag": string,
      "createTime": string,
      "updateTime": string,
    
      // Union field release_content can be only one of the following:
      "flagRevisionsRelease": {
        object ([FlagRevisionList](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flagReleases#FlagRevisionList))
      },
      "flagSetsRelease": {
        object ([FlagSetList](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flagReleases#FlagSetList))
      },
      "allFlagsRelease": boolean
      // End of list of possible types for union field release_content.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name (full URI of the resource) following the standard naming scheme:"projects/{project}/locations/{location}/flagReleases/{flagReleaseId}"  
`flagRevisions[]  
**(deprecated)**` |  `string` This item is deprecated!Optional. Immutable. DEPRECATED: Use flagRevisionsRelease instead. `[FlagRevision](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flagRevisions#FlagRevision)`s to be rolled out. Only one of flagRevisions, allFlags, or flagSets can be set. It used to be the ultimate source to truth and has been moved to effectiveFlagRevisions.  
`obsoleteFlags[]  
**(deprecated)**` |  `string` This item is deprecated!Optional. Immutable. Deprecated: Use the 'state' field in the 'Flag' resource to manage the cleanup of flag lifecycles including removal from UnitKind and Units. `[Flag](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flags#Flag)`s to be removed from given UnitKind and all related Units. If `[Flag](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flags#Flag)` is provided here, its `[FlagRevision](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flagRevisions#FlagRevision)`s will be removed from UnitKind and Units.  
`unitKind` |  `string` Required. Immutable. The `[UnitKind](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitKinds#UnitKind)` this FlagRelease applies to.  
`flagSets[]  
**(deprecated)**` |  `string` This item is deprecated!Optional. Immutable. DEPRECATED: Use flagSetsRelease instead. Flag sets to be rolled out. Only one of flagRevisions, allFlags, or flagSets can be set.  
`allFlags  
**(deprecated)**` |  `boolean` This item is deprecated!Optional. Immutable. DEPRECATED: Use allFlagsRelease instead. Rollout all flags in the provided UnitKind. Only one of flagRevisions, allFlags, or flagSets can be set.  
`effectiveFlagRevisions[]` |  `string` Output only. An OUTPUT_ONLY field that contains `[FlagRevision](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flagRevisions#FlagRevision)`s to be rolled out. This is the ultimate source of truth of what a `[Rollout](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.rollouts#Rollout)` or a `[UnitOperation](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitOperations#UnitOperation)` carries.  
`labels` |  `map (key: string, value: string)` Optional. The labels on the resource, which can be used for categorization. similar to Kubernetes resource labels.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`annotations` |  `map (key: string, value: string)` Optional. Annotations is an unstructured key-value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects.More info: <https://kubernetes.io/docs/user-guide/annotations>An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`uid` |  `string` Output only. The unique identifier of the resource. UID is unique in the time and space for this resource within the scope of the service. It is typically generated by the server on successful creation of a resource and must not be changed. UID is used to uniquely identify resources with resource name reuses. This should be a UUID4.  
`etag` |  `string` Output only. An opaque value that uniquely identifies a version or generation of a resource. It can be used to confirm that the client and server agree on the ordering of a resource being written.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was last updated. Any change to the resource made by users must refresh this value. Changes to a resource made by the service should refresh this value.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
Union field `release_content`. Defines the content or type of this flag release. Only one field within this oneof can be set. `release_content` can be only one of the following:  
`flagRevisionsRelease` |  `object (`[FlagRevisionList](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flagReleases#FlagRevisionList)`)` Optional. Immutable. Specifies the release consists of a list of flag revisions.  
`flagSetsRelease` |  `object (`[FlagSetList](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flagReleases#FlagSetList)`)` Optional. Immutable. Specifies the release consists of a list of flag sets.  
`allFlagsRelease` |  `boolean` Optional. Immutable. Specifies the release includes all flags.  
  
## FlagRevisionList

Wrapper for a list of flag revisions.

JSON representation  
---  
      
    
    {
      "revisions": [
        string
      ]
    }  
  
Fields  
---  
`revisions[]` |  `string` Required. `[FlagRevision](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flagRevisions#FlagRevision)`s to be rolled out.  
  
## FlagSetList

Wrapper for a list of flag sets.

JSON representation  
---  
      
    
    {
      "sets": [
        string
      ]
    }  
  
Fields  
---  
`sets[]` |  `string` Required. Flag sets to be rolled out.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flagReleases/create)`

|  Create a new flag release.  
  
### `[delete](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flagReleases/delete)`

|  Delete a single flag release.  
  
### `[get](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flagReleases/get)`

|  Retrieve a single flag release.  
  
### `[list](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flagReleases/list)`

|  Retrieve a collection of flag releases.  
  
### `[patch](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flagReleases/patch)`

|  Update a single flag release.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-17 UTC."],[],[]] 
