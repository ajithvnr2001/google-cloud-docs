---
url: https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.executor.v1.mutationaction.mod
title: Class protos.google.spanner.executor.v1.MutationAction.Mod (0.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:51:33.203984+00:00
---

# Class protos.google.spanner.executor.v1.MutationAction.Mod (0.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.executor.v1.mutationaction.mod

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.spanner.executor.v1.MutationAction.Mod (0.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a Mod.

## Implements

[protos.google.spanner.executor.v1.MutationAction.IMod](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.executor.v1.mutationaction.imod)

## Package

[@google-cloud/spanner-api](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.spanner.executor.v1.MutationAction.IMod);

Constructs a new Mod.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IMod](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.executor.v1.mutationaction.imod)`   
Properties to set  
  
## Properties 

### deleteKeys
    
    
    public deleteKeys?: (google.spanner.executor.v1.IKeySet|null);

Mod deleteKeys.

### insert
    
    
    public insert?: (google.spanner.executor.v1.MutationAction.IInsertArgs|null);

Mod insert.

### insertOrUpdate
    
    
    public insertOrUpdate?: (google.spanner.executor.v1.MutationAction.IInsertArgs|null);

Mod insertOrUpdate.

### replace
    
    
    public replace?: (google.spanner.executor.v1.MutationAction.IInsertArgs|null);

Mod replace.

### table
    
    
    public table: string;

Mod table.

### update
    
    
    public update?: (google.spanner.executor.v1.MutationAction.IUpdateArgs|null);

Mod update.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.spanner.executor.v1.MutationAction.IMod): google.spanner.executor.v1.MutationAction.Mod;

Creates a new Mod instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IMod](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.executor.v1.mutationaction.imod)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Mod](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.executor.v1.mutationaction.mod)` | Mod instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.spanner.executor.v1.MutationAction.Mod;

Decodes a Mod message from the specified reader or buffer.

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
`[Mod](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.executor.v1.mutationaction.mod)` | Mod  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.spanner.executor.v1.MutationAction.Mod;

Decodes a Mod message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Mod](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.executor.v1.mutationaction.mod)` | Mod  
  
### encode(message, writer)
    
    
    public static encode(message: google.spanner.executor.v1.MutationAction.IMod, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Mod message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IMod](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.executor.v1.mutationaction.imod)`   
Mod message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.spanner.executor.v1.MutationAction.IMod, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Mod message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IMod](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.executor.v1.mutationaction.imod)`   
Mod message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.spanner.executor.v1.MutationAction.Mod;

Creates a Mod message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Mod](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.executor.v1.mutationaction.mod)` | Mod  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Mod

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

Converts this Mod to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.spanner.executor.v1.MutationAction.Mod, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Mod message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Mod](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.executor.v1.mutationaction.mod)`   
Mod  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Mod message.

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

Last updated 2026-07-31 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-31 UTC."],[],[]] 
