---
url: https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.queryreservationsrequest-class
title: Class protos.google.cloud.capacityplanner.v1beta.QueryReservationsRequest (0.4.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:53:38.287243+00:00
---

# Class protos.google.cloud.capacityplanner.v1beta.QueryReservationsRequest (0.4.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.queryreservationsrequest-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.capacityplanner.v1beta.QueryReservationsRequest (0.4.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.1 (latest)  0.2.0  0.1.2 

Represents a QueryReservationsRequest.

## Implements

[protos.google.cloud.capacityplanner.v1beta.IQueryReservationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iqueryreservationsrequest)

## Package

[@google-cloud/capacityplanner](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.capacityplanner.v1beta.IQueryReservationsRequest);

Constructs a new QueryReservationsRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IQueryReservationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iqueryreservationsrequest)`   
Properties to set  
  
## Properties 

### aggregationMethod
    
    
    public aggregationMethod: (google.cloud.capacityplanner.v1beta.UsageHistory.AggregationMethod|keyof typeof google.cloud.capacityplanner.v1beta.UsageHistory.AggregationMethod);

QueryReservationsRequest aggregationMethod.

### cloudResourceType
    
    
    public cloudResourceType: string;

QueryReservationsRequest cloudResourceType.

### endDate
    
    
    public endDate?: (google.type.IDate|null);

QueryReservationsRequest endDate.

### gpuType
    
    
    public gpuType: string;

QueryReservationsRequest gpuType.

### includeUnapprovedReservations
    
    
    public includeUnapprovedReservations: boolean;

QueryReservationsRequest includeUnapprovedReservations.

### locationLevel
    
    
    public locationLevel: (google.cloud.capacityplanner.v1beta.TimeSeries.LocationType|keyof typeof google.cloud.capacityplanner.v1beta.TimeSeries.LocationType);

QueryReservationsRequest locationLevel.

### machineFamily
    
    
    public machineFamily: string;

QueryReservationsRequest machineFamily.

### machineShape
    
    
    public machineShape?: (google.cloud.capacityplanner.v1beta.IMachineShape|null);

QueryReservationsRequest machineShape.

### ownershipType
    
    
    public ownershipType: (google.cloud.capacityplanner.v1beta.QueryReservationsRequest.OwnershipType|keyof typeof google.cloud.capacityplanner.v1beta.QueryReservationsRequest.OwnershipType);

QueryReservationsRequest ownershipType.

### parent
    
    
    public parent: string;

QueryReservationsRequest parent.

### reservationDataLevel
    
    
    public reservationDataLevel: (google.cloud.capacityplanner.v1beta.QueryReservationsRequest.ReservationDataLevel|keyof typeof google.cloud.capacityplanner.v1beta.QueryReservationsRequest.ReservationDataLevel);

QueryReservationsRequest reservationDataLevel.

### reservationType
    
    
    public reservationType: (google.cloud.capacityplanner.v1beta.QueryReservationsRequest.ReservationType|keyof typeof google.cloud.capacityplanner.v1beta.QueryReservationsRequest.ReservationType);

QueryReservationsRequest reservationType.

### shareType
    
    
    public shareType: (google.cloud.capacityplanner.v1beta.QueryReservationsRequest.ShareType|keyof typeof google.cloud.capacityplanner.v1beta.QueryReservationsRequest.ShareType);

QueryReservationsRequest shareType.

### startDate
    
    
    public startDate?: (google.type.IDate|null);

QueryReservationsRequest startDate.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.capacityplanner.v1beta.IQueryReservationsRequest): google.cloud.capacityplanner.v1beta.QueryReservationsRequest;

Creates a new QueryReservationsRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IQueryReservationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iqueryreservationsrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[QueryReservationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.queryreservationsrequest-class)` | QueryReservationsRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.capacityplanner.v1beta.QueryReservationsRequest;

Decodes a QueryReservationsRequest message from the specified reader or buffer.

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
`[QueryReservationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.queryreservationsrequest-class)` | QueryReservationsRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.capacityplanner.v1beta.QueryReservationsRequest;

Decodes a QueryReservationsRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[QueryReservationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.queryreservationsrequest-class)` | QueryReservationsRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.capacityplanner.v1beta.IQueryReservationsRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified QueryReservationsRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IQueryReservationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iqueryreservationsrequest)`   
QueryReservationsRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.capacityplanner.v1beta.IQueryReservationsRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified QueryReservationsRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IQueryReservationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iqueryreservationsrequest)`   
QueryReservationsRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.capacityplanner.v1beta.QueryReservationsRequest;

Creates a QueryReservationsRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[QueryReservationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.queryreservationsrequest-class)` | QueryReservationsRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for QueryReservationsRequest

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

Converts this QueryReservationsRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.capacityplanner.v1beta.QueryReservationsRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a QueryReservationsRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[QueryReservationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.queryreservationsrequest-class)`   
QueryReservationsRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a QueryReservationsRequest message.

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
