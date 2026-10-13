---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations
title: REST Resource: projects.locations.collections.dataStores.conversations \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:56:15.794644+00:00
---

# REST Resource: projects.locations.collections.dataStores.conversations  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  REST Resource: projects.locations.collections.dataStores.conversations Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Conversation
    * JSON representation
    * State
    * ConversationMessage
      * JSON representation
    * TextInput
      * JSON representation
    * ConversationContext
      * JSON representation
    * Reply
      * JSON representation
    * Reference
      * JSON representation
    * Summary
      * JSON representation
    * SummarySkippedReason
    * SafetyAttributes
      * JSON representation
    * SummaryWithMetadata
      * JSON representation
    * CitationMetadata
      * JSON representation
    * Citation
      * JSON representation
    * CitationSource
      * JSON representation
    * Reference
      * JSON representation
    * ChunkContent
      * JSON representation
    * BlobAttachment
      * JSON representation
    * Blob
      * JSON representation
    * AttributionType
  * Methods



## Resource: Conversation

External conversation proto definition.

JSON representation  
---  
      
    
    {
      "name": string,
      "state": enum ([State](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.State)),
      "userPseudoId": string,
      "messages": [
        {
          object ([ConversationMessage](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.ConversationMessage))
        }
      ],
      "startTime": string,
      "endTime": string
    }  
  
Fields  
---  
`name` |  `string` Immutable. Fully qualified name `projects/{project}/locations/global/collections/{collection}/dataStore/*/conversations/*` or `projects/{project}/locations/global/collections/{collection}/engines/*/conversations/*`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.State)`)` The state of the Conversation.  
`userPseudoId` |  `string` A unique identifier for tracking users.  
`messages[]` |  `object (`[ConversationMessage](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.ConversationMessage)`)` Conversation messages.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the conversation started.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the conversation finished.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### State

Enumeration of the state of the conversation.

Enums  
---  
`STATE_UNSPECIFIED` | Unknown.  
`IN_PROGRESS` | Conversation is currently open.  
`COMPLETED` | Conversation has been completed.  
  
### ConversationMessage

Defines a conversation message.

JSON representation  
---  
      
    
    {
      "createTime": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "userInput": {
        object ([TextInput](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.TextInput))
      },
      "reply": {
        object ([Reply](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.Reply))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Message creation timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`userInput` |  `object (`[TextInput](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.TextInput)`)` User text input.  
`reply` |  `object (`[Reply](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.Reply)`)` Search reply.  
End of mutually exclusive fields.  
  
### TextInput

Defines text input.

JSON representation  
---  
      
    
    {
      "input": string,
      "context": {
        object ([ConversationContext](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.ConversationContext))
      }
    }  
  
Fields  
---  
`input` |  `string` Text input.  
`context` |  `object (`[ConversationContext](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.ConversationContext)`)` Conversation context of the input.  
  
### ConversationContext

Defines context of the conversation

JSON representation  
---  
      
    
    {
      "contextDocuments": [
        string
      ],
      "activeDocument": string
    }  
  
Fields  
---  
`contextDocuments[]` |  `string` The current list of documents the user is seeing. It contains the document resource references.  
`activeDocument` |  `string` The current active document the user opened. It contains the document resource reference.  
  
### Reply

Defines a reply message to user.

JSON representation  
---  
      
    
    {
      "reply": string,
      "references": [
        {
          object ([Reference](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.Reference))
        }
      ],
      "summary": {
        object ([Summary](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.Summary))
      }
    }  
  
Fields  
---  
`reply  
**(deprecated)**` |  `string` This item is deprecated!DEPRECATED: use `summary` instead. Text reply.  
`references[]  
**(deprecated)**` |  `object (`[Reference](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.Reference)`)` This item is deprecated!References in the reply.  
`summary` |  `object (`[Summary](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.Summary)`)` Summary based on search results.  
  
### Reference

This item is deprecated!

Defines reference in reply.

JSON representation  
---  
      
    
    {
      "uri": string,
      "anchorText": string,
      "start": integer,
      "end": integer
    }  
  
Fields  
---  
`uri` |  `string` URI link reference.  
`anchorText` |  `string` Anchor text.  
`start` |  `integer` Anchor text start index.  
`end` |  `integer` Anchor text end index.  
  
### Summary

Summary of the top N search results specified by the summary spec.

JSON representation  
---  
      
    
    {
      "summaryText": string,
      "summarySkippedReasons": [
        enum ([SummarySkippedReason](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.SummarySkippedReason))
      ],
      "safetyAttributes": {
        object ([SafetyAttributes](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.SafetyAttributes))
      },
      "summaryWithMetadata": {
        object ([SummaryWithMetadata](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.SummaryWithMetadata))
      }
    }  
  
Fields  
---  
`summaryText` |  `string` The summary content.  
`summarySkippedReasons[]` |  `enum (`[SummarySkippedReason](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.SummarySkippedReason)`)` Additional summary-skipped reasons. This provides the reason for ignored cases. If nothing is skipped, this field is not set.  
`safetyAttributes` |  `object (`[SafetyAttributes](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.SafetyAttributes)`)` A collection of Safety Attribute categories and their associated confidence scores.  
`summaryWithMetadata` |  `object (`[SummaryWithMetadata](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.SummaryWithMetadata)`)` Summary with metadata information.  
  
### SummarySkippedReason

An Enum for summary-skipped reasons.

Enums  
---  
`SUMMARY_SKIPPED_REASON_UNSPECIFIED` | Default value. The summary skipped reason is not specified.  
`ADVERSARIAL_QUERY_IGNORED` | The adversarial query ignored case.Only used when `[SummarySpec.ignore_adversarial_query](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/ContentSearchSpec#SummarySpec.FIELDS.ignore_adversarial_query)` is set to `true`.  
`NON_SUMMARY_SEEKING_QUERY_IGNORED` | The non-summary seeking query ignored case.Google skips the summary if the query is chit chat. Only used when `[SummarySpec.ignore_non_summary_seeking_query](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/ContentSearchSpec#SummarySpec.FIELDS.ignore_non_summary_seeking_query)` is set to `true`.  
`OUT_OF_DOMAIN_QUERY_IGNORED` | The out-of-domain query ignored case.Google skips the summary if there are no high-relevance search results. For example, the data store contains facts about company A but the user query is asking questions about company B.  
`POTENTIAL_POLICY_VIOLATION` | The potential policy violation case.Google skips the summary if there is a potential policy violation detected. This includes content that may be violent or toxic.  
`LLM_ADDON_NOT_ENABLED` | The LLM addon not enabled case.Google skips the summary if the LLM addon is not enabled.  
`NO_RELEVANT_CONTENT` | The no relevant content case.Google skips the summary if there is no relevant content in the retrieved search results.  
`JAIL_BREAKING_QUERY_IGNORED` | The jail-breaking query ignored case.For example, "Reply in the tone of a competing company's CEO". Only used when [SearchRequest.ContentSearchSpec.SummarySpec.ignore_jail_breaking_query] is set to `true`.  
`CUSTOMER_POLICY_VIOLATION` | The customer policy violation case.Google skips the summary if there is a customer policy violation detected. The policy is defined by the customer.  
`NON_SUMMARY_SEEKING_QUERY_IGNORED_V2` | The non-answer seeking query ignored case.Google skips the summary if the query doesn't have clear intent. Only used when [SearchRequest.ContentSearchSpec.SummarySpec.ignore_non_answer_seeking_query] is set to `true`.  
`TIME_OUT` | The time out case.Google skips the summary if the time out.  
  
### SafetyAttributes

Safety Attribute categories and their associated confidence scores.

JSON representation  
---  
      
    
    {
      "categories": [
        string
      ],
      "scores": [
        number
      ]
    }  
  
Fields  
---  
`categories[]` |  `string` The display names of Safety Attribute categories associated with the generated content. Order matches the Scores.  
`scores[]` |  `number` The confidence scores of the each category, higher value means higher confidence. Order matches the Categories.  
  
### SummaryWithMetadata

Summary with metadata information.

JSON representation  
---  
      
    
    {
      "summary": string,
      "citationMetadata": {
        object ([CitationMetadata](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.CitationMetadata))
      },
      "references": [
        {
          object ([Reference](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.Reference_1))
        }
      ],
      "blobAttachments": [
        {
          object ([BlobAttachment](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.BlobAttachment))
        }
      ]
    }  
  
Fields  
---  
`summary` |  `string` Summary text with no citation information.  
`citationMetadata` |  `object (`[CitationMetadata](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.CitationMetadata)`)` Citation metadata for given summary.  
`references[]` |  `object (`[Reference](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.Reference_1)`)` Document References.  
`blobAttachments[]` |  `object (`[BlobAttachment](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.BlobAttachment)`)` Output only. Store multimodal data for answer enhancement.  
  
### CitationMetadata

Citation metadata.

JSON representation  
---  
      
    
    {
      "citations": [
        {
          object ([Citation](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.Citation))
        }
      ]
    }  
  
Fields  
---  
`citations[]` |  `object (`[Citation](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.Citation)`)` Citations for segments.  
  
### Citation

Citation info for a segment.

JSON representation  
---  
      
    
    {
      "startIndex": string,
      "endIndex": string,
      "sources": [
        {
          object ([CitationSource](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.CitationSource))
        }
      ]
    }  
  
Fields  
---  
`startIndex` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Index indicates the start of the segment, measured in bytes/unicode.  
`endIndex` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` End of the attributed segment, exclusive.  
`sources[]` |  `object (`[CitationSource](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.CitationSource)`)` Citation sources for the attributed segment.  
  
### CitationSource

Citation source.

JSON representation  
---  
      
    
    {
      "referenceIndex": string
    }  
  
Fields  
---  
`referenceIndex` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Document reference index from SummaryWithMetadata.references. It is 0-indexed and the value will be zero if the referenceIndex is not set explicitly.  
  
### Reference

Document reference.

JSON representation  
---  
      
    
    {
      "title": string,
      "document": string,
      "uri": string,
      "chunkContents": [
        {
          object ([ChunkContent](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.ChunkContent))
        }
      ]
    }  
  
Fields  
---  
`title` |  `string` Title of the document.  
`document` |  `string` Required. `[Document.name](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.branches.documents#Document.FIELDS.name)` of the document. Full resource name of the referenced document, in the format `projects/*/locations/*/collections/*/dataStores/*/branches/*/documents/*`.  
`uri` |  `string` Cloud Storage or HTTP uri for the document.  
`chunkContents[]` |  `object (`[ChunkContent](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.ChunkContent)`)` List of cited chunk contents derived from document content.  
  
### ChunkContent

Chunk content.

JSON representation  
---  
      
    
    {
      "content": string,
      "pageIdentifier": string,
      "blobAttachmentIndexes": [
        string
      ]
    }  
  
Fields  
---  
`content` |  `string` Chunk textual content.  
`pageIdentifier` |  `string` Page identifier.  
`blobAttachmentIndexes[]` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Stores indexes of blobattachments linked to this chunk.  
  
### BlobAttachment

Stores binarydata attached to text answer, e.g. image, video, audio, etc.

JSON representation  
---  
      
    
    {
      "data": {
        object ([Blob](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.Blob))
      },
      "attributionType": enum ([AttributionType](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.AttributionType))
    }  
  
Fields  
---  
`data` |  `object (`[Blob](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.Blob)`)` Output only. The blob data.  
`attributionType` |  `enum (`[AttributionType](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.AttributionType)`)` Output only. The attribution type of the blob.  
  
### Blob

Stores type and data of the blob.

JSON representation  
---  
      
    
    {
      "mimeType": string,
      "data": string
    }  
  
Fields  
---  
`mimeType` |  `string` Output only. The media type (MIME type) of the generated data.  
`data` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Output only. Raw bytes.A base64-encoded string.  
  
### AttributionType

Defines the attribution type of the blob.

Enums  
---  
`ATTRIBUTION_TYPE_UNSPECIFIED` | Unspecified attribution type.  
`CORPUS` | The attachment data is from the corpus.  
`GENERATED` | The attachment data is generated by the model through code generation.  
  
## Methods  
  
---  
  
### `[converse](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations/converse)`

|  Converses a conversation.  
  
### `[create](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations/create)`

|  Creates a Conversation.  
  
### `[delete](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations/delete)`

|  Deletes a Conversation.  
  
### `[get](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations/get)`

|  Gets a Conversation.  
  
### `[list](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations/list)`

|  Lists all Conversations by their parent `[DataStore](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores#DataStore)`.  
  
### `[patch](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations/patch)`

|  Updates a Conversation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-03 UTC."],[],[]] 
