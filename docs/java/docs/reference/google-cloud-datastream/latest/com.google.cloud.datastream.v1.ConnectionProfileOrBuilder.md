---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfileOrBuilder
title: Interface ConnectionProfileOrBuilder (1.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:51:34.403487+00:00
---

# Interface ConnectionProfileOrBuilder (1.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfileOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ConnectionProfileOrBuilder (1.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.98.0 (latest)  1.94.0  1.93.0  1.92.0  1.90.0  1.87.0  1.86.0  1.84.0  1.82.0  1.81.0  1.80.0  1.79.0  1.77.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.0  1.69.0  1.67.0  1.66.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.2  1.1.1  1.0.0  0.4.2 
    
    
    public interface ConnectionProfileOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsLabels(String key)
    
    
    public abstract boolean containsLabels(String key)

Labels.

`map<string, string> labels = 4;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getBigqueryProfile()
    
    
    public abstract BigQueryProfile getBigqueryProfile()

BigQuery Connection Profile configuration.

`.google.cloud.datastream.v1.BigQueryProfile bigquery_profile = 103;`

**Returns**  
---  
**Type** | **Description**  
`[BigQueryProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.BigQueryProfile)` | The bigqueryProfile.  
  
### getBigqueryProfileOrBuilder()
    
    
    public abstract BigQueryProfileOrBuilder getBigqueryProfileOrBuilder()

BigQuery Connection Profile configuration.

`.google.cloud.datastream.v1.BigQueryProfile bigquery_profile = 103;`

**Returns**  
---  
**Type** | **Description**  
`[BigQueryProfileOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.BigQueryProfileOrBuilder)` |   
  
### getConnectivityCase()
    
    
    public abstract ConnectionProfile.ConnectivityCase getConnectivityCase()

**Returns**  
---  
**Type** | **Description**  
`[ConnectionProfile.ConnectivityCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile.ConnectivityCase)` |   
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. The create time of the resource.

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. The create time of the resource.

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDisplayName()
    
    
    public abstract String getDisplayName()

Required. Display name.

`string display_name = 5 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

Required. Display name.

`string display_name = 5 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getForwardSshConnectivity()
    
    
    public abstract ForwardSshTunnelConnectivity getForwardSshConnectivity()

Forward SSH tunnel connectivity.

`.google.cloud.datastream.v1.ForwardSshTunnelConnectivity forward_ssh_connectivity = 201; `

**Returns**  
---  
**Type** | **Description**  
`[ForwardSshTunnelConnectivity](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ForwardSshTunnelConnectivity)` | The forwardSshConnectivity.  
  
### getForwardSshConnectivityOrBuilder()
    
    
    public abstract ForwardSshTunnelConnectivityOrBuilder getForwardSshConnectivityOrBuilder()

Forward SSH tunnel connectivity.

`.google.cloud.datastream.v1.ForwardSshTunnelConnectivity forward_ssh_connectivity = 201; `

**Returns**  
---  
**Type** | **Description**  
`[ForwardSshTunnelConnectivityOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ForwardSshTunnelConnectivityOrBuilder)` |   
  
### getGcsProfile()
    
    
    public abstract GcsProfile getGcsProfile()

Cloud Storage ConnectionProfile configuration.

`.google.cloud.datastream.v1.GcsProfile gcs_profile = 101;`

**Returns**  
---  
**Type** | **Description**  
`[GcsProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.GcsProfile)` | The gcsProfile.  
  
### getGcsProfileOrBuilder()
    
    
    public abstract GcsProfileOrBuilder getGcsProfileOrBuilder()

Cloud Storage ConnectionProfile configuration.

`.google.cloud.datastream.v1.GcsProfile gcs_profile = 101;`

**Returns**  
---  
**Type** | **Description**  
`[GcsProfileOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.GcsProfileOrBuilder)` |   
  
### getLabels() (deprecated)
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfileOrBuilder#com_google_cloud_datastream_v1_ConnectionProfileOrBuilder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public abstract int getLabelsCount()

Labels.

`map<string, string> labels = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public abstract Map<String,String> getLabelsMap()

Labels.

`map<string, string> labels = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getLabelsOrDefault(String key, String defaultValue)

Labels.

`map<string, string> labels = 4;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getLabelsOrThrow(String key)
    
    
    public abstract String getLabelsOrThrow(String key)

Labels.

`map<string, string> labels = 4;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getMongodbProfile()
    
    
    public abstract MongodbProfile getMongodbProfile()

MongoDB Connection Profile configuration.

`.google.cloud.datastream.v1.MongodbProfile mongodb_profile = 108;`

**Returns**  
---  
**Type** | **Description**  
`[MongodbProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.MongodbProfile)` | The mongodbProfile.  
  
### getMongodbProfileOrBuilder()
    
    
    public abstract MongodbProfileOrBuilder getMongodbProfileOrBuilder()

MongoDB Connection Profile configuration.

`.google.cloud.datastream.v1.MongodbProfile mongodb_profile = 108;`

**Returns**  
---  
**Type** | **Description**  
`[MongodbProfileOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.MongodbProfileOrBuilder)` |   
  
### getMysqlProfile()
    
    
    public abstract MysqlProfile getMysqlProfile()

MySQL ConnectionProfile configuration.

`.google.cloud.datastream.v1.MysqlProfile mysql_profile = 102;`

**Returns**  
---  
**Type** | **Description**  
`[MysqlProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.MysqlProfile)` | The mysqlProfile.  
  
### getMysqlProfileOrBuilder()
    
    
    public abstract MysqlProfileOrBuilder getMysqlProfileOrBuilder()

MySQL ConnectionProfile configuration.

`.google.cloud.datastream.v1.MysqlProfile mysql_profile = 102;`

**Returns**  
---  
**Type** | **Description**  
`[MysqlProfileOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.MysqlProfileOrBuilder)` |   
  
### getName()
    
    
    public abstract String getName()

Output only. Identifier. The resource's name.

` string name = 1 [(.google.api.field_behavior) = IDENTIFIER, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Output only. Identifier. The resource's name.

` string name = 1 [(.google.api.field_behavior) = IDENTIFIER, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getOracleProfile()
    
    
    public abstract OracleProfile getOracleProfile()

Oracle ConnectionProfile configuration.

`.google.cloud.datastream.v1.OracleProfile oracle_profile = 100;`

**Returns**  
---  
**Type** | **Description**  
`[OracleProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OracleProfile)` | The oracleProfile.  
  
### getOracleProfileOrBuilder()
    
    
    public abstract OracleProfileOrBuilder getOracleProfileOrBuilder()

Oracle ConnectionProfile configuration.

`.google.cloud.datastream.v1.OracleProfile oracle_profile = 100;`

**Returns**  
---  
**Type** | **Description**  
`[OracleProfileOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OracleProfileOrBuilder)` |   
  
### getPostgresqlProfile()
    
    
    public abstract PostgresqlProfile getPostgresqlProfile()

PostgreSQL Connection Profile configuration.

`.google.cloud.datastream.v1.PostgresqlProfile postgresql_profile = 104;`

**Returns**  
---  
**Type** | **Description**  
`[PostgresqlProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.PostgresqlProfile)` | The postgresqlProfile.  
  
### getPostgresqlProfileOrBuilder()
    
    
    public abstract PostgresqlProfileOrBuilder getPostgresqlProfileOrBuilder()

PostgreSQL Connection Profile configuration.

`.google.cloud.datastream.v1.PostgresqlProfile postgresql_profile = 104;`

**Returns**  
---  
**Type** | **Description**  
`[PostgresqlProfileOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.PostgresqlProfileOrBuilder)` |   
  
### getPrivateConnectivity()
    
    
    public abstract PrivateConnectivity getPrivateConnectivity()

Private connectivity.

`.google.cloud.datastream.v1.PrivateConnectivity private_connectivity = 202;`

**Returns**  
---  
**Type** | **Description**  
`[PrivateConnectivity](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.PrivateConnectivity)` | The privateConnectivity.  
  
### getPrivateConnectivityOrBuilder()
    
    
    public abstract PrivateConnectivityOrBuilder getPrivateConnectivityOrBuilder()

Private connectivity.

`.google.cloud.datastream.v1.PrivateConnectivity private_connectivity = 202;`

**Returns**  
---  
**Type** | **Description**  
`[PrivateConnectivityOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.PrivateConnectivityOrBuilder)` |   
  
### getProfileCase()
    
    
    public abstract ConnectionProfile.ProfileCase getProfileCase()

**Returns**  
---  
**Type** | **Description**  
`[ConnectionProfile.ProfileCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile.ProfileCase)` |   
  
### getSalesforceProfile()
    
    
    public abstract SalesforceProfile getSalesforceProfile()

Salesforce Connection Profile configuration.

`.google.cloud.datastream.v1.SalesforceProfile salesforce_profile = 107;`

**Returns**  
---  
**Type** | **Description**  
`[SalesforceProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.SalesforceProfile)` | The salesforceProfile.  
  
### getSalesforceProfileOrBuilder()
    
    
    public abstract SalesforceProfileOrBuilder getSalesforceProfileOrBuilder()

Salesforce Connection Profile configuration.

`.google.cloud.datastream.v1.SalesforceProfile salesforce_profile = 107;`

**Returns**  
---  
**Type** | **Description**  
`[SalesforceProfileOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.SalesforceProfileOrBuilder)` |   
  
### getSatisfiesPzi()
    
    
    public abstract boolean getSatisfiesPzi()

Output only. Reserved for future use.

`optional bool satisfies_pzi = 7 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The satisfiesPzi.  
  
### getSatisfiesPzs()
    
    
    public abstract boolean getSatisfiesPzs()

Output only. Reserved for future use.

`optional bool satisfies_pzs = 6 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The satisfiesPzs.  
  
### getSqlServerProfile()
    
    
    public abstract SqlServerProfile getSqlServerProfile()

SQLServer Connection Profile configuration.

`.google.cloud.datastream.v1.SqlServerProfile sql_server_profile = 105;`

**Returns**  
---  
**Type** | **Description**  
`[SqlServerProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.SqlServerProfile)` | The sqlServerProfile.  
  
### getSqlServerProfileOrBuilder()
    
    
    public abstract SqlServerProfileOrBuilder getSqlServerProfileOrBuilder()

SQLServer Connection Profile configuration.

`.google.cloud.datastream.v1.SqlServerProfile sql_server_profile = 105;`

**Returns**  
---  
**Type** | **Description**  
`[SqlServerProfileOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.SqlServerProfileOrBuilder)` |   
  
### getStaticServiceIpConnectivity()
    
    
    public abstract StaticServiceIpConnectivity getStaticServiceIpConnectivity()

Static Service IP connectivity.

` .google.cloud.datastream.v1.StaticServiceIpConnectivity static_service_ip_connectivity = 200; `

**Returns**  
---  
**Type** | **Description**  
`[StaticServiceIpConnectivity](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.StaticServiceIpConnectivity)` | The staticServiceIpConnectivity.  
  
### getStaticServiceIpConnectivityOrBuilder()
    
    
    public abstract StaticServiceIpConnectivityOrBuilder getStaticServiceIpConnectivityOrBuilder()

Static Service IP connectivity.

` .google.cloud.datastream.v1.StaticServiceIpConnectivity static_service_ip_connectivity = 200; `

**Returns**  
---  
**Type** | **Description**  
`[StaticServiceIpConnectivityOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.StaticServiceIpConnectivityOrBuilder)` |   
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

Output only. The update time of the resource.

`.google.protobuf.Timestamp update_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. The update time of the resource.

`.google.protobuf.Timestamp update_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasBigqueryProfile()
    
    
    public abstract boolean hasBigqueryProfile()

BigQuery Connection Profile configuration.

`.google.cloud.datastream.v1.BigQueryProfile bigquery_profile = 103;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the bigqueryProfile field is set.  
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. The create time of the resource.

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasForwardSshConnectivity()
    
    
    public abstract boolean hasForwardSshConnectivity()

Forward SSH tunnel connectivity.

`.google.cloud.datastream.v1.ForwardSshTunnelConnectivity forward_ssh_connectivity = 201; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the forwardSshConnectivity field is set.  
  
### hasGcsProfile()
    
    
    public abstract boolean hasGcsProfile()

Cloud Storage ConnectionProfile configuration.

`.google.cloud.datastream.v1.GcsProfile gcs_profile = 101;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the gcsProfile field is set.  
  
### hasMongodbProfile()
    
    
    public abstract boolean hasMongodbProfile()

MongoDB Connection Profile configuration.

`.google.cloud.datastream.v1.MongodbProfile mongodb_profile = 108;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the mongodbProfile field is set.  
  
### hasMysqlProfile()
    
    
    public abstract boolean hasMysqlProfile()

MySQL ConnectionProfile configuration.

`.google.cloud.datastream.v1.MysqlProfile mysql_profile = 102;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the mysqlProfile field is set.  
  
### hasOracleProfile()
    
    
    public abstract boolean hasOracleProfile()

Oracle ConnectionProfile configuration.

`.google.cloud.datastream.v1.OracleProfile oracle_profile = 100;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the oracleProfile field is set.  
  
### hasPostgresqlProfile()
    
    
    public abstract boolean hasPostgresqlProfile()

PostgreSQL Connection Profile configuration.

`.google.cloud.datastream.v1.PostgresqlProfile postgresql_profile = 104;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the postgresqlProfile field is set.  
  
### hasPrivateConnectivity()
    
    
    public abstract boolean hasPrivateConnectivity()

Private connectivity.

`.google.cloud.datastream.v1.PrivateConnectivity private_connectivity = 202;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the privateConnectivity field is set.  
  
### hasSalesforceProfile()
    
    
    public abstract boolean hasSalesforceProfile()

Salesforce Connection Profile configuration.

`.google.cloud.datastream.v1.SalesforceProfile salesforce_profile = 107;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the salesforceProfile field is set.  
  
### hasSatisfiesPzi()
    
    
    public abstract boolean hasSatisfiesPzi()

Output only. Reserved for future use.

`optional bool satisfies_pzi = 7 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the satisfiesPzi field is set.  
  
### hasSatisfiesPzs()
    
    
    public abstract boolean hasSatisfiesPzs()

Output only. Reserved for future use.

`optional bool satisfies_pzs = 6 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the satisfiesPzs field is set.  
  
### hasSqlServerProfile()
    
    
    public abstract boolean hasSqlServerProfile()

SQLServer Connection Profile configuration.

`.google.cloud.datastream.v1.SqlServerProfile sql_server_profile = 105;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sqlServerProfile field is set.  
  
### hasStaticServiceIpConnectivity()
    
    
    public abstract boolean hasStaticServiceIpConnectivity()

Static Service IP connectivity.

` .google.cloud.datastream.v1.StaticServiceIpConnectivity static_service_ip_connectivity = 200; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the staticServiceIpConnectivity field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

Output only. The update time of the resource.

`.google.protobuf.Timestamp update_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
