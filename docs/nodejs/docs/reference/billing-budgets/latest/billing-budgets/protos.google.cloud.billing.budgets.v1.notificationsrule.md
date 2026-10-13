---
url: https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1.notificationsrule
title: Class protos.google.cloud.billing.budgets.v1.NotificationsRule (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:36:51.416211+00:00
---

# Class protos.google.cloud.billing.budgets.v1.NotificationsRule (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1.notificationsrule

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.billing.budgets.v1.NotificationsRule (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  4.2.2  4.1.2  3.3.0  3.2.8 

Represents a NotificationsRule.

## Implements

[protos.google.cloud.billing.budgets.v1.INotificationsRule](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1.inotificationsrule)

## Package

[@google-cloud/billing-budgets](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.billing.budgets.v1.INotificationsRule);

Constructs a new NotificationsRule.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[INotificationsRule](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1.inotificationsrule)`   
Properties to set  
  
## Properties 

### disableDefaultIamRecipients
    
    
    public disableDefaultIamRecipients: boolean;

NotificationsRule disableDefaultIamRecipients.

### enableProjectLevelRecipients
    
    
    public enableProjectLevelRecipients: boolean;

NotificationsRule enableProjectLevelRecipients.

### monitoringNotificationChannels
    
    
    public monitoringNotificationChannels: string[];

NotificationsRule monitoringNotificationChannels.

### pubsubTopic
    
    
    public pubsubTopic: string;

NotificationsRule pubsubTopic.

### schemaVersion
    
    
    public schemaVersion: string;

NotificationsRule schemaVersion.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.billing.budgets.v1.INotificationsRule): google.cloud.billing.budgets.v1.NotificationsRule;

Creates a new NotificationsRule instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[INotificationsRule](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1.inotificationsrule)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[NotificationsRule](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1.notificationsrule)` | NotificationsRule instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.billing.budgets.v1.NotificationsRule;

Decodes a NotificationsRule message from the specified reader or buffer.

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
`[NotificationsRule](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1.notificationsrule)` | NotificationsRule  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.billing.budgets.v1.NotificationsRule;

Decodes a NotificationsRule message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[NotificationsRule](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1.notificationsrule)` | NotificationsRule  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.billing.budgets.v1.INotificationsRule, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified NotificationsRule message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[INotificationsRule](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1.inotificationsrule)`   
NotificationsRule message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.billing.budgets.v1.INotificationsRule, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified NotificationsRule message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[INotificationsRule](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1.inotificationsrule)`   
NotificationsRule message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.billing.budgets.v1.NotificationsRule;

Creates a NotificationsRule message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[NotificationsRule](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1.notificationsrule)` | NotificationsRule  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for NotificationsRule

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

Converts this NotificationsRule to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.billing.budgets.v1.NotificationsRule, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a NotificationsRule message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[NotificationsRule](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1.notificationsrule)`   
NotificationsRule  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a NotificationsRule message.

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
