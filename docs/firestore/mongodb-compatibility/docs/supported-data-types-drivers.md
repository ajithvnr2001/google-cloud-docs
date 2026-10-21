---
url: https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/supported-data-types-drivers/
title: Supported MongoDB data types and drivers \u00a0|\u00a0 Firestore with MongoDB compatibility \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:18.152441+00:00
---

# Supported MongoDB data types and drivers  |  Firestore with MongoDB compatibility  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/supported-data-types-drivers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore with MongoDB compatibility ](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs)
  * [ Guides ](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Supported MongoDB data types and drivers

The following tables list supported MongoDB data types, drivers, and third-party tools for Firestore with MongoDB compatibility.

## Data types

**BSON Type** | **Supported**  
---|---  
32-bit Integer | Yes  
64-bit Integer | Yes  
Array | Yes  
Binary Data | Yes  
Boolean | Yes  
Date | Yes  
DBPointer | No  
Decimal128 | Yes  
Double | Yes  
JavaScript | No  
JavaScript (with scope) | No  
MaxKey | Yes  
MinKey | Yes  
Null | Yes  
Object | Yes  
ObjectId | Yes  
Regular Expression | Yes  
String | Yes  
Symbol | No  
Timestamp | Yes  
Undefined | No  
  
## Document `_id`

The top-level `_id` field in a document must be one of the following types:

  * ObjectId
  * String
  * 64-bit Integer
  * 32-bit Integer
  * Double
  * Binary
  * Object
  * Boolean



The total size of the `_id` must not exceed 1500 bytes.

Each values within an Object-typed ID must also be of a supported ID type or an Array of values, each of which is of a supported ID type.

Other BSON types are not supported.

## Languages and MongoDB drivers

Firestore with MongoDB compatibility supports the following driver versions:

**Language** | **Driver versions**  
---|---  
Java | 5.x  
Node.js | 6.x  
5.x  
Python | 4.x  
3.x (x ≥ 12)  
Go | 2.x  
C# | 3.x  
Ruby | 2.x (x ≥ 16)  
  
### OIDC authentication support

The Go, C#, and Ruby drivers support OpenID Connect (OIDC) authentication from Google Cloud for all supported driver versions.

The Java, Node.js, and Python drivers support OIDC authentication from Google Cloud starting with the following driver versions:

  * Java: 4.10
  * Node.js: 6.7
  * Python: 4.7



## Third-party tools

Firestore with MongoDB compatibility supports third-party tools described in this section.

**Tool** | **Description** | **Notes**  
---|---|---  
[ mongoimport ](https://www.mongodb.com/docs/database-tools/mongoimport/) | MongoDB Database Tools |  See [ Bulk data loading ](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/bulk-data-loading#mongoimport)  
[ mongoexport ](https://www.mongodb.com/docs/database-tools/mongoexport/) | MongoDB Database Tools |   
[ mongodump ](https://www.mongodb.com/docs/database-tools/mongodump/) | MongoDB Database Tools |   
[ mongorestore ](https://www.mongodb.com/docs/database-tools/mongorestore/) | MongoDB Database Tools |  See [ Bulk data loading ](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/bulk-data-loading#mongorestore)  
[ mongosh ](https://www.mongodb.com/docs/mongodb-shell/) | MongoDB Shell |   
[Mongoose](https://mongoosejs.com/) | MongoDB object modeling tool |   
[ MongoDB Compass ](https://www.mongodb.com/products/tools/compass) | GUI tool for data exploration |   
**Note:** Some third-party tools require a connection string. To obtain a connection string for your Firestore with MongoDB compatibility database, you can run the [`firestore databases connection-string` command](https://cloud.google.com/sdk/gcloud/reference/firestore/databases/connection-string) using Google Cloud CLI.

## BSON and Firestore type compatibility

This section summarizes the mapping between MongoDB BSON types and Firestore values. Since BSON is a binary format and the Firestore API uses Protocol Buffers, some types map directly, while others require special map representations.

### Mapping overview

The following tables show how BSON data types correspond to Firestore protocol buffer representations.

#### Direct mappings

These types have a direct equivalent in both systems.

BSON Type | BSON | Firestore Proto | Notes  
---|---|---|---  
**Double** | `1.23` | `double_value: 1.23` |   
**String** | `"hello"` | `string_value: "hello"` |   
**Object** | 
    
    
    {  
      "a": 1.23  
    }

| 
    
    
    map_value {  
      fields {  
        key: "a"  
        value {  
          double_value: 1.23  
        }  
      }  
    }

|   
**Array** | 
    
    
    [  
      1.23,  
      "a"  
    ]

| 
    
    
    array_value {  
      values {  
        double_value: 1.23  
      }  
      values {  
        string_value: "a"  
      }  
    }

|   
**Binary (Subtype Zero)** | `BinData(0, 'SGVsbG8=')` | `bytes_value: "Hello"` |   
**Boolean** | `true` | `boolean_value: true` |   
**Null** | `null` | `null_value: NULL_VALUE` |   
**64-bit Integer** | `Long('1234567890')` | `integer_value: 1234567890` |   
**Date** | `ISODate('2026-05-22T04:00:00Z')` | 
    
    
    timestamp_value {  
      seconds: 1779470400  
      nanos: 0  
    }

| Firestore timestamp values are stored at microsecond precision, but anything beyond millisecond precision is lost when converting to BSON.  
  
#### BSON types represented as maps in Firestore API

These BSON types are wrapped in the Firestore `map_value` with special keys to denote the type.

BSON Type | BSON | Firestore Proto | Notes  
---|---|---|---  
**32-bit Integer** | `123` | 
    
    
    map_value {  
      fields {  
        key: "__int__"  
        value {  
          integer_value: 123  
        }  
      }  
    }

|   
**Binary (Non-Zero Subtype)** | `BinData(1, 'AQIDBA==')` | 
    
    
    map_value {  
      fields {  
        key: "__binary__"  
        value {  
          bytes_value: "<subtype + data>"  
        }  
      }  
    }

| Subtype byte prepended to data.  
**ObjectId** | `ObjectId('67eea9446dc71ec469e9496a')` | 
    
    
    map_value {  
      fields {  
        key: "__oid__"  
        value {  
          string_value:  
            "67eea9446dc71ec469e9496a"  
        }  
      }  
    }

| Lowercase hex string.  
**Timestamp (Internal)** | `Timestamp(123, 1)` | 
    
    
    map_value {  
      fields {  
        key: "__request_timestamp__"  
        value {  
          map_value {  
            fields {  
              key: "seconds"  
              value {  
                integer_value: 123  
              }  
            }  
            fields {  
              key: "increment"  
              value {  
                integer_value: 1  
              }  
            }  
          }  
        }  
      }  
    }

| MongoDB internal timestamp.  
**Regular Expression** | `RegExp('.*', 'im')` | 
    
    
    map_value {  
      fields {  
        key: "__regex__"  
        value {  
          map_value {  
            fields {  
              key: "pattern"  
              value {  
                string_value: ".*"  
              }  
            }  
            fields {  
              key: "options"  
              value {  
                string_value: "im"  
              }  
            }  
          }  
        }  
      }  
    }

|   
**Min Key** | `MinKey()` | 
    
    
    map_value {  
      fields {  
        key: "__min__"  
        value {  
          null_value: NULL_VALUE  
        }  
      }  
    }

|   
**Max Key** | `MaxKey()` | 
    
    
    map_value {  
      fields {  
        key: "__max__"  
        value {  
          null_value: NULL_VALUE  
        }  
      }  
    }

|   
**Decimal128** | `Decimal128('4E7')` | 
    
    
    map_value {  
      fields {  
        key: "__decimal128__"  
        value {  
          string_value: "4E7"  
        }  
      }  
    }

|   
  
#### Firestore types not natively in BSON

These Firestore types are represented as specially structured maps when converted to BSON.

Firestore Type | BSON | Firestore Proto  
---|---|---  
**GeoPoint** | 
    
    
    {  
      "__fs_geopoint__": {  
        "latitude": 37.42,  
        "longitude": -122.08  
      }  
    }

| 
    
    
    geo_point_value {  
      latitude: 37.42  
      longitude: -122.08  
    }  
  
**Vector** | 
    
    
    {  
      "__fs_vector__": [  
        1.0,  
        2.0  
      ]  
    }

| 
    
    
    map_value {  
      fields {  
        key: "__type__"  
        value {  
          string_value: "__vector__"  
        }  
      }  
      fields {  
        key: "value"  
        value {  
          array_value {  
            ...  
          }  
        }  
      }  
    }  
  
**Document Ref** | 
    
    
    {  
      "__fs_ref__": "projects/.../documents/col/doc"  
    }

| `reference_value: "projects/.../documents/col/doc"`  
  
### Field names

Field names from MongoDB that match `__.*__` are escaped by incorporating `r:` when stored in Firestore. For example, a BSON field `__foo__` becomes `__r:foo__` in Firestore.

### BSON data types in client SDKs

When using Firestore client SDKs, you can use specialized SDK classes to represent BSON data types like 128-bit decimals, regular expressions, and BSON timestamps.

##### Node.js
    
    
    const { RegexValue, Decimal128Value, BsonTimestamp } = require('[@google-cloud/firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview.html)');
    
    // Setting fields with BSON data types
    const res = await db.collection('foo').doc('bar').set({
      regex: new [RegexValue](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/regexvalue.html)('myRegexPattern', 'i'),
      decimal: new [Decimal128Value](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/decimal128value.html)('0.73e-7'),
      bsonTimestamp: new [BsonTimestamp](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/bsontimestamp.html)(1732754912, 500),
    });
        

##### Java
    
    
    import com.google.cloud.firestore.[BsonTimestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.BsonTimestamp.html);
    import com.google.cloud.firestore.[Decimal128Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Decimal128Value.html);
    import com.google.cloud.firestore.[RegexValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.RegexValue.html);
    import java.util.HashMap;
    import java.util.Map;
    
    Map<String, Object> data = new HashMap<>();
    data.put("regex", new [RegexValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.RegexValue.html)("myRegexPattern", "i"));
    data.put("decimal", new [Decimal128Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Decimal128Value.html)("0.73e-7"));
    data.put("bson_timestamp", new [BsonTimestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.BsonTimestamp.html)(1732754912, 500));
    
    db.collection("foo").doc("bar").set(data);
        

##### Java  
Android
    
    
    import com.google.firebase.firestore.BsonTimestamp;
    import com.google.firebase.firestore.Decimal128Value;
    import com.google.firebase.firestore.RegexValue;
    import java.util.HashMap;
    import java.util.Map;
    
    Map<String, Object> data = new HashMap<>();
    data.put("regex", new RegexValue("myRegexPattern", "i"));
    data.put("decimal", new Decimal128Value("0.73e-7"));
    data.put("bson_timestamp", new BsonTimestamp(1732754912, 500));
    
    db.collection("foo").doc("bar").set(data);
        

##### Go
    
    
    import (
        "context"
    
        "cloud.google.com/go/firestore"
    )
    
    func writeBsonTypes(ctx context.Context, client *firestore.Client) error {
        _, err := client.Collection("foo").Doc("bar").Set(ctx, map[string]interface{}{
            "regex":     firestore.RegexValue{Pattern: "myRegexPattern", Options: "i"},
            "decimal":   firestore.Decimal128Value{Value: "0.73e-7"},
            "bson_timestamp": firestore.BsonTimestamp{Seconds: 1732754912, Increment: 500},
        })
        return err
    }
        

## What's next

  * Run the [Quickstart: Create a database and connect to it](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/create-and-query-database).
  * Learn about [Behavior differences](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/behavior-differences).
  * For a breakdown of supported features depending on MongoDB version, see 
    * [Supported features: 8.0](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/supported-features-80)
    * [Supported features: 7.0](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/supported-features-70)
    * [Supported features: 6.0](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/supported-features-60)
    * [Supported features: 5.0](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/supported-features-50)
    * [Supported features: 4.0](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/supported-features-40)
    * [Supported features: 3.6](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/supported-features-36)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
