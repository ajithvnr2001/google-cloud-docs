---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult/
title: InspectResult \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:46.819874+00:00
---

# InspectResult  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  InspectResult Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Finding
    * JSON representation
  * Location
    * JSON representation
  * Range
    * JSON representation
  * ContentLocation
    * JSON representation
  * RecordLocation
    * JSON representation
  * RecordKey
    * JSON representation
  * DatastoreKey
    * JSON representation
  * Key
    * JSON representation
  * PathElement
    * JSON representation
  * BigQueryKey
    * JSON representation
  * TableLocation
    * JSON representation
  * ImageLocation
    * JSON representation
  * BoundingBox
    * JSON representation
  * DocumentLocation
    * JSON representation
  * MetadataLocation
    * JSON representation
  * MetadataType
  * StorageMetadataLabel
    * JSON representation
  * KeyValueMetadataLabel
    * JSON representation
  * ConversationLocation
    * JSON representation
  * AllMessages
  * BatchContentLocation
    * JSON representation
  * QuoteInfo
    * JSON representation
  * DateTime
    * JSON representation
  * TimeZone
    * JSON representation



All the findings for a single scanned item.

JSON representation  
---  
      
    
    {
      "findings": [
        {
          object ([Finding](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#Finding))
        }
      ],
      "findingsTruncated": boolean
    }  
  
Fields  
---  
`findings[]` |  `object (`[Finding](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#Finding)`)` List of findings for an item.  
`findingsTruncated` |  `boolean` If true, then this item might have more findings than were returned, and the findings returned are an arbitrary subset of all findings. The findings list might be truncated because the input items were too large, or because the server reached the maximum amount of resources allowed for a single API call. For best results, divide the input into smaller batches.  
  
## Finding

Represents a piece of potentially sensitive content.

JSON representation  
---  
      
    
    {
      "name": string,
      "quote": string,
      "infoType": {
        object ([InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType))
      },
      "likelihood": enum ([Likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#Likelihood)),
      "location": {
        object ([Location](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#Location))
      },
      "createTime": string,
      "quoteInfo": {
        object ([QuoteInfo](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#QuoteInfo))
      },
      "resourceName": string,
      "triggerName": string,
      "labels": {
        string: string,
        ...
      },
      "jobCreateTime": string,
      "jobName": string,
      "findingId": string
    }  
  
Fields  
---  
`name` |  `string` Resource name in format projects/{project}/locations/{location}/findings/{finding} Populated only when viewing persisted findings.  
`quote` |  `string` The content that was found. Even if the content is not textual, it may be converted to a textual representation here. Provided if `includeQuote` is true and the finding is less than or equal to 4096 bytes long. If the finding exceeds 4096 bytes in length, the quote may be omitted.  
`infoType` |  `object (`[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType)`)` The type of content that might have been found. Provided if `excluded_types` is false.  
`likelihood` |  `enum (`[Likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#Likelihood)`)` Confidence of how likely it is that the `infoType` is correct.  
`location` |  `object (`[Location](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#Location)`)` Where the content was found.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp when finding was detected.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`quoteInfo` |  `object (`[QuoteInfo](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#QuoteInfo)`)` Contains data parsed from quotes. Only populated if includeQuote was set to true and a supported infoType was requested. Currently supported infoTypes: DATE, DATE_OF_BIRTH and TIME.  
`resourceName` |  `string` The job that stored the finding.  
`triggerName` |  `string` Job trigger name, if applicable, for this finding.  
`labels` |  `map (key: string, value: string)` The labels associated with this `Finding`.Label keys must be between 1 and 63 characters long and must conform to the following regular expression: `[a-z]([-a-z0-9]*[a-z0-9])?`.Label values must be between 0 and 63 characters long and must conform to the regular expression `([a-z]([-a-z0-9]*[a-z0-9])?)?`.No more than 10 labels can be associated with a given finding.Examples:

  * `"environment" : "production"`
  * `"pipeline" : "etl"`

An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`jobCreateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time the job started that produced this finding.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`jobName` |  `string` The job that stored the finding.  
`findingId` |  `string` The unique finding id.  
  
## Location

Specifies the location of the finding.

JSON representation  
---  
      
    
    {
      "byteRange": {
        object ([Range](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#Range))
      },
      "codepointRange": {
        object ([Range](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#Range))
      },
      "contentLocations": [
        {
          object ([ContentLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#ContentLocation))
        }
      ],
      "container": {
        object ([Container](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Container))
      }
    }  
  
Fields  
---  
`byteRange` |  `object (`[Range](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#Range)`)` Zero-based byte offsets delimiting the finding. These are relative to the finding's containing element. Note that when the content is not textual, this references the UTF-8 encoded textual representation of the content. Omitted if content is an image.  
`codepointRange` |  `object (`[Range](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#Range)`)` Unicode character offsets delimiting the finding. These are relative to the finding's containing element. Provided when the content is text.  
`contentLocations[]` |  `object (`[ContentLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#ContentLocation)`)` List of nested objects pointing to the precise location of the finding within the file or record.  
`container` |  `object (`[Container](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Container)`)` Information about the container where this finding occurred, if available.  
  
## Range

Generic half-open interval [start, end)

JSON representation  
---  
      
    
    {
      "start": string,
      "end": string
    }  
  
Fields  
---  
`start` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Index of the first character of the range (inclusive).  
`end` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Index of the last character of the range (exclusive).  
  
## ContentLocation

Precise location of the finding within a document, record, image, or metadata container.

JSON representation  
---  
      
    
    {
      "containerName": string,
      "containerTimestamp": string,
      "containerVersion": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "recordLocation": {
        object ([RecordLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#RecordLocation))
      },
      "imageLocation": {
        object ([ImageLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#ImageLocation))
      },
      "documentLocation": {
        object ([DocumentLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#DocumentLocation))
      },
      "metadataLocation": {
        object ([MetadataLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#MetadataLocation))
      },
      "conversationLocation": {
        object ([ConversationLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#ConversationLocation))
      },
      "batchContentLocation": {
        object ([BatchContentLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#BatchContentLocation))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`containerName` |  `string` Name of the container where the finding is located. The top level name is the source file name or table name. Names of some common storage containers are formatted as follows:

  * BigQuery tables: `{projectId}:{datasetId}.{tableId}`
  * Cloud Storage files: `gs://{bucket}/{path}`
  * Datastore namespace: {namespace}

Nested names could be absent if the embedded object has no string identifier (for example, an image contained within a document).  
`containerTimestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Finding container modification timestamp, if applicable. For Cloud Storage, this field contains the last file modification timestamp. For a BigQuery table, this field contains the lastModifiedTime property. For Datastore, this field isn't populated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`containerVersion` |  `string` Finding container version, if available ("generation" for Cloud Storage).  
Type of the container within the file with location of the finding. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`recordLocation` |  `object (`[RecordLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#RecordLocation)`)` Location within a row or record of a database table.  
`imageLocation` |  `object (`[ImageLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#ImageLocation)`)` Location within an image's pixels.  
`documentLocation` |  `object (`[DocumentLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#DocumentLocation)`)` Location data for document files.  
`metadataLocation` |  `object (`[MetadataLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#MetadataLocation)`)` Location within the metadata for inspected content.  
`conversationLocation` |  `object (`[ConversationLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#ConversationLocation)`)` Location within a conversation.  
`batchContentLocation` |  `object (`[BatchContentLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#BatchContentLocation)`)` Location within a batch of content.  
End of mutually exclusive fields.  
  
## RecordLocation

Location of a finding within a row or record.

JSON representation  
---  
      
    
    {
      "recordKey": {
        object ([RecordKey](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#RecordKey))
      },
      "fieldId": {
        object ([FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/FieldId))
      },
      "tableLocation": {
        object ([TableLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#TableLocation))
      }
    }  
  
Fields  
---  
`recordKey` |  `object (`[RecordKey](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#RecordKey)`)` Key of the finding.  
`fieldId` |  `object (`[FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/FieldId)`)` Field id of the field containing the finding.  
`tableLocation` |  `object (`[TableLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#TableLocation)`)` Location within a `ContentItem.Table`.  
  
## RecordKey

Message for a unique key indicating a record that contains a finding.

JSON representation  
---  
      
    
    {
      "idValues": [
        string
      ],
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "datastoreKey": {
        object ([DatastoreKey](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#DatastoreKey))
      },
      "bigQueryKey": {
        object ([BigQueryKey](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#BigQueryKey))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`idValues[]` |  `string` Values of identifying columns in the given row. Order of values matches the order of `identifyingFields` specified in the scanning request.  
Type of key The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`datastoreKey` |  `object (`[DatastoreKey](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#DatastoreKey)`)` BigQuery key  
`bigQueryKey` |  `object (`[BigQueryKey](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#BigQueryKey)`)` Datastore key  
End of mutually exclusive fields.  
  
## DatastoreKey

Record key for a finding in Cloud Datastore.

JSON representation  
---  
      
    
    {
      "entityKey": {
        object ([Key](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#Key))
      }
    }  
  
Fields  
---  
`entityKey` |  `object (`[Key](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#Key)`)` Datastore entity key.  
  
## Key

A unique identifier for a Datastore entity. If a key's partition ID or any of its path kinds or names are reserved/read-only, the key is reserved/read-only. A reserved/read-only key is forbidden in certain documented contexts.

JSON representation  
---  
      
    
    {
      "partitionId": {
        object ([PartitionId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#PartitionId))
      },
      "path": [
        {
          object ([PathElement](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#PathElement))
        }
      ]
    }  
  
Fields  
---  
`partitionId` |  `object (`[PartitionId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#PartitionId)`)` Entities are partitioned into subsets, currently identified by a project ID and namespace ID. Queries are scoped to a single partition.  
`path[]` |  `object (`[PathElement](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#PathElement)`)` The entity path. An entity path consists of one or more elements composed of a kind and a string or numerical identifier, which identify entities. The first element identifies a _root entity_ , the second element identifies a _child_ of the root entity, the third element identifies a child of the second entity, and so forth. The entities identified by all prefixes of the path are called the element's _ancestors_.A path can never be empty, and a path can have at most 100 elements.  
  
## PathElement

A (kind, ID/name) pair used to construct a key path.

If either name or ID is set, the element is complete. If neither is set, the element is incomplete.

JSON representation  
---  
      
    
    {
      "kind": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "id": string,
      "name": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`kind` |  `string` The kind of the entity. A kind matching regex `__.*__` is reserved/read-only. A kind must not contain more than 1500 bytes when UTF-8 encoded. Cannot be `""`.  
The type of ID. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`id` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The auto-allocated ID of the entity. Never equal to zero. Values less than zero are discouraged and may not be supported in the future.  
`name` |  `string` The name of the entity. A name matching regex `__.*__` is reserved/read-only. A name must not be more than 1500 bytes when UTF-8 encoded. Cannot be `""`.  
End of mutually exclusive fields.  
  
## BigQueryKey

Row key for identifying a record in BigQuery table.

JSON representation  
---  
      
    
    {
      "tableReference": {
        object ([BigQueryTable](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/BigQueryTable))
      },
      "rowNumber": string
    }  
  
Fields  
---  
`tableReference` |  `object (`[BigQueryTable](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/BigQueryTable)`)` Complete BigQuery table reference.  
`rowNumber` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Row number inferred at the time the table was scanned. This value is nondeterministic, cannot be queried, and may be null for inspection jobs. To locate findings within a table, specify `inspectJob.storage_config.big_query_options.identifying_fields` in `CreateDlpJobRequest`.  
  
## TableLocation

Location of a finding within a table.

JSON representation  
---  
      
    
    {
      "rowIndex": string
    }  
  
Fields  
---  
`rowIndex` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The zero-based index of the row where the finding is located. Only populated for resources that have a natural ordering, not BigQuery. In BigQuery, to identify the row a finding came from, populate BigQueryOptions.identifying_fields with your primary key column names and when you store the findings the value of those columns will be stored inside of Finding.  
  
## ImageLocation

Location of the finding within an image.

JSON representation  
---  
      
    
    {
      "boundingBoxes": [
        {
          object ([BoundingBox](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#BoundingBox))
        }
      ]
    }  
  
Fields  
---  
`boundingBoxes[]` |  `object (`[BoundingBox](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#BoundingBox)`)` Bounding boxes locating the pixels within the image containing the finding.  
  
## BoundingBox

Bounding box encompassing detected text within an image. Coordinates are in pixels and strictly within the image or frame bounds.

JSON representation  
---  
      
    
    {
      "top": integer,
      "left": integer,
      "width": integer,
      "height": integer
    }  
  
Fields  
---  
`top` |  `integer` Top coordinate of the bounding box. (0,0) is upper left.  
`left` |  `integer` Left coordinate of the bounding box. (0,0) is upper left.  
`width` |  `integer` Width of the bounding box in pixels.  
`height` |  `integer` Height of the bounding box in pixels.  
  
## DocumentLocation

Location of a finding within a document.

JSON representation  
---  
      
    
    {
      "fileOffset": string
    }  
  
Fields  
---  
`fileOffset` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Offset of the line, from the beginning of the file, where the finding is located.  
  
## MetadataLocation

Metadata Location

JSON representation  
---  
      
    
    {
      "type": enum ([MetadataType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#MetadataType)),
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "storageLabel": {
        object ([StorageMetadataLabel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#StorageMetadataLabel))
      },
      "keyValueMetadataLabel": {
        object ([KeyValueMetadataLabel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#KeyValueMetadataLabel))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`type` |  `enum (`[MetadataType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#MetadataType)`)` Type of metadata containing the finding.  
Label of the piece of metadata containing the finding, for example - latitude, author, caption. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`storageLabel` |  `object (`[StorageMetadataLabel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#StorageMetadataLabel)`)` Storage metadata.  
`keyValueMetadataLabel` |  `object (`[KeyValueMetadataLabel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#KeyValueMetadataLabel)`)` Metadata key that contains the finding.  
End of mutually exclusive fields.  
  
## MetadataType

Type of metadata containing the finding.

Enums  
---  
`METADATATYPE_UNSPECIFIED` | Unused  
`STORAGE_METADATA` | General file metadata provided by Cloud Storage.  
`CONTENT_METADATA` | Metadata extracted from the files.  
`CLIENT_PROVIDED_METADATA` | Metadata provided by the client.  
  
## StorageMetadataLabel

Storage metadata label to indicate which metadata entry contains findings.

JSON representation  
---  
      
    
    {
      "key": string
    }  
  
Fields  
---  
`key` |  `string` Label name.  
  
## KeyValueMetadataLabel

The metadata key that contains a finding.

JSON representation  
---  
      
    
    {
      "key": string
    }  
  
Fields  
---  
`key` |  `string` The metadata key. The format depends on the source of the metadata.Example:

  * `MSIP_Label_122709e3-8f6b-4860-985f-7f722a94f61e_Enabled` (a Microsoft Purview Information Protection key example)

  
  
## ConversationLocation

Location within a conversation.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "messageIndex": integer,
      "allMessages": {
        object ([AllMessages](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#AllMessages))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The location of the finding within a conversation. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`messageIndex` |  `integer` Matches an index of a message in the conversation provided in the request.  
`allMessages` |  `object (`[AllMessages](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#AllMessages)`)` If set, indicates that the finding applies to all messages in the conversation.  
End of mutually exclusive fields.  
  
## AllMessages

This type has no fields.

If set, indicates that the finding applies to all messages in the conversation.

## BatchContentLocation

Location within a batch of content.

JSON representation  
---  
      
    
    {
      "itemIndex": integer
    }  
  
Fields  
---  
`itemIndex` |  `integer` Matches an index of a batch item in the batch provided in the request.  
  
## QuoteInfo

Message for infoType-dependent details parsed from quote.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "dateTime": {
        object ([DateTime](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#DateTime))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Object representation of the quote. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`dateTime` |  `object (`[DateTime](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#DateTime)`)` The date time indicated by the quote.  
End of mutually exclusive fields.  
  
## DateTime

Message for a date time object. e.g. 2018-01-01, 5th August.

JSON representation  
---  
      
    
    {
      "date": {
        object ([Date](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Value#Date))
      },
      "dayOfWeek": enum ([DayOfWeek](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Value#DayOfWeek)),
      "time": {
        object ([TimeOfDay](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Value#TimeOfDay))
      },
      "timeZone": {
        object ([TimeZone](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#TimeZone))
      }
    }  
  
Fields  
---  
`date` |  `object (`[Date](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Value#Date)`)` One or more of the following must be set. Must be a valid date or time value.  
`dayOfWeek` |  `enum (`[DayOfWeek](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Value#DayOfWeek)`)` Day of week  
`time` |  `object (`[TimeOfDay](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Value#TimeOfDay)`)` Time of day  
`timeZone` |  `object (`[TimeZone](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#TimeZone)`)` Time zone  
  
## TimeZone

Time zone of the date time object.

JSON representation  
---  
      
    
    {
      "offsetMinutes": integer
    }  
  
Fields  
---  
`offsetMinutes` |  `integer` Set only if the offset can be determined. Positive for time ahead of UTC. E.g. For "UTC-9", this value is -540.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-05 UTC."],[],[]] 
