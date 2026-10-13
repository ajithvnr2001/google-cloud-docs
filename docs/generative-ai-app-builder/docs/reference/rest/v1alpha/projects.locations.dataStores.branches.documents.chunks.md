---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.dataStores.branches.documents.chunks
title: REST Resource: projects.locations.dataStores.branches.documents.chunks \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:14:59.824240+00:00
---

# REST Resource: projects.locations.dataStores.branches.documents.chunks  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.dataStores.branches.documents.chunks

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Reference ](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis)



Send feedback 

#  REST Resource: projects.locations.dataStores.branches.documents.chunks Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Chunk
    * JSON representation
  * Methods



## Resource: Chunk

Chunk captures all raw metadata information of items to be recommended or searched in the chunk mode.

JSON representation  
---  
      
    
    {
      "name": string,
      "id": string,
      "content": string,
      "documentMetadata": {
        object ([DocumentMetadata](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents.chunks#Chunk.DocumentMetadata))
      },
      "derivedStructData": {
        object
      },
      "pageSpan": {
        object ([PageSpan](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents.chunks#Chunk.PageSpan))
      },
      "chunkMetadata": {
        object ([ChunkMetadata](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents.chunks#Chunk.ChunkMetadata))
      },
      "dataUrls": [
        string
      ],
      "annotationContents": [
        string
      ],
      "annotationMetadata": [
        {
          object ([AnnotationMetadata](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents.chunks#Chunk.AnnotationMetadata))
        }
      ],
      "relevanceScore": number
    }  
  
Fields  
---  
`name` |  `string` The full resource name of the chunk. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStore}/branches/{branch}/documents/{documentId}/chunks/{chunk_id}`.This field must be a UTF-8 encoded string with a length limit of 1024 characters.  
`id` |  `string` Unique chunk ID of the current chunk.  
`content` |  `string` Content is a string from a document (parsed content).  
`documentMetadata` |  `object (`[DocumentMetadata](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents.chunks#Chunk.DocumentMetadata)`)` Metadata of the document from the current chunk.  
`derivedStructData` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Output only. This field is OUTPUT_ONLY. It contains derived data that are not in the original input document.  
`pageSpan` |  `object (`[PageSpan](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents.chunks#Chunk.PageSpan)`)` Page span of the chunk.  
`chunkMetadata` |  `object (`[ChunkMetadata](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents.chunks#Chunk.ChunkMetadata)`)` Output only. Metadata of the current chunk.  
`dataUrls[]` |  `string` Output only. Image Data URLs if the current chunk contains images. Data URLs are composed of four parts: a prefix (data:), a MIME type indicating the type of data, an optional base64 token if non-textual, and the data itself: data:[][;base64],  
`annotationContents[]` |  `string` Output only. Annotation contents if the current chunk contains annotations.  
`annotationMetadata[]` |  `object (`[AnnotationMetadata](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents.chunks#Chunk.AnnotationMetadata)`)` Output only. The annotation metadata includes structured content in the current chunk.  
`relevanceScore` |  `number` Output only. Represents the relevance score based on similarity. Higher score indicates higher chunk relevance. The score is in range [-1.0, 1.0]. Only populated on `[SearchResponse](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/SearchResponse)`.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.dataStores.branches.documents.chunks/get)`

|  Gets a `[Document](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents#Document)`.  
  
### `[list](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.dataStores.branches.documents.chunks/list)`

|  Gets a list of `[Chunk](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents.chunks#Chunk)`s.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
