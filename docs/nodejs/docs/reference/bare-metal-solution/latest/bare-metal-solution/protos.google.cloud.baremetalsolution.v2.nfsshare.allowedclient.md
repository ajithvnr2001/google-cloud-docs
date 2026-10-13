---
url: https://docs.cloud.google.com/nodejs/docs/reference/bare-metal-solution/latest/bare-metal-solution/protos.google.cloud.baremetalsolution.v2.nfsshare.allowedclient
title: Class protos.google.cloud.baremetalsolution.v2.NfsShare.AllowedClient (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:47:37.603608+00:00
---

# Class protos.google.cloud.baremetalsolution.v2.NfsShare.AllowedClient (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/bare-metal-solution/latest/bare-metal-solution/protos.google.cloud.baremetalsolution.v2.nfsshare.allowedclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.baremetalsolution.v2.NfsShare.AllowedClient (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  1.1.0  0.3.2  0.2.2 

Represents an AllowedClient.

## Implements

[protos.google.cloud.baremetalsolution.v2.NfsShare.IAllowedClient](https://docs.cloud.google.com/nodejs/docs/reference/bare-metal-solution/latest/bare-metal-solution/protos.google.cloud.baremetalsolution.v2.nfsshare.iallowedclient)

## Package

[@google-cloud/bare-metal-solution](https://docs.cloud.google.com/nodejs/docs/reference/bare-metal-solution/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.baremetalsolution.v2.NfsShare.IAllowedClient);

Constructs a new AllowedClient.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAllowedClient](https://docs.cloud.google.com/nodejs/docs/reference/bare-metal-solution/latest/bare-metal-solution/protos.google.cloud.baremetalsolution.v2.nfsshare.iallowedclient)`   
Properties to set  
  
## Properties 

### allowDev
    
    
    public allowDev: boolean;

AllowedClient allowDev.

### allowedClientsCidr
    
    
    public allowedClientsCidr: string;

AllowedClient allowedClientsCidr.

### allowSuid
    
    
    public allowSuid: boolean;

AllowedClient allowSuid.

### mountPermissions
    
    
    public mountPermissions: (google.cloud.baremetalsolution.v2.NfsShare.MountPermissions|keyof typeof google.cloud.baremetalsolution.v2.NfsShare.MountPermissions);

AllowedClient mountPermissions.

### network
    
    
    public network: string;

AllowedClient network.

### nfsPath
    
    
    public nfsPath: string;

AllowedClient nfsPath.

### noRootSquash
    
    
    public noRootSquash: boolean;

AllowedClient noRootSquash.

### shareIp
    
    
    public shareIp: string;

AllowedClient shareIp.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.baremetalsolution.v2.NfsShare.IAllowedClient): google.cloud.baremetalsolution.v2.NfsShare.AllowedClient;

Creates a new AllowedClient instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAllowedClient](https://docs.cloud.google.com/nodejs/docs/reference/bare-metal-solution/latest/bare-metal-solution/protos.google.cloud.baremetalsolution.v2.nfsshare.iallowedclient)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AllowedClient](https://docs.cloud.google.com/nodejs/docs/reference/bare-metal-solution/latest/bare-metal-solution/protos.google.cloud.baremetalsolution.v2.nfsshare.allowedclient)` | AllowedClient instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.baremetalsolution.v2.NfsShare.AllowedClient;

Decodes an AllowedClient message from the specified reader or buffer.

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
`[AllowedClient](https://docs.cloud.google.com/nodejs/docs/reference/bare-metal-solution/latest/bare-metal-solution/protos.google.cloud.baremetalsolution.v2.nfsshare.allowedclient)` | AllowedClient  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.baremetalsolution.v2.NfsShare.AllowedClient;

Decodes an AllowedClient message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AllowedClient](https://docs.cloud.google.com/nodejs/docs/reference/bare-metal-solution/latest/bare-metal-solution/protos.google.cloud.baremetalsolution.v2.nfsshare.allowedclient)` | AllowedClient  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.baremetalsolution.v2.NfsShare.IAllowedClient, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AllowedClient message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAllowedClient](https://docs.cloud.google.com/nodejs/docs/reference/bare-metal-solution/latest/bare-metal-solution/protos.google.cloud.baremetalsolution.v2.nfsshare.iallowedclient)`   
AllowedClient message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.baremetalsolution.v2.NfsShare.IAllowedClient, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AllowedClient message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAllowedClient](https://docs.cloud.google.com/nodejs/docs/reference/bare-metal-solution/latest/bare-metal-solution/protos.google.cloud.baremetalsolution.v2.nfsshare.iallowedclient)`   
AllowedClient message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.baremetalsolution.v2.NfsShare.AllowedClient;

Creates an AllowedClient message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AllowedClient](https://docs.cloud.google.com/nodejs/docs/reference/bare-metal-solution/latest/bare-metal-solution/protos.google.cloud.baremetalsolution.v2.nfsshare.allowedclient)` | AllowedClient  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AllowedClient

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

Converts this AllowedClient to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.baremetalsolution.v2.NfsShare.AllowedClient, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AllowedClient message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AllowedClient](https://docs.cloud.google.com/nodejs/docs/reference/bare-metal-solution/latest/bare-metal-solution/protos.google.cloud.baremetalsolution.v2.nfsshare.allowedclient)`   
AllowedClient  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AllowedClient message.

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
