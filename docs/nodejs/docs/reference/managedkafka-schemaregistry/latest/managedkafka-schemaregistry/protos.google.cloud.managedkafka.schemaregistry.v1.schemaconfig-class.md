---
url: https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.schemaconfig-class
title: Class protos.google.cloud.managedkafka.schemaregistry.v1.SchemaConfig (0.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:57:07.137961+00:00
---

# Class protos.google.cloud.managedkafka.schemaregistry.v1.SchemaConfig (0.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.schemaconfig-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.managedkafka.schemaregistry.v1.SchemaConfig (0.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a SchemaConfig.

## Implements

[protos.google.cloud.managedkafka.schemaregistry.v1.ISchemaConfig](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ischemaconfig)

## Package

[@google-cloud/managedkafka-schemaregistry](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.managedkafka.schemaregistry.v1.ISchemaConfig);

Constructs a new SchemaConfig.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISchemaConfig](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ischemaconfig)`   
Properties to set  
  
## Properties 

### alias
    
    
    public alias: string;

SchemaConfig alias.

### compatibility
    
    
    public compatibility?: (google.cloud.managedkafka.schemaregistry.v1.SchemaConfig.CompatibilityType|keyof typeof google.cloud.managedkafka.schemaregistry.v1.SchemaConfig.CompatibilityType|null);

SchemaConfig compatibility.

### normalize
    
    
    public normalize?: (boolean|null);

SchemaConfig normalize.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.managedkafka.schemaregistry.v1.ISchemaConfig): google.cloud.managedkafka.schemaregistry.v1.SchemaConfig;

Creates a new SchemaConfig instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISchemaConfig](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ischemaconfig)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[SchemaConfig](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.schemaconfig-class)` | SchemaConfig instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.managedkafka.schemaregistry.v1.SchemaConfig;

Decodes a SchemaConfig message from the specified reader or buffer.

**Parameters**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
`length` |  `number`   
Message length if known beforehand  
**Returns**  
---  
**Type** | **Description**  
`[SchemaConfig](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.schemaconfig-class)` | SchemaConfig  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.managedkafka.schemaregistry.v1.SchemaConfig;

Decodes a SchemaConfig message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[SchemaConfig](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.schemaconfig-class)` | SchemaConfig  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.managedkafka.schemaregistry.v1.ISchemaConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SchemaConfig message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISchemaConfig](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ischemaconfig)`   
SchemaConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.managedkafka.schemaregistry.v1.ISchemaConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SchemaConfig message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISchemaConfig](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ischemaconfig)`   
SchemaConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.managedkafka.schemaregistry.v1.SchemaConfig;

Creates a SchemaConfig message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[SchemaConfig](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.schemaconfig-class)` | SchemaConfig  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for SchemaConfig

**Parameter**  
---  
**Name** | **Description**  
`typeUrlPrefix` |  `string`   
your custom typeUrlPrefix(default "type.googleapis.com")  
**Returns**  
---  
**Type** | **Description**  
`string` | The default type url  
  
### toJSON()
    
    
    public toJSON(): { [k: string]: any };

Converts this SchemaConfig to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.managedkafka.schemaregistry.v1.SchemaConfig, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a SchemaConfig message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[SchemaConfig](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.schemaconfig-class)`   
SchemaConfig  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a SchemaConfig message.

**Parameter**  
---  
**Name** | **Description**  
`message` |  `{ [k: string]: any }`   
Plain object to verify  
**Returns**  
---  
**Type** | **Description**  
`(string|null)` | `null` if valid, otherwise the reason why it is not  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
