---
url: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage/latest/bigquery-storage/protos.google.cloud.bigquery.storage.v1.tablefieldschema-class
title: Class protos.google.cloud.bigquery.storage.v1.TableFieldSchema (5.1.2) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:56:31.082079+00:00
---

# Class protos.google.cloud.bigquery.storage.v1.TableFieldSchema (5.1.2)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage/latest/bigquery-storage/protos.google.cloud.bigquery.storage.v1.tablefieldschema-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.bigquery.storage.v1.TableFieldSchema (5.1.2) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.2 (latest)  5.1.1  4.10.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.1  4.1.0  4.0.0  3.4.0  3.2.0  3.1.1  2.8.0  2.7.0  2.6.2  2.5.4  2.3.0 

Represents a TableFieldSchema.

## Package

[@google-cloud/bigquery-storage](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.bigquery.storage.v1.ITableFieldSchema);

Constructs a new TableFieldSchema.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ITableFieldSchema](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage/latest/bigquery-storage/protos.google.cloud.bigquery.storage.v1.itablefieldschema)`   
Properties to set  
  
## Properties 

### defaultValueExpression
    
    
    public defaultValueExpression: string;

TableFieldSchema defaultValueExpression.

### description
    
    
    public description: string;

TableFieldSchema description.

### fields
    
    
    public fields: google.cloud.bigquery.storage.v1.ITableFieldSchema[];

TableFieldSchema fields.

### maxLength
    
    
    public maxLength: (number|Long|string);

TableFieldSchema maxLength.

### mode
    
    
    public mode: (google.cloud.bigquery.storage.v1.TableFieldSchema.Mode|keyof typeof google.cloud.bigquery.storage.v1.TableFieldSchema.Mode);

TableFieldSchema mode.

### name
    
    
    public name: string;

TableFieldSchema name.

### precision
    
    
    public precision: (number|Long|string);

TableFieldSchema precision.

### rangeElementType
    
    
    public rangeElementType?: (google.cloud.bigquery.storage.v1.TableFieldSchema.IFieldElementType|null);

TableFieldSchema rangeElementType.

### scale
    
    
    public scale: (number|Long|string);

TableFieldSchema scale.

### timestampPrecision
    
    
    public timestampPrecision?: (google.protobuf.IInt64Value|null);

TableFieldSchema timestampPrecision.

### type
    
    
    public type: (google.cloud.bigquery.storage.v1.TableFieldSchema.Type|keyof typeof google.cloud.bigquery.storage.v1.TableFieldSchema.Type);

TableFieldSchema type.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.bigquery.storage.v1.ITableFieldSchema): google.cloud.bigquery.storage.v1.TableFieldSchema;

Creates a new TableFieldSchema instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ITableFieldSchema](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage/latest/bigquery-storage/protos.google.cloud.bigquery.storage.v1.itablefieldschema)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[TableFieldSchema](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage/latest/bigquery-storage/protos.google.cloud.bigquery.storage.v1.tablefieldschema-class)` | TableFieldSchema instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.bigquery.storage.v1.TableFieldSchema;

Decodes a TableFieldSchema message from the specified reader or buffer.

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
`[TableFieldSchema](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage/latest/bigquery-storage/protos.google.cloud.bigquery.storage.v1.tablefieldschema-class)` | TableFieldSchema  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.bigquery.storage.v1.TableFieldSchema;

Decodes a TableFieldSchema message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[TableFieldSchema](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage/latest/bigquery-storage/protos.google.cloud.bigquery.storage.v1.tablefieldschema-class)` | TableFieldSchema  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.bigquery.storage.v1.ITableFieldSchema, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified TableFieldSchema message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ITableFieldSchema](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage/latest/bigquery-storage/protos.google.cloud.bigquery.storage.v1.itablefieldschema)`   
TableFieldSchema message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.bigquery.storage.v1.ITableFieldSchema, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified TableFieldSchema message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ITableFieldSchema](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage/latest/bigquery-storage/protos.google.cloud.bigquery.storage.v1.itablefieldschema)`   
TableFieldSchema message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.bigquery.storage.v1.TableFieldSchema;

Creates a TableFieldSchema message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[TableFieldSchema](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage/latest/bigquery-storage/protos.google.cloud.bigquery.storage.v1.tablefieldschema-class)` | TableFieldSchema  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for TableFieldSchema

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

Converts this TableFieldSchema to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.bigquery.storage.v1.TableFieldSchema, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a TableFieldSchema message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[TableFieldSchema](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage/latest/bigquery-storage/protos.google.cloud.bigquery.storage.v1.tablefieldschema-class)`   
TableFieldSchema  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a TableFieldSchema message.

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

Last updated 2026-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-16 UTC."],[],[]] 
