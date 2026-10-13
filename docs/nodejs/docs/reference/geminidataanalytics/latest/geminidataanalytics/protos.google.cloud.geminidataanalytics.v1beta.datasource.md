---
url: https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.datasource
title: Class protos.google.cloud.geminidataanalytics.v1beta.Datasource (0.13.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:09:26.777666+00:00
---

# Class protos.google.cloud.geminidataanalytics.v1beta.Datasource (0.13.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.datasource

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.geminidataanalytics.v1beta.Datasource (0.13.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.1 (latest)  0.13.0  0.7.0  0.6.0  0.4.0  0.2.0 

Represents a Datasource.

## Implements

[protos.google.cloud.geminidataanalytics.v1beta.IDatasource](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.idatasource)

## Package

[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.geminidataanalytics.v1beta.IDatasource);

Constructs a new Datasource.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDatasource](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.idatasource)`   
Properties to set  
  
## Properties 

### alloyDbReference
    
    
    public alloyDbReference?: (google.cloud.geminidataanalytics.v1beta.IAlloyDbReference|null);

Datasource alloyDbReference.

### bigqueryPropertyGraphReference
    
    
    public bigqueryPropertyGraphReference?: (google.cloud.geminidataanalytics.v1beta.IBigQueryPropertyGraphReference|null);

Datasource bigqueryPropertyGraphReference.

### bigqueryTableReference
    
    
    public bigqueryTableReference?: (google.cloud.geminidataanalytics.v1beta.IBigQueryTableReference|null);

Datasource bigqueryTableReference.

### bigtableReference
    
    
    public bigtableReference?: (google.cloud.geminidataanalytics.v1beta.IBigtableReference|null);

Datasource bigtableReference.

### cloudSqlReference
    
    
    public cloudSqlReference?: (google.cloud.geminidataanalytics.v1beta.ICloudSqlReference|null);

Datasource cloudSqlReference.

### firestoreReference
    
    
    public firestoreReference?: (google.cloud.geminidataanalytics.v1beta.IFirestoreReference|null);

Datasource firestoreReference.

### lookerExploreReference
    
    
    public lookerExploreReference?: (google.cloud.geminidataanalytics.v1beta.ILookerExploreReference|null);

Datasource lookerExploreReference.

### reference
    
    
    public reference?: ("bigqueryTableReference"|"studioDatasourceId"|"lookerExploreReference"|"alloyDbReference"|"spannerReference"|"cloudSqlReference"|"bigtableReference"|"bigqueryPropertyGraphReference"|"firestoreReference");

Datasource reference.

### schema
    
    
    public schema?: (google.cloud.geminidataanalytics.v1beta.ISchema|null);

Datasource schema.

### spannerReference
    
    
    public spannerReference?: (google.cloud.geminidataanalytics.v1beta.ISpannerReference|null);

Datasource spannerReference.

### structSchema
    
    
    public structSchema?: (google.protobuf.IStruct|null);

Datasource structSchema.

### studioDatasourceId
    
    
    public studioDatasourceId?: (string|null);

Datasource studioDatasourceId.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.geminidataanalytics.v1beta.IDatasource): google.cloud.geminidataanalytics.v1beta.Datasource;

Creates a new Datasource instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDatasource](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.idatasource)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Datasource](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.datasource)` | Datasource instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.geminidataanalytics.v1beta.Datasource;

Decodes a Datasource message from the specified reader or buffer.

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
`[Datasource](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.datasource)` | Datasource  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.geminidataanalytics.v1beta.Datasource;

Decodes a Datasource message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Datasource](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.datasource)` | Datasource  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.geminidataanalytics.v1beta.IDatasource, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Datasource message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDatasource](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.idatasource)`   
Datasource message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.geminidataanalytics.v1beta.IDatasource, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Datasource message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDatasource](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.idatasource)`   
Datasource message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.geminidataanalytics.v1beta.Datasource;

Creates a Datasource message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Datasource](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.datasource)` | Datasource  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Datasource

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

Converts this Datasource to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.geminidataanalytics.v1beta.Datasource, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Datasource message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Datasource](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1beta.datasource)`   
Datasource  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Datasource message.

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
