---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/parse/how-to-write-a-whiste-script/
title: Write scripts in Whistle \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:18.592443+00:00
---

# Write scripts in Whistle  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/parse/how-to-write-a-whiste-script/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Write scripts in Whistle

This guide provides general guidance on writing a Whistle script for a parser. For more information about the Whistle syntax and available functions, see the [Whistle reference](https://docs.cloud.google.com/manufacturing-data-engine/docs/reference/whistle/basics).

## Whistle script writing

Before starting to write a Whistle script, it is recommended to:

  1. **Understand the schema of the messages in the source message class to which the parser subscribes.** To prevent mapping failures and, as a result, messages landing in the dead letter queue, the Whistle script has to be able to map all incoming messages. If message schemas differ from message to message, your Whistle script needs to handle these differences.

Knowing the source message schema helps you understand what fields exist in the source messages and what their data types are, so that you can decide how to map fields in the source messages to the target type schema. It is also important to understand the semantics of the data, so that you can effectively decide which parts of the source message should be mapped to attributes in the target schema.

For example, knowing the frequency of attribute value change helps you decide what data should be mapped as embedded metadata versus cloud metadata. See the sections on [modeling source message classes](https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/ingest/how-to-create-a-source-message-class#modeling-a-source-message-class) and [modeling data](https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/model/how-to-model-data).

  2. **Understand the schema of the type version defined for the parser**. The Whistle script in the parser maps source messages to the type version schema that is defined for the parser. To know how to construct a proto record that meets the requirements of the type version, you should look up the type specification. In particular, you should note the schema of the `data` field, as well as any metadata bucket associations. It is particularly important to note if any metadata bucket associations are marked as `required: true`. If you plan to look up metadata instances by value, you should make note of the schemas of the associated buckets.

  3. **Write the Whistle script.** The Whistle script performs the actual source-to-target transformation. The source message is loaded into an input called `$root`. Consult the [Whistle reference](https://docs.cloud.google.com/manufacturing-data-engine/docs/reference/whistle/basics) for an overview of the language and available functions. Also, see the other guides in this section, such as [how to link records to metadata instances](https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/parse/how-to-link-records-to-metadata-instances).


**Note:** If your source data delivers date and time as **ISO 8601** formatted strings, you can use the [`getEpochMillis`](https://docs.cloud.google.com/manufacturing-data-engine/docs/reference/Whistle/Whistle-builtins#getepochmillis) function to convert it to the milliseconds since the Unix epoch.

## Best practices

This section outlines the best practices for writing Whistle scripts.

### Perform null checks when accessing message properties

It is recommended practice to check for null when accessing a message property, whenever there is a chance that the property might not be defined.
    
    
    //Add metadata from source bucket if metadata.source attribute is present
    if(isNotNil(input.metadata) and isNotNil(input.metadata.source)) then {
    {
        var metadataArray[]: {
            bucketReference: {
                bucketName: "source";
                version: 1;
            };
                naturalKey: input.metadata.source;
            }
        }
    }
    

## Examples

The following sections show some examples of basic operations using Whistle.

### Simple Whistle mapping

Given the following source message...
    
    
    {
      "sensor": "rotation-speed-sensor",
      "machine": "m-234",
      "timestamp": "1687973092857",
      "value": 1200
    }
    

And the following Whistle script:
    
    
    package mde
    
    [
        {
            tagName: $root.machine + " - " + $root.sensor;
            data: {
                numeric: $root.value;
            };
            timestamps: {
                eventTimestamp: $root.timestamp;
            }
        }
    ]
    

The parser will produce this proto record output:
    
    
    [
      {
        "tagName": "m-234-rotation-speed-sensor",
        "data": {
          "numeric": 1200
        },
        "timestamps": {
          "eventTimestamp": "1687973092857"
        }
      }
    ]
    

### Simple Whistle mapping using functions

Given the following source message:
    
    
    {
      "sensor": "rotation-speed-sensor",
      "machine": "m-234",
      "timestamp": "1687973092857",
      "value": 1200
    }
    

And the following Whistle script:
    
    
    package mde
    
    [
        {
            tagName: getTagName($root);
            data: getValue($root);
            timestamps: getTimestamp($root)
        }
    ]
    
    def getTagName(input) {
        input.machine + "-" + input.sensor;
    }
    
    def getTimestamp(input) {
        eventTimestamp: input.timestamp;
    }
    
    def getValue(input) {
        numeric: input.value;
    }
    
    

The parser will produce this proto record output:
    
    
    [
      {
        "tagName": "m-234-rotation-speed-sensor",
        "data": {
          "numeric": 1200
        },
        "timestamps": {
          "eventTimestamp": "1687973092857"
        }
      }
    ]
    

### Emitting several proto records from a parser 1

Given the following source message:
    
    
    {
      "tag": "plc-34",
      "machine": "controller",
      "timestamp": "1687973092857",
      "values": [200, 499]
    }
    

And the following Whistle script:
    
    
    package mde
    
    var valueLen: listLen($root.values);
    var indexes: range(0, valueLen);
    
    [
        getProtoRecords($root.values[], indexes[], $root)
    ]
    
    def getProtoRecords(value, index, input) {
            tagName: input.machine + "-" + input.tag + "-" + index;
            data: {
                numeric: value;
            };
            timestamps: {
                eventTimestamp: input.timestamp;
            };
    }
    

The parser will produce this proto record output:
    
    
    [
      {
        "tagName": "controller-plc-34-0",
        "data": {
          "value": 200.0
        },
        "timestamps": {
          "eventTimestamp": "1687973092857"
        }
      },
      {
        "tagName": "controller-plc-34-1",
        "data": {
          "value": 499.0
        },
        "timestamps": {
          "eventTimestamp": "1687973092857"
        }
      }
    ]
    

### Emitting several proto records from a parser 2

Given the following source message:
    
    
    {
      "machine": "controller",
      "timestamp": "1687973092857",
      "sensors": [
        {
          "tag": "plc-34",
          "value": 200
        },
        {
          "tag": "plc-35",
          "value": 499
        }
      ]
    }
    

And the following Whistle script:
    
    
    package mde
    
    [$$
        getProtoRecords($root.sensors[], $root)
    ]
    
    def getProtoRecords(sensor, input) {
            tagName: input.machine + "-" + sensor.tag;
            data: {
                numeric: sensor.value;
            };
            timestamps: {
                eventTimestamp: input.timestamp;
            };
    }
    

The parser will produce this proto record output:
    
    
    [
      {
        "tagName": "controller-plc-34",
        "timestamps": {
          "eventTimestamp": "1687973092857"
        },
        "data": {
          "numeric": 200
        }
      },
      {
        "tagName": "controller-plc-35",
        "timestamps": {
          "eventTimestamp": "1687973092857"
        },
        "data": {
          "numeric": 499
        }
      }
    ]
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
