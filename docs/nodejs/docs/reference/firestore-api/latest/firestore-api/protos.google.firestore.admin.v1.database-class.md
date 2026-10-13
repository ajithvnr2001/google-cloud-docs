---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.database-class
title: Class protos.google.firestore.admin.v1.Database (0.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:44:21.940716+00:00
---

# Class protos.google.firestore.admin.v1.Database (0.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.database-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.firestore.admin.v1.Database (0.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a Database.

## Implements

[protos.google.firestore.admin.v1.IDatabase](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.idatabase)

## Package

[@google-cloud/firestore-api](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.firestore.admin.v1.IDatabase);

Constructs a new Database.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDatabase](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.idatabase)`   
Properties to set  
  
## Properties 

### appEngineIntegrationMode
    
    
    public appEngineIntegrationMode: (google.firestore.admin.v1.Database.AppEngineIntegrationMode|keyof typeof google.firestore.admin.v1.Database.AppEngineIntegrationMode);

Database appEngineIntegrationMode.

### cmekConfig
    
    
    public cmekConfig?: (google.firestore.admin.v1.Database.ICmekConfig|null);

Database cmekConfig.

### concurrencyMode
    
    
    public concurrencyMode: (google.firestore.admin.v1.Database.ConcurrencyMode|keyof typeof google.firestore.admin.v1.Database.ConcurrencyMode);

Database concurrencyMode.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

Database createTime.

### databaseEdition
    
    
    public databaseEdition: (google.firestore.admin.v1.Database.DatabaseEdition|keyof typeof google.firestore.admin.v1.Database.DatabaseEdition);

Database databaseEdition.

### deleteProtectionState
    
    
    public deleteProtectionState: (google.firestore.admin.v1.Database.DeleteProtectionState|keyof typeof google.firestore.admin.v1.Database.DeleteProtectionState);

Database deleteProtectionState.

### deleteTime
    
    
    public deleteTime?: (google.protobuf.ITimestamp|null);

Database deleteTime.

### earliestVersionTime
    
    
    public earliestVersionTime?: (google.protobuf.ITimestamp|null);

Database earliestVersionTime.

### etag
    
    
    public etag: string;

Database etag.

### firestoreDataAccessMode
    
    
    public firestoreDataAccessMode: (google.firestore.admin.v1.Database.DataAccessMode|keyof typeof google.firestore.admin.v1.Database.DataAccessMode);

Database firestoreDataAccessMode.

### freeTier
    
    
    public freeTier?: (boolean|null);

Database freeTier.

### keyPrefix
    
    
    public keyPrefix: string;

Database keyPrefix.

### locationId
    
    
    public locationId: string;

Database locationId.

### mongodbCompatibleDataAccessMode
    
    
    public mongodbCompatibleDataAccessMode: (google.firestore.admin.v1.Database.DataAccessMode|keyof typeof google.firestore.admin.v1.Database.DataAccessMode);

Database mongodbCompatibleDataAccessMode.

### name
    
    
    public name: string;

Database name.

### pointInTimeRecoveryEnablement
    
    
    public pointInTimeRecoveryEnablement: (google.firestore.admin.v1.Database.PointInTimeRecoveryEnablement|keyof typeof google.firestore.admin.v1.Database.PointInTimeRecoveryEnablement);

Database pointInTimeRecoveryEnablement.

### previousId
    
    
    public previousId: string;

Database previousId.

### realtimeUpdatesMode
    
    
    public realtimeUpdatesMode: (google.firestore.admin.v1.RealtimeUpdatesMode|keyof typeof google.firestore.admin.v1.RealtimeUpdatesMode);

Database realtimeUpdatesMode.

### sourceInfo
    
    
    public sourceInfo?: (google.firestore.admin.v1.Database.ISourceInfo|null);

Database sourceInfo.

### tags
    
    
    public tags: { [k: string]: string };

Database tags.

### type
    
    
    public type: (google.firestore.admin.v1.Database.DatabaseType|keyof typeof google.firestore.admin.v1.Database.DatabaseType);

Database type.

### uid
    
    
    public uid: string;

Database uid.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

Database updateTime.

### versionRetentionPeriod
    
    
    public versionRetentionPeriod?: (google.protobuf.IDuration|null);

Database versionRetentionPeriod.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.firestore.admin.v1.IDatabase): google.firestore.admin.v1.Database;

Creates a new Database instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDatabase](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.idatabase)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Database](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.database-class)` | Database instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.firestore.admin.v1.Database;

Decodes a Database message from the specified reader or buffer.

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
`[Database](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.database-class)` | Database  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.firestore.admin.v1.Database;

Decodes a Database message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Database](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.database-class)` | Database  
  
### encode(message, writer)
    
    
    public static encode(message: google.firestore.admin.v1.IDatabase, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Database message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDatabase](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.idatabase)`   
Database message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.firestore.admin.v1.IDatabase, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Database message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDatabase](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.idatabase)`   
Database message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.firestore.admin.v1.Database;

Creates a Database message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Database](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.database-class)` | Database  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Database

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

Converts this Database to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.firestore.admin.v1.Database, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Database message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Database](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.database-class)`   
Database  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Database message.

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
