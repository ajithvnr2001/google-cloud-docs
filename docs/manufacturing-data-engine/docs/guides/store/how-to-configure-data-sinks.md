---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/store/how-to-configure-data-sinks/
title: Configure data sinks \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:47.071610+00:00
---

# Configure data sinks  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/store/how-to-configure-data-sinks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure data sinks

This guide describes how to configure data sinks in Manufacturing Data Engine (MDE).

MDE supports five data sinks for records:

  1. BigQuery
  2. Cloud Storage
  3. Bigtable and Federation API
  4. Pub/Sub (JSON format)
  5. Pub/Sub (Protobuf format)



## Record persistence

The following is an example for how you can configure individual sinks when creating a type:

### REST

`POST /configuration/v1/types`
    
    
    {
      "archetype": "<ARCHETYPE NAME>",
      "name": "<TYPE_NAME>",
      "metadataBuckets": [
        {
          "bucketName": "<BUCKET_NAME>",
          "version": "<BUCKET_VERSION>"
        }
      ],
      "storageSpecs": [
        {
          "sink": "BIG_QUERY",
          "disabled": "false",
          "materializeCloudMetadata": "false"
        },
        {
          "sink": "BIG_TABLE",
          "disabled": "false",
          "materializeCloudMetadata": "false"
        },
        {
          "sink": "GCS",
          "disabled": "false",
          "materializeCloudMetadata": "false"
        },
        {
          "sink": "PUBSUB_PROTO",
          "disabled": "false",
          "materializeCloudMetadata": "false"
        },
        {
          "sink": "PUBSUB_JSON",
          "disabled": "false",
          "materializeCloudMetadata": "false"
        }
      ]
    }
    

Replace the following:

  * `ARCHETYPE`: Name of the archetype. One of `DISCRETE_DATA_SERIES`, `CLUSTERED_DISCRETE_DATA_SERIES`, `NUMERIC_DATA_SERIES`, `CLUSTERED_NUMERIC_DATA_SERIES`, `CONTINUOUS_DATA_SERIES`, `CLUSTERED_CONTINUOUS_DATA_SERIES`.
  * `TYPE_NAME`: Name of the type to be created.
  * `BUCKET_NAME`: Name of the bucket to be associated to this type.
  * `BUCKET_VERSION`: Version of the bucket to be associated to this type.



### Console

  1. Open the **CLOUD TAGS** section in the web interface to modify the **Record** persistence setting for a given **Tag** :

![Tags section - List of tags](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-tags-list.png)

  2. Click the **Actions** icon for the tag you want to change the persistence settings.

  3. Chose the **View / Edit** option. The following side panel appears:

![Tags section - Edit tag](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-tags-edit-tag.png)

  4. Expand the section named **Storage Settings** and the list of all available persistence sinks will appear with a toggle button by the side of each of them:

![Tags section - Edit tag - Storage Specs](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-tags-edit-tag-storage-specs.png)

  5. Select the sinks that are active for the tag. All records ingested for this tag will be persisted in all the selected sinks.




Similarly, you can configure sinks when creating a new version on an existing type, like the following example:

### REST

`POST /configuration/v1/types/TYPE_NAME/versions`
    
    
    {
      "metadataBuckets": [
        {
          "bucketName": "EXISTING_BUCKET_NAME",
          "version": "EXISTING_BUCKET_VERSION"
        },
        {
          "bucketName": "NEW_BUCKET_NAME",
          "version": "NEW_BUCKET_VERSION"
        }
      ],
      "storageSpecs": [
        {
          "sink": "BIG_QUERY",
          "disabled": "false",
          "materializeCloudMetadata": "true"
        },
        {
          "sink": "BIG_TABLE",
          "disabled": "false",
          "materializeCloudMetadata": "false"
        },
        {
          "sink": "GCS",
          "disabled": "false",
          "materializeCloudMetadata": "false"
        },
        {
          "sink": "PUBSUB_PROTO",
          "disabled": "false",
          "materializeCloudMetadata": "false"
        },
        {
          "sink": "PUBSUB_JSON",
          "disabled": "false",
          "materializeCloudMetadata": "false"
        }
      ]
    }
    

Replace the following:

  * `TYPE_NAME`: Name of the type for which a new version is created
  * `EXISTING_BUCKET_NAME`: Name of the existing bucket already associated to this type.
  * `EXISTING_BUCKET_VERSION`: Version of the existing bucket already associated to this type.
  * `NEW_BUCKET_NAME`: name of the new bucket.
  * `NEW_BUCKET_VERSION`: Version of the new bucket.



### Console

  1. Open the **TYPES** section of the top menu to change the Storage Settings at **Type** level:

![Types section - list of Types](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-types-list.png)

  2. Select in the **Actions** icon of the **Type** you want to edit the **View / Edit** option. The **Edit Type Version** side menu is displayed.

  3. Expand the **Storage Settings** panel to access the persistence settings for the **Type** :

![Types section - Create Type - Storage Settings](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-types-new-storage-settings.png)

  4. Select each sink where the Records of the tags belonging to this Type will be persisted by default. The storage specification is inherited by the tags when they are created. The storage specification can be modified at the tag level at any time.




## Metadata instance materialization

Metadata instance materialization can be configured for each sink individually. for more information, see [instance materialization](https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/metadata#instance_materialization).

## Overriding default type version storage specifications for individual tags

You can also override the default storage specifications for a type version for individual tags. That means, tag configuration settings for a type version override the default settings for that type version.

## Sink-specific considerations

The following sections outline some sink-specific considerations:

### BigQuery

When you create a data type, MDE automatically creates a new table for it in the `mde_data` dataset. You can configure whether records are persisted to this table by enabling the BigQuery sink on a type version or tag for a type version.

### Bigtable Federation API

If you have provisioned a Bigtable cluster, you can configure whether records are persisted to Bigtable so that you can access them using the Federation API.

Cloud metadata instances are not persisted standalone in Bigtable. If you need to have Cloud metadata in records that you retrieve from Bigtable using Federation API, you should set the value of `materializeCloudMetadata` to `true` for the Bigtable sink.

### Cloud Storage

Records are stored in Cloud Storage bucket called `<project_id>-gcs-ingestion` in AVRO files using Hive partitioning using a ten minute window and ten partitions per window. Records are grouped in folders by type. Cloud metadata instances are not sent to the Cloud Storage sink standalone. If you need have Cloud metadata in records in Cloud Storage, you should set the value of `materializeCloudMetadata` to `true` for the Cloud Storage sink.

### Pub/Sub: Proto and JSON

MDE provides two flavors of the Pub/Sub sink - one that provides records in JSON data format and another that provides messages in Protobuf data format. See the reference section for the respective data schemas. 

The JSON formatted record stream is sent to the `mde-tag-stream-json` Pub/Sub topic, and the Protobuf formatted record stream is sent to the `mde-tag-stream-proto`. Cloud metadata instances are not sent to the respective Pub/Sub topics. If you need have Cloud metadata in records in sent to Pub/Sub, you should set the value of `materializeCloudMetadata` to `true` for the Pub/Sub sinks. If not explicitly enabled on a type, the Pub/Sub sinks are disabled by default.

## Persistence of metadata, logs and configuration data

MDE always persists metadata instances, logs and configuration data in the `mde_dimension` and `mde_system` datasets in BigQuery. Additionally, MDE always persists raw source messages in Cloud Storage. The persistence of this data can't be disabled.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
