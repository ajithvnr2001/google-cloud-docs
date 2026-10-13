---
url: https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1.attacheddisk-class
title: Class protos.google.cloud.backupdr.v1.AttachedDisk (0.12.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:05:03.261156+00:00
---

# Class protos.google.cloud.backupdr.v1.AttachedDisk (0.12.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1.attacheddisk-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.backupdr.v1.AttachedDisk (0.12.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.1 (latest)  0.12.0  0.9.0  0.8.0  0.7.0  0.6.0  0.1.0 

Represents an AttachedDisk.

## Implements

[protos.google.cloud.backupdr.v1.IAttachedDisk](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1.iattacheddisk)

## Package

[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.backupdr.v1.IAttachedDisk);

Constructs a new AttachedDisk.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAttachedDisk](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1.iattacheddisk)`   
Properties to set  
  
## Properties 

### autoDelete
    
    
    public autoDelete?: (boolean|null);

AttachedDisk autoDelete.

### boot
    
    
    public boot?: (boolean|null);

AttachedDisk boot.

### deviceName
    
    
    public deviceName?: (string|null);

AttachedDisk deviceName.

### diskEncryptionKey
    
    
    public diskEncryptionKey?: (google.cloud.backupdr.v1.ICustomerEncryptionKey|null);

AttachedDisk diskEncryptionKey.

### diskInterface
    
    
    public diskInterface?: (google.cloud.backupdr.v1.AttachedDisk.DiskInterface|keyof typeof google.cloud.backupdr.v1.AttachedDisk.DiskInterface|null);

AttachedDisk diskInterface.

### diskSizeGb
    
    
    public diskSizeGb?: (number|Long|string|null);

AttachedDisk diskSizeGb.

### diskType
    
    
    public diskType?: (string|null);

AttachedDisk diskType.

### diskTypeDeprecated
    
    
    public diskTypeDeprecated?: (google.cloud.backupdr.v1.AttachedDisk.DiskType|keyof typeof google.cloud.backupdr.v1.AttachedDisk.DiskType|null);

AttachedDisk diskTypeDeprecated.

### guestOsFeature
    
    
    public guestOsFeature: google.cloud.backupdr.v1.IGuestOsFeature[];

AttachedDisk guestOsFeature.

### index
    
    
    public index?: (number|Long|string|null);

AttachedDisk index.

### initializeParams
    
    
    public initializeParams?: (google.cloud.backupdr.v1.AttachedDisk.IInitializeParams|null);

AttachedDisk initializeParams.

### kind
    
    
    public kind?: (string|null);

AttachedDisk kind.

### license
    
    
    public license: string[];

AttachedDisk license.

### mode
    
    
    public mode?: (google.cloud.backupdr.v1.AttachedDisk.DiskMode|keyof typeof google.cloud.backupdr.v1.AttachedDisk.DiskMode|null);

AttachedDisk mode.

### savedState
    
    
    public savedState?: (google.cloud.backupdr.v1.AttachedDisk.DiskSavedState|keyof typeof google.cloud.backupdr.v1.AttachedDisk.DiskSavedState|null);

AttachedDisk savedState.

### source
    
    
    public source?: (string|null);

AttachedDisk source.

### type
    
    
    public type?: (google.cloud.backupdr.v1.AttachedDisk.DiskType|keyof typeof google.cloud.backupdr.v1.AttachedDisk.DiskType|null);

AttachedDisk type.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.backupdr.v1.IAttachedDisk): google.cloud.backupdr.v1.AttachedDisk;

Creates a new AttachedDisk instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAttachedDisk](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1.iattacheddisk)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AttachedDisk](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1.attacheddisk-class)` | AttachedDisk instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.backupdr.v1.AttachedDisk;

Decodes an AttachedDisk message from the specified reader or buffer.

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
`[AttachedDisk](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1.attacheddisk-class)` | AttachedDisk  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.backupdr.v1.AttachedDisk;

Decodes an AttachedDisk message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AttachedDisk](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1.attacheddisk-class)` | AttachedDisk  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.backupdr.v1.IAttachedDisk, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AttachedDisk message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAttachedDisk](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1.iattacheddisk)`   
AttachedDisk message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.backupdr.v1.IAttachedDisk, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AttachedDisk message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAttachedDisk](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1.iattacheddisk)`   
AttachedDisk message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.backupdr.v1.AttachedDisk;

Creates an AttachedDisk message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AttachedDisk](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1.attacheddisk-class)` | AttachedDisk  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AttachedDisk

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

Converts this AttachedDisk to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.backupdr.v1.AttachedDisk, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AttachedDisk message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AttachedDisk](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1.attacheddisk-class)`   
AttachedDisk  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AttachedDisk message.

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
