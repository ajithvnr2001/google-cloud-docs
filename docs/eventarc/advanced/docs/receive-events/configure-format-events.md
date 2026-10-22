---
url: https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/configure-format-events/
title: Format received events \u00a0|\u00a0 Eventarc Advanced \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:29.705539+00:00
---

# Format received events  |  Eventarc Advanced  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/configure-format-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/advanced/docs/overview)



Send feedback 

#  Format received events Stay organized with collections  Save and categorize content based on your preferences. 

[ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs/overview)

A pipeline connects a bus to a target destination, and routes event messages to that destination. You can configure a pipeline to expect event data in a specific format or, before events are delivered to a destination, you can convert event data from one supported format to another. For example, you might need to route events to an endpoint that only accepts Avro data.

## Supported formats

The following format conversions are supported:

  * Avro to JSON
  * Avro to Protobuf
  * JSON to Avro
  * JSON to Protobuf
  * Protobuf to Avro
  * Protobuf to JSON



#### Note the following:

  * When you convert the format of events, _only_ the event payload is converted and not the entire event message.

  * If an inbound data format is specified for a pipeline, all events must match that format. Any events that don't match the expected format are treated as [persistent errors](https://docs.cloud.google.com/eventarc/advanced/docs/retry-events#persistent).

  * If an inbound data format is _not_ specified for a pipeline, an outbound format _can't_ be set.

  * Before an event format is converted for a specific destination, any [data transformation](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events) that is configured is applied first.

  * Events are always delivered in a [CloudEvents format using an HTTP request in binary content mode](https://docs.cloud.google.com/eventarc/docs/cloudevents) unless you specify a [message binding](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events#message-binding).

  * JSON schemas are detected dynamically. For Protobuf schema definitions, you can define only one top-level type and import statements that refer to other types are not supported. Schema definitions without a `syntax` identifier default to `proto2`. Note that there is a [schema size limit](https://docs.cloud.google.com/eventarc/docs/quotas#limits).




## Configure a pipeline to format events

You can configure a pipeline to expect event data in a specific format, or to convert event data from one format to another, in the Google Cloud console or by using the gcloud CLI.

### Console

  1. In the Google Cloud console, go to the **Eventarc** > **Pipelines** page.

[Go to Pipelines](https://console.cloud.google.com/eventarc/pipelines)

  2. You can [create a pipeline](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/create-enrollment#console) or, if you are updating a pipeline, click the name of the pipeline.

  3. In the **Pipeline details** page, click edit **Edit**.

  4. In the **Event mediation** pane, do the following:

     1. Select the **Apply a transformation** checkbox.
     2. In the **Inbound format** list, select the applicable format.

Note that if an inbound data format is specified for a pipeline, all events must match that format. Any events that don't match the expected format are treated as [persistent errors](https://docs.cloud.google.com/eventarc/advanced/docs/retry-events#persistent).

     3. For Avro or Protobuf formats, you must specify an inbound schema. (Optionally, instead of specifying it directly, you can upload an inbound schema.)

     4. In the **CEL expression** field, write a transformation expression [using CEL](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/use-cel).

     5. Click **Continue**.

  5. In the **Destination** pane, do the following:

     1. If applicable, in the **Outbound format** list, select a format.

Note that if an inbound data format is _not_ specified for a pipeline, an outbound format _can't_ be set.

     2. Optional: Apply a **Message binding**. For more information, see [Message binding](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events#message-binding).

  6. Click **Save**.

It can take a couple of minutes to update a pipeline.




###  gcloud 

  1. Open a terminal.

  2. You can [create a pipeline](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/create-enrollment#gcloud) or you can update a pipeline using the [`gcloud eventarc pipelines update`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/pipelines/update) command:
         
         gcloud eventarc pipelines update PIPELINE_NAME \
             --location=REGION \
             --INPUT_PAYLOAD_FLAG \
             --destinations=OUTPUT_PAYLOAD_KEY

**Note:** The `--destinations` flag uses a hash symbol (`#`) as the default delimiter. If your expression contains a hash, specify a different delimiter to avoid parsing conflicts. For more information, see [gcloud topic escaping](https://docs.cloud.google.com/sdk/gcloud/reference/topic/escaping). For example, to use a semicolon (`;`) as a delimiter: `--destinations=^;^OUTPUT_PAYLOAD_KEY`

Replace the following:

     * `PIPELINE_NAME`: the ID of the pipeline or a fully qualified name
     * `REGION`: a [supported Eventarc Advanced location](https://docs.cloud.google.com/eventarc/docs/locations#advanced-regions)

Alternatively, you can set the gcloud CLI location property:
           
           gcloud config set eventarc/location REGION
           

     * `INPUT_PAYLOAD_FLAG`: an input data format flag that can be one of the following:

       * `--input-payload-format-avro-schema-definition`
       * `--input-payload-format-json`
       * `--input-payload-format-protobuf-schema-definition`

Note that if an input data format is specified for a pipeline, all events must match that format. Any events that don't match the expected format are treated as [persistent errors](https://docs.cloud.google.com/eventarc/advanced/docs/retry-events#persistent).

     * `OUTPUT_PAYLOAD_KEY`: an output data format key that can be one of the following:

       * `output_payload_format_avro_schema_definition`
       * `output_payload_format_json`
       * `output_payload_format_protobuf_schema_definition`

Note that if you set an output data format key, you must also specify an input data format flag.

It can take a couple of minutes to update a pipeline.

### Examples:

The following example use an `--input-payload-format-protobuf-schema-definition` flag to specify that the pipeline should expect events in a Protobuf data format with a specific schema:
    
    gcloud eventarc pipelines update my-pipeline \
        --input-payload-format-protobuf-schema-definition \
    '
      syntax = "proto3";
      message schema {
        string name = 1;
        string severity = 2;
      }
    '

The following example uses an `output_payload_format_avro_schema_definition` key and an `--input-payload-format-avro-schema-definition` flag to create a pipeline that expects events in an Avro format and outputs them in the same format:
    
    gcloud eventarc pipelines create my-pipeline \
        --location=us-central1 \
        --destinations=http_endpoint_uri='https://example-endpoint.com',output_payload_format_avro_schema_definition='{"type": "record", "name": "my_record", "fields": [{"name": "my_field", "type": "string"}]}' \
        --input-payload-format-avro-schema-definition='{"type": "record", "name": "my_record", "fields": [{"name": "my_field", "type": "string"}]}'

The following example uses an `output_payload_format_protobuf_schema_definition` key and an `--input-payload-format-avro-schema-definition` flag to update a pipeline and convert its event data from Avro to Protobuf using schema definitions:
    
    gcloud eventarc pipelines update my-pipeline \
        --location=us-central1 \
        --destinations=output_payload_format_protobuf_schema_definition='message MessageProto {string prop1 = 1; string prop2 = 2;}' \
        --input-payload-format-avro-schema-definition= \
        '
        {
          "type": "record",
          "name": "MessageProto",
          "fields": [
            { "name" : "prop1", "type": "string" },
            { "name" : "prop2", "type": "string" },
          ]
        }
        '




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
