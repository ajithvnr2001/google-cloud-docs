---
url: https://docs.cloud.google.com/healthcare-api/docs/hl7v2-pubsub-export/
title: Export HL7v2 messages to Pub/Sub \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:59.760806+00:00
---

# Export HL7v2 messages to Pub/Sub  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/hl7v2-pubsub-export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Export HL7v2 messages to Pub/Sub Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to export HL7v2 messages to Pub/Sub using the [`projects.locations.datasets.hl7V2Stores.export`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/export) method.

You can export HL7v2 messages to Pub/Sub for downstream processing. Suppose you have a Dataflow pipeline that transforms HL7v2 messages when new messages are ingested into an HL7v2 store. The pipeline reads from a Pub/Sub subscription and waits for notifications of new HL7v2 messages. When you import HL7v2 messages into an HL7v2 store using the [`hl7V2Stores.import`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/import) method, the method doesn't send [Pub/Sub notifications](https://docs.cloud.google.com/healthcare-api/docs/how-tos/pubsub). To trigger the pipeline, import the HL7v2 messages and then use the `hl7v2Stores.export` method to export them to Pub/Sub.

## Before you begin

### Enable the Pub/Sub API

In the Google Cloud console, enable the Pub/Sub API:

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=pubsub)

### Configure Pub/Sub permissions

To export messages from an HL7v2 store to Pub/Sub, you must add the `pubsub.publisher` role to your project's **Cloud Healthcare Service Agent** [service account](https://docs.cloud.google.com/iam/docs/service-accounts). See [DICOM, FHIR, and HL7v2 store Pub/Sub permissions](https://docs.cloud.google.com/healthcare-api/docs/how-tos/permissions-healthcare-api-gcp-products#dicom_fhir_and_hl7v2_store_cloud_pubsub_permissions) for steps to add the required role.

### Create a Pub/Sub topic

To create a topic, see [Create a topic](https://docs.cloud.google.com/pubsub/docs/create-topic#create_a_topic).

Individual data stores can have their own Pub/Sub topic, or multiple data stores can share the same topic.

Use the following format when specifying the Pub/Sub topic:
    
    
    projects/PROJECT_ID/topics/TOPIC_NAME

`PROJECT_ID` is your Google Cloud project ID and `TOPIC_NAME` is the name of the Pub/Sub topic.

## Export HL7v2 messages to Pub/Sub

### curl

To export HL7v2 messages to Pub/Sub, make a `POST` request and specify the following information:

  * The name of the parent dataset
  * The name of the HL7v2 store
  * The destination Pub/Sub topic



The following sample shows a `POST` request using `curl`.
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        --data "{
          'pubsubDestination': {
            'pubsubTopic': 'projects/PROJECT_ID/topics/PUBSUB_TOPIC'
          }
        }" "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID:export"

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
    }
    

The response contains an operation name. To track the status of the operation, you can use the [Operation `get` method](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get):
    
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"

If the request is successful, the server returns a response with the status of the operation in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.hl7v2.Hl7V2Service.ExportMessages",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "counter": {
          "success": "RESOURCE_COUNT"
        }
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.hl7v2.ExportMessagesResponse"
      }
    }
    

### Export a subset of HL7v2 messages using a filter

You can use the following fields in your filter criteria:

  * [`startTime`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/export#body.request_body.FIELDS.start_time)
  * [`endTime`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/export#body.request_body.FIELDS.end_time).



You can specify the following filter parameters as your filter criteria in the [`filter`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/export#body.request_body.FIELDS.filter) field. To learn the filter syntax and construct queries, see [Query strings](https://docs.cloud.google.com/appengine/docs/standard/python/search/query_strings).

  * `message_type`: from the MSH.9.1 field. For example, `NOT message_type = "ADT"`.
  * `send_date`: the `YYYY-MM-DD` date the message was sent from the MSH.7 segment, specified in the time zone of the dataset. For example, `send_date < "2017-01-02"`.
  * `send_time`: the timestamp when the message was sent. This parameter is from the MSH.7 segment of the message. This parameter uses the [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339) time format for comparisons. For example, `send_time < "2017-01-02T00:00:00-05:00"`.
  * `create_time`: the timestamp when the message was created in the Cloud Healthcare API, using the RFC 3339 time format for comparisons. For example: `create_time < "2017-01-02T00:00:00-05:00"`.
  * `send_facility`: the care center that the message came from, from the MSH.4 segment. For example, `send_facility = "ABC"`.

**Note:** Filtering with `startTime` and `endTime` is more efficient than specifying a filter using `send_time`. A filter created using the `startTime` and `endTime` fields defines a range of HL7v2 messages to which the filter is applied. A `send_time` filter only applies to HL7v2 messages with the exact send time.

The following samples show how to specify a filter to only export HL7v2 messages of type `ADT`.

### curl
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        --data "{
          'pubsubDestination': {
            'pubsubTopic': 'projects/PROJECT_ID/topics/PUBSUB_TOPIC'
          },
          'filter': 'message_type = \"ADT\"'
        }" "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID:export"

### View exported HL7v2 messages in Pub/Sub

To view the exported HL7v2 messages in Pub/Sub, run the [`gcloud pubsub subscriptions pull`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/pull) command. The command uses the `--format=json` flag to return the output as JSON instead of the default YAML.
    
    
    gcloud pubsub subscriptions pull --auto-ack projects/PROJECT_ID/subscriptions/PUBSUB_SUBSCRIPTION \
        --format=json

  * `PROJECT_ID` is the ID of your Google Cloud project
  * `PUBSUB_SUBSCRIPTION` is the subscription attached to the Pub/Sub topic where you exported HL7v2 messages



The output is the following:
    
    
    [
      {
        "ackId": "ACK_ID",
        "message": {
          "attributes": {
            "msgType": "TYPE"
          },
          "data": "DATA",
          "messageId": "8076570784126536",
          "publishTime": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ"
        }
      }
    ]
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
