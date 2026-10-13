---
url: https://docs.cloud.google.com/nodejs/docs/reference/gsuiteaddons/latest/gsuiteaddons/protos.google.apps.script.type.menuitemextensionpoint
title: Class protos.google.apps.script.type.MenuItemExtensionPoint (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:26:44.021569+00:00
---

# Class protos.google.apps.script.type.MenuItemExtensionPoint (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/gsuiteaddons/latest/gsuiteaddons/protos.google.apps.script.type.menuitemextensionpoint

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.apps.script.type.MenuItemExtensionPoint (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.1.0  0.1.2 

Represents a MenuItemExtensionPoint.

## Implements

[protos.google.apps.script.type.IMenuItemExtensionPoint](https://docs.cloud.google.com/nodejs/docs/reference/gsuiteaddons/latest/gsuiteaddons/protos.google.apps.script.type.imenuitemextensionpoint)

## Package

[@google-cloud/gsuiteaddons](https://docs.cloud.google.com/nodejs/docs/reference/gsuiteaddons/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.apps.script.type.IMenuItemExtensionPoint);

Constructs a new MenuItemExtensionPoint.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IMenuItemExtensionPoint](https://docs.cloud.google.com/nodejs/docs/reference/gsuiteaddons/latest/gsuiteaddons/protos.google.apps.script.type.imenuitemextensionpoint)`   
Properties to set  
  
## Properties 

### label
    
    
    public label: string;

MenuItemExtensionPoint label.

### logoUrl
    
    
    public logoUrl: string;

MenuItemExtensionPoint logoUrl.

### runFunction
    
    
    public runFunction: string;

MenuItemExtensionPoint runFunction.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.apps.script.type.IMenuItemExtensionPoint): google.apps.script.type.MenuItemExtensionPoint;

Creates a new MenuItemExtensionPoint instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IMenuItemExtensionPoint](https://docs.cloud.google.com/nodejs/docs/reference/gsuiteaddons/latest/gsuiteaddons/protos.google.apps.script.type.imenuitemextensionpoint)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[MenuItemExtensionPoint](https://docs.cloud.google.com/nodejs/docs/reference/gsuiteaddons/latest/gsuiteaddons/protos.google.apps.script.type.menuitemextensionpoint)` | MenuItemExtensionPoint instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.apps.script.type.MenuItemExtensionPoint;

Decodes a MenuItemExtensionPoint message from the specified reader or buffer.

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
`[MenuItemExtensionPoint](https://docs.cloud.google.com/nodejs/docs/reference/gsuiteaddons/latest/gsuiteaddons/protos.google.apps.script.type.menuitemextensionpoint)` | MenuItemExtensionPoint  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.apps.script.type.MenuItemExtensionPoint;

Decodes a MenuItemExtensionPoint message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[MenuItemExtensionPoint](https://docs.cloud.google.com/nodejs/docs/reference/gsuiteaddons/latest/gsuiteaddons/protos.google.apps.script.type.menuitemextensionpoint)` | MenuItemExtensionPoint  
  
### encode(message, writer)
    
    
    public static encode(message: google.apps.script.type.IMenuItemExtensionPoint, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified MenuItemExtensionPoint message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IMenuItemExtensionPoint](https://docs.cloud.google.com/nodejs/docs/reference/gsuiteaddons/latest/gsuiteaddons/protos.google.apps.script.type.imenuitemextensionpoint)`   
MenuItemExtensionPoint message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.apps.script.type.IMenuItemExtensionPoint, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified MenuItemExtensionPoint message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IMenuItemExtensionPoint](https://docs.cloud.google.com/nodejs/docs/reference/gsuiteaddons/latest/gsuiteaddons/protos.google.apps.script.type.imenuitemextensionpoint)`   
MenuItemExtensionPoint message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.apps.script.type.MenuItemExtensionPoint;

Creates a MenuItemExtensionPoint message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[MenuItemExtensionPoint](https://docs.cloud.google.com/nodejs/docs/reference/gsuiteaddons/latest/gsuiteaddons/protos.google.apps.script.type.menuitemextensionpoint)` | MenuItemExtensionPoint  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for MenuItemExtensionPoint

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

Converts this MenuItemExtensionPoint to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.apps.script.type.MenuItemExtensionPoint, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a MenuItemExtensionPoint message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[MenuItemExtensionPoint](https://docs.cloud.google.com/nodejs/docs/reference/gsuiteaddons/latest/gsuiteaddons/protos.google.apps.script.type.menuitemextensionpoint)`   
MenuItemExtensionPoint  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a MenuItemExtensionPoint message.

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
