---
url: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionTypes
title: REST Resource: projects.locations.goldengateConnectionTypes \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:48.597796+00:00
---

# REST Resource: projects.locations.goldengateConnectionTypes  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionTypes

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  REST Resource: projects.locations.goldengateConnectionTypes Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: GoldengateConnectionType
    * JSON representation
  * ConnectionType
  * Methods



## Resource: GoldengateConnectionType

Details of the Goldengate Connection Type resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "connectionType": enum ([ConnectionType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionTypes#ConnectionType)),
      "technologyTypes": [
        string
      ]
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the Goldengate Connection Type resource with the format: projects/{project}/locations/{region}/goldengateConnectionTypes/{goldengate_connection_type}  
`connectionType` |  `enum (`[ConnectionType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionTypes#ConnectionType)`)` Output only. The connection type of the Goldengate Connection Type resource.  
`technologyTypes[]` |  `string` Output only. The technology type of the Goldengate Connection Type resource.  
  
## ConnectionType

The connection type of the Goldengate Connection Type resource.

Enums  
---  
`CONNECTION_TYPE_UNSPECIFIED` | Default unspecified value.  
`GOLDENGATE` | Goldengate Connection Type category is GOLDENGATE.  
`KAFKA` | Goldengate Connection Type category is KAFKA.  
`KAFKA_SCHEMA_REGISTRY` | Goldengate Connection Type category is KAFKA_SCHEMA_REGISTRY.  
`MYSQL` | Goldengate Connection Type category is MYSQL.  
`JAVA_MESSAGE_SERVICE` | Goldengate Connection Type category is JAVA_MESSAGE_SERVICE.  
`MICROSOFT_SQLSERVER` | Goldengate Connection Type category is MICROSOFT_SQLSERVER.  
`OCI_OBJECT_STORAGE` | Goldengate Connection Type category is OCI_OBJECT_STORAGE.  
`ORACLE` | Goldengate Connection Type category is ORACLE.  
`AZURE_DATA_LAKE_STORAGE` | Goldengate Connection Type category is AZURE_DATA_LAKE_STORAGE.  
`POSTGRESQL` | Goldengate Connection Type category is POSTGRESQL.  
`AZURE_SYNAPSE_ANALYTICS` | Goldengate Connection Type category is AZURE_SYNAPSE_ANALYTICS.  
`SNOWFLAKE` | Goldengate Connection Type category is SNOWFLAKE.  
`AMAZON_S3` | Goldengate Connection Type category is AMAZON_S3.  
`HDFS` | Goldengate Connection Type category is HDFS.  
`ORACLE_AI_DATA_PLATFORM` | Goldengate Connection Type category is ORACLE_AI_DATA_PLATFORM.  
`ORACLE_NOSQL` | Goldengate Connection Type category is ORACLE_NOSQL.  
`MONGODB` | Goldengate Connection Type category is MONGODB.  
`AMAZON_KINESIS` | Goldengate Connection Type category is AMAZON_KINESIS.  
`AMAZON_REDSHIFT` | Goldengate Connection Type category is AMAZON_REDSHIFT.  
`DB2` | Goldengate Connection Type category is DB2.  
`REDIS` | Goldengate Connection Type category is REDIS.  
`ELASTICSEARCH` | Goldengate Connection Type category is ELASTICSEARCH.  
`GENERIC` | Goldengate Connection Type category is GENERIC.  
`GOOGLE_CLOUD_STORAGE` | Goldengate Connection Type category is GOOGLE_CLOUD_STORAGE.  
`GOOGLE_BIGQUERY` | Goldengate Connection Type category is GOOGLE_BIGQUERY.  
`DATABRICKS` | Goldengate Connection Type category is DATABRICKS.  
`GOOGLE_PUBSUB` | Goldengate Connection Type category is GOOGLE_PUBSUB.  
`MICROSOFT_FABRIC` | Goldengate Connection Type category is MICROSOFT_FABRIC.  
`ICEBERG` | Goldengate Connection Type category is ICEBERG.  
  
## Methods  
  
---  
  
### `[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionTypes/list)`

|  Lists GoldengateConnectionTypes in a given project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
