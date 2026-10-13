---
url: https://docs.cloud.google.com/nodejs/docs/reference/dms/latest/dms/protos.google.cloud.clouddms.v1.cloudsqlsettings-class
title: Class protos.google.cloud.clouddms.v1.CloudSqlSettings (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:08:06.413356+00:00
---

# Class protos.google.cloud.clouddms.v1.CloudSqlSettings (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dms/latest/dms/protos.google.cloud.clouddms.v1.cloudsqlsettings-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.clouddms.v1.CloudSqlSettings (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  2.2.2  2.1.2  1.1.0  1.0.5 

Represents a CloudSqlSettings.

## Implements

[protos.google.cloud.clouddms.v1.ICloudSqlSettings](https://docs.cloud.google.com/nodejs/docs/reference/dms/latest/dms/protos.google.cloud.clouddms.v1.icloudsqlsettings)

## Package

[@google-cloud/dms](https://docs.cloud.google.com/nodejs/docs/reference/dms/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.clouddms.v1.ICloudSqlSettings);

Constructs a new CloudSqlSettings.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICloudSqlSettings](https://docs.cloud.google.com/nodejs/docs/reference/dms/latest/dms/protos.google.cloud.clouddms.v1.icloudsqlsettings)`   
Properties to set  
  
## Properties 

### activationPolicy
    
    
    public activationPolicy: (google.cloud.clouddms.v1.CloudSqlSettings.SqlActivationPolicy|keyof typeof google.cloud.clouddms.v1.CloudSqlSettings.SqlActivationPolicy);

CloudSqlSettings activationPolicy.

### autoStorageIncrease
    
    
    public autoStorageIncrease?: (google.protobuf.IBoolValue|null);

CloudSqlSettings autoStorageIncrease.

### availabilityType
    
    
    public availabilityType: (google.cloud.clouddms.v1.CloudSqlSettings.SqlAvailabilityType|keyof typeof google.cloud.clouddms.v1.CloudSqlSettings.SqlAvailabilityType);

CloudSqlSettings availabilityType.

### cmekKeyName
    
    
    public cmekKeyName: string;

CloudSqlSettings cmekKeyName.

### collation
    
    
    public collation: string;

CloudSqlSettings collation.

### databaseFlags
    
    
    public databaseFlags: { [k: string]: string };

CloudSqlSettings databaseFlags.

### databaseVersion
    
    
    public databaseVersion: (google.cloud.clouddms.v1.CloudSqlSettings.SqlDatabaseVersion|keyof typeof google.cloud.clouddms.v1.CloudSqlSettings.SqlDatabaseVersion);

CloudSqlSettings databaseVersion.

### dataDiskSizeGb
    
    
    public dataDiskSizeGb?: (google.protobuf.IInt64Value|null);

CloudSqlSettings dataDiskSizeGb.

### dataDiskType
    
    
    public dataDiskType: (google.cloud.clouddms.v1.CloudSqlSettings.SqlDataDiskType|keyof typeof google.cloud.clouddms.v1.CloudSqlSettings.SqlDataDiskType);

CloudSqlSettings dataDiskType.

### edition
    
    
    public edition: (google.cloud.clouddms.v1.CloudSqlSettings.Edition|keyof typeof google.cloud.clouddms.v1.CloudSqlSettings.Edition);

CloudSqlSettings edition.

### ipConfig
    
    
    public ipConfig?: (google.cloud.clouddms.v1.ISqlIpConfig|null);

CloudSqlSettings ipConfig.

### rootPassword
    
    
    public rootPassword: string;

CloudSqlSettings rootPassword.

### rootPasswordSet
    
    
    public rootPasswordSet: boolean;

CloudSqlSettings rootPasswordSet.

### secondaryZone
    
    
    public secondaryZone: string;

CloudSqlSettings secondaryZone.

### sourceId
    
    
    public sourceId: string;

CloudSqlSettings sourceId.

### storageAutoResizeLimit
    
    
    public storageAutoResizeLimit?: (google.protobuf.IInt64Value|null);

CloudSqlSettings storageAutoResizeLimit.

### tier
    
    
    public tier: string;

CloudSqlSettings tier.

### userLabels
    
    
    public userLabels: { [k: string]: string };

CloudSqlSettings userLabels.

### zone
    
    
    public zone: string;

CloudSqlSettings zone.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.clouddms.v1.ICloudSqlSettings): google.cloud.clouddms.v1.CloudSqlSettings;

Creates a new CloudSqlSettings instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICloudSqlSettings](https://docs.cloud.google.com/nodejs/docs/reference/dms/latest/dms/protos.google.cloud.clouddms.v1.icloudsqlsettings)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[CloudSqlSettings](https://docs.cloud.google.com/nodejs/docs/reference/dms/latest/dms/protos.google.cloud.clouddms.v1.cloudsqlsettings-class)` | CloudSqlSettings instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.clouddms.v1.CloudSqlSettings;

Decodes a CloudSqlSettings message from the specified reader or buffer.

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
`[CloudSqlSettings](https://docs.cloud.google.com/nodejs/docs/reference/dms/latest/dms/protos.google.cloud.clouddms.v1.cloudsqlsettings-class)` | CloudSqlSettings  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.clouddms.v1.CloudSqlSettings;

Decodes a CloudSqlSettings message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[CloudSqlSettings](https://docs.cloud.google.com/nodejs/docs/reference/dms/latest/dms/protos.google.cloud.clouddms.v1.cloudsqlsettings-class)` | CloudSqlSettings  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.clouddms.v1.ICloudSqlSettings, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CloudSqlSettings message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICloudSqlSettings](https://docs.cloud.google.com/nodejs/docs/reference/dms/latest/dms/protos.google.cloud.clouddms.v1.icloudsqlsettings)`   
CloudSqlSettings message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.clouddms.v1.ICloudSqlSettings, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CloudSqlSettings message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICloudSqlSettings](https://docs.cloud.google.com/nodejs/docs/reference/dms/latest/dms/protos.google.cloud.clouddms.v1.icloudsqlsettings)`   
CloudSqlSettings message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.clouddms.v1.CloudSqlSettings;

Creates a CloudSqlSettings message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[CloudSqlSettings](https://docs.cloud.google.com/nodejs/docs/reference/dms/latest/dms/protos.google.cloud.clouddms.v1.cloudsqlsettings-class)` | CloudSqlSettings  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for CloudSqlSettings

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

Converts this CloudSqlSettings to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.clouddms.v1.CloudSqlSettings, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a CloudSqlSettings message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[CloudSqlSettings](https://docs.cloud.google.com/nodejs/docs/reference/dms/latest/dms/protos.google.cloud.clouddms.v1.cloudsqlsettings-class)`   
CloudSqlSettings  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a CloudSqlSettings message.

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
