---
url: https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.migrationwarning-class
title: Class protos.google.cloud.vmmigration.v1.MigrationWarning (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:45:08.184505+00:00
---

# Class protos.google.cloud.vmmigration.v1.MigrationWarning (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.migrationwarning-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.vmmigration.v1.MigrationWarning (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.0  3.0.2  2.3.2  2.2.1  2.1.0  1.0.0  0.2.0 

Represents a MigrationWarning.

## Implements

[protos.google.cloud.vmmigration.v1.IMigrationWarning](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.imigrationwarning)

## Package

[@google-cloud/vmmigration](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.vmmigration.v1.IMigrationWarning);

Constructs a new MigrationWarning.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IMigrationWarning](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.imigrationwarning)`   
Properties to set  
  
## Properties 

### actionItem
    
    
    public actionItem?: (google.rpc.ILocalizedMessage|null);

MigrationWarning actionItem.

### code
    
    
    public code: (google.cloud.vmmigration.v1.MigrationWarning.WarningCode|keyof typeof google.cloud.vmmigration.v1.MigrationWarning.WarningCode);

MigrationWarning code.

### helpLinks
    
    
    public helpLinks: google.rpc.Help.ILink[];

MigrationWarning helpLinks.

### warningMessage
    
    
    public warningMessage?: (google.rpc.ILocalizedMessage|null);

MigrationWarning warningMessage.

### warningTime
    
    
    public warningTime?: (google.protobuf.ITimestamp|null);

MigrationWarning warningTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.vmmigration.v1.IMigrationWarning): google.cloud.vmmigration.v1.MigrationWarning;

Creates a new MigrationWarning instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IMigrationWarning](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.imigrationwarning)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[MigrationWarning](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.migrationwarning-class)` | MigrationWarning instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.vmmigration.v1.MigrationWarning;

Decodes a MigrationWarning message from the specified reader or buffer.

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
`[MigrationWarning](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.migrationwarning-class)` | MigrationWarning  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.vmmigration.v1.MigrationWarning;

Decodes a MigrationWarning message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[MigrationWarning](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.migrationwarning-class)` | MigrationWarning  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.vmmigration.v1.IMigrationWarning, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified MigrationWarning message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IMigrationWarning](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.imigrationwarning)`   
MigrationWarning message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.vmmigration.v1.IMigrationWarning, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified MigrationWarning message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IMigrationWarning](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.imigrationwarning)`   
MigrationWarning message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.vmmigration.v1.MigrationWarning;

Creates a MigrationWarning message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[MigrationWarning](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.migrationwarning-class)` | MigrationWarning  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for MigrationWarning

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

Converts this MigrationWarning to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.vmmigration.v1.MigrationWarning, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a MigrationWarning message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[MigrationWarning](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.migrationwarning-class)`   
MigrationWarning  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a MigrationWarning message.

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
