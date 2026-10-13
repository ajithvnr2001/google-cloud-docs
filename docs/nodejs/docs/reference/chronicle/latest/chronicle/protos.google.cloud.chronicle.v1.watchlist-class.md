---
url: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.watchlist-class
title: Class protos.google.cloud.chronicle.v1.Watchlist (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:11:21.156625+00:00
---

# Class protos.google.cloud.chronicle.v1.Watchlist (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.watchlist-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.chronicle.v1.Watchlist (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.8.0  0.6.0  0.5.0 

Represents a Watchlist.

## Implements

[protos.google.cloud.chronicle.v1.IWatchlist](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iwatchlist)

## Package

[@google-cloud/chronicle](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.chronicle.v1.IWatchlist);

Constructs a new Watchlist.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IWatchlist](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iwatchlist)`   
Properties to set  
  
## Properties 

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

Watchlist createTime.

### description
    
    
    public description: string;

Watchlist description.

### displayName
    
    
    public displayName: string;

Watchlist displayName.

### entityCount
    
    
    public entityCount?: (google.cloud.chronicle.v1.Watchlist.IEntityCount|null);

Watchlist entityCount.

### entityPopulationMechanism
    
    
    public entityPopulationMechanism?: (google.cloud.chronicle.v1.Watchlist.IEntityPopulationMechanism|null);

Watchlist entityPopulationMechanism.

### multiplyingFactor
    
    
    public multiplyingFactor: number;

Watchlist multiplyingFactor.

### name
    
    
    public name: string;

Watchlist name.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

Watchlist updateTime.

### watchlistUserPreferences
    
    
    public watchlistUserPreferences?: (google.cloud.chronicle.v1.IWatchlistUserPreferences|null);

Watchlist watchlistUserPreferences.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.chronicle.v1.IWatchlist): google.cloud.chronicle.v1.Watchlist;

Creates a new Watchlist instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IWatchlist](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iwatchlist)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Watchlist](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.watchlist-class)` | Watchlist instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.chronicle.v1.Watchlist;

Decodes a Watchlist message from the specified reader or buffer.

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
`[Watchlist](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.watchlist-class)` | Watchlist  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.chronicle.v1.Watchlist;

Decodes a Watchlist message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Watchlist](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.watchlist-class)` | Watchlist  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.chronicle.v1.IWatchlist, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Watchlist message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IWatchlist](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iwatchlist)`   
Watchlist message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.chronicle.v1.IWatchlist, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Watchlist message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IWatchlist](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iwatchlist)`   
Watchlist message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.chronicle.v1.Watchlist;

Creates a Watchlist message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Watchlist](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.watchlist-class)` | Watchlist  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Watchlist

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

Converts this Watchlist to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.chronicle.v1.Watchlist, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Watchlist message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Watchlist](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.watchlist-class)`   
Watchlist  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Watchlist message.

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
