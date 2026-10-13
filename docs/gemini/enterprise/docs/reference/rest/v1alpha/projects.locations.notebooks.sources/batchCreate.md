---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.notebooks.sources/batchCreate/
title: Method: projects.locations.notebooks.sources.batchCreate \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:15:12.317090+00:00
---

# Method: projects.locations.notebooks.sources.batchCreate  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.notebooks.sources/batchCreate/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  Method: projects.locations.notebooks.sources.batchCreate Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * UserContent
    * JSON representation
  * GoogleDriveContent
    * JSON representation
  * TextContent
    * JSON representation
  * WebContent
    * JSON representation
  * VideoContent
    * JSON representation
  * AgentspaceContent
    * JSON representation



Creates a list of `[Source](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.notebooks.sources#Source)`s.

### HTTP request

Choose an endpoint:

globalus

  
`POST https://discoveryengine.googleapis.com/v1alpha/{parent=projects/*/locations/*/notebooks/*}/sources:batchCreate`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource where the sources will be created. Format: projects/{project}/locations/{location}/notebooks/{notebook}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "userContents": [
        {
          object ([UserContent](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.notebooks.sources/batchCreate#UserContent))
        }
      ]
    }  
  
Fields  
---  
`userContents[]` |  `object (`[UserContent](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.notebooks.sources/batchCreate#UserContent)`)` Required. The `[UserContent](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.notebooks.sources/batchCreate#UserContent)`s to be uploaded.  
  
### Response body

Response for `[SourceService.BatchCreateSources](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.notebooks.sources/batchCreate#google.cloud.notebooklm.v1alpha.SourceService.BatchCreateSources)` method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "sources": [
        {
          object ([Source](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.notebooks.sources#Source))
        }
      ]
    }  
  
Fields  
---  
`sources[]` |  `object (`[Source](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.notebooks.sources#Source)`)` The `[Source](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.notebooks.sources#Source)`s.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/discoveryengine.assist.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.serving.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `discoveryengine.sources.create`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## UserContent

The "Content" messages refer to data the user wants to upload.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "googleDriveContent": {
        object ([GoogleDriveContent](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.notebooks.sources/batchCreate#GoogleDriveContent))
      },
      "textContent": {
        object ([TextContent](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.notebooks.sources/batchCreate#TextContent))
      },
      "webContent": {
        object ([WebContent](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.notebooks.sources/batchCreate#WebContent))
      },
      "videoContent": {
        object ([VideoContent](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.notebooks.sources/batchCreate#VideoContent))
      },
      "agentspaceContent": {
        object ([AgentspaceContent](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.notebooks.sources/batchCreate#AgentspaceContent))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The user content. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`googleDriveContent` |  `object (`[GoogleDriveContent](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.notebooks.sources/batchCreate#GoogleDriveContent)`)` The content from Google Drive.  
`textContent` |  `object (`[TextContent](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.notebooks.sources/batchCreate#TextContent)`)` The text content uploaded as source.  
`webContent` |  `object (`[WebContent](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.notebooks.sources/batchCreate#WebContent)`)` The web content uploaded as source.  
`videoContent` |  `object (`[VideoContent](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.notebooks.sources/batchCreate#VideoContent)`)` The video content uploaded as source.  
`agentspaceContent` |  `object (`[AgentspaceContent](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.notebooks.sources/batchCreate#AgentspaceContent)`)` Agentspace content uploaded as source.  
End of mutually exclusive fields.  
  
## GoogleDriveContent

The content from Google Drive.

JSON representation  
---  
      
    
    {
      "documentId": string,
      "mimeType": string,
      "sourceName": string
    }  
  
Fields  
---  
`documentId` |  `string` The document ID of the selected document.  
`mimeType` |  `string` The mime type of the selected document.This can be used to differentiate type of content selected in the drive picker. Use application/vnd.google-apps.document for Google Docs or application/vnd.google-apps.presentation for Google Slides.  
`sourceName` |  `string` The name to be displayed for the source.  
  
## TextContent

The text content uploaded as source.

JSON representation  
---  
      
    
    {
      "sourceName": string,
      "content": string
    }  
  
Fields  
---  
`sourceName` |  `string` The display name of the text source.  
`content` |  `string` The name to be displayed for the source.  
  
## WebContent

The web content uploaded as source.

JSON representation  
---  
      
    
    {
      "url": string,
      "sourceName": string
    }  
  
Fields  
---  
`url` |  `string` If URL is supplied, will fetch the webpage in the backend.  
`sourceName` |  `string` The name to be displayed for the source.  
  
## VideoContent

Video content uploaded as source.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "youtubeUrl": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Specifies the format of the video content The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`youtubeUrl` |  `string` The youtube url of the video content.  
End of mutually exclusive fields.  
  
## AgentspaceContent

Agentspace content uploaded as source.

JSON representation  
---  
      
    
    {
      "documentName": string,
      "engineName": string,
      "ideaforgeIdeaName": string
    }  
  
Fields  
---  
`documentName` |  `string` Optional. The full resource name of the Agentspace document. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStore}/branches/{branch}/documents/{documentId}`.  
`engineName` |  `string` Optional. Engine to verify the permission of the document. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}`.  
`ideaforgeIdeaName` |  `string` Optional. Resource name of the idea forge instance. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/sessions/{session}/ideaForgeInstances/{instance}`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
