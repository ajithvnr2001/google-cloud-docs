---
url: https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1.diskrestoreproperties-class
title: Class protos.google.cloud.backupdr.v1.DiskRestoreProperties (0.12.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:26:35.981506+00:00
---

# Class protos.google.cloud.backupdr.v1.DiskRestoreProperties (0.12.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1.diskrestoreproperties-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.backupdr.v1.DiskRestoreProperties (0.12.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.1 (latest)  0.12.0  0.9.0  0.8.0  0.7.0  0.6.0  0.1.0 

Represents a DiskRestoreProperties.

## Implements

[protos.google.cloud.backupdr.v1.IDiskRestoreProperties](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1.idiskrestoreproperties)

## Package

[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.backupdr.v1.IDiskRestoreProperties);

Constructs a new DiskRestoreProperties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDiskRestoreProperties](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1.idiskrestoreproperties)`   
Properties to set  
  
## Properties 

### accessMode
    
    
    public accessMode?: (google.cloud.backupdr.v1.DiskRestoreProperties.AccessMode|keyof typeof google.cloud.backupdr.v1.DiskRestoreProperties.AccessMode|null);

DiskRestoreProperties accessMode.

### architecture
    
    
    public architecture?: (google.cloud.backupdr.v1.DiskRestoreProperties.Architecture|keyof typeof google.cloud.backupdr.v1.DiskRestoreProperties.Architecture|null);

DiskRestoreProperties architecture.

### description
    
    
    public description?: (string|null);

DiskRestoreProperties description.

### diskEncryptionKey
    
    
    public diskEncryptionKey?: (google.cloud.backupdr.v1.ICustomerEncryptionKey|null);

DiskRestoreProperties diskEncryptionKey.

### enableConfidentialCompute
    
    
    public enableConfidentialCompute?: (boolean|null);

DiskRestoreProperties enableConfidentialCompute.

### guestOsFeature
    
    
    public guestOsFeature: google.cloud.backupdr.v1.IGuestOsFeature[];

DiskRestoreProperties guestOsFeature.

### labels
    
    
    public labels: { [k: string]: string };

DiskRestoreProperties labels.

### licenses
    
    
    public licenses: string[];

DiskRestoreProperties licenses.

### name
    
    
    public name?: (string|null);

DiskRestoreProperties name.

### physicalBlockSizeBytes
    
    
    public physicalBlockSizeBytes?: (number|Long|string|null);

DiskRestoreProperties physicalBlockSizeBytes.

### provisionedIops
    
    
    public provisionedIops?: (number|Long|string|null);

DiskRestoreProperties provisionedIops.

### provisionedThroughput
    
    
    public provisionedThroughput?: (number|Long|string|null);

DiskRestoreProperties provisionedThroughput.

### resourceManagerTags
    
    
    public resourceManagerTags: { [k: string]: string };

DiskRestoreProperties resourceManagerTags.

### resourcePolicy
    
    
    public resourcePolicy: string[];

DiskRestoreProperties resourcePolicy.

### sizeGb
    
    
    public sizeGb?: (number|Long|string|null);

DiskRestoreProperties sizeGb.

### storagePool
    
    
    public storagePool?: (string|null);

DiskRestoreProperties storagePool.

### type
    
    
    public type?: (string|null);

DiskRestoreProperties type.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.backupdr.v1.IDiskRestoreProperties): google.cloud.backupdr.v1.DiskRestoreProperties;

Creates a new DiskRestoreProperties instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDiskRestoreProperties](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1.idiskrestoreproperties)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DiskRestoreProperties](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1.diskrestoreproperties-class)` | DiskRestoreProperties instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.backupdr.v1.DiskRestoreProperties;

Decodes a DiskRestoreProperties message from the specified reader or buffer.

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
`[DiskRestoreProperties](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1.diskrestoreproperties-class)` | DiskRestoreProperties  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.backupdr.v1.DiskRestoreProperties;

Decodes a DiskRestoreProperties message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DiskRestoreProperties](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1.diskrestoreproperties-class)` | DiskRestoreProperties  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.backupdr.v1.IDiskRestoreProperties, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DiskRestoreProperties message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDiskRestoreProperties](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1.idiskrestoreproperties)`   
DiskRestoreProperties message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.backupdr.v1.IDiskRestoreProperties, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DiskRestoreProperties message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDiskRestoreProperties](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1.idiskrestoreproperties)`   
DiskRestoreProperties message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.backupdr.v1.DiskRestoreProperties;

Creates a DiskRestoreProperties message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DiskRestoreProperties](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1.diskrestoreproperties-class)` | DiskRestoreProperties  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DiskRestoreProperties

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

Converts this DiskRestoreProperties to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.backupdr.v1.DiskRestoreProperties, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DiskRestoreProperties message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DiskRestoreProperties](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1.diskrestoreproperties-class)`   
DiskRestoreProperties  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DiskRestoreProperties message.

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
