---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.IamPolicyAnalysisQuery.Types.AccessSelector
title: Google Cloud Asset Inventory v1 API - Class IamPolicyAnalysisQuery.Types.AccessSelector (3.14.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:44:07.363073+00:00
---

# Google Cloud Asset Inventory v1 API - Class IamPolicyAnalysisQuery.Types.AccessSelector (3.14.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.IamPolicyAnalysisQuery.Types.AccessSelector

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Asset Inventory v1 API - Class IamPolicyAnalysisQuery.Types.AccessSelector (3.14.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.14.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.IamPolicyAnalysisQuery.Types.AccessSelector)
  * [ 3.13.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.13.0/Google.Cloud.Asset.V1.IamPolicyAnalysisQuery.Types.AccessSelector)
  * [ 3.12.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.12.0/Google.Cloud.Asset.V1.IamPolicyAnalysisQuery.Types.AccessSelector)
  * [ 3.11.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.11.0/Google.Cloud.Asset.V1.IamPolicyAnalysisQuery.Types.AccessSelector)
  * [ 3.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.10.0/Google.Cloud.Asset.V1.IamPolicyAnalysisQuery.Types.AccessSelector)
  * [ 3.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.9.0/Google.Cloud.Asset.V1.IamPolicyAnalysisQuery.Types.AccessSelector)
  * [ 3.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.8.0/Google.Cloud.Asset.V1.IamPolicyAnalysisQuery.Types.AccessSelector)
  * [ 3.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.7.0/Google.Cloud.Asset.V1.IamPolicyAnalysisQuery.Types.AccessSelector)
  * [ 3.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.6.0/Google.Cloud.Asset.V1.IamPolicyAnalysisQuery.Types.AccessSelector)
  * [ 3.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.5.0/Google.Cloud.Asset.V1.IamPolicyAnalysisQuery.Types.AccessSelector)
  * [ 3.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.4.0/Google.Cloud.Asset.V1.IamPolicyAnalysisQuery.Types.AccessSelector)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.3.0/Google.Cloud.Asset.V1.IamPolicyAnalysisQuery.Types.AccessSelector)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.2.0/Google.Cloud.Asset.V1.IamPolicyAnalysisQuery.Types.AccessSelector)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.1.0/Google.Cloud.Asset.V1.IamPolicyAnalysisQuery.Types.AccessSelector)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.0.0/Google.Cloud.Asset.V1.IamPolicyAnalysisQuery.Types.AccessSelector)
  * [ 2.11.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/2.11.0/Google.Cloud.Asset.V1.IamPolicyAnalysisQuery.Types.AccessSelector)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/2.10.0/Google.Cloud.Asset.V1.IamPolicyAnalysisQuery.Types.AccessSelector)
  * [ 2.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/2.9.0/Google.Cloud.Asset.V1.IamPolicyAnalysisQuery.Types.AccessSelector)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/2.8.0/Google.Cloud.Asset.V1.IamPolicyAnalysisQuery.Types.AccessSelector)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/2.7.0/Google.Cloud.Asset.V1.IamPolicyAnalysisQuery.Types.AccessSelector)


    
    
    public sealed class IamPolicyAnalysisQuery.Types.AccessSelector : IMessage<IamPolicyAnalysisQuery.Types.AccessSelector>, IEquatable<IamPolicyAnalysisQuery.Types.AccessSelector>, IDeepCloneable<IamPolicyAnalysisQuery.Types.AccessSelector>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Asset Inventory v1 API class IamPolicyAnalysisQuery.Types.AccessSelector.

Specifies roles and/or permissions to analyze, to determine both the identities possessing them and the resources they control. If multiple values are specified, results will include roles or permissions matching any of them. The total number of roles and permissions should be equal or less than 10.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > IamPolicyAnalysisQuery.Types.AccessSelector

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[IamPolicyAnalysisQuery](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.IamPolicyAnalysisQuery)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.IamPolicyAnalysisQuery.Types)[AccessSelector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.IamPolicyAnalysisQuery.Types.AccessSelector), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[IamPolicyAnalysisQuery](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.IamPolicyAnalysisQuery)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.IamPolicyAnalysisQuery.Types)[AccessSelector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.IamPolicyAnalysisQuery.Types.AccessSelector), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[IamPolicyAnalysisQuery](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.IamPolicyAnalysisQuery)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.IamPolicyAnalysisQuery.Types)[AccessSelector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.IamPolicyAnalysisQuery.Types.AccessSelector), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Asset.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1)

## Assembly

Google.Cloud.Asset.V1.dll

## Constructors 

### AccessSelector()
    
    
    public AccessSelector()

### AccessSelector(AccessSelector)
    
    
    public AccessSelector(IamPolicyAnalysisQuery.Types.AccessSelector other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[IamPolicyAnalysisQuery](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.IamPolicyAnalysisQuery)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.IamPolicyAnalysisQuery.Types)[AccessSelector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.IamPolicyAnalysisQuery.Types.AccessSelector)`  
  
  
## Properties 

### Permissions
    
    
    public RepeatedField<string> Permissions { get; }

Optional. The permissions to appear in result.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Roles
    
    
    public RepeatedField<string> Roles { get; }

Optional. The roles to appear in result.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
