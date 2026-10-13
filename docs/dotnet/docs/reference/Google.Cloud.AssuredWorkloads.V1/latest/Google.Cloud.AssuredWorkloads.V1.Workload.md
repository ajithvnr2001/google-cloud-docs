---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload
title: Assured Workloads v1 API - Class Workload (2.7.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:52:10.920631+00:00
---

# Assured Workloads v1 API - Class Workload (2.7.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Assured Workloads v1 API - Class Workload (2.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.7.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/2.6.0/Google.Cloud.AssuredWorkloads.V1.Workload)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/2.5.0/Google.Cloud.AssuredWorkloads.V1.Workload)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/2.4.0/Google.Cloud.AssuredWorkloads.V1.Workload)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/2.3.0/Google.Cloud.AssuredWorkloads.V1.Workload)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/2.2.0/Google.Cloud.AssuredWorkloads.V1.Workload)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/2.1.0/Google.Cloud.AssuredWorkloads.V1.Workload)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/2.0.0/Google.Cloud.AssuredWorkloads.V1.Workload)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/1.1.0/Google.Cloud.AssuredWorkloads.V1.Workload)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/1.0.0/Google.Cloud.AssuredWorkloads.V1.Workload)


    
    
    public sealed class Workload : IMessage<Workload>, IEquatable<Workload>, IDeepCloneable<Workload>, IBufferMessage, IMessage

Reference documentation and code samples for the Assured Workloads v1 API class Workload.

A Workload object for managing highly regulated workloads of cloud customers.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Workload

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AssuredWorkloads.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1)

## Assembly

Google.Cloud.AssuredWorkloads.V1.dll

## Constructors 

### Workload()
    
    
    public Workload()

### Workload(Workload)
    
    
    public Workload(Workload other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)`  
  
  
## Properties 

### BillingAccount
    
    
    public string BillingAccount { get; set; }

Optional. The billing account used for the resources which are direct children of workload. This billing account is initially associated with the resources created as part of Workload creation. After the initial creation of these resources, the customer can change the assigned billing account. The resource name has the form `billingAccounts/{billing_account_id}`. For example, `billingAccounts/012345-567890-ABCDEF`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ComplianceRegime
    
    
    public Workload.Types.ComplianceRegime ComplianceRegime { get; set; }

Required. Immutable. Compliance Regime associated with this workload.

**Property Value**  
---  
**Type** | **Description**  
`[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload.Types)[ComplianceRegime](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload.Types.ComplianceRegime)` |   
  
### CompliantButDisallowedServices
    
    
    public RepeatedField<string> CompliantButDisallowedServices { get; }

Output only. Urls for services which are compliant for this Assured Workload, but which are currently disallowed by the ResourceUsageRestriction org policy. Invoke RestrictAllowedResources endpoint to allow your project developers to use these services in their environment."

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. Immutable. The Workload creation timestamp.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### DisplayName
    
    
    public string DisplayName { get; set; }

Required. The user-assigned display name of the Workload. When present it must be between 4 to 30 characters. Allowed characters are: lowercase and uppercase letters, numbers, hyphen, and spaces.

Example: My Workload

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### EnableSovereignControls
    
    
    public bool EnableSovereignControls { get; set; }

Optional. Indicates the sovereignty status of the given workload. Currently meant to be used by Europe/Canada customers.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Etag
    
    
    public string Etag { get; set; }

Optional. ETag of the workload, it is calculated on the basis of the Workload contents. It will be used in Update & Delete operations.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### KajEnrollmentState
    
    
    public Workload.Types.KajEnrollmentState KajEnrollmentState { get; set; }

Output only. Represents the KAJ enrollment state of the given workload.

**Property Value**  
---  
**Type** | **Description**  
`[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload.Types)[KajEnrollmentState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload.Types.KajEnrollmentState)` |   
  
### KmsSettings
    
    
    [Obsolete]
    public Workload.Types.KMSSettings KmsSettings { get; set; }

Input only. Settings used to create a CMEK crypto key. When set, a project with a KMS CMEK key is provisioned. This field is deprecated as of Feb 28, 2022. In order to create a Keyring, callers should specify, ENCRYPTION_KEYS_PROJECT or KEYRING in ResourceSettings.resource_type field.

**Property Value**  
---  
**Type** | **Description**  
`[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload.Types)[KMSSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload.Types.KMSSettings)` |   
  
### Labels
    
    
    public MapField<string, string> Labels { get; }

Optional. Labels applied to the workload.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Optional. The resource name of the workload. Format: organizations/{organization}/locations/{location}/workloads/{workload}

Read-only.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Partner
    
    
    public Workload.Types.Partner Partner { get; set; }

Optional. Compliance Regime associated with this workload.

**Property Value**  
---  
**Type** | **Description**  
`[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload.Types)[Partner](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload.Types.Partner)` |   
  
### ProvisionedResourcesParent
    
    
    public string ProvisionedResourcesParent { get; set; }

Input only. The parent resource for the resources managed by this Assured Workload. May be either empty or a folder resource which is a child of the Workload parent. If not specified all resources are created under the parent organization. Format: folders/{folder_id}

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ResourceSettings
    
    
    public RepeatedField<Workload.Types.ResourceSettings> ResourceSettings { get; }

Input only. Resource properties that are used to customize workload resources. These properties (such as custom project id) will be used to create workload resources if possible. This field is optional.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload.Types)[ResourceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload.Types.ResourceSettings)` |   
  
### Resources
    
    
    public RepeatedField<Workload.Types.ResourceInfo> Resources { get; }

Output only. The resources associated with this workload. These resources will be created when creating the workload. If any of the projects already exist, the workload creation will fail. Always read only.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload.Types)[ResourceInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload.Types.ResourceInfo)` |   
  
### SaaEnrollmentResponse
    
    
    public Workload.Types.SaaEnrollmentResponse SaaEnrollmentResponse { get; set; }

Output only. Represents the SAA enrollment response of the given workload. SAA enrollment response is queried during GetWorkload call. In failure cases, user friendly error message is shown in SAA details page.

**Property Value**  
---  
**Type** | **Description**  
`[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload.Types)[SaaEnrollmentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload.Types.SaaEnrollmentResponse)` |   
  
### WorkloadName
    
    
    public WorkloadName WorkloadName { get; set; }

[WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.WorkloadName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload#Google_Cloud_AssuredWorkloads_V1_Workload_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.WorkloadName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
