---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.UpdateSecurityHealthAnalyticsCustomModuleRequest
title: Security Center Management v1 API - Class UpdateSecurityHealthAnalyticsCustomModuleRequest (1.3.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:29:33.095057+00:00
---

# Security Center Management v1 API - Class UpdateSecurityHealthAnalyticsCustomModuleRequest (1.3.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.UpdateSecurityHealthAnalyticsCustomModuleRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Security Center Management v1 API - Class UpdateSecurityHealthAnalyticsCustomModuleRequest (1.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.3.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.UpdateSecurityHealthAnalyticsCustomModuleRequest)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/1.2.0/Google.Cloud.SecurityCenterManagement.V1.UpdateSecurityHealthAnalyticsCustomModuleRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/1.1.0/Google.Cloud.SecurityCenterManagement.V1.UpdateSecurityHealthAnalyticsCustomModuleRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/1.0.0/Google.Cloud.SecurityCenterManagement.V1.UpdateSecurityHealthAnalyticsCustomModuleRequest)


    
    
    public sealed class UpdateSecurityHealthAnalyticsCustomModuleRequest : IMessage<UpdateSecurityHealthAnalyticsCustomModuleRequest>, IEquatable<UpdateSecurityHealthAnalyticsCustomModuleRequest>, IDeepCloneable<UpdateSecurityHealthAnalyticsCustomModuleRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Security Center Management v1 API class UpdateSecurityHealthAnalyticsCustomModuleRequest.

Request message for [SecurityCenterManagement.UpdateSecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.UpdateSecurityHealthAnalyticsCustomModule].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UpdateSecurityHealthAnalyticsCustomModuleRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[UpdateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.UpdateSecurityHealthAnalyticsCustomModuleRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[UpdateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.UpdateSecurityHealthAnalyticsCustomModuleRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[UpdateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.UpdateSecurityHealthAnalyticsCustomModuleRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.SecurityCenterManagement.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1)

## Assembly

Google.Cloud.SecurityCenterManagement.V1.dll

## Constructors 

### UpdateSecurityHealthAnalyticsCustomModuleRequest()
    
    
    public UpdateSecurityHealthAnalyticsCustomModuleRequest()

### UpdateSecurityHealthAnalyticsCustomModuleRequest(UpdateSecurityHealthAnalyticsCustomModuleRequest)
    
    
    public UpdateSecurityHealthAnalyticsCustomModuleRequest(UpdateSecurityHealthAnalyticsCustomModuleRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[UpdateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.UpdateSecurityHealthAnalyticsCustomModuleRequest)`  
  
  
## Properties 

### SecurityHealthAnalyticsCustomModule
    
    
    public SecurityHealthAnalyticsCustomModule SecurityHealthAnalyticsCustomModule { get; set; }

Required. The resource being updated.

**Property Value**  
---  
**Type** | **Description**  
`[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SecurityHealthAnalyticsCustomModule)` |   
  
### UpdateMask
    
    
    public FieldMask UpdateMask { get; set; }

Required. The fields to update. The following values are valid:

  * `custom_config`
  * `enablement_state`



If you omit this field or set it to the wildcard value `*`, then all eligible fields are updated.

**Property Value**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)` |   
  
### ValidateOnly
    
    
    public bool ValidateOnly { get; set; }

Optional. When set to `true`, the request will be validated (including IAM checks), but no module will be updated. An `OK` response indicates that the request is valid, while an error response indicates that the request is invalid.

If the request is valid, a subsequent request to update the module could still fail for one of the following reasons:

  * The state of your cloud resources changed; for example, you lost a required IAM permission
  * An error occurred during creation of the module



Defaults to `false`.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
