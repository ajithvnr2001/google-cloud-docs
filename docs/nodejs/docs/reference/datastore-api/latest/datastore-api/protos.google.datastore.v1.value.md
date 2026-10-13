---
url: https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.value
title: Class protos.google.datastore.v1.Value (0.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:47:55.385457+00:00
---

# Class protos.google.datastore.v1.Value (0.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.value

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.datastore.v1.Value (0.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a Value.

## Implements

[protos.google.datastore.v1.IValue](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.ivalue)

## Package

[@google-cloud/datastore-api](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.datastore.v1.IValue);

Constructs a new Value.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IValue](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.ivalue)`   
Properties to set  
  
## Properties 

### arrayValue
    
    
    public arrayValue?: (google.datastore.v1.IArrayValue|null);

Value arrayValue.

### blobValue
    
    
    public blobValue?: (Uint8Array|Buffer|string|null);

Value blobValue.

### booleanValue
    
    
    public booleanValue?: (boolean|null);

Value booleanValue.

### doubleValue
    
    
    public doubleValue?: (number|null);

Value doubleValue.

### entityValue
    
    
    public entityValue?: (google.datastore.v1.IEntity|null);

Value entityValue.

### excludeFromIndexes
    
    
    public excludeFromIndexes: boolean;

Value excludeFromIndexes.

### geoPointValue
    
    
    public geoPointValue?: (google.type.ILatLng|null);

Value geoPointValue.

### integerValue
    
    
    public integerValue?: (number|Long|string|null);

Value integerValue.

### keyValue
    
    
    public keyValue?: (google.datastore.v1.IKey|null);

Value keyValue.

### meaning
    
    
    public meaning: number;

Value meaning.

### nullValue
    
    
    public nullValue?: (google.protobuf.NullValue|keyof typeof google.protobuf.NullValue|null);

Value nullValue.

### stringValue
    
    
    public stringValue?: (string|null);

Value stringValue.

### timestampValue
    
    
    public timestampValue?: (google.protobuf.ITimestamp|null);

Value timestampValue.

### valueType
    
    
    public valueType?: ("nullValue"|"booleanValue"|"integerValue"|"doubleValue"|"timestampValue"|"keyValue"|"stringValue"|"blobValue"|"geoPointValue"|"entityValue"|"arrayValue");

Value valueType.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.datastore.v1.IValue): google.datastore.v1.Value;

Creates a new Value instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IValue](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.ivalue)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Value](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.value)` | Value instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.datastore.v1.Value;

Decodes a Value message from the specified reader or buffer.

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
`[Value](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.value)` | Value  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.datastore.v1.Value;

Decodes a Value message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Value](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.value)` | Value  
  
### encode(message, writer)
    
    
    public static encode(message: google.datastore.v1.IValue, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Value message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IValue](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.ivalue)`   
Value message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.datastore.v1.IValue, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Value message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IValue](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.ivalue)`   
Value message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.datastore.v1.Value;

Creates a Value message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Value](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.value)` | Value  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Value

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

Converts this Value to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.datastore.v1.Value, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Value message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Value](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.value)`   
Value  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Value message.

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

Last updated 2026-08-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-01 UTC."],[],[]] 
