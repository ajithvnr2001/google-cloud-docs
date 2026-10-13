---
url: https://docs.cloud.google.com/nodejs/docs/reference/gke-backup/latest/gke-backup/protos.google.cloud.gkebackup.v1.restoreconfig.restoreorder.groupkinddependency
title: Class protos.google.cloud.gkebackup.v1.RestoreConfig.RestoreOrder.GroupKindDependency (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:17:14.052928+00:00
---

# Class protos.google.cloud.gkebackup.v1.RestoreConfig.RestoreOrder.GroupKindDependency (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/gke-backup/latest/gke-backup/protos.google.cloud.gkebackup.v1.restoreconfig.restoreorder.groupkinddependency

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.gkebackup.v1.RestoreConfig.RestoreOrder.GroupKindDependency (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.1.0  2.0.1  1.3.0  1.0.0  0.3.2  0.2.2 

Represents a GroupKindDependency.

## Implements

[protos.google.cloud.gkebackup.v1.RestoreConfig.RestoreOrder.IGroupKindDependency](https://docs.cloud.google.com/nodejs/docs/reference/gke-backup/latest/gke-backup/protos.google.cloud.gkebackup.v1.restoreconfig.restoreorder.igroupkinddependency)

## Package

[@google-cloud/gke-backup](https://docs.cloud.google.com/nodejs/docs/reference/gke-backup/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.gkebackup.v1.RestoreConfig.RestoreOrder.IGroupKindDependency);

Constructs a new GroupKindDependency.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGroupKindDependency](https://docs.cloud.google.com/nodejs/docs/reference/gke-backup/latest/gke-backup/protos.google.cloud.gkebackup.v1.restoreconfig.restoreorder.igroupkinddependency)`   
Properties to set  
  
## Properties 

### requiring
    
    
    public requiring?: (google.cloud.gkebackup.v1.RestoreConfig.IGroupKind|null);

GroupKindDependency requiring.

### satisfying
    
    
    public satisfying?: (google.cloud.gkebackup.v1.RestoreConfig.IGroupKind|null);

GroupKindDependency satisfying.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.gkebackup.v1.RestoreConfig.RestoreOrder.IGroupKindDependency): google.cloud.gkebackup.v1.RestoreConfig.RestoreOrder.GroupKindDependency;

Creates a new GroupKindDependency instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGroupKindDependency](https://docs.cloud.google.com/nodejs/docs/reference/gke-backup/latest/gke-backup/protos.google.cloud.gkebackup.v1.restoreconfig.restoreorder.igroupkinddependency)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[GroupKindDependency](https://docs.cloud.google.com/nodejs/docs/reference/gke-backup/latest/gke-backup/protos.google.cloud.gkebackup.v1.restoreconfig.restoreorder.groupkinddependency)` | GroupKindDependency instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.gkebackup.v1.RestoreConfig.RestoreOrder.GroupKindDependency;

Decodes a GroupKindDependency message from the specified reader or buffer.

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
`[GroupKindDependency](https://docs.cloud.google.com/nodejs/docs/reference/gke-backup/latest/gke-backup/protos.google.cloud.gkebackup.v1.restoreconfig.restoreorder.groupkinddependency)` | GroupKindDependency  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.gkebackup.v1.RestoreConfig.RestoreOrder.GroupKindDependency;

Decodes a GroupKindDependency message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[GroupKindDependency](https://docs.cloud.google.com/nodejs/docs/reference/gke-backup/latest/gke-backup/protos.google.cloud.gkebackup.v1.restoreconfig.restoreorder.groupkinddependency)` | GroupKindDependency  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.gkebackup.v1.RestoreConfig.RestoreOrder.IGroupKindDependency, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GroupKindDependency message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGroupKindDependency](https://docs.cloud.google.com/nodejs/docs/reference/gke-backup/latest/gke-backup/protos.google.cloud.gkebackup.v1.restoreconfig.restoreorder.igroupkinddependency)`   
GroupKindDependency message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.gkebackup.v1.RestoreConfig.RestoreOrder.IGroupKindDependency, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GroupKindDependency message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGroupKindDependency](https://docs.cloud.google.com/nodejs/docs/reference/gke-backup/latest/gke-backup/protos.google.cloud.gkebackup.v1.restoreconfig.restoreorder.igroupkinddependency)`   
GroupKindDependency message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.gkebackup.v1.RestoreConfig.RestoreOrder.GroupKindDependency;

Creates a GroupKindDependency message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[GroupKindDependency](https://docs.cloud.google.com/nodejs/docs/reference/gke-backup/latest/gke-backup/protos.google.cloud.gkebackup.v1.restoreconfig.restoreorder.groupkinddependency)` | GroupKindDependency  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for GroupKindDependency

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

Converts this GroupKindDependency to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.gkebackup.v1.RestoreConfig.RestoreOrder.GroupKindDependency, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a GroupKindDependency message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[GroupKindDependency](https://docs.cloud.google.com/nodejs/docs/reference/gke-backup/latest/gke-backup/protos.google.cloud.gkebackup.v1.restoreconfig.restoreorder.groupkinddependency)`   
GroupKindDependency  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a GroupKindDependency message.

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

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
