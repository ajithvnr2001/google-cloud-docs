---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.Settings.V1Beta1/latest/Google.Cloud.SecurityCenter.Settings.V1Beta1.BatchGetSettingsRequest
title: Google Cloud Security Command Center Settings v1beta1 API - Class BatchGetSettingsRequest (2.0.0-beta05) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:44:35.451355+00:00
---

# Google Cloud Security Command Center Settings v1beta1 API - Class BatchGetSettingsRequest (2.0.0-beta05)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.Settings.V1Beta1/latest/Google.Cloud.SecurityCenter.Settings.V1Beta1.BatchGetSettingsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Security Command Center Settings v1beta1 API - Class BatchGetSettingsRequest (2.0.0-beta05) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta05 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.Settings.V1Beta1/latest/Google.Cloud.SecurityCenter.Settings.V1Beta1.BatchGetSettingsRequest)
  * [ 2.0.0-beta04 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.Settings.V1Beta1/2.0.0-beta04/Google.Cloud.SecurityCenter.Settings.V1Beta1.BatchGetSettingsRequest)
  * [ 1.0.0-beta04 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.Settings.V1Beta1/1.0.0-beta04/Google.Cloud.SecurityCenter.Settings.V1Beta1.BatchGetSettingsRequest)


    
    
    public sealed class BatchGetSettingsRequest : IMessage<BatchGetSettingsRequest>, IEquatable<BatchGetSettingsRequest>, IDeepCloneable<BatchGetSettingsRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Security Command Center Settings v1beta1 API class BatchGetSettingsRequest.

Request message for BatchGetSettings.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BatchGetSettingsRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[BatchGetSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.Settings.V1Beta1/latest/Google.Cloud.SecurityCenter.Settings.V1Beta1.BatchGetSettingsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BatchGetSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.Settings.V1Beta1/latest/Google.Cloud.SecurityCenter.Settings.V1Beta1.BatchGetSettingsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[BatchGetSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.Settings.V1Beta1/latest/Google.Cloud.SecurityCenter.Settings.V1Beta1.BatchGetSettingsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.SecurityCenter.Settings.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.Settings.V1Beta1/latest/Google.Cloud.SecurityCenter.Settings.V1Beta1)

## Assembly

Google.Cloud.SecurityCenter.Settings.V1Beta1.dll

## Constructors 

### BatchGetSettingsRequest()
    
    
    public BatchGetSettingsRequest()

### BatchGetSettingsRequest(BatchGetSettingsRequest)
    
    
    public BatchGetSettingsRequest(BatchGetSettingsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[BatchGetSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.Settings.V1Beta1/latest/Google.Cloud.SecurityCenter.Settings.V1Beta1.BatchGetSettingsRequest)`  
  
  
## Properties 

### Names
    
    
    public RepeatedField<string> Names { get; }

The names of the settings to retrieve. A maximum of 1000 settings can be retrieved in a batch. Formats:

  * `organizations/{organization}/settings`
  * `folders/{folder}/settings`
  * `projects/{project}/settings`
  * `projects/{project}/locations/{location}/clusters/{cluster}/settings`
  * `projects/{project}/regions/{region}/clusters/{cluster}/settings`
  * `projects/{project}/zones/{zone}/clusters/{cluster}/settings`



**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The relative resource name of the organization shared by all of the settings being retrieved. Format:

  * `organizations/{organization}`



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsOrganizationName
    
    
    public OrganizationName ParentAsOrganizationName { get; set; }

[OrganizationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.OrganizationName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.Settings.V1Beta1/latest/Google.Cloud.SecurityCenter.Settings.V1Beta1.BatchGetSettingsRequest#Google_Cloud_SecurityCenter_Settings_V1Beta1_BatchGetSettingsRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[OrganizationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.OrganizationName.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
