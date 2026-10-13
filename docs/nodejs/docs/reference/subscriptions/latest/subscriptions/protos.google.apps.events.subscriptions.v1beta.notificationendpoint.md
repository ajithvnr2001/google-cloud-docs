---
url: https://docs.cloud.google.com/nodejs/docs/reference/subscriptions/latest/subscriptions/protos.google.apps.events.subscriptions.v1beta.notificationendpoint
title: Class protos.google.apps.events.subscriptions.v1beta.NotificationEndpoint (0.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:45:25.168992+00:00
---

# Class protos.google.apps.events.subscriptions.v1beta.NotificationEndpoint (0.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/subscriptions/latest/subscriptions/protos.google.apps.events.subscriptions.v1beta.notificationendpoint

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.apps.events.subscriptions.v1beta.NotificationEndpoint (0.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.3.1 (latest)  0.3.0 

Represents a NotificationEndpoint.

## Implements

[protos.google.apps.events.subscriptions.v1beta.INotificationEndpoint](https://docs.cloud.google.com/nodejs/docs/reference/subscriptions/latest/subscriptions/protos.google.apps.events.subscriptions.v1beta.inotificationendpoint)

## Package

[@google-cloud/subscriptions](https://docs.cloud.google.com/nodejs/docs/reference/subscriptions/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.apps.events.subscriptions.v1beta.INotificationEndpoint);

Constructs a new NotificationEndpoint.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[INotificationEndpoint](https://docs.cloud.google.com/nodejs/docs/reference/subscriptions/latest/subscriptions/protos.google.apps.events.subscriptions.v1beta.inotificationendpoint)`   
Properties to set  
  
## Properties 

### endpoint
    
    
    public endpoint?: "pubsubTopic";

NotificationEndpoint endpoint.

### pubsubTopic
    
    
    public pubsubTopic?: (string|null);

NotificationEndpoint pubsubTopic.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.apps.events.subscriptions.v1beta.INotificationEndpoint): google.apps.events.subscriptions.v1beta.NotificationEndpoint;

Creates a new NotificationEndpoint instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[INotificationEndpoint](https://docs.cloud.google.com/nodejs/docs/reference/subscriptions/latest/subscriptions/protos.google.apps.events.subscriptions.v1beta.inotificationendpoint)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[NotificationEndpoint](https://docs.cloud.google.com/nodejs/docs/reference/subscriptions/latest/subscriptions/protos.google.apps.events.subscriptions.v1beta.notificationendpoint)` | NotificationEndpoint instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.apps.events.subscriptions.v1beta.NotificationEndpoint;

Decodes a NotificationEndpoint message from the specified reader or buffer.

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
`[NotificationEndpoint](https://docs.cloud.google.com/nodejs/docs/reference/subscriptions/latest/subscriptions/protos.google.apps.events.subscriptions.v1beta.notificationendpoint)` | NotificationEndpoint  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.apps.events.subscriptions.v1beta.NotificationEndpoint;

Decodes a NotificationEndpoint message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[NotificationEndpoint](https://docs.cloud.google.com/nodejs/docs/reference/subscriptions/latest/subscriptions/protos.google.apps.events.subscriptions.v1beta.notificationendpoint)` | NotificationEndpoint  
  
### encode(message, writer)
    
    
    public static encode(message: google.apps.events.subscriptions.v1beta.INotificationEndpoint, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified NotificationEndpoint message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[INotificationEndpoint](https://docs.cloud.google.com/nodejs/docs/reference/subscriptions/latest/subscriptions/protos.google.apps.events.subscriptions.v1beta.inotificationendpoint)`   
NotificationEndpoint message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.apps.events.subscriptions.v1beta.INotificationEndpoint, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified NotificationEndpoint message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[INotificationEndpoint](https://docs.cloud.google.com/nodejs/docs/reference/subscriptions/latest/subscriptions/protos.google.apps.events.subscriptions.v1beta.inotificationendpoint)`   
NotificationEndpoint message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.apps.events.subscriptions.v1beta.NotificationEndpoint;

Creates a NotificationEndpoint message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[NotificationEndpoint](https://docs.cloud.google.com/nodejs/docs/reference/subscriptions/latest/subscriptions/protos.google.apps.events.subscriptions.v1beta.notificationendpoint)` | NotificationEndpoint  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for NotificationEndpoint

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

Converts this NotificationEndpoint to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.apps.events.subscriptions.v1beta.NotificationEndpoint, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a NotificationEndpoint message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[NotificationEndpoint](https://docs.cloud.google.com/nodejs/docs/reference/subscriptions/latest/subscriptions/protos.google.apps.events.subscriptions.v1beta.notificationendpoint)`   
NotificationEndpoint  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a NotificationEndpoint message.

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
