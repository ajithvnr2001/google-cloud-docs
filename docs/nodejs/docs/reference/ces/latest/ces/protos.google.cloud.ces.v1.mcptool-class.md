---
url: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.mcptool-class
title: Class protos.google.cloud.ces.v1.McpTool (0.9.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:06:34.914658+00:00
---

# Class protos.google.cloud.ces.v1.McpTool (0.9.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.mcptool-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.ces.v1.McpTool (0.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0 

Represents a McpTool.

## Implements

[protos.google.cloud.ces.v1.IMcpTool](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.imcptool)

## Package

[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.ces.v1.IMcpTool);

Constructs a new McpTool.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IMcpTool](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.imcptool)`   
Properties to set  
  
## Properties 

### apiAuthentication
    
    
    public apiAuthentication?: (google.cloud.ces.v1.IApiAuthentication|null);

McpTool apiAuthentication.

### customHeaders
    
    
    public customHeaders: { [k: string]: string };

McpTool customHeaders.

### description
    
    
    public description: string;

McpTool description.

### inputSchema
    
    
    public inputSchema?: (google.cloud.ces.v1.ISchema|null);

McpTool inputSchema.

### name
    
    
    public name: string;

McpTool name.

### nameOverride
    
    
    public nameOverride: string;

McpTool nameOverride.

### outputSchema
    
    
    public outputSchema?: (google.cloud.ces.v1.ISchema|null);

McpTool outputSchema.

### serverAddress
    
    
    public serverAddress: string;

McpTool serverAddress.

### serviceDirectoryConfig
    
    
    public serviceDirectoryConfig?: (google.cloud.ces.v1.IServiceDirectoryConfig|null);

McpTool serviceDirectoryConfig.

### state
    
    
    public state: (google.cloud.ces.v1.McpTool.State|keyof typeof google.cloud.ces.v1.McpTool.State);

McpTool state.

### tlsConfig
    
    
    public tlsConfig?: (google.cloud.ces.v1.ITlsConfig|null);

McpTool tlsConfig.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.ces.v1.IMcpTool): google.cloud.ces.v1.McpTool;

Creates a new McpTool instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IMcpTool](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.imcptool)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[McpTool](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.mcptool-class)` | McpTool instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.ces.v1.McpTool;

Decodes a McpTool message from the specified reader or buffer.

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
`[McpTool](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.mcptool-class)` | McpTool  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.ces.v1.McpTool;

Decodes a McpTool message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[McpTool](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.mcptool-class)` | McpTool  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.ces.v1.IMcpTool, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified McpTool message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IMcpTool](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.imcptool)`   
McpTool message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.ces.v1.IMcpTool, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified McpTool message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IMcpTool](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.imcptool)`   
McpTool message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.ces.v1.McpTool;

Creates a McpTool message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[McpTool](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.mcptool-class)` | McpTool  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for McpTool

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

Converts this McpTool to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.ces.v1.McpTool, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a McpTool message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[McpTool](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.mcptool-class)`   
McpTool  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a McpTool message.

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
