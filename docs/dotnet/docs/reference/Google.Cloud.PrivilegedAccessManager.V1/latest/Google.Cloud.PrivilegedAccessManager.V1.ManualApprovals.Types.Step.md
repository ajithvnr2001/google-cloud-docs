---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.ManualApprovals.Types.Step
title: Privileged Access Manager v1 API - Class ManualApprovals.Types.Step (1.2.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:21:09.741809+00:00
---

# Privileged Access Manager v1 API - Class ManualApprovals.Types.Step (1.2.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.ManualApprovals.Types.Step

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Privileged Access Manager v1 API - Class ManualApprovals.Types.Step (1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.2.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.ManualApprovals.Types.Step)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/1.1.0/Google.Cloud.PrivilegedAccessManager.V1.ManualApprovals.Types.Step)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/1.0.0/Google.Cloud.PrivilegedAccessManager.V1.ManualApprovals.Types.Step)


    
    
    public sealed class ManualApprovals.Types.Step : IMessage<ManualApprovals.Types.Step>, IEquatable<ManualApprovals.Types.Step>, IDeepCloneable<ManualApprovals.Types.Step>, IBufferMessage, IMessage

Reference documentation and code samples for the Privileged Access Manager v1 API class ManualApprovals.Types.Step.

Step represents a logical step in a manual approval workflow.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ManualApprovals.Types.Step

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ManualApprovals](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.ManualApprovals)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.ManualApprovals.Types)[Step](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.ManualApprovals.Types.Step), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ManualApprovals](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.ManualApprovals)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.ManualApprovals.Types)[Step](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.ManualApprovals.Types.Step), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ManualApprovals](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.ManualApprovals)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.ManualApprovals.Types)[Step](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.ManualApprovals.Types.Step), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.PrivilegedAccessManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1)

## Assembly

Google.Cloud.PrivilegedAccessManager.V1.dll

## Constructors 

### Step()
    
    
    public Step()

### Step(Step)
    
    
    public Step(ManualApprovals.Types.Step other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ManualApprovals](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.ManualApprovals)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.ManualApprovals.Types)[Step](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.ManualApprovals.Types.Step)`  
  
  
## Properties 

### ApprovalsNeeded
    
    
    public int ApprovalsNeeded { get; set; }

Required. How many users from the above list need to approve. If there aren't enough distinct users in the list, then the workflow indefinitely blocks. Should always be greater than 0. 1 is the only supported value.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### ApproverEmailRecipients
    
    
    public RepeatedField<string> ApproverEmailRecipients { get; }

Optional. Additional email addresses to be notified when a grant is pending approval.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Approvers
    
    
    public RepeatedField<AccessControlEntry> Approvers { get; }

Optional. The potential set of approvers in this step. This list must contain at most one entry.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[AccessControlEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.AccessControlEntry)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
