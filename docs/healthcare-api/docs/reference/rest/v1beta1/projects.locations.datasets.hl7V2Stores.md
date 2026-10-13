---
url: https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores
title: REST Resource: projects.locations.datasets.hl7V2Stores \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:17:54.671124+00:00
---

# REST Resource: projects.locations.datasets.hl7V2Stores  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Reference ](https://docs.cloud.google.com/healthcare-api/docs/apis)



Send feedback 

#  REST Resource: projects.locations.datasets.hl7V2Stores Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: Hl7V2Store

Represents an HL7v2 store.

JSON representation  
---  
      
    
    {
      "name": string,
      "notificationConfig": {
        object([NotificationConfig](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/NotificationConfig))
      },
      "parserConfig": {
        object([ParserConfig](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores#ParserConfig))
      },
      "labels": {
        string: string,
        ...
      },
      "notificationConfigs": [
        {
          object([Hl7V2NotificationConfig](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores#Hl7V2NotificationConfig))
        }
      ],
      "rejectDuplicateMessage": boolean
    }  
  
Fields  
---  
`name` |  `string` Identifier. Resource name of the HL7v2 store, of the form `projects/{projectId}/locations/{locationId}/datasets/{datasetId}/hl7V2Stores/{hl7v2_store_id}`.  
`notificationConfig  
**(deprecated)**` |  `object(`[NotificationConfig](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/NotificationConfig)`)` This item is deprecated!The notification destination all messages (both Ingest & Create) are published on. Only the message name is sent as part of the notification. If this is unset, no notifications are sent. Supplied by the client.  
`parserConfig` |  `object(`[ParserConfig](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores#ParserConfig)`)` The configuration for the parser. It determines how the server parses the messages.  
`labels` |  `map (key: string, value: string)` User-supplied key-value pairs used to organize HL7v2 stores.Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\p{Ll}\p{Lo}][\p{Ll}\p{Lo}\p{N}_-]{0,62}Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\p{Ll}\p{Lo}\p{N}_-]{0,63}No more than 64 labels can be associated with a given store.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`notificationConfigs[]` |  `object(`[Hl7V2NotificationConfig](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores#Hl7V2NotificationConfig)`)` A list of notification configs. Each configuration uses a filter to determine whether to publish a message (both Ingest & Create) on the corresponding notification destination. Only the message name is sent as part of the notification. Supplied by the client.  
`rejectDuplicateMessage` |  `boolean` Determines whether to reject duplicate messages. A duplicate message is a message with the same raw bytes as a message that has already been ingested/created in this HL7v2 store. The default value is false, meaning that the store accepts the duplicate messages and it also returns the same ACK message in the `[IngestMessageResponse](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores.messages/ingest#body.IngestMessageResponse)` as has been returned previously. Note that only one resource is created in the store. When this field is set to true, `[CreateMessage](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores.messages/create#google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.CreateMessage)`/`[IngestMessage](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores.messages/ingest#google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.IngestMessage)` requests with a duplicate message will be rejected by the store, and `IngestMessageErrorDetail` returns a NACK message upon rejection.  
  
## ParserConfig

The configuration for the parser. It determines how the server parses the messages.

JSON representation  
---  
      
    
    {
      "allowNullHeader": boolean,
      "segmentTerminator": string,
      "schema": {
        object([SchemaPackage](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores#SchemaPackage))
      },
      "version": enum([ParserVersion](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores#ParserVersion))
    }  
  
Fields  
---  
`allowNullHeader` |  `boolean` Determines whether messages with no header are allowed.  
`segmentTerminator` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Byte(s) to use as the segment terminator. If this is unset, '\r' is used as segment terminator, matching the HL7 version 2 specification.A base64-encoded string.  
`schema` |  `object(`[SchemaPackage](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores#SchemaPackage)`)` Schemas used to parse messages in this store, if schematized parsing is desired.  
`version` |  `enum(`[ParserVersion](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores#ParserVersion)`)` Immutable. Determines the version of both the default parser to be used when `schema` is not given, as well as the schematized parser used when `schema` is specified. This field is immutable after HL7v2 store creation.  
  
## SchemaPackage

A schema package contains a set of schemas and type definitions.

JSON representation  
---  
      
    
    {
      "schematizedParsingType": enum([SchematizedParsingType](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores#SchematizedParsingType)),
      "schemas": [
        {
          object([Hl7SchemaConfig](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores#Hl7SchemaConfig))
        }
      ],
      "types": [
        {
          object([Hl7TypesConfig](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores#Hl7TypesConfig))
        }
      ],
      "ignoreMinOccurs": boolean,
      "unexpectedSegmentHandling": enum([UnexpectedSegmentHandlingMode](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores#UnexpectedSegmentHandlingMode))
    }  
  
Fields  
---  
`schematizedParsingType` |  `enum(`[SchematizedParsingType](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores#SchematizedParsingType)`)` Determines how messages that fail to parse are handled.  
`schemas[]` |  `object(`[Hl7SchemaConfig](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores#Hl7SchemaConfig)`)` Schema configs that are layered based on their VersionSources that match the incoming message. Schema configs present in higher indices override those in lower indices with the same message type and trigger event if their VersionSources all match an incoming message.  
`types[]` |  `object(`[Hl7TypesConfig](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores#Hl7TypesConfig)`)` Schema type definitions that are layered based on their VersionSources that match the incoming message. Type definitions present in higher indices override those in lower indices with the same type name if their VersionSources all match an incoming message.  
`ignoreMinOccurs` |  `boolean` Flag to ignore all minOccurs restrictions in the schema. This means that incoming messages can omit any group, segment, field, component, or subcomponent.  
`unexpectedSegmentHandling` |  `enum(`[UnexpectedSegmentHandlingMode](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores#UnexpectedSegmentHandlingMode)`)` Determines how unexpected segments (segments not matched to the schema) are handled.  
  
## SchematizedParsingType

Determines the failure mode for schematized parsing.

Enums  
---  
`SCHEMATIZED_PARSING_TYPE_UNSPECIFIED` | Unspecified schematized parsing type, equivalent to `SOFT_FAIL`.  
`SOFT_FAIL` | Messages that fail to parse are still stored and ACKed but a parser error is stored in place of the schematized data.  
`HARD_FAIL` | Messages that fail to parse are rejected from ingestion/insertion and return an error code.  
  
## Hl7SchemaConfig

Root config message for HL7v2 schema. This contains a schema structure of groups and segments, and filters that determine which messages to apply the schema structure to.

JSON representation  
---  
      
    
    {
      "version": [
        {
          object([VersionSource](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores#VersionSource))
        }
      ],
      "messageSchemaConfigs": {
        string: {
          object([SchemaGroup](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores#SchemaGroup))
        },
        ...
      }
    }  
  
Fields  
---  
`version[]` |  `object(`[VersionSource](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores#VersionSource)`)` Each VersionSource is tested and only if they all match is the schema used for the message.  
`messageSchemaConfigs` |  `map (key: string, value: object(`[SchemaGroup](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores#SchemaGroup)`))` Map from each HL7v2 message type and trigger event pair, such as ADT_A04, to its schema configuration root group.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## VersionSource

Describes a selector for extracting and matching an MSH field to a value.

JSON representation  
---  
      
    
    {
      "mshField": string,
      "value": string
    }  
  
Fields  
---  
`mshField` |  `string` The field to extract from the MSH segment. For example, "3.1" or "18[1].1".  
`value` |  `string` The value to match with the field. For example, "My Application Name" or "2.3".  
  
## SchemaGroup

An HL7v2 logical group construct.

JSON representation  
---  
      
    
    {
      "name": string,
      "choice": boolean,
      "minOccurs": integer,
      "maxOccurs": integer,
      "members": [
        {
          object([GroupOrSegment](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores#GroupOrSegment))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` The name of this group. For example, "ORDER_DETAIL".  
`choice` |  `boolean` True indicates that this is a choice group, meaning that only one of its segments can exist in a given message.  
`minOccurs` |  `integer` The minimum number of times this group must be present/repeated.  
`maxOccurs` |  `integer` The maximum number of times this group can be repeated. 0 or -1 means unbounded.  
`members[]` |  `object(`[GroupOrSegment](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores#GroupOrSegment)`)` Nested groups and/or segments.  
  
## GroupOrSegment

Construct representing a logical group or a segment.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "segment": {
        object([SchemaSegment](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores#SchemaSegment))
      },
      "group": {
        object([SchemaGroup](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores#SchemaGroup))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`segment` |  `object(`[SchemaSegment](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores#SchemaSegment)`)`  
`group` |  `object(`[SchemaGroup](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores#SchemaGroup)`)`  
End of mutually exclusive fields.  
  
## SchemaSegment

An HL7v2 Segment.

JSON representation  
---  
      
    
    {
      "type": string,
      "minOccurs": integer,
      "maxOccurs": integer
    }  
  
Fields  
---  
`type` |  `string` The Segment type. For example, "PID".  
`minOccurs` |  `integer` The minimum number of times this segment can be present in this group.  
`maxOccurs` |  `integer` The maximum number of times this segment can be present in this group. 0 or -1 means unbounded.  
  
## Hl7TypesConfig

Root config for HL7v2 datatype definitions for a specific HL7v2 version.

JSON representation  
---  
      
    
    {
      "version": [
        {
          object([VersionSource](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores#VersionSource))
        }
      ],
      "type": [
        {
          object([Type](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores#Type))
        }
      ]
    }  
  
Fields  
---  
`version[]` |  `object(`[VersionSource](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores#VersionSource)`)` The version selectors that this config applies to. A message must match ALL version sources to apply.  
`type[]` |  `object(`[Type](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores#Type)`)` The HL7v2 type definitions.  
  
## Type

A type definition for some HL7v2 type (incl. Segments and Datatypes).

JSON representation  
---  
      
    
    {
      "name": string,
      "primitive": enum([Primitive](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores#Primitive)),
      "fields": [
        {
          object([Field](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores#Field))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` The name of this type. This would be the segment or datatype name. For example, "PID" or "XPN".  
`primitive` |  `enum(`[Primitive](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores#Primitive)`)` If this is a primitive type then this field is the type of the primitive For example, STRING. Leave unspecified for composite types.  
`fields[]` |  `object(`[Field](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores#Field)`)` The (sub) fields this type has (if not primitive).  
  
## Primitive

Enums  
---  
`PRIMITIVE_UNSPECIFIED` | Not a primitive.  
`STRING` | String primitive.  
`VARIES` | Element that can have unschematized children.  
`UNESCAPED_STRING` | Like STRING, but all delimiters below this element are ignored.  
  
## Field

A (sub) field of a type.

JSON representation  
---  
      
    
    {
      "name": string,
      "type": string,
      "table": string,
      "minOccurs": integer,
      "maxOccurs": integer
    }  
  
Fields  
---  
`name` |  `string` The name of the field. For example, "PID-1" or just "1".  
`type` |  `string` The type of this field. A Type with this name must be defined in an Hl7TypesConfig.  
`table` |  `string` The HL7v2 table this field refers to. For example, PID-15 (Patient's Primary Language) usually refers to table "0296".  
`minOccurs` |  `integer` The minimum number of times this field must be present/repeated.  
`maxOccurs` |  `integer` The maximum number of times this field can be repeated. 0 or -1 means unbounded.  
  
## UnexpectedSegmentHandlingMode

Determines how unexpected segments are handled. An unexpected segment is a segment that is present in a message but has no corresponding match in the message type definition.

Enums  
---  
`UNEXPECTED_SEGMENT_HANDLING_MODE_UNSPECIFIED` | Unspecified handling mode, equivalent to FAIL.  
`FAIL` | Unexpected segments fail to parse and return an error.  
`SKIP` | Unexpected segments do not fail, but are omitted from the output.  
`PARSE` | Unexpected segments do not fail, but are parsed in place and added to the current group. If a segment has a type definition, it is used, otherwise it is parsed as VARIES.  
  
## ParserVersion

The parser version. Applies to both the default parser and the schematized parser. The highest version of the parser is recommended.

Enums  
---  
`PARSER_VERSION_UNSPECIFIED` | Unspecified parser version, equivalent to V1.  
`V1` | The `parsedData` includes every given non-empty message field except the Field Separator (MSH-1) field. As a result, the parsed MSH segment starts with the MSH-2 field and the field numbers are off-by-one with respect to the HL7 standard.  
`V2` | The `parsedData` includes every given non-empty message field.  
`V3` | This version is the same as V2, with the following change.The `parsedData` contains unescaped escaped field separators, component separators, sub-component separators, repetition separators, escape characters, and truncation characters.If `schema` is specified, the schematized parser uses improved parsing heuristics compared to previous versions.  
  
## Hl7V2NotificationConfig

Specifies where and whether to send notifications upon changes to a data store.

JSON representation  
---  
      
    
    {
      "pubsubTopic": string,
      "filter": string
    }  
  
Fields  
---  
`pubsubTopic` |  `string` The [Pub/Sub](https://cloud.google.com/pubsub/docs/) topic that notifications of changes are published on. Supplied by the client. The notification is a `PubsubMessage` with the following fields:

  * `PubsubMessage.Data` contains the resource name.
  * `PubsubMessage.MessageId` is the ID of this notification. It is guaranteed to be unique within the topic.
  * `PubsubMessage.PublishTime` is the time when the message was published.

Note that notifications are only sent if the topic is non-empty. [Topic names](https://cloud.google.com/pubsub/docs/overview#names) must be scoped to a project. Cloud Healthcare API service account must have publisher permissions on the given Pub/Sub topic. Not having adequate permissions causes the calls that send notifications to fail.If a notification can't be published to Pub/Sub, errors are logged to Cloud Logging. For more information, see [Viewing error logs in Cloud Logging](https://cloud.google.com/healthcare/docs/how-tos/logging).  
`filter` |  `string` Restricts notifications sent for messages matching a filter. If this is empty, all messages are matched. The following syntax is available:

  * A string field value can be written as text inside quotation marks, for example `"query text"`. The only valid relational operation for text fields is equality(`=`), where text is searched within the field, rather than having the field be equal to the text. For example, `"Comment = great"` returns messages with `great` in the comment field.
  * A number field value can be written as an integer, a decimal, or an exponential. The valid relational operators for number fields are the equality operator(`=`), along with the less than/greater than operators(`<`, `<=`, `>`, `>=`). Note that there is no inequality (`!=`) operator. You can prepend the `NOT` operator to an expression to negate it.
  * A date field value must be written in `yyyy-mm-dd` form. Fields with date and time use the RFC3339 time format. Leading zeros are required for one-digit months and days. The valid relational operators for date fields are the equality operator(`=`) , along with the less than/greater than operators(`<`, `<=`, `>`, `>=`). Note that there is no inequality(`!=`) operator. You can prepend the `NOT` operator to an expression to negate it.
  * Multiple field query expressions can be combined in one query by adding `AND` or `OR` operators between the expressions. If a boolean operator appears within a quoted string, it is not treated as special, it's just another part of the character string to be matched. You can prepend the `NOT` operator to an expression to negate it.

Fields/functions available for filtering are:

  * `messageType`, from the MSH-9.1 field. For example, `NOT messageType = "ADT"`.
  * `send_date` or `sendDate`, the YYYY-MM-DD date the message was sent in the dataset's timeZone, from the MSH-7 segment. For example, `send_date < "2017-01-02"`.
  * `sendTime`, the timestamp when the message was sent, using the RFC3339 time format for comparisons, from the MSH-7 segment. For example, `sendTime < "2017-01-02T00:00:00-05:00"`.
  * `createTime`, the timestamp when the message was created in the HL7v2 store. Use the RFC3339 time format for comparisons. For example, `createTime < "2017-01-02T00:00:00-05:00"`.
  * `sendFacility`, the care center that the message came from, from the MSH-4 segment. For example, `sendFacility = "ABC"`.
  * `PatientId(value, type)`, which matches if the message lists a patient having an ID of the given value and type in the PID-2, PID-3, or PID-4 segments. For example, `PatientId("123456", "MRN")`.
  * `labels.x`, a string value of the label with key `x` as set using the `[Message.labels](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores.messages#Message.FIELDS.labels)` map. For example, `labels."priority"="high"`. The operator `:*` can be used to assert the existence of a label. For example, `labels."priority":*`.

  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores/create)`

|  Creates a new HL7v2 store within the parent dataset.  
  
### `[delete](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores/delete)`

|  Deletes the specified HL7v2 store and removes all messages that it contains.  
  
### `[export](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores/export)`

|  Exports the messages to a destination.  
  
### `[get](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores/get)`

|  Gets the specified HL7v2 store.  
  
### `[getHL7v2StoreMetrics](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores/getHL7v2StoreMetrics)`

|  Gets metrics associated with the HL7v2 store.  
  
### `[getIamPolicy](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[import](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores/import)`

|  Import messages to the HL7v2 store by loading data from the specified sources.  
  
### `[list](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores/list)`

|  Lists the HL7v2 stores in the given dataset.  
  
### `[patch](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores/patch)`

|  Updates the HL7v2 store.  
  
### `[rollback](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores/rollback)`

|  Rolls back messages from the HL7v2 store to the specified time.  
  
### `[setIamPolicy](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
