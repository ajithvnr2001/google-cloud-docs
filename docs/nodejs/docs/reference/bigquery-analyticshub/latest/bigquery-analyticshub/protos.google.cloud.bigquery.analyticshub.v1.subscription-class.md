---
url: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.subscription-class
title: Class protos.google.cloud.bigquery.analyticshub.v1.Subscription (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:20:17.688800+00:00
---

# Class protos.google.cloud.bigquery.analyticshub.v1.Subscription (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.subscription-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.bigquery.analyticshub.v1.Subscription (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.4.0  2.2.0  1.6.0  1.1.0  0.2.2  0.1.2 

Represents a Subscription.

## Implements

[protos.google.cloud.bigquery.analyticshub.v1.ISubscription](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.isubscription)

## Package

[@google-cloud/bigquery-analyticshub](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.bigquery.analyticshub.v1.ISubscription);

Constructs a new Subscription.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISubscription](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.isubscription)`   
Properties to set  
  
## Properties 

### commercialInfo
    
    
    public commercialInfo?: (google.cloud.bigquery.analyticshub.v1.Subscription.ICommercialInfo|null);

Subscription commercialInfo.

### creationTime
    
    
    public creationTime?: (google.protobuf.ITimestamp|null);

Subscription creationTime.

### dataExchange
    
    
    public dataExchange?: (string|null);

Subscription dataExchange.

### destinationDataset
    
    
    public destinationDataset?: (google.cloud.bigquery.analyticshub.v1.IDestinationDataset|null);

Subscription destinationDataset.

### lastModifyTime
    
    
    public lastModifyTime?: (google.protobuf.ITimestamp|null);

Subscription lastModifyTime.

### linkedDatasetMap
    
    
    public linkedDatasetMap: { [k: string]: google.cloud.bigquery.analyticshub.v1.Subscription.ILinkedResource };

Subscription linkedDatasetMap.

### linkedResources
    
    
    public linkedResources: google.cloud.bigquery.analyticshub.v1.Subscription.ILinkedResource[];

Subscription linkedResources.

### listing
    
    
    public listing?: (string|null);

Subscription listing.

### logLinkedDatasetQueryUserEmail
    
    
    public logLinkedDatasetQueryUserEmail?: (boolean|null);

Subscription logLinkedDatasetQueryUserEmail.

### name
    
    
    public name: string;

Subscription name.

### organizationDisplayName
    
    
    public organizationDisplayName: string;

Subscription organizationDisplayName.

### organizationId
    
    
    public organizationId: string;

Subscription organizationId.

### resourceName
    
    
    public resourceName?: ("listing"|"dataExchange");

Subscription resourceName.

### resourceType
    
    
    public resourceType: (google.cloud.bigquery.analyticshub.v1.SharedResourceType|keyof typeof google.cloud.bigquery.analyticshub.v1.SharedResourceType);

Subscription resourceType.

### state
    
    
    public state: (google.cloud.bigquery.analyticshub.v1.Subscription.State|keyof typeof google.cloud.bigquery.analyticshub.v1.Subscription.State);

Subscription state.

### subscriberContact
    
    
    public subscriberContact: string;

Subscription subscriberContact.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.bigquery.analyticshub.v1.ISubscription): google.cloud.bigquery.analyticshub.v1.Subscription;

Creates a new Subscription instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISubscription](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.isubscription)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Subscription](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.subscription-class)` | Subscription instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.bigquery.analyticshub.v1.Subscription;

Decodes a Subscription message from the specified reader or buffer.

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
`[Subscription](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.subscription-class)` | Subscription  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.bigquery.analyticshub.v1.Subscription;

Decodes a Subscription message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Subscription](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.subscription-class)` | Subscription  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.bigquery.analyticshub.v1.ISubscription, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Subscription message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISubscription](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.isubscription)`   
Subscription message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.bigquery.analyticshub.v1.ISubscription, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Subscription message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISubscription](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.isubscription)`   
Subscription message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.bigquery.analyticshub.v1.Subscription;

Creates a Subscription message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Subscription](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.subscription-class)` | Subscription  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Subscription

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

Converts this Subscription to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.bigquery.analyticshub.v1.Subscription, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Subscription message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Subscription](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.subscription-class)`   
Subscription  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Subscription message.

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
