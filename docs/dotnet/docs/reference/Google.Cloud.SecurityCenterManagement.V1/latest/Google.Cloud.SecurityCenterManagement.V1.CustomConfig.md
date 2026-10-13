---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.CustomConfig
title: Security Center Management v1 API - Class CustomConfig (1.3.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:21:46.552032+00:00
---

# Security Center Management v1 API - Class CustomConfig (1.3.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.CustomConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Security Center Management v1 API - Class CustomConfig (1.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.3.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.CustomConfig)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/1.2.0/Google.Cloud.SecurityCenterManagement.V1.CustomConfig)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/1.1.0/Google.Cloud.SecurityCenterManagement.V1.CustomConfig)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/1.0.0/Google.Cloud.SecurityCenterManagement.V1.CustomConfig)


    
    
    public sealed class CustomConfig : IMessage<CustomConfig>, IEquatable<CustomConfig>, IDeepCloneable<CustomConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Security Center Management v1 API class CustomConfig.

Defines the properties in a custom module configuration for Security Health Analytics. Use the custom module configuration to create custom detectors that generate custom findings for resources that you specify.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CustomConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CustomConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.CustomConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CustomConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.CustomConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CustomConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.CustomConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.SecurityCenterManagement.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1)

## Assembly

Google.Cloud.SecurityCenterManagement.V1.dll

## Constructors 

### CustomConfig()
    
    
    public CustomConfig()

### CustomConfig(CustomConfig)
    
    
    public CustomConfig(CustomConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CustomConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.CustomConfig)`  
  
  
## Properties 

### CustomOutput
    
    
    public CustomConfig.Types.CustomOutputSpec CustomOutput { get; set; }

Optional. Custom output properties.

**Property Value**  
---  
**Type** | **Description**  
`[CustomConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.CustomConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.CustomConfig.Types)[CustomOutputSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.CustomConfig.Types.CustomOutputSpec)` |   
  
### Description
    
    
    public string Description { get; set; }

Optional. Text that describes the vulnerability or misconfiguration that the custom module detects. This explanation is returned with each finding instance to help investigators understand the detected issue. The text must be enclosed in quotation marks.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Predicate
    
    
    public Expr Predicate { get; set; }

Optional. The Common Expression Language (CEL) expression to evaluate to produce findings. When the expression evaluates to `true` against a resource, a finding is generated.

**Property Value**  
---  
**Type** | **Description**  
`[Expr](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Expr.html)` |   
  
### Recommendation
    
    
    public string Recommendation { get; set; }

Optional. An explanation of the recommended steps that security teams can take to resolve the detected issue. This explanation is returned with each finding generated by this module.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ResourceSelector
    
    
    public CustomConfig.Types.ResourceSelector ResourceSelector { get; set; }

Optional. The Cloud Asset Inventory resource types that the custom module operates on. For information about resource types, see [Supported asset types](https://cloud.google.com/asset-inventory/docs/supported-asset-types). Each custom module can specify up to 5 resource types.

**Property Value**  
---  
**Type** | **Description**  
`[CustomConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.CustomConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.CustomConfig.Types)[ResourceSelector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.CustomConfig.Types.ResourceSelector)` |   
  
### Severity
    
    
    public CustomConfig.Types.Severity Severity { get; set; }

Optional. The severity to assign to findings generated by the module.

**Property Value**  
---  
**Type** | **Description**  
`[CustomConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.CustomConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.CustomConfig.Types)[Severity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.CustomConfig.Types.Severity)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
