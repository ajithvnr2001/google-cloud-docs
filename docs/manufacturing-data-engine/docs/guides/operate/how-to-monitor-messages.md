---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/operate/how-to-monitor-messages/
title: Monitor messages \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:03.301402+00:00
---

# Monitor messages  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/operate/how-to-monitor-messages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Monitor messages

This guide describes how to monitor messages sent to Manufacturing Data Engine (MDE), how they flow through the processing pipeline, and diagnose any issues that might happen because of configuration or potential system issues.

In order to monitor messages flowing through MDE you should use the [operations-log](https://docs.cloud.google.com/manufacturing-data-engine/docs/reference/bigquery-schemas#operations_logs) BigQuery table. Whenever a step of the MDE pipeline fails to process a message, it sends it to the `operations-log` table indicating the step and the failure reason.

All failed messages are written to this table, however, you can configure MDE to also write successful messages to the `operations-log` table. This is useful when debugging issues, but shouldn't be left turned on as it can generate a lot of additional traffic in the system and could degrade performance in production.

### REST

Execute the following REST API request to configure the `operations-log` table:

`POST /configuration/v1/environment`
    
    
    {
      "operationsLogLevel": "ALL"
    }
    

Where:

  * `ALL`: All messages will be sent to the `operations-log` table for each step in the processing pipeline.
  * `ERROR`: Only messages that failed any of the processing steps will be sent to the `operations-log`table.



## Processing steps

In order to diagnose why a message is being rejected when passing through the processing pipeline, it's useful to know the different processing steps and understand what they do. For more information, see [MDE Architecture](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview#components).

  1. **message-mapper** : Reads the original JSON, matches it to the corresponding message-class and processes it using Whistle to emit one or more records.
  2. **configuration-manager** : Creates a new tag in the system if it doesn't already exist and adds to the record all the defined properties in the appropriate type (metadata buckets, sinks ,and transformations).
  3. **metadata-manager** : Resolves all metadata references of this record, updates the system metadata instances if a new one is received, adds materialized metadata to the record if it's configured to do so.
  4. **bigquery-sink** : Maps the record to the appropriate type structure and sends it to the corresponding PubSub topic to be written into BigQuery.
  5. **pubsub-sink** : Maps the record to the pubsub Proto or JSON structure and sends it to the corresponding topic.
  6. **GCSWriter** : Writes both, raw data as it's received from the `input-messages` topic as well as processed data after it goes through the metadata-manager.
  7. **BigtableWriter** : Writes data to Bigtable.
  8. **GCSReader** : Reads files from Cloud Storage and sends the messages to `input-messages`.



## Diagnose messages not showing in their configured sink

If you send a message to MDE and it isn't on the configured sink, first verify that the type has configured the sink properly (as explained in the [Type section](https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/type)) and that you're querying the correct table in BigQuery. Remember that the table is named after the type.

If that is configured correctly, then you must use the `operations-log` table to diagnose the issue. You can start with a general query, either ordering by `event_timestamp` or filtering it to when the message was sent, as the following example shows:
    
    
    SELECT
      *
    FROM
      `mde_system.operations-log`
    WHERE
      DATE(event_timestamp) = CURRENT_DATE()
    ORDER BY
      event_timestamp desc
    LIMIT 100;
    

You can also use the `source_message_id` to filter on a specific message. This ID is assigned by Pub/Sub when publishing a message. If you use [gcloud CLI](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/publish) to publish a message from the command line, it will return the `messageId` of the published message.
    
    
    SELECT
      *
    FROM
      `mde_system.operations-log`
    WHERE
      DATE(event_timestamp) <= CURRENT_DATE()
      AND source_message_id = 'PubSubMessageId';
    

If you can't find the message or there are too many, you can filter based on an attribute of the original message. The message is always logged in the `payload` field with the state that the last step left it, and it is saved in a JSON field, so it is easier to use `TO_JSON_STRING` and use `%` to look for any messages that contain the text you want.
    
    
    SELECT
      *
    FROM
      `mde_system.operations-log`
    WHERE
      DATE(event_timestamp) = CURRENT_DATE()
      AND TO_JSON_STRING(payload) LIKE "%TEXT-TO-FIND%"
    ORDER BY
      event_timestamp DESC;
    

Once you find your message in the `operations-log` table, look at the `error-message` column to find the reason the message was rejected. The most common errors are the following:

  * Couldn't match the incoming message with any of the registered message classes in the configuration manager.
  * No parsers found for message class `<MESSAGE_CLASS_NAME>`.
  * Skipping the message processing as it couldn't be deserialized (the message is not a valid JSON).
  * Couldn't construct a valid message with the parser `<PARSER_NAME>`. Message is missing timestamps field.
  * Couldn't construct a valid message with the parser `<PARSER_NAME>`. Message is missing tagName field or it is blank.
  * Couldn't construct a valid message with the parser `<PARSER_NAME>`. Message timestamp is out of the supported bounds.



After you find and fix the error that is causing the message to fail, the messages will start landing in their respective sinks.

**Note:** Configuration changes might take up to two minutes to be reflected in the system.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
