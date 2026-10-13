---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.sessions/listSessionFileMetadata/
title: Method: projects.locations.collections.engines.sessions.listSessionFileMetadata \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:57:41.333246+00:00
---

# Method: projects.locations.collections.engines.sessions.listSessionFileMetadata  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.sessions/listSessionFileMetadata/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Reference ](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis)



Send feedback 

#  Method: projects.locations.collections.engines.sessions.listSessionFileMetadata Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * FileMetadata
    * JSON representation
  * FileSource



Lists metadata for all files in the current session.

### HTTP request

Choose an endpoint:

globalus

  
`GET https://discoveryengine.googleapis.com/v1alpha/{name=projects/*/locations/*/collections/*/engines/*/sessions/*}:listSessionFileMetadata`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the Session. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/sessions/{session}`  
  
### Request body

The request body must be empty.

### Response body

Response message for `[AssistantService.ListSessionFileMetadata](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.sessions/listSessionFileMetadata#google.cloud.discoveryengine.v1alpha.AssistantService.ListSessionFileMetadata)` method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "fileMetadata": [
        {
          object ([FileMetadata](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.sessions/listSessionFileMetadata#FileMetadata))
        }
      ],
      "totalQuotaPercentage": number
    }  
  
Fields  
---  
`fileMetadata[]` |  `object (`[FileMetadata](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.sessions/listSessionFileMetadata#FileMetadata)`)` The `[FileMetadata](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.sessions/listSessionFileMetadata#FileMetadata)`s.  
`totalQuotaPercentage  
**(deprecated)**` |  `number` This item is deprecated!Deprecated: This field may not be set, or the value may not take all file types into account. To be removed.The total quota percentage used by all the files.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/discoveryengine.assist.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.serving.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `discoveryengine.sessions.listSessionFileMetadata`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## FileMetadata

The metadata of the file.

JSON representation  
---  
      
    
    {
      "fileId": string,
      "name": string,
      "mimeType": string,
      "byteSize": string,
      "tokenCount": string,
      "quotaPercentage": number,
      "selected": boolean,
      "usedInConversation": boolean,
      "originalUri": string,
      "originalSourceType": enum ([FileSource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.sessions/listSessionFileMetadata#FileSource)),
      "uploadTime": string,
      "metadata": {
        string: string,
        ...
      },
      "session": string
    }  
  
Fields  
---  
`fileId` |  `string` The ID of the file.  
`name` |  `string` The name of the file uploaded.  
`mimeType` |  `string` The content type of the file, see <https://www.iana.org/assignments/media-types/media-types.xhtml>.  
`byteSize` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The size of the context file in bytes.  
`tokenCount  
**(deprecated)**` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` This item is deprecated!Deprecated: This field will not be set for all file types, and will eventually be removed.The length of the file measured in tokens.  
`quotaPercentage  
**(deprecated)**` |  `number` This item is deprecated!Deprecated: This field will not be set for all file types, and will eventually be removed.The percentage of the quota used by the file.  
`selected` |  `boolean` If the file is selected to be used.  
`usedInConversation` |  `boolean` Whether the file was used in the session previously (i.e. was used in a query) and is part of the conversation history, or is only uploaded and not used yet.  
`originalUri` |  `string` Optional. The original location of the file. It may be a local file path, or any other URI that allows accessing the file in an external system. There are two scenarios in which this url may be empty: 1. If the file was sent as inline data (e.g. pasted from the clipboard). 2. If the original location is not available.Note that there's no guarantee that the URI will be pointing to a valid or actually existing file. For example, a file might have been uploaded to the session, and then deleted from the original source.  
`originalSourceType` |  `enum (`[FileSource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.sessions/listSessionFileMetadata#FileSource)`)` Optional. The type of the original source of the file.  
`uploadTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the file was uploaded (If this is a file generated by an internal process and then made available to the session, this indicates the moment it happened).Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`metadata` |  `map (key: string, value: string)` Optional. Represents metadata related to the file that can suit particular use cases. The prefix "google." is reserved for the key for use by Google, but other prefixes can be freely used.  
`session` |  `string` Output only. The resource name of the session. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/sessions/{session}`.  
  
## FileSource

Original source of the file.

Enums  
---  
`FILE_SOURCE_UNSPECIFIED` | Default value. Unknown source.  
`FILE_SOURCE_INLINE` | The data of the file was provided inline (e.g. pasted from the clipboard).  
`FILE_SOURCE_LOCAL` | The file was uploaded from a local file.  
`FILE_SOURCE_CLOUD_STORAGE` | The file was uploaded from Cloud Storage.  
`FILE_SOURCE_CLOUD_DRIVE` | The file was uploaded from Drive.  
`FILE_SOURCE_URL` | The file was retrieved from a URL (e.g. public web).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
