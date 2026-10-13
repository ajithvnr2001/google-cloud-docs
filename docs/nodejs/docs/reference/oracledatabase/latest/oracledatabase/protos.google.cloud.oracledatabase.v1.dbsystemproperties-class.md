---
url: https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.dbsystemproperties-class
title: Class protos.google.cloud.oracledatabase.v1.DbSystemProperties (0.11.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:36:24.160577+00:00
---

# Class protos.google.cloud.oracledatabase.v1.DbSystemProperties (0.11.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.dbsystemproperties-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.oracledatabase.v1.DbSystemProperties (0.11.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.1 (latest)  0.8.0  0.2.0  0.1.0 

Represents a DbSystemProperties.

## Implements

[protos.google.cloud.oracledatabase.v1.IDbSystemProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.idbsystemproperties)

## Package

[@google-cloud/oracledatabase](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.oracledatabase.v1.IDbSystemProperties);

Constructs a new DbSystemProperties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDbSystemProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.idbsystemproperties)`   
Properties to set  
  
## Properties 

### computeCount
    
    
    public computeCount: number;

DbSystemProperties computeCount.

### computeModel
    
    
    public computeModel: (google.cloud.oracledatabase.v1.DbSystemProperties.ComputeModel|keyof typeof google.cloud.oracledatabase.v1.DbSystemProperties.ComputeModel);

DbSystemProperties computeModel.

### databaseEdition
    
    
    public databaseEdition: (google.cloud.oracledatabase.v1.DbSystemProperties.DbSystemDatabaseEdition|keyof typeof google.cloud.oracledatabase.v1.DbSystemProperties.DbSystemDatabaseEdition);

DbSystemProperties databaseEdition.

### dataCollectionOptions
    
    
    public dataCollectionOptions?: (google.cloud.oracledatabase.v1.IDataCollectionOptionsDbSystem|null);

DbSystemProperties dataCollectionOptions.

### dataStorageSizeGb
    
    
    public dataStorageSizeGb: number;

DbSystemProperties dataStorageSizeGb.

### dbHome
    
    
    public dbHome?: (google.cloud.oracledatabase.v1.IDbHome|null);

DbSystemProperties dbHome.

### dbSystemOptions
    
    
    public dbSystemOptions?: (google.cloud.oracledatabase.v1.IDbSystemOptions|null);

DbSystemProperties dbSystemOptions.

### domain
    
    
    public domain: string;

DbSystemProperties domain.

### hostname
    
    
    public hostname: string;

DbSystemProperties hostname.

### hostnamePrefix
    
    
    public hostnamePrefix: string;

DbSystemProperties hostnamePrefix.

### initialDataStorageSizeGb
    
    
    public initialDataStorageSizeGb: number;

DbSystemProperties initialDataStorageSizeGb.

### licenseModel
    
    
    public licenseModel: (google.cloud.oracledatabase.v1.DbSystemProperties.LicenseModel|keyof typeof google.cloud.oracledatabase.v1.DbSystemProperties.LicenseModel);

DbSystemProperties licenseModel.

### lifecycleState
    
    
    public lifecycleState: (google.cloud.oracledatabase.v1.DbSystemProperties.DbSystemLifecycleState|keyof typeof google.cloud.oracledatabase.v1.DbSystemProperties.DbSystemLifecycleState);

DbSystemProperties lifecycleState.

### memorySizeGb
    
    
    public memorySizeGb: number;

DbSystemProperties memorySizeGb.

### nodeCount
    
    
    public nodeCount: number;

DbSystemProperties nodeCount.

### ocid
    
    
    public ocid: string;

DbSystemProperties ocid.

### privateIp
    
    
    public privateIp: string;

DbSystemProperties privateIp.

### recoStorageSizeGb
    
    
    public recoStorageSizeGb: number;

DbSystemProperties recoStorageSizeGb.

### shape
    
    
    public shape: string;

DbSystemProperties shape.

### sshPublicKeys
    
    
    public sshPublicKeys: string[];

DbSystemProperties sshPublicKeys.

### timeZone
    
    
    public timeZone?: (google.type.ITimeZone|null);

DbSystemProperties timeZone.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.oracledatabase.v1.IDbSystemProperties): google.cloud.oracledatabase.v1.DbSystemProperties;

Creates a new DbSystemProperties instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDbSystemProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.idbsystemproperties)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DbSystemProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.dbsystemproperties-class)` | DbSystemProperties instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.oracledatabase.v1.DbSystemProperties;

Decodes a DbSystemProperties message from the specified reader or buffer.

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
`[DbSystemProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.dbsystemproperties-class)` | DbSystemProperties  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.oracledatabase.v1.DbSystemProperties;

Decodes a DbSystemProperties message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DbSystemProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.dbsystemproperties-class)` | DbSystemProperties  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.oracledatabase.v1.IDbSystemProperties, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DbSystemProperties message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDbSystemProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.idbsystemproperties)`   
DbSystemProperties message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.oracledatabase.v1.IDbSystemProperties, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DbSystemProperties message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDbSystemProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.idbsystemproperties)`   
DbSystemProperties message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.oracledatabase.v1.DbSystemProperties;

Creates a DbSystemProperties message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DbSystemProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.dbsystemproperties-class)` | DbSystemProperties  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DbSystemProperties

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

Converts this DbSystemProperties to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.oracledatabase.v1.DbSystemProperties, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DbSystemProperties message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DbSystemProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.dbsystemproperties-class)`   
DbSystemProperties  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DbSystemProperties message.

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
