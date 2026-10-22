---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/parse/how-to-link-records-to-metadata-instances/
title: Link records to metadata instances \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:18.767094+00:00
---

# Link records to metadata instances  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/parse/how-to-link-records-to-metadata-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Link records to metadata instances

This guide describes how to link records to metadata instances. Manufacturing Data Engine (MDE) links records to metadata instances by writing the `instance_id` of the metadata bucket into the record. However you don't set the `instance_id` in a proto record in the parser directly. Instead, MDE automatically resolves the `instance_id` for you based on the inputs you provide in the proto record. MDE provides two ways to resolve in `instance_id`:

  1. By metadata instance natural key.
  2. By metadata instance value.

**Note:** If resolution of bucket references or instances fail, the message will still be processed, but with empty metadata references.

## Resolving a metadata instance_id by natural key

Each metadata instance in a metadata bucket has a natural key, and there may be more than one instance for a natural key. You can associate a record to the _latest_ metadata instance for a natural key by supplying the natural key in the proto record in the parser. MDE takes care of retrieving the latest instance for the natural key you supplied, and inserting the instance's `instance_id` in the record.

For example, given the following metadata instances in a record metadata bucket called `machine` with bucket number `1`:
    
    
    [
      {
        "instance_id": "a614e25d-fded-41c3-9a56-3222cd30070d",
        "bucket_number": "1",
        "bucket_name": "machine",
        "bucket_version": "1",
        "natural_key": "m-234",
        "instance": {
          "machineName": "CNC Mill"
        },
        "created_timestamp": "2023-06-27 20:00:29.603000 UTC"
      },
      {
        "instance_id": "6cfdf894-2fb6-4951-82c6-c4eada587529",
        "bucket_number": "1",
        "bucket_name": "machine",
        "bucket_version": "1",
        "natural_key": "m-234",
        "instance": {
          "machineName": "5 Axis CNC Mill"
        },
        "created_timestamp": "2023-06-28 20:00:29.632000 UTC"
      }
    ]
    

And given the following source message as sample:
    
    
    {
      "sensor": "rotation-speed-sensor",
      "machine": "m-234",
      "timestamp": "1687973092857",
      "value": 1200
    }
    

The following Whistle script:
    
    
    package mde
    
    [
        {
            tagName: $root.machine + "-" + $root.sensor;
            data: {
                numeric: $root.value;
            };
            timestamps: {
                eventTimestamp: $root.timestamp;
            }
            cloudMetadata: [{
                bucketReference: {
                    bucketName: "machine";
                    version: 1;
                }
                naturalKey: $root.machine
            }]
        }
    ]
    

Will produce the following proto record:
    
    
    [
      {
        "tagName": "m-234-rotation-speed-sensor",
        "data": {
          "numeric": 1200
        },
        "timestamps": {
          "eventTimestamp": "1687973092857"
        },
        "cloudMetadata": [
          {
            "bucketReference": {
              "bucketName": "machine",
              "number": 1
            },
            "naturalKey": "m-234"
          }
        ]
      }
    ]
    

After MDE finishes processing the proto record, it produces the following record (row) in BigQuery (assuming the BigQuery sink and metadata metadata materialization are turned on):
    
    
    [
      {
        "id": "6e008960-7f25-4418-899c-75b05c3d3186",
        "tag_name": "m-234-rotation-speed-sensor",
        "type_version": "1",
        "event_timestamp": "2023-06-28 17:24:52.526000 UTC",
        "value": "1200",
        "embedded_metadata": {},
        "materialized_cloud_metadata": {
          "machine": {
            "machineName": "5 Axis CNC Mill"
          }
        },
        "cloud_metadata_ref": {
          "machine": {
            "instance_id": "6cfdf894-2fb6-4951-82c6-c4eada587529"
          }
        },
        "event_timestamp": "2023-06-28 17:24:53.526000 UTC",
        "source_message_id": "8511923697775002"
      }
    ]
    

## Resolving a metadata `instance_id` by instance value

Alternatively, you can associate a record to the _latest_ metadata instance for a natural key by supplying the entire metadata instance object in the proto record in the parser. You can optionally provide a natural key. If you omit the natural key, MDE infers the natural key based on the bucket type:

  * If you are supplying a metadata instance value for a _tag_ bucket and omit the natural key, MDE automatically uses the tag name as the natural key.
  * If you are supplying a metadata instance value for a _record_ bucket and omit the natural key, MDE automatically the hash value of the instance object as the natural key.



After you have constructed a proto record in the parser, MDE compares the provided metadata instance object with the most recent metadata instance object for the supplied natural key.

If the instance objects are identical, MDE inserts into the record the `instance_id` of the most recent metadata instance for the natural key.

If the instance objects are not identical, MDE uses the metadata instance supplied by the proto record to create a new metadata instance for the given natural key. MDE then inserts the `instance_id` of newly created instance into the record.

Resolving a metadata `instance_id` by instance value is particularly useful when your edge sources deliver fully qualified messages. Using this method of resolving metadata instances lets you reference an already existing instance as well as creating new metadata instance dynamically.

### Referencing an existing instance by value

Example of metadata instances in a tag metadata bucket called `asset` with bucket number `1`:
    
    
    [
      {
        "instance_id": "a614e25d-fded-41c3-9a56-3222cd30070d",
        "bucket_number": "1",
        "bucket_name": "asset",
        "bucket_version": "1",
        "natural_key": "s-446-pressure",
        "instance": {
          "machineName": "Stamping M. 446"
        },
        "created_timestamp": "2023-06-27 20:00:29.603000 UTC"
      },
      {
        "instance_id": "6cfdf894-2fb6-4951-82c6-c4eada587529",
        "bucket_number": "1",
        "bucket_name": "asset",
        "bucket_version": "1",
        "natural_key": "s-446-pressure",
        "instance": {
          "machineName": "Stamping Machine 446"
        },
        "created_timestamp": "2023-06-28 20:00:29.632000 UTC"
      }
    ]
    

Given the following is a source message:
    
    
    {
      "sensor": "pressure",
      "machine": "s-446",
      "timestamp": "1687973092857",
      "machineName": "Stamping Machine 446",
      "value": 24
    }
    

And the following Whistle script:
    
    
    package mde
    
    var tagName: $root.machine + "-" + $root.sensor;
    
    [
        {
            tagName: tagName;
            data: {
                numeric: $root.value;
            };
            timestamps: {
                eventTimestamp: $root.timestamp;
            }
            cloudMetadata: [{
                bucketReference: {
                    bucketName: "asset";
                    version: 1;
                }
                instance: {
                  // optional. Since bucketReference points to a tag bucket, if omitted, the natural is inferred to be tagName
                  naturalKey: tagName
                  attributes: {
                    machineName: $root.machineName;
                  }
                }
            }]
        }
    ]
    
    

Applying the Whistle script produces the following proto record:
    
    
    [
      {
        "tagName": "s-446-pressure",
        "data": {
          "numeric": 24
        },
        "timestamps": {
          "eventTimestamp": "1687973092857"
        },
        "cloudMetadata": [
          {
            "bucketReference": {
              "bucketName": "asset",
              "number": 1
            },
            "naturalKey": "s-446-pressure",
            "attributes": {
              "machineName": "Stamping Machine 446"
            }
          }
        ]
      }
    ]
    

After MDE finishes processing the proto record, it produces the following record (row) in BigQuery (assuming the BigQuery sink and metadata metadata materialization are turned on):
    
    
    [
      {
        "id": "6e008960-7f25-4418-899c-75b05c3d3186",
        "tag_name": "s-446-pressure",
        "type_version": "1",
        "event_timestamp": "2023-06-28 17:24:52.526000 UTC",
        "value": "24",
        "embedded_metadata": {},
        "materialized_cloud_metadata": {
          "asset": {
            "machineName": "Stamping Machine 446"
          }
        },
        "cloud_metadata_ref": {
          "asset": {
            "instance_id": "6cfdf894-2fb6-4951-82c6-c4eada587529"
          }
        },
        "event_timestamp": "2023-06-28 17:24:53.526000 UTC",
        "source_message_id": "8511923697775002"
      }
    ]
    

### Creating a new instance by value

If the supplied metadata instance in the proto record is not identical to the most recent metadata instance for the provided natural key, MDE creates a new instance.

You can configure how thew new instance is created using the `instanceOverwriteMode` setting on buckets:

  * If `instanceOverwriteMode` is set to true, the new instance is created from the instance object supplied in the proto record. The new instance is stored in the metadata bucket if it passes the bucket's schema validation.
  * If `instanceOverwriteMode` is set to false, the new instance is created by _merging_ the most recent instance for the natural key with the instance object supplied in the proto record. The resulting object is stored as a new metadata instance in the metadata bucket if it passes the bucket's schema validation.



For example, given the following metadata instance in a tag metadata bucket called `asset` with bucket number `1`:
    
    
    [
      {
        "instance_id": "a614e25d-fded-41c3-9a56-3222cd30070d",
        "bucket_number": "1",
        "bucket_name": "asset",
        "bucket_version": "1",
        "natural_key": "s-446-pressure",
        "instance": {
          "machineName": "Stamping M. 446"
        },
        "created_timestamp": "2023-06-27 20:00:29.603000 UTC"
      }
    ]
    

And the following source message:
    
    
    {
      "sensor": "pressure",
      "machine": "s-446",
      "timestamp": "1687973092857",
      "machineName": "Stamping Machine 446",
      "value": 24
    }
    

With the following Whistle script:
    
    
    package mde
    
    var tagName: $root.machine + "-" + $root.sensor;
    
    [
        {
            tagName: tagName;
            data: {
                numeric: $root.value;
            };
            timestamps: {
                eventTimestamp: $root.timestamp;
            }
            cloudMetadata: [{
                bucketReference: {
                    bucketName: "asset";
                    number: 1;
                }
                instance: {
                  // optional. Since bucketReference points to a tag bucket, if omitted, the natural is inferred to be tagName
                  naturalKey: tagName
                  attributes: {
                    machineName: $root.machineName;
                  }
                }
            }]
        }
    ]
    
    

Applying the Whistle script produces the following proto record:
    
    
    [
      {
        "tagName": "s-446-pressure",
        "data": {
          "numeric": 24
        },
        "timestamps": {
          "eventTimestamp": "1687973092857"
        },
        "cloudMetadata": [
          {
            "bucketReference": {
              "bucketName": "asset",
              "number": 1
            },
            "naturalKey": "s-446-pressure",
            "attributes": {
              "machineName": "Stamping Machine 446"
            }
          }
        ]
      }
    ]
    

Since the supplied metadata instance is not equivalent to the most recent metadata instance for the natural key, MDE creates a new metadata instance. The metadata bucket now has two instances:
    
    
    [
      {
        "instance_id": "a614e25d-fded-41c3-9a56-3222cd30070d",
        "bucket_number": "1",
        "bucket_name": "asset",
        "bucket_version": "1",
        "natural_key": "s-446-pressure",
        "instance": {
          "machineName": "Stamping M. 446"
        },
        "created_timestamp": "2023-06-27 20:00:29.603000 UTC"
      },
      {
        "instance_id": "6cfdf894-2fb6-4951-82c6-c4eada587529",
        "bucket_number": "1",
        "bucket_name": "asset",
        "bucket_version": "1",
        "natural_key": "s-446-pressure",
        "instance": {
          "machineName": "Stamping Machine 446"
        },
        "created_timestamp": "2023-06-28 20:00:29.632000 UTC"
      }
    ]
    

After MDE finishes processing the proto record, it produces the following record (row) in BigQuery (assuming the BigQuery sink and metadata metadata materialization are turned on):
    
    
    [
      {
        "id": "6e008960-7f25-4418-899c-75b05c3d3186",
        "tag_name": "s-446-pressure",
        "type_version": "1",
        "event_timestamp": "2023-06-28 17:24:52.526000 UTC",
        "value": "24",
        "embedded_metadata": {},
        "materialized_cloud_metadata": {
          "asset": {
            "machineName": "Stamping Machine 446"
          }
        },
        "cloud_metadata_ref": {
          "asset": {
            "instance_id": "6cfdf894-2fb6-4951-82c6-c4eada587529"
          }
        },
        "event_timestamp": "2023-06-28 17:24:53.526000 UTC",
        "source_message_id": "8511923697775002"
      }
    ]
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
