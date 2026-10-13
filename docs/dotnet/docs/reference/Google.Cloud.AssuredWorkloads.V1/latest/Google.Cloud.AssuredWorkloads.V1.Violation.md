---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Violation
title: Assured Workloads v1 API - Class Violation (2.7.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:28:52.692888+00:00
---

# Assured Workloads v1 API - Class Violation (2.7.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Violation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Assured Workloads v1 API - Class Violation (2.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.7.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Violation)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/2.6.0/Google.Cloud.AssuredWorkloads.V1.Violation)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/2.5.0/Google.Cloud.AssuredWorkloads.V1.Violation)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/2.4.0/Google.Cloud.AssuredWorkloads.V1.Violation)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/2.3.0/Google.Cloud.AssuredWorkloads.V1.Violation)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/2.2.0/Google.Cloud.AssuredWorkloads.V1.Violation)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/2.1.0/Google.Cloud.AssuredWorkloads.V1.Violation)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/2.0.0/Google.Cloud.AssuredWorkloads.V1.Violation)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/1.1.0/Google.Cloud.AssuredWorkloads.V1.Violation)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/1.0.0/Google.Cloud.AssuredWorkloads.V1.Violation)


    
    
    public sealed class Violation : IMessage<Violation>, IEquatable<Violation>, IDeepCloneable<Violation>, IBufferMessage, IMessage

Reference documentation and code samples for the Assured Workloads v1 API class Violation.

Workload monitoring Violation.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Violation

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Violation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Violation), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Violation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Violation), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Violation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Violation), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AssuredWorkloads.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1)

## Assembly

Google.Cloud.AssuredWorkloads.V1.dll

## Constructors 

### Violation()
    
    
    public Violation()

### Violation(Violation)
    
    
    public Violation(Violation other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Violation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Violation)`  
  
  
## Properties 

### Acknowledged
    
    
    public bool Acknowledged { get; set; }

Output only. A boolean that indicates if the violation is acknowledged

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### AcknowledgementTime
    
    
    public Timestamp AcknowledgementTime { get; set; }

Optional. Timestamp when this violation was acknowledged last. This will be absent when acknowledged field is marked as false.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### AuditLogLink
    
    
    public string AuditLogLink { get; set; }

Output only. Immutable. Audit Log Link for violated resource Format: https://console.cloud.google.com/logs/query;query={logName}{protoPayload.resourceName}{timeRange}{folder}

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### BeginTime
    
    
    public Timestamp BeginTime { get; set; }

Output only. Time of the event which triggered the Violation.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Category
    
    
    public string Category { get; set; }

Output only. Category under which this violation is mapped. e.g. Location, Service Usage, Access, Encryption, etc.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Description
    
    
    public string Description { get; set; }

Output only. Description for the Violation. e.g. OrgPolicy gcp.resourceLocations has non compliant value.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ExceptionAuditLogLink
    
    
    public string ExceptionAuditLogLink { get; set; }

Output only. Immutable. Audit Log link to find business justification provided for violation exception. Format: https://console.cloud.google.com/logs/query;query={logName}{protoPayload.resourceName}{protoPayload.methodName}{timeRange}{organization}

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Output only. Immutable. Name of the Violation. Format: organizations/{organization}/locations/{location}/workloads/{workload_id}/violations/{violations_id}

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### NonCompliantOrgPolicy
    
    
    public string NonCompliantOrgPolicy { get; set; }

Output only. Immutable. Name of the OrgPolicy which was modified with non-compliant change and resulted this violation. Format: projects/{project_number}/policies/{constraint_name} folders/{folder_id}/policies/{constraint_name} organizations/{organization_id}/policies/{constraint_name}

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OrgPolicyConstraint
    
    
    public string OrgPolicyConstraint { get; set; }

Output only. Immutable. The org-policy-constraint that was incorrectly changed, which resulted in this violation.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Remediation
    
    
    public Violation.Types.Remediation Remediation { get; set; }

Output only. Compliance violation remediation

**Property Value**  
---  
**Type** | **Description**  
`[Violation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Violation)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Violation.Types)[Remediation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Violation.Types.Remediation)` |   
  
### ResolveTime
    
    
    public Timestamp ResolveTime { get; set; }

Output only. Time of the event which fixed the Violation. If the violation is ACTIVE this will be empty.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### State
    
    
    public Violation.Types.State State { get; set; }

Output only. State of the violation

**Property Value**  
---  
**Type** | **Description**  
`[Violation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Violation)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Violation.Types)[State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Violation.Types.State)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. The last time when the Violation record was updated.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### ViolationName
    
    
    public ViolationName ViolationName { get; set; }

[ViolationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Violation#Google_Cloud_AssuredWorkloads_V1_Violation_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ViolationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
