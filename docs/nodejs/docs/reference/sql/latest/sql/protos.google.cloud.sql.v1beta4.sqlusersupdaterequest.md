---
url: https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1beta4.sqlusersupdaterequest
title: Class protos.google.cloud.sql.v1beta4.SqlUsersUpdateRequest (0.29.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:18:51.746549+00:00
---

# Class protos.google.cloud.sql.v1beta4.SqlUsersUpdateRequest (0.29.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1beta4.sqlusersupdaterequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.sql.v1beta4.SqlUsersUpdateRequest (0.29.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.29.1 (latest)  0.29.0  0.25.0  0.23.0  0.19.1  0.16.0  0.15.0  0.14.0  0.13.0  0.11.0  0.8.0  0.7.0  0.5.0  0.4.0 

Represents a SqlUsersUpdateRequest.

## Implements

[protos.google.cloud.sql.v1beta4.ISqlUsersUpdateRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1beta4.isqlusersupdaterequest)

## Package

[@google-cloud/sql](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.sql.v1beta4.ISqlUsersUpdateRequest);

Constructs a new SqlUsersUpdateRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISqlUsersUpdateRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1beta4.isqlusersupdaterequest)`   
Properties to set  
  
## Properties 

### body
    
    
    public body?: (google.cloud.sql.v1beta4.IUser|null);

SqlUsersUpdateRequest body.

### databaseRoles
    
    
    public databaseRoles: string[];

SqlUsersUpdateRequest databaseRoles.

### host
    
    
    public host: string;

SqlUsersUpdateRequest host.

### instance
    
    
    public instance: string;

SqlUsersUpdateRequest instance.

### location
    
    
    public location: string;

SqlUsersUpdateRequest location.

### name
    
    
    public name: string;

SqlUsersUpdateRequest name.

### project
    
    
    public project: string;

SqlUsersUpdateRequest project.

### revokeExistingRoles
    
    
    public revokeExistingRoles?: (boolean|null);

SqlUsersUpdateRequest revokeExistingRoles.

### revokeExistingServerRoles
    
    
    public revokeExistingServerRoles?: (boolean|null);

SqlUsersUpdateRequest revokeExistingServerRoles.

### serverRoles
    
    
    public serverRoles: string[];

SqlUsersUpdateRequest serverRoles.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.sql.v1beta4.ISqlUsersUpdateRequest): google.cloud.sql.v1beta4.SqlUsersUpdateRequest;

Creates a new SqlUsersUpdateRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISqlUsersUpdateRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1beta4.isqlusersupdaterequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[SqlUsersUpdateRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1beta4.sqlusersupdaterequest)` | SqlUsersUpdateRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.sql.v1beta4.SqlUsersUpdateRequest;

Decodes a SqlUsersUpdateRequest message from the specified reader or buffer.

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
`[SqlUsersUpdateRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1beta4.sqlusersupdaterequest)` | SqlUsersUpdateRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.sql.v1beta4.SqlUsersUpdateRequest;

Decodes a SqlUsersUpdateRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[SqlUsersUpdateRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1beta4.sqlusersupdaterequest)` | SqlUsersUpdateRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.sql.v1beta4.ISqlUsersUpdateRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SqlUsersUpdateRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISqlUsersUpdateRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1beta4.isqlusersupdaterequest)`   
SqlUsersUpdateRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.sql.v1beta4.ISqlUsersUpdateRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SqlUsersUpdateRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISqlUsersUpdateRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1beta4.isqlusersupdaterequest)`   
SqlUsersUpdateRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.sql.v1beta4.SqlUsersUpdateRequest;

Creates a SqlUsersUpdateRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[SqlUsersUpdateRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1beta4.sqlusersupdaterequest)` | SqlUsersUpdateRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for SqlUsersUpdateRequest

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

Converts this SqlUsersUpdateRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.sql.v1beta4.SqlUsersUpdateRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a SqlUsersUpdateRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[SqlUsersUpdateRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1beta4.sqlusersupdaterequest)`   
SqlUsersUpdateRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a SqlUsersUpdateRequest message.

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
