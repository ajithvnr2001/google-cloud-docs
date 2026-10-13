---
url: https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.autonomousdatabase
title: Class protos.google.cloud.oracledatabase.v1.AutonomousDatabase (0.11.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:56:52.367574+00:00
---

# Class protos.google.cloud.oracledatabase.v1.AutonomousDatabase (0.11.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.autonomousdatabase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.oracledatabase.v1.AutonomousDatabase (0.11.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.1 (latest)  0.8.0  0.2.0  0.1.0 

Represents an AutonomousDatabase.

## Implements

[protos.google.cloud.oracledatabase.v1.IAutonomousDatabase](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.iautonomousdatabase)

## Package

[@google-cloud/oracledatabase](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.oracledatabase.v1.IAutonomousDatabase);

Constructs a new AutonomousDatabase.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAutonomousDatabase](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.iautonomousdatabase)`   
Properties to set  
  
## Properties 

### adminPassword
    
    
    public adminPassword: string;

AutonomousDatabase adminPassword.

### adminPasswordSecretVersion
    
    
    public adminPasswordSecretVersion: string;

AutonomousDatabase adminPasswordSecretVersion.

### cidr
    
    
    public cidr: string;

AutonomousDatabase cidr.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

AutonomousDatabase createTime.

### database
    
    
    public database: string;

AutonomousDatabase database.

### disasterRecoverySupportedLocations
    
    
    public disasterRecoverySupportedLocations: string[];

AutonomousDatabase disasterRecoverySupportedLocations.

### displayName
    
    
    public displayName: string;

AutonomousDatabase displayName.

### entitlementId
    
    
    public entitlementId: string;

AutonomousDatabase entitlementId.

### labels
    
    
    public labels: { [k: string]: string };

AutonomousDatabase labels.

### name
    
    
    public name: string;

AutonomousDatabase name.

### network
    
    
    public network: string;

AutonomousDatabase network.

### odbNetwork
    
    
    public odbNetwork: string;

AutonomousDatabase odbNetwork.

### odbSubnet
    
    
    public odbSubnet: string;

AutonomousDatabase odbSubnet.

### peerAutonomousDatabases
    
    
    public peerAutonomousDatabases: string[];

AutonomousDatabase peerAutonomousDatabases.

### properties
    
    
    public properties?: (google.cloud.oracledatabase.v1.IAutonomousDatabaseProperties|null);

AutonomousDatabase properties.

### sourceConfig
    
    
    public sourceConfig?: (google.cloud.oracledatabase.v1.ISourceConfig|null);

AutonomousDatabase sourceConfig.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.oracledatabase.v1.IAutonomousDatabase): google.cloud.oracledatabase.v1.AutonomousDatabase;

Creates a new AutonomousDatabase instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAutonomousDatabase](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.iautonomousdatabase)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AutonomousDatabase](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.autonomousdatabase)` | AutonomousDatabase instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.oracledatabase.v1.AutonomousDatabase;

Decodes an AutonomousDatabase message from the specified reader or buffer.

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
`[AutonomousDatabase](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.autonomousdatabase)` | AutonomousDatabase  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.oracledatabase.v1.AutonomousDatabase;

Decodes an AutonomousDatabase message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AutonomousDatabase](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.autonomousdatabase)` | AutonomousDatabase  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.oracledatabase.v1.IAutonomousDatabase, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AutonomousDatabase message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAutonomousDatabase](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.iautonomousdatabase)`   
AutonomousDatabase message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.oracledatabase.v1.IAutonomousDatabase, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AutonomousDatabase message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAutonomousDatabase](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.iautonomousdatabase)`   
AutonomousDatabase message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.oracledatabase.v1.AutonomousDatabase;

Creates an AutonomousDatabase message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AutonomousDatabase](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.autonomousdatabase)` | AutonomousDatabase  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AutonomousDatabase

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

Converts this AutonomousDatabase to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.oracledatabase.v1.AutonomousDatabase, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AutonomousDatabase message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AutonomousDatabase](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.autonomousdatabase)`   
AutonomousDatabase  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AutonomousDatabase message.

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
