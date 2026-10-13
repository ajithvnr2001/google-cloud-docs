---
url: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.executetoolrequest
title: Class protos.google.cloud.ces.v1.ExecuteToolRequest (0.9.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:06:17.065232+00:00
---

# Class protos.google.cloud.ces.v1.ExecuteToolRequest (0.9.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.executetoolrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.ces.v1.ExecuteToolRequest (0.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0 

Represents an ExecuteToolRequest.

## Implements

[protos.google.cloud.ces.v1.IExecuteToolRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iexecutetoolrequest)

## Package

[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.ces.v1.IExecuteToolRequest);

Constructs a new ExecuteToolRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IExecuteToolRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iexecutetoolrequest)`   
Properties to set  
  
## Properties 

### args
    
    
    public args?: (google.protobuf.IStruct|null);

ExecuteToolRequest args.

### context
    
    
    public context?: (google.protobuf.IStruct|null);

ExecuteToolRequest context.

### mockConfig
    
    
    public mockConfig?: (google.cloud.ces.v1.IMockConfig|null);

ExecuteToolRequest mockConfig.

### parent
    
    
    public parent: string;

ExecuteToolRequest parent.

### tool
    
    
    public tool?: (string|null);

ExecuteToolRequest tool.

### toolExecutionContext
    
    
    public toolExecutionContext?: ("variables"|"context");

ExecuteToolRequest toolExecutionContext.

### toolIdentifier
    
    
    public toolIdentifier?: ("tool"|"toolsetTool");

ExecuteToolRequest toolIdentifier.

### toolsetTool
    
    
    public toolsetTool?: (google.cloud.ces.v1.IToolsetTool|null);

ExecuteToolRequest toolsetTool.

### variables
    
    
    public variables?: (google.protobuf.IStruct|null);

ExecuteToolRequest variables.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.ces.v1.IExecuteToolRequest): google.cloud.ces.v1.ExecuteToolRequest;

Creates a new ExecuteToolRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IExecuteToolRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iexecutetoolrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ExecuteToolRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.executetoolrequest)` | ExecuteToolRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.ces.v1.ExecuteToolRequest;

Decodes an ExecuteToolRequest message from the specified reader or buffer.

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
`[ExecuteToolRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.executetoolrequest)` | ExecuteToolRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.ces.v1.ExecuteToolRequest;

Decodes an ExecuteToolRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ExecuteToolRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.executetoolrequest)` | ExecuteToolRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.ces.v1.IExecuteToolRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ExecuteToolRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IExecuteToolRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iexecutetoolrequest)`   
ExecuteToolRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.ces.v1.IExecuteToolRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ExecuteToolRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IExecuteToolRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iexecutetoolrequest)`   
ExecuteToolRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.ces.v1.ExecuteToolRequest;

Creates an ExecuteToolRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ExecuteToolRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.executetoolrequest)` | ExecuteToolRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ExecuteToolRequest

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

Converts this ExecuteToolRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.ces.v1.ExecuteToolRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an ExecuteToolRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ExecuteToolRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.executetoolrequest)`   
ExecuteToolRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an ExecuteToolRequest message.

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
