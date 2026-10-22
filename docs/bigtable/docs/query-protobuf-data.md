---
url: https://docs.cloud.google.com/bigtable/docs/query-protobuf-data/
title: Query protobuf data \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:23.417246+00:00
---

# Query protobuf data  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/query-protobuf-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Query protobuf data

This document provides examples of common query patterns for reading and querying protocol buffer (protobuf) data stored in Bigtable.

Before you read this page, familiarize yourself with the following:

  * [Create and manage protobuf schemas](https://docs.cloud.google.com/bigtable/docs/create-manage-protobuf-schemas)
  * [GoogleSQL for Bigtable](https://docs.cloud.google.com/bigtable/docs/googlesql-overview)



## Example data

The following examples use a `Music` table that stores information about albums and artists. The data is stored in a column family named `album_details`, with a column qualifier `album`. The column qualifier contains protobuf messages.

The protobuf schema is defined in the following proto files:

  * `artist.proto`:
        
        syntax = "proto3";
        
        package package_name;
        
        message Artist {
         string name = 1;
        }
        

  * `album.proto`:
        
        syntax = "proto3";
        
        package package_name;
        
        import "artist.proto";
        
        message Album {
         string title = 1;
         Artist artist = 2;
         int32 release_year = 3;
        }
        




As a result, Bigtable creates a schema bundle for this table that contains the following [protobuf file descriptor set](https://docs.cloud.google.com/bigtable/docs/create-manage-protobuf-schemas#descriptor-set) for these protobuf definitions:
    
    
    file {
      name: "artist.proto"
      package: "package_name"
      message_type {
        name: "Artist"
        field {
          name: "name"
          number: 1
          label: LABEL_OPTIONAL
          type: TYPE_STRING
          json_name: "name"
        }
      }
      syntax: "proto3"
    }
    file {
      name: "album.proto"
      package: "package_name"
      dependency: "artist.proto"
      message_type {
        name: "Album"
        field {
          name: "title"
          number: 1
          label: LABEL_OPTIONAL
          type: TYPE_STRING
          json_name: "title"
        }
        field {
          name: "artist"
          number: 2
          label: LABEL_OPTIONAL
          type: TYPE_MESSAGE
          type_name: ".package_name.Artist"
          json_name: "artist"
        }
        field {
          name: "release_year"
          number: 3
          label: LABEL_OPTIONAL
          type: TYPE_INT32
          json_name: "releaseYear"
        }
      }
      syntax: "proto3"
    }
    

## Example queries

The following examples show how to query protobuf data using GoogleSQL for Bigtable and BigQuery external tables.

### Cast a column to a protobuf message

You can use the `CAST` operator to interpret a `BYTES` value as a protobuf message. To do this, you must provide the full name of the protobuf message in the following format: `SCHEMA_BUNDLE_ID.FULLY_QUALIFIED_MESSAGE_NAME`.

Replace the following:

  * `SCHEMA_BUNDLE_ID`: The unique ID you assigned to your schema bundle when you created it.
  * `FULLY_QUALIFIED_MESSAGE_NAME`: The full name of the message, which must include the package name defined in your proto file–for example, `package_name.message_name`.



The following sample query casts the `album` column to the `Album` protobuf message. This message is defined in the `package_name` package and is part of a schema bundle named `bundle_name`:
    
    
    SELECT
      CAST(album_details['album'] AS bundle_name.package_name.Album).title
    FROM
      Music;
    

### Access nested fields

You can access nested fields within a protobuf message using dot notation.

The following query retrieves the name of the artist from the nested `Artist` message within the `Album` message:
    
    
    SELECT
      CAST(album_details['album'] AS bundle_name.package_name.Album).artist.name
    FROM
      Music;
    

### Filter based on protobuf fields

You can use the `WHERE` clause to filter rows based on the values of fields within a protobuf message.

The following query selects all albums by the artist Dana A.:
    
    
    SELECT
      *
    FROM
      Music
    WHERE
      CAST(album_details['album'] AS bundle_name.package_name.Album).artist.name = 'Dana A.';
    

### Aggregate protobuf fields

You can use aggregate functions like `SUM`, `AVG`, `MIN`, `MAX`, and `COUNT` on numeric fields within your protobuf messages.

The following query calculates the average release year of all albums in the table:
    
    
    SELECT
      AVG(CAST(album_details['album'] AS bundle_name.package_name.Album).release_year)
    FROM
      Music;
    

### Order by protobuf fields

You can use the `ORDER BY` clause to sort the result set based on a field in your protobuf message.

The following query retrieves all albums and sorts them by their release year in descending order:
    
    
    SELECT
      *
    FROM
      Music
    ORDER BY
      CAST(album_details['album'] AS bundle_name.package_name.Album).release_year DESC;
    

### Use with views

You can create [continuous materialized views](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-views) or [logical views](https://docs.cloud.google.com/bigtable/docs/create-manage-logical-views) that read protobuf data.

The following command creates a logical view which extracts all fields within the `Album` message:
    
    
    QUERY="SELECT _key, CAST(album_details['album'] AS bundle_name.package_name.Album).* FROM Music"
    
    gcloud bigtable logical-views create LOGICAL_VIEW_ID \
        --instance=INSTANCE_ID \
        --query=$QUERY
    

Replace the following:

  * `LOGICAL_VIEW_ID`: the ID of the logical view that references the schema bundle.
  * `INSTANCE_ID`: the ID of the instance that you're using to create the schema bundle.



When a view references a schema bundle, you must delete the view before you can delete the bundle. Also, don't update the schema bundle to a new protobuf file descriptor set that isn't backward compatible with the existing one.

### Use with BigQuery external tables

You can query protobuf data stored in Bigtable from BigQuery by creating an external table. When creating the external table, you specify the column type as `JSON`, its encoding as `PROTO_BINARY`, and you associate it with a schema bundle. This process converts the protobuf message bytes into the equivalent JSON data, allowing you to query its fields directly.

The following is an example of a table definition file for [creating a BigQuery external table](https://docs.cloud.google.com/bigquery/docs/create-bigtable-external-table) over the `Music` table:
    
    
    {
        "sourceFormat": "BIGTABLE",
        "sourceUris": [
            "https://googleapis.com/bigtable/projects/PROJECT_ID/instances/INSTANCE_ID/tables/Music"
        ],
        "bigtableOptions": {
            "columnFamilies" : [
                {
                    "familyId": "album_details",
                    "columns": [
                        {
                            "qualifierString": "album",
                            "type": "JSON",
                            "encoding": "PROTO_BINARY",
                            "protoConfig": {
                                "schemaBundleId": "bundle_name",
                                "protoMessageName": "package_name.Album"
                            }
                        }
                    ]
                }
            ]
        }
    }
    

Once the external table is created, you can query the protobuf data as a JSON column in BigQuery.

The following query retrieves the title of all albums released in 2022 from the BigQuery external table:
    
    
    SELECT JSON_VALUE(value, '$.title') AS title
    FROM
    `PROJECT_ID.DATASET.TABLE_NAME` AS t,
    UNNEST(t.album_details.album.cell)
    WHERE INT64(JSON_EXTRACT(value, '$.releaseYear')) = 2022;
    

## What's next

  * Read about [schema design best practices for protobufs](https://docs.cloud.google.com/bigtable/docs/schema-design#protobuf-data).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
