---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.AccessRulesOptions
title: Google Cloud Managed Lustre v1 API - Class AccessRulesOptions (1.1.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:58:20.729336+00:00
---

# Google Cloud Managed Lustre v1 API - Class AccessRulesOptions (1.1.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.AccessRulesOptions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Managed Lustre v1 API - Class AccessRulesOptions (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0 
    
    
    public sealed class AccessRulesOptions : IMessage<AccessRulesOptions>, IEquatable<AccessRulesOptions>, IDeepCloneable<AccessRulesOptions>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Managed Lustre v1 API class AccessRulesOptions.

IP-based access rules for the Managed Lustre instance. These options define the root user squash configuration.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AccessRulesOptions

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AccessRulesOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.AccessRulesOptions), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AccessRulesOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.AccessRulesOptions), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AccessRulesOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.AccessRulesOptions), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Lustre.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1)

## Assembly

Google.Cloud.Lustre.V1.dll

## Constructors 

### AccessRulesOptions()
    
    
    public AccessRulesOptions()

### AccessRulesOptions(AccessRulesOptions)
    
    
    public AccessRulesOptions(AccessRulesOptions other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AccessRulesOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.AccessRulesOptions)`  
  
  
## Properties 

### AccessRules
    
    
    public RepeatedField<AccessRulesOptions.Types.AccessRule> AccessRules { get; }

Optional. The access rules for the instance.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[AccessRulesOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.AccessRulesOptions)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.AccessRulesOptions.Types)[AccessRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.AccessRulesOptions.Types.AccessRule)` |   
  
### DefaultSquashGid
    
    
    public int DefaultSquashGid { get; set; }

Optional. The user squash GID for the default access rule. This user squash GID applies to all root users connecting from clients that are not matched by any of the access rules. If not set, the default is 0 (no GID squash).

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### DefaultSquashMode
    
    
    public AccessRulesOptions.Types.SquashMode DefaultSquashMode { get; set; }

Required. The squash mode for the default access rule.

**Property Value**  
---  
**Type** | **Description**  
`[AccessRulesOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.AccessRulesOptions)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.AccessRulesOptions.Types)[SquashMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.AccessRulesOptions.Types.SquashMode)` |   
  
### DefaultSquashUid
    
    
    public int DefaultSquashUid { get; set; }

Optional. The user squash UID for the default access rule. This user squash UID applies to all root users connecting from clients that are not matched by any of the access rules. If not set, the default is 0 (no UID squash).

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
