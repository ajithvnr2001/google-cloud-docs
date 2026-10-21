---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/cloud-bigtable-change-streams-to-pubsub/
title: Bigtable change streams to Pub/Sub template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:43:26.153672+00:00
---

# Bigtable change streams to Pub/Sub template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/cloud-bigtable-change-streams-to-pubsub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Bigtable change streams to Pub/Sub template Stay organized with collections  Save and categorize content based on your preferences. 

The Bigtable change streams to Pub/Sub template is a streaming pipeline that streams Bigtable data change records and publishes them to a Pub/Sub topic by using Dataflow.

A Bigtable change stream lets you subscribe to data mutations on a per-table basis. When you subscribe to table change streams, the following constraints apply:

  * Only modified cells and descriptors of delete operations are returned.
  * Only the new value of a modified cell is returned.



When data change records are published to a Pub/Sub topic, messages might be inserted out of order compared to the original Bigtable commit timestamp ordering.

Bigtable data change records that can't be published to Pub/Sub topics are temporarily placed in a dead-letter queue (unprocessed messages queue) directory in Cloud Storage. After the maximum number of unsuccessful retries, these records are indefinitely placed in the same dead-letter queue directory for human review or further processing by the user.

The pipeline requires that the destination Pub/Sub topic exists. The destination topic might be configured to validate messages using a schema. When a Pub/Sub topic specifies a schema, the pipeline only starts if the schema is valid. Depending on the schema type, use one of the following schema definitions for the destination topic:

### Protocol buffers
    
    
    syntax = "proto2";
    
    package com.google.cloud.teleport.bigtable;
    
    option java_outer_classname = "ChangeLogEntryProto";
    
    message ChangelogEntryProto{
      required bytes rowKey = 1;
      enum ModType {
        SET_CELL = 0;
        DELETE_FAMILY = 1;
        DELETE_CELLS = 2;
        UNKNOWN = 3;
      }
      required ModType modType = 2;
      required bool isGC = 3;
      required int32 tieBreaker = 4;
      required int64 commitTimestamp = 5;
      required string columnFamily = 6;
      optional bytes column = 7;
      optional int64 timestamp = 8;
      optional int64 timestampFrom = 9;
      optional int64 timestampTo = 10;
      optional bytes value = 11;
      required string sourceInstance = 12;
      required string sourceCluster = 13;
      required string sourceTable = 14;
    }
      

### Avro
    
    
    {
        "name" : "ChangelogEntryMessage",
        "type" : "record",
        "namespace" : "com.google.cloud.teleport.bigtable",
        "fields" : [
          { "name" : "rowKey", "type" : "bytes"},
          {
            "name" : "modType",
            "type" : {
              "name": "ModType",
              "type": "enum",
              "symbols": ["SET_CELL", "DELETE_FAMILY", "DELETE_CELLS", "UNKNOWN"]}
          },
          { "name": "isGC", "type": "boolean" },
          { "name": "tieBreaker", "type": "int"},
          { "name": "columnFamily", "type": "string"},
          { "name": "commitTimestamp", "type" : "long"},
          { "name" : "sourceInstance", "type" : "string"},
          { "name" : "sourceCluster", "type" : "string"},
          { "name" : "sourceTable", "type" : "string"},
          { "name": "column", "type" : ["null", "bytes"]},
          { "name": "timestamp", "type" : ["null", "long"]},
          { "name": "timestampFrom", "type" : ["null", "long"]},
          { "name": "timestampTo", "type" : ["null", "long"]},
          { "name" : "value", "type" : ["null", "bytes"]}
       ]
    }
        

### JSON

Use the following Protobuf schema with `JSON` message encoding:
    
    
    syntax = "proto2";
    
    package com.google.cloud.teleport.bigtable;
    
    option java_outer_classname = "ChangelogEntryMessageText";
    
    message ChangelogEntryText{
      required string rowKey = 1;
      enum ModType {
        SET_CELL = 0;
        DELETE_FAMILY = 1;
        DELETE_CELLS = 2;
        UNKNOWN = 3;
      }
      required ModType modType = 2;
      required bool isGC = 3;
      required int32 tieBreaker = 4;
      required int64 commitTimestamp = 5;
      required string columnFamily = 6;
      optional string column = 7;
      optional int64 timestamp = 8;
      optional int64 timestampFrom = 9;
      optional int64 timestampTo = 10;
      optional string value = 11;
      required string sourceInstance = 12;
      required string sourceCluster = 13;
      required string sourceTable = 14;
    }
        

Each new Pub/Sub message includes one entry from a [data change record](https://docs.cloud.google.com/bigtable/docs/change-streams-overview#data-change-record) returned by the change stream from its corresponding row in your Bigtable table. The Pub/Sub template flattens the entries in each data change record into individual cell-level changes.

## Pub/Sub output message description

Field name | Description  
---|---  
`rowKey` | The row key of the changed row. Arrives in a form of a byte array. When JSON message encoding is configured, row keys are returned as strings. When `useBase64Rowkeys` is specified, row keys are Base64-encoded. Otherwise, a charset specified by `bigtableChangeStreamCharset` is used to decode row key bytes into a string.  
`modType` | The type of the row mutation. Use one of the following values: `SET_CELL`, `DELETE_CELLS`, or `DELETE_FAMILY`.  
`columnFamily` | The column family affected by the row mutation.  
`column` | The column qualifier affected by the row mutation. For the `DELETE_FAMILY` mutation type, the column field isn't set. Arrives in a form of a byte array. When JSON message encoding is configured, columns are returned as strings. When `useBase64ColumnQualifier` is specified, the column field is Base64-encoded. Otherwise, a charset specified by `bigtableChangeStreamCharset` is used to decode row key bytes into a string.  
`commitTimestamp` | The time when Bigtable applies the mutation. The time is measured in microseconds since the Unix epoch (January 1, 1970 at UTC).  
`timestamp` | The timestamp value of the cell affected by the mutation. For `DELETE_CELLS` and `DELETE_FAMILY` mutation types, timestamp is not set. The time is measured in microseconds since the Unix epoch (January 1, 1970 at UTC).  
`timestampFrom` | Describes an inclusive start of the timestamp interval for all cells deleted by the `DELETE_CELLS` mutation. For other mutation types, `timestampFrom` isn't set. The time is measured in microseconds since the Unix epoch (January 1, 1970 at UTC).  
`timestampTo` | Describes an exclusive end of the timestamp interval for all cells deleted by the `DELETE_CELLS` mutation. For other mutation types, `timestampTo` isn't set.  
`isGC` | A boolean value that indicates whether the mutation is generated by a Bigtable garbage collection mechanism.  
`tieBreaker` | When two mutations are registered at the same time by different Bigtable clusters, the mutation with the highest `tiebreaker` value is applied to the source table. Mutations with lower `tiebreaker` values are discarded.  
`value` | The new value set by the mutation. Unless the `stripValues` pipeline option is set, the value is set for `SET_CELL` mutations. For other mutation types, the value isn't set. Arrives in a form of a byte array. When JSON message encoding is configured, values are returned as strings. When `useBase64Values` is specified, the value is Base64-encoded. Otherwise, a charset specified by `bigtableChangeStreamCharset` is used to decode value bytes into a string.  
`sourceInstance` | The name of the Bigtable instance that registered the mutation. Might be when multiple pipelines stream changes from different instances to the same Pub/Sub topic.  
`sourceCluster` | The name of the Bigtable cluster that registered the mutation. Might be used when multiple pipelines stream changes from different instances to the same Pub/Sub topic.  
`sourceTable` | The name of the Bigtable table that received the mutation. Might be used in case when a multiple pipelines stream changes from a different tables to the same Pub/Sub topic.  
  
## Pipeline requirements

  * The specified Bigtable source instance.
  * The specified Bigtable source table. The table must have change streams enabled.
  * The specified Bigtable application profile.
  * The specified Pub/Sub topic must exist.



## Template parameters

### Required parameters

  * **pubSubTopic** : The name of the destination Pub/Sub topic.
  * **bigtableChangeStreamAppProfile** : The Bigtable application profile ID. The application profile must use single-cluster routing and allow single-row transactions.
  * **bigtableReadInstanceId** : The source Bigtable instance ID.
  * **bigtableReadTableId** : The source Bigtable table ID.



### Optional parameters

  * **messageEncoding** : The encoding of the messages to be published to the Pub/Sub topic. When the schema of the destination topic is configured, the message encoding is determined by the topic settings. The following values are supported: `BINARY` and `JSON`. Defaults to `JSON`.
  * **messageFormat** : The encoding of the messages to publish to the Pub/Sub topic. When the schema of the destination topic is configured, the message encoding is determined by the topic settings. The following values are supported: `AVRO`, `PROTOCOL_BUFFERS`, and `JSON`. The default value is `JSON`. When the `JSON` format is used, the rowKey, column, and value fields of the message are strings, the contents of which are determined by the pipeline options `useBase64Rowkeys`, `useBase64ColumnQualifiers`, `useBase64Values`, and `bigtableChangeStreamCharset`.
  * **stripValues** : When set to `true`, the `SET_CELL` mutations are returned without new values set. Defaults to `false`. This parameter is useful when you don't need a new value to be present, also known as cache invalidation, or when values are extremely large and exceed Pub/Sub message size limits.
  * **dlqDirectory** : The directory for the dead-letter queue. Records that fail to be processed are stored in this directory. Defaults to a directory under the Dataflow job temp location. In most cases, you can use the default path.
  * **dlqRetryMinutes** : The number of minutes between dead-letter queue retries. Defaults to `10`.
  * **dlqMaxRetries** : The dead letter maximum retries. Defaults to `5`.
  * **useBase64Rowkeys** : Used with JSON message encoding. When set to `true`, the `rowKey` field is a Base64-encoded string. Otherwise, the `rowKey` is produced by using `bigtableChangeStreamCharset` to decode bytes into a string. Defaults to `false`.
  * **pubSubProjectId** : The Bigtable project ID. The default is the project of the Dataflow job.
  * **useBase64ColumnQualifiers** : Used with JSON message encoding. When set to `true`, the `column` field is a Base64-encoded string. Otherwise, the column is produced by using `bigtableChangeStreamCharset` to decode bytes into a string. Defaults to `false`.
  * **useBase64Values** : Used with JSON message encoding. When set to `true`, the value field is a Base64-encoded string. Otherwise, the value isproduced by using `bigtableChangeStreamCharset` to decode bytes into a string. Defaults to `false`.
  * **disableDlqRetries** : Whether or not to disable retries for the DLQ. Defaults to: false.
  * **bigtableChangeStreamMetadataInstanceId** : The Bigtable change streams metadata instance ID. Defaults to empty.
  * **bigtableChangeStreamMetadataTableTableId** : The ID of the Bigtable change streams connector metadata table. If not provided, a Bigtable change streams connector metadata table is automatically created during pipeline execution. Defaults to empty.
  * **bigtableChangeStreamCharset** : The Bigtable change streams charset name. Defaults to: UTF-8.
  * **bigtableChangeStreamStartTimestamp** : The starting timestamp (<https://tools.ietf.org/html/rfc3339>), inclusive, to use for reading change streams. For example, `2022-05-05T07:59:59Z`. Defaults to the timestamp of the pipeline start time.
  * **bigtableChangeStreamIgnoreColumnFamilies** : A comma-separated list of column family name changes to ignore. Defaults to empty.
  * **bigtableChangeStreamIgnoreColumns** : A comma-separated list of column name changes to ignore. Example: "cf1:col1,cf2:col2". Defaults to empty.
  * **bigtableChangeStreamName** : A unique name for the client pipeline. Lets you resume processing from the point at which a previously running pipeline stopped. Defaults to an automatically generated name. See the Dataflow job logs for the value used.
  * **bigtableChangeStreamResume** : When set to `true`, a new pipeline resumes processing from the point at which a previously running pipeline with the same `bigtableChangeStreamName` value stopped. If the pipeline with the given `bigtableChangeStreamName` value has never run, a new pipeline doesn't start. When set to `false`, a new pipeline starts. If a pipeline with the same `bigtableChangeStreamName` value has already run for the given source, a new pipeline doesn't start. Defaults to `false`.
  * **bigtableReadChangeStreamTimeoutMs** : The timeout for Bigtable ReadChangeStream requests in milliseconds.
  * **bigtableReadProjectId** : The Bigtable project ID. The default is the project for the Dataflow job.



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **Bigtable change streams to Pub/Sub** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run flex templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 284.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow flex-template run JOB_NAME \
        --region=REGION_NAME \
        --template-file-gcs-location=gs://dataflow-templates/VERSION/flex/Bigtable_Change_Streams_to_PubSub \
        --parameters \
    bigtableReadInstanceId=BIGTABLE_INSTANCE_ID,\
    bigtableReadTableId=BIGTABLE_TABLE_ID,\
    bigtableChangeStreamAppProfile=BIGTABLE_APPLICATION_PROFILE_ID,\
    pubSubTopic=PUBSUB_TOPIC

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID where you want to run the Dataflow job 
  * `JOB_NAME`: a unique job name of your choice 
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `BIGTABLE_INSTANCE_ID`: your Bigtable instance id.
  * `BIGTABLE_TABLE_ID`: your Bigtable table id.
  * `BIGTABLE_APPLICATION_PROFILE_ID`: your Bigtable application profile id.
  * `PUBSUB_TOPIC`: the Pub/Sub destination topic name



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/flexTemplates:launch
    {
      "launch_parameter": {
        "jobName": "JOB_NAME",
        "containerSpecGcsPath": "gs://dataflow-templates/VERSION/flex/Bigtable_Change_Streams_to_PubSub",
        "parameters": {
            "bigtableReadInstanceId": "BIGTABLE_INSTANCE_ID",
            "bigtableReadTableId": "BIGTABLE_TABLE_ID",
            "bigtableChangeStreamAppProfile": "BIGTABLE_APPLICATION_PROFILE_ID",
            "pubSubTopic": "PUBSUB_TOPIC"
        }
      }
    }

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID where you want to run the Dataflow job 
  * `JOB_NAME`: a unique job name of your choice 
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `LOCATION`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `BIGTABLE_INSTANCE_ID`: your Bigtable instance id.
  * `BIGTABLE_TABLE_ID`: your Bigtable table id.
  * `BIGTABLE_APPLICATION_PROFILE_ID`: your Bigtable application profile id.
  * `PUBSUB_TOPIC`: the Pub/Sub destination topic name



## Template source code

### Java
    
    
    /*
     * Copyright (C) 2023 Google LLC
     *
     * Licensed under the Apache License, Version 2.0 (the "License"); you may not
     * use this file except in compliance with the License. You may obtain a copy of
     * the License at
     *
     *   http://www.apache.org/licenses/LICENSE-2.0
     *
     * Unless required by applicable law or agreed to in writing, software
     * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
     * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
     * License for the specific language governing permissions and limitations under
     * the License.
     */
    package com.google.cloud.teleport.v2.templates.bigtablechangestreamstopubsub;
    
    import com.google.cloud.[Timestamp](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html);
    import com.google.cloud.[bigtable](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions.html#com_google_cloud_bigquery_FormatOptions_bigtable__).[data](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.Message.html#com_google_cloud_pubsublite_Message_data__).v2.models.[ChangeStreamMutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.ChangeStreamMutation.html);
    import com.google.cloud.[bigtable](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions.html#com_google_cloud_bigquery_FormatOptions_bigtable__).[data](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.Message.html#com_google_cloud_pubsublite_Message_data__).v2.models.[ChangeStreamMutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.ChangeStreamMutation.html).MutationType;
    import com.google.cloud.[bigtable](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions.html#com_google_cloud_bigquery_FormatOptions_bigtable__).[data](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.Message.html#com_google_cloud_pubsublite_Message_data__).v2.models.[DeleteCells](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.DeleteCells.html);
    import com.google.cloud.[bigtable](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions.html#com_google_cloud_bigquery_FormatOptions_bigtable__).[data](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.Message.html#com_google_cloud_pubsublite_Message_data__).v2.models.[DeleteFamily](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.DeleteFamily.html);
    import com.google.cloud.[bigtable](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions.html#com_google_cloud_bigquery_FormatOptions_bigtable__).[data](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.Message.html#com_google_cloud_pubsublite_Message_data__).v2.models.[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Entry.html);
    import com.google.cloud.[bigtable](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions.html#com_google_cloud_bigquery_FormatOptions_bigtable__).[data](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.Message.html#com_google_cloud_pubsublite_Message_data__).v2.models.[SetCell](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.SetCell.html);
    import com.google.cloud.pubsub.v1.[SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SchemaServiceClient.html);
    import com.google.cloud.pubsub.v1.[TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html);
    import com.google.cloud.teleport.metadata.[Template](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.Template.html);
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.v2.[bigtable](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions.html#com_google_cloud_bigquery_FormatOptions_bigtable__).options.BigtableCommonOptions;
    import com.google.cloud.teleport.v2.[bigtable](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions.html#com_google_cloud_bigquery_FormatOptions_bigtable__).utils.UnsupportedEntryException;
    import com.google.cloud.teleport.v2.cdc.dlq.DeadLetterQueueManager;
    import com.google.cloud.teleport.v2.cdc.dlq.StringDeadLetterQueueSanitizer;
    import com.google.cloud.teleport.v2.coders.FailsafeElementCoder;
    import com.google.cloud.teleport.v2.options.BigtableChangeStreamsToPubSubOptions;
    import com.google.cloud.teleport.v2.templates.bigtablechangestreamstopubsub.FailsafePublisher.PublishModJsonToTopic;
    import com.google.cloud.teleport.v2.templates.bigtablechangestreamstopubsub.[model](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.Translate.TranslateOption.html#com_google_cloud_translate_Translate_TranslateOption_model_java_lang_String_).MessageEncoding;
    import com.google.cloud.teleport.v2.templates.bigtablechangestreamstopubsub.[model](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.Translate.TranslateOption.html#com_google_cloud_translate_Translate_TranslateOption_model_java_lang_String_).[MessageFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.NotificationConfig.MessageFormat.html);
    import com.google.cloud.teleport.v2.templates.bigtablechangestreamstopubsub.[model](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.Translate.TranslateOption.html#com_google_cloud_translate_Translate_TranslateOption_model_java_lang_String_).Mod;
    import com.google.cloud.teleport.v2.templates.bigtablechangestreamstopubsub.[model](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.Translate.TranslateOption.html#com_google_cloud_translate_Translate_TranslateOption_model_java_lang_String_).ModType;
    import com.google.cloud.teleport.v2.templates.bigtablechangestreamstopubsub.[model](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.Translate.TranslateOption.html#com_google_cloud_translate_Translate_TranslateOption_model_java_lang_String_).PubSubDestination;
    import com.google.cloud.teleport.v2.templates.bigtablechangestreamstopubsub.[model](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.Translate.TranslateOption.html#com_google_cloud_translate_Translate_TranslateOption_model_java_lang_String_).TestChangeStreamMutation;
    import com.google.cloud.teleport.v2.templates.bigtablechangestreamstopubsub.schemautils.PubSubUtils;
    import com.google.cloud.teleport.v2.transforms.DLQWriteTransform;
    import com.google.cloud.teleport.v2.utils.[BigtableSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BigtableSource.html);
    import com.google.cloud.teleport.v2.values.FailsafeElement;
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import com.google.pubsub.v1.[Encoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Encoding.html);
    import com.google.pubsub.v1.[GetTopicRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.GetTopicRequest.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import com.google.pubsub.v1.[Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.html);
    import com.google.pubsub.v1.[SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html);
    import com.google.pubsub.v1.[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html);
    import com.google.pubsub.v1.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html);
    import com.google.pubsub.v1.[ValidateMessageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ValidateMessageRequest.html);
    import java.io.IOException;
    import java.nio.charset.Charset;
    import java.util.ArrayList;
    import java.util.Base64;
    import java.util.[List](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ExecuteDashboardQueryResponse.ColumnType.List.html);
    import org.apache.beam.runners.dataflow.options.DataflowPipelineOptions;
    import org.apache.beam.sdk.[Pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Pipeline.html);
    import org.apache.beam.sdk.[PipelineResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.PipelineResult.html);
    import org.apache.beam.sdk.coders.CoderRegistry;
    import org.apache.beam.sdk.coders.StringUtf8Coder;
    import org.apache.beam.sdk.io.gcp.[bigtable](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions.html#com_google_cloud_bigquery_FormatOptions_bigtable__).BigtableIO;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.transforms.Create;
    import org.apache.beam.sdk.transforms.DoFn;
    import org.apache.beam.sdk.transforms.Flatten;
    import org.apache.beam.sdk.transforms.MapElements;
    import org.apache.beam.sdk.transforms.ParDo;
    import org.apache.beam.sdk.transforms.[Values](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.Values.html);
    import org.apache.beam.sdk.values.PCollection;
    import org.apache.beam.sdk.values.PCollectionList;
    import org.apache.beam.sdk.values.PCollectionTuple;
    import org.apache.beam.sdk.values.TupleTag;
    import org.apache.commons.lang3.StringUtils;
    import org.joda.time.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import org.joda.time.Instant;
    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;
    
    /**
     * This pipeline ingests {@link ChangeStreamMutation} from Bigtable change stream. The {@link
     * ChangeStreamMutation} is then broken into {@link Mod}, which converted into PubsubMessage and
     * inserted into Pub/Sub topic.
     */
    @Template(
        name = "Bigtable_Change_Streams_to_PubSub",
        category = TemplateCategory.STREAMING,
        displayName = "Cloud Bigtable Change Streams to PubSub",
        description =
            "Streaming pipeline. Streams Bigtable data change records and writes them into PubSub using Dataflow Runner V2.",
        optionsClass = BigtableChangeStreamsToPubSubOptions.class,
        optionsOrder = {
          BigtableChangeStreamsToPubSubOptions.class,
          BigtableCommonOptions.ReadChangeStreamOptions.class,
          BigtableCommonOptions.ReadOptions.class
        },
        skipOptions = {
          "bigtableReadAppProfile",
          "bigtableAdditionalRetryCodes",
          "bigtableRpcAttemptTimeoutMs",
          "bigtableRpcTimeoutMs"
        },
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/cloud-bigtable-change-streams-to-pubsub",
        flexContainerName = "googlecloud-to-googlecloud",
        contactInformation = "https://cloud.google.com/support",
        streaming = true,
        supportsAtLeastOnce = true)
    public final class BigtableChangeStreamsToPubSub {
    
      /** String/String Coder for {@link FailsafeElement}. */
      public static final FailsafeElementCoder<String, String> FAILSAFE_ELEMENT_CODER =
          FailsafeElementCoder.of(StringUtf8Coder.of(), StringUtf8Coder.of());
    
      private static final Logger LOG = LoggerFactory.getLogger(BigtableChangeStreamsToPubSub.class);
    
      private static final [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) USE_RUNNER_V2_EXPERIMENT = "use_runner_v2";
    
      private static final TupleTag<FailsafeElement<String, String>> INVALID_MODS_TAG =
          new TupleTag<FailsafeElement<String, String>>("invalidMods") {};
      private static final TupleTag<FailsafeElement<String, String>> VALID_MODS_TAG =
          new TupleTag<FailsafeElement<String, String>>("validMods") {};
    
      /**
       * Main entry point for executing the pipeline.
       *
       * @param args The command-line arguments to the pipeline.
       */
      public static void main([String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html)[] args) {
        LOG.info("Starting to replicate change records from Cloud Bigtable change streams to PubSub");
    
        BigtableChangeStreamsToPubSubOptions options =
            PipelineOptionsFactory.fromArgs(args)
                .withValidation()
                .as(BigtableChangeStreamsToPubSubOptions.class);
    
        run(options);
      }
    
      private static void validateOptions(BigtableChangeStreamsToPubSubOptions options) {
        if (options.getDlqRetryMinutes() <= 0) {
          throw new IllegalArgumentException("dlqRetryMinutes must be positive.");
        }
        if (options.getDlqMaxRetries() < 0) {
          throw new IllegalArgumentException("dlqMaxRetries cannot be negative.");
        }
        if (options.getBigtableReadChangeStreamTimeoutMs() != null
            && options.getBigtableReadChangeStreamTimeoutMs() <= 0) {
          throw new IllegalArgumentException(
              "bigtableReadChangeStreamTimeoutMs must be greater than 0.");
        }
      }
    
      private static void setOptions(BigtableChangeStreamsToPubSubOptions options) {
        options.setStreaming(true);
        options.setEnableStreamingEngine(true);
    
        // Add use_runner_v2 to the experiments option, since change streams connector is only supported
        // on Dataflow runner v2.
        List<String> experiments = options.getExperiments();
        if (experiments == null) {
          experiments = new ArrayList<>();
        }
        boolean hasUseRunnerV2 = false;
        for ([String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) experiment : experiments) {
          if (experiment.equalsIgnoreCase(USE_RUNNER_V2_EXPERIMENT)) {
            hasUseRunnerV2 = true;
            break;
          }
        }
        if (!hasUseRunnerV2) {
          experiments.add(USE_RUNNER_V2_EXPERIMENT);
        }
        options.[setExperiments](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListExperimentsResponse.Builder.html#com_google_cloud_dialogflow_cx_v3_ListExperimentsResponse_Builder_setExperiments_int_com_google_cloud_dialogflow_cx_v3_Experiment_)(experiments);
      }
    
      /**
       * Runs the pipeline with the supplied options.
       *
       * @param options The execution parameters to the pipeline.
       * @return The result of the pipeline execution.
       */
      public static [PipelineResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.PipelineResult.html) run(BigtableChangeStreamsToPubSubOptions options) {
        setOptions(options);
        validateOptions(options);
    
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) bigtableProject = getBigtableProjectId(options);
    
        // Retrieve and parse the startTimestamp
        Instant startTimestamp =
            options.getBigtableChangeStreamStartTimestamp().isEmpty()
                ? Instant.[now](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html#com_google_cloud_Timestamp_now__)()
                : toInstant([Timestamp](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html).[parseTimestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html#com_google_cloud_Timestamp_parseTimestamp_java_lang_String_)(options.getBigtableChangeStreamStartTimestamp()));
    
        [BigtableSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BigtableSource.html) sourceInfo =
            new [BigtableSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BigtableSource.html)(
                options.getBigtableReadInstanceId(),
                options.getBigtableReadTableId(),
                getBigtableCharset(options),
                options.getBigtableChangeStreamIgnoreColumnFamilies(),
                options.getBigtableChangeStreamIgnoreColumns(),
                startTimestamp);
    
        [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html) topic = null;
        try ([TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html) topicAdminClient = [TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html).create()) {
          [GetTopicRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.GetTopicRequest.html) request =
              [GetTopicRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.GetTopicRequest.html).newBuilder()
                  .setTopic(
                      [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html).[ofProjectTopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html#com_google_pubsub_v1_TopicName_ofProjectTopicName_java_lang_String_java_lang_String_)(
                              getPubSubProjectId(options), options.getPubSubTopic())
                          .toString())
                  .build();
          topic = topicAdminClient.getTopic(request);
        } catch (Exception e) {
          throw new RuntimeException(e);
        }
    
        try {
          if (!validateSchema(topic, options, sourceInfo)) {
            final [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) errorMessage = "Configured topic doesn't accept messages of configured format";
            throw new IllegalArgumentException(errorMessage);
          }
    
        } catch (Exception e) {
          throw new IllegalArgumentException(e);
        }
    
        PubSubDestination destinationInfo = newPubSubDestination(options, topic);
        PubSubUtils pubSub = new PubSubUtils(sourceInfo, destinationInfo);
    
        /*
         * Stages:
         * 1) Read {@link ChangeStreamMutation} from change stream.
         * 2) Create {@link FailsafeElement} of {@link Mod} JSON and merge from:
         *    - {@link ChangeStreamMutation}.
         *    - GCS Dead letter queue.
         * 3) Convert {@link Mod} JSON into PubsubMessage and publish it to PubSub.
         * 4) Write Failures from 2) and 3) to GCS dead letter queue.
         */
        // Step 1
        [Pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Pipeline.html) pipeline = [Pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Pipeline.html).create(options);
    
        // Register the coders for pipeline
        CoderRegistry coderRegistry = [pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore.html#com_google_cloud_firestore_Firestore_pipeline__).getCoderRegistry();
        coderRegistry.registerCoderForType(
            FAILSAFE_ELEMENT_CODER.getEncodedTypeDescriptor(), FAILSAFE_ELEMENT_CODER);
    
        DeadLetterQueueManager dlqManager = buildDlqManager(options);
    
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) dlqDirectory = dlqManager.getRetryDlqDirectoryWithDateTime();
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) tempDlqDirectory = dlqManager.getRetryDlqDirectory() + "tmp/";
    
        if (options.getDisableDlqRetries()) {
          LOG.info(
              "Disabling retries for the DLQ, directly writing into severe DLQ: {}",
              dlqManager.getSevereDlqDirectoryWithDateTime());
          dlqDirectory = dlqManager.getSevereDlqDirectoryWithDateTime();
          tempDlqDirectory = dlqManager.getSevereDlqDirectory() + "tmp/";
        }
    
        BigtableIO.ReadChangeStream readChangeStream =
            BigtableIO.[readChangeStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html#com_google_cloud_bigtable_data_v2_BigtableDataClient_readChangeStream_com_google_cloud_bigtable_data_v2_models_ReadChangeStreamQuery_)()
                .withChangeStreamName(options.getBigtableChangeStreamName())
                .withExistingPipelineOptions(
                    options.getBigtableChangeStreamResume()
                        ? BigtableIO.ExistingPipelineOptions.RESUME_OR_FAIL
                        : BigtableIO.ExistingPipelineOptions.FAIL_IF_EXISTS)
                .withProjectId(bigtableProject)
                .withMetadataTableInstanceId(options.getBigtableChangeStreamMetadataInstanceId())
                .withInstanceId(options.getBigtableReadInstanceId())
                .withTableId(options.getBigtableReadTableId())
                .withAppProfileId(options.getBigtableChangeStreamAppProfile())
                .withStartTime(startTimestamp);
    
        if (!StringUtils.isBlank(options.getBigtableChangeStreamMetadataTableTableId())) {
          readChangeStream =
              [readChangeStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html#com_google_cloud_bigtable_data_v2_BigtableDataClient_readChangeStream_com_google_cloud_bigtable_data_v2_models_ReadChangeStreamQuery_).withMetadataTableTableId(
                  options.getBigtableChangeStreamMetadataTableTableId());
        }
    
        if (options.getBigtableReadChangeStreamTimeoutMs() != null) {
          readChangeStream =
              [readChangeStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html#com_google_cloud_bigtable_data_v2_BigtableDataClient_readChangeStream_com_google_cloud_bigtable_data_v2_models_ReadChangeStreamQuery_).withReadChangeStreamTimeout(
                  [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).millis(options.getBigtableReadChangeStreamTimeoutMs()));
        }
    
        // Step 2: just return the output for sending to pubSub and DLQ
        PCollection<ChangeStreamMutation> dataChangeRecord =
            [pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore.html#com_google_cloud_firestore_Firestore_pipeline__)
                .apply("Read from Cloud Bigtable Change Streams", readChangeStream)
                .apply([Values](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.Values.html).create());
    
        PCollection<FailsafeElement<String, String>> sourceFailsafeModJson =
            dataChangeRecord
                .apply(
                    "ChangeStreamMutation To Mod JSON",
                    ParDo.of(new ChangeStreamMutationToModJsonFn(sourceInfo)))
                .apply(
                    "Wrap Mod JSON In FailsafeElement",
                    ParDo.of(
                        new DoFn<String, FailsafeElement<String, String>>() {
                          @ProcessElement
                          public void process(
                              @Element String input,
                              OutputReceiver<FailsafeElement<String, String>> receiver) {
                            receiver.output(FailsafeElement.of(input, input));
                          }
                        }))
                .setCoder(FAILSAFE_ELEMENT_CODER);
    
        PCollectionTuple dlqModJson =
            dlqManager.getReconsumerDataTransform(
                [pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore.html#com_google_cloud_firestore_Firestore_pipeline__).apply(dlqManager.dlqReconsumer(options.getDlqRetryMinutes())));
    
        PCollection<FailsafeElement<String, String>> retryableDlqFailsafeModJson = null;
        if (options.getDisableDlqRetries()) {
          retryableDlqFailsafeModJson = [pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore.html#com_google_cloud_firestore_Firestore_pipeline__).apply(Create.[empty](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.RequestBody.html#com_google_cloud_storage_RequestBody_empty__)(FAILSAFE_ELEMENT_CODER));
        } else {
          retryableDlqFailsafeModJson =
              dlqModJson.get(DeadLetterQueueManager.RETRYABLE_ERRORS).setCoder(FAILSAFE_ELEMENT_CODER);
        }
    
        PCollection<FailsafeElement<String, String>> failsafeModJson =
            PCollectionList.of(sourceFailsafeModJson)
                .and(retryableDlqFailsafeModJson)
                .apply("Merge Source And DLQ Mod JSON", Flatten.pCollections());
    
        PublishModJsonToTopic publishModJsonToTopic =
            new PublishModJsonToTopic(pubSub, VALID_MODS_TAG, INVALID_MODS_TAG);
    
        PCollectionTuple failedToPublish =
            failsafeModJson.apply("Publish Mod JSON To Pubsub", publishModJsonToTopic);
    
        PCollection<String> transformDlqJson =
            failedToPublish
                .get(VALID_MODS_TAG)
                .setCoder(FAILSAFE_ELEMENT_CODER)
                .apply(
                    "Failed Mod JSON During Table Row Transformation",
                    MapElements.via(new StringDeadLetterQueueSanitizer()));
    
        PCollectionList.of(transformDlqJson)
            .apply("Merge Failed Mod JSON From Transform And PubSub", Flatten.pCollections())
            .apply(
                "Write Failed Mod JSON To DLQ",
                DLQWriteTransform.WriteDLQ.newBuilder()
                    .withDlqDirectory(dlqDirectory)
                    .withTmpDirectory(tempDlqDirectory)
                    .setIncludePaneInfo(true)
                    .build());
    
        PCollection<FailsafeElement<String, String>> nonRetryableDlqModJsonFailsafe =
            PCollectionList.of(
                    dlqModJson
                        .get(DeadLetterQueueManager.PERMANENT_ERRORS)
                        .setCoder(FAILSAFE_ELEMENT_CODER))
                .and(failedToPublish.get(INVALID_MODS_TAG).setCoder(FAILSAFE_ELEMENT_CODER))
                .apply("Merge Reconsume And Invalid Mods", Flatten.pCollections());
        LOG.info(
            "DLQ manager severe DLQ directory with date time: {}",
            dlqManager.getSevereDlqDirectoryWithDateTime());
        LOG.info("DLQ manager severe DLQ directory: {}", dlqManager.getSevereDlqDirectory() + "tmp/");
        nonRetryableDlqModJsonFailsafe
            .apply(
                "Write Mod JSON With Non-retriable Error To DLQ",
                MapElements.via(new StringDeadLetterQueueSanitizer()))
            .setCoder(StringUtf8Coder.of())
            .apply(
                DLQWriteTransform.WriteDLQ.newBuilder()
                    .withDlqDirectory(dlqManager.getSevereDlqDirectoryWithDateTime())
                    .withTmpDirectory(dlqManager.getSevereDlqDirectory() + "tmp/")
                    .setIncludePaneInfo(true)
                    .build());
    
        return [pipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore.html#com_google_cloud_firestore_Firestore_pipeline__).run();
      }
    
      private static PubSubDestination newPubSubDestination(
          BigtableChangeStreamsToPubSubOptions options, [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html) topic) {
        return new PubSubDestination(
            getPubSubProjectId(options),
            options.getPubSubTopic(),
            topic,
            options.getMessageFormat(),
            options.getMessageEncoding(),
            options.getUseBase64Rowkeys(),
            options.getUseBase64ColumnQualifiers(),
            options.getUseBase64Values(),
            options.getStripValues());
      }
    
      private static Instant toInstant([Timestamp](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html) timestamp) {
        if (timestamp == null) {
          return null;
        } else {
          return Instant.ofEpochMilli(timestamp.[getSeconds](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html#com_google_protobuf_Timestamp_getSeconds__)() * 1000 + timestamp.[getNanos](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html#com_google_protobuf_Timestamp_getNanos__)() / 1000000);
        }
      }
    
      private static DeadLetterQueueManager buildDlqManager(
          BigtableChangeStreamsToPubSubOptions options) {
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) tempLocation =
            options.as(DataflowPipelineOptions.class).getTempLocation().endsWith("/")
                ? options.as(DataflowPipelineOptions.class).getTempLocation()
                : options.as(DataflowPipelineOptions.class).getTempLocation() + "/";
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) dlqDirectory =
            options.getDlqDirectory().isEmpty() ? tempLocation + "dlq/" : options.getDlqDirectory();
    
        LOG.info("DLQ directory: {}", dlqDirectory);
        return DeadLetterQueueManager.create(dlqDirectory, options.getDlqMaxRetries());
      }
    
      private static [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) getBigtableCharset(BigtableChangeStreamsToPubSubOptions options) {
        return StringUtils.isEmpty(options.getBigtableChangeStreamCharset())
            ? "UTF-8"
            : options.getBigtableChangeStreamCharset();
      }
    
      private static [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) getBigtableProjectId(BigtableChangeStreamsToPubSubOptions options) {
        return StringUtils.isEmpty(options.getBigtableReadProjectId())
            ? options.getProject()
            : options.getBigtableReadProjectId();
      }
    
      private static [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) getPubSubProjectId(BigtableChangeStreamsToPubSubOptions options) {
        return StringUtils.isEmpty(options.getPubSubProjectId())
            ? options.getProject()
            : options.getPubSubProjectId();
      }
    
      private static Boolean validateSchema(
          [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html) topic, BigtableChangeStreamsToPubSubOptions options, [BigtableSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BigtableSource.html) source)
          throws Exception {
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) messageFormatPath = topic.[getSchemaSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html#com_google_pubsub_v1_Topic_getSchemaSettings__)().getSchema();
        if (topic.[getSchemaSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html#com_google_pubsub_v1_Topic_getSchemaSettings__)().getSchema().isEmpty()) {
          validateIncompatibleEncoding(options);
          LOG.info(
              "Topic has no schema configured, pipeline will use message format: {}, message encoding: {}",
              options.getMessageFormat(),
              options.getMessageEncoding());
          return true;
        } else {
          [SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html) schemaName = [SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html).parse(topic.[getSchemaSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html#com_google_pubsub_v1_Topic_getSchemaSettings__)().getSchema());
          [Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.html) schema;
          try ([SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SchemaServiceClient.html) schemaServiceClient = [SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SchemaServiceClient.html).create()) {
            schema = schemaServiceClient.getSchema(schemaName);
          }
    
          options.setMessageEncoding(toMessageEncoding(topic.[getSchemaSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html#com_google_pubsub_v1_Topic_getSchemaSettings__)().getEncoding()));
    
          [Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.html).[Type](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Type.html) schemaType = schema.[getType](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.html#com_google_pubsub_v1_Schema_getType__)();
          switch (schemaType) {
            case AVRO:
              options.[setMessageFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.NotificationConfig.Builder.html#com_google_cloud_dialogflow_v2_NotificationConfig_Builder_setMessageFormat_com_google_cloud_dialogflow_v2_NotificationConfig_MessageFormat_)([MessageFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.NotificationConfig.MessageFormat.html).AVRO);
              validateNoUseOfBase64(options);
              break;
            case PROTOCOL_BUFFER:
              if (options.getMessageEncoding() == MessageEncoding.JSON) {
                options.[setMessageFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.NotificationConfig.Builder.html#com_google_cloud_dialogflow_v2_NotificationConfig_Builder_setMessageFormat_com_google_cloud_dialogflow_v2_NotificationConfig_MessageFormat_)([MessageFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.NotificationConfig.MessageFormat.html).JSON);
              } else {
                options.[setMessageFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.NotificationConfig.Builder.html#com_google_cloud_dialogflow_v2_NotificationConfig_Builder_setMessageFormat_com_google_cloud_dialogflow_v2_NotificationConfig_MessageFormat_)([MessageFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.NotificationConfig.MessageFormat.html).PROTOCOL_BUFFERS);
                validateNoUseOfBase64(options);
              }
              break;
            case TYPE_UNSPECIFIED:
            case UNRECOGNIZED:
              // Not overriding messageFormat, will try what customer configured or the default if
              // not configured
              break;
            default:
              throw new IllegalArgumentException("Topic schema type is not supported: " + schemaType);
          }
    
          LOG.info("Topic has schema configured: {}", topic.[getSchemaSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html#com_google_pubsub_v1_Topic_getSchemaSettings__)().getSchema());
          LOG.info(
              "Pipeline will use message format: {}, message encoding: {}",
              options.getMessageFormat(),
              options.getMessageEncoding());
    
          PubSubDestination destination = newPubSubDestination(options, topic);
          PubSubUtils pubSub = new PubSubUtils(source, destination);
    
          [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) testChangeMessageData = createTestChangeMessage(pubSub).getData();
          [Encoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Encoding.html) encoding = toPubSubEncoding(options.getMessageEncoding());
          try ([SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SchemaServiceClient.html) schemaServiceClient = [SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SchemaServiceClient.html).create()) {
            [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) testMessageEncoded = toBase64String(testChangeMessageData);
            LOG.info("Validating a test message (Base64 encoded): {}", testMessageEncoded);
            [ValidateMessageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ValidateMessageRequest.html) request =
                [ValidateMessageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ValidateMessageRequest.html).newBuilder()
                    .setParent("projects/" + pubSub.getDestination().getPubSubProject())
                    .setEncoding(encoding)
                    .setMessage(testChangeMessageData)
                    .setName(messageFormatPath)
                    .build();
            schemaServiceClient.validateMessage(request);
            LOG.info("Test message successfully validated.");
          } catch (Exception e) {
            throw new IllegalArgumentException("Failed to validate test message", e);
          }
        }
        return true;
      }
    
      private static void validateNoUseOfBase64(BigtableChangeStreamsToPubSubOptions options) {
        if (options.getUseBase64Values()) {
          throw new IllegalArgumentException(
              "useBase64Values values can only be used with topics accepting JSON messages");
        }
        if (options.getUseBase64Rowkeys()) {
          throw new IllegalArgumentException(
              "useBase64Rowkeys values can only be used with topics accepting JSON messages");
        }
        if (options.getUseBase64ColumnQualifiers()) {
          throw new IllegalArgumentException(
              "useBase64ColumnQualifiers values can only be used with topics accepting JSON messages");
        }
      }
    
      private static void validateIncompatibleEncoding(BigtableChangeStreamsToPubSubOptions options) {
        if (options.getMessageEncoding() == MessageEncoding.BINARY
            && options.getMessageFormat() == [MessageFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.NotificationConfig.MessageFormat.html).JSON) {
          throw new IllegalArgumentException(
              "JSON message format is incompatible with BINARY message encoding");
        }
      }
    
      private static MessageEncoding toMessageEncoding([Encoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Encoding.html) encoding) {
        if (encoding == null) {
          return MessageEncoding.JSON;
        }
        switch (encoding) {
          case JSON:
          case ENCODING_UNSPECIFIED:
          case UNRECOGNIZED:
            return MessageEncoding.JSON;
          case BINARY:
            return MessageEncoding.BINARY;
          default:
            throw new IllegalArgumentException("Topic has unsupported message encoding: " + encoding);
        }
      }
    
      private static [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) toBase64String([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) testChangeMessageData) {
        return Base64.getEncoder().[encodeToString](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.connection.PartitionId.html#com_google_cloud_spanner_connection_PartitionId_encodeToString_com_google_cloud_spanner_BatchTransactionId_com_google_cloud_spanner_Partition_)(testChangeMessageData.[toByteArray](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_toByteArray__)());
      }
    
      private static [Encoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Encoding.html) toPubSubEncoding(MessageEncoding messageEncoding) {
        switch (messageEncoding) {
          case BINARY:
            return [Encoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Encoding.html).BINARY;
          case JSON:
            return [Encoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Encoding.html).JSON;
          default:
            throw new IllegalArgumentException("Unexpected message encoding: " + messageEncoding);
        }
      }
    
      private static [PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html) createTestChangeMessage(PubSubUtils pubSub) throws Exception {
        [SetCell](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.SetCell.html) setCell =
            [SetCell](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.SetCell.html).create(
                "test_column_family",
                [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).copyFrom("test_column", Charset.defaultCharset()),
                1000L, // timestamp
                [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).copyFrom("test_value", Charset.defaultCharset()));
    
        TestChangeStreamMutation mutation =
            new TestChangeStreamMutation(
                "test_rowkey",
                MutationType.USER,
                "source_cluster",
                java.time.Instant.[now](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html#com_google_cloud_Timestamp_now__)(), // commit timestamp
                1, // tiebreaker
                "token",
                java.time.Instant.[now](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html#com_google_cloud_Timestamp_now__)(), // low watermark
                setCell);
    
        Mod mod = new Mod(pubSub.getSource(), mutation, setCell);
    
        switch (pubSub.getDestination().getMessageFormat()) {
          case AVRO:
            return pubSub.mapChangeJsonStringToPubSubMessageAsAvro([mod](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.pipeline.expressions.Expression.html#com_google_cloud_firestore_pipeline_expressions_Expression_mod_com_google_cloud_firestore_pipeline_expressions_Expression_com_google_cloud_firestore_pipeline_expressions_Expression_).getChangeJson());
          case PROTOCOL_BUFFERS:
            return pubSub.mapChangeJsonStringToPubSubMessageAsProto([mod](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.pipeline.expressions.Expression.html#com_google_cloud_firestore_pipeline_expressions_Expression_mod_com_google_cloud_firestore_pipeline_expressions_Expression_com_google_cloud_firestore_pipeline_expressions_Expression_).getChangeJson());
          case JSON:
            return pubSub.mapChangeJsonStringToPubSubMessageAsJson([mod](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.pipeline.expressions.Expression.html#com_google_cloud_firestore_pipeline_expressions_Expression_mod_com_google_cloud_firestore_pipeline_expressions_Expression_com_google_cloud_firestore_pipeline_expressions_Expression_).getChangeJson());
          default:
            throw new IllegalArgumentException(
                "Unexpected message format: " + pubSub.getDestination().getMessageFormat());
        }
      }
    
      /**
       * DoFn that converts a {@link ChangeStreamMutation} to multiple {@link Mod} in serialized JSON
       * format.
       */
      static class ChangeStreamMutationToModJsonFn extends DoFn<ChangeStreamMutation, String> {
        private final [BigtableSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BigtableSource.html) sourceInfo;
    
        ChangeStreamMutationToModJsonFn([BigtableSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BigtableSource.html) source) {
          this.sourceInfo = source;
        }
    
        private static [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) toJsonString(Mod mod, [ChangeStreamMutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.ChangeStreamMutation.html) inputMutation) {
          try {
            return [mod](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.pipeline.expressions.Expression.html#com_google_cloud_firestore_pipeline_expressions_Expression_mod_com_google_cloud_firestore_pipeline_expressions_Expression_com_google_cloud_firestore_pipeline_expressions_Expression_).[toJson](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.PostPolicyV4.PostPolicyV4Document.html#com_google_cloud_storage_PostPolicyV4_PostPolicyV4Document_toJson__)();
          } catch (IOException e) {
            // Ignore exception and print bad format.
            return [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html).format("\"%s\"", inputMutation);
          }
        }
    
        @ProcessElement
        public void process(@Element [ChangeStreamMutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.ChangeStreamMutation.html) input, OutputReceiver<String> receiver)
            throws Exception {
          for ([Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Entry.html) entry : input.[getEntries](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.ChangeStreamMutation.html#com_google_cloud_bigtable_data_v2_models_ChangeStreamMutation_getEntries__)()) {
            ModType modType = getModType(entry);
    
            switch (modType) {
              case SET_CELL:
                [SetCell](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.SetCell.html) setCell = ([SetCell](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.SetCell.html)) entry;
                if (!sourceInfo.isIgnoredColumnFamily(setCell.[getFamilyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.SetCell.html#com_google_cloud_bigtable_data_v2_models_SetCell_getFamilyName__)())
                    && !sourceInfo.isIgnoredColumn(
                        setCell.getFamilyName(),
                        setCell.getQualifier().toString(Charset.forName(sourceInfo.getCharset())))) {
                  Mod mod = new Mod(sourceInfo, input, setCell);
                  receiver.output(toJsonString(mod, input));
                }
                break;
              case DELETE_CELLS:
                [DeleteCells](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.DeleteCells.html) deleteCells = ([DeleteCells](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.DeleteCells.html)) entry;
                if (!sourceInfo.isIgnoredColumnFamily(deleteCells.[getFamilyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.DeleteCells.html#com_google_cloud_bigtable_data_v2_models_DeleteCells_getFamilyName__)())
                    && !sourceInfo.isIgnoredColumn(
                        deleteCells.getFamilyName(),
                        deleteCells
                            .getQualifier()
                            .toString(Charset.forName(sourceInfo.getCharset())))) {
                  Mod mod = new Mod(sourceInfo, input, deleteCells);
                  receiver.output(toJsonString(mod, input));
                }
                break;
              case DELETE_FAMILY:
                [DeleteFamily](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.DeleteFamily.html) deleteFamily = ([DeleteFamily](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.DeleteFamily.html)) entry;
                if (!sourceInfo.isIgnoredColumnFamily(deleteFamily.[getFamilyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.DeleteFamily.html#com_google_cloud_bigtable_data_v2_models_DeleteFamily_getFamilyName__)())) {
                  Mod mod = new Mod(sourceInfo, input, deleteFamily);
                  receiver.output(toJsonString(mod, input));
                }
                break;
              default:
              case UNKNOWN:
                throw new UnsupportedEntryException(
                    "Cloud Bigtable change stream entry of type "
                        + entry.getClass().getName()
                        + " is not supported. The entry was put into a DLQ directory. "
                        + "Please update your Dataflow template with the latest template version");
            }
          }
        }
    
        private ModType getModType([Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Entry.html) entry) {
          if (entry instanceof [SetCell](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.SetCell.html)) {
            return ModType.SET_CELL;
          } else if (entry instanceof [DeleteCells](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.DeleteCells.html)) {
            return ModType.DELETE_CELLS;
          } else if (entry instanceof [DeleteFamily](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.DeleteFamily.html)) {
            return ModType.DELETE_FAMILY;
          }
          return ModType.UNKNOWN;
        }
      }
    }
    

## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
