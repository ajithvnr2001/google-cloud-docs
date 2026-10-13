---
url: https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/projects.locations.customClasses
title: REST Resource: projects.locations.customClasses \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:44:13.106470+00:00
---

# REST Resource: projects.locations.customClasses  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/projects.locations.customClasses

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)
  * [ Reference ](https://docs.cloud.google.com/speech-to-text/docs/apis)



Send feedback 

#  REST Resource: projects.locations.customClasses Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: CustomClass
    * JSON representation
  * ClassItem
    * JSON representation
  * State
  * Methods



## Resource: CustomClass

A set of words or phrases that represents a common concept likely to appear in your audio, for example a list of passenger ship names. CustomClass items can be substituted into placeholders that you set in PhraseSet phrases.

JSON representation  
---  
      
    
    {
      "name": string,
      "customClassId": string,
      "items": [
        {
          object ([ClassItem](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/projects.locations.customClasses#ClassItem))
        }
      ],
      "kmsKeyName": string,
      "kmsKeyVersionName": string,
      "uid": string,
      "displayName": string,
      "state": enum ([State](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/projects.locations.customClasses#State)),
      "deleteTime": string,
      "expireTime": string,
      "annotations": {
        string: string,
        ...
      },
      "etag": string,
      "reconciling": boolean
    }  
  
Fields  
---  
`name` |  `string` The resource name of the custom class.  
`customClassId` |  `string` If this custom class is a resource, the customClassId is the resource id of the CustomClass. Case sensitive.  
`items[]` |  `object (`[ClassItem](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/projects.locations.customClasses#ClassItem)`)` A collection of class items.  
`kmsKeyName` |  `string` Output only. The [KMS key name](https://cloud.google.com/kms/docs/resource-hierarchy#keys) with which the content of the ClassItem is encrypted. The expected format is `projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}`.  
`kmsKeyVersionName` |  `string` Output only. The [KMS key version name](https://cloud.google.com/kms/docs/resource-hierarchy#key_versions) with which content of the ClassItem is encrypted. The expected format is `projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}/cryptoKeyVersions/{crypto_key_version}`.  
`uid` |  `string` Output only. System-assigned unique identifier for the CustomClass. This field is not used.  
`displayName` |  `string` Output only. User-settable, human-readable name for the CustomClass. Must be 63 characters or less. This field is not used.  
`state` |  `enum (`[State](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/projects.locations.customClasses#State)`)` Output only. The CustomClass lifecycle state. This field is not used.  
`deleteTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which this resource was requested for deletion. This field is not used.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`expireTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which this resource will be purged. This field is not used.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`annotations` |  `map (key: string, value: string)` Output only. Allows users to store small amounts of arbitrary data. Both the key and the value must be 63 characters or less each. At most 100 annotations. This field is not used.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`etag` |  `string` Output only. This checksum is computed by the server based on the value of other fields. This may be sent on update, undelete, and delete requests to ensure the client has an up-to-date value before proceeding. This field is not used.  
`reconciling` |  `boolean` Output only. Whether or not this CustomClass is in the process of being updated. This field is not used.  
  
## ClassItem

An item of the class.

JSON representation  
---  
      
    
    {
      "value": string
    }  
  
Fields  
---  
`value` |  `string` The class item's value.  
  
## State

Set of states that define the lifecycle of a CustomClass.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified state. This is only used/useful for distinguishing unset values.  
`ACTIVE` | The normal and active state.  
`DELETED` | This CustomClass has been deleted.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/projects.locations.customClasses/create)`

|  Create a custom class.  
  
### `[delete](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/projects.locations.customClasses/delete)`

|  Delete a custom class.  
  
### `[get](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/projects.locations.customClasses/get)`

|  Get a custom class.  
  
### `[list](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/projects.locations.customClasses/list)`

|  List custom classes.  
  
### `[patch](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/projects.locations.customClasses/patch)`

|  Update a custom class.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-23 UTC."],[],[]] 
