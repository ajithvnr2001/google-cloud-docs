---
url: https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.managementserver-class
title: Class protos.google.cloud.backupdr.v1beta.ManagementServer (0.12.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:26:05.753820+00:00
---

# Class protos.google.cloud.backupdr.v1beta.ManagementServer (0.12.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.managementserver-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.backupdr.v1beta.ManagementServer (0.12.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.1 (latest)  0.12.0  0.9.0  0.8.0  0.7.0  0.6.0  0.1.0 

Represents a ManagementServer.

## Implements

[protos.google.cloud.backupdr.v1beta.IManagementServer](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.imanagementserver)

## Package

[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.backupdr.v1beta.IManagementServer);

Constructs a new ManagementServer.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IManagementServer](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.imanagementserver)`   
Properties to set  
  
## Properties 

### baProxyUri
    
    
    public baProxyUri: string[];

ManagementServer baProxyUri.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

ManagementServer createTime.

### description
    
    
    public description: string;

ManagementServer description.

### etag
    
    
    public etag: string;

ManagementServer etag.

### labels
    
    
    public labels: { [k: string]: string };

ManagementServer labels.

### managementUri
    
    
    public managementUri?: (google.cloud.backupdr.v1beta.IManagementURI|null);

ManagementServer managementUri.

### name
    
    
    public name: string;

ManagementServer name.

### networks
    
    
    public networks: google.cloud.backupdr.v1beta.INetworkConfig[];

ManagementServer networks.

### oauth2ClientId
    
    
    public oauth2ClientId: string;

ManagementServer oauth2ClientId.

### satisfiesPzi
    
    
    public satisfiesPzi: boolean;

ManagementServer satisfiesPzi.

### satisfiesPzs
    
    
    public satisfiesPzs?: (google.protobuf.IBoolValue|null);

ManagementServer satisfiesPzs.

### state
    
    
    public state: (google.cloud.backupdr.v1beta.ManagementServer.InstanceState|keyof typeof google.cloud.backupdr.v1beta.ManagementServer.InstanceState);

ManagementServer state.

### type
    
    
    public type: (google.cloud.backupdr.v1beta.ManagementServer.InstanceType|keyof typeof google.cloud.backupdr.v1beta.ManagementServer.InstanceType);

ManagementServer type.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

ManagementServer updateTime.

### workforceIdentityBasedManagementUri
    
    
    public workforceIdentityBasedManagementUri?: (google.cloud.backupdr.v1beta.IWorkforceIdentityBasedManagementURI|null);

ManagementServer workforceIdentityBasedManagementUri.

### workforceIdentityBasedOauth2ClientId
    
    
    public workforceIdentityBasedOauth2ClientId?: (google.cloud.backupdr.v1beta.IWorkforceIdentityBasedOAuth2ClientID|null);

ManagementServer workforceIdentityBasedOauth2ClientId.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.backupdr.v1beta.IManagementServer): google.cloud.backupdr.v1beta.ManagementServer;

Creates a new ManagementServer instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IManagementServer](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.imanagementserver)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ManagementServer](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.managementserver-class)` | ManagementServer instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.backupdr.v1beta.ManagementServer;

Decodes a ManagementServer message from the specified reader or buffer.

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
`[ManagementServer](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.managementserver-class)` | ManagementServer  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.backupdr.v1beta.ManagementServer;

Decodes a ManagementServer message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ManagementServer](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.managementserver-class)` | ManagementServer  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.backupdr.v1beta.IManagementServer, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ManagementServer message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IManagementServer](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.imanagementserver)`   
ManagementServer message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.backupdr.v1beta.IManagementServer, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ManagementServer message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IManagementServer](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.imanagementserver)`   
ManagementServer message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.backupdr.v1beta.ManagementServer;

Creates a ManagementServer message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ManagementServer](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.managementserver-class)` | ManagementServer  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ManagementServer

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

Converts this ManagementServer to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.backupdr.v1beta.ManagementServer, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ManagementServer message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ManagementServer](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.managementserver-class)`   
ManagementServer  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ManagementServer message.

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
