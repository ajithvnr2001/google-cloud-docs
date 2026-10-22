---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/access/how-to-query-in-gcs/
title: Query in Cloud Storage \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:04.010481+00:00
---

# Query in Cloud Storage  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/access/how-to-query-in-gcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Query in Cloud Storage

This guide explains how data is stored in Cloud Storage, both in raw and processed formats.

## Raw data

Manufacturing Data Engine (MDE) stores all messages received in raw format without being processed. This is useful both for archival reasons, and to reprocess data in case of configuration or system errors.

Raw data is stored in AVRO format using the following schema:
    
    
    {
      "type" : "record",
      "name" : "AvroPubsubMessageRecord",
      "namespace" : "com.google.cloud.industry.manufacturing.sfp.datalake.core",
      "fields" : [ {
        "name" : "attributes",
        "type" : {
          "type" : "map",
          "values" : "string"
        }
      }, {
        "name" : "message",
        "type" : {
          "type" : "bytes",
          "java-class" : "[B"
        }
      }, {
        "name" : "messageId",
        "type" : "string"
      }, {
        "name" : "timestamp",
        "type" : "long"
      } ]
    

The schema is composed by the following values:

  * **attributes** : Stores the Pub/Sub message attribute map.
  * **message** : Stores the raw message as received in the Pub/Sub topic `input-messages`.
  * **messageId** : ID set by Pub/Sub when receiving the message, it's written into all the sinks in order to have lineage of where the data came from.
  * **timestamp** : When the message was received by Pub/Sub.



The data is stored by default in a Cloud Storage bucket named `<project-id>-raw`. And then under a folder for the version, in this case `1.3`.

Date partitioning is then used to separate files by day with the format `dt=YYYY-MM-DD`.

Messages are grouped in 10 minute windows and 10 files are written in each of the windows, this data is used to produce the filenames. The following scripts shows an example of this:
    
    
    gs://<project-id>-raw/v1.3/dt=2023-08-08/gcsoutput2023-08-08T09:20:00.000Z-2023-08-08T09:30:00.000Z-pane-0-last-00-of-10avro
    gs://<project-id>-raw/v1.3/dt=2023-08-08/gcsoutput2023-08-08T09:20:00.000Z-2023-08-08T09:30:00.000Z-pane-0-last-01-of-10avro
    gs://<project-id>-raw/v1.3/dt=2023-08-08/gcsoutput2023-08-08T09:20:00.000Z-2023-08-08T09:30:00.000Z-pane-0-last-02-of-10avro
    gs://<project-id>-raw/v1.3/dt=2023-08-08/gcsoutput2023-08-08T09:20:00.000Z-2023-08-08T09:30:00.000Z-pane-0-last-03-of-10avro
    gs://<project-id>-raw/v1.3/dt=2023-08-08/gcsoutput2023-08-08T09:20:00.000Z-2023-08-08T09:30:00.000Z-pane-0-last-04-of-10avro
    gs://<project-id>-raw/v1.3/dt=2023-08-08/gcsoutput2023-08-08T09:20:00.000Z-2023-08-08T09:30:00.000Z-pane-0-last-05-of-10avro
    gs://<project-id>-raw/v1.3/dt=2023-08-08/gcsoutput2023-08-08T09:20:00.000Z-2023-08-08T09:30:00.000Z-pane-0-last-06-of-10avro
    gs://<project-id>-raw/v1.3/dt=2023-08-08/gcsoutput2023-08-08T09:20:00.000Z-2023-08-08T09:30:00.000Z-pane-0-last-07-of-10avro
    gs://<project-id>-raw/v1.3/dt=2023-08-08/gcsoutput2023-08-08T09:20:00.000Z-2023-08-08T09:30:00.000Z-pane-0-last-08-of-10avro
    gs://<project-id>-raw/v1.3/dt=2023-08-08/gcsoutput2023-08-08T09:20:00.000Z-2023-08-08T09:30:00.000Z-pane-0-last-09-of-10avro
    

### Reading from BigQuery

The following sections describe the data reading procedure from BigQuery.

## Processed data

Once data is processed by MDE it can be [configured](https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/store/how-to-configure-data-sinks) to be stored in Cloud Storage.

By default the data is saved in a bucket named `<project-id>-gcs-ingestion`. Then it's stored under a folder for the version, in this case `v1.3`, then each type is stored in its own folder `(default-discrete-records, default-numeric-records, etc)` and finally date partitioning is used to separate files by day with the format `dt=YYYY-MM-DD`.

As with Raw data, messages are grouped in 10 minute windows and 10 files are written in each of the windows, this data is used to produce the filenames, ie:
    
    
    gs://<project-id>-gcs-ingestion/v1.3/default-discrete-records/dt=2023-08-08/gcsoutput2023-08-08T09:40:00.000Z-2023-08-08T09:50:00.000Z-00000-of-00010.avro
    gs://<project-id>-gcs-ingestion/v1.3/default-discrete-records/dt=2023-08-08/gcsoutput2023-08-08T09:40:00.000Z-2023-08-08T09:50:00.000Z-00001-of-00010.avro
    gs://<project-id>-gcs-ingestion/v1.3/default-discrete-records/dt=2023-08-08/gcsoutput2023-08-08T09:40:00.000Z-2023-08-08T09:50:00.000Z-00002-of-00010.avro
    gs://<project-id>-gcs-ingestion/v1.3/default-discrete-records/dt=2023-08-08/gcsoutput2023-08-08T09:40:00.000Z-2023-08-08T09:50:00.000Z-00003-of-00010.avro
    gs://<project-id>-gcs-ingestion/v1.3/default-discrete-records/dt=2023-08-08/gcsoutput2023-08-08T09:40:00.000Z-2023-08-08T09:50:00.000Z-00004-of-00010.avro
    gs://<project-id>-gcs-ingestion/v1.3/default-discrete-records/dt=2023-08-08/gcsoutput2023-08-08T09:40:00.000Z-2023-08-08T09:50:00.000Z-00005-of-00010.avro
    gs://<project-id>-gcs-ingestion/v1.3/default-discrete-records/dt=2023-08-08/gcsoutput2023-08-08T09:40:00.000Z-2023-08-08T09:50:00.000Z-00006-of-00010.avro
    gs://<project-id>-gcs-ingestion/v1.3/default-discrete-records/dt=2023-08-08/gcsoutput2023-08-08T09:40:00.000Z-2023-08-08T09:50:00.000Z-00007-of-00010.avro
    gs://<project-id>-gcs-ingestion/v1.3/default-discrete-records/dt=2023-08-08/gcsoutput2023-08-08T09:40:00.000Z-2023-08-08T09:50:00.000Z-00008-of-00010.avro
    gs://<project-id>-gcs-ingestion/v1.3/default-discrete-records/dt=2023-08-08/gcsoutput2023-08-08T09:40:00.000Z-2023-08-08T09:50:00.000Z-00009-of-00010.avro
    

There's a different schema which only vary slightly for each Archetype, and so each type uses that corresponding schema. See the following examples:

`NumericDataSeries` archetype schema:
    
    
    {
      "type": "record",
      "namespace": "com.google.cloud.industry.manufacturing.sfp.datalake.storage.gcs",
      "name": "NumericDataSeriesGCSObject",
      "fields": [
        {
          "name": "id",
          "type": "string",
          "doc": "Unique record id"
        },
        {
          "name": "tag_name",
          "type": "string",
          "doc": "Name of the tag"
        },
        {
          "name": "type_name",
          "type": "string"
        },
        {
          "name": "type_version",
          "type": "int"
        },
        {
          "name": "embedded_metadata",
          "type": ["null", "string"],
          "default": null
        },
        {
          "name": "materialized_cloud_metadata",
          "type": ["null", "string"],
          "default": null
        },
        {
          "name": "cloud_metadata_ref",
          "type": ["null", "string"],
          "default": null
        },
        {
          "name": "source_message_id",
          "type": "string"
        },
        {
          "name": "event_timestamp",
          "type": {
            "type": "long",
            "logicalType": "timestamp-millis"
          }
        },
        {
          "name": "value",
          "type": "double"
        }
      ]
    }
    

`DiscreteDataSeries` archetype schema:
    
    
    {
      "type": "record",
      "name": "DiscreteDataSeriesGCSObject",
      "namespace": "com.google.cloud.industry.manufacturing.sfp.datalake.storage.gcs",
      "fields": [
        {
          "name": "id",
          "type": {
            "type": "string",
            "avro.java.string": "String"
          },
          "doc": "Unique record id"
        },
        {
          "name": "tag_name",
          "type": {
            "type": "string",
            "avro.java.string": "String"
          },
          "doc": "Name of the tag"
        },
        {
          "name": "type_name",
          "type": {
            "type": "string",
            "avro.java.string": "String"
          }
        },
        {
          "name": "type_version",
          "type": "int"
        },
        {
          "name": "embedded_metadata",
          "type": [
            "null",
            {
              "type": "string",
              "avro.java.string": "String"
            }
          ],
          "default": null
        },
        {
          "name": "materialized_cloud_metadata",
          "type": [
            "null",
            {
              "type": "string",
              "avro.java.string": "String"
            }
          ],
          "default": null
        },
        {
          "name": "cloud_metadata_ref",
          "type": [
            "null",
            {
              "type": "string",
              "avro.java.string": "String"
            }
          ],
          "default": null
        },
        {
          "name": "source_message_id",
          "type": {
            "type": "string",
            "avro.java.string": "String"
          }
        },
        {
          "name": "event_timestamp",
          "type": {
            "type": "long",
            "logicalType": "timestamp-millis"
          }
        },
        {
          "name": "data",
          "type": {
            "type": "string",
            "avro.java.string": "String"
          }
        }
      ]
    }
    

`ContinuousDataSeries` archetype schema:
    
    
    {
      "type": "record",
      "namespace": "com.google.cloud.industry.manufacturing.sfp.datalake.storage.gcs",
      "name": "ContinuousDataSeriesGCSObject",
      "fields": [
        {
          "name": "id",
          "type": "string",
          "doc": "Unique record id"
        },
        {
          "name": "tag_name",
          "type": "string",
          "doc": "Name of the tag"
        },
        {
          "name": "type_name",
          "type": "string"
        },
        {
          "name": "type_version",
          "type": "int"
        },
        {
          "name": "embedded_metadata",
          "type": ["null", "string"],
          "default": null
        },
        {
          "name": "materialized_cloud_metadata",
          "type": ["null", "string"],
          "default": null
        },
        {
          "name": "cloud_metadata_ref",
          "type": ["null", "string"],
          "default": null
        },
        {
          "name": "source_message_id",
          "type": "string"
        },
        {
          "name": "event_timestamp_start",
          "type": {
            "type": "long",
            "logicalType": "timestamp-millis"
          }
        },
        {
          "name": "event_timestamp_end",
          "type": {
            "type": "long",
            "logicalType": "timestamp-millis"
          }
        },
        {
          "name": "data",
          "type": "string"
        },
        {
          "name": "duration",
          "type": "long"
        }
      ]
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
