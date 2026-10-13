---
url: https://docs.cloud.google.com/nodejs/docs/reference/netapp/latest/netapp/protos.google.cloud.netapp.v1.cacheparameters-class
title: Class protos.google.cloud.netapp.v1.CacheParameters (0.20.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:30:41.848179+00:00
---

# Class protos.google.cloud.netapp.v1.CacheParameters (0.20.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/netapp/latest/netapp/protos.google.cloud.netapp.v1.cacheparameters-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.netapp.v1.CacheParameters (0.20.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.1 (latest)  0.15.0  0.12.0  0.8.0  0.7.0  0.6.0  0.2.1 

Represents a CacheParameters.

## Implements

[protos.google.cloud.netapp.v1.ICacheParameters](https://docs.cloud.google.com/nodejs/docs/reference/netapp/latest/netapp/protos.google.cloud.netapp.v1.icacheparameters)

## Package

[@google-cloud/netapp](https://docs.cloud.google.com/nodejs/docs/reference/netapp/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.netapp.v1.ICacheParameters);

Constructs a new CacheParameters.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICacheParameters](https://docs.cloud.google.com/nodejs/docs/reference/netapp/latest/netapp/protos.google.cloud.netapp.v1.icacheparameters)`   
Properties to set  
  
## Properties 

### cacheConfig
    
    
    public cacheConfig?: (google.cloud.netapp.v1.ICacheConfig|null);

CacheParameters cacheConfig.

### cacheState
    
    
    public cacheState: (google.cloud.netapp.v1.CacheParameters.CacheState|keyof typeof google.cloud.netapp.v1.CacheParameters.CacheState);

CacheParameters cacheState.

### command
    
    
    public command: string;

CacheParameters command.

### enableGlobalFileLock
    
    
    public enableGlobalFileLock?: (boolean|null);

CacheParameters enableGlobalFileLock.

### passphrase
    
    
    public passphrase: string;

CacheParameters passphrase.

### peerClusterName
    
    
    public peerClusterName: string;

CacheParameters peerClusterName.

### peeringCommandExpiryTime
    
    
    public peeringCommandExpiryTime?: (google.protobuf.ITimestamp|null);

CacheParameters peeringCommandExpiryTime.

### peerIpAddresses
    
    
    public peerIpAddresses: string[];

CacheParameters peerIpAddresses.

### peerSvmName
    
    
    public peerSvmName: string;

CacheParameters peerSvmName.

### peerVolumeName
    
    
    public peerVolumeName: string;

CacheParameters peerVolumeName.

### stateDetails
    
    
    public stateDetails: string;

CacheParameters stateDetails.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.netapp.v1.ICacheParameters): google.cloud.netapp.v1.CacheParameters;

Creates a new CacheParameters instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICacheParameters](https://docs.cloud.google.com/nodejs/docs/reference/netapp/latest/netapp/protos.google.cloud.netapp.v1.icacheparameters)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[CacheParameters](https://docs.cloud.google.com/nodejs/docs/reference/netapp/latest/netapp/protos.google.cloud.netapp.v1.cacheparameters-class)` | CacheParameters instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.netapp.v1.CacheParameters;

Decodes a CacheParameters message from the specified reader or buffer.

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
`[CacheParameters](https://docs.cloud.google.com/nodejs/docs/reference/netapp/latest/netapp/protos.google.cloud.netapp.v1.cacheparameters-class)` | CacheParameters  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.netapp.v1.CacheParameters;

Decodes a CacheParameters message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[CacheParameters](https://docs.cloud.google.com/nodejs/docs/reference/netapp/latest/netapp/protos.google.cloud.netapp.v1.cacheparameters-class)` | CacheParameters  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.netapp.v1.ICacheParameters, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CacheParameters message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICacheParameters](https://docs.cloud.google.com/nodejs/docs/reference/netapp/latest/netapp/protos.google.cloud.netapp.v1.icacheparameters)`   
CacheParameters message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.netapp.v1.ICacheParameters, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CacheParameters message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICacheParameters](https://docs.cloud.google.com/nodejs/docs/reference/netapp/latest/netapp/protos.google.cloud.netapp.v1.icacheparameters)`   
CacheParameters message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.netapp.v1.CacheParameters;

Creates a CacheParameters message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[CacheParameters](https://docs.cloud.google.com/nodejs/docs/reference/netapp/latest/netapp/protos.google.cloud.netapp.v1.cacheparameters-class)` | CacheParameters  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for CacheParameters

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

Converts this CacheParameters to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.netapp.v1.CacheParameters, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a CacheParameters message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[CacheParameters](https://docs.cloud.google.com/nodejs/docs/reference/netapp/latest/netapp/protos.google.cloud.netapp.v1.cacheparameters-class)`   
CacheParameters  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a CacheParameters message.

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
