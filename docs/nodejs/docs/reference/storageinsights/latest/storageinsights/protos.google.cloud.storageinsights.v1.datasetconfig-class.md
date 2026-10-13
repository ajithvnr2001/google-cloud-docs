---
url: https://docs.cloud.google.com/nodejs/docs/reference/storageinsights/latest/storageinsights/protos.google.cloud.storageinsights.v1.datasetconfig-class
title: Class protos.google.cloud.storageinsights.v1.DatasetConfig (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:30:33.447716+00:00
---

# Class protos.google.cloud.storageinsights.v1.DatasetConfig (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/storageinsights/latest/storageinsights/protos.google.cloud.storageinsights.v1.datasetconfig-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.storageinsights.v1.DatasetConfig (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.3.0  2.1.0  0.1.1 

Represents a DatasetConfig.

## Implements

[protos.google.cloud.storageinsights.v1.IDatasetConfig](https://docs.cloud.google.com/nodejs/docs/reference/storageinsights/latest/storageinsights/protos.google.cloud.storageinsights.v1.idatasetconfig)

## Package

[@google-cloud/storageinsights](https://docs.cloud.google.com/nodejs/docs/reference/storageinsights/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.storageinsights.v1.IDatasetConfig);

Constructs a new DatasetConfig.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDatasetConfig](https://docs.cloud.google.com/nodejs/docs/reference/storageinsights/latest/storageinsights/protos.google.cloud.storageinsights.v1.idatasetconfig)`   
Properties to set  
  
## Properties 

### cloudStorageBuckets
    
    
    public cloudStorageBuckets?: ("includeCloudStorageBuckets"|"excludeCloudStorageBuckets");

DatasetConfig cloudStorageBuckets.

### cloudStorageLocations
    
    
    public cloudStorageLocations?: ("includeCloudStorageLocations"|"excludeCloudStorageLocations");

DatasetConfig cloudStorageLocations.

### cloudStorageObjectPath
    
    
    public cloudStorageObjectPath?: (string|null);

DatasetConfig cloudStorageObjectPath.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

DatasetConfig createTime.

### datasetConfigState
    
    
    public datasetConfigState: (google.cloud.storageinsights.v1.DatasetConfig.ConfigState|keyof typeof google.cloud.storageinsights.v1.DatasetConfig.ConfigState);

DatasetConfig datasetConfigState.

### description
    
    
    public description: string;

DatasetConfig description.

### excludeCloudStorageBuckets
    
    
    public excludeCloudStorageBuckets?: (google.cloud.storageinsights.v1.DatasetConfig.ICloudStorageBuckets|null);

DatasetConfig excludeCloudStorageBuckets.

### excludeCloudStorageLocations
    
    
    public excludeCloudStorageLocations?: (google.cloud.storageinsights.v1.DatasetConfig.ICloudStorageLocations|null);

DatasetConfig excludeCloudStorageLocations.

### identity
    
    
    public identity?: (google.cloud.storageinsights.v1.IIdentity|null);

DatasetConfig identity.

### includeCloudStorageBuckets
    
    
    public includeCloudStorageBuckets?: (google.cloud.storageinsights.v1.DatasetConfig.ICloudStorageBuckets|null);

DatasetConfig includeCloudStorageBuckets.

### includeCloudStorageLocations
    
    
    public includeCloudStorageLocations?: (google.cloud.storageinsights.v1.DatasetConfig.ICloudStorageLocations|null);

DatasetConfig includeCloudStorageLocations.

### includeNewlyCreatedBuckets
    
    
    public includeNewlyCreatedBuckets: boolean;

DatasetConfig includeNewlyCreatedBuckets.

### labels
    
    
    public labels: { [k: string]: string };

DatasetConfig labels.

### link
    
    
    public link?: (google.cloud.storageinsights.v1.DatasetConfig.ILink|null);

DatasetConfig link.

### name
    
    
    public name: string;

DatasetConfig name.

### organizationNumber
    
    
    public organizationNumber: (number|Long|string);

DatasetConfig organizationNumber.

### organizationScope
    
    
    public organizationScope?: (boolean|null);

DatasetConfig organizationScope.

### retentionPeriodDays
    
    
    public retentionPeriodDays: number;

DatasetConfig retentionPeriodDays.

### skipVerificationAndIngest
    
    
    public skipVerificationAndIngest: boolean;

DatasetConfig skipVerificationAndIngest.

### sourceFolders
    
    
    public sourceFolders?: (google.cloud.storageinsights.v1.DatasetConfig.ISourceFolders|null);

DatasetConfig sourceFolders.

### sourceOptions
    
    
    public sourceOptions?: ("sourceProjects"|"sourceFolders"|"organizationScope"|"cloudStorageObjectPath");

DatasetConfig sourceOptions.

### sourceProjects
    
    
    public sourceProjects?: (google.cloud.storageinsights.v1.DatasetConfig.ISourceProjects|null);

DatasetConfig sourceProjects.

### status
    
    
    public status?: (google.rpc.IStatus|null);

DatasetConfig status.

### uid
    
    
    public uid: string;

DatasetConfig uid.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

DatasetConfig updateTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.storageinsights.v1.IDatasetConfig): google.cloud.storageinsights.v1.DatasetConfig;

Creates a new DatasetConfig instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDatasetConfig](https://docs.cloud.google.com/nodejs/docs/reference/storageinsights/latest/storageinsights/protos.google.cloud.storageinsights.v1.idatasetconfig)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DatasetConfig](https://docs.cloud.google.com/nodejs/docs/reference/storageinsights/latest/storageinsights/protos.google.cloud.storageinsights.v1.datasetconfig-class)` | DatasetConfig instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.storageinsights.v1.DatasetConfig;

Decodes a DatasetConfig message from the specified reader or buffer.

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
`[DatasetConfig](https://docs.cloud.google.com/nodejs/docs/reference/storageinsights/latest/storageinsights/protos.google.cloud.storageinsights.v1.datasetconfig-class)` | DatasetConfig  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.storageinsights.v1.DatasetConfig;

Decodes a DatasetConfig message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DatasetConfig](https://docs.cloud.google.com/nodejs/docs/reference/storageinsights/latest/storageinsights/protos.google.cloud.storageinsights.v1.datasetconfig-class)` | DatasetConfig  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.storageinsights.v1.IDatasetConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DatasetConfig message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDatasetConfig](https://docs.cloud.google.com/nodejs/docs/reference/storageinsights/latest/storageinsights/protos.google.cloud.storageinsights.v1.idatasetconfig)`   
DatasetConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.storageinsights.v1.IDatasetConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DatasetConfig message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDatasetConfig](https://docs.cloud.google.com/nodejs/docs/reference/storageinsights/latest/storageinsights/protos.google.cloud.storageinsights.v1.idatasetconfig)`   
DatasetConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.storageinsights.v1.DatasetConfig;

Creates a DatasetConfig message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DatasetConfig](https://docs.cloud.google.com/nodejs/docs/reference/storageinsights/latest/storageinsights/protos.google.cloud.storageinsights.v1.datasetconfig-class)` | DatasetConfig  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DatasetConfig

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

Converts this DatasetConfig to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.storageinsights.v1.DatasetConfig, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DatasetConfig message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DatasetConfig](https://docs.cloud.google.com/nodejs/docs/reference/storageinsights/latest/storageinsights/protos.google.cloud.storageinsights.v1.datasetconfig-class)`   
DatasetConfig  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DatasetConfig message.

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
