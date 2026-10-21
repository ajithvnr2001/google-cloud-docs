---
url: https://docs.cloud.google.com/eventarc/docs/cloudevents-json/
title: CloudEvents - JSON event format \u00a0|\u00a0 Eventarc \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:40:57.490318+00:00
---

# CloudEvents - JSON event format  |  Eventarc  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/docs/cloudevents-json/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Reference ](https://docs.cloud.google.com/eventarc/docs/apis)



Send feedback 

#  CloudEvents - JSON event format Stay organized with collections  Save and categorize content based on your preferences. 

[ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs/overview) [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

CloudEvents ([cloudevents.io](http://cloudevents.io)) is a specification for describing event data in a common way. The specification is under the Cloud Native Computing Foundation (CNCF) and is organized by the CNCF's Serverless Working Group.

Eventarc delivers events to the event receiver in the CloudEvents format through an HTTP request. The destination target—for example, the Workflows service—converts the event to a JSON object (following the CloudEvents specification) and passes the event into the workflow execution as a workflow runtime argument.

##  JSON payload format 

The destination service receives events from event routers and formats the events to the [JSON Event Format for CloudEvents version 1.0.1](https://github.com/cloudevents/spec/blob/v1.0.1/json-format.md#json-event-format-for-cloudevents---version-101) with the following CloudEvents attributes:

Attribute | Description | Example  
---|---|---  
data | The payload of the event data. | 
    
    
    {
      "subscription": "projects/my-project/subscriptions/my-sub",
      "message": {
        "attributes": {
          "attr1":"attr1-value"
        },
        "data": "aGVsbG8gd29ybGQ=",
        "messageId": "2070443601311540",
        "publishTime":"2021-02-26T19:13:55.749Z"
      }
    }  
  
datacontenttype | The type of data that has been passed | `application/json`  
id | The unique identifier for the event | `2070443601311540`  
source | The source of the event | `//pubsub.googleapis.com/projects/my-project/topics/my-topic`  
specversion | The CloudEvents specification version used for this event | 1.0  
type | The type of event data | `google.cloud.pubsub.topic.v1.messagePublished`  
time | Event generation time, in [RFC 3339](https://tools.ietf.org/html/rfc3339) format (optional) | `2020-12-20T13:37:33.647Z`  
  
Depending on the event type, the payload format is as follows:

###  Cloud Audit Logs 

The runtime argument is a JSON object detailing the Cloud Audit Logs event. In this document, see the [Common events example](https://docs.cloud.google.com/eventarc/docs/cloudevents-json#common-events). In the JSON object, you can find the `resourceName`, `serviceName`, and `methodName` values. For more information, see [Determine event filters for Cloud Audit Logs](https://docs.cloud.google.com/eventarc/docs/determining-filters-cal).

Events of type `google.cloud.audit.log.v1.written` have the following format:
    
    
    {
      "data":{ EVENT_DATA },
      "datacontenttype": "application/json; charset=utf-8",
      "id": "MESSAGE_ID",
      "source": "//cloudaudit.googleapis.com/projects/PROJECT_ID/logs/data_access",
      "specversion": "1.0",
      "type": "google.cloud.audit.log.v1.written",
      "time": "EVENT_GENERATION_TIME",
      "dataschema": "https://googleapis.github.io/google-cloudevents/jsonschema/google/events/cloud/audit/v1/LogEntryData.json",
      "methodName": "jobservice.jobcompleted",
      "resourceName": "projects/my-project/jobs/bqjob_r3ac45813612fa2d6_0000017d591922c9_1",
      "serviceName": "bigquery.googleapis.com",
      "subject": "bigquery.googleapis.com/projects/my-project/jobs/bqjob_r3ac45813612fa2d6_0000017d591922c9_1"
    }

  * `EVENT_DATA`: the decoded message content in JSON format. For more information, in this document, see Common events.
  * `MESSAGE_ID`, `EVENT_GENERATION_TIME`: system-generated.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `dataschema`, `methodName`, `resourceName`, `serviceName`, `subject`: attributes specific to the event type.



###  Cloud Storage 

The runtime arguments are changes to Cloud Storage. In the `data` field you can find the change in the Cloud Storage bucket. In this document, see the [Common events example](https://docs.cloud.google.com/eventarc/docs/cloudevents-json#common-events).

Events of type `google.cloud.storage.object.v1.finalized` have the following format:
    
    
    {
      "data":{ EVENT_DATA },
      "datacontenttype": "application/json",
      "id": "MESSAGE_ID",
      "source": "//storage.googleapis.com/projects/_/buckets/BUCKET_NAME",
      "specversion": "1.0",
      "type": "google.cloud.storage.object.v1.finalized",
      "time": "EVENT_GENERATION_TIME",
      "subject": "objects/my-file.txt"
    }

  * `EVENT_DATA`: the decoded message content in JSON format. For more information, in this document, see Common events.
  * `MESSAGE_ID`, `EVENT_GENERATION_TIME`: system-generated.
  * `BUCKET_NAME`: the name of the Cloud Storage bucket that gets updated.
  * `subject`: attribute specific to the event type.



###  Pub/Sub 

The runtime argument is a Pub/Sub push message. In the `data` field you can find the message as a Base64-encoded string. In this document, see the [Common events example](https://docs.cloud.google.com/eventarc/docs/cloudevents-json#common-events).

Events of type `google.cloud.pubsub.topic.v1.messagePublished` have the following format:
    
    
    {
      "data":{ EVENT_DATA },
      "datacontenttype": "application/json; charset=utf-8",
      "id": "MESSAGE_ID",
      "source": "//pubsub.googleapis.com/TOPIC_NAME",
      "specversion": "1.0",
      "type": "google.cloud.pubsub.topic.v1.messagePublished",
      "time": "EVENT_GENERATION_TIME"
    }

  * `EVENT_DATA`: the decoded message content in JSON format. For more information, in this document, see Common events.
  * `MESSAGE_ID`, `EVENT_GENERATION_TIME`: system-generated.
  * `TOPIC_NAME`: the Pub/Sub topic name to which the event was published to.



## Open source repository

The structure of the HTTP body for all events are available on the [CloudEvents GitHub repository](https://github.com/googleapis/google-cloudevents). 

The repository contains the following to help you understand and use CloudEvents data in your programming language: 

  * Google Protocol Buffers for CloudEvents data payloads
  * Generated JSON schemas
  * A public JSON schema catalog



Links to client libraries are also included. 

## Common events

Protocol Buffers (or protobufs) represent the data within events that are generated by Eventarc. Protocol Buffers for CloudEvents are provided as machine-readable schemas, allowing libraries of data types to be created and making it easier to consume events.

There are two protobuf messages that are relevant for any given CloudEvent type: 

  * The _envelope_ message that represents the complete CloudEvent, including any extension attributes; for example, `AuditLogWrittenEvent`.
  * The _data_ message; for example, `LogEntryData` or `StorageObjectData`.

Many CloudEvent types can use the same data message. For example, every event associated with a Cloud Storage object uses `StorageObjectData` as the data message. Each envelope message specifies the CloudEvent type that it is associated with through a proto annotation. For more information, see [Relationship between protobuf messages and CloudEvent types](https://github.com/googleapis/google-cloudevents/blob/main/proto/README.md#relationship-between-protobuf-messages-and-cloudevent-types). 

The following tables detail the components of some common events: 

### Cloud Audit Logs

Proto files| [google/events/cloud/audit/v1/events.proto](https://github.com/googleapis/google-cloudevents/blob/master/proto/google/events/cloud/audit/v1/events.proto)  
[google/events/cloud/audit/v1/data.proto](https://github.com/googleapis/google-cloudevents/blob/main/proto/google/events/cloud/audit/v1/data.proto)  
---|---  
Envelope message| `google.events.cloud.audit.v1.AuditLogWrittenEvent`  
Data message| `google.events.cloud.audit.v1.LogEntryData`  
Event type  
(when an audit log entry is written) | `google.cloud.audit.log.v1.written`  
Event extensions| 

  * `serviceName`
  * `methodName`
  * `resourceName`

See the list of [event types using Cloud Audit Logs](https://docs.cloud.google.com/eventarc/docs/event-types#using-cloud-audit-logs).   
Examples|  [Pub/Sub audit log](https://googleapis.github.io/google-cloudevents/examples/binary/audit/LogEntryData-pubsubCreateTopic.json)  
[BigQuery audit log](https://googleapis.github.io/google-cloudevents/examples/structured/audit/LogEntryData-bigqueryjobcompleted.json)  
More information|  [Create an Eventarc trigger for a Cloud Audit Logs event](https://docs.cloud.google.com/eventarc/docs/event-providers-targets#triggers)  
[Determine event filters for Cloud Audit Logs](https://docs.cloud.google.com/eventarc/docs/determining-filters-cal)  
[Google Cloud services with audit logs](https://docs.cloud.google.com/logging/docs/audit/services)  
  
### Cloud Storage

Proto files|  [google/events/cloud/storage/v1/events.proto](https://github.com/googleapis/google-cloudevents/blob/master/proto/google/events/cloud/storage/v1/events.proto)  
[google/events/cloud/storage/v1/data.proto](https://github.com/googleapis/google-cloudevents/blob/main/proto/google/events/cloud/storage/v1/data.proto)  
---|---  
Envelope messages| `google.events.cloud.storage.v1.ObjectFinalizedEvent`  
`google.events.cloud.storage.v1.ObjectArchivedEvent`  
`google.events.cloud.storage.v1.ObjectDeletedEvent`  
`google.events.cloud.storage.v1.ObjectMetadataUpdatedEvent `  
  
Data message| `google.events.cloud.storage.v1.StorageObjectData`  
Resource|  [`Objects` ](https://docs.cloud.google.com/storage/docs/json_api/v1/objects)  
Event types  
| See the list of [direct event types](https://docs.cloud.google.com/eventarc/docs/event-types#cloud-storage).   
Examples|  [Simple](https://googleapis.github.io/google-cloudevents/examples/binary/storage/StorageObjectData-simple.json)  
[Complex](https://googleapis.github.io/google-cloudevents/examples/binary/storage/StorageObjectData-complex.json)  
More information|  [Create an Eventarc trigger for a Cloud Storage event](https://docs.cloud.google.com/eventarc/docs/event-providers-targets#triggers)  
[Receive events from Cloud Storage in a Cloud Run service](https://docs.cloud.google.com/eventarc/standard/docs/run/create-trigger-storage-console)  
  
### Firestore

Proto files|  [google/events/cloud/firestore/v1/events.proto](https://github.com/googleapis/google-cloudevents/blob/master/proto/google/events/cloud/firestore/v1/events.proto)  
[google/events/cloud/firestore/v1/data.proto](https://github.com/googleapis/google-cloudevents/blob/main/proto/google/events/cloud/firestore/v1/data.proto)  
---|---  
Envelope messages| `google.events.cloud.firestore.v1.DocumentCreatedEvent`  
`google.events.cloud.firestore.v1.DocumentUpdatedEvent`  
`google.events.cloud.firestore.v1.DocumentDeletedEvent`  
`google.events.cloud.firestore.v1.DocumentWrittenEvent`  
  
Data message| `google.events.cloud.firestore.v1.DocumentEventData`  
Resource|  [`Document`](https://docs.cloud.google.com/firestore/docs/reference/rest/v1/projects.databases.documents)  
Event types | See the list of [direct event types](https://docs.cloud.google.com/eventarc/docs/event-types#cloud-firestore).   
Examples|  [Simple](https://googleapis.github.io/google-cloudevents/examples/binary/firestore/DocumentEventData-simple.json)  
[Complex](https://googleapis.github.io/google-cloudevents/examples/binary/firestore/DocumentEventData-complex.json)  
More information|  [Create an Eventarc trigger for a Firestore event](https://docs.cloud.google.com/eventarc/docs/event-providers-targets#triggers)  
[Create event-driven architectures with Eventarc and Firestore](https://docs.cloud.google.com/firestore/docs/eventarc)  
[Extend with Cloud Run functions to handle events triggered by changes in Firestore](https://docs.cloud.google.com/firestore/docs/extend-with-functions-2nd-gen)  
  
### Pub/Sub

Proto files|  [google/events/cloud/pubsub/v1/events.proto](https://github.com/googleapis/google-cloudevents/blob/master/proto/google/events/cloud/pubsub/v1/events.proto)  
[google/events/cloud/pubsub/v1/data.proto](https://github.com/googleapis/google-cloudevents/blob/main/proto/google/events/cloud/pubsub/v1/data.proto)  
---|---  
Envelope message| `google.events.cloud.pubsub.v1.MessagePublishedEvent`  
Data message| `google.events.cloud.pubsub.v1.MessagePublishedData`  
Resource|  [`PubsubMessage`](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage)  
Event type  
(when a Pub/Sub message is published) | `google.cloud.pubsub.topic.v1.messagePublished`  
Example|  [Text](https://googleapis.github.io/google-cloudevents/examples/binary/pubsub/MessagePublishedData-complex.json)  
More information|  [Receive events in a Cloud Run service using Pub/Sub messages](https://docs.cloud.google.com/eventarc/standard/docs/run/create-trigger-pub-sub-gcloud)  
[Trigger a workflow using Pub/Sub messages](https://docs.cloud.google.com/eventarc/standard/docs/workflows/quickstart-pubsub)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
