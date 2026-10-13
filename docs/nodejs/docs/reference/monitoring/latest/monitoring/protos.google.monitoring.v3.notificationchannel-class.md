---
url: https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.notificationchannel-class
title: Class protos.google.monitoring.v3.NotificationChannel (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:30:15.075538+00:00
---

# Class protos.google.monitoring.v3.NotificationChannel (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.notificationchannel-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.monitoring.v3.NotificationChannel (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.4.0  5.2.0  4.0.0  3.0.4  2.3.5 

Represents a NotificationChannel.

## Implements

[protos.google.monitoring.v3.INotificationChannel](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.inotificationchannel)

## Package

[@google-cloud/monitoring](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.monitoring.v3.INotificationChannel);

Constructs a new NotificationChannel.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[INotificationChannel](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.inotificationchannel)`   
Properties to set  
  
## Properties 

### creationRecord
    
    
    public creationRecord?: (google.monitoring.v3.IMutationRecord|null);

NotificationChannel creationRecord.

### description
    
    
    public description: string;

NotificationChannel description.

### displayName
    
    
    public displayName: string;

NotificationChannel displayName.

### enabled
    
    
    public enabled?: (google.protobuf.IBoolValue|null);

NotificationChannel enabled.

### labels
    
    
    public labels: { [k: string]: string };

NotificationChannel labels.

### mutationRecords
    
    
    public mutationRecords: google.monitoring.v3.IMutationRecord[];

NotificationChannel mutationRecords.

### name
    
    
    public name: string;

NotificationChannel name.

### type
    
    
    public type: string;

NotificationChannel type.

### userLabels
    
    
    public userLabels: { [k: string]: string };

NotificationChannel userLabels.

### verificationStatus
    
    
    public verificationStatus: (google.monitoring.v3.NotificationChannel.VerificationStatus|keyof typeof google.monitoring.v3.NotificationChannel.VerificationStatus);

NotificationChannel verificationStatus.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.monitoring.v3.INotificationChannel): google.monitoring.v3.NotificationChannel;

Creates a new NotificationChannel instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[INotificationChannel](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.inotificationchannel)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[NotificationChannel](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.notificationchannel-class)` | NotificationChannel instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.monitoring.v3.NotificationChannel;

Decodes a NotificationChannel message from the specified reader or buffer.

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
`[NotificationChannel](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.notificationchannel-class)` | NotificationChannel  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.monitoring.v3.NotificationChannel;

Decodes a NotificationChannel message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[NotificationChannel](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.notificationchannel-class)` | NotificationChannel  
  
### encode(message, writer)
    
    
    public static encode(message: google.monitoring.v3.INotificationChannel, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified NotificationChannel message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[INotificationChannel](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.inotificationchannel)`   
NotificationChannel message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.monitoring.v3.INotificationChannel, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified NotificationChannel message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[INotificationChannel](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.inotificationchannel)`   
NotificationChannel message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.monitoring.v3.NotificationChannel;

Creates a NotificationChannel message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[NotificationChannel](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.notificationchannel-class)` | NotificationChannel  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for NotificationChannel

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

Converts this NotificationChannel to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.monitoring.v3.NotificationChannel, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a NotificationChannel message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[NotificationChannel](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.notificationchannel-class)`   
NotificationChannel  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a NotificationChannel message.

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
