---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SimulatedFinding
title: Security Center Management v1 API - Class SimulatedFinding (1.3.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:19:11.991833+00:00
---

# Security Center Management v1 API - Class SimulatedFinding (1.3.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SimulatedFinding

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Security Center Management v1 API - Class SimulatedFinding (1.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.3.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SimulatedFinding)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/1.2.0/Google.Cloud.SecurityCenterManagement.V1.SimulatedFinding)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/1.1.0/Google.Cloud.SecurityCenterManagement.V1.SimulatedFinding)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/1.0.0/Google.Cloud.SecurityCenterManagement.V1.SimulatedFinding)


    
    
    public sealed class SimulatedFinding : IMessage<SimulatedFinding>, IEquatable<SimulatedFinding>, IDeepCloneable<SimulatedFinding>, IBufferMessage, IMessage

Reference documentation and code samples for the Security Center Management v1 API class SimulatedFinding.

The minimum set of fields needed to represent a simulated finding from a Security Health Analytics custom module.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SimulatedFinding

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[SimulatedFinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SimulatedFinding), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SimulatedFinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SimulatedFinding), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[SimulatedFinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SimulatedFinding), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.SecurityCenterManagement.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1)

## Assembly

Google.Cloud.SecurityCenterManagement.V1.dll

## Constructors 

### SimulatedFinding()
    
    
    public SimulatedFinding()

### SimulatedFinding(SimulatedFinding)
    
    
    public SimulatedFinding(SimulatedFinding other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SimulatedFinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SimulatedFinding)`  
  
  
## Properties 

### Category
    
    
    public string Category { get; set; }

The additional taxonomy group within findings from a given source. For example, `XSS_FLASH_INJECTION`. This field is immutable after creation time.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### EventTime
    
    
    public Timestamp EventTime { get; set; }

The time the finding was first detected. If an existing finding is updated, then this is the time the update occurred. If the finding is later resolved, then this time reflects when the finding was resolved.

For example, if the finding represents an open firewall, this property captures the time the detector believes the firewall became open. The accuracy is determined by the detector.

The event time must not be set to a value greater than the current timestamp.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### FindingClass
    
    
    public SimulatedFinding.Types.FindingClass FindingClass { get; set; }

The class of the finding.

**Property Value**  
---  
**Type** | **Description**  
`[SimulatedFinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SimulatedFinding)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SimulatedFinding.Types)[FindingClass](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SimulatedFinding.Types.FindingClass)` |   
  
### FindingName
    
    
    public FindingName FindingName { get; set; }

[FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.FindingName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SimulatedFinding#Google_Cloud_SecurityCenterManagement_V1_SimulatedFinding_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.FindingName)` |   
  
### Name
    
    
    public string Name { get; set; }

Identifier. The [relative resource name](https://google.aip.dev/122) of the finding, in one of the following formats:

  * `organizations/{organization_id}/sources/{source_id}/findings/{finding_id}`
  * `folders/{folder_id}/sources/{source_id}/findings/{finding_id}`
  * `projects/{project_id}/sources/{source_id}/findings/{finding_id}`



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

The [relative resource name](https://google.aip.dev/122) of the source the finding belongs to. For example, `organizations/{organization_id}/sources/{source_id}`. This field is immutable after creation time.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ResourceName
    
    
    public string ResourceName { get; set; }

For findings on Google Cloud resources, the [full resource name](https://google.aip.dev/122#full-resource-names) of the Google Cloud resource this finding is for. When the finding is for a non-Google Cloud resource, the value can be a customer or partner defined string. This field is immutable after creation time.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Severity
    
    
    public SimulatedFinding.Types.Severity Severity { get; set; }

The severity of the finding. This field is managed by the source that writes the finding.

**Property Value**  
---  
**Type** | **Description**  
`[SimulatedFinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SimulatedFinding)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SimulatedFinding.Types)[Severity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SimulatedFinding.Types.Severity)` |   
  
### SourceProperties
    
    
    public MapField<string, Value> SourceProperties { get; }

Source-specific properties. These properties are managed by the source that writes the finding. The key names must be between 1 and 255 characters; they must start with a letter and contain alphanumeric characters or underscores only.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[Value](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Value.html)` |   
  
### State
    
    
    public SimulatedFinding.Types.State State { get; set; }

Output only. The state of the finding.

**Property Value**  
---  
**Type** | **Description**  
`[SimulatedFinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SimulatedFinding)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SimulatedFinding.Types)[State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SimulatedFinding.Types.State)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
