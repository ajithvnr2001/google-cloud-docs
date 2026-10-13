---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchReadFeatureValuesRequest
title: Vertex AI v1 API - Class BatchReadFeatureValuesRequest (3.77.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:36:18.676976+00:00
---

# Vertex AI v1 API - Class BatchReadFeatureValuesRequest (3.77.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchReadFeatureValuesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1 API - Class BatchReadFeatureValuesRequest (3.77.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.77.0 (latest)  3.76.0  3.75.0  3.74.0  3.73.0  3.72.0  3.71.0  3.70.0  3.69.0  3.68.0  3.67.0  3.66.0  3.65.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class BatchReadFeatureValuesRequest : IMessage<BatchReadFeatureValuesRequest>, IEquatable<BatchReadFeatureValuesRequest>, IDeepCloneable<BatchReadFeatureValuesRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1 API class BatchReadFeatureValuesRequest.

Request message for [FeaturestoreService.BatchReadFeatureValues][google.cloud.aiplatform.v1.FeaturestoreService.BatchReadFeatureValues].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BatchReadFeatureValuesRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[BatchReadFeatureValuesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchReadFeatureValuesRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BatchReadFeatureValuesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchReadFeatureValuesRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[BatchReadFeatureValuesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchReadFeatureValuesRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1)

## Assembly

Google.Cloud.AIPlatform.V1.dll

## Constructors 

### BatchReadFeatureValuesRequest()
    
    
    public BatchReadFeatureValuesRequest()

### BatchReadFeatureValuesRequest(BatchReadFeatureValuesRequest)
    
    
    public BatchReadFeatureValuesRequest(BatchReadFeatureValuesRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[BatchReadFeatureValuesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchReadFeatureValuesRequest)`  
  
  
## Properties 

### BigqueryReadInstances
    
    
    public BigQuerySource BigqueryReadInstances { get; set; }

Similar to csv_read_instances, but from BigQuery source.

**Property Value**  
---  
**Type** | **Description**  
`[BigQuerySource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BigQuerySource)` |   
  
### CsvReadInstances
    
    
    public CsvSource CsvReadInstances { get; set; }

Each read instance consists of exactly one read timestamp and one or more entity IDs identifying entities of the corresponding EntityTypes whose Features are requested.

Each output instance contains Feature values of requested entities concatenated together as of the read time.

An example read instance may be `foo_entity_id, bar_entity_id, 2020-01-01T10:00:00.123Z`.

An example output instance may be `foo_entity_id, bar_entity_id, 2020-01-01T10:00:00.123Z, foo_entity_feature1_value, bar_entity_feature2_value`.

Timestamp in each read instance must be millisecond-aligned.

`csv_read_instances` are read instances stored in a plain-text CSV file. The header should be: [ENTITY_TYPE_ID1], [ENTITY_TYPE_ID2], ..., timestamp

The columns can be in any order.

Values in the timestamp column must use the RFC 3339 format, e.g. `2012-07-30T10:43:17.123Z`.

**Property Value**  
---  
**Type** | **Description**  
`[CsvSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CsvSource)` |   
  
### Destination
    
    
    public FeatureValueDestination Destination { get; set; }

Required. Specifies output location and format.

**Property Value**  
---  
**Type** | **Description**  
`[FeatureValueDestination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureValueDestination)` |   
  
### EntityTypeSpecs
    
    
    public RepeatedField<BatchReadFeatureValuesRequest.Types.EntityTypeSpec> EntityTypeSpecs { get; }

Required. Specifies EntityType grouping Features to read values of and settings.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[BatchReadFeatureValuesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchReadFeatureValuesRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchReadFeatureValuesRequest.Types)[EntityTypeSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchReadFeatureValuesRequest.Types.EntityTypeSpec)` |   
  
### Featurestore
    
    
    public string Featurestore { get; set; }

Required. The resource name of the Featurestore from which to query Feature values. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### FeaturestoreAsFeaturestoreName
    
    
    public FeaturestoreName FeaturestoreAsFeaturestoreName { get; set; }

[FeaturestoreName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeaturestoreName)-typed view over the [Featurestore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchReadFeatureValuesRequest#Google_Cloud_AIPlatform_V1_BatchReadFeatureValuesRequest_Featurestore) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[FeaturestoreName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeaturestoreName)` |   
  
### PassThroughFields
    
    
    public RepeatedField<BatchReadFeatureValuesRequest.Types.PassThroughField> PassThroughFields { get; }

When not empty, the specified fields in the *_read_instances source will be joined as-is in the output, in addition to those fields from the Featurestore Entity.

For BigQuery source, the type of the pass-through values will be automatically inferred. For CSV source, the pass-through values will be passed as opaque bytes.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[BatchReadFeatureValuesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchReadFeatureValuesRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchReadFeatureValuesRequest.Types)[PassThroughField](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchReadFeatureValuesRequest.Types.PassThroughField)` |   
  
### ReadOptionCase
    
    
    public BatchReadFeatureValuesRequest.ReadOptionOneofCase ReadOptionCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[BatchReadFeatureValuesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchReadFeatureValuesRequest)[ReadOptionOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchReadFeatureValuesRequest.ReadOptionOneofCase)` |   
  
### StartTime
    
    
    public Timestamp StartTime { get; set; }

Optional. Excludes Feature values with feature generation timestamp before this timestamp. If not set, retrieve oldest values kept in Feature Store. Timestamp, if present, must not have higher than millisecond precision.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
