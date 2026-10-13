---
url: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1.connection
title: Class protos.google.cloud.bigquery.connection.v1.Connection (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:06.479302+00:00
---

# Class protos.google.cloud.bigquery.connection.v1.Connection (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1.connection

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.bigquery.connection.v1.Connection (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  2.2.1  2.1.1  2.0.2  1.5.1  1.4.2  1.3.5 

Represents a Connection.

## Implements

[protos.google.cloud.bigquery.connection.v1.IConnection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1.iconnection)

## Package

[@google-cloud/bigquery-connection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.bigquery.connection.v1.IConnection);

Constructs a new Connection.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IConnection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1.iconnection)`   
Properties to set  
  
## Properties 

### aws
    
    
    public aws?: (google.cloud.bigquery.connection.v1.IAwsProperties|null);

Connection aws.

### azure
    
    
    public azure?: (google.cloud.bigquery.connection.v1.IAzureProperties|null);

Connection azure.

### cloudResource
    
    
    public cloudResource?: (google.cloud.bigquery.connection.v1.ICloudResourceProperties|null);

Connection cloudResource.

### cloudSpanner
    
    
    public cloudSpanner?: (google.cloud.bigquery.connection.v1.ICloudSpannerProperties|null);

Connection cloudSpanner.

### cloudSql
    
    
    public cloudSql?: (google.cloud.bigquery.connection.v1.ICloudSqlProperties|null);

Connection cloudSql.

### creationTime
    
    
    public creationTime: (number|Long|string);

Connection creationTime.

### description
    
    
    public description: string;

Connection description.

### friendlyName
    
    
    public friendlyName: string;

Connection friendlyName.

### hasCredential
    
    
    public hasCredential: boolean;

Connection hasCredential.

### lastModifiedTime
    
    
    public lastModifiedTime: (number|Long|string);

Connection lastModifiedTime.

### name
    
    
    public name: string;

Connection name.

### properties
    
    
    public properties?: ("cloudSql"|"aws"|"azure"|"cloudSpanner"|"cloudResource"|"spark"|"salesforceDataCloud");

Connection properties.

### salesforceDataCloud
    
    
    public salesforceDataCloud?: (google.cloud.bigquery.connection.v1.ISalesforceDataCloudProperties|null);

Connection salesforceDataCloud.

### spark
    
    
    public spark?: (google.cloud.bigquery.connection.v1.ISparkProperties|null);

Connection spark.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.bigquery.connection.v1.IConnection): google.cloud.bigquery.connection.v1.Connection;

Creates a new Connection instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IConnection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1.iconnection)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Connection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1.connection)` | Connection instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.bigquery.connection.v1.Connection;

Decodes a Connection message from the specified reader or buffer.

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
`[Connection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1.connection)` | Connection  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.bigquery.connection.v1.Connection;

Decodes a Connection message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Connection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1.connection)` | Connection  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.bigquery.connection.v1.IConnection, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Connection message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IConnection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1.iconnection)`   
Connection message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.bigquery.connection.v1.IConnection, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Connection message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IConnection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1.iconnection)`   
Connection message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.bigquery.connection.v1.Connection;

Creates a Connection message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Connection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1.connection)` | Connection  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Connection

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

Converts this Connection to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.bigquery.connection.v1.Connection, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Connection message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Connection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1.connection)`   
Connection  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Connection message.

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
