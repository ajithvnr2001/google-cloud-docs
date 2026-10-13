---
url: https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.goldengateconnectionproperties-class
title: Class protos.google.cloud.oracledatabase.v1.GoldengateConnectionProperties (0.11.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:09:10.410145+00:00
---

# Class protos.google.cloud.oracledatabase.v1.GoldengateConnectionProperties (0.11.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.goldengateconnectionproperties-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.oracledatabase.v1.GoldengateConnectionProperties (0.11.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.1 (latest)  0.8.0  0.2.0  0.1.0 

Represents a GoldengateConnectionProperties.

## Implements

[protos.google.cloud.oracledatabase.v1.IGoldengateConnectionProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.igoldengateconnectionproperties)

## Package

[@google-cloud/oracledatabase](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.oracledatabase.v1.IGoldengateConnectionProperties);

Constructs a new GoldengateConnectionProperties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGoldengateConnectionProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.igoldengateconnectionproperties)`   
Properties to set  
  
## Properties 

### amazonKinesisConnectionProperties
    
    
    public amazonKinesisConnectionProperties?: (google.cloud.oracledatabase.v1.IGoldengateAmazonKinesisConnectionProperties|null);

GoldengateConnectionProperties amazonKinesisConnectionProperties.

### amazonRedshiftConnectionProperties
    
    
    public amazonRedshiftConnectionProperties?: (google.cloud.oracledatabase.v1.IGoldengateAmazonRedshiftConnectionProperties|null);

GoldengateConnectionProperties amazonRedshiftConnectionProperties.

### amazonS3ConnectionProperties
    
    
    public amazonS3ConnectionProperties?: (google.cloud.oracledatabase.v1.IGoldengateAmazonS3ConnectionProperties|null);

GoldengateConnectionProperties amazonS3ConnectionProperties.

### azureDataLakeStorageConnectionProperties
    
    
    public azureDataLakeStorageConnectionProperties?: (google.cloud.oracledatabase.v1.IGoldengateAzureDataLakeStorageConnectionProperties|null);

GoldengateConnectionProperties azureDataLakeStorageConnectionProperties.

### azureSynapseAnalyticsConnectionProperties
    
    
    public azureSynapseAnalyticsConnectionProperties?: (google.cloud.oracledatabase.v1.IGoldengateAzureSynapseAnalyticsConnectionProperties|null);

GoldengateConnectionProperties azureSynapseAnalyticsConnectionProperties.

### connectionDetails
    
    
    public connectionDetails?: ("oracleConnectionProperties"|"goldengateConnectionProperties"|"genericConnectionProperties"|"googleCloudStorageConnectionProperties"|"googleBigQueryConnectionProperties"|"mysqlConnectionProperties"|"kafkaConnectionProperties"|"kafkaSchemaRegistryConnectionProperties"|"ociObjectStorageConnectionProperties"|"azureDataLakeStorageConnectionProperties"|"azureSynapseAnalyticsConnectionProperties"|"postgresqlConnectionProperties"|"microsoftSqlserverConnectionProperties"|"amazonS3ConnectionProperties"|"hdfsConnectionProperties"|"javaMessageServiceConnectionProperties"|"mongodbConnectionProperties"|"oracleNosqlConnectionProperties"|"snowflakeConnectionProperties"|"amazonRedshiftConnectionProperties"|"elasticsearchConnectionProperties"|"amazonKinesisConnectionProperties"|"db2ConnectionProperties"|"redisConnectionProperties"|"databricksConnectionProperties"|"googlePubsubConnectionProperties"|"microsoftFabricConnectionProperties"|"oracleAiDataPlatformConnectionProperties"|"icebergConnectionProperties");

GoldengateConnectionProperties connectionDetails.

### connectionType
    
    
    public connectionType: (google.cloud.oracledatabase.v1.GoldengateConnectionProperties.GoldengateConnectionType|keyof typeof google.cloud.oracledatabase.v1.GoldengateConnectionProperties.GoldengateConnectionType);

GoldengateConnectionProperties connectionType.

### databricksConnectionProperties
    
    
    public databricksConnectionProperties?: (google.cloud.oracledatabase.v1.IGoldengateDatabricksConnectionProperties|null);

GoldengateConnectionProperties databricksConnectionProperties.

### db2ConnectionProperties
    
    
    public db2ConnectionProperties?: (google.cloud.oracledatabase.v1.IGoldengateDb2ConnectionProperties|null);

GoldengateConnectionProperties db2ConnectionProperties.

### description
    
    
    public description: string;

GoldengateConnectionProperties description.

### displayName
    
    
    public displayName: string;

GoldengateConnectionProperties displayName.

### elasticsearchConnectionProperties
    
    
    public elasticsearchConnectionProperties?: (google.cloud.oracledatabase.v1.IGoldengateElasticsearchConnectionProperties|null);

GoldengateConnectionProperties elasticsearchConnectionProperties.

### genericConnectionProperties
    
    
    public genericConnectionProperties?: (google.cloud.oracledatabase.v1.IGoldengateGenericConnectionProperties|null);

GoldengateConnectionProperties genericConnectionProperties.

### goldengateConnectionProperties
    
    
    public goldengateConnectionProperties?: (google.cloud.oracledatabase.v1.IGoldengateGoldengateConnectionProperties|null);

GoldengateConnectionProperties goldengateConnectionProperties.

### googleBigQueryConnectionProperties
    
    
    public googleBigQueryConnectionProperties?: (google.cloud.oracledatabase.v1.IGoldengateGoogleBigQueryConnectionProperties|null);

GoldengateConnectionProperties googleBigQueryConnectionProperties.

### googleCloudStorageConnectionProperties
    
    
    public googleCloudStorageConnectionProperties?: (google.cloud.oracledatabase.v1.IGoldengateGoogleCloudStorageConnectionProperties|null);

GoldengateConnectionProperties googleCloudStorageConnectionProperties.

### googlePubsubConnectionProperties
    
    
    public googlePubsubConnectionProperties?: (google.cloud.oracledatabase.v1.IGoldengateGooglePubsubConnectionProperties|null);

GoldengateConnectionProperties googlePubsubConnectionProperties.

### hdfsConnectionProperties
    
    
    public hdfsConnectionProperties?: (google.cloud.oracledatabase.v1.IGoldengateHdfsConnectionProperties|null);

GoldengateConnectionProperties hdfsConnectionProperties.

### icebergConnectionProperties
    
    
    public icebergConnectionProperties?: (google.cloud.oracledatabase.v1.IGoldengateIcebergConnectionProperties|null);

GoldengateConnectionProperties icebergConnectionProperties.

### ingressIpAddresses
    
    
    public ingressIpAddresses: string[];

GoldengateConnectionProperties ingressIpAddresses.

### javaMessageServiceConnectionProperties
    
    
    public javaMessageServiceConnectionProperties?: (google.cloud.oracledatabase.v1.IGoldengateJavaMessageServiceConnectionProperties|null);

GoldengateConnectionProperties javaMessageServiceConnectionProperties.

### kafkaConnectionProperties
    
    
    public kafkaConnectionProperties?: (google.cloud.oracledatabase.v1.IGoldengateKafkaConnectionProperties|null);

GoldengateConnectionProperties kafkaConnectionProperties.

### kafkaSchemaRegistryConnectionProperties
    
    
    public kafkaSchemaRegistryConnectionProperties?: (google.cloud.oracledatabase.v1.IGoldengateKafkaSchemaRegistryConnectionProperties|null);

GoldengateConnectionProperties kafkaSchemaRegistryConnectionProperties.

### lifecycleDetails
    
    
    public lifecycleDetails: string;

GoldengateConnectionProperties lifecycleDetails.

### lifecycleState
    
    
    public lifecycleState: (google.cloud.oracledatabase.v1.GoldengateConnectionProperties.GoldengateConnectionLifecycleState|keyof typeof google.cloud.oracledatabase.v1.GoldengateConnectionProperties.GoldengateConnectionLifecycleState);

GoldengateConnectionProperties lifecycleState.

### microsoftFabricConnectionProperties
    
    
    public microsoftFabricConnectionProperties?: (google.cloud.oracledatabase.v1.IGoldengateMicrosoftFabricConnectionProperties|null);

GoldengateConnectionProperties microsoftFabricConnectionProperties.

### microsoftSqlserverConnectionProperties
    
    
    public microsoftSqlserverConnectionProperties?: (google.cloud.oracledatabase.v1.IGoldengateMicrosoftSqlserverConnectionProperties|null);

GoldengateConnectionProperties microsoftSqlserverConnectionProperties.

### mongodbConnectionProperties
    
    
    public mongodbConnectionProperties?: (google.cloud.oracledatabase.v1.IGoldengateMongodbConnectionProperties|null);

GoldengateConnectionProperties mongodbConnectionProperties.

### mysqlConnectionProperties
    
    
    public mysqlConnectionProperties?: (google.cloud.oracledatabase.v1.IGoldengateMysqlConnectionProperties|null);

GoldengateConnectionProperties mysqlConnectionProperties.

### ocid
    
    
    public ocid: string;

GoldengateConnectionProperties ocid.

### ociObjectStorageConnectionProperties
    
    
    public ociObjectStorageConnectionProperties?: (google.cloud.oracledatabase.v1.IGoldengateOciObjectStorageConnectionProperties|null);

GoldengateConnectionProperties ociObjectStorageConnectionProperties.

### oracleAiDataPlatformConnectionProperties
    
    
    public oracleAiDataPlatformConnectionProperties?: (google.cloud.oracledatabase.v1.IGoldengateOracleAIDataPlatformConnectionProperties|null);

GoldengateConnectionProperties oracleAiDataPlatformConnectionProperties.

### oracleConnectionProperties
    
    
    public oracleConnectionProperties?: (google.cloud.oracledatabase.v1.IGoldengateOracleConnectionProperties|null);

GoldengateConnectionProperties oracleConnectionProperties.

### oracleNosqlConnectionProperties
    
    
    public oracleNosqlConnectionProperties?: (google.cloud.oracledatabase.v1.IGoldengateOracleNosqlConnectionProperties|null);

GoldengateConnectionProperties oracleNosqlConnectionProperties.

### postgresqlConnectionProperties
    
    
    public postgresqlConnectionProperties?: (google.cloud.oracledatabase.v1.IGoldengatePostgresqlConnectionProperties|null);

GoldengateConnectionProperties postgresqlConnectionProperties.

### redisConnectionProperties
    
    
    public redisConnectionProperties?: (google.cloud.oracledatabase.v1.IGoldengateRedisConnectionProperties|null);

GoldengateConnectionProperties redisConnectionProperties.

### routingMethod
    
    
    public routingMethod: (google.cloud.oracledatabase.v1.GoldengateConnectionProperties.GoldengateConnectionRoutingMethod|keyof typeof google.cloud.oracledatabase.v1.GoldengateConnectionProperties.GoldengateConnectionRoutingMethod);

GoldengateConnectionProperties routingMethod.

### snowflakeConnectionProperties
    
    
    public snowflakeConnectionProperties?: (google.cloud.oracledatabase.v1.IGoldengateSnowflakeConnectionProperties|null);

GoldengateConnectionProperties snowflakeConnectionProperties.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

GoldengateConnectionProperties updateTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.oracledatabase.v1.IGoldengateConnectionProperties): google.cloud.oracledatabase.v1.GoldengateConnectionProperties;

Creates a new GoldengateConnectionProperties instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGoldengateConnectionProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.igoldengateconnectionproperties)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[GoldengateConnectionProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.goldengateconnectionproperties-class)` | GoldengateConnectionProperties instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.oracledatabase.v1.GoldengateConnectionProperties;

Decodes a GoldengateConnectionProperties message from the specified reader or buffer.

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
`[GoldengateConnectionProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.goldengateconnectionproperties-class)` | GoldengateConnectionProperties  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.oracledatabase.v1.GoldengateConnectionProperties;

Decodes a GoldengateConnectionProperties message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[GoldengateConnectionProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.goldengateconnectionproperties-class)` | GoldengateConnectionProperties  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.oracledatabase.v1.IGoldengateConnectionProperties, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GoldengateConnectionProperties message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGoldengateConnectionProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.igoldengateconnectionproperties)`   
GoldengateConnectionProperties message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.oracledatabase.v1.IGoldengateConnectionProperties, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GoldengateConnectionProperties message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGoldengateConnectionProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.igoldengateconnectionproperties)`   
GoldengateConnectionProperties message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.oracledatabase.v1.GoldengateConnectionProperties;

Creates a GoldengateConnectionProperties message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[GoldengateConnectionProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.goldengateconnectionproperties-class)` | GoldengateConnectionProperties  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for GoldengateConnectionProperties

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

Converts this GoldengateConnectionProperties to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.oracledatabase.v1.GoldengateConnectionProperties, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a GoldengateConnectionProperties message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[GoldengateConnectionProperties](https://docs.cloud.google.com/nodejs/docs/reference/oracledatabase/latest/oracledatabase/protos.google.cloud.oracledatabase.v1.goldengateconnectionproperties-class)`   
GoldengateConnectionProperties  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a GoldengateConnectionProperties message.

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
