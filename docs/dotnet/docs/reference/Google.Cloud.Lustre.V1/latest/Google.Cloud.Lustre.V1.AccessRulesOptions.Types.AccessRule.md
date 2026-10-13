---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.AccessRulesOptions.Types.AccessRule
title: Google Cloud Managed Lustre v1 API - Class AccessRulesOptions.Types.AccessRule (1.1.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:18:09.357521+00:00
---

# Google Cloud Managed Lustre v1 API - Class AccessRulesOptions.Types.AccessRule (1.1.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.AccessRulesOptions.Types.AccessRule

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Managed Lustre v1 API - Class AccessRulesOptions.Types.AccessRule (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0 
    
    
    public sealed class AccessRulesOptions.Types.AccessRule : IMessage<AccessRulesOptions.Types.AccessRule>, IEquatable<AccessRulesOptions.Types.AccessRule>, IDeepCloneable<AccessRulesOptions.Types.AccessRule>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Managed Lustre v1 API class AccessRulesOptions.Types.AccessRule.

A single policy group with IP-based access rules for the Managed Lustre instance.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AccessRulesOptions.Types.AccessRule

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AccessRulesOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.AccessRulesOptions)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.AccessRulesOptions.Types)[AccessRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.AccessRulesOptions.Types.AccessRule), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AccessRulesOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.AccessRulesOptions)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.AccessRulesOptions.Types)[AccessRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.AccessRulesOptions.Types.AccessRule), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AccessRulesOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.AccessRulesOptions)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.AccessRulesOptions.Types)[AccessRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.AccessRulesOptions.Types.AccessRule), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Lustre.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1)

## Assembly

Google.Cloud.Lustre.V1.dll

## Constructors 

### AccessRule()
    
    
    public AccessRule()

### AccessRule(AccessRule)
    
    
    public AccessRule(AccessRulesOptions.Types.AccessRule other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AccessRulesOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.AccessRulesOptions)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.AccessRulesOptions.Types)[AccessRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.AccessRulesOptions.Types.AccessRule)`  
  
  
## Properties 

### IpAddressRanges
    
    
    public RepeatedField<string> IpAddressRanges { get; }

Required. The IP address ranges to which to apply this access rule. Accepts non-overlapping CIDR ranges (e.g., `192.168.1.0/24`) and IP addresses (e.g., `192.168.1.0`).

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. The name of the access rule policy group. Must be 16 characters or less and include only alphanumeric characters or '_'.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SquashMode
    
    
    public AccessRulesOptions.Types.SquashMode SquashMode { get; set; }

Required. Squash mode for the access rule.

**Property Value**  
---  
**Type** | **Description**  
`[AccessRulesOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.AccessRulesOptions)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.AccessRulesOptions.Types)[SquashMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.AccessRulesOptions.Types.SquashMode)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
