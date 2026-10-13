---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.ConnectionOrBuilder
title: Interface ConnectionOrBuilder (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:27:14.778150+00:00
---

# Interface ConnectionOrBuilder (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.ConnectionOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ConnectionOrBuilder (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.83.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.6  2.4.0  2.2.4  2.1.11 
    
    
    public interface ConnectionOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAws()
    
    
    public abstract AwsProperties getAws()

Amazon Web Services (AWS) properties.

`.google.cloud.bigquery.connection.v1.AwsProperties aws = 8;`

**Returns**  
---  
**Type** | **Description**  
`[AwsProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.AwsProperties)` | The aws.  
  
### getAwsOrBuilder()
    
    
    public abstract AwsPropertiesOrBuilder getAwsOrBuilder()

Amazon Web Services (AWS) properties.

`.google.cloud.bigquery.connection.v1.AwsProperties aws = 8;`

**Returns**  
---  
**Type** | **Description**  
`[AwsPropertiesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.AwsPropertiesOrBuilder)` |   
  
### getAzure()
    
    
    public abstract AzureProperties getAzure()

Azure properties.

`.google.cloud.bigquery.connection.v1.AzureProperties azure = 11;`

**Returns**  
---  
**Type** | **Description**  
`[AzureProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.AzureProperties)` | The azure.  
  
### getAzureOrBuilder()
    
    
    public abstract AzurePropertiesOrBuilder getAzureOrBuilder()

Azure properties.

`.google.cloud.bigquery.connection.v1.AzureProperties azure = 11;`

**Returns**  
---  
**Type** | **Description**  
`[AzurePropertiesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.AzurePropertiesOrBuilder)` |   
  
### getCloudResource()
    
    
    public abstract CloudResourceProperties getCloudResource()

Cloud Resource properties.

`.google.cloud.bigquery.connection.v1.CloudResourceProperties cloud_resource = 22;`

**Returns**  
---  
**Type** | **Description**  
`[CloudResourceProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.CloudResourceProperties)` | The cloudResource.  
  
### getCloudResourceOrBuilder()
    
    
    public abstract CloudResourcePropertiesOrBuilder getCloudResourceOrBuilder()

Cloud Resource properties.

`.google.cloud.bigquery.connection.v1.CloudResourceProperties cloud_resource = 22;`

**Returns**  
---  
**Type** | **Description**  
`[CloudResourcePropertiesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.CloudResourcePropertiesOrBuilder)` |   
  
### getCloudSpanner()
    
    
    public abstract CloudSpannerProperties getCloudSpanner()

Cloud Spanner properties.

`.google.cloud.bigquery.connection.v1.CloudSpannerProperties cloud_spanner = 21;`

**Returns**  
---  
**Type** | **Description**  
`[CloudSpannerProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.CloudSpannerProperties)` | The cloudSpanner.  
  
### getCloudSpannerOrBuilder()
    
    
    public abstract CloudSpannerPropertiesOrBuilder getCloudSpannerOrBuilder()

Cloud Spanner properties.

`.google.cloud.bigquery.connection.v1.CloudSpannerProperties cloud_spanner = 21;`

**Returns**  
---  
**Type** | **Description**  
`[CloudSpannerPropertiesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.CloudSpannerPropertiesOrBuilder)` |   
  
### getCloudSql()
    
    
    public abstract CloudSqlProperties getCloudSql()

Cloud SQL properties.

`.google.cloud.bigquery.connection.v1.CloudSqlProperties cloud_sql = 4;`

**Returns**  
---  
**Type** | **Description**  
`[CloudSqlProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.CloudSqlProperties)` | The cloudSql.  
  
### getCloudSqlOrBuilder()
    
    
    public abstract CloudSqlPropertiesOrBuilder getCloudSqlOrBuilder()

Cloud SQL properties.

`.google.cloud.bigquery.connection.v1.CloudSqlProperties cloud_sql = 4;`

**Returns**  
---  
**Type** | **Description**  
`[CloudSqlPropertiesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.CloudSqlPropertiesOrBuilder)` |   
  
### getCreationTime()
    
    
    public abstract long getCreationTime()

Output only. The creation timestamp of the connection.

`int64 creation_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The creationTime.  
  
### getDescription()
    
    
    public abstract String getDescription()

User provided description.

`string description = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

User provided description.

`string description = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getFriendlyName()
    
    
    public abstract String getFriendlyName()

User provided display name for the connection.

`string friendly_name = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The friendlyName.  
  
### getFriendlyNameBytes()
    
    
    public abstract ByteString getFriendlyNameBytes()

User provided display name for the connection.

`string friendly_name = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for friendlyName.  
  
### getHasCredential()
    
    
    public abstract boolean getHasCredential()

Output only. True, if credential is configured for this connection.

`bool has_credential = 7 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The hasCredential.  
  
### getLastModifiedTime()
    
    
    public abstract long getLastModifiedTime()

Output only. The last update timestamp of the connection.

`int64 last_modified_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The lastModifiedTime.  
  
### getName()
    
    
    public abstract String getName()

The resource name of the connection in the form of: `projects/{project_id}/locations/{location_id}/connections/{connection_id}`

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

The resource name of the connection in the form of: `projects/{project_id}/locations/{location_id}/connections/{connection_id}`

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getPropertiesCase()
    
    
    public abstract Connection.PropertiesCase getPropertiesCase()

**Returns**  
---  
**Type** | **Description**  
`[Connection.PropertiesCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.Connection.PropertiesCase)` |   
  
### getSalesforceDataCloud()
    
    
    public abstract SalesforceDataCloudProperties getSalesforceDataCloud()

Optional. Salesforce DataCloud properties. This field is intended for use only by Salesforce partner projects. This field contains properties for your Salesforce DataCloud connection.

` .google.cloud.bigquery.connection.v1.SalesforceDataCloudProperties salesforce_data_cloud = 24 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SalesforceDataCloudProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.SalesforceDataCloudProperties)` | The salesforceDataCloud.  
  
### getSalesforceDataCloudOrBuilder()
    
    
    public abstract SalesforceDataCloudPropertiesOrBuilder getSalesforceDataCloudOrBuilder()

Optional. Salesforce DataCloud properties. This field is intended for use only by Salesforce partner projects. This field contains properties for your Salesforce DataCloud connection.

` .google.cloud.bigquery.connection.v1.SalesforceDataCloudProperties salesforce_data_cloud = 24 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SalesforceDataCloudPropertiesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.SalesforceDataCloudPropertiesOrBuilder)` |   
  
### getSpark()
    
    
    public abstract SparkProperties getSpark()

Spark properties.

`.google.cloud.bigquery.connection.v1.SparkProperties spark = 23;`

**Returns**  
---  
**Type** | **Description**  
`[SparkProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.SparkProperties)` | The spark.  
  
### getSparkOrBuilder()
    
    
    public abstract SparkPropertiesOrBuilder getSparkOrBuilder()

Spark properties.

`.google.cloud.bigquery.connection.v1.SparkProperties spark = 23;`

**Returns**  
---  
**Type** | **Description**  
`[SparkPropertiesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryconnection/latest/com.google.cloud.bigquery.connection.v1.SparkPropertiesOrBuilder)` |   
  
### hasAws()
    
    
    public abstract boolean hasAws()

Amazon Web Services (AWS) properties.

`.google.cloud.bigquery.connection.v1.AwsProperties aws = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the aws field is set.  
  
### hasAzure()
    
    
    public abstract boolean hasAzure()

Azure properties.

`.google.cloud.bigquery.connection.v1.AzureProperties azure = 11;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the azure field is set.  
  
### hasCloudResource()
    
    
    public abstract boolean hasCloudResource()

Cloud Resource properties.

`.google.cloud.bigquery.connection.v1.CloudResourceProperties cloud_resource = 22;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the cloudResource field is set.  
  
### hasCloudSpanner()
    
    
    public abstract boolean hasCloudSpanner()

Cloud Spanner properties.

`.google.cloud.bigquery.connection.v1.CloudSpannerProperties cloud_spanner = 21;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the cloudSpanner field is set.  
  
### hasCloudSql()
    
    
    public abstract boolean hasCloudSql()

Cloud SQL properties.

`.google.cloud.bigquery.connection.v1.CloudSqlProperties cloud_sql = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the cloudSql field is set.  
  
### hasSalesforceDataCloud()
    
    
    public abstract boolean hasSalesforceDataCloud()

Optional. Salesforce DataCloud properties. This field is intended for use only by Salesforce partner projects. This field contains properties for your Salesforce DataCloud connection.

` .google.cloud.bigquery.connection.v1.SalesforceDataCloudProperties salesforce_data_cloud = 24 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the salesforceDataCloud field is set.  
  
### hasSpark()
    
    
    public abstract boolean hasSpark()

Spark properties.

`.google.cloud.bigquery.connection.v1.SparkProperties spark = 23;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the spark field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
