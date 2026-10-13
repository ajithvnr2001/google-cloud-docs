---
url: https://docs.cloud.google.com/nodejs/docs/reference/lineage/latest/lineage/protos.google.cloud.datacatalog.lineage.v1.run-class
title: Class protos.google.cloud.datacatalog.lineage.v1.Run (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:39:13.281524+00:00
---

# Class protos.google.cloud.datacatalog.lineage.v1.Run (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/lineage/latest/lineage/protos.google.cloud.datacatalog.lineage.v1.run-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.datacatalog.lineage.v1.Run (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.2.0  1.1.0  0.1.2 

Represents a Run.

## Implements

[protos.google.cloud.datacatalog.lineage.v1.IRun](https://docs.cloud.google.com/nodejs/docs/reference/lineage/latest/lineage/protos.google.cloud.datacatalog.lineage.v1.irun)

## Package

[@google-cloud/lineage](https://docs.cloud.google.com/nodejs/docs/reference/lineage/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.datacatalog.lineage.v1.IRun);

Constructs a new Run.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IRun](https://docs.cloud.google.com/nodejs/docs/reference/lineage/latest/lineage/protos.google.cloud.datacatalog.lineage.v1.irun)`   
Properties to set  
  
## Properties 

### attributes
    
    
    public attributes: { [k: string]: google.protobuf.IValue };

Run attributes.

### displayName
    
    
    public displayName: string;

Run displayName.

### endTime
    
    
    public endTime?: (google.protobuf.ITimestamp|null);

Run endTime.

### name
    
    
    public name: string;

Run name.

### startTime
    
    
    public startTime?: (google.protobuf.ITimestamp|null);

Run startTime.

### state
    
    
    public state: (google.cloud.datacatalog.lineage.v1.Run.State|keyof typeof google.cloud.datacatalog.lineage.v1.Run.State);

Run state.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.datacatalog.lineage.v1.IRun): google.cloud.datacatalog.lineage.v1.Run;

Creates a new Run instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IRun](https://docs.cloud.google.com/nodejs/docs/reference/lineage/latest/lineage/protos.google.cloud.datacatalog.lineage.v1.irun)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Run](https://docs.cloud.google.com/nodejs/docs/reference/lineage/latest/lineage/protos.google.cloud.datacatalog.lineage.v1.run-class)` | Run instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.datacatalog.lineage.v1.Run;

Decodes a Run message from the specified reader or buffer.

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
`[Run](https://docs.cloud.google.com/nodejs/docs/reference/lineage/latest/lineage/protos.google.cloud.datacatalog.lineage.v1.run-class)` | Run  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.datacatalog.lineage.v1.Run;

Decodes a Run message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Run](https://docs.cloud.google.com/nodejs/docs/reference/lineage/latest/lineage/protos.google.cloud.datacatalog.lineage.v1.run-class)` | Run  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.datacatalog.lineage.v1.IRun, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Run message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IRun](https://docs.cloud.google.com/nodejs/docs/reference/lineage/latest/lineage/protos.google.cloud.datacatalog.lineage.v1.irun)`   
Run message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.datacatalog.lineage.v1.IRun, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Run message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IRun](https://docs.cloud.google.com/nodejs/docs/reference/lineage/latest/lineage/protos.google.cloud.datacatalog.lineage.v1.irun)`   
Run message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.datacatalog.lineage.v1.Run;

Creates a Run message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Run](https://docs.cloud.google.com/nodejs/docs/reference/lineage/latest/lineage/protos.google.cloud.datacatalog.lineage.v1.run-class)` | Run  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Run

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

Converts this Run to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.datacatalog.lineage.v1.Run, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Run message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Run](https://docs.cloud.google.com/nodejs/docs/reference/lineage/latest/lineage/protos.google.cloud.datacatalog.lineage.v1.run-class)`   
Run  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Run message.

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
