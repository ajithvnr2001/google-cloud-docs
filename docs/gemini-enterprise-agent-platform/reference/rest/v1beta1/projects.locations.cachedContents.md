---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.cachedContents
title: REST Resource: projects.locations.cachedContents \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:50:02.373979+00:00
---

# REST Resource: projects.locations.cachedContents  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.cachedContents

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  REST Resource: projects.locations.cachedContents Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: CachedContent

A resource used in LLM queries for users to explicitly specify what to cache and how to cache.

Fields  
  
`name` `string` Immutable. Identifier. The server-generated resource name of the cached content Format: projects/{project}/locations/{location}/cachedContents/{cachedContent} | `displayName` `string` Optional. Immutable. The user-generated meaningful display name of the cached content. | `model` `string` Immutable. The name of the `Model` to use for cached content. Currently, only the published Gemini base models are supported, in form of projects/{PROJECT}/locations/{LOCATION}/publishers/google/models/{MODEL} | `systemInstruction` `object (`[Content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/Content)`)` Optional. Input only. Immutable. Developer set system instruction. Currently, text only | `contents[]` `object (`[Content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/Content)`)` Optional. Input only. Immutable. The content to cache | `tools[]` `object (`[Tool](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/GeminiExample#Tool)`)` Optional. Input only. Immutable. A list of `Tools` the model may use to generate the next response | `toolConfig` `object (`[ToolConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/GeminiExample#ToolConfig)`)` Optional. Input only. Immutable. Tool config. This config is shared for all tools | `createTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Creation time of the cache entry.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `updateTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the cache entry was last updated in UTC time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `usageMetadata` `object (`[UsageMetadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.cachedContents#UsageMetadata)`)` Output only. metadata on the usage of the cached content. | `encryptionSpec` `object (`[EncryptionSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/EncryptionSpec)`)` Input only. Immutable. Customer-managed encryption key spec for a `CachedContent`. If set, this `CachedContent` and all its sub-resources will be secured by this key. | `expiration` `Union type`  
  
Expiration time of the cached content. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`expireTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` timestamp of when this resource is considered expired. This is _always_ provided on output, regardless of what was sent on input.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `ttl` `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Input only. The TTL for this resource. The expiration time is computed: now + TTL.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "model": string,
      "systemInstruction": {
        object ([Content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/Content))
      },
      "contents": [
        {
          object ([Content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/Content))
        }
      ],
      "tools": [
        {
          object ([Tool](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/GeminiExample#Tool))
        }
      ],
      "toolConfig": {
        object ([ToolConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/GeminiExample#ToolConfig))
      },
      "createTime": string,
      "updateTime": string,
      "usageMetadata": {
        object ([UsageMetadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.cachedContents#UsageMetadata))
      },
      "encryptionSpec": {
        object ([EncryptionSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/EncryptionSpec))
      },
    
      // expiration
      "expireTime": string,
      "ttl": string
      // Union type
    }  
  
## UsageMetadata

metadata on the usage of the cached content.

Fields  
  
`totalTokenCount` `integer` Total number of tokens that the cached content consumes. | `textCount` `integer` Number of text characters. | `imageCount` `integer` Number of images. | `videoDurationSeconds` `integer` Duration of video in seconds. | `audioDurationSeconds` `integer` Duration of audio in seconds. | JSON representation  
---  
      
    
    {
      "totalTokenCount": integer,
      "textCount": integer,
      "imageCount": integer,
      "videoDurationSeconds": integer,
      "audioDurationSeconds": integer
    }  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.cachedContents/create)`

|  Creates cached content, this call will initialize the cached content in the data storage, and users need to pay for the cache data storage.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.cachedContents/delete)`

|  Deletes cached content  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.cachedContents/get)`

|  Gets cached content configurations  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.cachedContents/list)`

|  Lists cached contents in a project  
  
### `[patch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.cachedContents/patch)`

|  Updates cached content configurations  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
