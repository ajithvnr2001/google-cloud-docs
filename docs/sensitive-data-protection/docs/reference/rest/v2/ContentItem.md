---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem/
title: ContentItem \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:43.129741+00:00
---

# ContentItem  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  ContentItem Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Table
    * JSON representation
  * Row
    * JSON representation
  * Conversation
    * JSON representation
  * ConversationMessage
    * JSON representation
  * MessagePart
    * JSON representation
  * MessageType
  * BatchContentItem
    * JSON representation
  * StringValueBatch
    * JSON representation
  * ContentMetadata
    * JSON representation
  * KeyValueMetadataProperty
    * JSON representation
  * FileLabel
    * JSON representation
  * SensitivityLabelMetadata
    * JSON representation
  * GoogleDriveLabelMetadata
    * JSON representation
  * LabelFieldMetadata
    * JSON representation



Type of content to inspect.

JSON representation  
---  
      
    
    {
      "contentMetadata": {
        object ([ContentMetadata](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem#ContentMetadata))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "value": string,
      "table": {
        object ([Table](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem#Table))
      },
      "byteItem": {
        object ([ByteContentItem](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ByteContentItem))
      },
      "conversation": {
        object ([Conversation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem#Conversation))
      },
      "batchContentItem": {
        object ([BatchContentItem](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem#BatchContentItem))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`contentMetadata` |  `object (`[ContentMetadata](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem#ContentMetadata)`)` User provided metadata for the content.  
Data of the item either in the byte array or UTF-8 string form, or table. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`value` |  `string` String data to inspect or redact.  
`table` |  `object (`[Table](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem#Table)`)` Structured content for inspection. See <https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-text#inspecting_a_table> to learn more.  
`byteItem` |  `object (`[ByteContentItem](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ByteContentItem)`)` Content data to inspect or redact. Replaces `type` and `data`.  
`conversation` |  `object (`[Conversation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem#Conversation)`)` Represents a conversation (either complete or a slice). It is assumed that all included messages are contiguous and ordered in chronological order.  
`batchContentItem` |  `object (`[BatchContentItem](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem#BatchContentItem)`)` Represents a batch of items to inspect.  
End of mutually exclusive fields.  
  
## Table

Structured content to inspect. Up to 50,000 `Value`s per request allowed. See <https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-structured-text#inspecting_a_table> to learn more.

JSON representation  
---  
      
    
    {
      "headers": [
        {
          object ([FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/FieldId))
        }
      ],
      "rows": [
        {
          object ([Row](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem#Row))
        }
      ]
    }  
  
Fields  
---  
`headers[]` |  `object (`[FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/FieldId)`)` Headers of the table.  
`rows[]` |  `object (`[Row](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem#Row)`)` Rows of the table.  
  
## Row

Values of the row.

JSON representation  
---  
      
    
    {
      "values": [
        {
          object ([Value](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Value))
        }
      ]
    }  
  
Fields  
---  
`values[]` |  `object (`[Value](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Value)`)` Individual cells.  
  
## Conversation

Complete conversation or slice of a conversation. It is assumed that all included messages are contiguous and ordered in chronological order.

JSON representation  
---  
      
    
    {
      "messages": [
        {
          object ([ConversationMessage](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem#ConversationMessage))
        }
      ]
    }  
  
Fields  
---  
`messages[]` |  `object (`[ConversationMessage](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem#ConversationMessage)`)` Messages exchanged within this conversation. The maximum number of messages allowed is 50k. The order of the messages is assumed to be chronological and will be used to index findings in the response.  
  
## ConversationMessage

Single message in a conversation.

JSON representation  
---  
      
    
    {
      "content": string,
      "messageParts": [
        {
          object ([MessagePart](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem#MessagePart))
        }
      ],
      "messageType": enum ([MessageType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem#MessageType)),
      "participantId": string
    }  
  
Fields  
---  
`content  
**(deprecated)**` |  `string` This item is deprecated!Deprecated: Use `messageParts` instead. The contents of this message. Only one of `content` and `messageParts` can be set.  
`messageParts[]` |  `object (`[MessagePart](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem#MessagePart)`)` Optional. The parts of the message. Restricted to being at most a single text item. Only one of `content` and `messageParts` can be set.  
`messageType` |  `enum (`[MessageType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem#MessageType)`)` The type of message.  
`participantId` |  `string` Optional. The identifier of the participant, for example 'test-user' or 'gemini'. The participant ID can contain lowercase letters, numbers, and hyphens; that is, it must match the regular expression: `^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`. The maximum length is 63 characters.  
  
## MessagePart

A part of a conversation message.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "text": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The content of the message part. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`text` |  `string` String content for text-based messages.  
End of mutually exclusive fields.  
  
## MessageType

The type of message. New values can be added in the future.

Enums  
---  
`MESSAGE_TYPE_UNSPECIFIED` | Unused.  
`CONTENT` | Message contains content to be inspected.  
`CONTEXT` | Message contains context only and will not have findings reported from it during inspection or redacted from it during de-identification.  
  
## BatchContentItem

Represents a batch of content to inspect or redact.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "stringValueBatch": {
        object ([StringValueBatch](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem#StringValueBatch))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Represents the batch to inspect or redact. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`stringValueBatch` |  `object (`[StringValueBatch](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem#StringValueBatch)`)` Optional. Represents a batch of string values to inspect or redact.  
End of mutually exclusive fields.  
  
## StringValueBatch

Represents a batch of string values to inspect or redact.

JSON representation  
---  
      
    
    {
      "values": [
        string
      ]
    }  
  
Fields  
---  
`values[]` |  `string` Optional. Represents string data to inspect or redact.  
  
## ContentMetadata

Metadata on content to be scanned.

JSON representation  
---  
      
    
    {
      "properties": [
        {
          object ([KeyValueMetadataProperty](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem#KeyValueMetadataProperty))
        }
      ],
      "fileLabels": [
        {
          object ([FileLabel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem#FileLabel))
        }
      ]
    }  
  
Fields  
---  
`properties[]` |  `object (`[KeyValueMetadataProperty](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem#KeyValueMetadataProperty)`)` User provided key-value pairs of content metadata.  
`fileLabels[]` |  `object (`[FileLabel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem#FileLabel)`)` Optional. The file labels associated with the content.  
  
## KeyValueMetadataProperty

A key-value pair in the Metadata.

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string` The key of the property.  
`value` |  `string` The value of the property.  
  
## FileLabel

Represents a file label.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "sensitivityLabel": {
        object ([SensitivityLabelMetadata](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem#SensitivityLabelMetadata))
      },
      "googleDriveLabel": {
        object ([GoogleDriveLabelMetadata](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem#GoogleDriveLabelMetadata))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The type of file label. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`sensitivityLabel` |  `object (`[SensitivityLabelMetadata](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem#SensitivityLabelMetadata)`)` Sensitivity labels published by Microsoft.  
`googleDriveLabel` |  `object (`[GoogleDriveLabelMetadata](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem#GoogleDriveLabelMetadata)`)` Google Drive labels published by Google.  
End of mutually exclusive fields.  
  
## SensitivityLabelMetadata

Sensitivity labels published by Microsoft.

JSON representation  
---  
      
    
    {
      "guid": string
    }  
  
Fields  
---  
`guid` |  `string` Required. The GUID of the sensitivity label.  
  
## GoogleDriveLabelMetadata

Google Drive labels published by Google.

JSON representation  
---  
      
    
    {
      "labelId": string,
      "labelFields": [
        {
          object ([LabelFieldMetadata](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem#LabelFieldMetadata))
        }
      ]
    }  
  
Fields  
---  
`labelId` |  `string` The [label ID](https://developers.google.com/workspace/drive/labels/guides/overview) of the Google Drive label.  
`labelFields[]` |  `object (`[LabelFieldMetadata](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem#LabelFieldMetadata)`)` The field values of the Google Drive label  
  
## LabelFieldMetadata

The field values of the Google Drive label

JSON representation  
---  
      
    
    {
      "id": string,
      "value": {
        object ([Value](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Value))
      }
    }  
  
Fields  
---  
`id` |  `string` The identifier of the Label Field.  
`value` |  `object (`[Value](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Value)`)` The value of the Label Field.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-05 UTC."],[],[]] 
