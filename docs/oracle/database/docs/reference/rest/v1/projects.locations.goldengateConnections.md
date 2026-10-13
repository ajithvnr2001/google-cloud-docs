---
url: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections
title: REST Resource: projects.locations.goldengateConnections \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:49.571888+00:00
---

# REST Resource: projects.locations.goldengateConnections  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  REST Resource: projects.locations.goldengateConnections Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: GoldengateConnection
    * JSON representation
  * GoldengateConnectionProperties
    * JSON representation
  * GoldengateOracleConnectionProperties
    * JSON representation
  * OracleAuthenticationMode
  * SessionMode
  * GoldengateGoldengateConnectionProperties
    * JSON representation
  * GoldengateGenericConnectionProperties
    * JSON representation
  * GoldengateGoogleCloudStorageConnectionProperties
    * JSON representation
  * GoldengateGoogleBigQueryConnectionProperties
    * JSON representation
  * GoldengateMysqlConnectionProperties
    * JSON representation
  * MysqlSecurityProtocol
  * SSLMode
  * NameValuePair
    * JSON representation
  * GoldengateKafkaConnectionProperties
    * JSON representation
  * KafkaBootstrapServer
    * JSON representation
  * KafkaSecurityProtocol
  * GoldengateKafkaSchemaRegistryConnectionProperties
    * JSON representation
  * AuthenticationType
  * GoldengateOciObjectStorageConnectionProperties
    * JSON representation
  * GoldengateAzureDataLakeStorageConnectionProperties
    * JSON representation
  * AuthenticationType
  * GoldengateAzureSynapseAnalyticsConnectionProperties
    * JSON representation
  * GoldengatePostgresqlConnectionProperties
    * JSON representation
  * PostgresqlSecurityProtocol
  * PostgresqlSslMode
  * GoldengateMicrosoftSqlserverConnectionProperties
    * JSON representation
  * MicrosoftSqlserverSecurityProtocol
  * GoldengateAmazonS3ConnectionProperties
    * JSON representation
  * GoldengateHdfsConnectionProperties
    * JSON representation
  * GoldengateJavaMessageServiceConnectionProperties
    * JSON representation
  * JmsSecurityProtocol
  * JmsAuthenticationType
  * GoldengateMongodbConnectionProperties
    * JSON representation
  * MongodbSecurityProtocol
  * GoldengateOracleNosqlConnectionProperties
    * JSON representation
  * GoldengateSnowflakeConnectionProperties
    * JSON representation
  * AuthenticationType
  * GoldengateAmazonRedshiftConnectionProperties
    * JSON representation
  * GoldengateElasticsearchConnectionProperties
    * JSON representation
  * ElasticsearchSecurityProtocol
  * ElasticsearchAuthenticationType
  * GoldengateAmazonKinesisConnectionProperties
    * JSON representation
  * GoldengateDb2ConnectionProperties
    * JSON representation
  * Db2SecurityProtocol
  * GoldengateRedisConnectionProperties
    * JSON representation
  * RedisSecurityProtocol
  * RedisAuthenticationType
  * GoldengateDatabricksConnectionProperties
    * JSON representation
  * DatabricksAuthenticationType
  * GoldengateGooglePubsubConnectionProperties
    * JSON representation
  * GoldengateMicrosoftFabricConnectionProperties
    * JSON representation
  * GoldengateOracleAIDataPlatformConnectionProperties
    * JSON representation
  * GoldengateIcebergConnectionProperties
    * JSON representation
  * IcebergCatalog
    * JSON representation
  * GlueIcebergCatalog
    * JSON representation
  * NessieIcebergCatalog
    * JSON representation
  * PolarisIcebergCatalog
    * JSON representation
  * RestIcebergCatalog
    * JSON representation
  * CatalogType
  * IcebergStorage
    * JSON representation
  * AmazonS3IcebergStorage
    * JSON representation
  * SchemeType
  * GoogleCloudStorageIcebergStorage
    * JSON representation
  * AzureDataLakeStorageIcebergStorage
    * JSON representation
  * StorageType
  * GoldengateConnectionType
  * GoldengateConnectionLifecycleState
  * GoldengateConnectionRoutingMethod
  * Methods



## Resource: GoldengateConnection

Details of the GoldengateConnection resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "properties": {
        object ([GoldengateConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateConnectionProperties))
      },
      "gcpOracleZone": string,
      "labels": {
        string: string,
        ...
      },
      "odbNetwork": string,
      "odbSubnet": string,
      "entitlementId": string,
      "createTime": string,
      "ociUrl": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the GoldengateConnection resource in the following format: projects/{project}/locations/{region}/goldengateConnections/{goldengateConnection}  
`properties` |  `object (`[GoldengateConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateConnectionProperties)`)` Required. The properties of the GoldengateConnection.  
`gcpOracleZone` |  `string` Optional. The GCP Oracle zone where Oracle GoldengateConnection is hosted. Example: us-east4-b-r2. If not specified, the system will pick a zone based on availability.  
`labels` |  `map (key: string, value: string)` Optional. The labels or tags associated with the GoldengateConnection.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`odbNetwork` |  `string` Optional. The name of the OdbNetwork associated with the GoldengateConnection. The format is projects/{project}/locations/{location}/odbNetworks/{odbNetwork}. It is optional but if specified, this should match the parent ODBNetwork of the OdbSubnet.  
`odbSubnet` |  `string` Optional. The name of the OdbSubnet associated with the GoldengateConnection for IP allocation. Format: projects/{project}/locations/{location}/odbNetworks/{odbNetwork}/odbSubnets/{odbSubnet}  
`entitlementId` |  `string` Output only. The ID of the subscription entitlement associated with the GoldengateConnection.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time that the GoldengateConnection was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`ociUrl` |  `string` Output only. HTTPS link to OCI resources exposed to Customer via UI Interface.  
  
## GoldengateConnectionProperties

The properties of a GoldengateConnection.

JSON representation  
---  
      
    
    {
      "connectionType": enum ([GoldengateConnectionType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateConnectionType)),
      "ocid": string,
      "displayName": string,
      "description": string,
      "lifecycleState": enum ([GoldengateConnectionLifecycleState](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateConnectionLifecycleState)),
      "lifecycleDetails": string,
      "updateTime": string,
      "routingMethod": enum ([GoldengateConnectionRoutingMethod](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateConnectionRoutingMethod)),
      "ingressIpAddresses": [
        string
      ],
    
      // Union field connection_details can be only one of the following:
      "oracleConnectionProperties": {
        object ([GoldengateOracleConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateOracleConnectionProperties))
      },
      "goldengateConnectionProperties": {
        object ([GoldengateGoldengateConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateGoldengateConnectionProperties))
      },
      "genericConnectionProperties": {
        object ([GoldengateGenericConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateGenericConnectionProperties))
      },
      "googleCloudStorageConnectionProperties": {
        object ([GoldengateGoogleCloudStorageConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateGoogleCloudStorageConnectionProperties))
      },
      "googleBigQueryConnectionProperties": {
        object ([GoldengateGoogleBigQueryConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateGoogleBigQueryConnectionProperties))
      },
      "mysqlConnectionProperties": {
        object ([GoldengateMysqlConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateMysqlConnectionProperties))
      },
      "kafkaConnectionProperties": {
        object ([GoldengateKafkaConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateKafkaConnectionProperties))
      },
      "kafkaSchemaRegistryConnectionProperties": {
        object ([GoldengateKafkaSchemaRegistryConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateKafkaSchemaRegistryConnectionProperties))
      },
      "ociObjectStorageConnectionProperties": {
        object ([GoldengateOciObjectStorageConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateOciObjectStorageConnectionProperties))
      },
      "azureDataLakeStorageConnectionProperties": {
        object ([GoldengateAzureDataLakeStorageConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateAzureDataLakeStorageConnectionProperties))
      },
      "azureSynapseAnalyticsConnectionProperties": {
        object ([GoldengateAzureSynapseAnalyticsConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateAzureSynapseAnalyticsConnectionProperties))
      },
      "postgresqlConnectionProperties": {
        object ([GoldengatePostgresqlConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengatePostgresqlConnectionProperties))
      },
      "microsoftSqlserverConnectionProperties": {
        object ([GoldengateMicrosoftSqlserverConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateMicrosoftSqlserverConnectionProperties))
      },
      "amazonS3ConnectionProperties": {
        object ([GoldengateAmazonS3ConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateAmazonS3ConnectionProperties))
      },
      "hdfsConnectionProperties": {
        object ([GoldengateHdfsConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateHdfsConnectionProperties))
      },
      "javaMessageServiceConnectionProperties": {
        object ([GoldengateJavaMessageServiceConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateJavaMessageServiceConnectionProperties))
      },
      "mongodbConnectionProperties": {
        object ([GoldengateMongodbConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateMongodbConnectionProperties))
      },
      "oracleNosqlConnectionProperties": {
        object ([GoldengateOracleNosqlConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateOracleNosqlConnectionProperties))
      },
      "snowflakeConnectionProperties": {
        object ([GoldengateSnowflakeConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateSnowflakeConnectionProperties))
      },
      "amazonRedshiftConnectionProperties": {
        object ([GoldengateAmazonRedshiftConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateAmazonRedshiftConnectionProperties))
      },
      "elasticsearchConnectionProperties": {
        object ([GoldengateElasticsearchConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateElasticsearchConnectionProperties))
      },
      "amazonKinesisConnectionProperties": {
        object ([GoldengateAmazonKinesisConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateAmazonKinesisConnectionProperties))
      },
      "db2ConnectionProperties": {
        object ([GoldengateDb2ConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateDb2ConnectionProperties))
      },
      "redisConnectionProperties": {
        object ([GoldengateRedisConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateRedisConnectionProperties))
      },
      "databricksConnectionProperties": {
        object ([GoldengateDatabricksConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateDatabricksConnectionProperties))
      },
      "googlePubsubConnectionProperties": {
        object ([GoldengateGooglePubsubConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateGooglePubsubConnectionProperties))
      },
      "microsoftFabricConnectionProperties": {
        object ([GoldengateMicrosoftFabricConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateMicrosoftFabricConnectionProperties))
      },
      "oracleAiDataPlatformConnectionProperties": {
        object ([GoldengateOracleAIDataPlatformConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateOracleAIDataPlatformConnectionProperties))
      },
      "icebergConnectionProperties": {
        object ([GoldengateIcebergConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateIcebergConnectionProperties))
      }
      // End of list of possible types for union field connection_details.
    }  
  
Fields  
---  
`connectionType` |  `enum (`[GoldengateConnectionType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateConnectionType)`)` Required. The connection type.  
`ocid` |  `string` Output only. The [OCID] of the connection being referenced.  
`displayName` |  `string` Required. An object's Display Name.  
`description` |  `string` Optional. Metadata about this specific object.  
`lifecycleState` |  `enum (`[GoldengateConnectionLifecycleState](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateConnectionLifecycleState)`)` Output only. The lifecycle state of the connection.  
`lifecycleDetails` |  `string` Output only. Describes the object's current state in detail. For example, it can be used to provide actionable information for a resource in a Failed state.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the resource was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`routingMethod` |  `enum (`[GoldengateConnectionRoutingMethod](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateConnectionRoutingMethod)`)` Optional. The routing method for the GoldengateConnection.  
`ingressIpAddresses[]` |  `string` Output only. The Ingress IPs of the GoldengateConnection.  
Union field `connection_details`. The connection details. `connection_details` can be only one of the following:  
`oracleConnectionProperties` |  `object (`[GoldengateOracleConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateOracleConnectionProperties)`)` Properties for an Oracle Database Connection.  
`goldengateConnectionProperties` |  `object (`[GoldengateGoldengateConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateGoldengateConnectionProperties)`)` Properties for a Goldengate Connection.  
`genericConnectionProperties` |  `object (`[GoldengateGenericConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateGenericConnectionProperties)`)` Properties for a Generic Connection.  
`googleCloudStorageConnectionProperties` |  `object (`[GoldengateGoogleCloudStorageConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateGoogleCloudStorageConnectionProperties)`)` Properties for a Google Cloud Storage Connection.  
`googleBigQueryConnectionProperties` |  `object (`[GoldengateGoogleBigQueryConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateGoogleBigQueryConnectionProperties)`)` Properties for a Google BigQuery Connection.  
`mysqlConnectionProperties` |  `object (`[GoldengateMysqlConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateMysqlConnectionProperties)`)` Properties for a Mysql Connection.  
`kafkaConnectionProperties` |  `object (`[GoldengateKafkaConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateKafkaConnectionProperties)`)` Properties for a Kafka Connection.  
`kafkaSchemaRegistryConnectionProperties` |  `object (`[GoldengateKafkaSchemaRegistryConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateKafkaSchemaRegistryConnectionProperties)`)` Properties for a Kafka Schema Registry Connection.  
`ociObjectStorageConnectionProperties` |  `object (`[GoldengateOciObjectStorageConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateOciObjectStorageConnectionProperties)`)` Properties for an OCI Object Storage Connection.  
`azureDataLakeStorageConnectionProperties` |  `object (`[GoldengateAzureDataLakeStorageConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateAzureDataLakeStorageConnectionProperties)`)` Properties for an Azure Data Lake Storage Connection.  
`azureSynapseAnalyticsConnectionProperties` |  `object (`[GoldengateAzureSynapseAnalyticsConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateAzureSynapseAnalyticsConnectionProperties)`)` Properties for an Azure Synapse Analytics connection.  
`postgresqlConnectionProperties` |  `object (`[GoldengatePostgresqlConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengatePostgresqlConnectionProperties)`)` Properties for a PostgreSQL connection.  
`microsoftSqlserverConnectionProperties` |  `object (`[GoldengateMicrosoftSqlserverConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateMicrosoftSqlserverConnectionProperties)`)` Properties for a Microsoft SQL Server connection.  
`amazonS3ConnectionProperties` |  `object (`[GoldengateAmazonS3ConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateAmazonS3ConnectionProperties)`)` Properties for an Amazon S3 connection.  
`hdfsConnectionProperties` |  `object (`[GoldengateHdfsConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateHdfsConnectionProperties)`)` Properties for an HDFS connection.  
`javaMessageServiceConnectionProperties` |  `object (`[GoldengateJavaMessageServiceConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateJavaMessageServiceConnectionProperties)`)` Properties for a Java Message Service connection.  
`mongodbConnectionProperties` |  `object (`[GoldengateMongodbConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateMongodbConnectionProperties)`)` Properties for a MongoDB connection.  
`oracleNosqlConnectionProperties` |  `object (`[GoldengateOracleNosqlConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateOracleNosqlConnectionProperties)`)` Properties for an Oracle NoSQL connection.  
`snowflakeConnectionProperties` |  `object (`[GoldengateSnowflakeConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateSnowflakeConnectionProperties)`)` Properties for a Snowflake connection.  
`amazonRedshiftConnectionProperties` |  `object (`[GoldengateAmazonRedshiftConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateAmazonRedshiftConnectionProperties)`)` Properties for an Amazon Redshift connection.  
`elasticsearchConnectionProperties` |  `object (`[GoldengateElasticsearchConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateElasticsearchConnectionProperties)`)` Properties for an Elasticsearch connection.  
`amazonKinesisConnectionProperties` |  `object (`[GoldengateAmazonKinesisConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateAmazonKinesisConnectionProperties)`)` Properties for an Amazon Kinesis connection.  
`db2ConnectionProperties` |  `object (`[GoldengateDb2ConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateDb2ConnectionProperties)`)` Properties for a DB2 connection.  
`redisConnectionProperties` |  `object (`[GoldengateRedisConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateRedisConnectionProperties)`)` Properties for a Redis connection.  
`databricksConnectionProperties` |  `object (`[GoldengateDatabricksConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateDatabricksConnectionProperties)`)` Properties for a Databricks connection.  
`googlePubsubConnectionProperties` |  `object (`[GoldengateGooglePubsubConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateGooglePubsubConnectionProperties)`)` Properties for a Google Pub/Sub connection.  
`microsoftFabricConnectionProperties` |  `object (`[GoldengateMicrosoftFabricConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateMicrosoftFabricConnectionProperties)`)` Properties for a Microsoft Fabric connection.  
`oracleAiDataPlatformConnectionProperties` |  `object (`[GoldengateOracleAIDataPlatformConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateOracleAIDataPlatformConnectionProperties)`)` Properties for an Oracle AI Data Platform connection.  
`icebergConnectionProperties` |  `object (`[GoldengateIcebergConnectionProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoldengateIcebergConnectionProperties)`)` Properties for an Iceberg connection.  
  
## GoldengateOracleConnectionProperties

The properties of Goldengate Oracle Database Connection.

JSON representation  
---  
      
    
    {
      "technologyType": string,
      "username": string,
      "authenticationMode": enum ([OracleAuthenticationMode](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#OracleAuthenticationMode)),
      "connectionString": string,
      "sessionMode": enum ([SessionMode](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#SessionMode)),
      "gcpOracleDatabaseId": string,
      "walletFile": string,
    
      // Union field connection_password_options can be only one of the following:
      "password": string,
      "passwordSecretVersion": string
      // End of list of possible types for union field connection_password_options.
    }  
  
Fields  
---  
`technologyType` |  `string` Optional. The technology type.  
`username` |  `string` Optional. The username Oracle Goldengate uses to connect.  
`authenticationMode` |  `enum (`[OracleAuthenticationMode](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#OracleAuthenticationMode)`)` Optional. Authentication mode.  
`connectionString` |  `string` Optional. Connect descriptor or Easy Connect Naming method used to connect to a database.  
`sessionMode` |  `enum (`[SessionMode](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#SessionMode)`)` Optional. The mode of the database connection session to be established by the data client.  
`gcpOracleDatabaseId` |  `string` Optional. Autonomous AI Database instance id of database in Oracle Database @ Google Cloud. If gcpOracleDatabaseId is provided, connectionString must be empty. Format: projects/{project}/locations/{location}/autonomousDatabases/{autonomousDatabase}  
`walletFile` |  `string` Optional. The wallet contents Oracle Goldengate uses to make connections to a database. This attribute is expected to be base64 encoded.  
Union field `connection_password_options`. The password Oracle Goldengate uses to connect the associated system of the given technology. It must conform to the specific security requirements including length, case sensitivity, and so on. `connection_password_options` can be only one of the following:  
`password` |  `string` Optional. Input only. The password Oracle Goldengate uses in plain text.  
`passwordSecretVersion` |  `string` Optional. Input only. The resource name of a secret version in Secret Manager which contains the password Oracle Goldengate uses. Format: projects/{project}/secrets/{secret}/versions/{version}.  
  
## OracleAuthenticationMode

Enum for Authentication mode.

Enums  
---  
`ORACLE_AUTHENTICATION_MODE_UNSPECIFIED` | Authentication mode not specified.  
`TLS` | TLS authentication mode.  
`MTLS` | MTLS authentication mode.  
  
## SessionMode

The various session modes of the GoldengateConnection.

Enums  
---  
`SESSION_MODE_UNSPECIFIED` | Default unspecified value.  
`DIRECT` | Indicates that the resource is using direct session mode.  
`REDIRECT` | Indicates that the resource is using redirect session mode.  
  
## GoldengateGoldengateConnectionProperties

The properties of GoldengateGoldengateConnectionProperties.

JSON representation  
---  
      
    
    {
      "technologyType": string,
      "goldengateDeploymentId": string,
      "host": string,
      "port": integer,
      "username": string,
    
      // Union field connection_password_options can be only one of the following:
      "password": string,
      "passwordSecretVersion": string
      // End of list of possible types for union field connection_password_options.
    }  
  
Fields  
---  
`technologyType` |  `string` Optional. The technology type.  
`goldengateDeploymentId` |  `string` Optional. The name of the GoldengateDeployment associated with the GoldengateConnection. Format: projects/{project}/locations/{location}/goldengateDeployments/{goldengateDeployment}  
`host` |  `string` Optional. The host of the GoldengateConnection.  
`port` |  `integer` Optional. The port of the GoldengateConnection.  
`username` |  `string` Optional. The username credential.  
Union field `connection_password_options`. The password used to connect to the Oracle Goldengate accessed through this connection. `connection_password_options` can be only one of the following:  
`password` |  `string` Optional. Input only. The password used to connect to the Oracle Goldengate in plain text.  
`passwordSecretVersion` |  `string` Optional. Input only. The resource name of a secret version in Secret Manager which contains the password used to connect to the Oracle Goldengate. Format: projects/{project}/secrets/{secret}/versions/{version}.  
  
## GoldengateGenericConnectionProperties

The properties of GoldengateGenericConnectionProperties.

JSON representation  
---  
      
    
    {
      "technologyType": string,
      "host": string
    }  
  
Fields  
---  
`technologyType` |  `string` Optional. The technology type.  
`host` |  `string` Optional. The host of the GenericConnection.  
  
## GoldengateGoogleCloudStorageConnectionProperties

The properties of GoldengateGoogleCloudStorageConnectionProperties.

JSON representation  
---  
      
    
    {
      "technologyType": string,
      "serviceAccountKeyFile": string
    }  
  
Fields  
---  
`technologyType` |  `string` Optional. The technology type.  
`serviceAccountKeyFile` |  `string` Optional. The base64 encoded content of the service account key file containing the credentials required to use Google Cloud Storage.  
  
## GoldengateGoogleBigQueryConnectionProperties

The properties of GoldengateGoogleBigQueryConnectionProperties.

JSON representation  
---  
      
    
    {
      "technologyType": string,
      "serviceAccountKeyFile": string
    }  
  
Fields  
---  
`technologyType` |  `string` Optional. The technology type.  
`serviceAccountKeyFile` |  `string` Optional. The base64 encoded content of the service account key file containing the credentials required to use Google BigQuery.  
  
## GoldengateMysqlConnectionProperties

Properties of GoldengateMysqlConnection.

JSON representation  
---  
      
    
    {
      "technologyType": string,
      "username": string,
      "host": string,
      "port": integer,
      "database": string,
      "securityProtocol": enum ([MysqlSecurityProtocol](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#MysqlSecurityProtocol)),
      "sslMode": enum ([SSLMode](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#SSLMode)),
      "sslCaFile": string,
      "sslCrlFile": string,
      "sslCertFile": string,
      "sslKeyFile": string,
      "additionalAttributes": [
        {
          object ([NameValuePair](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#NameValuePair))
        }
      ],
      "dbSystemId": string,
    
      // Union field connection_password_options can be only one of the following:
      "password": string,
      "passwordSecretVersion": string
      // End of list of possible types for union field connection_password_options.
    }  
  
Fields  
---  
`technologyType` |  `string` Optional. The technology type of MysqlConnection.  
`username` |  `string` Optional. The username Oracle Goldengate uses to connect the associated system of the given technology.  
`host` |  `string` Optional. The name or address of a host.  
`port` |  `integer` Optional. The port of an endpoint usually specified for a connection.  
`database` |  `string` Optional. The name of the database.  
`securityProtocol` |  `enum (`[MysqlSecurityProtocol](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#MysqlSecurityProtocol)`)` Optional. Security Type for MySQL.  
`sslMode` |  `enum (`[SSLMode](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#SSLMode)`)` Optional. SSL modes for MySQL.  
`sslCaFile` |  `string` Optional. Database Certificate - The base64 encoded content of a .pem or .crt file containing the server public key (for 1 and 2-way SSL).  
`sslCrlFile` |  `string` Optional. The base64 encoded list of certificates revoked by the trusted certificate authorities (Trusted CA).  
`sslCertFile` |  `string` Optional. Client Certificate - The base64 encoded content of a .pem or .crt file containing the client public key (for 2-way SSL).  
`sslKeyFile` |  `string` Optional. Client Key - The base64 encoded content of a .pem or .crt file containing the client private key (for 2-way SSL).  
`additionalAttributes[]` |  `object (`[NameValuePair](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#NameValuePair)`)` Optional. An array of name-value pair attribute entries. Used as additional parameters in connection string.  
`dbSystemId` |  `string` Optional. The OCID of the database system being referenced.  
Union field `connection_password_options`. The password Oracle Goldengate uses to connect the associated system of the given technology. It must conform to the specific security requirements including length, case sensitivity, and so on. `connection_password_options` can be only one of the following:  
`password` |  `string` Optional. Input only. The password Oracle Goldengate uses to connect to MySQL in plain text.  
`passwordSecretVersion` |  `string` Optional. Input only. The resource name of a secret version in Secret Manager which contains the password Oracle Goldengate uses to connect to MySQL. Format: projects/{project}/secrets/{secret}/versions/{version}.  
  
## MysqlSecurityProtocol

Enum for Security Type for MySQL.

Enums  
---  
`MYSQL_SECURITY_PROTOCOL_UNSPECIFIED` | Security type not specified.  
`PLAIN` | Plain text communication.  
`TLS` | Transport Layer Security.  
`MTLS` | Mutual Transport Layer Security.  
  
## SSLMode

Enum for SSL modes for MySQL.

Enums  
---  
`SSL_MODE_UNSPECIFIED` | SSL mode not specified.  
`DISABLED` | SSL is disabled.  
`PREFERRED` | SSL is preferred.  
`REQUIRED` | SSL is required.  
`VERIFY_CA` | SSL is required and certificate is verified.  
`VERIFY_IDENTITY` | SSL is required and certificate and hostname are verified.  
  
## NameValuePair

A name-value pair representing an attribute entry usable in a list of attributes.

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string` Required. The name of the property entry.  
`value` |  `string` Required. The value of the property entry.  
  
## GoldengateKafkaConnectionProperties

The properties of GoldengateKafkaConnection.

JSON representation  
---  
      
    
    {
      "technologyType": string,
      "streamPoolId": string,
      "clusterId": string,
      "bootstrapServers": [
        {
          object ([KafkaBootstrapServer](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#KafkaBootstrapServer))
        }
      ],
      "securityProtocol": enum ([KafkaSecurityProtocol](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#KafkaSecurityProtocol)),
      "username": string,
      "trustStoreFile": string,
      "keyStoreFile": string,
      "consumerPropertiesFile": string,
      "producerPropertiesFile": string,
      "useResourcePrincipal": boolean,
    
      // Union field connection_password_options can be only one of the following:
      "password": string,
      "passwordSecretVersion": string
      // End of list of possible types for union field connection_password_options.
    
      // Union field trust_store_password_options can be only one of the following:
      "trustStorePassword": string,
      "trustStorePasswordSecretVersion": string
      // End of list of possible types for union field trust_store_password_options.
    
      // Union field key_store_password_options can be only one of the following:
      "keyStorePassword": string,
      "keyStorePasswordSecretVersion": string
      // End of list of possible types for union field key_store_password_options.
    
      // Union field ssl_key_password_options can be only one of the following:
      "sslKeyPassword": string,
      "sslKeyPasswordSecretVersion": string
      // End of list of possible types for union field ssl_key_password_options.
    }  
  
Fields  
---  
`technologyType` |  `string` Optional. The technology type of KafkaConnection.  
`streamPoolId` |  `string` Optional. The OCID of the stream pool being referenced.  
`clusterId` |  `string` Optional. The OCID of the Kafka cluster being referenced from OCI Streaming with Apache Kafka.  
`bootstrapServers[]` |  `object (`[KafkaBootstrapServer](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#KafkaBootstrapServer)`)` Optional. Kafka bootstrap. Equivalent of bootstrap.servers configuration property in Kafka: list of KafkaBootstrapServer objects specified by host/port. Used for establishing the initial connection to the Kafka cluster. Example: "server1.example.com:9092,server2.example.com:9092"  
`securityProtocol` |  `enum (`[KafkaSecurityProtocol](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#KafkaSecurityProtocol)`)` Optional. Security Type for Kafka.  
`username` |  `string` Optional. The username Oracle Goldengate uses to connect the associated system of the given technology.  
`trustStoreFile` |  `string` Optional. The base64 encoded content of the TrustStore file.  
`keyStoreFile` |  `string` Optional. The base64 encoded content of the KeyStore file.  
`consumerPropertiesFile` |  `string` Optional. The base64 encoded content of the consumer.properties file.  
`producerPropertiesFile` |  `string` Optional. The base64 encoded content of the producer.properties file.  
`useResourcePrincipal` |  `boolean` Optional. Specifies that the user intends to authenticate to the instance using a resource principal. Applicable only for OCI Streaming connections.  
Union field `connection_password_options`. The password for Kafka basic/SASL auth. `connection_password_options` can be only one of the following:  
`password` |  `string` Optional. Input only. The password for Kafka basic/SASL auth in plain text.  
`passwordSecretVersion` |  `string` Optional. Input only. The resource name of a secret version in Secret Manager which contains the password for Kafka basic/SASL auth. Format: projects/{project}/secrets/{secret}/versions/{version}.  
Union field `trust_store_password_options`. The TrustStore password. `trust_store_password_options` can be only one of the following:  
`trustStorePassword` |  `string` Optional. Input only. The TrustStore password in plain text.  
`trustStorePasswordSecretVersion` |  `string` Optional. Input only. The resource name of a secret version in Secret Manager which contains the TrustStore password. Format: projects/{project}/secrets/{secret}/versions/{version}.  
Union field `key_store_password_options`. The KeyStore password. `key_store_password_options` can be only one of the following:  
`keyStorePassword` |  `string` Optional. Input only. The KeyStore password in plain text.  
`keyStorePasswordSecretVersion` |  `string` Optional. Input only. The resource name of a secret version in Secret Manager which contains the KeyStore password. Format: projects/{project}/secrets/{secret}/versions/{version}.  
Union field `ssl_key_password_options`. The password for the cert inside of the KeyStore. In case it differs from the KeyStore password, it should be provided. `ssl_key_password_options` can be only one of the following:  
`sslKeyPassword` |  `string` Optional. Input only. The password for the cert inside of the KeyStore in plain text.  
`sslKeyPasswordSecretVersion` |  `string` Optional. Input only. The resource name of a secret version in Secret Manager which contains the password for the cert inside of the KeyStore. Format: projects/{project}/secrets/{secret}/versions/{version}.  
  
## KafkaBootstrapServer

Represents a Kafka bootstrap server with host name, optional port defaults to 9092, and an optional private ip.

JSON representation  
---  
      
    
    {
      "host": string,
      "port": integer,
      "privateIpAddress": string
    }  
  
Fields  
---  
`host` |  `string` Required. The name or address of a host.  
`port` |  `integer` Optional. The port of an endpoint usually specified for a connection.  
`privateIpAddress` |  `string` Optional. The private IP address of the connection's endpoint in the customer's VCN, typically a database endpoint or a big data endpoint (e.g. Kafka bootstrap server). In case the privateIp is provided, the subnetId must also be provided. In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible. In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.  
  
## KafkaSecurityProtocol

Enum for Security Type for Kafka.

Enums  
---  
`KAFKA_SECURITY_PROTOCOL_UNSPECIFIED` | Security type not specified.  
`SSL` | SSL security protocol.  
`SASL_SSL` | SASL SSL security protocol.  
`PLAINTEXT` | Plaintext security protocol.  
`SASL_PLAINTEXT` | SASL Plaintext security protocol.  
  
## GoldengateKafkaSchemaRegistryConnectionProperties

The properties of GoldengateKafkaSchemaRegistryConnection.

JSON representation  
---  
      
    
    {
      "technologyType": string,
      "url": string,
      "authenticationType": enum ([AuthenticationType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#AuthenticationType)),
      "username": string,
      "trustStoreFile": string,
      "keyStoreFile": string,
    
      // Union field connection_password_options can be only one of the following:
      "password": string,
      "passwordSecretVersion": string
      // End of list of possible types for union field connection_password_options.
    
      // Union field trust_store_password_options can be only one of the following:
      "trustStorePassword": string,
      "trustStorePasswordSecretVersion": string
      // End of list of possible types for union field trust_store_password_options.
    
      // Union field key_store_password_options can be only one of the following:
      "keyStorePassword": string,
      "keyStorePasswordSecretVersion": string
      // End of list of possible types for union field key_store_password_options.
    
      // Union field ssl_key_password_options can be only one of the following:
      "sslKeyPassword": string,
      "sslKeyPasswordSecretVersion": string
      // End of list of possible types for union field ssl_key_password_options.
    }  
  
Fields  
---  
`technologyType` |  `string` Optional. The technology type of KafkaSchemaRegistryConnection.  
`url` |  `string` Optional. Kafka Schema Registry URL. e.g.: 'https://server1.us.oracle.com:8081'  
`authenticationType` |  `enum (`[AuthenticationType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#AuthenticationType)`)` Optional. Used authentication mechanism to access Schema Registry.  
`username` |  `string` Optional. The username to access Schema Registry using basic authentication. This value is injected into 'schema.registry.basic.auth.user.info=user:password' configuration property.  
`trustStoreFile` |  `string` Optional. The base64 encoded content of the TrustStore file.  
`keyStoreFile` |  `string` Optional. The base64 encoded content of the KeyStore file.  
Union field `connection_password_options`. The password to access Schema Registry using basic authentication. `connection_password_options` can be only one of the following:  
`password` |  `string` Optional. Input only. The password to access Schema Registry in plain text.  
`passwordSecretVersion` |  `string` Optional. Input only. The resource name of a secret version in Secret Manager which contains the password to access Schema Registry using basic authentication. Format: projects/{project}/secrets/{secret}/versions/{version}.  
Union field `trust_store_password_options`. The TrustStore password. `trust_store_password_options` can be only one of the following:  
`trustStorePassword` |  `string` Optional. Input only. The TrustStore password in plain text.  
`trustStorePasswordSecretVersion` |  `string` Optional. Input only. The resource name of a secret version in Secret Manager which contains the TrustStore password. Format: projects/{project}/secrets/{secret}/versions/{version}.  
Union field `key_store_password_options`. The KeyStore password. `key_store_password_options` can be only one of the following:  
`keyStorePassword` |  `string` Optional. Input only. The KeyStore password in plain text.  
`keyStorePasswordSecretVersion` |  `string` Optional. Input only. The resource name of a secret version in Secret Manager which contains the KeyStore password. Format: projects/{project}/secrets/{secret}/versions/{version}.  
Union field `ssl_key_password_options`. The password for the cert inside the KeyStore. `ssl_key_password_options` can be only one of the following:  
`sslKeyPassword` |  `string` Optional. Input only. The password for the cert inside the KeyStore in plain text.  
`sslKeyPasswordSecretVersion` |  `string` Optional. Input only. The resource name of a secret version in Secret Manager which contains the password for the cert inside the KeyStore. Format: projects/{project}/secrets/{secret}/versions/{version}.  
  
## AuthenticationType

Enum for authentication mechanism to access Schema Registry.

Enums  
---  
`AUTHENTICATION_TYPE_UNSPECIFIED` | Authentication type not specified.  
`NONE` | No authentication.  
`BASIC` | Basic authentication.  
`MUTUAL` | Mutual authentication.  
  
## GoldengateOciObjectStorageConnectionProperties

The properties of GoldengateOciObjectStorageConnection.

JSON representation  
---  
      
    
    {
      "technologyType": string,
      "tenancyId": string,
      "region": string,
      "userId": string,
      "privateKeyFile": string,
      "privateKeyPassphraseSecret": string,
      "publicKeyFingerprint": string,
      "useResourcePrincipal": boolean
    }  
  
Fields  
---  
`technologyType` |  `string` Optional. The technology type of OciObjectStorageConnection.  
`tenancyId` |  `string` Optional. The OCID of the related OCI tenancy.  
`region` |  `string` Optional. The name of the region of OCI Object Storage. e.g.: us-ashburn-1 If the region is not provided, backend will default to the default region.  
`userId` |  `string` Optional. The OCID of the OCI user who will access the Object Storage. The user must have write access to the bucket they want to connect to.  
`privateKeyFile` |  `string` Optional. The content of the private key file (PEM file) corresponding to the API key of the fingerprint.  
`privateKeyPassphraseSecret` |  `string` Optional. The passphrase of the private key.  
`publicKeyFingerprint` |  `string` Optional. The fingerprint of the API Key of the user specified by the userId.  
`useResourcePrincipal` |  `boolean` Optional. Specifies that the user intends to authenticate to the instance using a resource principal.  
  
## GoldengateAzureDataLakeStorageConnectionProperties

The properties of GoldengateAzureDataLakeStorageConnection.

JSON representation  
---  
      
    
    {
      "technologyType": string,
      "authenticationType": enum ([AuthenticationType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#AuthenticationType_1)),
      "account": string,
      "accountKeySecret": string,
      "sasTokenSecret": string,
      "azureTenantId": string,
      "clientId": string,
      "clientSecret": string,
      "endpoint": string,
      "azureAuthorityHost": string
    }  
  
Fields  
---  
`technologyType` |  `string` Optional. The technology type of AzureDataLakeStorageConnection.  
`authenticationType` |  `enum (`[AuthenticationType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#AuthenticationType_1)`)` Optional. Authentication mechanism to access Azure Data Lake Storage.  
`account` |  `string` Optional. Sets the Azure storage account name.  
`accountKeySecret` |  `string` Optional. Azure storage account key. This property is required when 'authenticationType' is set to 'SHARED_KEY'.  
`sasTokenSecret` |  `string` Optional. Credential that uses a shared access signature (SAS) to authenticate to an Azure Service.  
`azureTenantId` |  `string` Optional. Azure tenant ID of the application. This property is required when 'authenticationType' is set to 'AZURE_ACTIVE_DIRECTORY'.  
`clientId` |  `string` Optional. Azure client ID of the application. This property is required when 'authenticationType' is set to 'AZURE_ACTIVE_DIRECTORY'.  
`clientSecret` |  `string` Optional. Azure client secret (aka application password) for authentication.  
`endpoint` |  `string` Optional. Azure Storage service endpoint. e.g: <https://test.blob.core.windows.net>  
`azureAuthorityHost` |  `string` Optional. The endpoint used for authentication with Microsoft Entra ID (formerly Azure Active Directory). Default value: <https://login.microsoftonline.com>  
  
## AuthenticationType

Enum for authentication mechanism to access Azure Data Lake Storage.

Enums  
---  
`AUTHENTICATION_TYPE_UNSPECIFIED` | Authentication type not specified.  
`SHARED_KEY` | Shared key authentication.  
`SHARED_ACCESS_SIGNATURE` | Shared access signature authentication.  
`AZURE_ACTIVE_DIRECTORY` | Azure active directory authentication.  
  
## GoldengateAzureSynapseAnalyticsConnectionProperties

The properties of GoldengateAzureSynapseAnalyticsConnection.

JSON representation  
---  
      
    
    {
      "technologyType": string,
      "connectionString": string,
      "username": string,
    
      // Union field connection_password_options can be only one of the following:
      "password": string,
      "passwordSecretVersion": string
      // End of list of possible types for union field connection_password_options.
    }  
  
Fields  
---  
`technologyType` |  `string` Optional. The technology type of AzureSynapseAnalyticsConnection.  
`connectionString` |  `string` Optional. JDBC connection string. e.g.: 'jdbc:sqlserver://.sql.azuresynapse.net:1433;database=;encrypt=true;trustServerCertificate=false;hostNameInCertificate=*.sql.azuresynapse.net;loginTimeout=300;'  
`username` |  `string` Optional. The username Oracle Goldengate uses to connect the associated system of the given technology.  
Union field `connection_password_options`. The password Oracle Goldengate uses to connect the associated system of the given technology. `connection_password_options` can be only one of the following:  
`password` |  `string` Optional. Input only. The password Oracle Goldengate uses for Azure Synapse Analytics connection in plain text.  
`passwordSecretVersion` |  `string` Optional. Input only. The resource name of a secret version in Secret Manager which contains the password Oracle Goldengate uses for Azure Synapse Analytics connection. Format: projects/{project}/secrets/{secret}/versions/{version}.  
  
## GoldengatePostgresqlConnectionProperties

The properties of GoldengatePostgresqlConnection.

JSON representation  
---  
      
    
    {
      "technologyType": string,
      "database": string,
      "host": string,
      "port": integer,
      "username": string,
      "additionalAttributes": [
        {
          object ([NameValuePair](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#NameValuePair))
        }
      ],
      "securityProtocol": enum ([PostgresqlSecurityProtocol](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#PostgresqlSecurityProtocol)),
      "sslMode": enum ([PostgresqlSslMode](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#PostgresqlSslMode)),
      "sslCaFile": string,
      "sslCrlFile": string,
      "sslCertFile": string,
      "sslKeyFile": string,
      "dbSystemId": string,
    
      // Union field connection_password_options can be only one of the following:
      "password": string,
      "passwordSecretVersion": string
      // End of list of possible types for union field connection_password_options.
    }  
  
Fields  
---  
`technologyType` |  `string` Optional. The technology type of PostgresqlConnection.  
`database` |  `string` Optional. The name of the database.  
`host` |  `string` Optional. The name or address of a host.  
`port` |  `integer` Optional. The port of an endpoint usually specified for a connection.  
`username` |  `string` Optional. The username Oracle Goldengate uses to connect the associated system of the given technology.  
`additionalAttributes[]` |  `object (`[NameValuePair](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#NameValuePair)`)` Optional. An array of name-value pair attribute entries. Used as additional parameters in connection string.  
`securityProtocol` |  `enum (`[PostgresqlSecurityProtocol](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#PostgresqlSecurityProtocol)`)` Optional. Security protocol for PostgreSQL.  
`sslMode` |  `enum (`[PostgresqlSslMode](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#PostgresqlSslMode)`)` Optional. SSL modes for PostgreSQL.  
`sslCaFile` |  `string` Optional. The base64 encoded certificate of the trusted certificate authorities (Trusted CA) for PostgreSQL.  
`sslCrlFile` |  `string` Optional. The base64 encoded list of certificates revoked by the trusted certificate authorities (Trusted CA).  
`sslCertFile` |  `string` Optional. The base64 encoded certificate of the PostgreSQL server.  
`sslKeyFile` |  `string` Optional. The base64 encoded private key of the PostgreSQL server.  
`dbSystemId` |  `string` Optional. The OCID of the database system being referenced.  
Union field `connection_password_options`. The password Oracle Goldengate uses to connect the associated system of the given technology. `connection_password_options` can be only one of the following:  
`password` |  `string` Optional. Input only. The password Oracle Goldengate uses for PostgreSQL connection in plain text.  
`passwordSecretVersion` |  `string` Optional. Input only. The resource name of a secret version in Secret Manager which contains the password Oracle Goldengate uses for PostgreSQL connection. Format: projects/{project}/secrets/{secret}/versions/{version}.  
  
## PostgresqlSecurityProtocol

Enum for Security protocol for PostgreSQL.

Enums  
---  
`POSTGRESQL_SECURITY_PROTOCOL_UNSPECIFIED` | Security protocol not specified.  
`PLAIN` | Plain text communication.  
`TLS` | Transport Layer Security.  
`MTLS` | Mutual Transport Layer Security.  
  
## PostgresqlSslMode

Enum for SSL modes for PostgreSQL.

Enums  
---  
`POSTGRESQL_SSL_MODE_UNSPECIFIED` | SSL mode not specified.  
`PREFER` | Prefer SSL.  
`REQUIRE` | Require SSL.  
`VERIFY_CA` | Verify Certificate Authority.  
`VERIFY_FULL` | Verify Full.  
  
## GoldengateMicrosoftSqlserverConnectionProperties

The properties of GoldengateMicrosoftSqlserverConnection.

JSON representation  
---  
      
    
    {
      "technologyType": string,
      "database": string,
      "host": string,
      "port": integer,
      "username": string,
      "additionalAttributes": [
        {
          object ([NameValuePair](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#NameValuePair))
        }
      ],
      "securityProtocol": enum ([MicrosoftSqlserverSecurityProtocol](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#MicrosoftSqlserverSecurityProtocol)),
      "sslCaFile": string,
      "serverCertificateValidationRequired": boolean,
    
      // Union field connection_password_options can be only one of the following:
      "password": string,
      "passwordSecretVersion": string
      // End of list of possible types for union field connection_password_options.
    }  
  
Fields  
---  
`technologyType` |  `string` Optional. The technology type of MicrosoftSqlserverConnection.  
`database` |  `string` Optional. The name of the database.  
`host` |  `string` Optional. The name or address of a host.  
`port` |  `integer` Optional. The port of an endpoint usually specified for a connection.  
`username` |  `string` Optional. The username Oracle Goldengate uses to connect to the Microsoft SQL Server.  
`additionalAttributes[]` |  `object (`[NameValuePair](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#NameValuePair)`)` Optional. An array of name-value pair attribute entries. Used as additional parameters in connection string.  
`securityProtocol` |  `enum (`[MicrosoftSqlserverSecurityProtocol](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#MicrosoftSqlserverSecurityProtocol)`)` Optional. Security Type for Microsoft SQL Server.  
`sslCaFile` |  `string` Optional. Database Certificate - The base64 encoded content of a .pem or .crt file containing the server public key (for 1-way SSL).  
`serverCertificateValidationRequired` |  `boolean` Optional. If set to true, the driver validates the certificate that is sent by the database server.  
Union field `connection_password_options`. The password Oracle Goldengate uses to connect the associated Microsoft SQL Server. `connection_password_options` can be only one of the following:  
`password` |  `string` Optional. Input only. The password Oracle Goldengate uses for Microsoft SQL Server connection in plain text.  
`passwordSecretVersion` |  `string` Optional. Input only. The resource name of a secret version in Secret Manager which contains the password Oracle Goldengate uses for Microsoft SQL Server connection. Format: projects/{project}/secrets/{secret}/versions/{version}.  
  
## MicrosoftSqlserverSecurityProtocol

Enum for Security Type for Microsoft SQL Server.

Enums  
---  
`MICROSOFT_SQLSERVER_SECURITY_PROTOCOL_UNSPECIFIED` | Security type not specified.  
`PLAIN` | Plain text communication.  
`TLS` | Transport Layer Security.  
  
## GoldengateAmazonS3ConnectionProperties

The properties of GoldengateAmazonS3Connection.

JSON representation  
---  
      
    
    {
      "technologyType": string,
      "accessKeyId": string,
      "secretAccessKeySecret": string,
      "endpoint": string,
      "region": string
    }  
  
Fields  
---  
`technologyType` |  `string` Optional. The technology type of AmazonS3Connection.  
`accessKeyId` |  `string` Optional. Access key ID to access the Amazon S3 bucket.  
`secretAccessKeySecret` |  `string` Optional. Secret access key to access the Amazon S3 bucket.  
`endpoint` |  `string` Optional. The Amazon Endpoint for S3.  
`region` |  `string` Optional. The name of the AWS region where the bucket is created.  
  
## GoldengateHdfsConnectionProperties

The properties of GoldengateHdfsConnection.

JSON representation  
---  
      
    
    {
      "technologyType": string,
      "coreSiteXml": string
    }  
  
Fields  
---  
`technologyType` |  `string` Optional. The technology type of HdfsConnection.  
`coreSiteXml` |  `string` Optional. The content of the Hadoop Distributed File System configuration file (core-site.xml).  
  
## GoldengateJavaMessageServiceConnectionProperties

The properties of GoldengateJavaMessageServiceConnection.

JSON representation  
---  
      
    
    {
      "technologyType": string,
      "useJndi": boolean,
      "jndiConnectionFactory": string,
      "jndiProviderUrl": string,
      "jndiInitialContextFactory": string,
      "jndiSecurityPrincipal": string,
      "jndiSecurityCredentialsSecret": string,
      "connectionUrl": string,
      "connectionFactory": string,
      "username": string,
      "securityProtocol": enum ([JmsSecurityProtocol](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#JmsSecurityProtocol)),
      "authenticationType": enum ([JmsAuthenticationType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#JmsAuthenticationType)),
      "trustStoreFile": string,
      "keyStoreFile": string,
    
      // Union field connection_password_options can be only one of the following:
      "password": string,
      "passwordSecretVersion": string
      // End of list of possible types for union field connection_password_options.
    
      // Union field trust_store_password_options can be only one of the following:
      "trustStorePassword": string,
      "trustStorePasswordSecretVersion": string
      // End of list of possible types for union field trust_store_password_options.
    
      // Union field key_store_password_options can be only one of the following:
      "keyStorePassword": string,
      "keyStorePasswordSecretVersion": string
      // End of list of possible types for union field key_store_password_options.
    
      // Union field ssl_key_password_options can be only one of the following:
      "sslKeyPassword": string,
      "sslKeyPasswordSecretVersion": string
      // End of list of possible types for union field ssl_key_password_options.
    }  
  
Fields  
---  
`technologyType` |  `string` Optional. The technology type of JavaMessageServiceConnection.  
`useJndi` |  `boolean` Optional. If set to true, Java Naming and Directory Interface (JNDI) properties should be provided.  
`jndiConnectionFactory` |  `string` Optional. The Connection Factory can be looked up using this name. e.g.: 'ConnectionFactory'  
`jndiProviderUrl` |  `string` Optional. The URL that Java Message Service will use to contact the JNDI provider. e.g.: 'tcp://myjms.host.domain:61616?jms.prefetchPolicy.all=1000'  
`jndiInitialContextFactory` |  `string` Optional. The implementation of javax.naming.spi.InitialContextFactory interface used to obtain initial naming context.  
`jndiSecurityPrincipal` |  `string` Optional. Specifies the identity of the principal (user) to be authenticated.  
`jndiSecurityCredentialsSecret` |  `string` Optional. The password associated to the principal.  
`connectionUrl` |  `string` Optional. Connection URL of the Java Message Service, specifying the protocol, host, and port. e.g.: 'mq://myjms.host.domain:7676'  
`connectionFactory` |  `string` Optional. The Java class implementing javax.jms.ConnectionFactory interface supplied by the JMS provider.  
`username` |  `string` Optional. The username Oracle Goldengate uses to connect to the Java Message Service.  
`securityProtocol` |  `enum (`[JmsSecurityProtocol](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#JmsSecurityProtocol)`)` Optional. Security protocol for Java Message Service.  
`authenticationType` |  `enum (`[JmsAuthenticationType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#JmsAuthenticationType)`)` Optional. Authentication type for Java Message Service.  
`trustStoreFile` |  `string` Optional. The base64 encoded content of the TrustStore file.  
`keyStoreFile` |  `string` Optional. The base64 encoded content of the KeyStore file.  
Union field `connection_password_options`. The password Oracle Goldengate uses to connect the associated Java Message Service. `connection_password_options` can be only one of the following:  
`password` |  `string` Optional. Input only. The password Oracle Goldengate uses to connect the Java Message Service in plain text.  
`passwordSecretVersion` |  `string` Optional. Input only. The resource name of a secret version in Secret Manager which contains the password Oracle Goldengate uses to connect the associated Java Message Service. Format: projects/{project}/secrets/{secret}/versions/{version}.  
Union field `trust_store_password_options`. The TrustStore password. `trust_store_password_options` can be only one of the following:  
`trustStorePassword` |  `string` Optional. Input only. The TrustStore password in plain text.  
`trustStorePasswordSecretVersion` |  `string` Optional. Input only. The resource name of a secret version in Secret Manager which contains the TrustStore password. Format: projects/{project}/secrets/{secret}/versions/{version}.  
Union field `key_store_password_options`. The KeyStore password. `key_store_password_options` can be only one of the following:  
`keyStorePassword` |  `string` Optional. Input only. The KeyStore password in plain text.  
`keyStorePasswordSecretVersion` |  `string` Optional. Input only. The resource name of a secret version in Secret Manager which contains the KeyStore password. Format: projects/{project}/secrets/{secret}/versions/{version}.  
Union field `ssl_key_password_options`. The password for the cert inside of the KeyStore. In case it differs from the KeyStore password, it should be provided. `ssl_key_password_options` can be only one of the following:  
`sslKeyPassword` |  `string` Optional. Input only. The password for the cert inside of the KeyStore in plain text.  
`sslKeyPasswordSecretVersion` |  `string` Optional. Input only. The resource name of a secret version in Secret Manager which contains the password for the cert inside of the KeyStore. Format: projects/{project}/secrets/{secret}/versions/{version}.  
  
## JmsSecurityProtocol

Enum for Security protocol for Java Message Service.

Enums  
---  
`JMS_SECURITY_PROTOCOL_UNSPECIFIED` | Security protocol not specified.  
`PLAIN` | Plain text communication.  
`TLS` | Transport Layer Security.  
`MTLS` | Mutual Transport Layer Security.  
  
## JmsAuthenticationType

Enum for Authentication type for Java Message Service.

Enums  
---  
`JMS_AUTHENTICATION_TYPE_UNSPECIFIED` | Authentication type not specified.  
`NONE` | No authentication.  
`BASIC` | Basic authentication.  
  
## GoldengateMongodbConnectionProperties

The properties of GoldengateMongodbConnection.

JSON representation  
---  
      
    
    {
      "technologyType": string,
      "connectionString": string,
      "username": string,
      "databaseId": string,
      "securityProtocol": enum ([MongodbSecurityProtocol](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#MongodbSecurityProtocol)),
      "tlsCaFile": string,
      "tlsCertificateKeyFile": string,
    
      // Union field connection_password_options can be only one of the following:
      "password": string,
      "passwordSecretVersion": string
      // End of list of possible types for union field connection_password_options.
    
      // Union field tls_certificate_key_file_password_options can be only one of the
      // following:
      "tlsCertificateKeyFilePassword": string,
      "tlsCertificateKeyFilePasswordSecretVersion": string
      // End of list of possible types for union field
      // tls_certificate_key_file_password_options.
    }  
  
Fields  
---  
`technologyType` |  `string` Optional. The technology type of MongodbConnection.  
`connectionString` |  `string` Optional. MongoDB connection string. e.g.: 'mongodb://mongodb0.example.com:27017/recordsrecords'  
`username` |  `string` Optional. The username Oracle Goldengate uses to connect to the database.  
`databaseId` |  `string` Optional. The OCID of the Oracle Autonomous Json Database.  
`securityProtocol` |  `enum (`[MongodbSecurityProtocol](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#MongodbSecurityProtocol)`)` Optional. Security Type for MongoDB.  
`tlsCaFile` |  `string` Optional. Database Certificate - The base64 encoded content of a .pem file, containing the server public key (for 1 and 2-way SSL).  
`tlsCertificateKeyFile` |  `string` Optional. Client Certificate - The base64 encoded content of a .pem file, containing the client public key (for 2-way SSL).  
Union field `connection_password_options`. The password Oracle Goldengate uses to connect the associated database. `connection_password_options` can be only one of the following:  
`password` |  `string` Optional. Input only. The password Oracle Goldengate uses to connect the Mongodb connection in plain text.  
`passwordSecretVersion` |  `string` Optional. Input only. The resource name of a secret version in Secret Manager which contains the password Oracle Goldengate uses to connect the Mongodb connection. Format: projects/{project}/secrets/{secret}/versions/{version}.  
Union field `tls_certificate_key_file_password_options`. Client Certificate key file password. `tls_certificate_key_file_password_options` can be only one of the following:  
`tlsCertificateKeyFilePassword` |  `string` Optional. Input only. The Client Certificate key file password in plain text.  
`tlsCertificateKeyFilePasswordSecretVersion` |  `string` Optional. Input only. The resource name of a secret version in Secret Manager which contains the Client Certificate key file password in Secret Manager. Format: projects/{project}/secrets/{secret}/versions/{version}.  
  
## MongodbSecurityProtocol

Enum for Security Type for MongoDB.

Enums  
---  
`MONGODB_SECURITY_PROTOCOL_UNSPECIFIED` | Security type not specified.  
`PLAIN` | Plain text communication.  
`TLS` | Transport Layer Security.  
`MTLS` | Mutual Transport Layer Security.  
  
## GoldengateOracleNosqlConnectionProperties

The properties of GoldengateOracleNosqlConnection.

JSON representation  
---  
      
    
    {
      "technologyType": string,
      "tenancyId": string,
      "region": string,
      "userId": string,
      "privateKeyFile": string,
      "privateKeyPassphraseSecret": string,
      "publicKeyFingerprint": string,
      "useResourcePrincipal": boolean
    }  
  
Fields  
---  
`technologyType` |  `string` Optional. The technology type of OracleNosqlConnection.  
`tenancyId` |  `string` Optional. The OCID of the OCI tenancy.  
`region` |  `string` Optional. The name of the region. e.g.: us-ashburn-1  
`userId` |  `string` Optional. The OCID of the OCI user who will access the Oracle NoSQL database.  
`privateKeyFile` |  `string` Optional. The content of the private key file (PEM file) corresponding to the API key of the fingerprint.  
`privateKeyPassphraseSecret` |  `string` Optional. The passphrase of the private key.  
`publicKeyFingerprint` |  `string` Optional. The fingerprint of the API Key of the user specified by the userId.  
`useResourcePrincipal` |  `boolean` Optional. Specifies that the user intends to authenticate to the instance using a resource principal.  
  
## GoldengateSnowflakeConnectionProperties

The properties of GoldengateSnowflakeConnection.

JSON representation  
---  
      
    
    {
      "technologyType": string,
      "connectionUrl": string,
      "authenticationType": enum ([AuthenticationType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#AuthenticationType_2)),
      "username": string,
      "privateKeyFile": string,
      "privateKeyPassphraseSecret": string,
    
      // Union field connection_password_options can be only one of the following:
      "password": string,
      "passwordSecretVersion": string
      // End of list of possible types for union field connection_password_options.
    }  
  
Fields  
---  
`technologyType` |  `string` Optional. The technology type of SnowflakeConnection.  
`connectionUrl` |  `string` Optional. JDBC connection URL. e.g.: 'jdbc:snowflake://.snowflakecomputing.com/?warehouse=&db='  
`authenticationType` |  `enum (`[AuthenticationType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#AuthenticationType_2)`)` Optional. Used authentication mechanism to access Snowflake.  
`username` |  `string` Optional. The username Oracle Goldengate uses to connect to Snowflake.  
`privateKeyFile` |  `string` Optional. The content of private key file in PEM format.  
`privateKeyPassphraseSecret` |  `string` Optional. Password if the private key file is encrypted.  
Union field `connection_password_options`. The password Oracle Goldengate uses to connect to Snowflake platform. `connection_password_options` can be only one of the following:  
`password` |  `string` Optional. Input only. The password Oracle Goldengate uses to connect to Snowflake platform in plain text.  
`passwordSecretVersion` |  `string` Optional. Input only. The resource name of a secret version in Secret Manager which contains the password Oracle Goldengate uses to connect to Snowflake platform. Format: projects/{project}/secrets/{secret}/versions/{version}.  
  
## AuthenticationType

Enum for authentication mechanism to access Snowflake.

Enums  
---  
`AUTHENTICATION_TYPE_UNSPECIFIED` | Authentication type not specified.  
`BASIC` | Basic authentication.  
`KEY_PAIR` | Key pair authentication.  
  
## GoldengateAmazonRedshiftConnectionProperties

The properties of GoldengateAmazonRedshiftConnection.

JSON representation  
---  
      
    
    {
      "technologyType": string,
      "connectionUrl": string,
      "username": string,
    
      // Union field connection_password_options can be only one of the following:
      "password": string,
      "passwordSecretVersion": string
      // End of list of possible types for union field connection_password_options.
    }  
  
Fields  
---  
`technologyType` |  `string` Optional. The technology type of AmazonRedshiftConnection.  
`connectionUrl` |  `string` Optional. Connection URL. e.g.: 'jdbc:<redshift://aws-redshift-instance.aaaaaaaaaaaa.us-east-2.redshift.amazonaws.com:5439/mydb>'  
`username` |  `string` Optional. The username Oracle Goldengate uses to connect the associated system of the given technology.  
Union field `connection_password_options`. The password Oracle Goldengate uses to connect the associated system of the given technology. `connection_password_options` can be only one of the following:  
`password` |  `string` Optional. Input only. The password Oracle Goldengate uses for Amazon Redshift connection in plain text.  
`passwordSecretVersion` |  `string` Optional. Input only. The resource name of a secret version in Secret Manager which contains the password Oracle Goldengate uses for Amazon Redshift connection. Format: projects/{project}/secrets/{secret}/versions/{version}.  
  
## GoldengateElasticsearchConnectionProperties

The properties of GoldengateElasticsearchConnection.

JSON representation  
---  
      
    
    {
      "technologyType": string,
      "servers": string,
      "securityProtocol": enum ([ElasticsearchSecurityProtocol](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#ElasticsearchSecurityProtocol)),
      "authenticationType": enum ([ElasticsearchAuthenticationType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#ElasticsearchAuthenticationType)),
      "username": string,
      "fingerprint": string,
    
      // Union field connection_password_options can be only one of the following:
      "password": string,
      "passwordSecretVersion": string
      // End of list of possible types for union field connection_password_options.
    }  
  
Fields  
---  
`technologyType` |  `string` Optional. The technology type of ElasticsearchConnection.  
`servers` |  `string` Optional. Comma separated list of Elasticsearch server addresses, specified as host:port entries, where :port is optional. If port is not specified, it defaults to 9200. Example: "server1.example.com:4000,server2.example.com:4000"  
`securityProtocol` |  `enum (`[ElasticsearchSecurityProtocol](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#ElasticsearchSecurityProtocol)`)` Optional. Security protocol for Elasticsearch.  
`authenticationType` |  `enum (`[ElasticsearchAuthenticationType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#ElasticsearchAuthenticationType)`)` Optional. Authentication type for Elasticsearch.  
`username` |  `string` Optional. The username Oracle Goldengate uses to connect the associated system of the given technology.  
`fingerprint` |  `string` Optional. Fingerprint required by TLS security protocol. Eg.: '6152b2dfbff200f973c5074a5b91d06ab3b472c07c09a1ea57bb7fd406cdce9c'  
Union field `connection_password_options`. The password Oracle Goldengate uses to connect the associated system of the given technology. `connection_password_options` can be only one of the following:  
`password` |  `string` Optional. Input only. The password Oracle Goldengate uses for Elastic Search connection in plain text.  
`passwordSecretVersion` |  `string` Optional. Input only. The resource name of a secret version in Secret Manager which contains the password Oracle Goldengate uses for Elastic Search connection. Format: projects/{project}/secrets/{secret}/versions/{version}.  
  
## ElasticsearchSecurityProtocol

Enum for Security protocol for Elasticsearch.

Enums  
---  
`ELASTICSEARCH_SECURITY_PROTOCOL_UNSPECIFIED` | Security protocol not specified.  
`PLAIN` | Plain text communication.  
`TLS` | Transport Layer Security.  
  
## ElasticsearchAuthenticationType

Enum for Authentication type for Elasticsearch.

Enums  
---  
`ELASTICSEARCH_AUTHENTICATION_TYPE_UNSPECIFIED` | Authentication type not specified.  
`NONE` | No authentication.  
`BASIC` | Basic authentication.  
  
## GoldengateAmazonKinesisConnectionProperties

The properties of GoldengateAmazonKinesisConnection.

JSON representation  
---  
      
    
    {
      "technologyType": string,
      "accessKeyId": string,
      "secretAccessKeySecret": string,
      "endpoint": string,
      "awsRegion": string
    }  
  
Fields  
---  
`technologyType` |  `string` Optional. The technology type of AmazonKinesisConnection.  
`accessKeyId` |  `string` Optional. Access key ID to access the Amazon Kinesis.  
`secretAccessKeySecret` |  `string` Optional. Secret access key to access the Amazon Kinesis.  
`endpoint` |  `string` Optional. The endpoint URL of the Amazon Kinesis service. e.g.: 'https://kinesis.us-east-1.amazonaws.com' If not provided, Goldengate will default to 'https://kinesis..amazonaws.com'.  
`awsRegion` |  `string` Optional. The name of the AWS region. If not provided, Goldengate will default to 'us-west-1'.  
  
## GoldengateDb2ConnectionProperties

The properties of GoldengateDb2Connection.

JSON representation  
---  
      
    
    {
      "technologyType": string,
      "host": string,
      "port": integer,
      "database": string,
      "username": string,
      "securityProtocol": enum ([Db2SecurityProtocol](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#Db2SecurityProtocol)),
      "additionalAttributes": [
        {
          object ([NameValuePair](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#NameValuePair))
        }
      ],
      "sslClientKeystoredbFile": string,
      "sslClientKeystashFile": string,
      "sslServerCertificateFile": string,
    
      // Union field connection_password_options can be only one of the following:
      "password": string,
      "passwordSecretVersion": string
      // End of list of possible types for union field connection_password_options.
    }  
  
Fields  
---  
`technologyType` |  `string` Optional. The technology type of Db2Connection.  
`host` |  `string` Optional. The name or address of a host.  
`port` |  `integer` Optional. The port of an endpoint usually specified for a connection.  
`database` |  `string` Optional. The name of the database.  
`username` |  `string` Optional. The username Oracle Goldengate uses to connect to the DB2 database.  
`securityProtocol` |  `enum (`[Db2SecurityProtocol](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#Db2SecurityProtocol)`)` Optional. Security protocol for the DB2 database.  
`additionalAttributes[]` |  `object (`[NameValuePair](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#NameValuePair)`)` Optional. An array of name-value pair attribute entries. Used as additional parameters in connection string.  
`sslClientKeystoredbFile` |  `string` Optional. The keystore file created at the client containing the server certificate / CA root certificate. Not supported for IBM Db2 for i.  
`sslClientKeystashFile` |  `string` Optional. The keystash file which contains the encrypted password to the key database file. Not supported for IBM Db2 for i.  
`sslServerCertificateFile` |  `string` Optional. The file which contains the self-signed server certificate / Certificate Authority (CA) certificate.  
Union field `connection_password_options`. The password Oracle Goldengate uses to connect to the associated DB2 database. `connection_password_options` can be only one of the following:  
`password` |  `string` Optional. Input only. The password Oracle Goldengate uses for Db2 connection in plain text.  
`passwordSecretVersion` |  `string` Optional. Input only. The resource name of a secret version in Secret Manager which contains the password Oracle Goldengate uses for Db2 connection. Format: projects/{project}/secrets/{secret}/versions/{version}.  
  
## Db2SecurityProtocol

Enum for Security protocol for the DB2 database.

Enums  
---  
`DB2_SECURITY_PROTOCOL_UNSPECIFIED` | Security protocol not specified.  
`PLAIN` | Plain text communication.  
`TLS` | Transport Layer Security.  
  
## GoldengateRedisConnectionProperties

The properties of GoldengateRedisConnection.

JSON representation  
---  
      
    
    {
      "technologyType": string,
      "servers": string,
      "securityProtocol": enum ([RedisSecurityProtocol](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#RedisSecurityProtocol)),
      "authenticationType": enum ([RedisAuthenticationType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#RedisAuthenticationType)),
      "username": string,
      "redisClusterId": string,
      "trustStoreFile": string,
      "keyStoreFile": string,
    
      // Union field connection_password_options can be only one of the following:
      "password": string,
      "passwordSecretVersion": string
      // End of list of possible types for union field connection_password_options.
    
      // Union field trust_store_password_options can be only one of the following:
      "trustStorePassword": string,
      "trustStorePasswordSecretVersion": string
      // End of list of possible types for union field trust_store_password_options.
    
      // Union field key_store_password_options can be only one of the following:
      "keyStorePassword": string,
      "keyStorePasswordSecretVersion": string
      // End of list of possible types for union field key_store_password_options.
    }  
  
Fields  
---  
`technologyType` |  `string` Optional. The technology type of RedisConnection.  
`servers` |  `string` Optional. Comma separated list of Redis server addresses, specified as host:port entries, where :port is optional. If port is not specified, it defaults to 6379. Example: "server1.example.com:6379,server2.example.com:6379"  
`securityProtocol` |  `enum (`[RedisSecurityProtocol](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#RedisSecurityProtocol)`)` Optional. Security protocol for Redis.  
`authenticationType` |  `enum (`[RedisAuthenticationType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#RedisAuthenticationType)`)` Optional. Authentication type for Redis.  
`username` |  `string` Optional. The username Oracle Goldengate uses to connect the associated system of the given technology.  
`redisClusterId` |  `string` Optional. The OCID of the Redis cluster.  
`trustStoreFile` |  `string` Optional. The base64 encoded content of the TrustStore file.  
`keyStoreFile` |  `string` Optional. The base64 encoded content of the KeyStore file.  
Union field `connection_password_options`. The password Oracle Goldengate uses to connect the associated system of the given technology. `connection_password_options` can be only one of the following:  
`password` |  `string` Optional. Input only. The password Oracle Goldengate uses for Redis connection in plain text.  
`passwordSecretVersion` |  `string` Optional. Input only. The resource name of a secret version in Secret Manager which contains the password Oracle Goldengate uses for Redis connection. Format: projects/{project}/secrets/{secret}/versions/{version}.  
Union field `trust_store_password_options`. The TrustStore password. `trust_store_password_options` can be only one of the following:  
`trustStorePassword` |  `string` Optional. Input only. The TrustStore password in plain text.  
`trustStorePasswordSecretVersion` |  `string` Optional. Input only. The resource name of a secret version in Secret Manager which contains the TrustStore password. Format: projects/{project}/secrets/{secret}/versions/{version}.  
Union field `key_store_password_options`. The KeyStore password. `key_store_password_options` can be only one of the following:  
`keyStorePassword` |  `string` Optional. Input only. The KeyStore password in plain text.  
`keyStorePasswordSecretVersion` |  `string` Optional. Input only. The resource name of a secret version in Secret Manager which contains the KeyStore password. Format: projects/{project}/secrets/{secret}/versions/{version}.  
  
## RedisSecurityProtocol

Enum for Security protocol for Redis.

Enums  
---  
`REDIS_SECURITY_PROTOCOL_UNSPECIFIED` | Security protocol not specified.  
`PLAIN` | Plain text communication.  
`TLS` | Transport Layer Security.  
`MTLS` | Mutual Transport Layer Security.  
  
## RedisAuthenticationType

Enum for Authentication type for Redis.

Enums  
---  
`REDIS_AUTHENTICATION_TYPE_UNSPECIFIED` | Authentication type not specified.  
`NONE` | No authentication.  
`BASIC` | Basic authentication.  
  
## GoldengateDatabricksConnectionProperties

The properties of GoldengateDatabricksConnection.

JSON representation  
---  
      
    
    {
      "technologyType": string,
      "authenticationType": enum ([DatabricksAuthenticationType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#DatabricksAuthenticationType)),
      "connectionUrl": string,
      "clientId": string,
      "clientSecret": string,
      "storageCredential": string,
    
      // Union field connection_password_options can be only one of the following:
      "password": string,
      "passwordSecretVersion": string
      // End of list of possible types for union field connection_password_options.
    }  
  
Fields  
---  
`technologyType` |  `string` Optional. The technology type of DatabricksConnection.  
`authenticationType` |  `enum (`[DatabricksAuthenticationType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#DatabricksAuthenticationType)`)` Optional. Authentication type for Databricks.  
`connectionUrl` |  `string` Optional. Connection URL. e.g.: 'jdbc:<databricks://adb-33934.4.azuredatabricks.net:443/default;transportMode=http;ssl=1;httpPath=sql/protocolv1/o/3393########44/0##3-7-hlrb>'  
`clientId` |  `string` Optional. OAuth client id, only applicable for authenticationType == OAUTH_M2M  
`clientSecret` |  `string` Optional. OAuth client secret, only applicable for authenticationType == OAUTH_M2M  
`storageCredential` |  `string` Optional. External storage credential name to access files on object storage such as ADLS Gen2, S3 or Cloud Storage.  
Union field `connection_password_options`. The password used to connect to Databricks. Only applicable for authentication_type == PERSONAL_ACCESS_TOKEN. `connection_password_options` can be only one of the following:  
`password` |  `string` Optional. Input only. The password used to connect to Databricks in plain text.  
`passwordSecretVersion` |  `string` Optional. Input only. The resource name of a secret version in Secret Manager which contains the password used to connect to Databricks. Format: projects/{project}/secrets/{secret}/versions/{version}.  
  
## DatabricksAuthenticationType

Enum for authentication type for Databricks.

Enums  
---  
`DATABRICKS_AUTHENTICATION_TYPE_UNSPECIFIED` | Authentication type not specified.  
`PERSONAL_ACCESS_TOKEN` | Personal access token authentication.  
`OAUTH_M2M` | OAuth M2M authentication.  
  
## GoldengateGooglePubsubConnectionProperties

The properties of GoldengateGooglePubsubConnection.

JSON representation  
---  
      
    
    {
      "technologyType": string,
      "serviceAccountKeyFile": string
    }  
  
Fields  
---  
`technologyType` |  `string` Optional. The technology type of GooglePubsubConnection.  
`serviceAccountKeyFile` |  `string` Optional. The base64 encoded content of the service account key file containing the credentials required to use Google Pub/Sub.  
  
## GoldengateMicrosoftFabricConnectionProperties

The properties of GoldengateMicrosoftFabricConnection.

JSON representation  
---  
      
    
    {
      "technologyType": string,
      "tenantId": string,
      "clientId": string,
      "clientSecret": string,
      "endpoint": string
    }  
  
Fields  
---  
`technologyType` |  `string` Optional. The technology type of MicrosoftFabricConnection.  
`tenantId` |  `string` Optional. Azure tenant ID of the application.  
`clientId` |  `string` Optional. Azure client ID of the application.  
`clientSecret` |  `string` Optional. Client secret associated with the client id.  
`endpoint` |  `string` Optional. Optional Microsoft Fabric service endpoint. Default value: <https://onelake.dfs.fabric.microsoft.com>  
  
## GoldengateOracleAIDataPlatformConnectionProperties

The properties of GoldengateOracleAIDataPlatformConnection.

JSON representation  
---  
      
    
    {
      "technologyType": string,
      "connectionUrl": string,
      "tenancyId": string,
      "region": string,
      "userId": string,
      "privateKeyFile": string,
      "privateKeyPassphraseSecret": string,
      "publicKeyFingerprint": string,
      "useResourcePrincipal": boolean
    }  
  
Fields  
---  
`technologyType` |  `string` Optional. The technology type of OracleAiDataPlatformConnection.  
`connectionUrl` |  `string` Optional. Connection URL. It must start with 'jdbc:spark://'  
`tenancyId` |  `string` Optional. The OCID of the related OCI tenancy.  
`region` |  `string` Optional. The name of the region. e.g.: us-ashburn-1  
`userId` |  `string` Optional. The OCID of the OCI user who will access.  
`privateKeyFile` |  `string` Optional. The content of the private key file (PEM file) corresponding to the API key of the fingerprint.  
`privateKeyPassphraseSecret` |  `string` Optional. The passphrase of the private key.  
`publicKeyFingerprint` |  `string` Optional. The fingerprint of the API Key of the user specified by the userId.  
`useResourcePrincipal` |  `boolean` Optional. Specifies that the user intends to authenticate to the instance using a resource principal.  
  
## GoldengateIcebergConnectionProperties

The properties of GoldengateIcebergConnection.

JSON representation  
---  
      
    
    {
      "technologyType": string,
      "catalog": {
        object ([IcebergCatalog](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#IcebergCatalog))
      },
      "storage": {
        object ([IcebergStorage](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#IcebergStorage))
      }
    }  
  
Fields  
---  
`technologyType` |  `string` Required. The technology type of Iceberg connection.  
`catalog` |  `object (`[IcebergCatalog](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#IcebergCatalog)`)` Required. The Iceberg catalog.  
`storage` |  `object (`[IcebergStorage](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#IcebergStorage)`)` Required. The Iceberg storage.  
  
## IcebergCatalog

The Iceberg catalog details.

JSON representation  
---  
      
    
    {
      "catalogType": enum ([CatalogType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#CatalogType)),
    
      // Union field catalog_details can be only one of the following:
      "glueIcebergCatalog": {
        object ([GlueIcebergCatalog](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GlueIcebergCatalog))
      },
      "nessieIcebergCatalog": {
        object ([NessieIcebergCatalog](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#NessieIcebergCatalog))
      },
      "polarisIcebergCatalog": {
        object ([PolarisIcebergCatalog](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#PolarisIcebergCatalog))
      },
      "restIcebergCatalog": {
        object ([RestIcebergCatalog](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#RestIcebergCatalog))
      }
      // End of list of possible types for union field catalog_details.
    }  
  
Fields  
---  
`catalogType` |  `enum (`[CatalogType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#CatalogType)`)` Required. The type of Iceberg catalog.  
Union field `catalog_details`. The type of Iceberg catalog. `catalog_details` can be only one of the following:  
`glueIcebergCatalog` |  `object (`[GlueIcebergCatalog](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GlueIcebergCatalog)`)` The Glue Iceberg catalog.  
`nessieIcebergCatalog` |  `object (`[NessieIcebergCatalog](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#NessieIcebergCatalog)`)` The Nessie Iceberg catalog.  
`polarisIcebergCatalog` |  `object (`[PolarisIcebergCatalog](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#PolarisIcebergCatalog)`)` The Polaris Iceberg catalog.  
`restIcebergCatalog` |  `object (`[RestIcebergCatalog](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#RestIcebergCatalog)`)` The REST Iceberg catalog.  
  
## GlueIcebergCatalog

The Glue Iceberg catalog.

JSON representation  
---  
      
    
    {
      "glueId": string
    }  
  
Fields  
---  
`glueId` |  `string` Required. The catalog ID of Glue.  
  
## NessieIcebergCatalog

The Nessie Iceberg catalog.

JSON representation  
---  
      
    
    {
      "uri": string,
      "branch": string
    }  
  
Fields  
---  
`uri` |  `string` Required. The Nessie uri.  
`branch` |  `string` Required. The Nessie branch.  
  
## PolarisIcebergCatalog

The Polaris Iceberg catalog.

JSON representation  
---  
      
    
    {
      "uri": string,
      "polarisCatalog": string,
      "clientId": string,
      "principalRole": string,
      "clientSecret": string
    }  
  
Fields  
---  
`uri` |  `string` Required. The Polaris uri.  
`polarisCatalog` |  `string` Required. The catalog name within Polaris.  
`clientId` |  `string` Required. The Polaris client ID.  
`principalRole` |  `string` Required. The Polaris principal role.  
`clientSecret` |  `string` Optional. The Polaris client secret.  
  
## RestIcebergCatalog

The REST Iceberg catalog.

JSON representation  
---  
      
    
    {
      "uri": string,
      "properties": string
    }  
  
Fields  
---  
`uri` |  `string` Required. The REST uri.  
`properties` |  `string` Optional. The base64 encoded content of the configuration file containing additional properties for the REST catalog.  
  
## CatalogType

The type of Iceberg catalog.

Enums  
---  
`CATALOG_TYPE_UNSPECIFIED` | Catalog type not specified.  
`GLUE` | Glue catalog.  
`HADOOP` | Hadoop catalog.  
`NESSIE` | Nessie catalog.  
`POLARIS` | Polaris catalog.  
`REST` | REST catalog.  
  
## IcebergStorage

The Iceberg storage details.

JSON representation  
---  
      
    
    {
      "storageType": enum ([StorageType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#StorageType)),
    
      // Union field storage_details can be only one of the following:
      "amazonS3IcebergStorage": {
        object ([AmazonS3IcebergStorage](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#AmazonS3IcebergStorage))
      },
      "googleCloudStorageIcebergStorage": {
        object ([GoogleCloudStorageIcebergStorage](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoogleCloudStorageIcebergStorage))
      },
      "azureDataLakeStorageIcebergStorage": {
        object ([AzureDataLakeStorageIcebergStorage](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#AzureDataLakeStorageIcebergStorage))
      }
      // End of list of possible types for union field storage_details.
    }  
  
Fields  
---  
`storageType` |  `enum (`[StorageType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#StorageType)`)` Required. The type of Iceberg storage.  
Union field `storage_details`. The type of Iceberg storage. `storage_details` can be only one of the following:  
`amazonS3IcebergStorage` |  `object (`[AmazonS3IcebergStorage](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#AmazonS3IcebergStorage)`)` The Amazon S3 Iceberg storage.  
`googleCloudStorageIcebergStorage` |  `object (`[GoogleCloudStorageIcebergStorage](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#GoogleCloudStorageIcebergStorage)`)` The Google Cloud Storage Iceberg storage.  
`azureDataLakeStorageIcebergStorage` |  `object (`[AzureDataLakeStorageIcebergStorage](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#AzureDataLakeStorageIcebergStorage)`)` The Azure Data Lake Storage Iceberg storage.  
  
## AmazonS3IcebergStorage

The Amazon S3 Iceberg storage.

JSON representation  
---  
      
    
    {
      "schemeType": enum ([SchemeType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#SchemeType)),
      "accessKeyId": string,
      "region": string,
      "bucket": string,
      "endpoint": string,
      "secretAccessKeySecret": string
    }  
  
Fields  
---  
`schemeType` |  `enum (`[SchemeType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections#SchemeType)`)` Required. The scheme type of Amazon S3.  
`accessKeyId` |  `string` Required. The access key ID of Amazon S3.  
`region` |  `string` Required. The region of Amazon S3.  
`bucket` |  `string` Required. The bucket of Amazon S3.  
`endpoint` |  `string` Optional. The endpoint of Amazon S3.  
`secretAccessKeySecret` |  `string` Optional. The secret access key of Amazon S3.  
  
## SchemeType

Enum for scheme type of Amazon S3.

Enums  
---  
`SCHEME_TYPE_UNSPECIFIED` | Scheme type not specified.  
`S3` | S3 scheme.  
`S3A` | S3A scheme.  
  
## GoogleCloudStorageIcebergStorage

The Google Cloud Storage Iceberg storage.

JSON representation  
---  
      
    
    {
      "bucket": string,
      "projectId": string,
      "serviceAccountKeyFile": string
    }  
  
Fields  
---  
`bucket` |  `string` Required. The bucket of Google Cloud Storage.  
`projectId` |  `string` Required. The project ID of Google Cloud Storage.  
`serviceAccountKeyFile` |  `string` Optional. The base64 encoded content of the service account key file of Google Cloud Storage.  
  
## AzureDataLakeStorageIcebergStorage

The Azure Data Lake Storage Iceberg storage.

JSON representation  
---  
      
    
    {
      "azureAccount": string,
      "container": string,
      "accountKeySecret": string,
      "endpoint": string
    }  
  
Fields  
---  
`azureAccount` |  `string` Required. The account of Azure Data Lake Storage.  
`container` |  `string` Required. The container of Azure Data Lake Storage.  
`accountKeySecret` |  `string` Optional. The account key of Azure Data Lake Storage.  
`endpoint` |  `string` Optional. The endpoint of Azure Data Lake Storage.  
  
## StorageType

The type of Iceberg storage.

Enums  
---  
`STORAGE_TYPE_UNSPECIFIED` | Storage type not specified.  
`AMAZON_S3` | Amazon S3 storage.  
`GOOGLE_CLOUD_STORAGE` | Google Cloud Storage storage.  
`AZURE_DATA_LAKE_STORAGE` | Azure Data Lake Storage storage.  
  
## GoldengateConnectionType

Enum for Connection type.

Enums  
---  
`GOLDENGATE_CONNECTION_TYPE_UNSPECIFIED` | Connection type unspecified.  
`GOLDENGATE` | Goldengate connection type.  
`KAFKA` | Kafka connection type.  
`KAFKA_SCHEMA_REGISTRY` | Kafka schema registry connection type.  
`MYSQL` | MySQL connection type.  
`JAVA_MESSAGE_SERVICE` | Java message service connection type.  
`MICROSOFT_SQLSERVER` | Microsoft SQL Server connection type.  
`OCI_OBJECT_STORAGE` | OCI object storage connection type.  
`ORACLE` | Oracle connection type.  
`AZURE_DATA_LAKE_STORAGE` | Azure data lake storage connection type.  
`POSTGRESQL` | PostgreSQL connection type.  
`AZURE_SYNAPSE_ANALYTICS` | Azure synapse analytics connection type.  
`SNOWFLAKE` | Snowflake connection type.  
`AMAZON_S3` | Amazon S3 connection type.  
`HDFS` | HDFS connection type.  
`ORACLE_AI_DATA_PLATFORM` | Oracle AI data platform connection type.  
`ORACLE_NOSQL` | Oracle NoSQL connection type.  
`MONGODB` | MongoDB connection type.  
`AMAZON_KINESIS` | Amazon Kinesis connection type.  
`AMAZON_REDSHIFT` | Amazon Redshift connection type.  
`DB2` | DB2 connection type.  
`REDIS` | Redis connection type.  
`ELASTICSEARCH` | Elasticsearch connection type.  
`GENERIC` | Generic connection type.  
`GOOGLE_CLOUD_STORAGE` | Google Cloud Storage connection type.  
`GOOGLE_BIGQUERY` | Google BigQuery connection type.  
`DATABRICKS` | Databricks connection type.  
`GOOGLE_PUBSUB` | Google Pub/Sub connection type.  
`MICROSOFT_FABRIC` | Microsoft Fabric connection type.  
`ICEBERG` | Iceberg connection type.  
  
## GoldengateConnectionLifecycleState

Possible lifecycle states for connection.

Enums  
---  
`GOLDENGATE_CONNECTION_LIFECYCLE_STATE_UNSPECIFIED` | Default unspecified value.  
`CREATING` | Indicates that the resource is in provisioning state.  
`ACTIVE` | Indicates that the resource is in active state.  
`UPDATING` | Indicates that the resource is in updating state.  
`DELETING` | Indicates that the resource is in deleting state.  
`DELETED` | Indicates that the resource is in deleted state.  
`FAILED` | Indicates that the resource is in failed state.  
  
## GoldengateConnectionRoutingMethod

The various routing methods of the GoldengateConnection.

Enums  
---  
`GOLDENGATE_CONNECTION_ROUTING_METHOD_UNSPECIFIED` | Default unspecified value.  
`SHARED_DEPLOYMENT_ENDPOINT` | Network traffic flows from the assigned deployment's private endpoint through the deployment's subnet.  
`DEDICATED_ENDPOINT` | A dedicated private endpoint is created in the target VCN subnet for the connection.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections/create)`

|  Creates a new GoldengateConnection in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections/delete)`

|  Deletes a single GoldengateConnection.  
  
### `[get](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections/get)`

|  Gets details of a single GoldengateConnection.  
  
### `[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections/list)`

|  Lists all the GoldengateConnections for the given project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
