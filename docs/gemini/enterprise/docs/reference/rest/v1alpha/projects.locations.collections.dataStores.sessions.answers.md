---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers
title: REST Resource: projects.locations.collections.dataStores.sessions.answers \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:48:07.759211+00:00
---

# REST Resource: projects.locations.collections.dataStores.sessions.answers  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  REST Resource: projects.locations.collections.dataStores.sessions.answers Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Answer
    * JSON representation
    * State
    * Citation
      * JSON representation
    * CitationSource
      * JSON representation
    * GroundingSupport
      * JSON representation
    * Reference
      * JSON representation
    * UnstructuredDocumentInfo
      * JSON representation
    * ChunkContent
      * JSON representation
    * ChunkInfo
      * JSON representation
    * DocumentMetadata
      * JSON representation
    * StructuredDocumentInfo
      * JSON representation
    * BlobAttachment
      * JSON representation
    * Blob
      * JSON representation
    * AttributionType
    * Step
      * JSON representation
    * State
    * Action
      * JSON representation
    * SearchAction
      * JSON representation
    * Observation
      * JSON representation
    * SearchResult
      * JSON representation
    * SnippetInfo
      * JSON representation
    * ChunkInfo
      * JSON representation
    * QueryUnderstandingInfo
      * JSON representation
    * QueryClassificationInfo
      * JSON representation
    * Type
    * AnswerSkippedReason
    * SafetyRating
      * JSON representation
    * HarmCategory
    * HarmProbability
    * HarmSeverity
  * Methods



## Resource: Answer

Defines an answer.

JSON representation  
---  
      
    
    {
      "name": string,
      "state": enum ([State](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.State)),
      "answerText": string,
      "citations": [
        {
          object ([Citation](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.Citation))
        }
      ],
      "groundingSupports": [
        {
          object ([GroundingSupport](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.GroundingSupport))
        }
      ],
      "references": [
        {
          object ([Reference](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.Reference))
        }
      ],
      "blobAttachments": [
        {
          object ([BlobAttachment](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.BlobAttachment))
        }
      ],
      "relatedQuestions": [
        string
      ],
      "steps": [
        {
          object ([Step](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.Step))
        }
      ],
      "queryUnderstandingInfo": {
        object ([QueryUnderstandingInfo](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.QueryUnderstandingInfo))
      },
      "answerSkippedReasons": [
        enum ([AnswerSkippedReason](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.AnswerSkippedReason))
      ],
      "createTime": string,
      "completeTime": string,
      "safetyRatings": [
        {
          object ([SafetyRating](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.SafetyRating))
        }
      ],
      "groundingScore": number
    }  
  
Fields  
---  
`name` |  `string` Immutable. Fully qualified name `projects/{project}/locations/global/collections/{collection}/engines/{engine}/sessions/*/answers/*`  
`state` |  `enum (`[State](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.State)`)` The State of the answer generation.  
`answerText` |  `string` The textual answer.  
`citations[]` |  `object (`[Citation](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.Citation)`)` Citations.  
`groundingSupports[]` |  `object (`[GroundingSupport](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.GroundingSupport)`)` Optional. Grounding supports.  
`references[]` |  `object (`[Reference](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.Reference)`)` References.  
`blobAttachments[]` |  `object (`[BlobAttachment](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.BlobAttachment)`)` Output only. List of blob attachments in the answer.  
`relatedQuestions[]` |  `string` Suggested related questions.  
`steps[]` |  `object (`[Step](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.Step)`)` Answer generation steps.  
`queryUnderstandingInfo` |  `object (`[QueryUnderstandingInfo](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.QueryUnderstandingInfo)`)` Query understanding information.  
`answerSkippedReasons[]` |  `enum (`[AnswerSkippedReason](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.AnswerSkippedReason)`)` Additional answer-skipped reasons. This provides the reason for ignored cases. If nothing is skipped, this field is not set.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Answer creation timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`completeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Answer completed timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`safetyRatings[]` |  `object (`[SafetyRating](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.SafetyRating)`)` Optional. Safety ratings.  
`groundingScore` |  `number` A score in the range of [0, 1] describing how grounded the answer is by the reference chunks.  
  
### State

Enumeration of the State of the answer generation.

Enums  
---  
`STATE_UNSPECIFIED` | Unknown.  
`IN_PROGRESS` | Answer generation is currently in progress.  
`FAILED` | Answer generation currently failed.  
`SUCCEEDED` | Answer generation has succeeded.  
`STREAMING` | Answer generation is currently in progress.  
  
### Citation

Citation info for a segment.

JSON representation  
---  
      
    
    {
      "startIndex": string,
      "endIndex": string,
      "sources": [
        {
          object ([CitationSource](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.CitationSource))
        }
      ]
    }  
  
Fields  
---  
`startIndex` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Index indicates the start of the segment, measured in bytes (UTF-8 unicode). If there are multi-byte characters,such as non-ASCII characters, the index measurement is longer than the string length.  
`endIndex` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` End of the attributed segment, exclusive. Measured in bytes (UTF-8 unicode). If there are multi-byte characters,such as non-ASCII characters, the index measurement is longer than the string length.  
`sources[]` |  `object (`[CitationSource](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.CitationSource)`)` Citation sources for the attributed segment.  
  
### CitationSource

Citation source.

JSON representation  
---  
      
    
    {
      "referenceId": string
    }  
  
Fields  
---  
`referenceId` |  `string` ID of the citation source.  
  
### GroundingSupport

Grounding support for a claim in `answerText`.

JSON representation  
---  
      
    
    {
      "startIndex": string,
      "endIndex": string,
      "sources": [
        {
          object ([CitationSource](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.CitationSource))
        }
      ],
      "groundingScore": number,
      "groundingCheckRequired": boolean
    }  
  
Fields  
---  
`startIndex` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. Index indicates the start of the claim, measured in bytes (UTF-8 unicode).  
`endIndex` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. End of the claim, exclusive.  
`sources[]` |  `object (`[CitationSource](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.CitationSource)`)` Optional. Citation sources for the claim.  
`groundingScore` |  `number` A score in the range of [0, 1] describing how grounded is a specific claim by the references. Higher value means that the claim is better supported by the reference chunks.  
`groundingCheckRequired` |  `boolean` Indicates that this claim required grounding check. When the system decided this claim didn't require attribution/grounding check, this field is set to false. In that case, no grounding check was done for the claim and therefore `groundingScore`, `sources` is not returned.  
  
### Reference

Reference.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "unstructuredDocumentInfo": {
        object ([UnstructuredDocumentInfo](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.UnstructuredDocumentInfo))
      },
      "chunkInfo": {
        object ([ChunkInfo](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.ChunkInfo))
      },
      "structuredDocumentInfo": {
        object ([StructuredDocumentInfo](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.StructuredDocumentInfo))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Search result content. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`unstructuredDocumentInfo` |  `object (`[UnstructuredDocumentInfo](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.UnstructuredDocumentInfo)`)` Unstructured document information.  
`chunkInfo` |  `object (`[ChunkInfo](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.ChunkInfo)`)` Chunk information.  
`structuredDocumentInfo` |  `object (`[StructuredDocumentInfo](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.StructuredDocumentInfo)`)` Structured document information.  
End of mutually exclusive fields.  
  
### UnstructuredDocumentInfo

Unstructured document information.

JSON representation  
---  
      
    
    {
      "document": string,
      "uri": string,
      "title": string,
      "chunkContents": [
        {
          object ([ChunkContent](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.ChunkContent))
        }
      ],
      "structData": {
        object
      }
    }  
  
Fields  
---  
`document` |  `string` Document resource name.  
`uri` |  `string` URI for the document.  
`title` |  `string` Title.  
`chunkContents[]` |  `object (`[ChunkContent](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.ChunkContent)`)` List of cited chunk contents derived from document content.  
`structData` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` The structured JSON metadata for the document. It is populated from the struct data from the Chunk in search result.  
  
### ChunkContent

Chunk content.

JSON representation  
---  
      
    
    {
      "content": string,
      "pageIdentifier": string,
      "blobAttachmentIndexes": [
        string
      ],
      "relevanceScore": number
    }  
  
Fields  
---  
`content` |  `string` Chunk textual content.  
`pageIdentifier` |  `string` Page identifier.  
`blobAttachmentIndexes[]` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Stores indexes of blobattachments linked to this chunk.  
`relevanceScore` |  `number` The relevance of the chunk for a given query. Values range from 0.0 (completely irrelevant) to 1.0 (completely relevant). This value is for informational purpose only. It may change for the same query and chunk at any time due to a model retraining or change in implementation.  
  
### ChunkInfo

Chunk information.

JSON representation  
---  
      
    
    {
      "chunk": string,
      "content": string,
      "documentMetadata": {
        object ([DocumentMetadata](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.DocumentMetadata))
      },
      "blobAttachmentIndexes": [
        string
      ],
      "relevanceScore": number
    }  
  
Fields  
---  
`chunk` |  `string` Chunk resource name.  
`content` |  `string` Chunk textual content.  
`documentMetadata` |  `object (`[DocumentMetadata](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.DocumentMetadata)`)` Document metadata.  
`blobAttachmentIndexes[]` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Stores indexes of blobattachments linked to this chunk.  
`relevanceScore` |  `number` The relevance of the chunk for a given query. Values range from 0.0 (completely irrelevant) to 1.0 (completely relevant). This value is for informational purpose only. It may change for the same query and chunk at any time due to a model retraining or change in implementation.  
  
### DocumentMetadata

Document metadata.

JSON representation  
---  
      
    
    {
      "document": string,
      "uri": string,
      "title": string,
      "pageIdentifier": string,
      "structData": {
        object
      }
    }  
  
Fields  
---  
`document` |  `string` Document resource name.  
`uri` |  `string` URI for the document.  
`title` |  `string` Title.  
`pageIdentifier` |  `string` Page identifier.  
`structData` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` The structured JSON metadata for the document. It is populated from the struct data from the Chunk in search result.  
  
### StructuredDocumentInfo

Structured search information.

JSON representation  
---  
      
    
    {
      "document": string,
      "structData": {
        object
      },
      "title": string,
      "uri": string
    }  
  
Fields  
---  
`document` |  `string` Document resource name.  
`structData` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Structured search data.  
`title` |  `string` Output only. The title of the document.  
`uri` |  `string` Output only. The URI of the document.  
  
### BlobAttachment

Stores binarydata attached to text answer, e.g. image, video, audio, etc.

JSON representation  
---  
      
    
    {
      "data": {
        object ([Blob](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.Blob))
      },
      "attributionType": enum ([AttributionType](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.AttributionType))
    }  
  
Fields  
---  
`data` |  `object (`[Blob](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.Blob)`)` Output only. The mime type and data of the blob.  
`attributionType` |  `enum (`[AttributionType](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.AttributionType)`)` Output only. The attribution type of the blob.  
  
### Blob

The media type and data of the blob.

JSON representation  
---  
      
    
    {
      "mimeType": string,
      "data": string
    }  
  
Fields  
---  
`mimeType` |  `string` Output only. The media type (MIME type) of the generated or retrieved data.  
`data` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Output only. Raw bytes.A base64-encoded string.  
  
### AttributionType

The source of the blob.

Enums  
---  
`ATTRIBUTION_TYPE_UNSPECIFIED` | Unspecified attribution type.  
`CORPUS` | The attachment data is from the corpus.  
`GENERATED` | The attachment data is generated by the model through code generation.  
  
### Step

Step information.

JSON representation  
---  
      
    
    {
      "state": enum ([State](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.State_1)),
      "description": string,
      "thought": string,
      "actions": [
        {
          object ([Action](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.Action))
        }
      ]
    }  
  
Fields  
---  
`state` |  `enum (`[State](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.State_1)`)` The state of the step.  
`description` |  `string` The description of the step.  
`thought` |  `string` The thought of the step.  
`actions[]` |  `object (`[Action](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.Action)`)` Actions.  
  
### State

Enumeration of the state of the step.

Enums  
---  
`STATE_UNSPECIFIED` | Unknown.  
`IN_PROGRESS` | Step is currently in progress.  
`FAILED` | Step currently failed.  
`SUCCEEDED` | Step has succeeded.  
  
### Action

Action.

JSON representation  
---  
      
    
    {
      "observation": {
        object ([Observation](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.Observation))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "searchAction": {
        object ([SearchAction](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.SearchAction))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`observation` |  `object (`[Observation](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.Observation)`)` Observation.  
The action. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`searchAction` |  `object (`[SearchAction](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.SearchAction)`)` Search action.  
End of mutually exclusive fields.  
  
### SearchAction

Search action.

JSON representation  
---  
      
    
    {
      "query": string
    }  
  
Fields  
---  
`query` |  `string` The query to search.  
  
### Observation

Observation.

JSON representation  
---  
      
    
    {
      "searchResults": [
        {
          object ([SearchResult](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.SearchResult))
        }
      ]
    }  
  
Fields  
---  
`searchResults[]` |  `object (`[SearchResult](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.SearchResult)`)` Search results observed by the search action, it can be snippets info or chunk info, depending on the citation type set by the user.  
  
### SearchResult

JSON representation  
---  
      
    
    {
      "document": string,
      "uri": string,
      "title": string,
      "snippetInfo": [
        {
          object ([SnippetInfo](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.SnippetInfo))
        }
      ],
      "chunkInfo": [
        {
          object ([ChunkInfo](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.ChunkInfo_1))
        }
      ],
      "structData": {
        object
      }
    }  
  
Fields  
---  
`document` |  `string` Document resource name.  
`uri` |  `string` URI for the document.  
`title` |  `string` Title.  
`snippetInfo[]` |  `object (`[SnippetInfo](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.SnippetInfo)`)` If citation_type is DOCUMENT_LEVEL_CITATION, populate document level snippets.  
`chunkInfo[]` |  `object (`[ChunkInfo](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.ChunkInfo_1)`)` If citation_type is CHUNK_LEVEL_CITATION and chunk mode is on, populate chunk info.  
`structData` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Data representation. The structured JSON data for the document. It's populated from the struct data from the Document, or the Chunk in search result.  
  
### SnippetInfo

Snippet information.

JSON representation  
---  
      
    
    {
      "snippet": string,
      "snippetStatus": string
    }  
  
Fields  
---  
`snippet` |  `string` Snippet content.  
`snippetStatus` |  `string` Status of the snippet defined by the search team.  
  
### ChunkInfo

Chunk information.

JSON representation  
---  
      
    
    {
      "chunk": string,
      "content": string,
      "relevanceScore": number
    }  
  
Fields  
---  
`chunk` |  `string` Chunk resource name.  
`content` |  `string` Chunk textual content.  
`relevanceScore` |  `number` The relevance of the chunk for a given query. Values range from 0.0 (completely irrelevant) to 1.0 (completely relevant). This value is for informational purpose only. It may change for the same query and chunk at any time due to a model retraining or change in implementation.  
  
### QueryUnderstandingInfo

Query understanding information.

JSON representation  
---  
      
    
    {
      "queryClassificationInfo": [
        {
          object ([QueryClassificationInfo](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.QueryClassificationInfo))
        }
      ]
    }  
  
Fields  
---  
`queryClassificationInfo[]` |  `object (`[QueryClassificationInfo](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.QueryClassificationInfo)`)` Query classification information.  
  
### QueryClassificationInfo

Query classification information.

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.Type)),
      "positive": boolean
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.Type)`)` Query classification type.  
`positive` |  `boolean` Classification output.  
  
### Type

Query classification types.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified query classification type.  
`ADVERSARIAL_QUERY` | Adversarial query classification type.  
`NON_ANSWER_SEEKING_QUERY` | Non-answer-seeking query classification type, for chit chat.  
`JAIL_BREAKING_QUERY` | Jail-breaking query classification type.  
`NON_ANSWER_SEEKING_QUERY_V2` | Non-answer-seeking query classification type, for no clear intent.  
`USER_DEFINED_CLASSIFICATION_QUERY` | User defined query classification type.  
  
### AnswerSkippedReason

An enum for answer skipped reasons.

Enums  
---  
`ANSWER_SKIPPED_REASON_UNSPECIFIED` | Default value. The answer skipped reason is not specified.  
`ADVERSARIAL_QUERY_IGNORED` | The adversarial query ignored case.  
`NON_ANSWER_SEEKING_QUERY_IGNORED` | The non-answer seeking query ignored caseGoogle skips the answer if the query is chit chat.  
`OUT_OF_DOMAIN_QUERY_IGNORED` | The out-of-domain query ignored case.Google skips the answer if there are no high-relevance search results.  
`POTENTIAL_POLICY_VIOLATION` | The potential policy violation case.Google skips the answer if there is a potential policy violation detected. This includes content that may be violent or toxic.  
`NO_RELEVANT_CONTENT` | The no relevant content case.Google skips the answer if there is no relevant content in the retrieved search results.  
`JAIL_BREAKING_QUERY_IGNORED` | The jail-breaking query ignored case.For example, "Reply in the tone of a competing company's CEO". Google skips the answer if the query is classified as a jail-breaking query.  
`CUSTOMER_POLICY_VIOLATION` | The customer policy violation case.Google skips the summary if there is a customer policy violation detected. The policy is defined by the customer.  
`NON_ANSWER_SEEKING_QUERY_IGNORED_V2` | The non-answer seeking query ignored case.Google skips the answer if the query doesn't have clear intent.  
`LOW_GROUNDED_ANSWER` | The low-grounded answer case.Google skips the answer if a well grounded answer was unable to be generated.  
`USER_DEFINED_CLASSIFICATION_QUERY_IGNORED` | The user defined query classification ignored case.Google skips the answer if the query is classified as a user defined query classification.  
`UNHELPFUL_ANSWER` | The unhelpful answer case.Google skips the answer if the answer is not helpful. This can be due to a variety of factors, including but not limited to: the query is not answerable, the answer is not relevant to the query, or the answer is not well-formatted.  
  
### SafetyRating

Safety rating corresponding to the generated content.

JSON representation  
---  
      
    
    {
      "category": enum ([HarmCategory](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.HarmCategory)),
      "probability": enum ([HarmProbability](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.HarmProbability)),
      "probabilityScore": number,
      "severity": enum ([HarmSeverity](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.HarmSeverity)),
      "severityScore": number,
      "blocked": boolean
    }  
  
Fields  
---  
`category` |  `enum (`[HarmCategory](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.HarmCategory)`)` Output only. Harm category.  
`probability` |  `enum (`[HarmProbability](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.HarmProbability)`)` Output only. Harm probability levels in the content.  
`probabilityScore` |  `number` Output only. Harm probability score.  
`severity` |  `enum (`[HarmSeverity](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers#Answer.HarmSeverity)`)` Output only. Harm severity levels in the content.  
`severityScore` |  `number` Output only. Harm severity score.  
`blocked` |  `boolean` Output only. Indicates whether the content was filtered out because of this rating.  
  
### HarmCategory

Harm categories that will block the content.

Enums  
---  
`HARM_CATEGORY_UNSPECIFIED` | The harm category is unspecified.  
`HARM_CATEGORY_HATE_SPEECH` | The harm category is hate speech.  
`HARM_CATEGORY_DANGEROUS_CONTENT` | The harm category is dangerous content.  
`HARM_CATEGORY_HARASSMENT` | The harm category is harassment.  
`HARM_CATEGORY_SEXUALLY_EXPLICIT` | The harm category is sexually explicit content.  
`HARM_CATEGORY_CIVIC_INTEGRITY` | The harm category is civic integrity.  
  
### HarmProbability

Harm probability levels in the content.

Enums  
---  
`HARM_PROBABILITY_UNSPECIFIED` | Harm probability unspecified.  
`NEGLIGIBLE` | Negligible level of harm.  
`LOW` | Low level of harm.  
`MEDIUM` | Medium level of harm.  
`HIGH` | High level of harm.  
  
### HarmSeverity

Harm severity levels.

Enums  
---  
`HARM_SEVERITY_UNSPECIFIED` | Harm severity unspecified.  
`HARM_SEVERITY_NEGLIGIBLE` | Negligible level of harm severity.  
`HARM_SEVERITY_LOW` | Low level of harm severity.  
`HARM_SEVERITY_MEDIUM` | Medium level of harm severity.  
`HARM_SEVERITY_HIGH` | High level of harm severity.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.sessions.answers/get)`

|  Gets a Answer.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-03 UTC."],[],[]] 
