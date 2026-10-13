---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.session-class
title: Class protos.google.cloud.dataproc.v1.Session (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:04:00.342847+00:00
---

# Class protos.google.cloud.dataproc.v1.Session (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.session-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dataproc.v1.Session (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  6.8.0  6.7.0  6.6.0  5.13.0  5.12.0  5.10.0  5.9.0  5.7.0  5.5.0  5.4.0  4.5.0  4.3.1  4.1.1  3.2.0  3.1.0  3.0.0  2.5.0  2.4.4 

Represents a Session.

## Implements

[protos.google.cloud.dataproc.v1.ISession](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.isession)

## Package

[@google-cloud/dataproc](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.dataproc.v1.ISession);

Constructs a new Session.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISession](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.isession)`   
Properties to set  
  
## Properties 

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

Session createTime.

### creator
    
    
    public creator: string;

Session creator.

### environmentConfig
    
    
    public environmentConfig?: (google.cloud.dataproc.v1.IEnvironmentConfig|null);

Session environmentConfig.

### jupyterSession
    
    
    public jupyterSession?: (google.cloud.dataproc.v1.IJupyterConfig|null);

Session jupyterSession.

### labels
    
    
    public labels: { [k: string]: string };

Session labels.

### name
    
    
    public name: string;

Session name.

### runtimeConfig
    
    
    public runtimeConfig?: (google.cloud.dataproc.v1.IRuntimeConfig|null);

Session runtimeConfig.

### runtimeInfo
    
    
    public runtimeInfo?: (google.cloud.dataproc.v1.IRuntimeInfo|null);

Session runtimeInfo.

### sessionConfig
    
    
    public sessionConfig?: ("jupyterSession"|"sparkConnectSession");

Session sessionConfig.

### sessionTemplate
    
    
    public sessionTemplate: string;

Session sessionTemplate.

### sparkConnectSession
    
    
    public sparkConnectSession?: (google.cloud.dataproc.v1.ISparkConnectConfig|null);

Session sparkConnectSession.

### state
    
    
    public state: (google.cloud.dataproc.v1.Session.State|keyof typeof google.cloud.dataproc.v1.Session.State);

Session state.

### stateHistory
    
    
    public stateHistory: google.cloud.dataproc.v1.Session.ISessionStateHistory[];

Session stateHistory.

### stateMessage
    
    
    public stateMessage: string;

Session stateMessage.

### stateTime
    
    
    public stateTime?: (google.protobuf.ITimestamp|null);

Session stateTime.

### user
    
    
    public user: string;

Session user.

### uuid
    
    
    public uuid: string;

Session uuid.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.dataproc.v1.ISession): google.cloud.dataproc.v1.Session;

Creates a new Session instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISession](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.isession)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Session](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.session-class)` | Session instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.dataproc.v1.Session;

Decodes a Session message from the specified reader or buffer.

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
`[Session](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.session-class)` | Session  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.dataproc.v1.Session;

Decodes a Session message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Session](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.session-class)` | Session  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.dataproc.v1.ISession, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Session message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISession](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.isession)`   
Session message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.dataproc.v1.ISession, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Session message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISession](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.isession)`   
Session message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.dataproc.v1.Session;

Creates a Session message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Session](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.session-class)` | Session  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Session

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

Converts this Session to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.dataproc.v1.Session, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Session message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Session](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.session-class)`   
Session  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Session message.

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

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
