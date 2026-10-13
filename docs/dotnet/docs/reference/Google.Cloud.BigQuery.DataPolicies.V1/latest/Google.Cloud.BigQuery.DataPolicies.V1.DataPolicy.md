---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/latest/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicy
title: BigQuery Data Policy v1 API - Class DataPolicy (1.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:21:27.046365+00:00
---

# BigQuery Data Policy v1 API - Class DataPolicy (1.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/latest/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicy

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  BigQuery Data Policy v1 API - Class DataPolicy (1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/latest/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicy)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/1.5.0/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicy)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/1.4.0/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicy)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/1.3.0/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicy)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/1.2.0/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicy)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/1.1.0/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicy)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/1.0.0/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicy)


    
    
    public sealed class DataPolicy : IMessage<DataPolicy>, IEquatable<DataPolicy>, IDeepCloneable<DataPolicy>, IBufferMessage, IMessage

Reference documentation and code samples for the BigQuery Data Policy v1 API class DataPolicy.

Represents the label-policy binding.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DataPolicy

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DataPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/latest/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicy), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DataPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/latest/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicy), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DataPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/latest/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicy), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.BigQuery.DataPolicies.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/latest/Google.Cloud.BigQuery.DataPolicies.V1)

## Assembly

Google.Cloud.BigQuery.DataPolicies.V1.dll

## Constructors 

### DataPolicy()
    
    
    public DataPolicy()

### DataPolicy(DataPolicy)
    
    
    public DataPolicy(DataPolicy other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DataPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/latest/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicy)`  
  
  
## Properties 

### DataMaskingPolicy
    
    
    public DataMaskingPolicy DataMaskingPolicy { get; set; }

The data masking policy that specifies the data masking rule to use.

**Property Value**  
---  
**Type** | **Description**  
`[DataMaskingPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/latest/Google.Cloud.BigQuery.DataPolicies.V1.DataMaskingPolicy)` |   
  
### DataPolicyId
    
    
    public string DataPolicyId { get; set; }

User-assigned (human readable) ID of the data policy that needs to be unique within a project. Used as {data_policy_id} in part of the resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DataPolicyName
    
    
    public DataPolicyName DataPolicyName { get; set; }

[DataPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/latest/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicyName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/latest/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicy#Google_Cloud_BigQuery_DataPolicies_V1_DataPolicy_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[DataPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/latest/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicyName)` |   
  
### DataPolicyType
    
    
    public DataPolicy.Types.DataPolicyType DataPolicyType { get; set; }

Type of data policy.

**Property Value**  
---  
**Type** | **Description**  
`[DataPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/latest/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicy)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/latest/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicy.Types)[DataPolicyType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/latest/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicy.Types.DataPolicyType)` |   
  
### HasPolicyTag
    
    
    public bool HasPolicyTag { get; }

Gets whether the "policy_tag" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### MatchingLabelCase
    
    
    public DataPolicy.MatchingLabelOneofCase MatchingLabelCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[DataPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/latest/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicy)[MatchingLabelOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/latest/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicy.MatchingLabelOneofCase)` |   
  
### Name
    
    
    public string Name { get; set; }

Output only. Resource name of this data policy, in the format of `projects/{project_number}/locations/{location_id}/dataPolicies/{data_policy_id}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PolicyCase
    
    
    public DataPolicy.PolicyOneofCase PolicyCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[DataPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/latest/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicy)[PolicyOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataPolicies.V1/latest/Google.Cloud.BigQuery.DataPolicies.V1.DataPolicy.PolicyOneofCase)` |   
  
### PolicyTag
    
    
    public string PolicyTag { get; set; }

Policy tag resource name, in the format of `projects/{project_number}/locations/{location_id}/taxonomies/{taxonomy_id}/policyTags/{policyTag_id}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
