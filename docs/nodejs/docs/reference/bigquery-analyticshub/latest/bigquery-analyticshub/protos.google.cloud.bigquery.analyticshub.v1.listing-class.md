---
url: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.listing-class
title: Class protos.google.cloud.bigquery.analyticshub.v1.Listing (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:20:12.994420+00:00
---

# Class protos.google.cloud.bigquery.analyticshub.v1.Listing (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.listing-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.bigquery.analyticshub.v1.Listing (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.4.0  2.2.0  1.6.0  1.1.0  0.2.2  0.1.2 

Represents a Listing.

## Implements

[protos.google.cloud.bigquery.analyticshub.v1.IListing](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.ilisting)

## Package

[@google-cloud/bigquery-analyticshub](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.bigquery.analyticshub.v1.IListing);

Constructs a new Listing.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListing](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.ilisting)`   
Properties to set  
  
## Properties 

### allowOnlyMetadataSharing
    
    
    public allowOnlyMetadataSharing?: (boolean|null);

Listing allowOnlyMetadataSharing.

### bigqueryDataset
    
    
    public bigqueryDataset?: (google.cloud.bigquery.analyticshub.v1.Listing.IBigQueryDatasetSource|null);

Listing bigqueryDataset.

### categories
    
    
    public categories: google.cloud.bigquery.analyticshub.v1.Listing.Category[];

Listing categories.

### commercialInfo
    
    
    public commercialInfo?: (google.cloud.bigquery.analyticshub.v1.Listing.ICommercialInfo|null);

Listing commercialInfo.

### dataProvider
    
    
    public dataProvider?: (google.cloud.bigquery.analyticshub.v1.IDataProvider|null);

Listing dataProvider.

### description
    
    
    public description: string;

Listing description.

### discoveryType
    
    
    public discoveryType?: (google.cloud.bigquery.analyticshub.v1.DiscoveryType|keyof typeof google.cloud.bigquery.analyticshub.v1.DiscoveryType|null);

Listing discoveryType.

### displayName
    
    
    public displayName: string;

Listing displayName.

### documentation
    
    
    public documentation: string;

Listing documentation.

### icon
    
    
    public icon: (Uint8Array|Buffer|string);

Listing icon.

### logLinkedDatasetQueryUserEmail
    
    
    public logLinkedDatasetQueryUserEmail?: (boolean|null);

Listing logLinkedDatasetQueryUserEmail.

### name
    
    
    public name: string;

Listing name.

### primaryContact
    
    
    public primaryContact: string;

Listing primaryContact.

### publisher
    
    
    public publisher?: (google.cloud.bigquery.analyticshub.v1.IPublisher|null);

Listing publisher.

### pubsubTopic
    
    
    public pubsubTopic?: (google.cloud.bigquery.analyticshub.v1.Listing.IPubSubTopicSource|null);

Listing pubsubTopic.

### requestAccess
    
    
    public requestAccess: string;

Listing requestAccess.

### resourceType
    
    
    public resourceType: (google.cloud.bigquery.analyticshub.v1.SharedResourceType|keyof typeof google.cloud.bigquery.analyticshub.v1.SharedResourceType);

Listing resourceType.

### restrictedExportConfig
    
    
    public restrictedExportConfig?: (google.cloud.bigquery.analyticshub.v1.Listing.IRestrictedExportConfig|null);

Listing restrictedExportConfig.

### source
    
    
    public source?: ("bigqueryDataset"|"pubsubTopic");

Listing source.

### state
    
    
    public state: (google.cloud.bigquery.analyticshub.v1.Listing.State|keyof typeof google.cloud.bigquery.analyticshub.v1.Listing.State);

Listing state.

### storedProcedureConfig
    
    
    public storedProcedureConfig?: (google.cloud.bigquery.analyticshub.v1.IStoredProcedureConfig|null);

Listing storedProcedureConfig.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.bigquery.analyticshub.v1.IListing): google.cloud.bigquery.analyticshub.v1.Listing;

Creates a new Listing instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListing](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.ilisting)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Listing](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.listing-class)` | Listing instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.bigquery.analyticshub.v1.Listing;

Decodes a Listing message from the specified reader or buffer.

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
`[Listing](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.listing-class)` | Listing  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.bigquery.analyticshub.v1.Listing;

Decodes a Listing message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Listing](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.listing-class)` | Listing  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.bigquery.analyticshub.v1.IListing, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Listing message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListing](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.ilisting)`   
Listing message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.bigquery.analyticshub.v1.IListing, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Listing message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListing](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.ilisting)`   
Listing message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.bigquery.analyticshub.v1.Listing;

Creates a Listing message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Listing](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.listing-class)` | Listing  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Listing

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

Converts this Listing to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.bigquery.analyticshub.v1.Listing, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Listing message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Listing](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.listing-class)`   
Listing  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Listing message.

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
