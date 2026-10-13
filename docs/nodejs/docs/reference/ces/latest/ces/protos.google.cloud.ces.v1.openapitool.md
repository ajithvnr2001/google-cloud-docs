---
url: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.openapitool
title: Class protos.google.cloud.ces.v1.OpenApiTool (0.9.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:06:40.506408+00:00
---

# Class protos.google.cloud.ces.v1.OpenApiTool (0.9.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.openapitool

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.ces.v1.OpenApiTool (0.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0 

Represents an OpenApiTool.

## Implements

[protos.google.cloud.ces.v1.IOpenApiTool](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iopenapitool)

## Package

[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.ces.v1.IOpenApiTool);

Constructs a new OpenApiTool.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IOpenApiTool](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iopenapitool)`   
Properties to set  
  
## Properties 

### apiAuthentication
    
    
    public apiAuthentication?: (google.cloud.ces.v1.IApiAuthentication|null);

OpenApiTool apiAuthentication.

### description
    
    
    public description: string;

OpenApiTool description.

### ignoreUnknownFields
    
    
    public ignoreUnknownFields: boolean;

OpenApiTool ignoreUnknownFields.

### name
    
    
    public name: string;

OpenApiTool name.

### openApiSchema
    
    
    public openApiSchema: string;

OpenApiTool openApiSchema.

### serviceDirectoryConfig
    
    
    public serviceDirectoryConfig?: (google.cloud.ces.v1.IServiceDirectoryConfig|null);

OpenApiTool serviceDirectoryConfig.

### tlsConfig
    
    
    public tlsConfig?: (google.cloud.ces.v1.ITlsConfig|null);

OpenApiTool tlsConfig.

### url
    
    
    public url: string;

OpenApiTool url.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.ces.v1.IOpenApiTool): google.cloud.ces.v1.OpenApiTool;

Creates a new OpenApiTool instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IOpenApiTool](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iopenapitool)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[OpenApiTool](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.openapitool)` | OpenApiTool instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.ces.v1.OpenApiTool;

Decodes an OpenApiTool message from the specified reader or buffer.

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
`[OpenApiTool](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.openapitool)` | OpenApiTool  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.ces.v1.OpenApiTool;

Decodes an OpenApiTool message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[OpenApiTool](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.openapitool)` | OpenApiTool  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.ces.v1.IOpenApiTool, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified OpenApiTool message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IOpenApiTool](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iopenapitool)`   
OpenApiTool message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.ces.v1.IOpenApiTool, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified OpenApiTool message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IOpenApiTool](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iopenapitool)`   
OpenApiTool message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.ces.v1.OpenApiTool;

Creates an OpenApiTool message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[OpenApiTool](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.openapitool)` | OpenApiTool  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for OpenApiTool

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

Converts this OpenApiTool to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.ces.v1.OpenApiTool, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an OpenApiTool message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[OpenApiTool](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.openapitool)`   
OpenApiTool  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an OpenApiTool message.

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
