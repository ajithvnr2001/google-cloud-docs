---
url: https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.plugin-class
title: Class protos.google.cloud.apihub.v1.Plugin (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:06:13.389338+00:00
---

# Class protos.google.cloud.apihub.v1.Plugin (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.plugin-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.apihub.v1.Plugin (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a Plugin.

## Implements

[protos.google.cloud.apihub.v1.IPlugin](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iplugin)

## Package

[@google-cloud/apihub](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.apihub.v1.IPlugin);

Constructs a new Plugin.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPlugin](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iplugin)`   
Properties to set  
  
## Properties 

### actionsConfig
    
    
    public actionsConfig: google.cloud.apihub.v1.IPluginActionConfig[];

Plugin actionsConfig.

### configTemplate
    
    
    public configTemplate?: (google.cloud.apihub.v1.Plugin.IConfigTemplate|null);

Plugin configTemplate.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

Plugin createTime.

### description
    
    
    public description: string;

Plugin description.

### displayName
    
    
    public displayName: string;

Plugin displayName.

### documentation
    
    
    public documentation?: (google.cloud.apihub.v1.IDocumentation|null);

Plugin documentation.

### gatewayType
    
    
    public gatewayType: (google.cloud.apihub.v1.GatewayType|keyof typeof google.cloud.apihub.v1.GatewayType);

Plugin gatewayType.

### hostingService
    
    
    public hostingService?: (google.cloud.apihub.v1.Plugin.IHostingService|null);

Plugin hostingService.

### name
    
    
    public name: string;

Plugin name.

### ownershipType
    
    
    public ownershipType: (google.cloud.apihub.v1.Plugin.OwnershipType|keyof typeof google.cloud.apihub.v1.Plugin.OwnershipType);

Plugin ownershipType.

### pluginCategory
    
    
    public pluginCategory: (google.cloud.apihub.v1.PluginCategory|keyof typeof google.cloud.apihub.v1.PluginCategory);

Plugin pluginCategory.

### state
    
    
    public state: (google.cloud.apihub.v1.Plugin.State|keyof typeof google.cloud.apihub.v1.Plugin.State);

Plugin state.

### type
    
    
    public type?: (google.cloud.apihub.v1.IAttributeValues|null);

Plugin type.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

Plugin updateTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.apihub.v1.IPlugin): google.cloud.apihub.v1.Plugin;

Creates a new Plugin instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPlugin](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iplugin)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Plugin](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.plugin-class)` | Plugin instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.apihub.v1.Plugin;

Decodes a Plugin message from the specified reader or buffer.

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
`[Plugin](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.plugin-class)` | Plugin  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.apihub.v1.Plugin;

Decodes a Plugin message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Plugin](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.plugin-class)` | Plugin  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.apihub.v1.IPlugin, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Plugin message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPlugin](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iplugin)`   
Plugin message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.apihub.v1.IPlugin, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Plugin message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPlugin](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iplugin)`   
Plugin message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.apihub.v1.Plugin;

Creates a Plugin message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Plugin](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.plugin-class)` | Plugin  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Plugin

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

Converts this Plugin to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.apihub.v1.Plugin, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Plugin message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Plugin](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.plugin-class)`   
Plugin  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Plugin message.

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
