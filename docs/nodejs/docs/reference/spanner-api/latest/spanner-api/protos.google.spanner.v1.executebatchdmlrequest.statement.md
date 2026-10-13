---
url: https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.v1.executebatchdmlrequest.statement
title: Class protos.google.spanner.v1.ExecuteBatchDmlRequest.Statement (0.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:24:14.111684+00:00
---

# Class protos.google.spanner.v1.ExecuteBatchDmlRequest.Statement (0.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.v1.executebatchdmlrequest.statement

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.spanner.v1.ExecuteBatchDmlRequest.Statement (0.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a Statement.

## Implements

[protos.google.spanner.v1.ExecuteBatchDmlRequest.IStatement](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.v1.executebatchdmlrequest.istatement)

## Package

[@google-cloud/spanner-api](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.spanner.v1.ExecuteBatchDmlRequest.IStatement);

Constructs a new Statement.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IStatement](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.v1.executebatchdmlrequest.istatement)`   
Properties to set  
  
## Properties 

### params
    
    
    public params?: (google.protobuf.IStruct|null);

Statement params.

### paramTypes
    
    
    public paramTypes: { [k: string]: google.spanner.v1.IType };

Statement paramTypes.

### sql
    
    
    public sql: string;

Statement sql.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.spanner.v1.ExecuteBatchDmlRequest.IStatement): google.spanner.v1.ExecuteBatchDmlRequest.Statement;

Creates a new Statement instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IStatement](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.v1.executebatchdmlrequest.istatement)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Statement](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.v1.executebatchdmlrequest.statement)` | Statement instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.spanner.v1.ExecuteBatchDmlRequest.Statement;

Decodes a Statement message from the specified reader or buffer.

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
`[Statement](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.v1.executebatchdmlrequest.statement)` | Statement  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.spanner.v1.ExecuteBatchDmlRequest.Statement;

Decodes a Statement message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Statement](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.v1.executebatchdmlrequest.statement)` | Statement  
  
### encode(message, writer)
    
    
    public static encode(message: google.spanner.v1.ExecuteBatchDmlRequest.IStatement, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Statement message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IStatement](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.v1.executebatchdmlrequest.istatement)`   
Statement message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.spanner.v1.ExecuteBatchDmlRequest.IStatement, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Statement message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IStatement](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.v1.executebatchdmlrequest.istatement)`   
Statement message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.spanner.v1.ExecuteBatchDmlRequest.Statement;

Creates a Statement message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Statement](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.v1.executebatchdmlrequest.statement)` | Statement  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Statement

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

Converts this Statement to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.spanner.v1.ExecuteBatchDmlRequest.Statement, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Statement message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Statement](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.v1.executebatchdmlrequest.statement)`   
Statement  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Statement message.

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
