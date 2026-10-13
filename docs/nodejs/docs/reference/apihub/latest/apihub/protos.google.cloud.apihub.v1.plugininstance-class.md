---
url: https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.plugininstance-class
title: Class protos.google.cloud.apihub.v1.PluginInstance (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:58:26.006534+00:00
---

# Class protos.google.cloud.apihub.v1.PluginInstance (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.plugininstance-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.apihub.v1.PluginInstance (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a PluginInstance.

## Implements

[protos.google.cloud.apihub.v1.IPluginInstance](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iplugininstance)

## Package

[@google-cloud/apihub](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.apihub.v1.IPluginInstance);

Constructs a new PluginInstance.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPluginInstance](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iplugininstance)`   
Properties to set  
  
## Properties 

### actions
    
    
    public actions: google.cloud.apihub.v1.IPluginInstanceAction[];

PluginInstance actions.

### additionalConfig
    
    
    public additionalConfig: { [k: string]: google.cloud.apihub.v1.IConfigVariable };

PluginInstance additionalConfig.

### authConfig
    
    
    public authConfig?: (google.cloud.apihub.v1.IAuthConfig|null);

PluginInstance authConfig.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

PluginInstance createTime.

### displayName
    
    
    public displayName: string;

PluginInstance displayName.

### errorMessage
    
    
    public errorMessage: string;

PluginInstance errorMessage.

### name
    
    
    public name: string;

PluginInstance name.

### sourceProjectId
    
    
    public sourceProjectId: string;

PluginInstance sourceProjectId.

### state
    
    
    public state: (google.cloud.apihub.v1.PluginInstance.State|keyof typeof google.cloud.apihub.v1.PluginInstance.State);

PluginInstance state.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

PluginInstance updateTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.apihub.v1.IPluginInstance): google.cloud.apihub.v1.PluginInstance;

Creates a new PluginInstance instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPluginInstance](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iplugininstance)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[PluginInstance](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.plugininstance-class)` | PluginInstance instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.apihub.v1.PluginInstance;

Decodes a PluginInstance message from the specified reader or buffer.

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
`[PluginInstance](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.plugininstance-class)` | PluginInstance  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.apihub.v1.PluginInstance;

Decodes a PluginInstance message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[PluginInstance](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.plugininstance-class)` | PluginInstance  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.apihub.v1.IPluginInstance, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified PluginInstance message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPluginInstance](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iplugininstance)`   
PluginInstance message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.apihub.v1.IPluginInstance, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified PluginInstance message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPluginInstance](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iplugininstance)`   
PluginInstance message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.apihub.v1.PluginInstance;

Creates a PluginInstance message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[PluginInstance](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.plugininstance-class)` | PluginInstance  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for PluginInstance

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

Converts this PluginInstance to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.apihub.v1.PluginInstance, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a PluginInstance message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[PluginInstance](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.plugininstance-class)`   
PluginInstance  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a PluginInstance message.

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
