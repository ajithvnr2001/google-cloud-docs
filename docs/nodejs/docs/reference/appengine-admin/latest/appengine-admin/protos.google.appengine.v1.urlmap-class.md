---
url: https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.urlmap-class
title: Class protos.google.appengine.v1.UrlMap (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:41:44.535085+00:00
---

# Class protos.google.appengine.v1.UrlMap (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.urlmap-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.appengine.v1.UrlMap (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  5.1.0  3.2.0  2.2.2  2.1.2  1.2.0  1.1.0  1.0.6 

Represents an UrlMap.

## Implements

[protos.google.appengine.v1.IUrlMap](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.iurlmap)

## Package

[@google-cloud/appengine-admin](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.appengine.v1.IUrlMap);

Constructs a new UrlMap.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUrlMap](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.iurlmap)`   
Properties to set  
  
## Properties 

### apiEndpoint
    
    
    public apiEndpoint?: (google.appengine.v1.IApiEndpointHandler|null);

UrlMap apiEndpoint.

### authFailAction
    
    
    public authFailAction: (google.appengine.v1.AuthFailAction|keyof typeof google.appengine.v1.AuthFailAction);

UrlMap authFailAction.

### handlerType
    
    
    public handlerType?: ("staticFiles"|"script"|"apiEndpoint");

UrlMap handlerType.

### login
    
    
    public login: (google.appengine.v1.LoginRequirement|keyof typeof google.appengine.v1.LoginRequirement);

UrlMap login.

### redirectHttpResponseCode
    
    
    public redirectHttpResponseCode: (google.appengine.v1.UrlMap.RedirectHttpResponseCode|keyof typeof google.appengine.v1.UrlMap.RedirectHttpResponseCode);

UrlMap redirectHttpResponseCode.

### script
    
    
    public script?: (google.appengine.v1.IScriptHandler|null);

UrlMap script.

### securityLevel
    
    
    public securityLevel: (google.appengine.v1.SecurityLevel|keyof typeof google.appengine.v1.SecurityLevel);

UrlMap securityLevel.

### staticFiles
    
    
    public staticFiles?: (google.appengine.v1.IStaticFilesHandler|null);

UrlMap staticFiles.

### urlRegex
    
    
    public urlRegex: string;

UrlMap urlRegex.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.appengine.v1.IUrlMap): google.appengine.v1.UrlMap;

Creates a new UrlMap instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUrlMap](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.iurlmap)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[UrlMap](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.urlmap-class)` | UrlMap instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.appengine.v1.UrlMap;

Decodes an UrlMap message from the specified reader or buffer.

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
`[UrlMap](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.urlmap-class)` | UrlMap  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.appengine.v1.UrlMap;

Decodes an UrlMap message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[UrlMap](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.urlmap-class)` | UrlMap  
  
### encode(message, writer)
    
    
    public static encode(message: google.appengine.v1.IUrlMap, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UrlMap message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUrlMap](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.iurlmap)`   
UrlMap message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.appengine.v1.IUrlMap, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UrlMap message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUrlMap](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.iurlmap)`   
UrlMap message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.appengine.v1.UrlMap;

Creates an UrlMap message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[UrlMap](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.urlmap-class)` | UrlMap  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for UrlMap

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

Converts this UrlMap to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.appengine.v1.UrlMap, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an UrlMap message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[UrlMap](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.urlmap-class)`   
UrlMap  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an UrlMap message.

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
