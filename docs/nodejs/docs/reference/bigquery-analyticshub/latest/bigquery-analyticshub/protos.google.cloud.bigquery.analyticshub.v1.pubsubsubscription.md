---
url: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.pubsubsubscription
title: Class protos.google.cloud.bigquery.analyticshub.v1.PubSubSubscription (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:20:13.777139+00:00
---

# Class protos.google.cloud.bigquery.analyticshub.v1.PubSubSubscription (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.pubsubsubscription

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.bigquery.analyticshub.v1.PubSubSubscription (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.4.0  2.2.0  1.6.0  1.1.0  0.2.2  0.1.2 

Represents a PubSubSubscription.

## Implements

[protos.google.cloud.bigquery.analyticshub.v1.IPubSubSubscription](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.ipubsubsubscription)

## Package

[@google-cloud/bigquery-analyticshub](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.bigquery.analyticshub.v1.IPubSubSubscription);

Constructs a new PubSubSubscription.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPubSubSubscription](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.ipubsubsubscription)`   
Properties to set  
  
## Properties 

### ackDeadlineSeconds
    
    
    public ackDeadlineSeconds: number;

PubSubSubscription ackDeadlineSeconds.

### bigqueryConfig
    
    
    public bigqueryConfig?: (google.cloud.bigquery.analyticshub.v1.IBigQueryConfig|null);

PubSubSubscription bigqueryConfig.

### cloudStorageConfig
    
    
    public cloudStorageConfig?: (google.cloud.bigquery.analyticshub.v1.ICloudStorageConfig|null);

PubSubSubscription cloudStorageConfig.

### deadLetterPolicy
    
    
    public deadLetterPolicy?: (google.cloud.bigquery.analyticshub.v1.IDeadLetterPolicy|null);

PubSubSubscription deadLetterPolicy.

### detached
    
    
    public detached: boolean;

PubSubSubscription detached.

### enableExactlyOnceDelivery
    
    
    public enableExactlyOnceDelivery: boolean;

PubSubSubscription enableExactlyOnceDelivery.

### enableMessageOrdering
    
    
    public enableMessageOrdering: boolean;

PubSubSubscription enableMessageOrdering.

### expirationPolicy
    
    
    public expirationPolicy?: (google.cloud.bigquery.analyticshub.v1.IExpirationPolicy|null);

PubSubSubscription expirationPolicy.

### filter
    
    
    public filter: string;

PubSubSubscription filter.

### labels
    
    
    public labels: { [k: string]: string };

PubSubSubscription labels.

### messageRetentionDuration
    
    
    public messageRetentionDuration?: (google.protobuf.IDuration|null);

PubSubSubscription messageRetentionDuration.

### messageTransforms
    
    
    public messageTransforms: google.cloud.bigquery.analyticshub.v1.IMessageTransform[];

PubSubSubscription messageTransforms.

### name
    
    
    public name: string;

PubSubSubscription name.

### pushConfig
    
    
    public pushConfig?: (google.cloud.bigquery.analyticshub.v1.IPushConfig|null);

PubSubSubscription pushConfig.

### retainAckedMessages
    
    
    public retainAckedMessages: boolean;

PubSubSubscription retainAckedMessages.

### retryPolicy
    
    
    public retryPolicy?: (google.cloud.bigquery.analyticshub.v1.IRetryPolicy|null);

PubSubSubscription retryPolicy.

### tags
    
    
    public tags: { [k: string]: string };

PubSubSubscription tags.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.bigquery.analyticshub.v1.IPubSubSubscription): google.cloud.bigquery.analyticshub.v1.PubSubSubscription;

Creates a new PubSubSubscription instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPubSubSubscription](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.ipubsubsubscription)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.pubsubsubscription)` | PubSubSubscription instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.bigquery.analyticshub.v1.PubSubSubscription;

Decodes a PubSubSubscription message from the specified reader or buffer.

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
`[PubSubSubscription](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.pubsubsubscription)` | PubSubSubscription  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.bigquery.analyticshub.v1.PubSubSubscription;

Decodes a PubSubSubscription message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.pubsubsubscription)` | PubSubSubscription  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.bigquery.analyticshub.v1.IPubSubSubscription, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified PubSubSubscription message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPubSubSubscription](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.ipubsubsubscription)`   
PubSubSubscription message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.bigquery.analyticshub.v1.IPubSubSubscription, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified PubSubSubscription message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPubSubSubscription](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.ipubsubsubscription)`   
PubSubSubscription message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.bigquery.analyticshub.v1.PubSubSubscription;

Creates a PubSubSubscription message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[PubSubSubscription](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.pubsubsubscription)` | PubSubSubscription  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for PubSubSubscription

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

Converts this PubSubSubscription to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.bigquery.analyticshub.v1.PubSubSubscription, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a PubSubSubscription message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[PubSubSubscription](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.pubsubsubscription)`   
PubSubSubscription  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a PubSubSubscription message.

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
