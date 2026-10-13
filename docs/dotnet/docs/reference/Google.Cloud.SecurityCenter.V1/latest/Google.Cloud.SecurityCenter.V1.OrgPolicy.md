---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.OrgPolicy
title: Google Cloud Security Command Center v1 API - Class OrgPolicy (3.28.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:52:26.239765+00:00
---

# Google Cloud Security Command Center v1 API - Class OrgPolicy (3.28.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.OrgPolicy

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Security Command Center v1 API - Class OrgPolicy (3.28.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.28.0 (latest)  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class OrgPolicy : IMessage<OrgPolicy>, IEquatable<OrgPolicy>, IDeepCloneable<OrgPolicy>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Security Command Center v1 API class OrgPolicy.

Contains information about the org policies associated with the finding.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > OrgPolicy

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[OrgPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.OrgPolicy), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[OrgPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.OrgPolicy), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[OrgPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.OrgPolicy), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.SecurityCenter.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1)

## Assembly

Google.Cloud.SecurityCenter.V1.dll

## Constructors 

### OrgPolicy()
    
    
    public OrgPolicy()

### OrgPolicy(OrgPolicy)
    
    
    public OrgPolicy(OrgPolicy other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[OrgPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.OrgPolicy)`  
  
  
## Properties 

### Name
    
    
    public string Name { get; set; }

The resource name of the org policy. Example: "organizations/{organization_id}/policies/{constraint_name}"

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PolicyName
    
    
    public PolicyName PolicyName { get; set; }

[PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.OrgPolicy#Google_Cloud_SecurityCenter_V1_OrgPolicy_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
