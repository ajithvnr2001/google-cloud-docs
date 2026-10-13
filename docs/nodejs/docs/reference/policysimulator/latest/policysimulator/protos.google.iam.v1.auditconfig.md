---
url: https://docs.cloud.google.com/nodejs/docs/reference/policysimulator/latest/policysimulator/protos.google.iam.v1.auditconfig
title: Class protos.google.iam.v1.AuditConfig (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:24:38.642269+00:00
---

# Class protos.google.iam.v1.AuditConfig (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/policysimulator/latest/policysimulator/protos.google.iam.v1.auditconfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.iam.v1.AuditConfig (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.6.0  0.5.1 

Represents an AuditConfig.

## Implements

[protos.google.iam.v1.IAuditConfig](https://docs.cloud.google.com/nodejs/docs/reference/policysimulator/latest/policysimulator/protos.google.iam.v1.iauditconfig)

## Package

[@google-cloud/policysimulator](https://docs.cloud.google.com/nodejs/docs/reference/policysimulator/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.iam.v1.IAuditConfig);

Constructs a new AuditConfig.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAuditConfig](https://docs.cloud.google.com/nodejs/docs/reference/policysimulator/latest/policysimulator/protos.google.iam.v1.iauditconfig)`   
Properties to set  
  
## Properties 

### auditLogConfigs
    
    
    public auditLogConfigs: google.iam.v1.IAuditLogConfig[];

AuditConfig auditLogConfigs.

### service
    
    
    public service: string;

AuditConfig service.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.iam.v1.IAuditConfig): google.iam.v1.AuditConfig;

Creates a new AuditConfig instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAuditConfig](https://docs.cloud.google.com/nodejs/docs/reference/policysimulator/latest/policysimulator/protos.google.iam.v1.iauditconfig)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AuditConfig](https://docs.cloud.google.com/nodejs/docs/reference/policysimulator/latest/policysimulator/protos.google.iam.v1.auditconfig)` | AuditConfig instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.iam.v1.AuditConfig;

Decodes an AuditConfig message from the specified reader or buffer.

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
`[AuditConfig](https://docs.cloud.google.com/nodejs/docs/reference/policysimulator/latest/policysimulator/protos.google.iam.v1.auditconfig)` | AuditConfig  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.iam.v1.AuditConfig;

Decodes an AuditConfig message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AuditConfig](https://docs.cloud.google.com/nodejs/docs/reference/policysimulator/latest/policysimulator/protos.google.iam.v1.auditconfig)` | AuditConfig  
  
### encode(message, writer)
    
    
    public static encode(message: google.iam.v1.IAuditConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AuditConfig message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAuditConfig](https://docs.cloud.google.com/nodejs/docs/reference/policysimulator/latest/policysimulator/protos.google.iam.v1.iauditconfig)`   
AuditConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.iam.v1.IAuditConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AuditConfig message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAuditConfig](https://docs.cloud.google.com/nodejs/docs/reference/policysimulator/latest/policysimulator/protos.google.iam.v1.iauditconfig)`   
AuditConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.iam.v1.AuditConfig;

Creates an AuditConfig message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AuditConfig](https://docs.cloud.google.com/nodejs/docs/reference/policysimulator/latest/policysimulator/protos.google.iam.v1.auditconfig)` | AuditConfig  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AuditConfig

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

Converts this AuditConfig to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.iam.v1.AuditConfig, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AuditConfig message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AuditConfig](https://docs.cloud.google.com/nodejs/docs/reference/policysimulator/latest/policysimulator/protos.google.iam.v1.auditconfig)`   
AuditConfig  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AuditConfig message.

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
