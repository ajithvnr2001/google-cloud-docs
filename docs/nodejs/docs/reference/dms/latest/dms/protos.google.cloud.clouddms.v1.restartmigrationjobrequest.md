---
url: https://docs.cloud.google.com/nodejs/docs/reference/dms/latest/dms/protos.google.cloud.clouddms.v1.restartmigrationjobrequest
title: Class protos.google.cloud.clouddms.v1.RestartMigrationJobRequest (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:18:08.906351+00:00
---

# Class protos.google.cloud.clouddms.v1.RestartMigrationJobRequest (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dms/latest/dms/protos.google.cloud.clouddms.v1.restartmigrationjobrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.clouddms.v1.RestartMigrationJobRequest (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  2.2.2  2.1.2  1.1.0  1.0.5 

Represents a RestartMigrationJobRequest.

## Implements

[protos.google.cloud.clouddms.v1.IRestartMigrationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dms/latest/dms/protos.google.cloud.clouddms.v1.irestartmigrationjobrequest)

## Package

[@google-cloud/dms](https://docs.cloud.google.com/nodejs/docs/reference/dms/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.clouddms.v1.IRestartMigrationJobRequest);

Constructs a new RestartMigrationJobRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IRestartMigrationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dms/latest/dms/protos.google.cloud.clouddms.v1.irestartmigrationjobrequest)`   
Properties to set  
  
## Properties 

### name
    
    
    public name: string;

RestartMigrationJobRequest name.

### skipValidation
    
    
    public skipValidation: boolean;

RestartMigrationJobRequest skipValidation.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.clouddms.v1.IRestartMigrationJobRequest): google.cloud.clouddms.v1.RestartMigrationJobRequest;

Creates a new RestartMigrationJobRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IRestartMigrationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dms/latest/dms/protos.google.cloud.clouddms.v1.irestartmigrationjobrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[RestartMigrationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dms/latest/dms/protos.google.cloud.clouddms.v1.restartmigrationjobrequest)` | RestartMigrationJobRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.clouddms.v1.RestartMigrationJobRequest;

Decodes a RestartMigrationJobRequest message from the specified reader or buffer.

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
`[RestartMigrationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dms/latest/dms/protos.google.cloud.clouddms.v1.restartmigrationjobrequest)` | RestartMigrationJobRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.clouddms.v1.RestartMigrationJobRequest;

Decodes a RestartMigrationJobRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[RestartMigrationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dms/latest/dms/protos.google.cloud.clouddms.v1.restartmigrationjobrequest)` | RestartMigrationJobRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.clouddms.v1.IRestartMigrationJobRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified RestartMigrationJobRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IRestartMigrationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dms/latest/dms/protos.google.cloud.clouddms.v1.irestartmigrationjobrequest)`   
RestartMigrationJobRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.clouddms.v1.IRestartMigrationJobRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified RestartMigrationJobRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IRestartMigrationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dms/latest/dms/protos.google.cloud.clouddms.v1.irestartmigrationjobrequest)`   
RestartMigrationJobRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.clouddms.v1.RestartMigrationJobRequest;

Creates a RestartMigrationJobRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[RestartMigrationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dms/latest/dms/protos.google.cloud.clouddms.v1.restartmigrationjobrequest)` | RestartMigrationJobRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for RestartMigrationJobRequest

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

Converts this RestartMigrationJobRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.clouddms.v1.RestartMigrationJobRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a RestartMigrationJobRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[RestartMigrationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dms/latest/dms/protos.google.cloud.clouddms.v1.restartmigrationjobrequest)`   
RestartMigrationJobRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a RestartMigrationJobRequest message.

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
