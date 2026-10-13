---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta.DimensionsInfo
title: Cloud Quotas v1beta API - Class DimensionsInfo (1.0.0-beta04) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:14:12.421200+00:00
---

# Cloud Quotas v1beta API - Class DimensionsInfo (1.0.0-beta04)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta.DimensionsInfo

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Quotas v1beta API - Class DimensionsInfo (1.0.0-beta04) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-beta04 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta.DimensionsInfo)
  * [ 1.0.0-beta03 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/1.0.0-beta03/Google.Cloud.CloudQuotas.V1Beta.DimensionsInfo)


    
    
    public sealed class DimensionsInfo : IMessage<DimensionsInfo>, IEquatable<DimensionsInfo>, IDeepCloneable<DimensionsInfo>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Quotas v1beta API class DimensionsInfo.

The detailed quota information such as effective quota value for a combination of dimensions.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DimensionsInfo

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DimensionsInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta.DimensionsInfo), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DimensionsInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta.DimensionsInfo), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DimensionsInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta.DimensionsInfo), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.CloudQuotas.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta)

## Assembly

Google.Cloud.CloudQuotas.V1Beta.dll

## Constructors 

### DimensionsInfo()
    
    
    public DimensionsInfo()

### DimensionsInfo(DimensionsInfo)
    
    
    public DimensionsInfo(DimensionsInfo other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DimensionsInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta.DimensionsInfo)`  
  
  
## Properties 

### ApplicableLocations
    
    
    public RepeatedField<string> ApplicableLocations { get; }

The applicable regions or zones of this dimension. The field is set to ['global'] for quotas that are not per region or per zone. Otherwise, it will be set to the list of locations this dimension info is applicable to.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Details
    
    
    public QuotaDetails Details { get; set; }

Quota details for the specified dimensions.

**Property Value**  
---  
**Type** | **Description**  
`[QuotaDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta.QuotaDetails)` |   
  
### Dimensions
    
    
    public MapField<string, string> Dimensions { get; }

The map of dimensions in key-value pairs. The key of a map entry is "region", "zone", or the name of a service-specific dimension, and the value of a map entry is the value of the dimension. If a dimension does not appear in the map of dimensions, the dimensions info applies to all the dimension values except for those that have another DimensionInfo instance configured for the specific value. For example: `{"provider" : "Example Organization"}` where `provider` is a service-specific quota dimension and `Example Organization` is the provider name.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
