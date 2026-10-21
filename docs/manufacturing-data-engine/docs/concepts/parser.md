---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/parser/
title: Parser \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:59:37.048206+00:00
---

# Parser  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/parser/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Parser

Parsers are configuration entities that define how messages from a specific _source message class_ are _parsed and transformed_ to records of a specific _target_ type.

![source-to-target](https://docs.cloud.google.com/static/manufacturing-data-engine/images/source-to-target.png)

A parser configuration has the following three components:

  1. **Source message class association** : A parser processes source messages from a single source message class. For more information, see [Source Message classes](https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/source-message-class).
  2. **Type version association** : A parser emits proto records of a single type version. The type version configuration defines what fields must be present on the emitted proto record and dictates their structure (schema). For more information, see [Type](https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/type).
  3. **Whistle script** : Whistle scripts define how to transform source messages into proto records using mapping, parsing, and transformation logic. Whistle scripts are written by users; however, Manufacturing Data Engine (MDE) provides configuration packages for typical use-cases. For more information, see the following section.



## Whistle definition

Whistle is a mapping language that can be used to convert complex nested data from one schema to another. In manufacturing, data models can be complex and can contain many nested and repeated structures. This makes it difficult to express mapping logic in a procedural format. Whistle addresses this issue by providing a declarative language that lets you to define mapping and transformation logic in a natural way.

For example, you could use Whistle to harmonize several sensor data models across different factories into a unified MDE type model. The source data might contain nested structures, such as a list of components or a hierarchy of features. Whistle lets you express the mapping logic for these nested structures in a natural way, without having to write procedural code.

Whistle also supports functions which lets you break down complex mappings involving repeated structures into functions. This makes it easier to understand and maintain your mapping code, and it also makes it easier to reuse code.

Whistle provides benefits over procedural approaches. See the following example:

**Warning:** This example uses incomplete code for demonstration purposes and is not guaranteed to work.

Given this sample payload:
    
    
    {
      "payload": {
        "tag": "vibration-sensor"
      },
      "details": {
        "value": 0.24,
        "timestamp": "2023-06-26 12:19:20.046000 UTC"
      }
    }
    

And the following Whistle script:
    
    
    package mde
    
    [{
        tagName: $root.payload.tag
        timestamps: {
            eventTimestamp: $root.details.timestamp
        }
        data: {
            numeric: $root.details.value
        }
    }]
    

Applying the previous Whistle script, the parser would produce a proto record like the following:
    
    
    [
      {
        "tagName": "vibration-sensor",
        "timestamps": {
          "eventTimestamp": "2023-06-26 12:19:20.046000 UTC"
        },
        "data": {
          "value": 0.24
        }
      }
    ]
    

For more information about the Whistle language syntax and available functions, see [Whistle documentation](https://docs.cloud.google.com/manufacturing-data-engine/docs/reference/whistle/basics).

## Runtime behavior of parsers

At runtime the parser receives all messages of the source message class with which it's associated, applies the configured Whistle script on each message, and emits one or more proto records of the configured type.

The emitted proto records must comply with the type configuration. If they don't comply, they are moved to the dead letter queue.

## Association rules

A parser can only be associated to a single message class and a single type version. However, a parser may emit one or more records as long as they are of the type version to which the parser is linked. The output of a parser is an array of proto record objects.

![parser-multiple-proto-records](https://docs.cloud.google.com/static/manufacturing-data-engine/images/parser-records.png)

Emitting more than one record from a parser is useful in scenarios where a source message contains an array of readings or events that you want to de-aggregate. Parsers allow you to "split" the source message into multiple proto records so that each reading, for example, becomes a row in a record table in BigQuery.

The emitted proto records may reference any tag name. This behavior is a change from v1.1 and v1.2 where tag names were scoped to the type. After v1.3 MDE proto records emitted by any parser can

## Proto record schema

The JSON schema that the proto records must conform to depends on:

  1. **Archetype** : The specific archetype associated with the type.
  2. **Type Configuration** : The configuration settings defined for the type.



The archetype defines the base schema for records. For example, a type of in the `discrete` archetype family requires that proto records contain values for the following attributes:

  * `tagName`
  * `timestamps.eventTimestamp`
  * `data.complex`



The type can impose further restrictions on the proto records. For example, you can define a schema for the `data` field, or you can require that proto records provide a reference to a metadata instance.

For more information, see the [proto record reference](https://docs.cloud.google.com/manufacturing-data-engine/docs/reference/proto-record-schema).

## Reference data lookup

MDE provides a custom Whistle function to lookup a value for a provided key from a [lookup bucket](https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/metadata#types_of_buckets).

You can look up a look up bucket instance by its natural key by calling the [mde::lookupByKey](https://docs.cloud.google.com/manufacturing-data-engine/docs/reference/Whistle/Whistle-mde-functions#lookupbykey) function in a Whistle script. The function takes the lookup`bucketName`, `bucketVersion`, and `naturalKey` of the instance as the arguments, and returns the latest metadata instance for the provided natural key. You can use the instance to populate fields in a proto record in the parser. For example:
    
    
    "data" : {
      "complex" : {
        "VIN" : mde::lookupByKey("vin-lookup-bucket", input.vinKey, 1).VIN,
        "vin_registration_time" : mde::lookupByKey("vin-lookup-bucket", input.vinKey, 1).vin_registration_time,
        "ResultValue" : 163.0482614,
      }
    }
    
    

**Warning:** The previous example uses incomplete code for demonstration purposes only and might not work.

### Naming restrictions for Parsers

A parser name can contain the following:

  * Letters (uppercase and lowercase), numbers, and the special characters `-` and `_`.
  * Can be up to 255 characters long.



You can use the following regular expression for validation: `^[a-z][a-z0-9\\-_]{1,255}$`.

If you try to create an entity violating the naming restrictions you will get a `400 error`.

You can use the `mde::sanitizeTagName()` function to ensure that your name is compliant with the naming restrictions. For more information, see [Whistle MDE functions](https://docs.cloud.google.com/manufacturing-data-engine/docs/reference/Whistle/Whistle-mde-functions).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
