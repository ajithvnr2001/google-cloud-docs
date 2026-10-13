---
url: https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1beta.backupfile
title: Class protos.google.cloud.memorystore.v1beta.BackupFile (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:02:09.668129+00:00
---

# Class protos.google.cloud.memorystore.v1beta.BackupFile (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1beta.backupfile

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.memorystore.v1beta.BackupFile (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.8.0  0.7.0  0.4.0  0.1.0 

Represents a BackupFile.

## Implements

[protos.google.cloud.memorystore.v1beta.IBackupFile](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1beta.ibackupfile)

## Package

[@google-cloud/memorystore](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.memorystore.v1beta.IBackupFile);

Constructs a new BackupFile.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBackupFile](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1beta.ibackupfile)`   
Properties to set  
  
## Properties 

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

BackupFile createTime.

### fileName
    
    
    public fileName: string;

BackupFile fileName.

### sizeBytes
    
    
    public sizeBytes: (number|Long|string);

BackupFile sizeBytes.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.memorystore.v1beta.IBackupFile): google.cloud.memorystore.v1beta.BackupFile;

Creates a new BackupFile instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBackupFile](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1beta.ibackupfile)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[BackupFile](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1beta.backupfile)` | BackupFile instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.memorystore.v1beta.BackupFile;

Decodes a BackupFile message from the specified reader or buffer.

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
`[BackupFile](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1beta.backupfile)` | BackupFile  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.memorystore.v1beta.BackupFile;

Decodes a BackupFile message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[BackupFile](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1beta.backupfile)` | BackupFile  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.memorystore.v1beta.IBackupFile, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BackupFile message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBackupFile](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1beta.ibackupfile)`   
BackupFile message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.memorystore.v1beta.IBackupFile, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BackupFile message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBackupFile](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1beta.ibackupfile)`   
BackupFile message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.memorystore.v1beta.BackupFile;

Creates a BackupFile message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[BackupFile](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1beta.backupfile)` | BackupFile  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for BackupFile

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

Converts this BackupFile to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.memorystore.v1beta.BackupFile, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a BackupFile message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[BackupFile](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1beta.backupfile)`   
BackupFile  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a BackupFile message.

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
