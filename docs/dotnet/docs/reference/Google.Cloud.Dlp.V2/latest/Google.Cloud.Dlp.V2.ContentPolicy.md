---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy
title: Google Cloud Data Loss Prevention v2 API - Class ContentPolicy (4.27.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:46:46.276437+00:00
---

# Google Cloud Data Loss Prevention v2 API - Class ContentPolicy (4.27.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Data Loss Prevention v2 API - Class ContentPolicy (4.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.27.0 (latest)  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.5.0  3.4.0  3.3.0  3.2.0  2.16.0  2.15.0 
    
    
    public sealed class ContentPolicy : IMessage<ContentPolicy>, IEquatable<ContentPolicy>, IDeepCloneable<ContentPolicy>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Data Loss Prevention v2 API class ContentPolicy.

A policy to apply to content based on its inspection findings.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ContentPolicy

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ContentPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ContentPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ContentPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2)

## Assembly

Google.Cloud.Dlp.V2.dll

## Constructors 

### ContentPolicy()
    
    
    public ContentPolicy()

### ContentPolicy(ContentPolicy)
    
    
    public ContentPolicy(ContentPolicy other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ContentPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy)`  
  
  
## Properties 

### ContentPolicyName
    
    
    public ContentPolicyName ContentPolicyName { get; set; }

[ContentPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicyName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy#Google_Cloud_Dlp_V2_ContentPolicy_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ContentPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicyName)` |   
  
### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. The creation timestamp of a contentPolicy; output-only field.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### DefaultAction
    
    
    public ContentPolicy.Types.PolicyAction DefaultAction { get; set; }

Action to take if the content is scanned and no rules match. Defaults to returning an ALLOW verdict if not set.

**Property Value**  
---  
**Type** | **Description**  
`[ContentPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy.Types)[PolicyAction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy.Types.PolicyAction)` |   
  
### DisplayName
    
    
    public string DisplayName { get; set; }

Optional. Display name (max 63 chars)

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Errors
    
    
    public RepeatedField<Error> Errors { get; }

Output only. A stream of errors encountered when the policy was applied. Output only field. Will return the last 100 errors. Whenever the policy is modified this list will be cleared.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Error](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Error)` |   
  
### FailedToScanSupportedFileType
    
    
    public ContentPolicy.Types.PolicyAction FailedToScanSupportedFileType { get; set; }

Optional. Action to take if the content is a supported file type and size but fails to be scanned, for example because the file is encrypted or corrupted.

**Property Value**  
---  
**Type** | **Description**  
`[ContentPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy.Types)[PolicyAction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy.Types.PolicyAction)` |   
  
### InputTooLarge
    
    
    public ContentPolicy.Types.PolicyAction InputTooLarge { get; set; }

Optional. Action to take if the content is a supported file type but is too large to be scanned.

**Property Value**  
---  
**Type** | **Description**  
`[ContentPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy.Types)[PolicyAction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy.Types.PolicyAction)` |   
  
### InspectConfig
    
    
    public InspectConfig InspectConfig { get; set; }

Optional. InspectConfig to use to produce findings.

**Property Value**  
---  
**Type** | **Description**  
`[InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig)` |   
  
### LoggingConfigs
    
    
    public RepeatedField<ContentPolicy.Types.LoggingConfig> LoggingConfigs { get; }

Optional. Log the actions taken by the content policy to external systems.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[ContentPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy.Types)[LoggingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy.Types.LoggingConfig)` |   
  
### Name
    
    
    public string Name { get; set; }

Output only. Resource name of the policy.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Rules
    
    
    public RepeatedField<ContentPolicy.Types.PolicyRule> Rules { get; }

Required. Policies to apply, based on the findings returned by inspection. The first rule to match applies.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[ContentPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy.Types)[PolicyRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy.Types.PolicyRule)` |   
  
### UnsupportedFileType
    
    
    public ContentPolicy.Types.PolicyAction UnsupportedFileType { get; set; }

Optional. Action to take if the content is an unsupported file type.

**Property Value**  
---  
**Type** | **Description**  
`[ContentPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy.Types)[PolicyAction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentPolicy.Types.PolicyAction)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. The last update timestamp of a contentPolicy; output-only field.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
