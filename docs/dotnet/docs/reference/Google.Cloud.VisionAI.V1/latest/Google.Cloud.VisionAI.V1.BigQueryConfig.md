---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.BigQueryConfig
title: Vision AI v1 API - Class BigQueryConfig (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:04:46.724679+00:00
---

# Vision AI v1 API - Class BigQueryConfig (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.BigQueryConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vision AI v1 API - Class BigQueryConfig (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta01 
    
    
    public sealed class BigQueryConfig : IMessage<BigQueryConfig>, IEquatable<BigQueryConfig>, IDeepCloneable<BigQueryConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Vision AI v1 API class BigQueryConfig.

Message of configurations for BigQuery processor.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BigQueryConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[BigQueryConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.BigQueryConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BigQueryConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.BigQueryConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[BigQueryConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.BigQueryConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.VisionAI.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1)

## Assembly

Google.Cloud.VisionAI.V1.dll

## Constructors 

### BigQueryConfig()
    
    
    public BigQueryConfig()

### BigQueryConfig(BigQueryConfig)
    
    
    public BigQueryConfig(BigQueryConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[BigQueryConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.BigQueryConfig)`  
  
  
## Properties 

### CloudFunctionMapping
    
    
    public MapField<string, string> CloudFunctionMapping { get; }

Data Schema By default, Vision AI Application will try to write annotations to the target BigQuery table using the following schema:

ingestion_time: TIMESTAMP, the ingestion time of the original data.

application: STRING, name of the application which produces the annotation.

instance: STRING, Id of the instance which produces the annotation.

node: STRING, name of the application graph node which produces the annotation.

annotation: STRING or JSON, the actual annotation protobuf will be converted to json string with bytes field as 64 encoded string. It can be written to both String or Json type column.

To forward annotation data to an existing BigQuery table, customer needs to make sure the compatibility of the schema. The map maps application node name to its corresponding cloud function endpoint to transform the annotations directly to the google.cloud.bigquery.storage.v1.AppendRowsRequest (only avro_rows or proto_rows should be set). If configured, annotations produced by corresponding application node will sent to the Cloud Function at first before be forwarded to BigQuery.

If the default table schema doesn't fit, customer is able to transform the annotation output from Vision AI Application to arbitrary BigQuery table schema with CloudFunction.

  * The cloud function will receive AppPlatformCloudFunctionRequest where the annotations field will be the json format of Vision AI annotation.
  * The cloud function should return AppPlatformCloudFunctionResponse with AppendRowsRequest stored in the annotations field.
  * To drop the annotation, simply clear the annotations field in the returned AppPlatformCloudFunctionResponse.



**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CreateDefaultTableIfNotExists
    
    
    public bool CreateDefaultTableIfNotExists { get; set; }

If true, App Platform will create the BigQuery DataSet and the BigQuery Table with default schema if the specified table doesn't exist. This doesn't work if any cloud function customized schema is specified since the system doesn't know your desired schema. JSON column will be used in the default table created by App Platform.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Table
    
    
    public string Table { get; set; }

BigQuery table resource for Vision AI Platform to ingest annotations to.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
