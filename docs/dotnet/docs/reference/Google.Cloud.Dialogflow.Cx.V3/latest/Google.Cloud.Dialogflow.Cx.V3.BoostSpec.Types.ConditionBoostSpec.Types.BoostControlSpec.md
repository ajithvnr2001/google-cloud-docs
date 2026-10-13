---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec
title: Dialogflow v3 API - Class BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec (3.2.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:52.065445+00:00
---

# Dialogflow v3 API - Class BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec (3.2.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dialogflow v3 API - Class BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec (3.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.2.0 (latest)  3.1.0  3.0.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec : IMessage<BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec>, IEquatable<BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec>, IDeepCloneable<BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec>, IBufferMessage, IMessage

Reference documentation and code samples for the Dialogflow v3 API class BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec.

Specification for custom ranking based on customer specified attribute value. It provides more controls for customized ranking than the simple (condition, boost) combination above.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[BoostSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types)[ConditionBoostSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types.ConditionBoostSpec)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types.ConditionBoostSpec.Types)[BoostControlSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BoostSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types)[ConditionBoostSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types.ConditionBoostSpec)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types.ConditionBoostSpec.Types)[BoostControlSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[BoostSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types)[ConditionBoostSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types.ConditionBoostSpec)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types.ConditionBoostSpec.Types)[BoostControlSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dialogflow.Cx.V3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3)

## Assembly

Google.Cloud.Dialogflow.Cx.V3.dll

## Constructors 

### BoostControlSpec()
    
    
    public BoostControlSpec()

### BoostControlSpec(BoostControlSpec)
    
    
    public BoostControlSpec(BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[BoostSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types)[ConditionBoostSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types.ConditionBoostSpec)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types.ConditionBoostSpec.Types)[BoostControlSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec)`  
  
  
## Properties 

### AttributeType
    
    
    public BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec.Types.AttributeType AttributeType { get; set; }

Optional. The attribute type to be used to determine the boost amount. The attribute value can be derived from the field value of the specified field_name. In the case of numerical it is straightforward i.e. attribute_value = numerical_field_value. In the case of freshness however, attribute_value = (time.now() - datetime_field_value).

**Property Value**  
---  
**Type** | **Description**  
`[BoostSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types)[ConditionBoostSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types.ConditionBoostSpec)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types.ConditionBoostSpec.Types)[BoostControlSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec.Types)[AttributeType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec.Types.AttributeType)` |   
  
### ControlPoints
    
    
    public RepeatedField<BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec.Types.ControlPoint> ControlPoints { get; }

Optional. The control points used to define the curve. The monotonic function (defined through the interpolation_type above) passes through the control points listed here.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[BoostSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types)[ConditionBoostSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types.ConditionBoostSpec)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types.ConditionBoostSpec.Types)[BoostControlSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec.Types)[ControlPoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec.Types.ControlPoint)` |   
  
### FieldName
    
    
    public string FieldName { get; set; }

Optional. The name of the field whose value will be used to determine the boost amount.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### InterpolationType
    
    
    public BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec.Types.InterpolationType InterpolationType { get; set; }

Optional. The interpolation type to be applied to connect the control points listed below.

**Property Value**  
---  
**Type** | **Description**  
`[BoostSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types)[ConditionBoostSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types.ConditionBoostSpec)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types.ConditionBoostSpec.Types)[BoostControlSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec.Types)[InterpolationType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec.Types.InterpolationType)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
