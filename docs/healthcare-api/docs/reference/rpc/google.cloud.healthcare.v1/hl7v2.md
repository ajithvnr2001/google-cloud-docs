---
url: https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2/
title: Package google.cloud.healthcare.v1.hl7v2 \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:15:04.451173+00:00
---

# Package google.cloud.healthcare.v1.hl7v2  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Reference ](https://docs.cloud.google.com/healthcare-api/docs/apis)



Send feedback 

#  Package google.cloud.healthcare.v1.hl7v2 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[Hl7V2Service](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Hl7V2Service)` (interface)
  * `[CreateHl7V2StoreRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.CreateHl7V2StoreRequest)` (message)
  * `[CreateMessageRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.CreateMessageRequest)` (message)
  * `[DeleteHl7V2StoreRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.DeleteHl7V2StoreRequest)` (message)
  * `[DeleteMessageRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.DeleteMessageRequest)` (message)
  * `[ExportMessagesRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.ExportMessagesRequest)` (message)
  * `[ExportMessagesResponse](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.ExportMessagesResponse)` (message)
  * `[GcsDestination](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.GcsDestination)` (message)
  * `[GcsDestination.ContentStructure](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.GcsDestination.ContentStructure)` (enum)
  * `[GcsSource](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.GcsSource)` (message)
  * `[GetHl7V2StoreMetricsRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.GetHl7V2StoreMetricsRequest)` (message)
  * `[GetHl7V2StoreRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.GetHl7V2StoreRequest)` (message)
  * `[GetMessageRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.GetMessageRequest)` (message)
  * `[GroupOrSegment](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.GroupOrSegment)` (message)
  * `[Hl7SchemaConfig](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Hl7SchemaConfig)` (message)
  * `[Hl7TypesConfig](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Hl7TypesConfig)` (message)
  * `[Hl7V2Store](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Hl7V2Store)` (message)
  * `[Hl7V2Store.Hl7V2NotificationConfig](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Hl7V2Store.Hl7V2NotificationConfig)` (message)
  * `[Hl7V2StoreMetrics](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Hl7V2StoreMetrics)` (message)
  * `[Hl7V2StoreMetrics.Hl7V2StoreMetric](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Hl7V2StoreMetrics.Hl7V2StoreMetric)` (message)
  * `[ImportMessagesRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.ImportMessagesRequest)` (message)
  * `[ImportMessagesResponse](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.ImportMessagesResponse)` (message)
  * `[IngestMessageErrorDetail](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.IngestMessageErrorDetail)` (message)
  * `[IngestMessageRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.IngestMessageRequest)` (message)
  * `[IngestMessageResponse](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.IngestMessageResponse)` (message)
  * `[ListHl7V2StoresRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.ListHl7V2StoresRequest)` (message)
  * `[ListHl7V2StoresResponse](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.ListHl7V2StoresResponse)` (message)
  * `[ListMessagesRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.ListMessagesRequest)` (message)
  * `[ListMessagesResponse](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.ListMessagesResponse)` (message)
  * `[Message](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Message)` (message)
  * `[MessageView](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.MessageView)` (enum)
  * `[ParsedData](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.ParsedData)` (message)
  * `[ParserConfig](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.ParserConfig)` (message)
  * `[ParserConfig.ParserVersion](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.ParserConfig.ParserVersion)` (enum)
  * `[PubsubDestination](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.PubsubDestination)` (message)
  * `[SchemaGroup](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.SchemaGroup)` (message)
  * `[SchemaPackage](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.SchemaPackage)` (message)
  * `[SchemaPackage.UnexpectedSegmentHandlingMode](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.SchemaPackage.UnexpectedSegmentHandlingMode)` (enum)
  * `[SchemaSegment](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.SchemaSegment)` (message)
  * `[SchematizedData](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.SchematizedData)` (message)
  * `[SchematizedParsingType](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.SchematizedParsingType)` (enum)
  * `[Segment](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Segment)` (message)
  * `[Type](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Type)` (message)
  * `[Type.Field](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Type.Field)` (message)
  * `[Type.Primitive](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Type.Primitive)` (enum)
  * `[UpdateHl7V2StoreRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.UpdateHl7V2StoreRequest)` (message)
  * `[UpdateMessageRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.UpdateMessageRequest)` (message)
  * `[VersionSource](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.VersionSource)` (message)



## Hl7V2Service

A service for handling HL7v2 messages (v2.x).

CreateHl7V2Store  
---  
` rpc CreateHl7V2Store(`[CreateHl7V2StoreRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.CreateHl7V2StoreRequest)`) returns (`[Hl7V2Store](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Hl7V2Store)`) ` Creates a new HL7v2 store within the parent dataset.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-healthcare`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
CreateMessage  
---  
` rpc CreateMessage(`[CreateMessageRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.CreateMessageRequest)`) returns (`[Message](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Message)`) ` Parses and stores an HL7v2 message. This method triggers an asynchronous notification to any Pub/Sub topic configured in `[Hl7V2Store.Hl7V2NotificationConfig](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Hl7V2Store.Hl7V2NotificationConfig)`, if the filtering matches the message. If an MLLP adapter is configured to listen to a Pub/Sub topic, the adapter transmits the message when a notification is received.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-healthcare`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
DeleteHl7V2Store  
---  
` rpc DeleteHl7V2Store(`[DeleteHl7V2StoreRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.DeleteHl7V2StoreRequest)`) returns (`[Empty](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Empty)`) ` Deletes the specified HL7v2 store and removes all messages that it contains.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-healthcare`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
DeleteMessage  
---  
` rpc DeleteMessage(`[DeleteMessageRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.DeleteMessageRequest)`) returns (`[Empty](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Empty)`) ` Deletes an HL7v2 message.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-healthcare`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
ExportMessages  
---  
` rpc ExportMessages(`[ExportMessagesRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.ExportMessagesRequest)`) returns (`[Operation](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Exports the messages to a destination. To filter messages to be exported, define a filter using the start and end time, relative to the message generation time (MSH.7).This API returns an `[Operation](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.longrunning#google.longrunning.Operation)` that can be used to track the status of the job by calling `[GetOperation](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.longrunning#google.longrunning.Operations.GetOperation)`.Immediate fatal errors appear in the `[error](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.longrunning#google.longrunning.Operation.FIELDS.google.rpc.Status.google.longrunning.Operation.error)` field. Otherwise, when the operation finishes, a detailed response of type `[ExportMessagesResponse](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.ExportMessagesResponse)` is returned in the `[response](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.longrunning#google.longrunning.Operation.FIELDS.google.protobuf.Any.google.longrunning.Operation.response)` field. The `[metadata](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.longrunning#google.longrunning.Operation.FIELDS.google.protobuf.Any.google.longrunning.Operation.metadata)` field type for this operation is `[OperationMetadata](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1#google.cloud.healthcare.v1.OperationMetadata)`.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-healthcare`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
GetHl7V2Store  
---  
` rpc GetHl7V2Store(`[GetHl7V2StoreRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.GetHl7V2StoreRequest)`) returns (`[Hl7V2Store](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Hl7V2Store)`) ` Gets the specified HL7v2 store.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-healthcare`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
GetHl7V2StoreMetrics  
---  
` rpc GetHl7V2StoreMetrics(`[GetHl7V2StoreMetricsRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.GetHl7V2StoreMetricsRequest)`) returns (`[Hl7V2StoreMetrics](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Hl7V2StoreMetrics)`) ` Gets metrics associated with the HL7v2 store.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-healthcare`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
GetMessage  
---  
` rpc GetMessage(`[GetMessageRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.GetMessageRequest)`) returns (`[Message](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Message)`) ` Gets an HL7v2 message.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-healthcare`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
ImportMessages  
---  
` rpc ImportMessages(`[ImportMessagesRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.ImportMessagesRequest)`) returns (`[Operation](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Import messages to the HL7v2 store by loading data from the specified sources. This method is optimized to load large quantities of data using import semantics that ignore some HL7v2 store configuration options and are not suitable for all use cases. It is primarily intended to load data into an empty HL7v2 store that is not being used by other clients.An existing message will be overwritten if a duplicate message is imported. A duplicate message is a message with the same raw bytes as a message that already exists in this HL7v2 store. When a message is overwritten, its labels will also be overwritten.The import operation is idempotent unless the input data contains multiple valid messages with the same raw bytes but different labels. In that case, after the import completes, the store contains exactly one message with those raw bytes but there is no ordering guarantee on which version of the labels it has. The operation result counters do not count duplicated raw bytes as an error and count one success for each message in the input, which might result in a success count larger than the number of messages in the HL7v2 store.If some messages fail to import, for example due to parsing errors, successfully imported messages are not rolled back.This method returns an `[Operation](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.longrunning#google.longrunning.Operation)` that can be used to track the status of the import by calling `[GetOperation](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.longrunning#google.longrunning.Operations.GetOperation)`.Immediate fatal errors appear in the `[error](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.longrunning#google.longrunning.Operation.FIELDS.google.rpc.Status.google.longrunning.Operation.error)` field, errors are also logged to Cloud Logging (see [Viewing error logs in Cloud Logging](https://cloud.google.com/healthcare/docs/how-tos/logging)). Otherwise, when the operation finishes, a response of type `[ImportMessagesResponse](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.ImportMessagesResponse)` is returned in the `[response](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.longrunning#google.longrunning.Operation.FIELDS.google.protobuf.Any.google.longrunning.Operation.response)` field. The `[metadata](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.longrunning#google.longrunning.Operation.FIELDS.google.protobuf.Any.google.longrunning.Operation.metadata)` field type for this operation is `[OperationMetadata](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1#google.cloud.healthcare.v1.OperationMetadata)`.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-healthcare`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
IngestMessage  
---  
` rpc IngestMessage(`[IngestMessageRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.IngestMessageRequest)`) returns (`[IngestMessageResponse](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.IngestMessageResponse)`) ` Parses and stores an HL7v2 message. This method triggers an asynchronous notification to any Pub/Sub topic configured in `[Hl7V2Store.Hl7V2NotificationConfig](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Hl7V2Store.Hl7V2NotificationConfig)`, if the filtering matches the message. If an MLLP adapter is configured to listen to a Pub/Sub topic, the adapter transmits the message when a notification is received. If the method is successful, it generates a response containing an HL7v2 acknowledgment (`ACK`) message. If the method encounters an error, it returns a negative acknowledgment (`NACK`) message. This behavior is suitable for replying to HL7v2 interface systems that expect these acknowledgments.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-healthcare`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
ListHl7V2Stores  
---  
` rpc ListHl7V2Stores(`[ListHl7V2StoresRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.ListHl7V2StoresRequest)`) returns (`[ListHl7V2StoresResponse](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.ListHl7V2StoresResponse)`) ` Lists the HL7v2 stores in the given dataset.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-healthcare`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
ListMessages  
---  
` rpc ListMessages(`[ListMessagesRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.ListMessagesRequest)`) returns (`[ListMessagesResponse](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.ListMessagesResponse)`) ` Lists all the messages in the given HL7v2 store with support for filtering.Note: HL7v2 messages are indexed asynchronously, so there might be a slight delay between the time a message is created and when it can be found through a filter.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-healthcare`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
UpdateHl7V2Store  
---  
` rpc UpdateHl7V2Store(`[UpdateHl7V2StoreRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.UpdateHl7V2StoreRequest)`) returns (`[Hl7V2Store](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Hl7V2Store)`) ` Updates the HL7v2 store.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-healthcare`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
UpdateMessage  
---  
` rpc UpdateMessage(`[UpdateMessageRequest](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.UpdateMessageRequest)`) returns (`[Message](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Message)`) ` Update the message.The contents of the message in `[Message.data](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Message.FIELDS.bytes.google.cloud.healthcare.v1.hl7v2.Message.data)` and data extracted from the contents such as `[Message.create_time](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Message.FIELDS.google.protobuf.Timestamp.google.cloud.healthcare.v1.hl7v2.Message.create_time)` cannot be altered. Only the `[Message.labels](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Message.FIELDS.repeated.google.cloud.healthcare.v1.hl7v2.Message.LabelsEntry.google.cloud.healthcare.v1.hl7v2.Message.labels)` field is allowed to be updated. The labels in the request are merged with the existing set of labels. Existing labels with the same keys are updated.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-healthcare`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
  
## CreateHl7V2StoreRequest

Creates a new HL7v2 store.

Fields  
---  
`parent` |  `string` Required. The name of the dataset this HL7v2 store belongs to. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `healthcare.hl7V2Stores.create`

  
`hl7_v2_store_id` |  `string` Required. The ID of the HL7v2 store that is being created. The string must match the following regex: `[\p{L}\p{N}_\-\.]{1,256}`.  
`hl7_v2_store` |  ``[Hl7V2Store](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Hl7V2Store)`` Configuration info for this HL7v2 store.  
  
## CreateMessageRequest

Creates a new message.

Fields  
---  
`parent` |  `string` Required. The name of the HL7v2 store this message belongs to. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `healthcare.hl7V2Messages.create`

  
`message` |  ``[Message](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Message)`` Required. HL7v2 message.  
  
## DeleteHl7V2StoreRequest

Deletes the specified HL7v2 store.

Fields  
---  
`name` |  `string` Required. The resource name of the HL7v2 store to delete. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `healthcare.hl7V2Stores.delete`

  
  
## DeleteMessageRequest

Deletes a message from the specified HL7v2 store.

Fields  
---  
`name` |  `string` Required. The resource name of the HL7v2 message to delete. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `healthcare.hl7V2Messages.delete`

  
  
## ExportMessagesRequest

Request to schedule an export.

Fields  
---  
`name` |  `string` Required. The name of the source HL7v2 store, in the format `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/hl7v2Stores/{hl7v2_store_id}` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `healthcare.hl7v2Stores.export`

  
`start_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` The start of the range in `send_time` (MSH.7, <https://www.hl7.org/documentcenter/public_temp_2E58C1F9-1C23-BA17-0C6126475344DA9D/wg/conf/HL7MSH.htm>) to process. If not specified, the UNIX epoch (1970-01-01T00:00:00Z) is used.This value has to come before the `end_time` defined below. Only messages whose `send_time` lies in the range `start_time` (inclusive) to `end_time` (exclusive) are exported.  
`end_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` The end of the range in `send_time` (MSH.7, <https://www.hl7.org/documentcenter/public_temp_2E58C1F9-1C23-BA17-0C6126475344DA9D/wg/conf/HL7MSH.htm>) to process. If not specified, the time when the export is scheduled is used.This value has to come after the `start_time` defined below. Only messages whose `send_time` lies in the range `start_time` (inclusive) to `end_time` (exclusive) are exported.  
`filter` |  `string` Restricts messages exported to those matching a filter, only applicable to `[PubsubDestination](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.PubsubDestination)` and `[GcsDestination](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.GcsDestination)`. The following syntax is available:

  * A string field value can be written as text inside quotation marks, for example `"query text"`. The only valid relational operation for text fields is equality (`=`), where text is searched within the field, rather than having the field be equal to the text. For example, `"Comment = great"` returns messages with `great` in the comment field.
  * A number field value can be written as an integer, a decimal, or an exponential. The valid relational operators for number fields are the equality operator (`=`), along with the less than/greater than operators (`<`, `<=`, `>`, `>=`). Note that there is no inequality (`!=`) operator. You can prepend the `NOT` operator to an expression to negate it.
  * A date field value must be written in the `yyyy-mm-dd` format. Fields with date and time use the RFC3339 time format. Leading zeros are required for one-digit months and days. The valid relational operators for date fields are the equality operator (`=`) , along with the less than/greater than operators (`<`, `<=`, `>`, `>=`). Note that there is no inequality (`!=`) operator. You can prepend the `NOT` operator to an expression to negate it.
  * Multiple field query expressions can be combined in one query by adding `AND` or `OR` operators between the expressions. If a boolean operator appears within a quoted string, it is not treated as special, and is just another part of the character string to be matched. You can prepend the `NOT` operator to an expression to negate it.

The following fields and functions are available for filtering:

  * `message_type`, from the MSH-9.1 field. For example, `NOT message_type = "ADT"`.
  * `send_date` or `sendDate`, the `yyyy-mm-dd` date the message was sent in the dataset's time_zone, from the MSH-7 segment. For example, `send_date < "2017-01-02"`.
  * `send_time`, the timestamp when the message was sent, using the RFC3339 time format for comparisons, from the MSH-7 segment. For example, `send_time < "2017-01-02T00:00:00-05:00"`.
  * `create_time`, the timestamp when the message was created in the HL7v2 store. Use the RFC3339 time format for comparisons. For example, `create_time < "2017-01-02T00:00:00-05:00"`.
  * `send_facility`, the care center that the message came from, from the MSH-4 segment. For example, `send_facility = "ABC"`.

Note: The filter will be applied to every message in the HL7v2 store whose `send_time` lies in the range defined by the `start_time` and the `end_time`. Even if the filter only matches a small set of messages, the export operation can still take a long time to finish when a lot of messages are between the specified `start_time` and `end_time` range.  
Union field `destination`. Export destination. `destination` can be only one of the following:  
`gcs_destination` |  ``[GcsDestination](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.GcsDestination)`` Export to a Cloud Storage destination.  
`pubsub_destination` |  ``[PubsubDestination](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.PubsubDestination)`` Export messages to a Pub/Sub topic.  
  
## ExportMessagesResponse

This type has no fields.

Final response for the export operation. This structure is included in the `[response](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.longrunning#google.longrunning.Operation.FIELDS.google.protobuf.Any.google.longrunning.Operation.response)` to describe the detailed outcome.

## GcsDestination

The Cloud Storage output destination.

The Cloud Healthcare Service Agent requires the `roles/storage.objectAdmin` Cloud IAM roles on the Cloud Storage location.

Fields  
---  
`uri_prefix` |  `string` URI of an existing Cloud Storage directory where the server writes result files, in the format `gs://{bucket-id}/{path/to/destination/dir}`. If there is no trailing slash, the service appends one when composing the object path.  
`message_view` |  ``[MessageView](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.MessageView)`` Specifies the parts of the Message resource to include in the export. If not specified, FULL is used.  
`content_structure` |  ``[ContentStructure](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.GcsDestination.ContentStructure)`` The format of the exported HL7v2 message files.  
  
## ContentStructure

The content structure of the exported HL7v2 message files.

Enums  
---  
`CONTENT_STRUCTURE_UNSPECIFIED` | If the content structure is not specified, the default value `MESSAGE_JSON` will be used.  
`MESSAGE_JSON` | Messages are printed using the JSON format returned from the `GetMessage` API. Messages are delimited with newlines.  
  
## GcsSource

Specifies the configuration for importing data from Cloud Storage.

Fields  
---  
`uri` |  `string` Points to a Cloud Storage URI containing file(s) to import.The URI must be in the following format: `gs://{bucket_id}/{object_id}`. The URI can include wildcards in `object_id` and thus identify multiple files. Supported wildcards:

  * `*` to match 0 or more non-separator characters
  * `**` to match 0 or more characters (including separators). Must be used at the end of a path and with no other wildcards in the path. Can also be used with a file extension (such as .ndjson), which imports all files with the extension in the specified directory and its sub-directories. For example, `gs://my-bucket/my-directory/**.ndjson` imports all files with `.ndjson` extensions in `my-directory/` and its sub-directories.
  * `?` to match 1 character

Files matching the wildcard are expected to contain content only, no metadata.  
  
## GetHl7V2StoreMetricsRequest

Request to get HL7v2 store metrics.

Fields  
---  
`name` |  `string` Required. The resource name of the HL7v2 store to get metrics for, in the format `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/hl7V2Stores/{hl7v2_store_id}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `healthcare.hl7V2Stores.get`

  
  
## GetHl7V2StoreRequest

Gets an HL7v2 store.

Fields  
---  
`name` |  `string` Required. The resource name of the HL7v2 store to get. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `healthcare.hl7V2Stores.get`

  
  
## GetMessageRequest

Gets a message from the specified HL7v2 store.

Fields  
---  
`name` |  `string` Required. The resource name of the HL7v2 message to retrieve. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `healthcare.hl7V2Messages.get`

  
`view` |  ``[MessageView](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.MessageView)`` Specifies which parts of the Message resource to return in the response. When unspecified, equivalent to FULL.  
  
## GroupOrSegment

Construct representing a logical group or a segment.

Fields  
---  
Union field `value`.`value` can be only one of the following:  
`segment` |  ``[SchemaSegment](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.SchemaSegment)``  
`group` |  ``[SchemaGroup](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.SchemaGroup)``  
  
## Hl7SchemaConfig

Root config message for HL7v2 schema. This contains a schema structure of groups and segments, and filters that determine which messages to apply the schema structure to.

Fields  
---  
`version[]` |  ``[VersionSource](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.VersionSource)`` Each VersionSource is tested and only if they all match is the schema used for the message.  
`message_schema_configs` |  `map<string, `[SchemaGroup](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.SchemaGroup)`>` Map from each HL7v2 message type and trigger event pair, such as ADT_A04, to its schema configuration root group.  
  
## Hl7TypesConfig

Root config for HL7v2 datatype definitions for a specific HL7v2 version.

Fields  
---  
`version[]` |  ``[VersionSource](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.VersionSource)`` The version selectors that this config applies to. A message must match ALL version sources to apply.  
`type[]` |  ``[Type](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Type)`` The HL7v2 type definitions.  
  
## Hl7V2Store

Represents an HL7v2 store.

Fields  
---  
`name` |  `string` Identifier. Resource name of the HL7v2 store, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/hl7V2Stores/{hl7v2_store_id}`.  
`parser_config` |  ``[ParserConfig](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.ParserConfig)`` The configuration for the parser. It determines how the server parses the messages.  
`labels` |  `map<string, string>` User-supplied key-value pairs used to organize HL7v2 stores.Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\p{Ll}\p{Lo}][\p{Ll}\p{Lo}\p{N}_-]{0,62}Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\p{Ll}\p{Lo}\p{N}_-]{0,63}No more than 64 labels can be associated with a given store.  
`notification_configs[]` |  ``[Hl7V2NotificationConfig](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Hl7V2Store.Hl7V2NotificationConfig)`` A list of notification configs. Each configuration uses a filter to determine whether to publish a message (both Ingest & Create) on the corresponding notification destination. Only the message name is sent as part of the notification. Supplied by the client.  
`reject_duplicate_message` |  `bool` Determines whether to reject duplicate messages. A duplicate message is a message with the same raw bytes as a message that has already been ingested/created in this HL7v2 store. The default value is false, meaning that the store accepts the duplicate messages and it also returns the same ACK message in the `[IngestMessageResponse](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.IngestMessageResponse)` as has been returned previously. Note that only one resource is created in the store. When this field is set to true, `[CreateMessage](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Hl7V2Service.CreateMessage)`/`[IngestMessage](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Hl7V2Service.IngestMessage)` requests with a duplicate message will be rejected by the store, and `[IngestMessageErrorDetail](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.IngestMessageErrorDetail)` returns a NACK message upon rejection.  
  
## Hl7V2NotificationConfig

Specifies where and whether to send notifications upon changes to a data store.

Fields  
---  
`pubsub_topic` |  `string` The [Pub/Sub](https://cloud.google.com/pubsub/docs/) topic that notifications of changes are published on. Supplied by the client.The notification is a `PubsubMessage` with the following fields:

  * `PubsubMessage.Data` contains the resource name.
  * `PubsubMessage.MessageId` is the ID of this notification. It's guaranteed to be unique within the topic.
  * `PubsubMessage.PublishTime` is the time when the message was published.

Note that notifications are only sent if the topic is non-empty. [Topic names](https://cloud.google.com/pubsub/docs/overview#names) must be scoped to a project.The Cloud Healthcare API service account, [service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com](mailto:service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com), must have publisher permissions on the given Pub/Sub topic. Not having adequate permissions causes the calls that send notifications to fail.If a notification cannot be published to Pub/Sub, errors are logged to Cloud Logging. For more information, see [Viewing error logs in Cloud Logging](https://cloud.google.com/healthcare/docs/how-tos/logging)).  
`filter` |  `string` Restricts notifications sent for messages matching a filter. If this is empty, all messages are matched. The following syntax is available:

  * A string field value can be written as text inside quotation marks, for example `"query text"`. The only valid relational operation for text fields is equality (`=`), where text is searched within the field, rather than having the field be equal to the text. For example, `"Comment = great"` returns messages with `great` in the comment field.
  * A number field value can be written as an integer, a decimal, or an exponential. The valid relational operators for number fields are the equality operator (`=`), along with the less than/greater than operators (`<`, `<=`, `>`, `>=`). Note that there is no inequality (`!=`) operator. You can prepend the `NOT` operator to an expression to negate it.
  * A date field value must be written in `yyyy-mm-dd` form. Fields with date and time use the RFC3339 time format. Leading zeros are required for one-digit months and days. The valid relational operators for date fields are the equality operator (`=`) , along with the less than/greater than operators (`<`, `<=`, `>`, `>=`). Note that there is no inequality (`!=`) operator. You can prepend the `NOT` operator to an expression to negate it.
  * Multiple field query expressions can be combined in one query by adding `AND` or `OR` operators between the expressions. If a boolean operator appears within a quoted string, it is not treated as special, it's just another part of the character string to be matched. You can prepend the `NOT` operator to an expression to negate it.

The following fields and functions are available for filtering:

  * `message_type`, from the MSH-9.1 field. For example, `NOT message_type = "ADT"`.
  * `send_date` or `sendDate`, the YYYY-MM-DD date the message was sent in the dataset's time_zone, from the MSH-7 segment. For example, `send_date < "2017-01-02"`.
  * `send_time`, the timestamp when the message was sent, using the RFC3339 time format for comparisons, from the MSH-7 segment. For example, `send_time < "2017-01-02T00:00:00-05:00"`.
  * `create_time`, the timestamp when the message was created in the HL7v2 store. Use the RFC3339 time format for comparisons. For example, `create_time < "2017-01-02T00:00:00-05:00"`.
  * `send_facility`, the care center that the message came from, from the MSH-4 segment. For example, `send_facility = "ABC"`.
  * `PatientId(value, type)`, which matches if the message lists a patient having an ID of the given value and type in the PID-2, PID-3, or PID-4 segments. For example, `PatientId("123456", "MRN")`.
  * `labels.x`, a string value of the label with key `x` as set using the `[Message.labels](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1beta1/hl7v2#google.cloud.healthcare.v1beta1.hl7v2.Message.FIELDS.repeated.google.cloud.healthcare.v1beta1.hl7v2.Message.LabelsEntry.google.cloud.healthcare.v1beta1.hl7v2.Message.labels)` map. For example, `labels."priority"="high"`. The operator `:*` can be used to assert the existence of a label. For example, `labels."priority":*`.

  
  
## Hl7V2StoreMetrics

List of metrics for a given HL7v2 store.

Fields  
---  
`name` |  `string` The resource name of the HL7v2 store to get metrics for, in the format `projects/{project_id}/datasets/{dataset_id}/hl7V2Stores/{hl7v2_store_id}`.  
`metrics[]` |  ``[Hl7V2StoreMetric](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Hl7V2StoreMetrics.Hl7V2StoreMetric)`` List of HL7v2 store metrics by message type.  
  
## Hl7V2StoreMetric

Count of messages and total storage size by type for a given HL7 store.

Fields  
---  
`message_type` |  `string` The Hl7v2 message type this metric applies to, such as `ADT` or `ORU`.  
`count` |  `int64` The total count of HL7v2 messages in the store for the given message type.  
`structured_storage_size_bytes` |  `int64` The total amount of structured storage used by HL7v2 messages of this message type in the store.  
  
## ImportMessagesRequest

Request to import messages.

Fields  
---  
`name` |  `string` Required. The name of the target HL7v2 store, in the format `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/hl7v2Stores/{hl7v2_store_id}` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `healthcare.hl7v2Stores.import`

  
Union field `source`. Specifies the import source and configuration.To enable the Cloud Healthcare API to read from resources in your project such as Cloud Storage buckets, you must give the consumer Cloud Healthcare API service account the proper permissions. The service account is: `service-{PROJECT_NUMBER}@gcp-sa-healthcare.iam.gserviceaccount.com`. The `PROJECT_NUMBER` identifies the project that contains the target HL7v2 store. To get the project number, go to the Cloud Console Dashboard. `source` can be only one of the following:  
`gcs_source` |  ``[GcsSource](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.GcsSource)`` Cloud Storage source data location and import configuration.The Cloud Healthcare Service Agent requires the `roles/storage.objectViewer` Cloud IAM roles on the Cloud Storage location.  
  
## ImportMessagesResponse

This type has no fields.

Final response of importing messages. This structure is included in the `[response](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.longrunning#google.longrunning.Operation.FIELDS.google.protobuf.Any.google.longrunning.Operation.response)` to describe the detailed outcome. It is only included when the operation finishes successfully.

## IngestMessageErrorDetail

Contains the HL7v2 NACK message for ingest message failure.

Fields  
---  
`hl7_nack` |  `bytes` HL7v2 NACK message.  
  
## IngestMessageRequest

Ingests a message into the specified HL7v2 store.

Fields  
---  
`parent` |  `string` Required. The name of the HL7v2 store this message belongs to. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `healthcare.hl7V2Messages.ingest`

  
`message` |  ``[Message](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Message)`` Required. HL7v2 message to ingest.  
  
## IngestMessageResponse

Acknowledges that a message has been ingested into the specified HL7v2 store.

Fields  
---  
`hl7_ack` |  `bytes` HL7v2 ACK message.  
`message` |  ``[Message](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Message)`` Created message resource.  
  
## ListHl7V2StoresRequest

Lists the HL7v2 stores in the given dataset.

Fields  
---  
`parent` |  `string` Required. Name of the dataset. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `healthcare.hl7V2Stores.list`

  
`page_size` |  `int32` Limit on the number of HL7v2 stores to return in a single response. If not specified, 100 is used. May not be larger than 1000.  
`page_token` |  `string` The next_page_token value returned from the previous List request, if any.  
`filter` |  `string` Restricts stores returned to those matching a filter. The following syntax is available:

  * A string field value can be written as text inside quotation marks, for example `"query text"`. The only valid relational operation for text fields is equality (`=`), where text is searched within the field, rather than having the field be equal to the text. For example, `"Comment = great"` returns messages with `great` in the comment field.
  * A number field value can be written as an integer, a decimal, or an exponential. The valid relational operators for number fields are the equality operator (`=`), along with the less than/greater than operators (`<`, `<=`, `>`, `>=`). Note that there is no inequality (`!=`) operator. You can prepend the `NOT` operator to an expression to negate it.
  * A date field value must be written in `yyyy-mm-dd` form. Fields with date and time use the RFC3339 time format. Leading zeros are required for one-digit months and days. The valid relational operators for date fields are the equality operator (`=`) , along with the less than/greater than operators (`<`, `<=`, `>`, `>=`). Note that there is no inequality (`!=`) operator. You can prepend the `NOT` operator to an expression to negate it.
  * Multiple field query expressions can be combined in one query by adding `AND` or `OR` operators between the expressions. If a boolean operator appears within a quoted string, it is not treated as special, it's just another part of the character string to be matched. You can prepend the `NOT` operator to an expression to negate it.

Only filtering on labels is supported. For example, `labels.key=value`.  
  
## ListHl7V2StoresResponse

Lists the HL7v2 stores in the given dataset.

Fields  
---  
`hl7_v2_stores[]` |  ``[Hl7V2Store](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Hl7V2Store)`` The returned HL7v2 stores. Won't be more HL7v2 stores than the value of page_size in the request.  
`next_page_token` |  `string` Token to retrieve the next page of results or empty if there are no more results in the list.  
  
## ListMessagesRequest

Lists the messages in the specified HL7v2 store.

Fields  
---  
`parent` |  `string` Required. Name of the HL7v2 store to retrieve messages from. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `healthcare.hl7V2Messages.list`

  
`page_size` |  `int32` Limit on the number of messages to return in a single response. If not specified, 100 is used. May not be larger than 1000.  
`page_token` |  `string` The next_page_token value returned from the previous List request, if any.  
`filter` |  `string` Restricts messages returned to those matching a filter. The following syntax is available:

  * A string field value can be written as text inside quotation marks, for example `"query text"`. The only valid relational operation for text fields is equality (`=`), where text is searched within the field, rather than having the field be equal to the text. For example, `"Comment = great"` returns messages with `great` in the comment field.
  * A number field value can be written as an integer, a decimal, or an exponential. The valid relational operators for number fields are the equality operator (`=`), along with the less than/greater than operators (`<`, `<=`, `>`, `>=`). Note that there is no inequality (`!=`) operator. You can prepend the `NOT` operator to an expression to negate it.
  * A date field value must be written in `yyyy-mm-dd` form. Fields with date and time use the RFC3339 time format. Leading zeros are required for one-digit months and days. The valid relational operators for date fields are the equality operator (`=`) , along with the less than/greater than operators (`<`, `<=`, `>`, `>=`). Note that there is no inequality (`!=`) operator. You can prepend the `NOT` operator to an expression to negate it.
  * Multiple field query expressions can be combined in one query by adding `AND` or `OR` operators between the expressions. If a boolean operator appears within a quoted string, it is not treated as special, it's just another part of the character string to be matched. You can prepend the `NOT` operator to an expression to negate it.

Fields/functions available for filtering are:

  * `message_type`, from the MSH-9.1 field. For example, `NOT message_type = "ADT"`.
  * `send_date` or `sendDate`, the YYYY-MM-DD date the message was sent in the dataset's time_zone, from the MSH-7 segment. For example, `send_date < "2017-01-02"`.
  * `send_time`, the timestamp when the message was sent, using the RFC3339 time format for comparisons, from the MSH-7 segment. For example, `send_time < "2017-01-02T00:00:00-05:00"`.
  * `create_time`, the timestamp when the message was created in the HL7v2 store. Use the RFC3339 time format for comparisons. For example, `create_time < "2017-01-02T00:00:00-05:00"`.
  * `send_facility`, the care center that the message came from, from the MSH-4 segment. For example, `send_facility = "ABC"`.
  * `PatientId(value, type)`, which matches if the message lists a patient having an ID of the given value and type in the PID-2, PID-3, or PID-4 segments. For example, `PatientId("123456", "MRN")`.
  * `labels.x`, a string value of the label with key `x` as set using the `[Message.labels](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Message.FIELDS.repeated.google.cloud.healthcare.v1.hl7v2.Message.LabelsEntry.google.cloud.healthcare.v1.hl7v2.Message.labels)` map. For example, `labels."priority"="high"`. The operator `:*` can be used to assert the existence of a label. For example, `labels."priority":*`.

  
`order_by` |  `string` Orders messages returned by the specified order_by clause. Syntax: <https://cloud.google.com/apis/design/design_patterns#sorting_order>Fields available for ordering are:

  * `send_time`

  
`view` |  ``[MessageView](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.MessageView)`` Specifies the parts of the Message to return in the response. When unspecified, equivalent to BASIC. Setting this to anything other than BASIC with a `page_size` larger than the default can generate a large response, which impacts the performance of this method.  
  
## ListMessagesResponse

Lists the messages in the specified HL7v2 store.

Fields  
---  
`hl7_v2_messages[]` |  ``[Message](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Message)`` The returned Messages. Won't be more Messages than the value of page_size in the request. See `[view](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.ListMessagesRequest.FIELDS.google.cloud.healthcare.v1.hl7v2.MessageView.google.cloud.healthcare.v1.hl7v2.ListMessagesRequest.view)` for populated fields.  
`next_page_token` |  `string` Token to retrieve the next page of results or empty if there are no more results in the list.  
  
## Message

A complete HL7v2 message. See [Introduction to HL7 Standards](https://www.hl7.org/implement/standards/index.cfm?ref=common) for details on the standard.

Fields  
---  
`name` |  `string` Output only. Resource name of the Message, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/hl7V2Stores/{hl7_v2_store_id}/messages/{message_id}`. Assigned by the server.  
`data` |  `bytes` Required. Raw message bytes.  
`create_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` Output only. The datetime when the message was created. Set by the server.  
`send_facility` |  `string` The hospital that this message came from. MSH-4.  
`send_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` The datetime the sending application sent this message. MSH-7.  
`message_type` |  `string` The message type for this message. MSH-9.1.  
`patient_ids[]` |  ``[PatientId](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1#google.cloud.healthcare.v1.PatientId)`` All patient IDs listed in the PID-2, PID-3, and PID-4 segments of this message.  
`labels` |  `map<string, string>` User-supplied key-value pairs used to organize HL7v2 stores.Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\p{Ll}\p{Lo}][\p{Ll}\p{Lo}\p{N}_-]{0,62}Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\p{Ll}\p{Lo}\p{N}_-]{0,63}No more than 64 labels can be associated with a given store.  
`parsed_data` |  ``[ParsedData](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.ParsedData)`` Output only. The parsed version of the raw message data.  
`schematized_data` |  ``[SchematizedData](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.SchematizedData)`` The parsed version of the raw message data schematized according to this store's schemas and type definitions.  
  
## MessageView

Enums  
---  
`MESSAGE_VIEW_UNSPECIFIED` | Not specified, equivalent to FULL.  
`RAW_ONLY` | Server responses include all the message fields except parsed_data field, and schematized_data fields.  
`PARSED_ONLY` | Server responses include all the message fields except data field, and schematized_data fields.  
`FULL` | Server responses include all the message fields.  
`SCHEMATIZED_ONLY` | Server responses include all the message fields except data and parsed_data fields.  
`BASIC` | Server responses include only the name field.  
  
## ParsedData

The content of a HL7v2 message in a structured format.

Fields  
---  
`segments[]` |  ``[Segment](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Segment)``  
  
## ParserConfig

The configuration for the parser. It determines how the server parses the messages.

Fields  
---  
`allow_null_header` |  `bool` Determines whether messages with no header are allowed.  
`segment_terminator` |  `bytes` Byte(s) to use as the segment terminator. If this is unset, '\r' is used as segment terminator, matching the HL7 version 2 specification.  
`schema` |  ``[SchemaPackage](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.SchemaPackage)`` Schemas used to parse messages in this store, if schematized parsing is desired.  
`version` |  ``[ParserVersion](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.ParserConfig.ParserVersion)`` Immutable. Determines the version of both the default parser to be used when `schema` is not given, as well as the schematized parser used when `schema` is specified. This field is immutable after HL7v2 store creation.  
  
## ParserVersion

The parser version. Applies to both the default parser and the schematized parser. The highest version of the parser is recommended.

Enums  
---  
`PARSER_VERSION_UNSPECIFIED` | Unspecified parser version, equivalent to V1.  
`V1` | The `parsed_data` includes every given non-empty message field except the Field Separator (MSH-1) field. As a result, the parsed MSH segment starts with the MSH-2 field and the field numbers are off-by-one with respect to the HL7 standard.  
`V2` | The `parsed_data` includes every given non-empty message field.  
`V3` | This version is the same as V2, with the following change.The `parsed_data` contains unescaped escaped field separators, component separators, sub-component separators, repetition separators, escape characters, and truncation characters.If `schema` is specified, the schematized parser uses improved parsing heuristics compared to previous versions.  
  
## PubsubDestination

The Pub/Sub output destination.

The Cloud Healthcare Service Agent requires the `roles/pubsub.publisher` Cloud IAM role on the Pub/Sub topic.

Fields  
---  
`pubsub_topic` |  `string` The [Pub/Sub](https://cloud.google.com/pubsub/docs/) topic that Pub/Sub messages are published on. Supplied by the client.The `PubsubMessage` contains the following fields:

  * `PubsubMessage.Data` contains the resource name.
  * `PubsubMessage.MessageId` is the ID of this notification. It is guaranteed to be unique within the topic.
  * `PubsubMessage.PublishTime` is the time when the message was published.

[Topic names](https://cloud.google.com/pubsub/docs/overview#names) must be scoped to a project.The Cloud Healthcare API service account, [service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com](mailto:service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com), must have publisher permissions on the given Pub/Sub topic. Not having adequate permissions causes the calls that send notifications to fail.  
  
## SchemaGroup

An HL7v2 logical group construct.

Fields  
---  
`name` |  `string` The name of this group. For example, "ORDER_DETAIL".  
`choice` |  `bool` True indicates that this is a choice group, meaning that only one of its segments can exist in a given message.  
`min_occurs` |  `int32` The minimum number of times this group must be present/repeated.  
`max_occurs` |  `int32` The maximum number of times this group can be repeated. 0 or -1 means unbounded.  
`members[]` |  ``[GroupOrSegment](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.GroupOrSegment)`` Nested groups and/or segments.  
  
## SchemaPackage

A schema package contains a set of schemas and type definitions.

Fields  
---  
`schematized_parsing_type` |  ``[SchematizedParsingType](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.SchematizedParsingType)`` Determines how messages that fail to parse are handled.  
`schemas[]` |  ``[Hl7SchemaConfig](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Hl7SchemaConfig)`` Schema configs that are layered based on their VersionSources that match the incoming message. Schema configs present in higher indices override those in lower indices with the same message type and trigger event if their VersionSources all match an incoming message.  
`types[]` |  ``[Hl7TypesConfig](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Hl7TypesConfig)`` Schema type definitions that are layered based on their VersionSources that match the incoming message. Type definitions present in higher indices override those in lower indices with the same type name if their VersionSources all match an incoming message.  
`ignore_min_occurs` |  `bool` Flag to ignore all min_occurs restrictions in the schema. This means that incoming messages can omit any group, segment, field, component, or subcomponent.  
`unexpected_segment_handling` |  ``[UnexpectedSegmentHandlingMode](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.SchemaPackage.UnexpectedSegmentHandlingMode)`` Determines how unexpected segments (segments not matched to the schema) are handled.  
  
## UnexpectedSegmentHandlingMode

Determines how unexpected segments are handled. An unexpected segment is a segment that is present in a message but has no corresponding match in the message type definition.

Enums  
---  
`UNEXPECTED_SEGMENT_HANDLING_MODE_UNSPECIFIED` | Unspecified handling mode, equivalent to FAIL.  
`FAIL` | Unexpected segments fail to parse and return an error.  
`SKIP` | Unexpected segments do not fail, but are omitted from the output.  
`PARSE` | Unexpected segments do not fail, but are parsed in place and added to the current group. If a segment has a type definition, it is used, otherwise it is parsed as VARIES.  
  
## SchemaSegment

An HL7v2 Segment.

Fields  
---  
`type` |  `string` The Segment type. For example, "PID".  
`min_occurs` |  `int32` The minimum number of times this segment can be present in this group.  
`max_occurs` |  `int32` The maximum number of times this segment can be present in this group. 0 or -1 means unbounded.  
  
## SchematizedData

The content of an HL7v2 message in a structured format as specified by a schema.

Fields  
---  
Union field `result`.`result` can be only one of the following:  
`data` |  `string` JSON output of the parser.  
`error` |  `string` The error output of the parser.  
  
## SchematizedParsingType

Determines the failure mode for schematized parsing.

Enums  
---  
`SCHEMATIZED_PARSING_TYPE_UNSPECIFIED` | Unspecified schematized parsing type, equivalent to `SOFT_FAIL`.  
`SOFT_FAIL` | Messages that fail to parse are still stored and ACKed but a parser error is stored in place of the schematized data.  
`HARD_FAIL` | Messages that fail to parse are rejected from ingestion/insertion and return an error code.  
  
## Segment

A segment in a structured format.

Fields  
---  
`segment_id` |  `string` A string that indicates the type of segment. For example, EVN or PID.  
`set_id` |  `string` Set ID for segments that can be in a set. This can be empty if it's missing or isn't applicable.  
`fields` |  `map<string, string>` A mapping from the positional location to the value. The key string uses zero-based indexes separated by dots to identify Fields, components and sub-components. A bracket notation is also used to identify different instances of a repeated field. Regex for key: (\d+)([\d+])?(.\d+)?(.\d+)?Examples of (key, value) pairs:

  * (0.1, "hemoglobin") denotes that the first component of Field 0 has the value "hemoglobin".
  * (1.1.2, "CBC") denotes that the second sub-component of the first component of Field 1 has the value "CBC".
  * (1[0].1, "HbA1c") denotes that the first component of the first Instance of Field 1, which is repeated, has the value "HbA1c".

  
  
## Type

A type definition for some HL7v2 type (incl. Segments and Datatypes).

Fields  
---  
`name` |  `string` The name of this type. This would be the segment or datatype name. For example, "PID" or "XPN".  
`primitive` |  ``[Primitive](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Type.Primitive)`` If this is a primitive type then this field is the type of the primitive For example, STRING. Leave unspecified for composite types.  
`fields[]` |  ``[Field](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Type.Field)`` The (sub) fields this type has (if not primitive).  
  
## Field

A (sub) field of a type.

Fields  
---  
`name` |  `string` The name of the field. For example, "PID-1" or just "1".  
`type` |  `string` The type of this field. A Type with this name must be defined in an Hl7TypesConfig.  
`table` |  `string` The HL7v2 table this field refers to. For example, PID-15 (Patient's Primary Language) usually refers to table "0296".  
`min_occurs` |  `int32` The minimum number of times this field must be present/repeated.  
`max_occurs` |  `int32` The maximum number of times this field can be repeated. 0 or -1 means unbounded.  
  
## Primitive

Enums  
---  
`PRIMITIVE_UNSPECIFIED` | Not a primitive.  
`STRING` | String primitive.  
`VARIES` | Element that can have unschematized children.  
`UNESCAPED_STRING` | Like STRING, but all delimiters below this element are ignored.  
  
## UpdateHl7V2StoreRequest

Request to update the given HL7v2 store. For example, to change the Cloud Pub/Sub topic.

Fields  
---  
`hl7_v2_store` |  ``[Hl7V2Store](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Hl7V2Store)`` Required. The HL7v2 store to update. Only fields listed in `update_mask` are applied. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `hl7V2Store`:

  * `healthcare.hl7V2Stores.update`

  
`update_mask` |  ``[FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask)`` Required. The update mask applies to the resource. For the `FieldMask` definition, see <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask>  
  
## UpdateMessageRequest

Request to update labels on the given message.

Fields  
---  
`message` |  ``[Message](https://docs.cloud.google.com/healthcare-api/docs/reference/rpc/google.cloud.healthcare.v1/hl7v2#google.cloud.healthcare.v1.hl7v2.Message)`` Required. The message resource which updates the resource on the server. Only fields listed in `update_mask` are applied. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `message`:

  * `healthcare.hl7V2Messages.update`

  
`update_mask` |  ``[FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask)`` Required. The update mask applies to the resource. For the `FieldMask` definition, see <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask>  
  
## VersionSource

Describes a selector for extracting and matching an MSH field to a value.

Fields  
---  
`msh_field` |  `string` The field to extract from the MSH segment. For example, "3.1" or "18[1].1".  
`value` |  `string` The value to match with the field. For example, "My Application Name" or "2.3".  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
