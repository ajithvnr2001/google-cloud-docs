---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/configuration/content/
title: File content \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:11.986189+00:00
---

# File content  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/configuration/content/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# File content

This page describes the content of each configuration package folder on Manufacturing Data Engine (MDE)'s package.

Under each configuration package folder, MDE expects to find one JSON file per configuration object. If you want to create two buckets, then there should be two separate files. The names of the files are ignored. However, it's recommended to name the files after the configuration object name that you would like to create. The actual JSON schema for each object depends on the type of the configuration entity you want to create, but it matches the JSON schema of the corresponding API response.

To organize the configuration package further, you can refer to other JSON files to be embedded in the file under a particular field. For example, the following JSON specifies an MDE bucket with a schema where the schema is defined in another JSON file. This enhances the overall readability and maintainability of the configuration package.
    
    
    {
      "type": "TAG",
      "name": "second-tag-bucket",
      "attributes": {
        "instanceOverwriteMode": "true"
      },
      "versions": [
        {
          "version": 1,
          "schema": "'{{schemas/generic-schema.json}}'",
          "provider": "local",
        }
      ]
    }
    
    

To reference another file, you can use the `{{relative-path/file.json}}` directive which contains the relative path of the file that needs to be included in the existing file. MDE will resolve the file and include the JSON contents as the value of the field that has the reference directive. The value of the `schema` field in the previous example, will contain an embedded JSON sub-object that matches the contents of the file.

For certain objects, you need to embed the JSON contents as a string. As an example, the `schema` field in the bucket object requires the bucket schema to be embedded as a string, and in that case, the reference directive should be surrounded by single quotes `'` which tells MDE to embed the contents unprocessed as a string; the reference directive will be: `'{{relative-path/file.json}}'`.

The referenced file could be in any directory, and you can create different directories for organization purposes. For example, the directory called `schemas` in the previous example is an arbitrary folder structure to group common files together. The type of files that can be embedded are either `JSON` or `WSTL` for Whistle scripts.

The following are sample configurations for each MDE entity.

## Bucket

This section shares a sample configuration for a MDE bucket.
    
    
    {
      "type": "TAG",
      "name": "second-tag-bucket",
      "attributes": {
        "instanceOverwriteMode": "true"
      },
      "versions": [
        {
          "version": 1,
          "schema": "'{{schemas/generic-schema.json}}'",
          "provider": "local"
        }
      ]
    }
    
    
    

## Ingestion specification

This section shares a sample configuration for a MDE ingestion specification.
    
    
    {
        "name": "csv-full-ingestion-specification",
        "source": "CSV",
        "folderName": "test-csv-folder",
        "separator": ",",
        "skipRows": 10,
        "headers": {
            "headerNames": {
                "names": [
                    "one",
                    "two",
                    "three"
                ]
            }
        },
        "insertMetadata": true,
        "disabled": false
    }
    
    

## Message classes

This section shares a sample configuration for MDE message classes.
    
    
    {
      "name": "default-numeric-message-class",
      "priority": 970,
      "expression": "#root.event['value'] instanceof T(Number) && #root.event['timestamp'] != null && #root.event['tagName'] != null && #root.event['cluster'] == null"
    }
    
    

## Metadata instances

This section shares a sample configuration for MDE metadata instances.
    
    
    {
        "bucketReference": {
            "bucketName": "default-tag-bucket",
            "bucketType": "TAG",
            "version": 1
        },
        "naturalKey": "cloud-natural-key",
        "instance": {
            "site": "simulated-site",
            "factory": "test-factory"
        }
    }
    
    

## Parsers

This section shares a sample configuration for MDE parsers.
    
    
    {
      "name": "default-numeric-parser",
      "messageClassName": "default-numeric-message-class",
      "typeReference": {
        "name": "default-numeric-type",
        "version": 1
      },
      "disabled": false,
      "script": "'{{scripts/parser-script.wstl}}'"
    }
    
    

## Type

This section shares a sample configuration for a MDE type.
    
    
    {
      "archetype": "NUMERIC_DATA_SERIES",
      "name": "default-numeric-type",
      "disabled": false,
      "versions": [
        {
          "version": 1,
          "dataSchema": "",
          "storageSpecs": [
            {
              "sink": "PUBSUB_PROTO",
              "disabled": true,
              "materializeCloudMetadata": false
            },
            {
              "sink": "BIG_QUERY",
              "disabled": false,
              "materializeCloudMetadata": true
            },
            {
              "sink": "GCS",
              "disabled": false,
              "materializeCloudMetadata": false
            },
            {
              "sink": "PUBSUB_JSON",
              "disabled": true,
              "materializeCloudMetadata": false
            },
            {
              "sink": "BIG_TABLE",
              "disabled": false,
              "materializeCloudMetadata": false
            }
          ],
          "metadataBuckets": [
            {
              "bucketName": "default-record-bucket",
              "version": 1,
              "required": false
            },
            {
              "bucketName": "second-tag-bucket",
              "version": 1,
              "required": false
            },
            {
              "bucketName": "default-tag-bucket",
              "version": 1,
              "required": false
            }
          ],
          "transformations": [
            {
              "window": {
                "id": "10-minutes-window",
                "durationMinutes": 10,
                "valueExpression": "#message['data']['numeric'].toString()"
              }
            },
            {
              "eventChange": {
                "keyExpression": "#message['tagName']",
                "valueExpression": "#message['data']['numeric'].toString()"
              }
            }
          ]
        }
      ]
    }
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
