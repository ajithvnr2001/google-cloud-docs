---
url: https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.connector
title: Class protos.google.cloud.connectors.v1.Connector (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:26:21.307563+00:00
---

# Class protos.google.cloud.connectors.v1.Connector (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.connector

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.connectors.v1.Connector (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a Connector.

## Implements

[protos.google.cloud.connectors.v1.IConnector](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.iconnector)

## Package

[@google-cloud/connectors](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.connectors.v1.IConnector);

Constructs a new Connector.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IConnector](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.iconnector)`   
Properties to set  
  
## Properties 

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

Connector createTime.

### description
    
    
    public description: string;

Connector description.

### displayName
    
    
    public displayName: string;

Connector displayName.

### documentationUri
    
    
    public documentationUri: string;

Connector documentationUri.

### externalUri
    
    
    public externalUri: string;

Connector externalUri.

### labels
    
    
    public labels: { [k: string]: string };

Connector labels.

### launchStage
    
    
    public launchStage: (google.cloud.connectors.v1.LaunchStage|keyof typeof google.cloud.connectors.v1.LaunchStage);

Connector launchStage.

### name
    
    
    public name: string;

Connector name.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

Connector updateTime.

### webAssetsLocation
    
    
    public webAssetsLocation: string;

Connector webAssetsLocation.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.connectors.v1.IConnector): google.cloud.connectors.v1.Connector;

Creates a new Connector instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IConnector](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.iconnector)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Connector](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.connector)` | Connector instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.connectors.v1.Connector;

Decodes a Connector message from the specified reader or buffer.

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
`[Connector](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.connector)` | Connector  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.connectors.v1.Connector;

Decodes a Connector message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Connector](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.connector)` | Connector  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.connectors.v1.IConnector, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Connector message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IConnector](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.iconnector)`   
Connector message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.connectors.v1.IConnector, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Connector message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IConnector](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.iconnector)`   
Connector message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.connectors.v1.Connector;

Creates a Connector message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Connector](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.connector)` | Connector  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Connector

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

Converts this Connector to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.connectors.v1.Connector, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Connector message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Connector](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.connector)`   
Connector  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Connector message.

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
