---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.Tensor
title: Vertex AI v1 API - Class Tensor (3.77.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:33:43.406145+00:00
---

# Vertex AI v1 API - Class Tensor (3.77.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.Tensor

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1 API - Class Tensor (3.77.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.77.0 (latest)  3.76.0  3.75.0  3.74.0  3.73.0  3.72.0  3.71.0  3.70.0  3.69.0  3.68.0  3.67.0  3.66.0  3.65.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class Tensor : IMessage<Tensor>, IEquatable<Tensor>, IDeepCloneable<Tensor>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1 API class Tensor.

A tensor value type.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Tensor

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Tensor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.Tensor), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Tensor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.Tensor), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Tensor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.Tensor), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1)

## Assembly

Google.Cloud.AIPlatform.V1.dll

## Constructors 

### Tensor()
    
    
    public Tensor()

### Tensor(Tensor)
    
    
    public Tensor(Tensor other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Tensor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.Tensor)`  
  
  
## Properties 

### BoolVal
    
    
    public RepeatedField<bool> BoolVal { get; }

Type specific representations that make it easy to create tensor protos in all languages. Only the representation corresponding to "dtype" can be set. The values hold the flattened representation of the tensor in row major order.

[BOOL][google.cloud.aiplatform.v1.Tensor.DataType.BOOL]

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### BytesVal
    
    
    public RepeatedField<ByteString> BytesVal { get; }

[STRING][google.cloud.aiplatform.v1.Tensor.DataType.STRING]

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)` |   
  
### DoubleVal
    
    
    public RepeatedField<double> DoubleVal { get; }

[DOUBLE][google.cloud.aiplatform.v1.Tensor.DataType.DOUBLE]

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[double](https://learn.microsoft.com/dotnet/api/system.double)` |   
  
### Dtype
    
    
    public Tensor.Types.DataType Dtype { get; set; }

The data type of tensor.

**Property Value**  
---  
**Type** | **Description**  
`[Tensor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.Tensor)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.Tensor.Types)[DataType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.Tensor.Types.DataType)` |   
  
### FloatVal
    
    
    public RepeatedField<float> FloatVal { get; }

[FLOAT][google.cloud.aiplatform.v1.Tensor.DataType.FLOAT]

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[float](https://learn.microsoft.com/dotnet/api/system.single)` |   
  
### Int64Val
    
    
    public RepeatedField<long> Int64Val { get; }

[INT64][google.cloud.aiplatform.v1.Tensor.DataType.INT64]

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### IntVal
    
    
    public RepeatedField<int> IntVal { get; }

[INT_8][google.cloud.aiplatform.v1.Tensor.DataType.INT8] [INT_16][google.cloud.aiplatform.v1.Tensor.DataType.INT16] [INT_32][google.cloud.aiplatform.v1.Tensor.DataType.INT32]

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### ListVal
    
    
    public RepeatedField<Tensor> ListVal { get; }

A list of tensor values.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Tensor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.Tensor)` |   
  
### Shape
    
    
    public RepeatedField<long> Shape { get; }

Shape of the tensor.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### StringVal
    
    
    public RepeatedField<string> StringVal { get; }

[STRING][google.cloud.aiplatform.v1.Tensor.DataType.STRING]

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### StructVal
    
    
    public MapField<string, Tensor> StructVal { get; }

A map of string to tensor.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[Tensor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.Tensor)` |   
  
### TensorVal
    
    
    public ByteString TensorVal { get; set; }

Serialized raw tensor content.

**Property Value**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)` |   
  
### Uint64Val
    
    
    public RepeatedField<ulong> Uint64Val { get; }

[UINT64][google.cloud.aiplatform.v1.Tensor.DataType.UINT64]

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)System.UInt64` |   
  
### UintVal
    
    
    public RepeatedField<uint> UintVal { get; }

[UINT8][google.cloud.aiplatform.v1.Tensor.DataType.UINT8] [UINT16][google.cloud.aiplatform.v1.Tensor.DataType.UINT16] [UINT32][google.cloud.aiplatform.v1.Tensor.DataType.UINT32]

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)System.UInt32` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
