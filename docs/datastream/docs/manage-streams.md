---
url: https://docs.cloud.google.com/datastream/docs/manage-streams/
title: Manage streams \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:42.136228+00:00
---

# Manage streams  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/manage-streams/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Manage streams Stay organized with collections  Save and categorize content based on your preferences. 

The Datastream API lets you automate your data replication workflows through REST API calls or the Google Cloud CLI. You can create, validate, modify, and delete streams, or retrieve and list streams and stream objects.

You can also start, pause, resume, or recover streams, manage object backfill, adjust task concurrency, and stream large Oracle objects. For command reference details, see [`gcloud datastream streams`](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/streams). For an end-to-end walkthrough, see [Use Datastream APIs](https://docs.cloud.google.com/datastream/docs/using-datastream-apis).

## Create a stream

In this section, you learn how to create a stream that's used to transfer data from your source to a destination. The examples that follow aren't comprehensive, but rather highlight specific features of Datastream. To address your specific use case, use these examples together with the Datastream [API reference documentation](https://docs.cloud.google.com/datastream/docs/reference/rest).

This section covers the following use cases:

  * Stream from Oracle to Cloud Storage
  * Stream from MySQL to BigQuery
  * Stream from PostgreSQL to BigQuery
  * Define a set of objects to include in the stream
  * Backfill all objects included in the stream
  * Exclude objects from the stream
  * Exclude objects from the backfill
  * Define CMEK for encrypting data at rest
  * Define write mode for a stream
  * Stream to a different project in BigQuery
  * Stream data to Apache Iceberg tables
  * Stream from MongoDB using strict JSON mode



### Example 1: Stream specific objects to BigQuery

In this example, you learn how to:

  * Stream from MySQL to BigQuery
  * Include a set of objects in the stream
  * Define write mode for the stream as append-only
  * Backfill all objects included in the stream



The following is a request to pull all tables from `schema1` and two specific tables from `schema2`: `tableA` and `tableC`. The events are written to a dataset in BigQuery.

The request doesn't include the `customerManagedEncryptionKey` parameter, therefore the Google Cloud internal key management system is used to encrypt your data instead of CMEK.

The `backfillAll` parameter associated with performing the historical backfill (or snapshot) is set to an empty dictionary (`{}`), which means that Datastream backfills the historical data from all tables included in the stream.

### REST
    
    
    POST https://datastream.googleapis.com/v1/projects/myProjectId1/locations/us-central1/streams?streamId=mysqlCdcStream
    {
      "displayName": "MySQL CDC to BigQuery",
      "sourceConfig": {
        "sourceConnectionProfileName": "/projects/myProjectId1/locations/us-central1/streams/mysqlCp",
        "mysqlSourceConfig": {
          "includeObjects": {
            "mysqlDatabases": [
              { "database": "schema1" },
              {
                "database": "schema2",
                "mysqlTables": [
                  {
                    "table": "tableA",
                    "table": "tableC"
                  }
                ]
              }
            ]
          },
        }
      },
      "destinationConfig": {
        "destinationConnectionProfileName": "BigQueryCp",
        "bigqueryDestinationConfig": {
          "sourceHierarchyDatasets": {
            "datasetTemplate": {
              "location": "us",
              "datasetIdPrefix": "prefix_"
            }
          },
          "dataFreshness": "900s"
        }
      },
      "backfillAll": {}
    }

### gcloud

For more information about using `gcloud` to create a stream, see [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/streams/create).

### Example 2: Exclude specific objects from a stream with a PostgreSQL source

In this example, you learn how to:

  * Stream from PostgreSQL to BigQuery
  * Exclude objects from the stream
  * Exclude objects from the backfill



The following code shows a request to create a stream that's used to transfer data from a source PostgreSQL database to BigQuery. When creating a stream from a source PostgreSQL database, you need to specify two additional, PostgreSQL-specific fields in your request:

  * `replicationSlot`: a replication slot is a prerequisite for configuring a PostgreSQL database for replication. You need to create a replication slot for each stream.
  * `publication`: a publication is a group of tables that you want to replicate changes from. The publication name must exist in the database before starting a stream. At a minimum, the publication has to include the tables specified in the stream's `includeObjects` list.



The `backfillAll` parameter associated with performing the historical backfill (or snapshot) is set to exclude one table.

### REST
    
    
    POST https://datastream.googleapis.com/v1/projects/myProjectId1/locations/
    us-central1/streams?streamId=myPostgresStream
    {
      "displayName": "PostgreSQL to BigQueryCloud Storage",
      "sourceConfig": {
        "sourceConnectionProfileName": "/projects/myProjectId1/locations/us-central1/connectionProfiles/postgresCp",
        "postgresqlSourceConfig": {
          "replicationSlot": "replicationSlot1",
          "publication": "publicationA",
          "includeObjects": {
            "postgresqlSchemas": {
              "schema": "schema1"
            }
          },
          "excludeObjects": {
            "postgresqlSchemas": [
              { "schema": "schema1",
            "postgresqlTables": [
              {
                "table": "tableA",
                "postgresqlColumns": [
                  { "column": "column5" }
                  ]
                  }
                ]
              }
            ]
          }
        }
      },
      "destinationConfig": {
        "destinationConnectionProfileName": "BigQueryCp",
        "bigqueryDestinationConfig": {
          "dataFreshness": "900s",
          "sourceHierarchyDatasets": {
            "datasetTemplate": {
               "location": "us",
               "datasetIdPrefix": "prefix_"
            }
          }
        }
      },
      "backfillAll": {
        "postgresqlExcludedObjects": {
            "postgresqlSchemas": [
              { "schema": "schema1",
                "postgresqlTables": [
                  { "table": "tableA" }
                ]
              }
            ]
          }
        }
      }

### gcloud

For more information about using `gcloud` to create a stream, see [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/streams/create).

### Example 3: Specify append-only write mode for a stream

When streaming to BigQuery, you can define the write mode: `merge` or `appendOnly`. For more information, see [Configure write mode](https://docs.cloud.google.com/datastream/docs/destination-bigquery#configure-write-mode).

If you don't specify the write mode in your request to create a stream, the default `merge` mode is used.

The following request shows how to define the `appendOnly` mode when you create a MySQL to BigQuery stream.

### REST
    
    
    POST https://datastream.googleapis.com/v1/projects/myProjectId1/locations/us-central1/streams?streamId=appendOnlyStream
    {
      "displayName": "My append-only stream",
      "sourceConfig": {
        "sourceConnectionProfileName": "/projects/myProjectId1/locations/us-central1/streams/mysqlCp",
        "mysqlSourceConfig": {
          "includeObjects": {
            "mysqlDatabases": [
              { "database": "myMySqlDb"
              }
            ]
          }
        }
      },
      "destinationConfig": {
        "destinationConnectionProfileName": "BigQueryCp",
        "bigqueryDestinationConfig": {
          "sourceHierarchyDatasets": {
            "datasetTemplate": {
              "location": "us",
              "datasetIdPrefix": "prefix_"
            }
          },
          "appendOnly": {}
        }
      },
      "backfillAll": {}
    }

### gcloud

For more information about using `gcloud` to create a stream, see [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/streams/create).

### Example 4: Stream to a different project in BigQuery

If you created your Datastream resources in one project, but want to stream to a different project in BigQuery, then you can do that using a request similar to the one that follows.

If you specify `sourceHierarchyDatasets` for your destination dataset, then you need to populate the `projectId` field.

If you specify `singleTargetDataset` for your destination dataset, then populate the `datasetId` field in the `projectId:datasetId` format.

### REST

For `sourceHierarchyDatasets`:
    
    
    POST https://datastream.googleapis.com/v1/projects/myProjectId1/locations/us-central1/streams?streamId=crossProjectBqStream1
    {
      "displayName": "My cross-project stream",
      "sourceConfig": {
        "sourceConnectionProfileName": "/projects/myProjectId1/locations/us-central1/streams/mysqlCp",
        "mysqlSourceConfig": {
          "includeObjects": {
            "mysqlDatabases": [
              { "database": "myMySqlDb"
              }
            ]
          }
        }
      },
      "destinationConfig": {
        "destinationConnectionProfileName": "BigQueryCp",
        "bigqueryDestinationConfig": {
          "sourceHierarchyDatasets": {
            "datasetTemplate": {
              "location": "us",
              "datasetIdPrefix": "prefix_"
            },
            "projectId": "myProjectId2"
          }
        }
      },
      "backfillAll": {}
    }

For `singleTargetDataset`:
    
    
    POST https://datastream.googleapis.com/v1/projects/myProjectId1/locations/us-central1/streams?streamId=crossProjectBqStream2
    {
      "displayName": "My cross-project stream",
      "sourceConfig": {
        "sourceConnectionProfileName": "/projects/myProjectId1/locations/us-central1/streams/mysqlCp",
        "mysqlSourceConfig": {
          "includeObjects": {
            "mysqlDatabases": [
              { "database": "myMySqlDb"
              }
            ]
          }
        }
      },
      "destinationConfig": {
        "destinationConnectionProfileName": "BigQueryCp",
        "bigqueryDestinationConfig": {
          "singleTargetDataset": {
            "datasetId": "myProjectId2:myDatasetId"
          },
        }
      },
      "backfillAll": {}
    }

### gcloud

For `sourceHierarchyDatasets`:
    
    
      datastream streams create crossProjectBqStream1 --location=us-central1
      --display-name=my-cross-project-stream --source=source-cp --mysql-source-config=mysql_source_config.json
      --destination=destination-cp --bigquery-destination-config=source_hierarchy_cross_project_config.json
      --backfill-none
      

The contents of the `source_hierarchy_cross_project_config.json` configuration file:
    
    
      {"sourceHierarchyDatasets": {"datasetTemplate": {"location": "us-central1", "datasetIdPrefix": "prefix_"}, "projectId": "myProjectId2"}}
      

For `singleTargetDataset`:
    
    
      datastream streams create crossProjectBqStream --location=us-central1
      --display-name=my-cross-project-stream --source=source-cp --mysql-source-config=mysql_source_config.json
      --destination=destination-cp --bigquery-destination-config=single_target_cross_project_config.json
      --backfill-none
      

The contents of the `single_target_cross_project_config.json` configuration file:
    
    
      {"singleTargetDataset": {"datasetId": "myProjectId2:myDatastetId"}}
      

For more information about using `gcloud` to create a stream, see [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/streams/create).

### Example 5: Stream to a Cloud Storage destination

In this example, you learn how to:

  * Stream from Oracle to Cloud Storage
  * Define a set of objects to include in the stream
  * Define CMEK for encrypting data at rest



The following request shows how to create a stream that writes the events to a bucket in Cloud Storage.

In this example request, the events are written in the JSON output format, and a new file is created every 100 MB or 30 seconds (overriding the default values of 50 MB and 60 seconds).

For the JSON format, you can:

  * Include a unified types schema file in the path. As a result, Datastream writes two files to Cloud Storage: a JSON data file and an Avro schema file. The schema file has the same name as the data file, with a `.schema` extension.

  * Enable gzip compression to have Datastream compress the files that are written to Cloud Storage.




By using the `backfillNone` parameter, the request specifies that only ongoing changes are streamed into the destination, with no backfill.

The request specifies the customer-managed encryption key parameter which lets you control the keys used to encrypt data at rest within a Google Cloud project. The parameter refers to the CMEK that Datastream uses to encrypt data that's streamed from the source to the destination. It also specifies the key ring for your CMEK.

For more information about key rings, see [Cloud KMS resources](https://docs.cloud.google.com/kms/docs/resource-hierarchy). For more information about protecting your data using encryption keys, see [Cloud Key Management Service (KMS)](https://docs.cloud.google.com/kms/docs).

### REST
    
    
    POST https://datastream.googleapis.com/v1/projects/myProjectId1/locations/
    us-central1/streams?streamId=myOracleCdcStream
    {
      "displayName": "Oracle CDC to Cloud Storage",
      "sourceConfig": {
        "sourceConnectionProfileName": "/projects/myProjectId1/locations/us-central1/
        connectionProfiles/OracleCp",
        "oracleSourceConfig": {
          "includeObjects": {
            "oracleSchemas": [
              {
                "schema": "schema1"
              }
            ]
          }
        }
      },
      "destinationConfig": {
        "destinationConnectionProfileName": "GcsBucketCp",
        "gcsDestinationConfig": {
          "path": "/folder1",
          "jsonFileFormat": {
            "schemaFileFormat": "AVRO_SCHEMA_FILE"
          },
          "fileRotationMb": 100,
          "fileRotationInterval": 30
        }
      },
      "customerManagedEncryptionKey": "projects/myProjectId1/locations/us-central1/
      keyRings/myRing/cryptoKeys/myEncryptionKey",
      "backfillNone": {}
    }

### gcloud

For more information about using `gcloud` to create a stream, see [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/streams/create).

### Example 6: Stream to an Apache Iceberg table

In this example, you learn how to configure a stream to replicate data from a MySQL database to an Apache Iceberg table in `append-only` mode. Before you create the request, make sure that you've completed the following steps:

  * Have a Cloud Storage bucket where you want to store your data
  * Create a [Cloud resource connection](https://docs.cloud.google.com/bigquery/docs/create-cloud-resource-connection)
  * Grant your Cloud resource connection access to the Cloud Storage bucket



You can then use the following request to create your stream:

### REST
    
    
    POST https://datastream.googleapis.com/v1/projects/myProjectId1/locations/us-central1/streams?streamId=mysqlIcebergStream
    {
      "displayName": "MySQL to Apache Iceberg stream",
      "sourceConfig": {
        "sourceConnectionProfileName": "/projects/myProjectId1/locations/us-central1/streams/mysqlIcebergCp",
        "mysqlSourceConfig": {
          "includeObjects": {
            "mysqlDatabases": [
              {
                "database": "my-mysql-database"
              }
            ]
          }
        }
      },
      "destinationConfig": {
        "destinationConnectionProfileName": "projects/myProjectId1/locations/us-central1/connectionProfiles/my-bq-cp-id",
        "bigqueryDestinationConfig": {
          "blmtConfig": {
            "bucket": "my-gcs-bucket-name",
            "rootPath": "my/folder",
            "connectionName": "my-project-id.us-central1.my-bigquery-connection-name",
            "fileFormat": "PARQUET",
            "tableFormat": "ICEBERG"
            },
          "singleTargetDataset": {
            "datasetId": "my-project-id:my-bigquery-dataset-id"
          },
          "appendOnly": {}
        }
      },
      "backfillAll": {}
    }

### gcloud
    
    
    datastream streams create mysqlIcebergStream --location=us-central1
    --display-name=mysql-to-bl-stream --source=source --mysql-source-config=mysql_source_config.json
    --destination=destination --bigquery-destination-config=bl_config.json
    --backfill-none

The contents of the `mysql_source_config.json` source configuration file:
    
    
    {"excludeObjects": {}, "includeObjects": {"mysqlDatabases":[{"database":"my-mysql-database"}]}}

The contents of the `bl_config.json` configuration file:
    
    
    { "blmtConfig": { "bucket": "my-gcs-bucket-name", "rootPath": "my/folder", "connectionName": "my-project-id.us-central1.my-bigquery-connection-name", "fileFormat": "PARQUET", "tableFormat": "ICEBERG" }, "singleTargetDataset": {"datasetId": "my-project-id:my-bigquery-dataset-id"}, "appendOnly": {} }

### Terraform
    
    
    resource "google_datastream_stream" "stream" {
      stream_id    = "mysqlBlStream"
      location     = "us-central1"
      display_name = "MySQL to Apache Iceberg stream"
    
      source_config {
        source_connection_profile = "/projects/myProjectId1/locations/us-central1/streams/mysqlBlCp"
        mysql_source_config {
          include_objects {
            mysql_databases {
              database = "my-mysql-database"
            }
          }
        }
      }
    
      destination_config {
        destination_connection_profile = "projects/myProjectId1/locations/us-central1/connectionProfiles/my-bq-cp-id"
        bigquery_destination_config {
          single_target_dataset {
            dataset_id = "my-project-id:my-bigquery-dataset-id"
          }
          blmt_config {
            bucket          = "my-gcs-bucket-name"
            table_format    = "ICEBERG"
            file_format     = "PARQUET"
            connection_name = "my-project-id.us-central1.my-bigquery-connection-name"
            root_path       = "my/folder"
          }
          append_only {}
        }
      }
    
      backfill_none {}
    }
        

### Example 7: Stream from MongoDB using strict JSON mode

In this example, you configure a stream to replicate data from a MongoDB source to BigQuery using strict JSON mode.

By default, Datastream uses canonical JSON mode (`CANONICAL`) to prioritize data fidelity. If your downstream applications require compatibility with standard JSON parsers, you can specify strict JSON mode (`STRICT`).

When creating a stream from a MongoDB source:

  * Valid values for `jsonMode` in the API are `CANONICAL` (default) and `STRICT`.
  * In the gcloud CLI, there is no standalone flag for the JSON mode. Instead, configure MongoDB source settings through a configuration file passed to the `--mongodb-source-config` flag.



### REST

In the Datastream REST API, set `jsonMode` to `"STRICT"` within the `sourceConfig.mongodbSourceConfig` object:
    
    
    POST https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/streams?streamId=STREAM_ID
    {
      "displayName": "STREAM_DISPLAY_NAME",
      "sourceConfig": {
        "sourceConnectionProfile": "projects/PROJECT_ID/locations/LOCATION/connectionProfiles/SOURCE_PROFILE",
        "mongodbSourceConfig": {
          "jsonMode": "STRICT",
          "includeObjects": {
            "databases": [
              {
                "database": "DATABASE_NAME",
                "collections": [
                  {
                    "collection": "COLLECTION_NAME"
                  }
                ]
              }
            ]
          }
        }
      },
      "destinationConfig": {
        "destinationConnectionProfile": "projects/PROJECT_ID/locations/LOCATION/connectionProfiles/DEST_PROFILE",
        "bigqueryDestinationConfig": {
          "singleTargetDataset": {
            "datasetId": "PROJECT_ID:DATASET_ID"
          }
        }
      }
    }

Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION`: the region where the stream is created, such as `us-central1`.
  * `STREAM_ID`: the identifier of the stream.
  * `STREAM_DISPLAY_NAME`: a user-friendly name for the stream.
  * `SOURCE_PROFILE`: the identifier of the source MongoDB connection profile.
  * `DEST_PROFILE`: the identifier of the destination connection profile.
  * `DATABASE_NAME`: the name of the database in the source MongoDB cluster.
  * `COLLECTION_NAME`: the name of the collection in the database.
  * `DATASET_ID`: the identifier of the destination dataset in BigQuery.



### gcloud

To create a stream with a MongoDB source and strict JSON mode using the gcloud CLI:

  1. Create a source configuration file in JSON or YAML format specifying `"jsonMode": "STRICT"` and the objects to replicate.



JSON configuration file, for example, `mongo_source_config.json`:
    
    
    {
      "jsonMode": "STRICT",
      "includeObjects": {
        "databases": [
          {
            "database": "DATABASE_NAME",
            "collections": [
              {
                "collection": "COLLECTION_NAME"
              }
            ]
          }
        ]
      }
    }

YAML configuration file, for example, `mongo_source_config.yaml`:
    
    
    jsonMode: STRICT
    includeObjects:
      databases:
        - database: DATABASE_NAME
          collections:
            - collection: COLLECTION_NAME

  2. Pass the configuration file to the `--mongodb-source-config` flag when creating the stream:


    
    
    gcloud datastream streams create STREAM_ID \
        --location=LOCATION \
        --display-name="STREAM_DISPLAY_NAME" \
        --source=projects/PROJECT_ID/locations/LOCATION/connectionProfiles/SOURCE_PROFILE \
        --destination=projects/PROJECT_ID/locations/LOCATION/connectionProfiles/DEST_PROFILE \
        --mongodb-source-config=mongo_source_config.json \
        --bigquery-destination-config=bigquery_destination_config.json
    

The contents of the `bigquery_destination_config.json` configuration file:
    
    
    {
      "singleTargetDataset": {
        "datasetId": "PROJECT_ID:DATASET_ID"
      }
    }

Replace the following:

  * `STREAM_ID`: the identifier of the stream.
  * `LOCATION`: the region where the stream is created, such as `us-central1`.
  * `STREAM_DISPLAY_NAME`: a user-friendly name for the stream.
  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `SOURCE_PROFILE`: the identifier of the source MongoDB connection profile.
  * `DEST_PROFILE`: the identifier of the destination connection profile.
  * `DATABASE_NAME`: the name of the database in the source MongoDB cluster.
  * `COLLECTION_NAME`: the name of the collection in the database.
  * `DATASET_ID`: the identifier of the destination dataset in BigQuery.



For more information about using `gcloud` to create a stream, see [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/streams/create).

## Validate the definition of a stream

Before creating a stream, you can validate its definition. This way, you can ensure that all validation checks pass, and that the stream will run successfully when created.

Validating a stream checks:

  * Whether the source is configured properly to allow Datastream to stream data from it.
  * Whether the stream can connect to both the source and the destination.
  * The end-to-end configuration of the stream.



To validate a stream, add `&validate_only=true` to the URL preceding the body of your request:
    
    
    POST "https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/streams?streamId=STREAM_ID**& validate_only=true**"

After you make this request, you'll see the validation checks that Datastream runs for your source and destination, along with whether the checks pass or fail. For any validation check that doesn't pass, information appears as to why it failed and what to do to rectify the problem.

For example, suppose you have a customer-managed encryption key (CMEK) that you want Datastream to use to encrypt data that's streamed from the source to the destination. As part of validating the stream, Datastream will verify that the key exists, and that Datastream has permissions to use the key. If either of these conditions aren't met, then when you validate the stream, the following error message will be returned:
    
    
    CMEK_DOES_NOT_EXIST_OR_MISSING_PERMISSIONS

To resolve this issue, verify that the key that you provided exists, and that the Datastream service account has the `cloudkms.cryptoKeys.get` permission for the key.

After making the appropriate corrections, make the request again to ensure that all validation checks pass. For the preceding example, the `CMEK_VALIDATE_PERMISSIONS` check will no longer return an error message, but will have a status of `PASSED`.

To learn more about the validation checks that Datastream runs for your source and destination, see [Create a stream](https://docs.cloud.google.com/datastream/docs/create-a-stream#validationchecks).

For more information about the `customerManagedEncryptionKey` parameter, see Create a stream.

## Get information about a stream

The following code shows a request to retrieve information about a stream. This information includes:

  * The stream's name (unique identifier)
  * A user-friendly name for the stream (display name)
  * Timestamps of when the stream was created and last updated
  * Information about the source and destination connection profiles associated with the stream
  * The stream's state



### REST
    
    
    GET https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/streams/STREAM_ID

The response appears, as follows:
    
    
    {
      "name": "myOracleCdcStream",
      "displayName": "Oracle CDC to Cloud Storage",
      "createTime": "2019-12-15T15:01:23.045123456Z",
      "updateTime": "2019-12-15T15:01:23.045123456Z",
      "sourceConfig": {
        "sourceConnectionProfileName": "myOracleDb",
        "oracleSourceConfig": {
          "includeObjects": {
            "oracleSchemas": [
              {
                "schema": "schema1"
              },
              {
                "schema": "schema3",
                "oracleTables": [
                  { "table": "tableA" },
                  { "table": "tableC" }
                ]
              }
            ]
          }
        }
      },
      "destinationConfig": {
        "destinationConnectionProfileName": "myGcsBucket",
        "gcsDestinationConfig": {
          "path": "/folder1",
          "avroFileFormat": {},
          "fileRotationMb": 100,
          "fileRotationInterval": 60
        }
      },
      "state": "RUNNING"
      "customerManagedEncryptionKey": "projects/myProjectId1/locations/us-central1/
      keyRings/myRing/cryptoKeys/myEncryptionKey",
      "backfillAll": {}
    }

### gcloud

For more information about using `gcloud` to retrieve information about your stream, see the [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/streams/describe).

## List streams

The following code shows a request to retrieve a list of all streams in the specified project and location.

### REST
    
    
    GET https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/streams

### gcloud

For more information about using `gcloud` to retrieve information about all of your streams, see the [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/streams/list).

## List objects of a stream

The following code shows a request to retrieve information about all objects of a stream.

### REST
    
    
    GET https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/streams/STREAM_ID/objects

### gcloud

For more information about using `gcloud` to retrieve information about all objects of your stream, see the [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/objects/list).

The list of objects that's returned may look similar to the following:

### REST
    
    
    {
      "streamObjects": [
        {
          "name": "projects/myProjectId1/locations/us-central1/streams/myStream/
          objects/object1",
          "displayName": "employees.salaries",
          "backfillJob": {
            "state": "ACTIVE",
            "trigger": "AUTOMATIC",
            "lastStartTime": "2021-10-18T12:12:26.344878Z"
          },
          "sourceObject": {
            "mysqlIdentifier": {
              "database": "employees",
              "table": "salaries"
            }
          }
        },
        {
          "name": "projects/myProjectId1/locations/us-central1/streams/myStream/
          objects/object2",
          "displayName": "contractors.hours",
          "sourceObject": {
            "mysqlIdentifier": {
              "database": "contractors",
              "table": "hours"
            }
          }
        },
        {
          "name": "projects/myProjectId1/locations/us-central1/streams/myStream/
          objects/object3",
          "displayName": "employees.departments",
          "backfillJob": {
            "state": "COMPLETED",
            "trigger": "AUTOMATIC",
            "lastStartTime": "2021-10-18T11:26:12.869880Z",
            "lastEndTime": "2021-10-18T11:26:28.405653Z"
          },
          "sourceObject": {
            "mysqlIdentifier": {
              "database": "employees",
              "table": "departments"
            }
          }
        }
      ]
    }

### gcloud

For more information about using `gcloud` to list objects of a stream, see the [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/streams/update).

## Start a stream

The following code shows a request to start a stream.

By using the `updateMask` parameter in the request, only the fields that you specify have to be included in the body of the request. To start a stream, change the value in the `state` field from `CREATED` to `RUNNING`.

When a stream is started, the status first changes to `STARTING`. This signifies that the stream is in the process of being started and validated.

  * If the stream is valid, then the status of the stream changes from `STARTING` to `RUNNING`.
  * If the stream isn't valid, then the status of the stream changes from `STARTING` back to `CREATED`. There will be errors that you can address to [rectify the problems of the stream](https://docs.cloud.google.com/datastream/docs/troubleshoot-a-stream). For example, if errors are associated with the connectivity information of the stream, then modify the stream definition. After resolving all problems of the stream, start it again, and the status changes to `STARTING`, and then to `RUNNING`.



### REST
    
    
    PATCH https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/streams/STREAM_ID?updateMask=state
    {
      "state": "RUNNING"
    }

### gcloud

For more information about using `gcloud` to start your stream, see the [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/streams/update).

If you want to start a stream without validating it, then add `&force=true` to the request.

For example: PATCH https://datastream.googleapis.com/v1/projects/myProjectId1/locations/ us-central1/streams/myOracleCdcStream?updateMask=state**& force=true**

## Pause a stream

The following code shows a request to pause a running stream.

For this example, the field specified for the `updateMask` parameter is the `state` field. By pausing the stream, you're changing its state from `RUNNING` to `PAUSED`.

When a stream is paused, Datastream won't pull any new data from the source database into the destination. However, some data may continue to be written to the destination because "in flight" data will continue to flow. 

Therefore, after you pause a stream, the status of the stream changes from `RUNNING` to `DRAINING`. Draining a stream is the process of emptying the stream so that it doesn't contain any data. After the stream is drained of all data, then the status of the stream changes from `DRAINING` to `PAUSED`.

### REST
    
    
    PATCH https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/streams/STREAM_ID?updateMask=state
    {
      "state": "PAUSED"
    }

### gcloud

For more information about using `gcloud` to pause your stream, see the [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/streams/update).

## Resume a stream

The following code shows a request to resume a paused stream.

For this example, the field specified for the `updateMask` parameter is the `state` field. By resuming the stream, you're changing its state from `PAUSED` to `RUNNING`.

### REST
    
    
    PATCH https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/streams/STREAM_ID?updateMask=state
    {
      "state": "RUNNING"
    }

### gcloud

For more information about using `gcloud` to resume your stream, see the [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/streams/update).

## Recover a stream

You can recover a permanently failed stream using the `RunStream` method. Each source database type has its own definition of what stream recovery operations are possible. For more information, see [Recover a stream](https://docs.cloud.google.com/datastream/docs/recover-a-stream).

### Recover a stream for a MySQL or an Oracle source

The following code samples show requests to recover a stream for a MySQL or an Oracle source from various log file positions:

### REST

Recover a stream from the current position. This is the default option:
    
    
    POST https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/streams/STREAM_ID:run

Recover a stream from the next available position:
    
    
    POST https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/streams/STREAM_ID:run
    {
      "cdcStrategy": {
        "nextAvailableStartPosition": {}
      }
    }

Recover a stream from the most recent position:
    
    
    POST https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/streams/STREAM_ID:run
    {
      "cdcStrategy": {
        "mostRecentStartPosition": {}
      }
    }

Recover a stream from a specific position (MySQL binlog-based replication):
    
    
    POST https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/streams/STREAM_ID:run
    {
      "cdcStrategy": {
        "specificStartPosition": {
          "mysqlLogPosition": {
            "logFile": "NAME_OF_THE_LOG_FILE"
            "logPosition": POSITION
          }
        }
      }
    }

Replace the following:

  * NAME_OF_THE_LOG_FILE: The name of the log file from which you want to recover your stream
  * POSITION: The position in the log file from which you want to recover your stream. If you don't provide the value, Datastream recovers the stream from the head of the file.



For example:
    
    
    POST https://datastream.googleapis.com/v1/projects/myProjectId1/locations/
    us-central1/streams/myStreamId1:run
    {
      "cdcStrategy": {
        "specificStartPosition": {
          "mysqlLogPosition": {
            "logFile": "binlog.001"
            "logPosition": 4
          }
        }
      }
    }

Recover a stream from a specific position (MySQL GTID-based replication):
    
    
    POST https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/streams/STREAM_ID:run
    {
      "cdcStrategy": {
        "specificStartPosition": {
          "mysqlGtidPosition": {
            "gtidSet": "GTID_SET"
          }
        }
      }
    }

Replace GTID_SET with one or more single GTIDs or ranges of GTIDs from which you want to recover your stream.

For example:
    
    
    POST https://datastream.googleapis.com/v1/projects/myProjectId1/locations/
    us-central1/streams/myStreamId1:run
    {
      "cdcStrategy": {
        "specificStartPosition": {
          "mysqlGtidPosition": {
            "gtidSet": "22cc56f5-3862-379a-9af5-051c59baef9d:1-561143685:561143688-591036613,b8d7df02-832b-32b9-bec7-2018806b76f6:1-3"
          }
        }
      }
    }

Recover a stream from a specific position (Oracle):
    
    
    POST https://datastream.googleapis.com/v1/projects/[project-id]/locations/
    [location]/streams/[stream-id]:run
    {
      "cdcStrategy": {
        "specificStartPosition": {
          "oracleScnPosition": {
            "scn": scn
          }
        }
      }
    }

Replace scn with the system change number (SCN) in the redo log file from which you want to recover your stream. This field is mandatory. 

For example:
    
    
    POST https://datastream.googleapis.com/v1/projects/myProjectId1/locations/
    us-central1/streams/myStreamId1:run
    {
      "cdcStrategy": {
        "specificStartPosition": {
          "oracleScnPosition": {
            "scn": 234234
          }
        }
      }
    }
    

For more information about available recovery options, see [Recover a stream](https://docs.cloud.google.com/datastream/docs/recover-a-stream).

### gcloud

Recovering a stream using `gcloud` isn't supported.

### Recover a stream for a PostgreSQL source

The following code sample shows a request to recover a stream for a PostgreSQL source. During recovery, the stream starts reading from the first log sequence number (LSN) in the replication slot configured for the stream.

### REST
    
    
    POST https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/streams/STREAM_ID:run
    {
      "cdcStrategy": {
        "nextAvailableStartPosition": {}
      }
    }

For example:
    
    
    POST https://datastream.googleapis.com/v1/projects/myProjectId1/locations/
    us-central1/streams/myStreamId1:run

If you want to change the replication slot, update the stream with the new replication slot name first:
    
    
    PATCH https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/streams/STREAM_ID?updateMask=sourceConfig.postgresqlSourceConfig.replicationSlot
    {
      "sourceConfig": {
        "postgresqlSourceConfig": {
          "replicationSlot": "NEW_REPLICATION_SLOT_NAME"
        }
      }
    }

### gcloud

Recovering a stream using `gcloud` isn't supported.

### Recover a stream for a SQL Server source

The following code samples show example requests to recover a stream for a SQL Server source.

### REST

Recover a stream from the first available position:
    
    
    POST https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/streams/STREAM_ID:run

For example:
    
    
    POST https://datastream.googleapis.com/v1/projects/myProjectId1/locations/
    us-central1/streams/mySqlServerStreamId:run

Recover a stream from a preferred log sequence number:
    
    
    POST https://datastream.googleapis.com/v1/projects/[project-id]/locations/
    [location]/streams/[stream-id]:run
    {
      "cdcStrategy": {
        "specificStartPosition": {
          "sqlServerLsnPosition": {
            "lsn": lsn
          }
        }
      }
    }

For example:
    
    
    POST https://datastream.googleapis.com/v1/projects/myProjectId1/locations/
    us-central1/streams/mySqlServerStreamId:run
    {
      "cdcStrategy": {
        "specificStartPosition": {
          "sqlServerLsnPosition": {
            "lsn": 0000123C:0000BA78:0004
          }
        }
      }
    }
    

### gcloud

Recovering a stream using `gcloud` isn't supported.

## Start or resume a stream from a specific position

You can start a stream or resume a paused stream from a specific position for MySQL, Oracle, and SQL Server sources. This might be useful when you want to perform backfill using an external tool, or start CDC from a position that you indicate:

  * For a MySQL source, you need to indicate a binlog position or a GTID set.
  * For an Oracle source, you need to indicate a system change number (SCN) in the redo log file.
  * For a SQL Server source, you need to indicate a log sequence number (LSN) in a change table.



The following code shows example requests to start or resume an already created stream from a specific position.

Start or resume a stream from a specific binlog position (MySQL):

### REST
    
    
    POST https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/streams/STREAM_ID:run
    {
      "cdcStrategy": {
        "specificStartPosition": {
          "mysqlLogPosition": {
            "logFile": "NAME_OF_THE_LOG_FILE"
            "logPosition": POSITION
          }
        }
      }
    }

Replace the following:

  * NAME_OF_THE_LOG_FILE: The name of the log file from which you want to start your stream.
  * POSITION: The position in the log file from which you want to start your stream. If you don't provide the value, Datastream starts reading from the head of the file.



For example:
    
    
    POST https://datastream.googleapis.com/v1/projects/myProjectId1/locations/
    us-central1/streams/myStreamId1:run
    {
      "cdcStrategy": {
        "specificStartPosition": {
          "mysqlLogPosition": {
            "logFile": "binlog.001"
            "logPosition": 2
          }
        }
      }
    }

### gcloud

Starting or resuming a stream from a specific position using `gcloud` isn't supported. For information about using `gcloud` to start or resume a stream, see [Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/streams/update).

Start or resume a stream from a specific GTID set (MySQL):

### REST
    
    
    POST https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/streams/STREAM_ID:run
    {
      "cdcStrategy": {
        "specificStartPosition": {
          "mysqlGtidPosition": {
            "gtidSet": "GTID_SET"
          }
        }
      }
    }

Replace GTID_SET with one or more single GTIDs or ranges of GTIDs from which you want to start or resume your stream.

For example:
    
    
    POST https://datastream.googleapis.com/v1/projects/myProjectId1/locations/
    us-central1/streams/myStreamId1:run
    {
      "cdcStrategy": {
        "specificStartPosition": {
          "mysqlGtidPosition": {
            "gtidSet": "22cc56f5-3862-379a-9af5-051c59baef9d:1-561143685:561143688-591036613,b8d7df02-832b-32b9-bec7-2018806b76f6:3-7"
          }
        }
      }
    }

### gcloud

Starting or resuming a stream from a specific position using `gcloud` isn't supported. For information about using `gcloud` to start or resume a stream, see [Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/streams/update).

Start or resume a stream from a specific system change number in the redo log file (Oracle):

### REST
    
    
    POST https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/streams/STREAM_ID:run
    {
      "cdcStrategy": {
        "specificStartPosition": {
          "oracleScnPosition": {
            "scn": scn
          }
        }
      }
    }

Replace scn with the system change number (SCN) in the redo log file from which you want to start your stream. This field is mandatory. 

For example:
    
    
    POST https://datastream.googleapis.com/v1/projects/myProjectId1/locations/
    us-central1/streams/myStreamId1:run
    {
      "cdcStrategy": {
        "specificStartPosition": {
          "oracleScnPosition": {
            "scn": 123123
          }
        }
      }
    }
    

### gcloud

Starting or resuming a stream from a specific position using `gcloud` isn't supported. For information about using `gcloud` to start a stream, see [Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/streams/update).

Start or resume a stream from a specific log sequence number (SQL Server):

### REST
    
    
    POST https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/streams/STREAM_ID:run
    {
      "cdcStrategy": {
        "specificStartPosition": {
          "sqlServerLsnPosition": {
            "lsn": "lsn"
          }
        }
      }
    }

Replace lsn with the log sequence number in the change table from which you want to start your stream. This field is mandatory.

For example:
    
    
    POST https://datastream.googleapis.com/v1/projects/myProjectId1/locations/
    us-central1/streams/myStreamId1:run
    {
      "cdcStrategy": {
        "specificStartPosition": {
          "sqlServerLsnPosition": {
            "lsn": "0000123C0000BA780004"
          }
        }
      }
    }
    

For more information, see the Datastream API [reference documentation](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams/run).

### gcloud

Starting or resuming a stream from a specific position using `gcloud` isn't supported. For information about using `gcloud` to start a stream, see [Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/streams/update).

## Modify a stream

The following code shows a request to update the file rotation configuration of a stream to rotate the file every 75 MB or 45 seconds.

For this example, the fields specified for the `updateMask` parameter include the `fileRotationMb` and `fileRotationInterval` fields, represented by the `destinationConfig.gcsDestinationConfig.fileRotationMb` and `destinationConfig.gcsDestinationConfig.fileRotationInterval` flags, respectively.

### REST
    
    
    PATCH https://datastream.googleapis.com/v1/projects/myProjectId1/locations/us-central1/streams/myStream?updateMask=destinationConfig.gcsDestinationConfig.
    fileRotationMb,destinationConfig.gcsDestinationConfig.fileRotationInterval
    {
      "destinationConfig": {
        "gcsDestinationConfig": {
          "fileRotationMb": 75,
          "fileRotationInterval": 45
        }
      }
    }

The following code shows a request to include a Unified Types schema file in the path of files that Datastream writes to Cloud Storage. As a result, Datastream writes two files: a JSON data file and an Avro schema file.

For this example, the field specified is the `jsonFileFormat` field, represented by the `destinationConfig.gcsDestinationConfig.jsonFileFormat` flag.
    
    
    PATCH https://datastream.googleapis.com/v1/projects/myProjectId1/locations/us-central1/streams/myStream?updateMask=destinationConfig.gcsDestinationConfig.
    jsonFileFormat
    {
      "destinationConfig": {
        "gcsDestinationConfig": {
          "jsonFileFormat" {
            "schemaFileFormat": "AVRO_SCHEMA_FILE"
          }  
        }
      }
    }

The following code shows a request for Datastream to replicate existing data, in addition to ongoing changes to the data, from the source database into the destination.

The `oracleExcludedObjects` section of the code shows those tables and schemas that are restricted from being backfilled into the destination.

For this example, all tables and schemas will be backfilled, except for tableA in schema3.
    
    
    PATCH https://datastream.googleapis.com/v1/projects/myProjectId1/locations/us-central1/streams/myStream?updateMask=backfillAll
    {
      "backfillAll": {
        "oracleExcludedObjects": {
          "oracleSchemas": [
            {
              "schema": "schema3",
              "oracleTables": [
                { "table": "tableA" }
              ]
            }
          ]
        }
      }
    }  

### gcloud

For more information about using `gcloud` to modify your stream, see the [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/streams/update).

## Initiate backfill for an object of a stream

A stream in Datastream can backfill historical data, as well as stream ongoing changes into a destination. Ongoing changes will always be streamed from a source into a destination. However, you can specify whether you want historical data to be streamed.

If you want historical data to be streamed from the source into the destination, then use the `backfillAll` parameter.

Datastream also lets you stream historical data only for specific database tables. To do this, use the `backfillAll` parameter, and exclude the tables for which you don't want historical data.

If you want only ongoing changes to be streamed into the destination, then use the `backfillNone` parameter. If you then want Datastream to stream a snapshot of all existing data from the source to the destination, you must initiate backfill manually for the objects that contain this data.

Another reason for initiating backfill for an object is if data is out of sync between the source and the destination. For example, a user can delete data in the destination inadvertently, and the data is now lost. In this case, initiating backfill for the object serves as a "reset mechanism" because all data is streamed into the destination in one shot. As a result, the data is synced between the source and the destination.

Before you can initiate backfill for an object of a stream, you must retrieve information about the object.

Each object has an OBJECT_ID, which uniquely identifies the object. You use the OBJECT_ID to initiate backfill for the stream.

### REST
    
    
    POST https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/streams/STREAM_ID/objects/OBJECT_ID:startBackfillJob

### gcloud

For more information about using `gcloud` to initiate backfill for an object of your stream, see the [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/objects/start-backfill).

## Stop backfill for an object of a stream

After initiating backfill for an object of a stream, you can stop backfill for the object. For example, if a user modifies a database schema, then the schema or data may be corrupted. You don't want this schema or data to be streamed into the destination, and so you stop backfill for the object.

You can also stop backfill for an object for load balancing purposes. Datastream can run multiple backfills in parallel. This may put an additional load on the source. If the load is significant, stop backfill for each object, and then initiate backfill for the objects, one by one.

Before you can stop backfill for an object of a stream, you must make a request to retrieve information about all objects of a stream. Each object that's returned has an OBJECT_ID, which uniquely identifies the object. You use the OBJECT_ID to stop backfill for the stream.

### REST
    
    
    POST https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/streams/STREAM_ID/objects/OBJECT_ID:stopBackfillJob

### gcloud

For more information about using `gcloud` to stop backfill for an object of your stream, see the [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/objects/stop-backfill).

## Change the number of maximum concurrent CDC tasks

**Note:** This configuration is only available for MySQL and Oracle sources.

The following code shows how to set the number of maximum concurrent change data capture (CDC) tasks for a MySQL stream to 7.

For this example, the field specified for the `updateMask` parameter is the `maxConcurrentCdcTasks` field. By setting its value to 7, you're changing the number of maximum concurrent CDC tasks from the previous value to 7. You can use values from 0 to 50 (inclusive). If you don't define the value, or if you define it as 0, the system default of 5 tasks is set for the stream.

### REST
    
    
    PATCH https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/streams/STREAM_ID?updateMask=sourceConfig.mysqlSourceConfig.maxConcurrentCdcTasks
    {
      "sourceConfig": {
        "mysqlSourceConfig": {
          "maxConcurrentCdcTasks": "7"
          }
        }  
    }

### gcloud

For more information about using `gcloud`, see the [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/streams/update).

## Change the number of maximum concurrent backfill tasks

The following code shows how to set the number of maximum concurrent backfill tasks for a MySQL stream to 25.

For this example, the field specified for the `updateMask` parameter is the `maxConcurrentBackfillTasks` field. By setting its value to 25, you're changing the number of maximum concurrent backfill tasks from the previous value to 25. You can use values from 0 to 50 (inclusive). If you don't define the value, or if you define it as 0, the system default of 16 tasks is set for the stream.

### REST
    
    
    PATCH https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/
    streams/STREAM_ID?updateMask=sourceConfig.mysqlSourceConfig.maxConcurrentBackfillTasks
    {
      "sourceConfig": {
        "mysqlSourceConfig": {
          "maxConcurrentBackfillTasks": "25"
          }
        }  
    }

### gcloud

For more information about using `gcloud`, see the [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/streams/update).

## Enable streaming of large objects for Oracle sources

You can enable streaming of large objects, such as binary large objects (`BLOB`), character large objects (`CLOB`) and national character large objects (`NCLOB`) for streams with Oracle sources. The `streamLargeObjects` flag lets you include large objects both in new and existing streams. The flag is set on stream level, you don't need to specify the columns of large object data types.

The following example shows how to create a stream that lets you stream large objects.

### REST
    
    
    POST https://datastream.googleapis.com/v1/projects/myProjectId1/locations/
    us-central1/streams?streamId=myOracleLobStream
    {
      "displayName": "Oracle LOB stream",
      "sourceConfig": {
        "sourceConnectionProfileName": "/projects/myProjectId1/locations/us-central1/connectionProfiles/OracleCp",
        "oracleSourceConfig": {
          "includeObjects": {
            "oracleSchemas": [
              {
                "schema": "schema1",
                "oracleTables": [
                  {
                    "table": "tableA",
                    "oracleColumns": [
                      {
                        "column": "column1,column2"
                      }
                    ]
                  }
                ]
              }
            ]
          },
          "excludeObjects": {},
          "streamLargeObjects": {}
        }
      }
    }

### gcloud

For more information about using `gcloud` to update a stream, see [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/streams/update).

## Delete a stream

The following code shows a request to delete a stream.

### REST
    
    
    DELETE https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/streams/STREAM_ID

### gcloud

For more information about using `gcloud` to delete your stream, see the [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/streams/delete).

## What's next

  * Learn how to [use the Datastream API to manage connection profiles](https://docs.cloud.google.com/datastream/docs/manage-connection-profiles).
  * Learn how to [use the Datastream API to manage private connectivity configurations](https://docs.cloud.google.com/datastream/docs/manage-private-connectivity-configurations).
  * For more information about using the Datastream API, see the [reference documentation](https://docs.cloud.google.com/datastream/docs/reference/rest).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
