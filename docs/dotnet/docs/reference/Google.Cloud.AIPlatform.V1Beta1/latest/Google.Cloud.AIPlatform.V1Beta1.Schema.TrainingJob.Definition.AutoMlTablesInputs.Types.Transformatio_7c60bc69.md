---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs.Types.Transformation.Types.TextArrayTransformation
title: Vertex AI v1beta1 API - Class AutoMlTablesInputs.Types.Transformation.Types.TextArrayTransformation (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:29:47.769200+00:00
---

# Vertex AI v1beta1 API - Class AutoMlTablesInputs.Types.Transformation.Types.TextArrayTransformation (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs.Types.Transformation.Types.TextArrayTransformation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class AutoMlTablesInputs.Types.Transformation.Types.TextArrayTransformation (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class AutoMlTablesInputs.Types.Transformation.Types.TextArrayTransformation : IMessage<AutoMlTablesInputs.Types.Transformation.Types.TextArrayTransformation>, IEquatable<AutoMlTablesInputs.Types.Transformation.Types.TextArrayTransformation>, IDeepCloneable<AutoMlTablesInputs.Types.Transformation.Types.TextArrayTransformation>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1beta1 API class AutoMlTablesInputs.Types.Transformation.Types.TextArrayTransformation.

Treats the column as text array and performs following transformation functions.

  * Concatenate all text values in the array into a single text value using a space (" ") as a delimiter, and then treat the result as a single text value. Apply the transformations for Text columns.
  * Empty arrays treated as an empty text.



## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AutoMlTablesInputs.Types.Transformation.Types.TextArrayTransformation

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AutoMlTablesInputs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs.Types)[Transformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs.Types.Transformation)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs.Types.Transformation.Types)[TextArrayTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs.Types.Transformation.Types.TextArrayTransformation), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AutoMlTablesInputs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs.Types)[Transformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs.Types.Transformation)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs.Types.Transformation.Types)[TextArrayTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs.Types.Transformation.Types.TextArrayTransformation), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AutoMlTablesInputs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs.Types)[Transformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs.Types.Transformation)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs.Types.Transformation.Types)[TextArrayTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs.Types.Transformation.Types.TextArrayTransformation), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### TextArrayTransformation()
    
    
    public TextArrayTransformation()

### TextArrayTransformation(TextArrayTransformation)
    
    
    public TextArrayTransformation(AutoMlTablesInputs.Types.Transformation.Types.TextArrayTransformation other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AutoMlTablesInputs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs.Types)[Transformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs.Types.Transformation)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs.Types.Transformation.Types)[TextArrayTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs.Types.Transformation.Types.TextArrayTransformation)`  
  
  
## Properties 

### ColumnName
    
    
    public string ColumnName { get; set; }

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
