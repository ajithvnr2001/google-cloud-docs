---
url: https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1.backendauthenticationconfig-class
title: Class protos.google.cloud.networksecurity.v1.BackendAuthenticationConfig (4.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:58.723818+00:00
---

# Class protos.google.cloud.networksecurity.v1.BackendAuthenticationConfig (4.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1.backendauthenticationconfig-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.networksecurity.v1.BackendAuthenticationConfig (4.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.1.1 (latest)  3.6.0  3.1.0  1.1.2  1.0.2  0.5.0  0.3.0  0.2.0 

Represents a BackendAuthenticationConfig.

## Implements

[protos.google.cloud.networksecurity.v1.IBackendAuthenticationConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1.ibackendauthenticationconfig)

## Package

[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.networksecurity.v1.IBackendAuthenticationConfig);

Constructs a new BackendAuthenticationConfig.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBackendAuthenticationConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1.ibackendauthenticationconfig)`   
Properties to set  
  
## Properties 

### clientCertificate
    
    
    public clientCertificate: string;

BackendAuthenticationConfig clientCertificate.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

BackendAuthenticationConfig createTime.

### description
    
    
    public description: string;

BackendAuthenticationConfig description.

### etag
    
    
    public etag: string;

BackendAuthenticationConfig etag.

### labels
    
    
    public labels: { [k: string]: string };

BackendAuthenticationConfig labels.

### name
    
    
    public name: string;

BackendAuthenticationConfig name.

### trustConfig
    
    
    public trustConfig: string;

BackendAuthenticationConfig trustConfig.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

BackendAuthenticationConfig updateTime.

### wellKnownRoots
    
    
    public wellKnownRoots: (google.cloud.networksecurity.v1.BackendAuthenticationConfig.WellKnownRoots|keyof typeof google.cloud.networksecurity.v1.BackendAuthenticationConfig.WellKnownRoots);

BackendAuthenticationConfig wellKnownRoots.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.networksecurity.v1.IBackendAuthenticationConfig): google.cloud.networksecurity.v1.BackendAuthenticationConfig;

Creates a new BackendAuthenticationConfig instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBackendAuthenticationConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1.ibackendauthenticationconfig)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[BackendAuthenticationConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1.backendauthenticationconfig-class)` | BackendAuthenticationConfig instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.networksecurity.v1.BackendAuthenticationConfig;

Decodes a BackendAuthenticationConfig message from the specified reader or buffer.

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
`[BackendAuthenticationConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1.backendauthenticationconfig-class)` | BackendAuthenticationConfig  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.networksecurity.v1.BackendAuthenticationConfig;

Decodes a BackendAuthenticationConfig message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[BackendAuthenticationConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1.backendauthenticationconfig-class)` | BackendAuthenticationConfig  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.networksecurity.v1.IBackendAuthenticationConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BackendAuthenticationConfig message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBackendAuthenticationConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1.ibackendauthenticationconfig)`   
BackendAuthenticationConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.networksecurity.v1.IBackendAuthenticationConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BackendAuthenticationConfig message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBackendAuthenticationConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1.ibackendauthenticationconfig)`   
BackendAuthenticationConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.networksecurity.v1.BackendAuthenticationConfig;

Creates a BackendAuthenticationConfig message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[BackendAuthenticationConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1.backendauthenticationconfig-class)` | BackendAuthenticationConfig  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for BackendAuthenticationConfig

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

Converts this BackendAuthenticationConfig to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.networksecurity.v1.BackendAuthenticationConfig, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a BackendAuthenticationConfig message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[BackendAuthenticationConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1.backendauthenticationconfig-class)`   
BackendAuthenticationConfig  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a BackendAuthenticationConfig message.

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
