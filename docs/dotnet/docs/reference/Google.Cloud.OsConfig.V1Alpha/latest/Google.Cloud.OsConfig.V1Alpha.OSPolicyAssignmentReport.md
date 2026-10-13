---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReport
title: Google Cloud OS Config v1alpha API - Class OSPolicyAssignmentReport (2.0.0-alpha07) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:35:56.459138+00:00
---

# Google Cloud OS Config v1alpha API - Class OSPolicyAssignmentReport (2.0.0-alpha07)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReport

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud OS Config v1alpha API - Class OSPolicyAssignmentReport (2.0.0-alpha07) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-alpha07 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReport)
  * [ 2.0.0-alpha06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/2.0.0-alpha06/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReport)
  * [ 1.0.0-alpha04 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/1.0.0-alpha04/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReport)


    
    
    public sealed class OSPolicyAssignmentReport : IMessage<OSPolicyAssignmentReport>, IEquatable<OSPolicyAssignmentReport>, IDeepCloneable<OSPolicyAssignmentReport>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud OS Config v1alpha API class OSPolicyAssignmentReport.

A report of the OS policy assignment status for a given instance.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > OSPolicyAssignmentReport

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[OSPolicyAssignmentReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReport), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[OSPolicyAssignmentReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReport), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[OSPolicyAssignmentReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReport), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.OsConfig.V1Alpha](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha)

## Assembly

Google.Cloud.OsConfig.V1Alpha.dll

## Constructors 

### OSPolicyAssignmentReport()
    
    
    public OSPolicyAssignmentReport()

### OSPolicyAssignmentReport(OSPolicyAssignmentReport)
    
    
    public OSPolicyAssignmentReport(OSPolicyAssignmentReport other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[OSPolicyAssignmentReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReport)`  
  
  
## Properties 

### Instance
    
    
    public string Instance { get; set; }

The Compute Engine VM instance name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### LastRunId
    
    
    public string LastRunId { get; set; }

Unique identifier of the last attempted run to apply the OS policies associated with this assignment on the VM.

This ID is logged by the OS Config agent while applying the OS policies associated with this assignment on the VM. NOTE: If the service is unable to successfully connect to the agent for this run, then this id will not be available in the agent logs.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

The `OSPolicyAssignmentReport` API resource name.

Format: `projects/{project_number}/locations/{location}/instances/{instance_id}/osPolicyAssignments/{os_policy_assignment_id}/report`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OSPolicyAssignmentReportName
    
    
    public OSPolicyAssignmentReportName OSPolicyAssignmentReportName { get; set; }

[OSPolicyAssignmentReportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReportName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReport#Google_Cloud_OsConfig_V1Alpha_OSPolicyAssignmentReport_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[OSPolicyAssignmentReportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReportName)` |   
  
### OsPolicyAssignment
    
    
    public string OsPolicyAssignment { get; set; }

Reference to the `OSPolicyAssignment` API resource that the `OSPolicy` belongs to.

Format: `projects/{project_number}/locations/{location}/osPolicyAssignments/{os_policy_assignment_id@revision_id}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OsPolicyAssignmentAsOSPolicyAssignmentName
    
    
    public OSPolicyAssignmentName OsPolicyAssignmentAsOSPolicyAssignmentName { get; set; }

[OSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentName)-typed view over the [OsPolicyAssignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReport#Google_Cloud_OsConfig_V1Alpha_OSPolicyAssignmentReport_OsPolicyAssignment) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[OSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentName)` |   
  
### OsPolicyCompliances
    
    
    public RepeatedField<OSPolicyAssignmentReport.Types.OSPolicyCompliance> OsPolicyCompliances { get; }

Compliance data for each `OSPolicy` that is applied to the VM.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[OSPolicyAssignmentReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReport)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReport.Types)[OSPolicyCompliance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.OSPolicyAssignmentReport.Types.OSPolicyCompliance)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Timestamp for when the report was last generated.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
