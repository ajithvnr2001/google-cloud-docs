---
url: https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.lookupversionrequest
title: Class protos.google.cloud.managedkafka.schemaregistry.v1.LookupVersionRequest (0.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:57:06.089775+00:00
---

# Class protos.google.cloud.managedkafka.schemaregistry.v1.LookupVersionRequest (0.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.lookupversionrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.managedkafka.schemaregistry.v1.LookupVersionRequest (0.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a LookupVersionRequest.

## Implements

[protos.google.cloud.managedkafka.schemaregistry.v1.ILookupVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ilookupversionrequest)

## Package

[@google-cloud/managedkafka-schemaregistry](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.managedkafka.schemaregistry.v1.ILookupVersionRequest);

Constructs a new LookupVersionRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ILookupVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ilookupversionrequest)`   
Properties to set  
  
## Properties 

### deleted
    
    
    public deleted?: (boolean|null);

LookupVersionRequest deleted.

### normalize
    
    
    public normalize?: (boolean|null);

LookupVersionRequest normalize.

### parent
    
    
    public parent: string;

LookupVersionRequest parent.

### references
    
    
    public references: google.cloud.managedkafka.schemaregistry.v1.Schema.ISchemaReference[];

LookupVersionRequest references.

### schema
    
    
    public schema: string;

LookupVersionRequest schema.

### schemaType
    
    
    public schemaType?: (google.cloud.managedkafka.schemaregistry.v1.Schema.SchemaType|keyof typeof google.cloud.managedkafka.schemaregistry.v1.Schema.SchemaType|null);

LookupVersionRequest schemaType.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.managedkafka.schemaregistry.v1.ILookupVersionRequest): google.cloud.managedkafka.schemaregistry.v1.LookupVersionRequest;

Creates a new LookupVersionRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ILookupVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ilookupversionrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[LookupVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.lookupversionrequest)` | LookupVersionRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.managedkafka.schemaregistry.v1.LookupVersionRequest;

Decodes a LookupVersionRequest message from the specified reader or buffer.

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
`[LookupVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.lookupversionrequest)` | LookupVersionRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.managedkafka.schemaregistry.v1.LookupVersionRequest;

Decodes a LookupVersionRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[LookupVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.lookupversionrequest)` | LookupVersionRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.managedkafka.schemaregistry.v1.ILookupVersionRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified LookupVersionRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ILookupVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ilookupversionrequest)`   
LookupVersionRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.managedkafka.schemaregistry.v1.ILookupVersionRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified LookupVersionRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ILookupVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.ilookupversionrequest)`   
LookupVersionRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.managedkafka.schemaregistry.v1.LookupVersionRequest;

Creates a LookupVersionRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[LookupVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.lookupversionrequest)` | LookupVersionRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for LookupVersionRequest

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

Converts this LookupVersionRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.managedkafka.schemaregistry.v1.LookupVersionRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a LookupVersionRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[LookupVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/managedkafka-schemaregistry/latest/managedkafka-schemaregistry/protos.google.cloud.managedkafka.schemaregistry.v1.lookupversionrequest)`   
LookupVersionRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a LookupVersionRequest message.

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
