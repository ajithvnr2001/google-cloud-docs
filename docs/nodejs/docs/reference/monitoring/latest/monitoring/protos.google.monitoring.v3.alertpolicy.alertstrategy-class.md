---
url: https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.alertpolicy.alertstrategy-class
title: Class protos.google.monitoring.v3.AlertPolicy.AlertStrategy (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:48.601636+00:00
---

# Class protos.google.monitoring.v3.AlertPolicy.AlertStrategy (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.alertpolicy.alertstrategy-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.monitoring.v3.AlertPolicy.AlertStrategy (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.4.0  5.2.0  4.0.0  3.0.4  2.3.5 

Represents an AlertStrategy.

## Implements

[protos.google.monitoring.v3.AlertPolicy.IAlertStrategy](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.alertpolicy.ialertstrategy)

## Package

[@google-cloud/monitoring](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.monitoring.v3.AlertPolicy.IAlertStrategy);

Constructs a new AlertStrategy.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAlertStrategy](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.alertpolicy.ialertstrategy)`   
Properties to set  
  
## Properties 

### autoClose
    
    
    public autoClose?: (google.protobuf.IDuration|null);

AlertStrategy autoClose.

### notificationChannelStrategy
    
    
    public notificationChannelStrategy: google.monitoring.v3.AlertPolicy.AlertStrategy.INotificationChannelStrategy[];

AlertStrategy notificationChannelStrategy.

### notificationPrompts
    
    
    public notificationPrompts: google.monitoring.v3.AlertPolicy.AlertStrategy.NotificationPrompt[];

AlertStrategy notificationPrompts.

### notificationRateLimit
    
    
    public notificationRateLimit?: (google.monitoring.v3.AlertPolicy.AlertStrategy.INotificationRateLimit|null);

AlertStrategy notificationRateLimit.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.monitoring.v3.AlertPolicy.IAlertStrategy): google.monitoring.v3.AlertPolicy.AlertStrategy;

Creates a new AlertStrategy instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAlertStrategy](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.alertpolicy.ialertstrategy)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AlertStrategy](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.alertpolicy.alertstrategy-class)` | AlertStrategy instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.monitoring.v3.AlertPolicy.AlertStrategy;

Decodes an AlertStrategy message from the specified reader or buffer.

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
`[AlertStrategy](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.alertpolicy.alertstrategy-class)` | AlertStrategy  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.monitoring.v3.AlertPolicy.AlertStrategy;

Decodes an AlertStrategy message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AlertStrategy](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.alertpolicy.alertstrategy-class)` | AlertStrategy  
  
### encode(message, writer)
    
    
    public static encode(message: google.monitoring.v3.AlertPolicy.IAlertStrategy, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AlertStrategy message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAlertStrategy](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.alertpolicy.ialertstrategy)`   
AlertStrategy message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.monitoring.v3.AlertPolicy.IAlertStrategy, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AlertStrategy message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAlertStrategy](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.alertpolicy.ialertstrategy)`   
AlertStrategy message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.monitoring.v3.AlertPolicy.AlertStrategy;

Creates an AlertStrategy message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AlertStrategy](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.alertpolicy.alertstrategy-class)` | AlertStrategy  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AlertStrategy

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

Converts this AlertStrategy to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.monitoring.v3.AlertPolicy.AlertStrategy, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AlertStrategy message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AlertStrategy](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.alertpolicy.alertstrategy-class)`   
AlertStrategy  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AlertStrategy message.

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
